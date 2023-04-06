# Comparing `tmp/casagui-0.2.8.tar.gz` & `tmp/casagui-0.2.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "casagui-0.2.8.tar", last modified: Thu Aug 25 15:52:13 2022, max compression
+gzip compressed data, was "casagui-0.2.9.tar", last modified: Thu Aug 25 16:33:08 2022, max compression
```

## Comparing `casagui-0.2.8.tar` & `casagui-0.2.9.tar`

### file list

```diff
@@ -1,63 +1,63 @@
--rw-r--r--   0 runner    (1001) docker     (121)    26526 2022-08-25 15:51:51.537205 casagui-0.2.8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)    26371 2022-08-25 15:51:51.565205 casagui-0.2.8/casagui/LICENSE.rst
--rw-r--r--   0 runner    (1001) docker     (121)      604 2022-08-25 15:51:51.565205 casagui-0.2.8/casagui/README.rst
--rw-r--r--   0 runner    (1001) docker     (121)     1755 2022-08-25 15:51:51.565205 casagui-0.2.8/casagui/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1542 2022-08-25 15:51:51.565205 casagui-0.2.8/casagui/apps/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    53786 2022-08-25 15:51:51.565205 casagui-0.2.8/casagui/apps/_interactiveclean.py
--rw-r--r--   0 runner    (1001) docker     (121)     5937 2022-08-25 15:51:51.565205 casagui-0.2.8/casagui/apps/_makemask.py
--rwxr-xr-x   0 runner    (1001) docker     (121)    10835 2022-08-25 15:51:51.565205 casagui-0.2.8/casagui/apps/_plotants.py
--rw-r--r--   0 runner    (1001) docker     (121)     4152 2022-08-25 15:51:51.565205 casagui-0.2.8/casagui/apps/_plotants_logpos.py
--rw-r--r--   0 runner    (1001) docker     (121)      185 2022-08-25 15:51:51.565205 casagui-0.2.8/casagui/apps/_plotbandpass.py
--rw-r--r--   0 runner    (1001) docker     (121)     1371 2022-08-25 15:51:51.565205 casagui-0.2.8/casagui/bokeh/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    18657 2022-08-25 15:51:51.565205 casagui-0.2.8/casagui/bokeh/components/CustomIcon.ts
--rw-r--r--   0 runner    (1001) docker     (121)     1468 2022-08-25 15:51:51.565205 casagui-0.2.8/casagui/bokeh/components/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      687 2022-08-25 15:51:51.565205 casagui-0.2.8/casagui/bokeh/components/_button_group.py
--rw-r--r--   0 runner    (1001) docker     (121)      652 2022-08-25 15:51:51.565205 casagui-0.2.8/casagui/bokeh/components/_iclean_button.py
--rw-r--r--   0 runner    (1001) docker     (121)      652 2022-08-25 15:51:51.565205 casagui-0.2.8/casagui/bokeh/components/_iclean_slider.py
--rw-r--r--   0 runner    (1001) docker     (121)      619 2022-08-25 15:51:51.565205 casagui-0.2.8/casagui/bokeh/components/_svg_icon.py
--rw-r--r--   0 runner    (1001) docker     (121)     1270 2022-08-25 15:51:51.565205 casagui-0.2.8/casagui/bokeh/components/button_group.ts
--rw-r--r--   0 runner    (1001) docker     (121)     1279 2022-08-25 15:51:51.565205 casagui-0.2.8/casagui/bokeh/components/iclean_button.ts
--rw-r--r--   0 runner    (1001) docker     (121)     1279 2022-08-25 15:51:51.565205 casagui-0.2.8/casagui/bokeh/components/iclean_slider.ts
--rw-r--r--   0 runner    (1001) docker     (121)     3579 2022-08-25 15:51:51.565205 casagui-0.2.8/casagui/bokeh/components/svg_icon.ts
--rw-r--r--   0 runner    (1001) docker     (121)     1525 2022-08-25 15:51:51.565205 casagui-0.2.8/casagui/bokeh/sources/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11063 2022-08-25 15:51:51.565205 casagui-0.2.8/casagui/bokeh/sources/_data_pipe.py
--rw-r--r--   0 runner    (1001) docker     (121)     2639 2022-08-25 15:51:51.565205 casagui-0.2.8/casagui/bokeh/sources/_image_data_source.py
--rw-r--r--   0 runner    (1001) docker     (121)    10858 2022-08-25 15:51:51.565205 casagui-0.2.8/casagui/bokeh/sources/_image_pipe.py
--rw-r--r--   0 runner    (1001) docker     (121)     2135 2022-08-25 15:51:51.565205 casagui-0.2.8/casagui/bokeh/sources/_spectra_data_source.py
--rw-r--r--   0 runner    (1001) docker     (121)     6338 2022-08-25 15:51:51.565205 casagui-0.2.8/casagui/bokeh/sources/data_pipe.ts
--rw-r--r--   0 runner    (1001) docker     (121)     2576 2022-08-25 15:51:51.565205 casagui-0.2.8/casagui/bokeh/sources/image_data_source.ts
--rw-r--r--   0 runner    (1001) docker     (121)     6837 2022-08-25 15:51:51.565205 casagui-0.2.8/casagui/bokeh/sources/image_pipe.ts
--rw-r--r--   0 runner    (1001) docker     (121)     1632 2022-08-25 15:51:51.565205 casagui-0.2.8/casagui/bokeh/sources/spectra_data_source.ts
--rw-r--r--   0 runner    (1001) docker     (121)     1504 2022-08-25 15:51:51.565205 casagui-0.2.8/casagui/bokeh/state/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    10227 2022-08-25 15:51:51.565205 casagui-0.2.8/casagui/bokeh/state/_initialize.py
--rw-r--r--   0 runner    (1001) docker     (121)     1761 2022-08-25 15:51:51.565205 casagui-0.2.8/casagui/bokeh/state/_session.py
--rw-r--r--   0 runner    (1001) docker     (121)   799179 2022-08-25 15:51:51.573205 casagui-0.2.8/casagui/bokeh/state/js/bokeh-2.4.1.min.js
--rw-r--r--   0 runner    (1001) docker     (121)   185643 2022-08-25 15:51:51.573205 casagui-0.2.8/casagui/bokeh/state/js/bokeh-gl-2.4.1.min.js
--rw-r--r--   0 runner    (1001) docker     (121)   292438 2022-08-25 15:51:51.573205 casagui-0.2.8/casagui/bokeh/state/js/bokeh-tables-2.4.1.min.js
--rw-r--r--   0 runner    (1001) docker     (121)   251390 2022-08-25 15:51:51.577206 casagui-0.2.8/casagui/bokeh/state/js/bokeh-widgets-2.4.1.min.js
--rw-r--r--   0 runner    (1001) docker     (121)     8432 2022-08-25 15:51:51.577206 casagui-0.2.8/casagui/bokeh/state/js/casaguijs-v0.0.4.0-b2.4.min.js
--rw-r--r--   0 runner    (1001) docker     (121)     8587 2022-08-25 15:51:51.577206 casagui-0.2.8/casagui/bokeh/state/js/casaguijs-v0.0.5.0-b2.4.min.js
--rw-r--r--   0 runner    (1001) docker     (121)     8981 2022-08-25 15:51:51.577206 casagui-0.2.8/casagui/bokeh/state/js/casaguijs-v0.0.6.0-b2.4.min.js
--rw-r--r--   0 runner    (1001) docker     (121)      384 2022-08-25 15:51:51.577206 casagui-0.2.8/casagui/bokeh/state/js/casalib-v0.0.1.min.js
--rw-r--r--   0 runner    (1001) docker     (121)     1479 2022-08-25 15:51:51.577206 casagui-0.2.8/casagui/bokeh/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3168 2022-08-25 15:51:51.577206 casagui-0.2.8/casagui/bokeh/utils/_axes_labels.py
--rw-r--r--   0 runner    (1001) docker     (121)     2184 2022-08-25 15:51:51.577206 casagui-0.2.8/casagui/bokeh/utils/_conversion.py
--rw-r--r--   0 runner    (1001) docker     (121)    12509 2022-08-25 15:51:51.577206 casagui-0.2.8/casagui/bokeh/utils/_serialization.py
--rw-r--r--   0 runner    (1001) docker     (121)     1349 2022-08-25 15:51:51.577206 casagui-0.2.8/casagui/toolbox/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    85239 2022-08-25 15:51:51.577206 casagui-0.2.8/casagui/toolbox/_cube.py
--rw-r--r--   0 runner    (1001) docker     (121)     3410 2022-08-25 15:51:51.577206 casagui-0.2.8/casagui/utils/_ResourceManager.py
--rw-r--r--   0 runner    (1001) docker     (121)    22581 2022-08-25 15:51:51.577206 casagui-0.2.8/casagui/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2348 2022-08-25 15:51:51.577206 casagui-0.2.8/casagui/utils/_logging.py
--rw-r--r--   0 runner    (1001) docker     (121)      772 2022-08-25 15:51:51.613206 casagui-0.2.8/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)     5960 2022-08-25 15:51:51.613206 casagui-0.2.8/readme.rst
--rw-r--r--   0 runner    (1001) docker     (121)      940 2022-08-25 15:51:51.613206 casagui-0.2.8/tests/manual/cubemask-demo/image-slider-spectra-done-stats.py
--rw-r--r--   0 runner    (1001) docker     (121)      878 2022-08-25 15:51:51.613206 casagui-0.2.8/tests/manual/cubemask-demo/image-slider-spectra-done.py
--rw-r--r--   0 runner    (1001) docker     (121)      649 2022-08-25 15:51:51.613206 casagui-0.2.8/tests/manual/cubemask-demo/image-slider-spectra.py
--rw-r--r--   0 runner    (1001) docker     (121)      605 2022-08-25 15:51:51.613206 casagui-0.2.8/tests/manual/cubemask-demo/image-slider.py
--rw-r--r--   0 runner    (1001) docker     (121)      560 2022-08-25 15:51:51.613206 casagui-0.2.8/tests/manual/cubemask-demo/image.py
--rw-r--r--   0 runner    (1001) docker     (121)     2851 2022-08-25 15:51:51.613206 casagui-0.2.8/tests/manual/iclean-demo/m100_interactive.py
--rw-r--r--   0 runner    (1001) docker     (121)     1043 2022-08-25 15:51:51.613206 casagui-0.2.8/tests/manual/iclean-demo/run-gclean.py
--rw-r--r--   0 runner    (1001) docker     (121)     2242 2022-08-25 15:51:51.613206 casagui-0.2.8/tests/manual/iclean-demo/run-iclean.py
--rw-r--r--   0 runner    (1001) docker     (121)      653 2022-08-25 15:51:51.613206 casagui-0.2.8/tests/manual/makemask-demo/run-makemask.py
--rw-r--r--   0 runner    (1001) docker     (121)      508 2022-08-25 15:51:51.613206 casagui-0.2.8/tests/manual/svg-test.py
--rw-------   0 runner    (1001) docker     (121)     6285 2022-08-25 15:52:13.203001 casagui-0.2.8/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)    26526 2022-08-25 16:32:50.805089 casagui-0.2.9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)    26371 2022-08-25 16:32:50.825090 casagui-0.2.9/casagui/LICENSE.rst
+-rw-r--r--   0 runner    (1001) docker     (121)      604 2022-08-25 16:32:50.825090 casagui-0.2.9/casagui/README.rst
+-rw-r--r--   0 runner    (1001) docker     (121)     1755 2022-08-25 16:32:50.825090 casagui-0.2.9/casagui/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1542 2022-08-25 16:32:50.825090 casagui-0.2.9/casagui/apps/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    53786 2022-08-25 16:32:50.825090 casagui-0.2.9/casagui/apps/_interactiveclean.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5937 2022-08-25 16:32:50.825090 casagui-0.2.9/casagui/apps/_makemask.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)    10835 2022-08-25 16:32:50.825090 casagui-0.2.9/casagui/apps/_plotants.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4152 2022-08-25 16:32:50.825090 casagui-0.2.9/casagui/apps/_plotants_logpos.py
+-rw-r--r--   0 runner    (1001) docker     (121)      185 2022-08-25 16:32:50.829089 casagui-0.2.9/casagui/apps/_plotbandpass.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1371 2022-08-25 16:32:50.829089 casagui-0.2.9/casagui/bokeh/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18657 2022-08-25 16:32:50.829089 casagui-0.2.9/casagui/bokeh/components/CustomIcon.ts
+-rw-r--r--   0 runner    (1001) docker     (121)     1468 2022-08-25 16:32:50.829089 casagui-0.2.9/casagui/bokeh/components/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      687 2022-08-25 16:32:50.829089 casagui-0.2.9/casagui/bokeh/components/_button_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)      652 2022-08-25 16:32:50.829089 casagui-0.2.9/casagui/bokeh/components/_iclean_button.py
+-rw-r--r--   0 runner    (1001) docker     (121)      652 2022-08-25 16:32:50.829089 casagui-0.2.9/casagui/bokeh/components/_iclean_slider.py
+-rw-r--r--   0 runner    (1001) docker     (121)      619 2022-08-25 16:32:50.829089 casagui-0.2.9/casagui/bokeh/components/_svg_icon.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1270 2022-08-25 16:32:50.829089 casagui-0.2.9/casagui/bokeh/components/button_group.ts
+-rw-r--r--   0 runner    (1001) docker     (121)     1279 2022-08-25 16:32:50.829089 casagui-0.2.9/casagui/bokeh/components/iclean_button.ts
+-rw-r--r--   0 runner    (1001) docker     (121)     1279 2022-08-25 16:32:50.829089 casagui-0.2.9/casagui/bokeh/components/iclean_slider.ts
+-rw-r--r--   0 runner    (1001) docker     (121)     3579 2022-08-25 16:32:50.829089 casagui-0.2.9/casagui/bokeh/components/svg_icon.ts
+-rw-r--r--   0 runner    (1001) docker     (121)     1525 2022-08-25 16:32:50.829089 casagui-0.2.9/casagui/bokeh/sources/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11063 2022-08-25 16:32:50.829089 casagui-0.2.9/casagui/bokeh/sources/_data_pipe.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2639 2022-08-25 16:32:50.829089 casagui-0.2.9/casagui/bokeh/sources/_image_data_source.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10858 2022-08-25 16:32:50.829089 casagui-0.2.9/casagui/bokeh/sources/_image_pipe.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2135 2022-08-25 16:32:50.829089 casagui-0.2.9/casagui/bokeh/sources/_spectra_data_source.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6338 2022-08-25 16:32:50.829089 casagui-0.2.9/casagui/bokeh/sources/data_pipe.ts
+-rw-r--r--   0 runner    (1001) docker     (121)     2576 2022-08-25 16:32:50.829089 casagui-0.2.9/casagui/bokeh/sources/image_data_source.ts
+-rw-r--r--   0 runner    (1001) docker     (121)     6837 2022-08-25 16:32:50.829089 casagui-0.2.9/casagui/bokeh/sources/image_pipe.ts
+-rw-r--r--   0 runner    (1001) docker     (121)     1632 2022-08-25 16:32:50.829089 casagui-0.2.9/casagui/bokeh/sources/spectra_data_source.ts
+-rw-r--r--   0 runner    (1001) docker     (121)     1504 2022-08-25 16:32:50.829089 casagui-0.2.9/casagui/bokeh/state/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10227 2022-08-25 16:32:50.829089 casagui-0.2.9/casagui/bokeh/state/_initialize.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1761 2022-08-25 16:32:50.829089 casagui-0.2.9/casagui/bokeh/state/_session.py
+-rw-r--r--   0 runner    (1001) docker     (121)   799179 2022-08-25 16:32:50.833090 casagui-0.2.9/casagui/bokeh/state/js/bokeh-2.4.1.min.js
+-rw-r--r--   0 runner    (1001) docker     (121)   185643 2022-08-25 16:32:50.833090 casagui-0.2.9/casagui/bokeh/state/js/bokeh-gl-2.4.1.min.js
+-rw-r--r--   0 runner    (1001) docker     (121)   292438 2022-08-25 16:32:50.833090 casagui-0.2.9/casagui/bokeh/state/js/bokeh-tables-2.4.1.min.js
+-rw-r--r--   0 runner    (1001) docker     (121)   251390 2022-08-25 16:32:50.837090 casagui-0.2.9/casagui/bokeh/state/js/bokeh-widgets-2.4.1.min.js
+-rw-r--r--   0 runner    (1001) docker     (121)     8432 2022-08-25 16:32:50.837090 casagui-0.2.9/casagui/bokeh/state/js/casaguijs-v0.0.4.0-b2.4.min.js
+-rw-r--r--   0 runner    (1001) docker     (121)     8587 2022-08-25 16:32:50.837090 casagui-0.2.9/casagui/bokeh/state/js/casaguijs-v0.0.5.0-b2.4.min.js
+-rw-r--r--   0 runner    (1001) docker     (121)     8981 2022-08-25 16:32:50.837090 casagui-0.2.9/casagui/bokeh/state/js/casaguijs-v0.0.6.0-b2.4.min.js
+-rw-r--r--   0 runner    (1001) docker     (121)      384 2022-08-25 16:32:50.837090 casagui-0.2.9/casagui/bokeh/state/js/casalib-v0.0.1.min.js
+-rw-r--r--   0 runner    (1001) docker     (121)     1479 2022-08-25 16:32:50.837090 casagui-0.2.9/casagui/bokeh/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3168 2022-08-25 16:32:50.837090 casagui-0.2.9/casagui/bokeh/utils/_axes_labels.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2184 2022-08-25 16:32:50.837090 casagui-0.2.9/casagui/bokeh/utils/_conversion.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12509 2022-08-25 16:32:50.837090 casagui-0.2.9/casagui/bokeh/utils/_serialization.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1349 2022-08-25 16:32:50.837090 casagui-0.2.9/casagui/toolbox/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    85239 2022-08-25 16:32:50.837090 casagui-0.2.9/casagui/toolbox/_cube.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3410 2022-08-25 16:32:50.837090 casagui-0.2.9/casagui/utils/_ResourceManager.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22581 2022-08-25 16:32:50.837090 casagui-0.2.9/casagui/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2348 2022-08-25 16:32:50.837090 casagui-0.2.9/casagui/utils/_logging.py
+-rw-r--r--   0 runner    (1001) docker     (121)      772 2022-08-25 16:32:50.869090 casagui-0.2.9/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (121)     5960 2022-08-25 16:32:50.869090 casagui-0.2.9/readme.rst
+-rw-r--r--   0 runner    (1001) docker     (121)      940 2022-08-25 16:32:50.869090 casagui-0.2.9/tests/manual/cubemask-demo/image-slider-spectra-done-stats.py
+-rw-r--r--   0 runner    (1001) docker     (121)      878 2022-08-25 16:32:50.869090 casagui-0.2.9/tests/manual/cubemask-demo/image-slider-spectra-done.py
+-rw-r--r--   0 runner    (1001) docker     (121)      649 2022-08-25 16:32:50.869090 casagui-0.2.9/tests/manual/cubemask-demo/image-slider-spectra.py
+-rw-r--r--   0 runner    (1001) docker     (121)      605 2022-08-25 16:32:50.869090 casagui-0.2.9/tests/manual/cubemask-demo/image-slider.py
+-rw-r--r--   0 runner    (1001) docker     (121)      560 2022-08-25 16:32:50.869090 casagui-0.2.9/tests/manual/cubemask-demo/image.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2851 2022-08-25 16:32:50.869090 casagui-0.2.9/tests/manual/iclean-demo/m100_interactive.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1043 2022-08-25 16:32:50.869090 casagui-0.2.9/tests/manual/iclean-demo/run-gclean.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2242 2022-08-25 16:32:50.869090 casagui-0.2.9/tests/manual/iclean-demo/run-iclean.py
+-rw-r--r--   0 runner    (1001) docker     (121)      653 2022-08-25 16:32:50.869090 casagui-0.2.9/tests/manual/makemask-demo/run-makemask.py
+-rw-r--r--   0 runner    (1001) docker     (121)      508 2022-08-25 16:32:50.869090 casagui-0.2.9/tests/manual/svg-test.py
+-rw-------   0 runner    (1001) docker     (121)     6285 2022-08-25 16:33:08.593272 casagui-0.2.9/PKG-INFO
```

### Comparing `casagui-0.2.8/LICENSE` & `casagui-0.2.9/LICENSE`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/LICENSE.rst` & `casagui-0.2.9/casagui/LICENSE.rst`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/README.rst` & `casagui-0.2.9/casagui/README.rst`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/__init__.py` & `casagui-0.2.9/casagui/__init__.py`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/apps/__init__.py` & `casagui-0.2.9/casagui/apps/__init__.py`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/apps/_interactiveclean.py` & `casagui-0.2.9/casagui/apps/_interactiveclean.py`

 * *Ordering differences only*

 * *Files 0% similar despite different names*

```diff
@@ -145,14 +145,15 @@
                   width='', interpolation='linear', gridder='standard', pblimit=0.2, deconvolver='hogbom', niter=0,
                   threshold='0.1Jy', cycleniter=-1, cyclefactor=1.0, scales=[], weighting='natural', robust=float(0.5) ):
 
         ###
         ### used by data pipe (websocket) initialization function
         ###
         self.__pipes_initialized = False
+        self._mask_history = [ ]
 
         ###
         ### color specs
         ###
         self._color = { 'residual': 'black',
                         'flux':     'forestgreen' }
 
@@ -202,15 +203,14 @@
         self._imagename = imagename
         self._residual_path = ("%s.residual" % imagename) if self._clean.has_next() else (self._clean.finalize()['image'])
         self._pipe = { 'control': None, 'converge': None }
         self._control = { }
         self._cb = { }
         self._ids = { }
         self._last_mask_breadcrumbs = ''
-        self._mask_history = [ ]
 
         ###
         ### The tclean convergence data is automatically generated by tclean and it
         ### accumulates in this object. If the data becomes bigger than these
         ### thresholds, the implementation switches to fetching threshold data
         ### from python for each channel selected in the GUI within the browser.
         ###
```

### Comparing `casagui-0.2.8/casagui/apps/_makemask.py` & `casagui-0.2.9/casagui/apps/_makemask.py`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/apps/_plotants.py` & `casagui-0.2.9/casagui/apps/_plotants.py`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/apps/_plotants_logpos.py` & `casagui-0.2.9/casagui/apps/_plotants_logpos.py`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/bokeh/__init__.py` & `casagui-0.2.9/casagui/bokeh/__init__.py`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/bokeh/components/CustomIcon.ts` & `casagui-0.2.9/casagui/bokeh/components/CustomIcon.ts`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/bokeh/components/__init__.py` & `casagui-0.2.9/casagui/bokeh/components/__init__.py`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/bokeh/components/_button_group.py` & `casagui-0.2.9/casagui/bokeh/components/_button_group.py`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/bokeh/components/_iclean_button.py` & `casagui-0.2.9/casagui/bokeh/components/_iclean_button.py`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/bokeh/components/_iclean_slider.py` & `casagui-0.2.9/casagui/bokeh/components/_iclean_slider.py`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/bokeh/components/_svg_icon.py` & `casagui-0.2.9/casagui/bokeh/components/_svg_icon.py`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/bokeh/components/button_group.ts` & `casagui-0.2.9/casagui/bokeh/components/button_group.ts`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/bokeh/components/iclean_button.ts` & `casagui-0.2.9/casagui/bokeh/components/iclean_button.ts`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/bokeh/components/iclean_slider.ts` & `casagui-0.2.9/casagui/bokeh/components/iclean_slider.ts`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/bokeh/components/svg_icon.ts` & `casagui-0.2.9/casagui/bokeh/components/svg_icon.ts`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/bokeh/sources/__init__.py` & `casagui-0.2.9/casagui/bokeh/sources/__init__.py`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/bokeh/sources/_data_pipe.py` & `casagui-0.2.9/casagui/bokeh/sources/_data_pipe.py`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/bokeh/sources/_image_data_source.py` & `casagui-0.2.9/casagui/bokeh/sources/_image_data_source.py`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/bokeh/sources/_image_pipe.py` & `casagui-0.2.9/casagui/bokeh/sources/_image_pipe.py`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/bokeh/sources/_spectra_data_source.py` & `casagui-0.2.9/casagui/bokeh/sources/_spectra_data_source.py`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/bokeh/sources/data_pipe.ts` & `casagui-0.2.9/casagui/bokeh/sources/data_pipe.ts`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/bokeh/sources/image_data_source.ts` & `casagui-0.2.9/casagui/bokeh/sources/image_data_source.ts`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/bokeh/sources/image_pipe.ts` & `casagui-0.2.9/casagui/bokeh/sources/image_pipe.ts`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/bokeh/sources/spectra_data_source.ts` & `casagui-0.2.9/casagui/bokeh/sources/spectra_data_source.ts`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/bokeh/state/__init__.py` & `casagui-0.2.9/casagui/bokeh/state/__init__.py`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/bokeh/state/_initialize.py` & `casagui-0.2.9/casagui/bokeh/state/_initialize.py`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/bokeh/state/_session.py` & `casagui-0.2.9/casagui/bokeh/state/_session.py`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/bokeh/state/js/bokeh-2.4.1.min.js` & `casagui-0.2.9/casagui/bokeh/state/js/bokeh-2.4.1.min.js`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/bokeh/state/js/bokeh-gl-2.4.1.min.js` & `casagui-0.2.9/casagui/bokeh/state/js/bokeh-gl-2.4.1.min.js`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/bokeh/state/js/bokeh-tables-2.4.1.min.js` & `casagui-0.2.9/casagui/bokeh/state/js/bokeh-tables-2.4.1.min.js`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/bokeh/state/js/bokeh-widgets-2.4.1.min.js` & `casagui-0.2.9/casagui/bokeh/state/js/bokeh-widgets-2.4.1.min.js`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/bokeh/state/js/casaguijs-v0.0.4.0-b2.4.min.js` & `casagui-0.2.9/casagui/bokeh/state/js/casaguijs-v0.0.4.0-b2.4.min.js`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/bokeh/state/js/casaguijs-v0.0.5.0-b2.4.min.js` & `casagui-0.2.9/casagui/bokeh/state/js/casaguijs-v0.0.5.0-b2.4.min.js`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/bokeh/state/js/casaguijs-v0.0.6.0-b2.4.min.js` & `casagui-0.2.9/casagui/bokeh/state/js/casaguijs-v0.0.6.0-b2.4.min.js`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/bokeh/utils/__init__.py` & `casagui-0.2.9/casagui/bokeh/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/bokeh/utils/_axes_labels.py` & `casagui-0.2.9/casagui/bokeh/utils/_axes_labels.py`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/bokeh/utils/_conversion.py` & `casagui-0.2.9/casagui/bokeh/utils/_conversion.py`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/bokeh/utils/_serialization.py` & `casagui-0.2.9/casagui/bokeh/utils/_serialization.py`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/toolbox/__init__.py` & `casagui-0.2.9/casagui/toolbox/__init__.py`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/toolbox/_cube.py` & `casagui-0.2.9/casagui/toolbox/_cube.py`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/utils/_ResourceManager.py` & `casagui-0.2.9/casagui/utils/_ResourceManager.py`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/utils/__init__.py` & `casagui-0.2.9/casagui/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/casagui/utils/_logging.py` & `casagui-0.2.9/casagui/utils/_logging.py`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/pyproject.toml` & `casagui-0.2.9/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -12,15 +12,15 @@
     "bokeh>=2.4.0",
     "astropy>=5.1",
     "regions>=0.6",
     "websockets>=10.3",
 ]
 requires-python = ">=3.8"
 readme = "readme.rst"
-version = "0.2.8"
+version = "0.2.9"
 
 [project.license]
 text = "LGPL"
 
 [tool.pdm.build]
 
 [tool.pdm.version]
```

### Comparing `casagui-0.2.8/readme.rst` & `casagui-0.2.9/readme.rst`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/tests/manual/cubemask-demo/image-slider-spectra-done-stats.py` & `casagui-0.2.9/tests/manual/cubemask-demo/image-slider-spectra-done-stats.py`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/tests/manual/cubemask-demo/image-slider-spectra-done.py` & `casagui-0.2.9/tests/manual/cubemask-demo/image-slider-spectra-done.py`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/tests/manual/cubemask-demo/image-slider-spectra.py` & `casagui-0.2.9/tests/manual/cubemask-demo/image-slider-spectra.py`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/tests/manual/cubemask-demo/image-slider.py` & `casagui-0.2.9/tests/manual/cubemask-demo/image-slider.py`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/tests/manual/cubemask-demo/image.py` & `casagui-0.2.9/tests/manual/cubemask-demo/image.py`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/tests/manual/iclean-demo/m100_interactive.py` & `casagui-0.2.9/tests/manual/iclean-demo/m100_interactive.py`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/tests/manual/iclean-demo/run-gclean.py` & `casagui-0.2.9/tests/manual/iclean-demo/run-gclean.py`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/tests/manual/iclean-demo/run-iclean.py` & `casagui-0.2.9/tests/manual/iclean-demo/run-iclean.py`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/tests/manual/makemask-demo/run-makemask.py` & `casagui-0.2.9/tests/manual/makemask-demo/run-makemask.py`

 * *Files identical despite different names*

### Comparing `casagui-0.2.8/PKG-INFO` & `casagui-0.2.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: casagui
-Version: 0.2.8
+Version: 0.2.9
 Summary: visualization toolkit and apps for casa
 License: LGPL
 Author-email: Darrell Schiebel <darrell@schiebel.us>,Joshua Hoskins <jhoskins@nrao.edu>,Jorge Lopez <jalopez@nrao.edu>,Pam Harris <pharris@nrao.edu>
 Requires-Python: >=3.8
 Description-Content-Type: text/x-rst
 
 casagui - visualization tools and applications for CASA
```

