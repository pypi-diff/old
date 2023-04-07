# Comparing `tmp/holoviews-1.9.4.tar.gz` & `tmp/holoviews-1.9.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/holoviews-1.9.4.tar", last modified: Fri Feb 16 16:52:32 2018, max compression
+gzip compressed data, was "dist/holoviews-1.9.5.tar", last modified: Fri Mar  2 13:00:26 2018, max compression
```

## Comparing `holoviews-1.9.4.tar` & `holoviews-1.9.5.tar`

### file list

```diff
@@ -1,801 +1,805 @@
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:32.000000 holoviews-1.9.4/
--rw-r--r--   0 jstevens   (501) wheel        (0)    64921 2018-02-16 15:56:20.000000 holoviews-1.9.4/CHANGELOG.md
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/doc/
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/doc/_static/
--rw-r--r--   0 jstevens   (501) wheel        (0)    15086 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/_static/favicon.ico
--rw-r--r--   0 jstevens   (501) wheel        (0)     4278 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/_static/holoviews_logo.png
--rw-r--r--   0 jstevens   (501) wheel        (0)      651 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/_static/rtd_bootstrap.css
--rw-r--r--   0 jstevens   (501) wheel        (0)      819 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/about.rst
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/doc/assets/
--rw-r--r--   0 jstevens   (501) wheel        (0)   338681 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/assets/macaw.png
--rw-r--r--   0 jstevens   (501) wheel        (0)  1046222 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/assets/nesting-diagram.svg
--rw-r--r--   0 jstevens   (501) wheel        (0)   175335 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/assets/penguins.png
--rw-r--r--   0 jstevens   (501) wheel        (0)      337 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/assets/README.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)     5250 2018-02-16 15:51:52.000000 holoviews-1.9.4/doc/conf.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     7101 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/FAQ.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)     4158 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/features.rst
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/doc/getting_started/
--rw-r--r--   0 jstevens   (501) wheel        (0)      121 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/getting_started/Customization.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)      130 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/getting_started/Gridded_Datasets.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)     1457 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/getting_started/index.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)      118 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/getting_started/Introduction.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)      204 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/getting_started/Live_Data.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)      130 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/getting_started/Tabular_Datasets.rst
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/doc/holoviews_theme/
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/doc/holoviews_theme/includes/
--rw-r--r--   0 jstevens   (501) wheel        (0)      409 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/holoviews_theme/includes/ga.html
--rw-r--r--   0 jstevens   (501) wheel        (0)      341 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/holoviews_theme/includes/searchbox.html
--rw-r--r--   0 jstevens   (501) wheel        (0)     4751 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/holoviews_theme/layout.html
--rw-r--r--   0 jstevens   (501) wheel        (0)     1399 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/holoviews_theme/search.html
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/doc/holoviews_theme/static/
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/doc/holoviews_theme/static/images/
--rw-r--r--   0 jstevens   (501) wheel        (0)     6139 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/holoviews_theme/static/images/favicon.ico
--rw-r--r--   0 jstevens   (501) wheel        (0)    17919 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/holoviews_theme/static/images/logo.png
--rw-r--r--   0 jstevens   (501) wheel        (0)     4386 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/holoviews_theme/static/images/logo.svg
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/doc/holoviews_theme/static/js/
--rw-r--r--   0 jstevens   (501) wheel        (0)     2188 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/holoviews_theme/static/js/main.js
--rw-r--r--   0 jstevens   (501) wheel        (0)       99 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/holoviews_theme/theme.conf
--rw-r--r--   0 jstevens   (501) wheel        (0)     7007 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/Homepage.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     5669 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/index.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)     2591 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/install.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)      319 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/latest_news.html
--rw-r--r--   0 jstevens   (501) wheel        (0)      163 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/Makefile
--rw-r--r--   0 jstevens   (501) wheel        (0)  1280080 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/mandelbrot.npy
--rw-r--r--   0 jstevens   (501) wheel        (0)       63 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/notebook.json
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/doc/Reference_Manual/
--rw-r--r--   0 jstevens   (501) wheel        (0)     2409 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/Reference_Manual/index.rst
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/doc/showcase/
--rw-r--r--   0 jstevens   (501) wheel        (0)       97 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/showcase/boids.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)      130 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/showcase/hipster_dynamics.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)     3152 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/showcase/index.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)      106 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/showcase/lsystems.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)      116 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/showcase/square_limit.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)      135 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/showcase/sri_model.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)      149 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/site_map.rst
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/doc/test_data/
--rw-r--r--   0 jstevens   (501) wheel        (0)      231 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/test_data/README.rst
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/doc/Tutorials/
--rw-r--r--   0 jstevens   (501) wheel        (0)    17298 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/Tutorials/Bokeh_Backend.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    54084 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/Tutorials/Bokeh_Elements.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    35575 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/Tutorials/Columnar_Data.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    16108 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/Tutorials/Composing_Data.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    22811 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/Tutorials/Containers.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    14967 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/Tutorials/Continuous_Coordinates.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    29346 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/Tutorials/Dynamic_Map.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    54557 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/Tutorials/Elements.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    24754 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/Tutorials/Exploring_Data.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    25741 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/Tutorials/Exporting.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4322 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/Tutorials/index.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)    32364 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/Tutorials/Introduction.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    16793 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/Tutorials/Linked_Streams.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    16872 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/Tutorials/Operations.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    33130 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/Tutorials/Options.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    12227 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/Tutorials/Pandas_Seaborn.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    23789 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/Tutorials/Rich_Display.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    15916 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/Tutorials/Sampling_Data.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    24755 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/Tutorials/Showcase.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    28850 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/Tutorials/Streams.ipynb
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/doc/user_guide/
--rw-r--r--   0 jstevens   (501) wheel        (0)      133 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/user_guide/Annotating_Data.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)      156 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/user_guide/Building_Composite_Objects.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)      133 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/user_guide/Composing_Elements.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)      141 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/user_guide/Continuous_Coordinates.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)      162 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/user_guide/Custom_Interactivity.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)      129 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/user_guide/Customizing_Plots.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)      174 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/user_guide/Dashboards.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)      142 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/user_guide/Data_Pipelines.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)      159 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/user_guide/Deploying_Bokeh_Apps.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)      145 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/user_guide/Dimensioned_Containers.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)      144 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/user_guide/Exporting_and_Archiving.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)      126 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/user_guide/Gridded_Datasets.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)     5560 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/user_guide/index.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)      159 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/user_guide/Indexing_and_Selecting_Data.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)      173 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/user_guide/Installing_and_Configuring.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)       30 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/user_guide/IPython_Magics.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)      168 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/user_guide/Large_Data.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)      105 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/user_guide/Live_Data.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)      156 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/user_guide/Plots_and_Renderers.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)      132 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/user_guide/Plotting_with_Bokeh.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)       50 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/user_guide/Plotting_with_Matplotlib.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)      138 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/user_guide/Responding_to_Events.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)      170 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/user_guide/Streaming_Data.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)      126 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/user_guide/Tabular_Datasets.rst
--rw-r--r--   0 jstevens   (501) wheel        (0)      141 2018-02-16 15:51:14.000000 holoviews-1.9.4/doc/user_guide/Transforming_Elements.rst
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/examples/
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/examples/assets/
--rw-r--r--   0 jstevens   (501) wheel        (0)   978004 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/assets/diseases.csv.gz
--rw-r--r--   0 jstevens   (501) wheel        (0)    18624 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/assets/fb_edges.csv
--rw-r--r--   0 jstevens   (501) wheel        (0)    16723 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/assets/fb_nodes.csv
--rw-r--r--   0 jstevens   (501) wheel        (0)   660600 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/assets/hourly_taxi_data.npz
--rw-r--r--   0 jstevens   (501) wheel        (0)   175335 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/assets/penguins.png
--rw-r--r--   0 jstevens   (501) wheel        (0)     2096 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/assets/spike_train.csv.gz
--rw-r--r--   0 jstevens   (501) wheel        (0)     4690 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/assets/station_info.csv
--rw-r--r--   0 jstevens   (501) wheel        (0)   535712 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/assets/twophoton.npz
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/examples/gallery/
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/examples/gallery/demos/
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/examples/gallery/demos/bokeh/
--rw-r--r--   0 jstevens   (501) wheel        (0)     1874 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/bokeh/area_chart.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1261 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/bokeh/autompg_histogram.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4629 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/bokeh/bachelors_degrees_by_gender.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1659 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/bokeh/bars_economic.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1501 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/bokeh/boxplot_chart.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1779 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/bokeh/dot_example.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4362 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/bokeh/dragon_curve.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2136 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/bokeh/dropdown_economic.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4284 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/bokeh/histogram_example.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1799 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/bokeh/iris_density_grid.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1376 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/bokeh/iris_example.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1892 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/bokeh/iris_grouped_grid.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1650 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/bokeh/iris_splom_example.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1869 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/bokeh/legend_example.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2940 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/bokeh/lesmis_example.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2000 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/bokeh/lorenz_attractor_example.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2213 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/bokeh/mandelbrot_section.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2663 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/bokeh/measles_example.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1827 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/bokeh/network_graph.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2221 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/bokeh/quiver_demo.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1832 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/bokeh/scatter_economic.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     6061 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/bokeh/square_limit.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2065 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/bokeh/step_chart.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2472 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/bokeh/stocks_example.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1937 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/bokeh/texas_choropleth_example.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2708 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/bokeh/topographic_hillshading.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1826 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/bokeh/us_unemployment.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3793 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/bokeh/verhulst_mandelbrot.ipynb
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/examples/gallery/demos/matplotlib/
--rw-r--r--   0 jstevens   (501) wheel        (0)     1904 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/matplotlib/area_chart.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1243 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/matplotlib/autompg_histogram.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4579 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/matplotlib/bachelors_degrees_by_gender.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1682 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/matplotlib/bars_economic.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1476 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/matplotlib/boxplot_chart.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4383 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/matplotlib/dragon_curve.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2058 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/matplotlib/dropdown_economic.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4245 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/matplotlib/histogram_example.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1768 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/matplotlib/iris_density_grid.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1375 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/matplotlib/iris_example.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1854 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/matplotlib/iris_grouped_grid.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1599 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/matplotlib/iris_splom_example.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1830 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/matplotlib/legend_example.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1993 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/matplotlib/lorenz_attractor_example.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2160 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/matplotlib/mandelbrot_section.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2863 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/matplotlib/measles_example.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1772 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/matplotlib/network_graph.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1355 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/matplotlib/polar_scatter_demo.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2287 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/matplotlib/quiver_demo.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1852 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/matplotlib/scatter_economic.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     6136 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/matplotlib/square_limit.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2026 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/matplotlib/step_chart.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2511 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/matplotlib/stocks_example.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1401 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/matplotlib/surface_3d.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1915 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/matplotlib/texas_choropleth_example.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2729 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/matplotlib/topographic_hillshading.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2141 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/matplotlib/trisurf3d_demo.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1811 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/matplotlib/us_unemployment.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3778 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/matplotlib/verhulst_mandelbrot.ipynb
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/examples/gallery/demos/plotly/
--rw-r--r--   0 jstevens   (501) wheel        (0)     1567 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/plotly/surface_3d.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2169 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/gallery/demos/plotly/trisurf3d_demo.ipynb
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/examples/getting_started/
--rw-r--r--   0 jstevens   (501) wheel        (0)    18070 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/getting_started/1-Introduction.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    13692 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/getting_started/2-Customization.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    12141 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/getting_started/3-Tabular_Datasets.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    12520 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/getting_started/4-Gridded_Datasets.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    13473 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/getting_started/5-Live_Data.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1259 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/README.md
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/examples/reference/
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/examples/reference/containers/
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/examples/reference/containers/bokeh/
--rw-r--r--   0 jstevens   (501) wheel        (0)     4122 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/containers/bokeh/DynamicMap.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3501 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/containers/bokeh/GridSpace.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     6188 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/containers/bokeh/HoloMap.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2852 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/containers/bokeh/Layout.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4616 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/containers/bokeh/NdLayout.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4458 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/containers/bokeh/NdOverlay.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2764 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/containers/bokeh/Overlay.ipynb
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/examples/reference/containers/matplotlib/
--rw-r--r--   0 jstevens   (501) wheel        (0)     4127 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/containers/matplotlib/DynamicMap.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3478 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/containers/matplotlib/GridSpace.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     6188 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/containers/matplotlib/HoloMap.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2853 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/containers/matplotlib/Layout.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4616 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/containers/matplotlib/NdLayout.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4458 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/containers/matplotlib/NdOverlay.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2763 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/containers/matplotlib/Overlay.ipynb
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/examples/reference/elements/
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/examples/reference/elements/assets/
--rw-r--r--   0 jstevens   (501) wheel        (0)   175335 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/assets/penguins.png
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/examples/reference/elements/bokeh/
--rw-r--r--   0 jstevens   (501) wheel        (0)     3846 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/bokeh/Area.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2134 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/bokeh/Arrow.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3161 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/bokeh/Bars.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4028 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/bokeh/Bivariate.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2133 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/bokeh/Bounds.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2506 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/bokeh/Box.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2926 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/bokeh/BoxWhisker.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3081 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/bokeh/Contours.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2791 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/bokeh/Curve.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4326 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/bokeh/Distribution.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2568 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/bokeh/Ellipse.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3065 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/bokeh/ErrorBars.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     5525 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/bokeh/Graph.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3199 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/bokeh/HeatMap.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3734 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/bokeh/Histogram.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1557 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/bokeh/HLine.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2914 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/bokeh/HSV.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3743 2018-02-16 15:51:52.000000 holoviews-1.9.4/examples/reference/elements/bokeh/Image.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1873 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/bokeh/ItemTable.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4762 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/bokeh/Path.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4662 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/bokeh/Points.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3952 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/bokeh/Polygons.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3979 2018-02-16 15:51:52.000000 holoviews-1.9.4/examples/reference/elements/bokeh/QuadMesh.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1904 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/bokeh/Raster.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3652 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/bokeh/RGB.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4814 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/bokeh/Scatter.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4314 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/bokeh/Spikes.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1752 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/bokeh/Spline.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3039 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/bokeh/Spread.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3489 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/bokeh/Table.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1412 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/bokeh/Text.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4856 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/bokeh/VectorField.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1520 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/bokeh/VLine.ipynb
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/examples/reference/elements/matplotlib/
--rw-r--r--   0 jstevens   (501) wheel        (0)     3851 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/matplotlib/Area.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2140 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/matplotlib/Arrow.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3238 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/matplotlib/Bars.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3981 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/matplotlib/Bivariate.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2137 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/matplotlib/Bounds.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2509 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/matplotlib/Box.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2928 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/matplotlib/BoxWhisker.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3102 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/matplotlib/Contours.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2778 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/matplotlib/Curve.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4395 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/matplotlib/Distribution.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2572 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/matplotlib/Ellipse.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3070 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/matplotlib/ErrorBars.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     5513 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/matplotlib/Graph.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3130 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/matplotlib/HeatMap.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3773 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/matplotlib/Histogram.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1561 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/matplotlib/HLine.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2919 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/matplotlib/HSV.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3748 2018-02-16 15:51:52.000000 holoviews-1.9.4/examples/reference/elements/matplotlib/Image.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1840 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/matplotlib/ItemTable.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4776 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/matplotlib/Path.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4657 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/matplotlib/Points.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3901 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/matplotlib/Polygons.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3266 2018-02-16 15:51:52.000000 holoviews-1.9.4/examples/reference/elements/matplotlib/QuadMesh.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1908 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/matplotlib/Raster.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3657 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/matplotlib/RGB.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4819 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/matplotlib/Scatter.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2279 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/matplotlib/Scatter3D.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4304 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/matplotlib/Spikes.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1804 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/matplotlib/Spline.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3027 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/matplotlib/Spread.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2696 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/matplotlib/Surface.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3403 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/matplotlib/Table.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1417 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/matplotlib/Text.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2562 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/matplotlib/TriSurface.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     5292 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/matplotlib/VectorField.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1524 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/matplotlib/VLine.ipynb
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/examples/reference/elements/plotly/
--rw-r--r--   0 jstevens   (501) wheel        (0)     2596 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/plotly/BoxWhiskers.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2774 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/plotly/Curve.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1987 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/plotly/Distribution.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3122 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/plotly/ErrorBars.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3237 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/plotly/HeatMap.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3549 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/plotly/Image.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1892 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/plotly/ItemTable.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4677 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/plotly/Points.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1957 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/plotly/Raster.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4838 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/plotly/Scatter.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2333 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/plotly/Scatter3D.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2573 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/plotly/Surface.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3460 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/plotly/Table.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2598 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/elements/plotly/TriSurface.ipynb
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/examples/reference/features/
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/examples/reference/features/bokeh/
--rw-r--r--   0 jstevens   (501) wheel        (0)     1675 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/features/bokeh/table_hooks_example.ipynb
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/examples/reference/streams/
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/examples/reference/streams/bokeh/
--rw-r--r--   0 jstevens   (501) wheel        (0)     2756 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/streams/bokeh/Bounds.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1797 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/streams/bokeh/BoundsX.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2032 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/streams/bokeh/BoundsY.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2098 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/streams/bokeh/PointerX.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1925 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/streams/bokeh/PointerXY.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1917 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/streams/bokeh/RangeXY.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1565 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/streams/bokeh/Selection1D.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2277 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/streams/bokeh/Selection1D_paired.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2149 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/streams/bokeh/Selection1D_points.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3258 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/streams/bokeh/Selection1D_tap.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2723 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/reference/streams/bokeh/Tap.ipynb
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/examples/topics/
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/examples/topics/geometry/
--rw-r--r--   0 jstevens   (501) wheel        (0)    15860 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/topics/geometry/lsystems.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    10960 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/topics/geometry/square_limit.ipynb
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/examples/topics/simulation/
--rw-r--r--   0 jstevens   (501) wheel        (0)     9738 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/topics/simulation/boids.ipynb
--rwxr-xr-x   0 jstevens   (501) wheel        (0)    13977 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/topics/simulation/hipster_dynamics.ipynb
--rwxr-xr-x   0 jstevens   (501) wheel        (0)    28641 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/topics/simulation/sri_model.ipynb
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/examples/user_guide/
--rw-r--r--   0 jstevens   (501) wheel        (0)    12341 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/user_guide/01-Annotating_Data.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    14136 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/user_guide/02-Composing_Elements.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    21529 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/user_guide/03-Customizing_Plots.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    12295 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/user_guide/04-Dimensioned_Containers.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    16424 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/user_guide/05-Building_Composite_Objects.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    29485 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/user_guide/06-Live_Data.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    22018 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/user_guide/07-Tabular_Datasets.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    11996 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/user_guide/08-Gridded_Datasets.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    18763 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/user_guide/09-Indexing_and_Selecting_Data.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    22088 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/user_guide/10-Transforming_Elements.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    29588 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/user_guide/11-Responding_to_Events.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    19594 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/user_guide/12-Custom_Interactivity.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     8512 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/user_guide/13-Data_Pipelines.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    19182 2018-02-16 15:51:52.000000 holoviews-1.9.4/examples/user_guide/14-Large_Data.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    25079 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/user_guide/15-Streaming_Data.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     7880 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/user_guide/16-Dashboards.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    15196 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/user_guide/Continuous_Coordinates.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    22354 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/user_guide/Deploying_Bokeh_Apps.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    26456 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/user_guide/Exporting_and_Archiving.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     6099 2018-02-16 15:51:52.000000 holoviews-1.9.4/examples/user_guide/Installing_and_Configuring.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    12659 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/user_guide/Network_Graphs.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    18793 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/user_guide/Plots_and_Renderers.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    18463 2018-02-16 15:51:52.000000 holoviews-1.9.4/examples/user_guide/Plotting_with_Bokeh.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     6140 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/user_guide/Plotting_with_Matplotlib.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2603 2018-02-16 15:51:14.000000 holoviews-1.9.4/examples/user_guide/Tips_and_Tricks.ipynb
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/
--rw-r--r--   0 jstevens   (501) wheel        (0)     3808 2018-02-16 16:09:43.000000 holoviews-1.9.4/holoviews/__init__.py
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/core/
--rw-r--r--   0 jstevens   (501) wheel        (0)     1828 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/core/__init__.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    10528 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/core/boundingregion.py
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/core/data/
--rw-r--r--   0 jstevens   (501) wheel        (0)    26340 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/core/data/__init__.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     9405 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/core/data/array.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     9893 2018-02-16 16:06:39.000000 holoviews-1.9.4/holoviews/core/data/dask.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    14076 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/core/data/dictionary.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    17850 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/core/data/grid.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    10717 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/core/data/image.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    12313 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/core/data/interface.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    11740 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/core/data/iris.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     8669 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/core/data/multipath.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    11331 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/core/data/pandas.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    13871 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/core/data/xarray.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    47699 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/core/dimension.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    15012 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/core/element.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    33790 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/core/io.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    18417 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/core/layout.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    31988 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/core/ndmapping.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     8111 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/core/operation.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    64694 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/core/options.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     8816 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/core/overlay.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    15136 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/core/pprint.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    20510 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/core/sheetcoords.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    62603 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/core/spaces.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     5152 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/core/traversal.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     9886 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/core/tree.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    56281 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/core/util.py
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/element/
--rw-r--r--   0 jstevens   (501) wheel        (0)     4121 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/element/__init__.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     9535 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/element/annotation.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    15384 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/element/chart.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     2939 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/element/chart3d.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    25981 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/element/comparison.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    15810 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/element/graphs.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    13610 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/element/path.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    33144 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/element/raster.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     4184 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/element/stats.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     5927 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/element/tabular.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    10674 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/element/util.py
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/examples/
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/examples/assets/
--rw-r--r--   0 jstevens   (501) wheel        (0)   978004 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/assets/diseases.csv.gz
--rw-r--r--   0 jstevens   (501) wheel        (0)    18624 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/assets/fb_edges.csv
--rw-r--r--   0 jstevens   (501) wheel        (0)    16723 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/assets/fb_nodes.csv
--rw-r--r--   0 jstevens   (501) wheel        (0)   660600 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/assets/hourly_taxi_data.npz
--rw-r--r--   0 jstevens   (501) wheel        (0)   175335 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/assets/penguins.png
--rw-r--r--   0 jstevens   (501) wheel        (0)     2096 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/assets/spike_train.csv.gz
--rw-r--r--   0 jstevens   (501) wheel        (0)     4690 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/assets/station_info.csv
--rw-r--r--   0 jstevens   (501) wheel        (0)   535712 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/assets/twophoton.npz
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/examples/gallery/
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/examples/gallery/apps/
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/examples/gallery/apps/bokeh/
--rw-r--r--   0 jstevens   (501) wheel        (0)     2582 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/apps/bokeh/crossfilter.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     2458 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/apps/bokeh/game_of_life.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     3045 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/apps/bokeh/gapminder.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     2179 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/apps/bokeh/mandelbrot.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     2072 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/apps/bokeh/nytaxi_hover.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     1804 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/apps/bokeh/streaming_psutil.py
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/
--rw-r--r--   0 jstevens   (501) wheel        (0)     1874 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/area_chart.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1261 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/autompg_histogram.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4629 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/bachelors_degrees_by_gender.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1659 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/bars_economic.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1501 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/boxplot_chart.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1779 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/dot_example.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4362 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/dragon_curve.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2136 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/dropdown_economic.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4284 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/histogram_example.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1799 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/iris_density_grid.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1376 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/iris_example.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1892 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/iris_grouped_grid.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1650 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/iris_splom_example.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1869 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/legend_example.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2940 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/lesmis_example.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2000 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/lorenz_attractor_example.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2213 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/mandelbrot_section.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2663 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/measles_example.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1827 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/network_graph.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2221 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/quiver_demo.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1832 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/scatter_economic.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     6061 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/square_limit.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2065 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/step_chart.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2472 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/stocks_example.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1937 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/texas_choropleth_example.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2708 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/topographic_hillshading.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1826 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/us_unemployment.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3793 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/verhulst_mandelbrot.ipynb
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/
--rw-r--r--   0 jstevens   (501) wheel        (0)     1904 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/area_chart.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1243 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/autompg_histogram.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4579 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/bachelors_degrees_by_gender.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1682 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/bars_economic.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1476 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/boxplot_chart.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4383 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/dragon_curve.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2058 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/dropdown_economic.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4245 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/histogram_example.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1768 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/iris_density_grid.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1375 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/iris_example.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1854 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/iris_grouped_grid.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1599 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/iris_splom_example.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1830 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/legend_example.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1993 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/lorenz_attractor_example.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2160 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/mandelbrot_section.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2863 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/measles_example.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1772 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/network_graph.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1355 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/polar_scatter_demo.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2287 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/quiver_demo.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1852 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/scatter_economic.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     6136 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/square_limit.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2026 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/step_chart.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2511 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/stocks_example.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1401 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/surface_3d.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1915 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/texas_choropleth_example.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2729 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/topographic_hillshading.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2141 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/trisurf3d_demo.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1811 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/us_unemployment.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3778 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/verhulst_mandelbrot.ipynb
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/plotly/
--rw-r--r--   0 jstevens   (501) wheel        (0)     1567 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/plotly/surface_3d.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2169 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/gallery/demos/plotly/trisurf3d_demo.ipynb
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/examples/getting_started/
--rw-r--r--   0 jstevens   (501) wheel        (0)    18070 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/getting_started/1-Introduction.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    13692 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/getting_started/2-Customization.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    12141 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/getting_started/3-Tabular_Datasets.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    12520 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/getting_started/4-Gridded_Datasets.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    13473 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/getting_started/5-Live_Data.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1259 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/README.md
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/examples/reference/
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/examples/reference/apps/
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/examples/reference/apps/bokeh/
--rw-r--r--   0 jstevens   (501) wheel        (0)     1436 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/apps/bokeh/player.py
--rw-r--r--   0 jstevens   (501) wheel        (0)      850 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/apps/bokeh/selection_stream.py
--rw-r--r--   0 jstevens   (501) wheel        (0)      589 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/apps/bokeh/sine.py
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/examples/reference/containers/
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/examples/reference/containers/bokeh/
--rw-r--r--   0 jstevens   (501) wheel        (0)     4122 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/containers/bokeh/DynamicMap.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3501 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/containers/bokeh/GridSpace.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     6188 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/containers/bokeh/HoloMap.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2852 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/containers/bokeh/Layout.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4616 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/containers/bokeh/NdLayout.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4458 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/containers/bokeh/NdOverlay.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2764 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/containers/bokeh/Overlay.ipynb
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/examples/reference/containers/matplotlib/
--rw-r--r--   0 jstevens   (501) wheel        (0)     4127 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/containers/matplotlib/DynamicMap.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3478 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/containers/matplotlib/GridSpace.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     6188 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/containers/matplotlib/HoloMap.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2853 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/containers/matplotlib/Layout.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4616 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/containers/matplotlib/NdLayout.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4458 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/containers/matplotlib/NdOverlay.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2763 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/containers/matplotlib/Overlay.ipynb
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/examples/reference/elements/
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/examples/reference/elements/assets/
--rw-r--r--   0 jstevens   (501) wheel        (0)   175335 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/assets/penguins.png
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/
--rw-r--r--   0 jstevens   (501) wheel        (0)     3846 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Area.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2134 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Arrow.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3161 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Bars.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4028 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Bivariate.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2133 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Bounds.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2506 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Box.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2926 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/BoxWhisker.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3081 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Contours.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2791 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Curve.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4326 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Distribution.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2568 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Ellipse.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3065 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/ErrorBars.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     5525 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Graph.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3199 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/HeatMap.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3734 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Histogram.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1557 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/HLine.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2914 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/HSV.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3743 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Image.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1873 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/ItemTable.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4762 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Path.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4662 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Points.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3952 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Polygons.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3979 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/QuadMesh.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1904 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Raster.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3652 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/RGB.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4814 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Scatter.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4314 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Spikes.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1752 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Spline.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3039 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Spread.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3489 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Table.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1412 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Text.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4856 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/VectorField.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1520 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/VLine.ipynb
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/
--rw-r--r--   0 jstevens   (501) wheel        (0)     3851 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Area.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2140 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Arrow.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3238 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Bars.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3981 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Bivariate.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2137 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Bounds.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2509 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Box.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2928 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/BoxWhisker.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3102 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Contours.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2778 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Curve.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4395 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Distribution.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2572 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Ellipse.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3070 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/ErrorBars.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     5513 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Graph.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3130 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/HeatMap.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3773 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Histogram.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1561 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/HLine.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2919 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/HSV.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3748 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Image.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1840 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/ItemTable.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4776 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Path.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4657 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Points.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3901 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Polygons.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3266 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/QuadMesh.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1908 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Raster.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3657 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/RGB.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4819 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Scatter.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2279 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Scatter3D.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4304 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Spikes.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1804 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Spline.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3027 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Spread.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2696 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Surface.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3403 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Table.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1417 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Text.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2562 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/TriSurface.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     5292 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/VectorField.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1524 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/VLine.ipynb
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/examples/reference/elements/plotly/
--rw-r--r--   0 jstevens   (501) wheel        (0)     2596 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/plotly/BoxWhiskers.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2774 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/plotly/Curve.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1987 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/plotly/Distribution.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3122 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/plotly/ErrorBars.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3237 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/plotly/HeatMap.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3549 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/plotly/Image.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1892 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/plotly/ItemTable.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4677 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/plotly/Points.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1957 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/plotly/Raster.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     4838 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/plotly/Scatter.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2333 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/plotly/Scatter3D.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2573 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/plotly/Surface.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3460 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/plotly/Table.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2598 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/elements/plotly/TriSurface.ipynb
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/examples/reference/features/
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/examples/reference/features/bokeh/
--rw-r--r--   0 jstevens   (501) wheel        (0)     1675 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/features/bokeh/table_hooks_example.ipynb
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/examples/reference/streams/
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/examples/reference/streams/bokeh/
--rw-r--r--   0 jstevens   (501) wheel        (0)     2756 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/streams/bokeh/Bounds.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1797 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/streams/bokeh/BoundsX.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2032 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/streams/bokeh/BoundsY.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2098 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/streams/bokeh/PointerX.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1925 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/streams/bokeh/PointerXY.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1917 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/streams/bokeh/RangeXY.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     1565 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/streams/bokeh/Selection1D.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2277 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/streams/bokeh/Selection1D_paired.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2149 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/streams/bokeh/Selection1D_points.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     3258 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/streams/bokeh/Selection1D_tap.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2723 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/reference/streams/bokeh/Tap.ipynb
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/examples/topics/
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/examples/topics/geometry/
--rw-r--r--   0 jstevens   (501) wheel        (0)    15860 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/topics/geometry/lsystems.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    10960 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/topics/geometry/square_limit.ipynb
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/examples/topics/simulation/
--rw-r--r--   0 jstevens   (501) wheel        (0)     9738 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/topics/simulation/boids.ipynb
--rwxr-xr-x   0 jstevens   (501) wheel        (0)    13977 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/topics/simulation/hipster_dynamics.ipynb
--rwxr-xr-x   0 jstevens   (501) wheel        (0)    28641 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/topics/simulation/sri_model.ipynb
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/examples/user_guide/
--rw-r--r--   0 jstevens   (501) wheel        (0)    12341 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/user_guide/01-Annotating_Data.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    14136 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/user_guide/02-Composing_Elements.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    21529 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/user_guide/03-Customizing_Plots.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    12295 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/user_guide/04-Dimensioned_Containers.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    16424 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/user_guide/05-Building_Composite_Objects.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    29485 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/user_guide/06-Live_Data.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    22018 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/user_guide/07-Tabular_Datasets.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    11996 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/user_guide/08-Gridded_Datasets.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    18763 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/user_guide/09-Indexing_and_Selecting_Data.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    22088 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/user_guide/10-Transforming_Elements.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    29588 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/user_guide/11-Responding_to_Events.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    19594 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/user_guide/12-Custom_Interactivity.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     8512 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/user_guide/13-Data_Pipelines.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    19182 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/examples/user_guide/14-Large_Data.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    25079 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/user_guide/15-Streaming_Data.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     7880 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/user_guide/16-Dashboards.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    15196 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/user_guide/Continuous_Coordinates.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    22354 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/user_guide/Deploying_Bokeh_Apps.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    26456 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/user_guide/Exporting_and_Archiving.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     6099 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/examples/user_guide/Installing_and_Configuring.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    12659 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/user_guide/Network_Graphs.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    18793 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/user_guide/Plots_and_Renderers.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)    18463 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/examples/user_guide/Plotting_with_Bokeh.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     6140 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/user_guide/Plotting_with_Matplotlib.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)     2603 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/examples/user_guide/Tips_and_Tricks.ipynb
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/ipython/
--rw-r--r--   0 jstevens   (501) wheel        (0)     9866 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/ipython/__init__.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    12249 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/ipython/archive.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    10610 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/ipython/display_hooks.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    13605 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/ipython/load_notebook.html
--rw-r--r--   0 jstevens   (501) wheel        (0)    15787 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/ipython/magics.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     7474 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/ipython/preprocessors.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     8646 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/ipython/widgets.py
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/operation/
--rw-r--r--   0 jstevens   (501) wheel        (0)      730 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/operation/__init__.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    36179 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/operation/datashader.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    31868 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/operation/element.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     6595 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/operation/normalization.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     9674 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/operation/stats.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     4593 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/operation/timeseries.py
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/plotting/
--rw-r--r--   0 jstevens   (501) wheel        (0)     1277 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/__init__.py
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/plotting/bokeh/
--rw-r--r--   0 jstevens   (501) wheel        (0)     9062 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/plotting/bokeh/__init__.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     6954 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/bokeh/annotation.py
--rw-r--r--   0 jstevens   (501) wheel        (0)      165 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/bokeh/bokehwidgets.css
--rw-r--r--   0 jstevens   (501) wheel        (0)     1042 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/bokeh/bokehwidgets.js
--rw-r--r--   0 jstevens   (501) wheel        (0)    30115 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/plotting/bokeh/callbacks.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    46368 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/plotting/bokeh/chart.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    62281 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/plotting/bokeh/element.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    11065 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/plotting/bokeh/graphs.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     7341 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/bokeh/path.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    35219 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/plotting/bokeh/plot.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     7490 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/plotting/bokeh/raster.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    11448 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/plotting/bokeh/renderer.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     1154 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/plotting/bokeh/stats.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     5064 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/plotting/bokeh/tabular.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    20733 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/plotting/bokeh/util.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    11556 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/bokeh/widgets.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     6280 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/comms.py
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/plotting/mpl/
--rw-r--r--   0 jstevens   (501) wheel        (0)    10573 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/plotting/mpl/__init__.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     4359 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/mpl/annotation.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    41985 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/plotting/mpl/chart.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     7570 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/mpl/chart3d.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     2598 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/mpl/comms.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     1030 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/mpl/default.mplstyle
--rw-r--r--   0 jstevens   (501) wheel        (0)     1058 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/mpl/default1.5.mplstyle
--rw-r--r--   0 jstevens   (501) wheel        (0)    36750 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/mpl/element.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     6624 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/plotting/mpl/graphs.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     1330 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/mpl/mplwidgets.js
--rw-r--r--   0 jstevens   (501) wheel        (0)     4652 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/mpl/path.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    47648 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/mpl/plot.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    16596 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/plotting/mpl/raster.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    10743 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/mpl/renderer.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     1154 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/plotting/mpl/stats.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     5240 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/mpl/tabular.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     6075 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/mpl/util.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     1669 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/mpl/widgets.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    43149 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/plot.py
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/plotting/plotly/
--rw-r--r--   0 jstevens   (501) wheel        (0)     2609 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/plotly/__init__.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     8139 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/plotly/chart.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     3895 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/plotly/chart3d.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     9535 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/plotly/element.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    15858 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/plotly/plot.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     1248 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/plotly/plotlywidgets.js
--rw-r--r--   0 jstevens   (501) wheel        (0)     1724 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/plotly/raster.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     5713 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/plotly/renderer.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     1002 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/plotly/tabular.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     1098 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/plotly/util.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     1248 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/plotly/widgets.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    20342 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/plotting/renderer.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    32276 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/util.py
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/plotting/widgets/
--rw-r--r--   0 jstevens   (501) wheel        (0)    15651 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/widgets/__init__.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     2345 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/widgets/jsscrubber.jinja
--rw-r--r--   0 jstevens   (501) wheel        (0)      996 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/widgets/jsslider.css
--rw-r--r--   0 jstevens   (501) wheel        (0)     9912 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/widgets/jsslider.jinja
--rw-r--r--   0 jstevens   (501) wheel        (0)     9308 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/plotting/widgets/widgets.js
--rw-r--r--   0 jstevens   (501) wheel        (0)    28544 2018-02-16 15:51:52.000000 holoviews-1.9.4/holoviews/streams.py
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews/util/
--rw-r--r--   0 jstevens   (501) wheel        (0)    14495 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/util/__init__.py
--rwxr-xr-x   0 jstevens   (501) wheel        (0)     3137 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/util/command.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    17156 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/util/parser.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    15783 2018-02-16 15:51:14.000000 holoviews-1.9.4/holoviews/util/settings.py
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews.egg-info/
--rw-r--r--   0 jstevens   (501) wheel        (0)        1 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews.egg-info/dependency_links.txt
--rw-r--r--   0 jstevens   (501) wheel        (0)       59 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews.egg-info/entry_points.txt
--rw-r--r--   0 jstevens   (501) wheel        (0)     1237 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews.egg-info/PKG-INFO
--rw-r--r--   0 jstevens   (501) wheel        (0)      519 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews.egg-info/requires.txt
--rw-r--r--   0 jstevens   (501) wheel        (0)    32369 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews.egg-info/SOURCES.txt
--rw-r--r--   0 jstevens   (501) wheel        (0)       10 2018-02-16 16:52:31.000000 holoviews-1.9.4/holoviews.egg-info/top_level.txt
--rw-r--r--   0 jstevens   (501) wheel        (0)     1499 2018-02-16 15:51:14.000000 holoviews-1.9.4/LICENSE.txt
--rw-r--r--   0 jstevens   (501) wheel        (0)      412 2018-02-16 15:51:14.000000 holoviews-1.9.4/MANIFEST.in
--rw-r--r--   0 jstevens   (501) wheel        (0)     1237 2018-02-16 16:52:32.000000 holoviews-1.9.4/PKG-INFO
--rw-r--r--   0 jstevens   (501) wheel        (0)       59 2018-02-16 16:52:32.000000 holoviews-1.9.4/setup.cfg
--rw-r--r--   0 jstevens   (501) wheel        (0)     6906 2018-02-16 16:09:29.000000 holoviews-1.9.4/setup.py
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:32.000000 holoviews-1.9.4/tests/
--rw-r--r--   0 jstevens   (501) wheel        (0)     3840 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/__init__.py
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:32.000000 holoviews-1.9.4/tests/notebooks/
--rw-r--r--   0 jstevens   (501) wheel        (0)      361 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/notebooks/test_opts_image_cell_magic.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)      404 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/notebooks/test_opts_image_cell_magic_offset.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)      319 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/notebooks/test_opts_image_line_magic.ipynb
--rw-r--r--   0 jstevens   (501) wheel        (0)      295 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/notebooks/test_output_svg_line_magic.ipynb
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:32.000000 holoviews-1.9.4/tests/operation/
--rw-r--r--   0 jstevens   (501) wheel        (0)        0 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/operation/__init__.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    12575 2018-02-16 15:51:52.000000 holoviews-1.9.4/tests/operation/testdatashader.py
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:32.000000 holoviews-1.9.4/tests/plotting/
--rw-r--r--   0 jstevens   (501) wheel        (0)        0 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/plotting/__init__.py
-drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-02-16 16:52:32.000000 holoviews-1.9.4/tests/plotting/bokeh/
--rw-r--r--   0 jstevens   (501) wheel        (0)        0 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/plotting/bokeh/__init__.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     5807 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/plotting/bokeh/testserver.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     2165 2018-02-16 15:51:52.000000 holoviews-1.9.4/tests/plotting/bokeh/testtabular.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    21869 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/plotting/testplotutils.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     2007 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/testaliases.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     2160 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/testannotations.py
--rw-r--r--   0 jstevens   (501) wheel        (0)      985 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/testapiconsistency.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     5316 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/testarchives.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     3928 2018-02-16 15:51:52.000000 holoviews-1.9.4/tests/testbokehcallbacks.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     8557 2018-02-16 15:51:52.000000 holoviews-1.9.4/tests/testbokehgraphs.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     3687 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/testbokehutils.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     7291 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/testbokehwidgets.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     2356 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/testboundingregion.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    12914 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/testcallable.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     3718 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/testcollation.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     2242 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/testcomms.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     7557 2018-02-16 15:51:52.000000 holoviews-1.9.4/tests/testcomparisonchart.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     4823 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/testcomparisoncomposite.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     7517 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/testcomparisondimension.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     3440 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/testcomparisonpath.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     6350 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/testcomparisonraster.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     3976 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/testcomparisonsimple.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    16402 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/testcomposites.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    23470 2018-02-16 15:51:52.000000 holoviews-1.9.4/tests/testcoreutils.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    73135 2018-02-16 15:51:52.000000 holoviews-1.9.4/tests/testdataset.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    10553 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/testdimensions.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     3695 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/testdimselect.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    32714 2018-02-16 15:51:52.000000 holoviews-1.9.4/tests/testdynamic.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     7557 2018-02-16 15:51:52.000000 holoviews-1.9.4/tests/testelementconstructors.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     5207 2018-02-16 15:51:52.000000 holoviews-1.9.4/tests/testelementindexing.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     3519 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/testelementranges.py
--rw-r--r--   0 jstevens   (501) wheel        (0)      789 2018-02-16 15:51:52.000000 holoviews-1.9.4/tests/testelementutils.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     5344 2018-02-16 15:51:52.000000 holoviews-1.9.4/tests/testellipsis.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     5561 2018-02-16 15:51:52.000000 holoviews-1.9.4/tests/testgraphelement.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    26935 2018-02-16 15:51:52.000000 holoviews-1.9.4/tests/testimageinterfaces.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     7744 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/testimportexport.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     4179 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/testirisinterface.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     1243 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/testlayers.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     5123 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/testlayouts.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     7219 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/testmagics.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     4454 2018-02-16 15:51:52.000000 holoviews-1.9.4/tests/testmplgraphs.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     5925 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/testmultiinterface.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    10776 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/testndmapping.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     3041 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/testnotebooks.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     7916 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/testoperation.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    28828 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/testoptions.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     5406 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/testoptscompleter.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    11792 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/testparsers.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     3050 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/testpaths.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    90959 2018-02-16 15:51:52.000000 holoviews-1.9.4/tests/testplotinstantiation.py
--rw-r--r--   0 jstevens   (501) wheel        (0)      987 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/testprettyprint.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     2513 2018-02-16 15:51:52.000000 holoviews-1.9.4/tests/testraster.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     5644 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/testrenderclass.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     8621 2018-02-16 15:51:52.000000 holoviews-1.9.4/tests/teststatselements.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     2098 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/teststatsoperations.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     3951 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/teststoreoptions.py
--rw-r--r--   0 jstevens   (501) wheel        (0)    17918 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/teststreams.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     3105 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/testtimeseriesoperations.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     3388 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/testtraversal.py
--rw-r--r--   0 jstevens   (501) wheel        (0)     4181 2018-02-16 15:51:14.000000 holoviews-1.9.4/tests/testutils.py
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/
+-rw-r--r--   0 jstevens   (501) wheel        (0)    65589 2018-03-02 12:29:25.000000 holoviews-1.9.5/CHANGELOG.md
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:25.000000 holoviews-1.9.5/doc/
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:25.000000 holoviews-1.9.5/doc/_static/
+-rw-r--r--   0 jstevens   (501) wheel        (0)    15086 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/_static/favicon.ico
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4278 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/_static/holoviews_logo.png
+-rw-r--r--   0 jstevens   (501) wheel        (0)      651 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/_static/rtd_bootstrap.css
+-rw-r--r--   0 jstevens   (501) wheel        (0)      819 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/about.rst
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:25.000000 holoviews-1.9.5/doc/assets/
+-rw-r--r--   0 jstevens   (501) wheel        (0)   338681 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/assets/macaw.png
+-rw-r--r--   0 jstevens   (501) wheel        (0)  1046222 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/assets/nesting-diagram.svg
+-rw-r--r--   0 jstevens   (501) wheel        (0)   175335 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/assets/penguins.png
+-rw-r--r--   0 jstevens   (501) wheel        (0)      337 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/assets/README.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)     5250 2018-03-02 12:16:24.000000 holoviews-1.9.5/doc/conf.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     7101 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/FAQ.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4158 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/features.rst
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:25.000000 holoviews-1.9.5/doc/getting_started/
+-rw-r--r--   0 jstevens   (501) wheel        (0)      121 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/getting_started/Customization.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)      130 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/getting_started/Gridded_Datasets.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1457 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/getting_started/index.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)      118 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/getting_started/Introduction.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)      204 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/getting_started/Live_Data.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)      130 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/getting_started/Tabular_Datasets.rst
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:25.000000 holoviews-1.9.5/doc/holoviews_theme/
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:25.000000 holoviews-1.9.5/doc/holoviews_theme/includes/
+-rw-r--r--   0 jstevens   (501) wheel        (0)      409 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/holoviews_theme/includes/ga.html
+-rw-r--r--   0 jstevens   (501) wheel        (0)      341 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/holoviews_theme/includes/searchbox.html
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4751 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/holoviews_theme/layout.html
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1399 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/holoviews_theme/search.html
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:25.000000 holoviews-1.9.5/doc/holoviews_theme/static/
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:25.000000 holoviews-1.9.5/doc/holoviews_theme/static/images/
+-rw-r--r--   0 jstevens   (501) wheel        (0)     6139 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/holoviews_theme/static/images/favicon.ico
+-rw-r--r--   0 jstevens   (501) wheel        (0)    17919 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/holoviews_theme/static/images/logo.png
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4386 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/holoviews_theme/static/images/logo.svg
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:25.000000 holoviews-1.9.5/doc/holoviews_theme/static/js/
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2188 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/holoviews_theme/static/js/main.js
+-rw-r--r--   0 jstevens   (501) wheel        (0)       99 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/holoviews_theme/theme.conf
+-rw-r--r--   0 jstevens   (501) wheel        (0)     7007 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/Homepage.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     5669 2018-03-02 12:16:24.000000 holoviews-1.9.5/doc/index.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2591 2018-03-02 12:16:24.000000 holoviews-1.9.5/doc/install.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)      319 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/latest_news.html
+-rw-r--r--   0 jstevens   (501) wheel        (0)      163 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/Makefile
+-rw-r--r--   0 jstevens   (501) wheel        (0)  1280080 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/mandelbrot.npy
+-rw-r--r--   0 jstevens   (501) wheel        (0)       63 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/notebook.json
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:25.000000 holoviews-1.9.5/doc/Reference_Manual/
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2409 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/Reference_Manual/index.rst
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:25.000000 holoviews-1.9.5/doc/showcase/
+-rw-r--r--   0 jstevens   (501) wheel        (0)       97 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/showcase/boids.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)      130 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/showcase/hipster_dynamics.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3152 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/showcase/index.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)      106 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/showcase/lsystems.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)      116 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/showcase/square_limit.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)      135 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/showcase/sri_model.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)      149 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/site_map.rst
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:25.000000 holoviews-1.9.5/doc/test_data/
+-rw-r--r--   0 jstevens   (501) wheel        (0)      231 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/test_data/README.rst
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:25.000000 holoviews-1.9.5/doc/Tutorials/
+-rw-r--r--   0 jstevens   (501) wheel        (0)    17298 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/Tutorials/Bokeh_Backend.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    54084 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/Tutorials/Bokeh_Elements.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    35575 2018-03-02 12:16:24.000000 holoviews-1.9.5/doc/Tutorials/Columnar_Data.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    16108 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/Tutorials/Composing_Data.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    22811 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/Tutorials/Containers.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    14967 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/Tutorials/Continuous_Coordinates.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    29346 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/Tutorials/Dynamic_Map.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    54557 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/Tutorials/Elements.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    24754 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/Tutorials/Exploring_Data.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    25741 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/Tutorials/Exporting.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4322 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/Tutorials/index.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)    32364 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/Tutorials/Introduction.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    16793 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/Tutorials/Linked_Streams.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    16872 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/Tutorials/Operations.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    33130 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/Tutorials/Options.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    12227 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/Tutorials/Pandas_Seaborn.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    23789 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/Tutorials/Rich_Display.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    15916 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/Tutorials/Sampling_Data.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    24755 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/Tutorials/Showcase.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    28850 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/Tutorials/Streams.ipynb
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:25.000000 holoviews-1.9.5/doc/user_guide/
+-rw-r--r--   0 jstevens   (501) wheel        (0)      133 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/user_guide/Annotating_Data.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)      156 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/user_guide/Building_Composite_Objects.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)      133 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/user_guide/Composing_Elements.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)      141 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/user_guide/Continuous_Coordinates.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)      162 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/user_guide/Custom_Interactivity.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)      129 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/user_guide/Customizing_Plots.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)      174 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/user_guide/Dashboards.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)      142 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/user_guide/Data_Pipelines.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)      159 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/user_guide/Deploying_Bokeh_Apps.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)      145 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/user_guide/Dimensioned_Containers.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)      144 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/user_guide/Exporting_and_Archiving.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)      126 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/user_guide/Gridded_Datasets.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)     5560 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/user_guide/index.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)      159 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/user_guide/Indexing_and_Selecting_Data.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)      173 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/user_guide/Installing_and_Configuring.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)       30 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/user_guide/IPython_Magics.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)      168 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/user_guide/Large_Data.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)      105 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/user_guide/Live_Data.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)      156 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/user_guide/Plots_and_Renderers.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)      132 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/user_guide/Plotting_with_Bokeh.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)       50 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/user_guide/Plotting_with_Matplotlib.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)      138 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/user_guide/Responding_to_Events.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)      170 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/user_guide/Streaming_Data.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)      126 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/user_guide/Tabular_Datasets.rst
+-rw-r--r--   0 jstevens   (501) wheel        (0)      141 2018-03-02 12:12:30.000000 holoviews-1.9.5/doc/user_guide/Transforming_Elements.rst
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:25.000000 holoviews-1.9.5/examples/
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:25.000000 holoviews-1.9.5/examples/assets/
+-rw-r--r--   0 jstevens   (501) wheel        (0)   978004 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/assets/diseases.csv.gz
+-rw-r--r--   0 jstevens   (501) wheel        (0)    18624 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/assets/fb_edges.csv
+-rw-r--r--   0 jstevens   (501) wheel        (0)    16723 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/assets/fb_nodes.csv
+-rw-r--r--   0 jstevens   (501) wheel        (0)   660600 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/assets/hourly_taxi_data.npz
+-rw-r--r--   0 jstevens   (501) wheel        (0)   175335 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/assets/penguins.png
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2096 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/assets/spike_train.csv.gz
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4690 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/assets/station_info.csv
+-rw-r--r--   0 jstevens   (501) wheel        (0)   535712 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/assets/twophoton.npz
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:25.000000 holoviews-1.9.5/examples/gallery/
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:25.000000 holoviews-1.9.5/examples/gallery/demos/
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:25.000000 holoviews-1.9.5/examples/gallery/demos/bokeh/
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1874 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/bokeh/area_chart.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1261 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/bokeh/autompg_histogram.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4629 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/bokeh/bachelors_degrees_by_gender.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1659 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/bokeh/bars_economic.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1501 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/bokeh/boxplot_chart.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1779 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/bokeh/dot_example.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4362 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/bokeh/dragon_curve.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2136 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/bokeh/dropdown_economic.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4284 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/bokeh/histogram_example.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1799 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/bokeh/iris_density_grid.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1376 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/bokeh/iris_example.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1892 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/bokeh/iris_grouped_grid.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1650 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/bokeh/iris_splom_example.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1869 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/bokeh/legend_example.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2940 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/bokeh/lesmis_example.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2000 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/bokeh/lorenz_attractor_example.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2213 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/bokeh/mandelbrot_section.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2663 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/bokeh/measles_example.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1827 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/bokeh/network_graph.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2221 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/bokeh/quiver_demo.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1832 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/bokeh/scatter_economic.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     6061 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/bokeh/square_limit.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2065 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/bokeh/step_chart.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2472 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/bokeh/stocks_example.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1937 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/bokeh/texas_choropleth_example.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2708 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/bokeh/topographic_hillshading.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1826 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/bokeh/us_unemployment.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3793 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/bokeh/verhulst_mandelbrot.ipynb
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/examples/gallery/demos/matplotlib/
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1904 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/matplotlib/area_chart.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1243 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/matplotlib/autompg_histogram.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4579 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/matplotlib/bachelors_degrees_by_gender.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1682 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/matplotlib/bars_economic.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1476 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/matplotlib/boxplot_chart.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4383 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/matplotlib/dragon_curve.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2058 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/matplotlib/dropdown_economic.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4245 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/matplotlib/histogram_example.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1768 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/matplotlib/iris_density_grid.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1375 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/matplotlib/iris_example.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1854 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/matplotlib/iris_grouped_grid.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1599 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/matplotlib/iris_splom_example.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1830 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/matplotlib/legend_example.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1993 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/matplotlib/lorenz_attractor_example.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2160 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/matplotlib/mandelbrot_section.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2863 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/matplotlib/measles_example.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1772 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/matplotlib/network_graph.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1355 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/matplotlib/polar_scatter_demo.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2287 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/matplotlib/quiver_demo.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1852 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/matplotlib/scatter_economic.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     6136 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/matplotlib/square_limit.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2026 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/matplotlib/step_chart.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2511 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/matplotlib/stocks_example.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1401 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/matplotlib/surface_3d.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1915 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/matplotlib/texas_choropleth_example.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2729 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/matplotlib/topographic_hillshading.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2141 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/matplotlib/trisurf3d_demo.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1811 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/matplotlib/us_unemployment.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3778 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/matplotlib/verhulst_mandelbrot.ipynb
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/examples/gallery/demos/plotly/
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1567 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/plotly/surface_3d.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2169 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/gallery/demos/plotly/trisurf3d_demo.ipynb
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/examples/getting_started/
+-rw-r--r--   0 jstevens   (501) wheel        (0)    18070 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/getting_started/1-Introduction.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    15769 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/getting_started/2-Customization.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    12141 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/getting_started/3-Tabular_Datasets.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    12520 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/getting_started/4-Gridded_Datasets.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    13473 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/getting_started/5-Live_Data.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1259 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/README.md
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:25.000000 holoviews-1.9.5/examples/reference/
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:25.000000 holoviews-1.9.5/examples/reference/containers/
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/examples/reference/containers/bokeh/
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4122 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/containers/bokeh/DynamicMap.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3501 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/containers/bokeh/GridSpace.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     6188 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/containers/bokeh/HoloMap.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2852 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/containers/bokeh/Layout.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4616 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/containers/bokeh/NdLayout.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4458 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/containers/bokeh/NdOverlay.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2764 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/containers/bokeh/Overlay.ipynb
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/examples/reference/containers/matplotlib/
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4127 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/containers/matplotlib/DynamicMap.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3478 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/containers/matplotlib/GridSpace.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     6188 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/containers/matplotlib/HoloMap.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2853 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/containers/matplotlib/Layout.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4616 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/containers/matplotlib/NdLayout.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4458 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/containers/matplotlib/NdOverlay.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2763 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/containers/matplotlib/Overlay.ipynb
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:25.000000 holoviews-1.9.5/examples/reference/elements/
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/examples/reference/elements/assets/
+-rw-r--r--   0 jstevens   (501) wheel        (0)   175335 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/assets/penguins.png
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/examples/reference/elements/bokeh/
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3846 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/bokeh/Area.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2134 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/bokeh/Arrow.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3161 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/bokeh/Bars.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4028 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/bokeh/Bivariate.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2133 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/bokeh/Bounds.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2506 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/bokeh/Box.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2926 2018-03-02 12:16:24.000000 holoviews-1.9.5/examples/reference/elements/bokeh/BoxWhisker.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3081 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/bokeh/Contours.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2791 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/bokeh/Curve.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4326 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/bokeh/Distribution.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2568 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/bokeh/Ellipse.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3065 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/bokeh/ErrorBars.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     5525 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/bokeh/Graph.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3199 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/bokeh/HeatMap.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3734 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/bokeh/Histogram.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1557 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/bokeh/HLine.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2914 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/bokeh/HSV.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3743 2018-03-02 12:16:24.000000 holoviews-1.9.5/examples/reference/elements/bokeh/Image.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1873 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/bokeh/ItemTable.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4762 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/bokeh/Path.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4662 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/bokeh/Points.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3952 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/bokeh/Polygons.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3979 2018-03-02 12:16:24.000000 holoviews-1.9.5/examples/reference/elements/bokeh/QuadMesh.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1904 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/bokeh/Raster.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3652 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/bokeh/RGB.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4814 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/bokeh/Scatter.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4314 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/bokeh/Spikes.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1752 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/bokeh/Spline.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3039 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/bokeh/Spread.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3489 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/bokeh/Table.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1412 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/bokeh/Text.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4856 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/bokeh/VectorField.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1520 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/bokeh/VLine.ipynb
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/examples/reference/elements/matplotlib/
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3851 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/matplotlib/Area.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2140 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/matplotlib/Arrow.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3238 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/matplotlib/Bars.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3981 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/matplotlib/Bivariate.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2137 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/matplotlib/Bounds.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2509 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/matplotlib/Box.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2928 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/matplotlib/BoxWhisker.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3102 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/matplotlib/Contours.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2778 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/matplotlib/Curve.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4395 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/matplotlib/Distribution.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2572 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/matplotlib/Ellipse.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3070 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/matplotlib/ErrorBars.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     5513 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/matplotlib/Graph.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3130 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/matplotlib/HeatMap.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3773 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/matplotlib/Histogram.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1561 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/matplotlib/HLine.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2919 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/matplotlib/HSV.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3748 2018-03-02 12:16:24.000000 holoviews-1.9.5/examples/reference/elements/matplotlib/Image.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1840 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/matplotlib/ItemTable.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4776 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/matplotlib/Path.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4657 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/matplotlib/Points.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3901 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/matplotlib/Polygons.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3266 2018-03-02 12:16:24.000000 holoviews-1.9.5/examples/reference/elements/matplotlib/QuadMesh.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1908 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/matplotlib/Raster.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3657 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/matplotlib/RGB.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4819 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/matplotlib/Scatter.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2279 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/matplotlib/Scatter3D.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4304 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/matplotlib/Spikes.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1804 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/matplotlib/Spline.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3027 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/matplotlib/Spread.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2696 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/matplotlib/Surface.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3403 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/matplotlib/Table.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1417 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/matplotlib/Text.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2562 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/matplotlib/TriSurface.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     5292 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/matplotlib/VectorField.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1524 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/matplotlib/VLine.ipynb
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/examples/reference/elements/plotly/
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2596 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/plotly/BoxWhiskers.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2774 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/plotly/Curve.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1987 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/plotly/Distribution.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3122 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/plotly/ErrorBars.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3237 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/plotly/HeatMap.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3549 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/plotly/Image.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1892 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/plotly/ItemTable.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4677 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/plotly/Points.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1957 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/plotly/Raster.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4838 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/plotly/Scatter.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2333 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/plotly/Scatter3D.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2573 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/plotly/Surface.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3460 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/plotly/Table.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2598 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/elements/plotly/TriSurface.ipynb
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:25.000000 holoviews-1.9.5/examples/reference/features/
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/examples/reference/features/bokeh/
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1675 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/features/bokeh/table_hooks_example.ipynb
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:25.000000 holoviews-1.9.5/examples/reference/streams/
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/examples/reference/streams/bokeh/
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2756 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/streams/bokeh/Bounds.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1797 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/streams/bokeh/BoundsX.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2032 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/streams/bokeh/BoundsY.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2098 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/streams/bokeh/PointerX.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1925 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/streams/bokeh/PointerXY.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1917 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/streams/bokeh/RangeXY.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1565 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/streams/bokeh/Selection1D.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2277 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/streams/bokeh/Selection1D_paired.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2149 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/streams/bokeh/Selection1D_points.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3258 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/streams/bokeh/Selection1D_tap.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2723 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/reference/streams/bokeh/Tap.ipynb
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:25.000000 holoviews-1.9.5/examples/topics/
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/examples/topics/geometry/
+-rw-r--r--   0 jstevens   (501) wheel        (0)    15860 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/topics/geometry/lsystems.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    10960 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/topics/geometry/square_limit.ipynb
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/examples/topics/simulation/
+-rw-r--r--   0 jstevens   (501) wheel        (0)     9738 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/topics/simulation/boids.ipynb
+-rwxr-xr-x   0 jstevens   (501) wheel        (0)    13977 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/topics/simulation/hipster_dynamics.ipynb
+-rwxr-xr-x   0 jstevens   (501) wheel        (0)    28641 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/topics/simulation/sri_model.ipynb
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/examples/user_guide/
+-rw-r--r--   0 jstevens   (501) wheel        (0)    12341 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/user_guide/01-Annotating_Data.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    14136 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/user_guide/02-Composing_Elements.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    23190 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/user_guide/03-Customizing_Plots.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    12295 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/user_guide/04-Dimensioned_Containers.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    16424 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/user_guide/05-Building_Composite_Objects.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    29485 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/user_guide/06-Live_Data.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    22018 2018-03-02 12:16:24.000000 holoviews-1.9.5/examples/user_guide/07-Tabular_Datasets.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    11996 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/user_guide/08-Gridded_Datasets.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    18763 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/user_guide/09-Indexing_and_Selecting_Data.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    22088 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/user_guide/10-Transforming_Elements.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    29588 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/user_guide/11-Responding_to_Events.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    19594 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/user_guide/12-Custom_Interactivity.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     8512 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/user_guide/13-Data_Pipelines.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    19182 2018-03-02 12:16:24.000000 holoviews-1.9.5/examples/user_guide/14-Large_Data.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    25079 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/user_guide/15-Streaming_Data.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     7880 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/user_guide/16-Dashboards.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    15196 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/user_guide/Continuous_Coordinates.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    22354 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/user_guide/Deploying_Bokeh_Apps.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    26456 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/user_guide/Exporting_and_Archiving.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     6099 2018-03-02 12:16:24.000000 holoviews-1.9.5/examples/user_guide/Installing_and_Configuring.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    12659 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/user_guide/Network_Graphs.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    18793 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/user_guide/Plots_and_Renderers.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    18463 2018-03-02 12:16:24.000000 holoviews-1.9.5/examples/user_guide/Plotting_with_Bokeh.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     6140 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/user_guide/Plotting_with_Matplotlib.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2603 2018-03-02 12:12:30.000000 holoviews-1.9.5/examples/user_guide/Tips_and_Tricks.ipynb
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/holoviews/
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3808 2018-03-02 12:32:55.000000 holoviews-1.9.5/holoviews/__init__.py
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/holoviews/core/
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1828 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/core/__init__.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    10528 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/core/boundingregion.py
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/holoviews/core/data/
+-rw-r--r--   0 jstevens   (501) wheel        (0)    26340 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/core/data/__init__.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     9405 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/core/data/array.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     9893 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/core/data/dask.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    14076 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/core/data/dictionary.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    17850 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/core/data/grid.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    10717 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/core/data/image.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    12513 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/core/data/interface.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    11740 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/core/data/iris.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     8669 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/core/data/multipath.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    11451 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/core/data/pandas.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    13871 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/core/data/xarray.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    50101 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/core/dimension.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    15012 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/core/element.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    33790 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/core/io.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    18417 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/core/layout.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    31988 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/core/ndmapping.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     8111 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/core/operation.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    64759 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/core/options.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     8816 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/core/overlay.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    15136 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/core/pprint.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    20510 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/core/sheetcoords.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    64515 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/core/spaces.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     5152 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/core/traversal.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     9886 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/core/tree.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    56309 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/core/util.py
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/holoviews/element/
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4121 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/element/__init__.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     9535 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/element/annotation.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    15384 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/element/chart.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2939 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/element/chart3d.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    25981 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/element/comparison.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    15810 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/element/graphs.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    13610 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/element/path.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    33144 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/element/raster.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4184 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/element/stats.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     5927 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/element/tabular.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    10674 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/element/util.py
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/holoviews/examples/
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/holoviews/examples/assets/
+-rw-r--r--   0 jstevens   (501) wheel        (0)   978004 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/assets/diseases.csv.gz
+-rw-r--r--   0 jstevens   (501) wheel        (0)    18624 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/assets/fb_edges.csv
+-rw-r--r--   0 jstevens   (501) wheel        (0)    16723 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/assets/fb_nodes.csv
+-rw-r--r--   0 jstevens   (501) wheel        (0)   660600 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/assets/hourly_taxi_data.npz
+-rw-r--r--   0 jstevens   (501) wheel        (0)   175335 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/assets/penguins.png
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2096 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/assets/spike_train.csv.gz
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4690 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/assets/station_info.csv
+-rw-r--r--   0 jstevens   (501) wheel        (0)   535712 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/assets/twophoton.npz
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:25.000000 holoviews-1.9.5/holoviews/examples/gallery/
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:25.000000 holoviews-1.9.5/holoviews/examples/gallery/apps/
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/holoviews/examples/gallery/apps/bokeh/
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2582 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/apps/bokeh/crossfilter.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2458 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/apps/bokeh/game_of_life.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3045 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/apps/bokeh/gapminder.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2179 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/apps/bokeh/mandelbrot.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2072 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/apps/bokeh/nytaxi_hover.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1804 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/apps/bokeh/streaming_psutil.py
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:25.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1874 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/area_chart.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1261 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/autompg_histogram.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4629 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/bachelors_degrees_by_gender.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1659 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/bars_economic.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1501 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/boxplot_chart.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1779 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/dot_example.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4362 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/dragon_curve.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2136 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/dropdown_economic.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4284 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/histogram_example.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1799 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/iris_density_grid.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1376 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/iris_example.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1892 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/iris_grouped_grid.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1650 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/iris_splom_example.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1869 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/legend_example.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2940 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/lesmis_example.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2000 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/lorenz_attractor_example.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2213 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/mandelbrot_section.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2663 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/measles_example.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1827 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/network_graph.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2221 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/quiver_demo.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1832 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/scatter_economic.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     6061 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/square_limit.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2065 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/step_chart.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2472 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/stocks_example.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1937 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/texas_choropleth_example.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2708 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/topographic_hillshading.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1826 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/us_unemployment.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3793 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/verhulst_mandelbrot.ipynb
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1904 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/area_chart.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1243 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/autompg_histogram.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4579 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/bachelors_degrees_by_gender.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1682 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/bars_economic.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1476 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/boxplot_chart.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4383 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/dragon_curve.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2058 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/dropdown_economic.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4245 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/histogram_example.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1768 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/iris_density_grid.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1375 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/iris_example.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1854 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/iris_grouped_grid.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1599 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/iris_splom_example.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1830 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/legend_example.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1993 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/lorenz_attractor_example.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2160 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/mandelbrot_section.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2863 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/measles_example.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1772 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/network_graph.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1355 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/polar_scatter_demo.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2287 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/quiver_demo.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1852 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/scatter_economic.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     6136 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/square_limit.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2026 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/step_chart.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2511 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/stocks_example.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1401 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/surface_3d.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1915 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/texas_choropleth_example.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2729 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/topographic_hillshading.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2141 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/trisurf3d_demo.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1811 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/us_unemployment.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3778 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/verhulst_mandelbrot.ipynb
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/plotly/
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1567 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/plotly/surface_3d.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2169 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/gallery/demos/plotly/trisurf3d_demo.ipynb
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/holoviews/examples/getting_started/
+-rw-r--r--   0 jstevens   (501) wheel        (0)    18070 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/getting_started/1-Introduction.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    15769 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/getting_started/2-Customization.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    12141 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/getting_started/3-Tabular_Datasets.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    12520 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/getting_started/4-Gridded_Datasets.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    13473 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/getting_started/5-Live_Data.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1259 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/README.md
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:25.000000 holoviews-1.9.5/holoviews/examples/reference/
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:25.000000 holoviews-1.9.5/holoviews/examples/reference/apps/
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/holoviews/examples/reference/apps/bokeh/
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1436 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/apps/bokeh/player.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)      850 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/apps/bokeh/selection_stream.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)      589 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/apps/bokeh/sine.py
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:25.000000 holoviews-1.9.5/holoviews/examples/reference/containers/
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/holoviews/examples/reference/containers/bokeh/
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4122 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/containers/bokeh/DynamicMap.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3501 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/containers/bokeh/GridSpace.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     6188 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/containers/bokeh/HoloMap.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2852 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/containers/bokeh/Layout.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4616 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/containers/bokeh/NdLayout.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4458 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/containers/bokeh/NdOverlay.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2764 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/containers/bokeh/Overlay.ipynb
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/holoviews/examples/reference/containers/matplotlib/
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4127 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/containers/matplotlib/DynamicMap.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3478 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/containers/matplotlib/GridSpace.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     6188 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/containers/matplotlib/HoloMap.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2853 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/containers/matplotlib/Layout.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4616 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/containers/matplotlib/NdLayout.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4458 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/containers/matplotlib/NdOverlay.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2763 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/containers/matplotlib/Overlay.ipynb
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:25.000000 holoviews-1.9.5/holoviews/examples/reference/elements/
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/holoviews/examples/reference/elements/assets/
+-rw-r--r--   0 jstevens   (501) wheel        (0)   175335 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/assets/penguins.png
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3846 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Area.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2134 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Arrow.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3161 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Bars.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4028 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Bivariate.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2133 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Bounds.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2506 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Box.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2926 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/BoxWhisker.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3081 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Contours.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2791 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Curve.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4326 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Distribution.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2568 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Ellipse.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3065 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/ErrorBars.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     5525 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Graph.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3199 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/HeatMap.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3734 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Histogram.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1557 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/HLine.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2914 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/HSV.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3743 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Image.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1873 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/ItemTable.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4762 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Path.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4662 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Points.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3952 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Polygons.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3979 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/QuadMesh.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1904 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Raster.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3652 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/RGB.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4814 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Scatter.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4314 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Spikes.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1752 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Spline.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3039 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Spread.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3489 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Table.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1412 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Text.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4856 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/VectorField.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1520 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/VLine.ipynb
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3851 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Area.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2140 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Arrow.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3238 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Bars.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3981 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Bivariate.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2137 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Bounds.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2509 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Box.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2928 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/BoxWhisker.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3102 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Contours.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2778 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Curve.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4395 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Distribution.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2572 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Ellipse.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3070 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/ErrorBars.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     5513 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Graph.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3130 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/HeatMap.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3773 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Histogram.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1561 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/HLine.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2919 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/HSV.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3748 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Image.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1840 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/ItemTable.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4776 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Path.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4657 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Points.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3901 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Polygons.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3266 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/QuadMesh.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1908 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Raster.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3657 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/RGB.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4819 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Scatter.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2279 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Scatter3D.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4304 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Spikes.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1804 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Spline.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3027 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Spread.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2696 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Surface.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3403 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Table.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1417 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Text.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2562 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/TriSurface.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     5292 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/VectorField.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1524 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/VLine.ipynb
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/holoviews/examples/reference/elements/plotly/
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2596 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/plotly/BoxWhiskers.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2774 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/plotly/Curve.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1987 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/plotly/Distribution.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3122 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/plotly/ErrorBars.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3237 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/plotly/HeatMap.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3549 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/plotly/Image.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1892 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/plotly/ItemTable.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4677 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/plotly/Points.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1957 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/plotly/Raster.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4838 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/plotly/Scatter.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2333 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/plotly/Scatter3D.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2573 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/plotly/Surface.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3460 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/plotly/Table.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2598 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/elements/plotly/TriSurface.ipynb
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:25.000000 holoviews-1.9.5/holoviews/examples/reference/features/
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/holoviews/examples/reference/features/bokeh/
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1675 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/features/bokeh/table_hooks_example.ipynb
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:25.000000 holoviews-1.9.5/holoviews/examples/reference/streams/
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/holoviews/examples/reference/streams/bokeh/
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2756 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/streams/bokeh/Bounds.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1797 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/streams/bokeh/BoundsX.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2032 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/streams/bokeh/BoundsY.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2098 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/streams/bokeh/PointerX.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1925 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/streams/bokeh/PointerXY.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1917 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/streams/bokeh/RangeXY.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1565 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/streams/bokeh/Selection1D.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2277 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/streams/bokeh/Selection1D_paired.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2149 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/streams/bokeh/Selection1D_points.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3258 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/streams/bokeh/Selection1D_tap.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2723 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/reference/streams/bokeh/Tap.ipynb
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:25.000000 holoviews-1.9.5/holoviews/examples/topics/
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/holoviews/examples/topics/geometry/
+-rw-r--r--   0 jstevens   (501) wheel        (0)    15860 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/topics/geometry/lsystems.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    10960 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/topics/geometry/square_limit.ipynb
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/holoviews/examples/topics/simulation/
+-rw-r--r--   0 jstevens   (501) wheel        (0)     9738 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/topics/simulation/boids.ipynb
+-rwxr-xr-x   0 jstevens   (501) wheel        (0)    13977 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/topics/simulation/hipster_dynamics.ipynb
+-rwxr-xr-x   0 jstevens   (501) wheel        (0)    28641 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/topics/simulation/sri_model.ipynb
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/holoviews/examples/user_guide/
+-rw-r--r--   0 jstevens   (501) wheel        (0)    12341 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/user_guide/01-Annotating_Data.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    14136 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/user_guide/02-Composing_Elements.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    23190 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/user_guide/03-Customizing_Plots.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    12295 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/user_guide/04-Dimensioned_Containers.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    16424 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/user_guide/05-Building_Composite_Objects.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    29485 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/user_guide/06-Live_Data.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    22018 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/examples/user_guide/07-Tabular_Datasets.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    11996 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/user_guide/08-Gridded_Datasets.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    18763 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/user_guide/09-Indexing_and_Selecting_Data.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    22088 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/user_guide/10-Transforming_Elements.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    29588 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/user_guide/11-Responding_to_Events.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    19594 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/user_guide/12-Custom_Interactivity.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     8512 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/user_guide/13-Data_Pipelines.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    19182 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/examples/user_guide/14-Large_Data.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    25079 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/user_guide/15-Streaming_Data.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     7880 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/user_guide/16-Dashboards.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    15196 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/user_guide/Continuous_Coordinates.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    22354 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/user_guide/Deploying_Bokeh_Apps.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    26456 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/user_guide/Exporting_and_Archiving.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     6099 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/examples/user_guide/Installing_and_Configuring.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    12659 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/user_guide/Network_Graphs.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    18793 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/user_guide/Plots_and_Renderers.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)    18463 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/examples/user_guide/Plotting_with_Bokeh.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     6140 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/user_guide/Plotting_with_Matplotlib.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2603 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/examples/user_guide/Tips_and_Tricks.ipynb
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/holoviews/ipython/
+-rw-r--r--   0 jstevens   (501) wheel        (0)     9865 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/ipython/__init__.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    12249 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/ipython/archive.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    10610 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/ipython/display_hooks.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    13605 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/ipython/load_notebook.html
+-rw-r--r--   0 jstevens   (501) wheel        (0)    15787 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/ipython/magics.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     7474 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/ipython/preprocessors.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     8646 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/ipython/widgets.py
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/holoviews/operation/
+-rw-r--r--   0 jstevens   (501) wheel        (0)      730 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/operation/__init__.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    36179 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/operation/datashader.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    31868 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/operation/element.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     6595 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/operation/normalization.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     9674 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/operation/stats.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4593 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/operation/timeseries.py
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/holoviews/plotting/
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1277 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/plotting/__init__.py
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/holoviews/plotting/bokeh/
+-rw-r--r--   0 jstevens   (501) wheel        (0)     9062 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/plotting/bokeh/__init__.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     6954 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/plotting/bokeh/annotation.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)      165 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/plotting/bokeh/bokehwidgets.css
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1042 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/plotting/bokeh/bokehwidgets.js
+-rw-r--r--   0 jstevens   (501) wheel        (0)    30115 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/plotting/bokeh/callbacks.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    46368 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/plotting/bokeh/chart.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    62372 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/plotting/bokeh/element.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    11065 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/plotting/bokeh/graphs.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     7341 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/plotting/bokeh/path.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    36784 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/plotting/bokeh/plot.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     7490 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/plotting/bokeh/raster.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    11448 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/plotting/bokeh/renderer.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1154 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/plotting/bokeh/stats.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     5064 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/plotting/bokeh/tabular.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    21266 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/plotting/bokeh/util.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    11556 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/plotting/bokeh/widgets.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     6280 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/plotting/comms.py
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/holoviews/plotting/mpl/
+-rw-r--r--   0 jstevens   (501) wheel        (0)    10573 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/plotting/mpl/__init__.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4359 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/plotting/mpl/annotation.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    41985 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/plotting/mpl/chart.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     7570 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/plotting/mpl/chart3d.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2598 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/plotting/mpl/comms.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1030 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/plotting/mpl/default.mplstyle
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1058 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/plotting/mpl/default1.5.mplstyle
+-rw-r--r--   0 jstevens   (501) wheel        (0)    36750 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/plotting/mpl/element.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     6624 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/plotting/mpl/graphs.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1330 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/plotting/mpl/mplwidgets.js
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4652 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/plotting/mpl/path.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    47648 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/plotting/mpl/plot.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    16596 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/plotting/mpl/raster.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    10743 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/plotting/mpl/renderer.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1154 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/plotting/mpl/stats.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     5240 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/plotting/mpl/tabular.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     6075 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/plotting/mpl/util.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1669 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/plotting/mpl/widgets.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    43149 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/plotting/plot.py
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/holoviews/plotting/plotly/
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2609 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/plotting/plotly/__init__.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     8139 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/plotting/plotly/chart.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3895 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/plotting/plotly/chart3d.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     9535 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/plotting/plotly/element.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    15858 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/plotting/plotly/plot.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1248 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/plotting/plotly/plotlywidgets.js
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1724 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/plotting/plotly/raster.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     5713 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/plotting/plotly/renderer.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1002 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/plotting/plotly/tabular.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1098 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/plotting/plotly/util.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1248 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/plotting/plotly/widgets.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    20342 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/plotting/renderer.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    32276 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/plotting/util.py
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/holoviews/plotting/widgets/
+-rw-r--r--   0 jstevens   (501) wheel        (0)    15651 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/plotting/widgets/__init__.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2345 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/plotting/widgets/jsscrubber.jinja
+-rw-r--r--   0 jstevens   (501) wheel        (0)      996 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/plotting/widgets/jsslider.css
+-rw-r--r--   0 jstevens   (501) wheel        (0)     9912 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/plotting/widgets/jsslider.jinja
+-rw-r--r--   0 jstevens   (501) wheel        (0)     9308 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/plotting/widgets/widgets.js
+-rw-r--r--   0 jstevens   (501) wheel        (0)    28544 2018-03-02 12:16:24.000000 holoviews-1.9.5/holoviews/streams.py
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/holoviews/util/
+-rw-r--r--   0 jstevens   (501) wheel        (0)    18274 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/util/__init__.py
+-rwxr-xr-x   0 jstevens   (501) wheel        (0)     3137 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/util/command.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    17156 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/util/parser.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    15783 2018-03-02 12:12:30.000000 holoviews-1.9.5/holoviews/util/settings.py
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/holoviews.egg-info/
+-rw-r--r--   0 jstevens   (501) wheel        (0)        1 2018-03-02 13:00:25.000000 holoviews-1.9.5/holoviews.egg-info/dependency_links.txt
+-rw-r--r--   0 jstevens   (501) wheel        (0)       59 2018-03-02 13:00:25.000000 holoviews-1.9.5/holoviews.egg-info/entry_points.txt
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1271 2018-03-02 13:00:25.000000 holoviews-1.9.5/holoviews.egg-info/PKG-INFO
+-rw-r--r--   0 jstevens   (501) wheel        (0)      517 2018-03-02 13:00:25.000000 holoviews-1.9.5/holoviews.egg-info/requires.txt
+-rw-r--r--   0 jstevens   (501) wheel        (0)    32424 2018-03-02 13:00:25.000000 holoviews-1.9.5/holoviews.egg-info/SOURCES.txt
+-rw-r--r--   0 jstevens   (501) wheel        (0)       10 2018-03-02 13:00:25.000000 holoviews-1.9.5/holoviews.egg-info/top_level.txt
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1499 2018-03-02 12:12:30.000000 holoviews-1.9.5/LICENSE.txt
+-rw-r--r--   0 jstevens   (501) wheel        (0)      412 2018-03-02 12:12:30.000000 holoviews-1.9.5/MANIFEST.in
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1271 2018-03-02 13:00:26.000000 holoviews-1.9.5/PKG-INFO
+-rw-r--r--   0 jstevens   (501) wheel        (0)     5124 2018-03-02 12:16:24.000000 holoviews-1.9.5/README.md
+-rw-r--r--   0 jstevens   (501) wheel        (0)       38 2018-03-02 13:00:26.000000 holoviews-1.9.5/setup.cfg
+-rw-r--r--   0 jstevens   (501) wheel        (0)     6906 2018-03-02 12:31:32.000000 holoviews-1.9.5/setup.py
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/tests/
+-rw-r--r--   0 jstevens   (501) wheel        (0)      145 2018-03-02 12:12:30.000000 holoviews-1.9.5/tests/__init__.py
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/tests/core/
+-rw-r--r--   0 jstevens   (501) wheel        (0)     7059 2018-03-02 12:12:30.000000 holoviews-1.9.5/tests/core/testdimensioned.py
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/tests/notebooks/
+-rw-r--r--   0 jstevens   (501) wheel        (0)      361 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/notebooks/test_opts_image_cell_magic.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)      404 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/notebooks/test_opts_image_cell_magic_offset.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)      319 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/notebooks/test_opts_image_line_magic.ipynb
+-rw-r--r--   0 jstevens   (501) wheel        (0)      295 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/notebooks/test_output_svg_line_magic.ipynb
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/tests/operation/
+-rw-r--r--   0 jstevens   (501) wheel        (0)        0 2018-03-02 12:12:30.000000 holoviews-1.9.5/tests/operation/__init__.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    12575 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/operation/testdatashader.py
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/tests/plotting/
+-rw-r--r--   0 jstevens   (501) wheel        (0)        0 2018-03-02 12:12:30.000000 holoviews-1.9.5/tests/plotting/__init__.py
+drwxr-xr-x   0 jstevens   (501) wheel        (0)        0 2018-03-02 13:00:26.000000 holoviews-1.9.5/tests/plotting/bokeh/
+-rw-r--r--   0 jstevens   (501) wheel        (0)        0 2018-03-02 12:12:30.000000 holoviews-1.9.5/tests/plotting/bokeh/__init__.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     5807 2018-03-02 12:12:30.000000 holoviews-1.9.5/tests/plotting/bokeh/testserver.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2165 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/plotting/bokeh/testtabular.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    21869 2018-03-02 12:12:30.000000 holoviews-1.9.5/tests/plotting/testplotutils.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2007 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testaliases.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2160 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testannotations.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)      985 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testapiconsistency.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     5316 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testarchives.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3928 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testbokehcallbacks.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     8557 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testbokehgraphs.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3687 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testbokehutils.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     7291 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testbokehwidgets.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2356 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testboundingregion.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    12920 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testcallable.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3718 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testcollation.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2242 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testcomms.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     7557 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testcomparisonchart.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4823 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testcomparisoncomposite.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     7517 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testcomparisondimension.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3440 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testcomparisonpath.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     6350 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testcomparisonraster.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3976 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testcomparisonsimple.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    16402 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testcomposites.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    23470 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testcoreutils.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    73283 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testdataset.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    10558 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testdimensions.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3695 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testdimselect.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    32714 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testdynamic.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     7557 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testelementconstructors.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     5207 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testelementindexing.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3519 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testelementranges.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)      789 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testelementutils.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     5344 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testellipsis.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     5561 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testgraphelement.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    26935 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testimageinterfaces.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     7744 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testimportexport.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4179 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testirisinterface.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     1243 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testlayers.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     5123 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testlayouts.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     7219 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testmagics.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4454 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testmplgraphs.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     5925 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testmultiinterface.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    10776 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testndmapping.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3041 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testnotebooks.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     7916 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testoperation.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    28828 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testoptions.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     5406 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testoptscompleter.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    11792 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testparsers.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3050 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testpaths.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    90959 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testplotinstantiation.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)      987 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testprettyprint.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2513 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testraster.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     5644 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testrenderclass.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     8621 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/teststatselements.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     2098 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/teststatsoperations.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3951 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/teststoreoptions.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)    17918 2018-03-02 12:12:30.000000 holoviews-1.9.5/tests/teststreams.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3105 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testtimeseriesoperations.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3388 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testtraversal.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     4181 2018-03-02 12:16:24.000000 holoviews-1.9.5/tests/testutils.py
+-rw-r--r--   0 jstevens   (501) wheel        (0)     3694 2018-03-02 12:12:30.000000 holoviews-1.9.5/tests/utils.py
```

### Comparing `holoviews-1.9.4/CHANGELOG.md` & `holoviews-1.9.5/CHANGELOG.md`

 * *Files 1% similar despite different names*

```diff
@@ -1,7 +1,28 @@
+Version 1.9.5
+=============
+
+This release includes a very small number of minor bugfixes and a new
+feature to simplify setting options in python:
+
+Enhancements:
+
+-  Added .options method for simplified options setting.
+   ([\#2306](https://github.com/ioam/holoviews/pull/2306))
+
+Fixes:
+
+-  Allow plotting bytes datausing the bokeh backend in python3
+   ([\#2357](https://github.com/ioam/holoviews/pull/2357))
+-  Allow .range to work on data with heterogeneous types in Python 3
+   ([\#2345](https://github.com/ioam/holoviews/pull/2345))
+-  Fixed bug streaming data containing datetimes using bokeh>=0.12.14
+   ([\#2383](https://github.com/ioam/holoviews/pull/2383))
+
+
 Version 1.9.4
 =============
 
 This release contains a small number of important bug fixes:
 
 -    Compatibility with recent versions of dask and pandas
      ([\#2329](https://github.com/ioam/holoviews/pull/2329))
```

### Comparing `holoviews-1.9.4/doc/_static/favicon.ico` & `holoviews-1.9.5/doc/_static/favicon.ico`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/_static/holoviews_logo.png` & `holoviews-1.9.5/doc/_static/holoviews_logo.png`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/_static/rtd_bootstrap.css` & `holoviews-1.9.5/doc/_static/rtd_bootstrap.css`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/about.rst` & `holoviews-1.9.5/doc/about.rst`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/assets/macaw.png` & `holoviews-1.9.5/doc/assets/macaw.png`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/assets/nesting-diagram.svg` & `holoviews-1.9.5/doc/assets/nesting-diagram.svg`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/assets/penguins.png` & `holoviews-1.9.5/doc/assets/penguins.png`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/conf.py` & `holoviews-1.9.5/doc/conf.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/FAQ.rst` & `holoviews-1.9.5/doc/FAQ.rst`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/features.rst` & `holoviews-1.9.5/doc/features.rst`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/getting_started/index.rst` & `holoviews-1.9.5/doc/getting_started/index.rst`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/holoviews_theme/layout.html` & `holoviews-1.9.5/doc/holoviews_theme/layout.html`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/holoviews_theme/search.html` & `holoviews-1.9.5/doc/holoviews_theme/search.html`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/holoviews_theme/static/images/favicon.ico` & `holoviews-1.9.5/doc/holoviews_theme/static/images/favicon.ico`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/holoviews_theme/static/images/logo.png` & `holoviews-1.9.5/doc/holoviews_theme/static/images/logo.png`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/holoviews_theme/static/images/logo.svg` & `holoviews-1.9.5/doc/holoviews_theme/static/images/logo.svg`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/holoviews_theme/static/js/main.js` & `holoviews-1.9.5/doc/holoviews_theme/static/js/main.js`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/Homepage.ipynb` & `holoviews-1.9.5/doc/Homepage.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/index.rst` & `holoviews-1.9.5/doc/index.rst`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/install.rst` & `holoviews-1.9.5/doc/install.rst`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/mandelbrot.npy` & `holoviews-1.9.5/doc/mandelbrot.npy`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/Reference_Manual/index.rst` & `holoviews-1.9.5/doc/Reference_Manual/index.rst`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/showcase/index.rst` & `holoviews-1.9.5/doc/showcase/index.rst`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/Tutorials/Bokeh_Backend.ipynb` & `holoviews-1.9.5/doc/Tutorials/Bokeh_Backend.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/Tutorials/Bokeh_Elements.ipynb` & `holoviews-1.9.5/doc/Tutorials/Bokeh_Elements.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/Tutorials/Columnar_Data.ipynb` & `holoviews-1.9.5/doc/Tutorials/Columnar_Data.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/Tutorials/Composing_Data.ipynb` & `holoviews-1.9.5/doc/Tutorials/Composing_Data.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/Tutorials/Containers.ipynb` & `holoviews-1.9.5/doc/Tutorials/Containers.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/Tutorials/Continuous_Coordinates.ipynb` & `holoviews-1.9.5/doc/Tutorials/Continuous_Coordinates.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/Tutorials/Dynamic_Map.ipynb` & `holoviews-1.9.5/doc/Tutorials/Dynamic_Map.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/Tutorials/Elements.ipynb` & `holoviews-1.9.5/doc/Tutorials/Elements.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/Tutorials/Exploring_Data.ipynb` & `holoviews-1.9.5/doc/Tutorials/Exploring_Data.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/Tutorials/Exporting.ipynb` & `holoviews-1.9.5/doc/Tutorials/Exporting.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/Tutorials/index.rst` & `holoviews-1.9.5/doc/Tutorials/index.rst`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/Tutorials/Introduction.ipynb` & `holoviews-1.9.5/doc/Tutorials/Introduction.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/Tutorials/Linked_Streams.ipynb` & `holoviews-1.9.5/doc/Tutorials/Linked_Streams.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/Tutorials/Operations.ipynb` & `holoviews-1.9.5/doc/Tutorials/Operations.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/Tutorials/Options.ipynb` & `holoviews-1.9.5/doc/Tutorials/Options.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/Tutorials/Pandas_Seaborn.ipynb` & `holoviews-1.9.5/doc/Tutorials/Pandas_Seaborn.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/Tutorials/Rich_Display.ipynb` & `holoviews-1.9.5/doc/Tutorials/Rich_Display.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/Tutorials/Sampling_Data.ipynb` & `holoviews-1.9.5/doc/Tutorials/Sampling_Data.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/Tutorials/Showcase.ipynb` & `holoviews-1.9.5/doc/Tutorials/Showcase.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/Tutorials/Streams.ipynb` & `holoviews-1.9.5/doc/Tutorials/Streams.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/doc/user_guide/index.rst` & `holoviews-1.9.5/doc/user_guide/index.rst`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/assets/diseases.csv.gz` & `holoviews-1.9.5/examples/assets/diseases.csv.gz`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/assets/fb_edges.csv` & `holoviews-1.9.5/examples/assets/fb_edges.csv`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/assets/fb_nodes.csv` & `holoviews-1.9.5/examples/assets/fb_nodes.csv`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/assets/hourly_taxi_data.npz` & `holoviews-1.9.5/examples/assets/hourly_taxi_data.npz`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/assets/penguins.png` & `holoviews-1.9.5/examples/assets/penguins.png`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/assets/spike_train.csv.gz` & `holoviews-1.9.5/examples/assets/spike_train.csv.gz`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/assets/station_info.csv` & `holoviews-1.9.5/examples/assets/station_info.csv`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/assets/twophoton.npz` & `holoviews-1.9.5/examples/assets/twophoton.npz`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/bokeh/area_chart.ipynb` & `holoviews-1.9.5/examples/gallery/demos/bokeh/area_chart.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/bokeh/autompg_histogram.ipynb` & `holoviews-1.9.5/examples/gallery/demos/bokeh/autompg_histogram.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/bokeh/bachelors_degrees_by_gender.ipynb` & `holoviews-1.9.5/examples/gallery/demos/bokeh/bachelors_degrees_by_gender.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/bokeh/bars_economic.ipynb` & `holoviews-1.9.5/examples/gallery/demos/bokeh/bars_economic.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/bokeh/boxplot_chart.ipynb` & `holoviews-1.9.5/examples/gallery/demos/bokeh/boxplot_chart.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/bokeh/dot_example.ipynb` & `holoviews-1.9.5/examples/gallery/demos/bokeh/dot_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/bokeh/dragon_curve.ipynb` & `holoviews-1.9.5/examples/gallery/demos/bokeh/dragon_curve.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/bokeh/dropdown_economic.ipynb` & `holoviews-1.9.5/examples/gallery/demos/bokeh/dropdown_economic.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/bokeh/histogram_example.ipynb` & `holoviews-1.9.5/examples/gallery/demos/bokeh/histogram_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/bokeh/iris_density_grid.ipynb` & `holoviews-1.9.5/examples/gallery/demos/bokeh/iris_density_grid.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/bokeh/iris_example.ipynb` & `holoviews-1.9.5/examples/gallery/demos/bokeh/iris_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/bokeh/iris_grouped_grid.ipynb` & `holoviews-1.9.5/examples/gallery/demos/bokeh/iris_grouped_grid.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/bokeh/iris_splom_example.ipynb` & `holoviews-1.9.5/examples/gallery/demos/bokeh/iris_splom_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/bokeh/legend_example.ipynb` & `holoviews-1.9.5/examples/gallery/demos/bokeh/legend_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/bokeh/lesmis_example.ipynb` & `holoviews-1.9.5/examples/gallery/demos/bokeh/lesmis_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/bokeh/lorenz_attractor_example.ipynb` & `holoviews-1.9.5/examples/gallery/demos/bokeh/lorenz_attractor_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/bokeh/mandelbrot_section.ipynb` & `holoviews-1.9.5/examples/gallery/demos/bokeh/mandelbrot_section.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/bokeh/measles_example.ipynb` & `holoviews-1.9.5/examples/gallery/demos/bokeh/measles_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/bokeh/network_graph.ipynb` & `holoviews-1.9.5/examples/gallery/demos/bokeh/network_graph.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/bokeh/quiver_demo.ipynb` & `holoviews-1.9.5/examples/gallery/demos/bokeh/quiver_demo.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/bokeh/scatter_economic.ipynb` & `holoviews-1.9.5/examples/gallery/demos/bokeh/scatter_economic.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/bokeh/square_limit.ipynb` & `holoviews-1.9.5/examples/gallery/demos/bokeh/square_limit.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/bokeh/step_chart.ipynb` & `holoviews-1.9.5/examples/gallery/demos/bokeh/step_chart.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/bokeh/stocks_example.ipynb` & `holoviews-1.9.5/examples/gallery/demos/bokeh/stocks_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/bokeh/texas_choropleth_example.ipynb` & `holoviews-1.9.5/examples/gallery/demos/bokeh/texas_choropleth_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/bokeh/topographic_hillshading.ipynb` & `holoviews-1.9.5/examples/gallery/demos/bokeh/topographic_hillshading.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/bokeh/us_unemployment.ipynb` & `holoviews-1.9.5/examples/gallery/demos/bokeh/us_unemployment.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/bokeh/verhulst_mandelbrot.ipynb` & `holoviews-1.9.5/examples/gallery/demos/bokeh/verhulst_mandelbrot.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/matplotlib/area_chart.ipynb` & `holoviews-1.9.5/examples/gallery/demos/matplotlib/area_chart.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/matplotlib/autompg_histogram.ipynb` & `holoviews-1.9.5/examples/gallery/demos/matplotlib/autompg_histogram.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/matplotlib/bachelors_degrees_by_gender.ipynb` & `holoviews-1.9.5/examples/gallery/demos/matplotlib/bachelors_degrees_by_gender.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/matplotlib/bars_economic.ipynb` & `holoviews-1.9.5/examples/gallery/demos/matplotlib/bars_economic.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/matplotlib/boxplot_chart.ipynb` & `holoviews-1.9.5/examples/gallery/demos/matplotlib/boxplot_chart.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/matplotlib/dragon_curve.ipynb` & `holoviews-1.9.5/examples/gallery/demos/matplotlib/dragon_curve.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/matplotlib/dropdown_economic.ipynb` & `holoviews-1.9.5/examples/gallery/demos/matplotlib/dropdown_economic.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/matplotlib/histogram_example.ipynb` & `holoviews-1.9.5/examples/gallery/demos/matplotlib/histogram_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/matplotlib/iris_density_grid.ipynb` & `holoviews-1.9.5/examples/gallery/demos/matplotlib/iris_density_grid.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/matplotlib/iris_example.ipynb` & `holoviews-1.9.5/examples/gallery/demos/matplotlib/iris_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/matplotlib/iris_grouped_grid.ipynb` & `holoviews-1.9.5/examples/gallery/demos/matplotlib/iris_grouped_grid.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/matplotlib/iris_splom_example.ipynb` & `holoviews-1.9.5/examples/gallery/demos/matplotlib/iris_splom_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/matplotlib/legend_example.ipynb` & `holoviews-1.9.5/examples/gallery/demos/matplotlib/legend_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/matplotlib/lorenz_attractor_example.ipynb` & `holoviews-1.9.5/examples/gallery/demos/matplotlib/lorenz_attractor_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/matplotlib/mandelbrot_section.ipynb` & `holoviews-1.9.5/examples/gallery/demos/matplotlib/mandelbrot_section.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/matplotlib/measles_example.ipynb` & `holoviews-1.9.5/examples/gallery/demos/matplotlib/measles_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/matplotlib/network_graph.ipynb` & `holoviews-1.9.5/examples/gallery/demos/matplotlib/network_graph.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/matplotlib/polar_scatter_demo.ipynb` & `holoviews-1.9.5/examples/gallery/demos/matplotlib/polar_scatter_demo.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/matplotlib/quiver_demo.ipynb` & `holoviews-1.9.5/examples/gallery/demos/matplotlib/quiver_demo.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/matplotlib/scatter_economic.ipynb` & `holoviews-1.9.5/examples/gallery/demos/matplotlib/scatter_economic.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/matplotlib/square_limit.ipynb` & `holoviews-1.9.5/examples/gallery/demos/matplotlib/square_limit.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/matplotlib/step_chart.ipynb` & `holoviews-1.9.5/examples/gallery/demos/matplotlib/step_chart.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/matplotlib/stocks_example.ipynb` & `holoviews-1.9.5/examples/gallery/demos/matplotlib/stocks_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/matplotlib/surface_3d.ipynb` & `holoviews-1.9.5/examples/gallery/demos/matplotlib/surface_3d.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/matplotlib/texas_choropleth_example.ipynb` & `holoviews-1.9.5/examples/gallery/demos/matplotlib/texas_choropleth_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/matplotlib/topographic_hillshading.ipynb` & `holoviews-1.9.5/examples/gallery/demos/matplotlib/topographic_hillshading.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/matplotlib/trisurf3d_demo.ipynb` & `holoviews-1.9.5/examples/gallery/demos/matplotlib/trisurf3d_demo.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/matplotlib/us_unemployment.ipynb` & `holoviews-1.9.5/examples/gallery/demos/matplotlib/us_unemployment.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/matplotlib/verhulst_mandelbrot.ipynb` & `holoviews-1.9.5/examples/gallery/demos/matplotlib/verhulst_mandelbrot.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/plotly/surface_3d.ipynb` & `holoviews-1.9.5/examples/gallery/demos/plotly/surface_3d.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/gallery/demos/plotly/trisurf3d_demo.ipynb` & `holoviews-1.9.5/examples/gallery/demos/plotly/trisurf3d_demo.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/getting_started/1-Introduction.ipynb` & `holoviews-1.9.5/examples/getting_started/1-Introduction.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/getting_started/2-Customization.ipynb` & `holoviews-1.9.5/examples/getting_started/2-Customization.ipynb`

 * *Files 8% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9819529291979949%*

 * *Differences: {"'cells'": "{13: {'source': {insert: [(6, '(curve + spikes).cols(1)')], delete: [6]}}, 14: "*

 * *            "{'source': {insert: [(17, 'As you can see, these tools allow significant "*

 * *            'customization of how our elements appear. HoloViews offers many other tools for '*

 * *            'setting options either locally or globally, including the ``%output`` and ``%opts`` '*

 * *            '*line magics*, the ``.opts`` and ``.options`` methods on all HoloViews objects and '*

 * *            'the ``hv.output`` and ``h […]*

```diff
@@ -133,15 +133,15 @@
             "source": [
                 "%%output size=150\n",
                 "%%opts Curve  [height=100 width=600 xaxis=None tools=['hover']]\n",
                 "%%opts Curve (color='red' line_width=1.5)\n",
                 "%%opts Spikes [height=100 width=600 yaxis=None] (color='grey' line_width=0.25)\n",
                 "curve  = hv.Curve( spike_train, 'milliseconds', 'Hertz')\n",
                 "spikes = hv.Spikes(spike_train, 'milliseconds', [])\n",
-                "(curve+spikes).cols(1)"
+                "(curve + spikes).cols(1)"
             ]
         },
         {
             "cell_type": "markdown",
             "metadata": {},
             "source": [
                 "Much better! It's the same underlying data, but now we can clearly see both the individual spike events and how they affect the moving average.  You can also see how the moving average trails the actual spiking, due to how the window function was defined.\n",
@@ -157,15 +157,57 @@
                 "\n",
                 "* The element type is specified following by special groups of keywords.\n",
                 "* The keywords in square brackets ``[...]`` are ***plot options*** that instruct HoloViews how to build that type of plot.\n",
                 "* The keywords in parentheses ``(...)`` are **style options** with keywords that are passed directly to the plotting library when rendering that type of plot.\n",
                 "\n",
                 "The corresponding [User Guide](../user_guide/03-Customizing_Plots.ipynb) entry explains the keywords used in detail, but a quick summary is that we have elongated the ``Curve`` and ``Scatter`` elements and toggled various axes with the ***plot options***. We have also specified the color and line widths of the [Bokeh glyphs](http://bokeh.pydata.org/en/latest/docs/user_guide/plotting.html) with the ***style options***.\n",
                 "\n",
-                "As you can see, these tools allow significant customization of how our elements appear. HoloViews offers many other tools for setting options either locally or globally, including the ``%output`` and ``%opts`` *line magics*, the ``.opts`` method on all HoloViews objects and the ``hv.output`` and ``hv.opts`` utilities. All these tools, how they work and details of the opts syntax can be found in the [User Guide](../user_guide/03-Customizing_Plots.ipynb)."
+                "As you can see, these tools allow significant customization of how our elements appear. HoloViews offers many other tools for setting options either locally or globally, including the ``%output`` and ``%opts`` *line magics*, the ``.opts`` and ``.options`` methods on all HoloViews objects and the ``hv.output`` and ``hv.opts`` utilities. We will briefly consider the ``.options`` based approach, which makes it possible to work outside the notebook. All these tools, how they work and details of the opts syntax can be found in the [User Guide](../user_guide/03-Customizing_Plots.ipynb)."
+            ]
+        },
+        {
+            "cell_type": "markdown",
+            "metadata": {},
+            "source": [
+                "# Outside the notebook\n",
+                "\n",
+                "When working inside the notebook environment using the ``%%opts`` magic is a very convenient and powerful way of working because it allows tab-completion of the options however outside the notebook and when you're are customizing a specific object it is often useful to set the options directly on an object. The simplest way of doing so is using the ``.options`` method, which will automatically deduce whether an option is a ``style``, ``plot`` or ``norm`` option.\n",
+                "\n",
+                "To demonstrate this we can reproduce the plot above by combining both the plot and style options above into a flat set of options:"
+            ]
+        },
+        {
+            "cell_type": "code",
+            "execution_count": null,
+            "metadata": {},
+            "outputs": [],
+            "source": [
+                "curve_opts = dict(height=100, width=600, xaxis=None, tools=['hover'], color='red', line_width=1.5)\n",
+                "spike_opts = dict(height=100, width=600, yaxis=None, color='grey', line_width=0.25)\n",
+                "\n",
+                "curve = hv.Curve(spike_train, 'milliseconds', 'Hertz')\n",
+                "spikes = hv.Spikes(spike_train, 'milliseconds', [])\n",
+                "\n",
+                "(curve.options(**curve_opts) + spikes.options(**spike_opts)).cols(1)"
+            ]
+        },
+        {
+            "cell_type": "markdown",
+            "metadata": {},
+            "source": [
+                "When using ``.options`` to apply options directly to an individual object we do not have to explicitly declare which object the options apply to, however often it is useful to set options on a composite object. In these cases the options can be declared as a dictionary of the type name and the options. The code below is therefore equivalent to the syntax we used above:"
+            ]
+        },
+        {
+            "cell_type": "code",
+            "execution_count": null,
+            "metadata": {},
+            "outputs": [],
+            "source": [
+                "layout = (curve + spikes).options({'Curve': curve_opts, 'Spikes': spike_opts}).cols(1)"
             ]
         },
         {
             "cell_type": "markdown",
             "metadata": {},
             "source": [
                 "# Switching to matplotlib\n",
```

### Comparing `holoviews-1.9.4/examples/getting_started/3-Tabular_Datasets.ipynb` & `holoviews-1.9.5/examples/getting_started/3-Tabular_Datasets.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/getting_started/4-Gridded_Datasets.ipynb` & `holoviews-1.9.5/examples/getting_started/4-Gridded_Datasets.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/getting_started/5-Live_Data.ipynb` & `holoviews-1.9.5/examples/getting_started/5-Live_Data.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/README.md` & `holoviews-1.9.5/examples/README.md`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/containers/bokeh/DynamicMap.ipynb` & `holoviews-1.9.5/examples/reference/containers/bokeh/DynamicMap.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/containers/bokeh/GridSpace.ipynb` & `holoviews-1.9.5/examples/reference/containers/bokeh/GridSpace.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/containers/bokeh/HoloMap.ipynb` & `holoviews-1.9.5/examples/reference/containers/bokeh/HoloMap.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/containers/bokeh/Layout.ipynb` & `holoviews-1.9.5/examples/reference/containers/bokeh/Layout.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/containers/bokeh/NdLayout.ipynb` & `holoviews-1.9.5/examples/reference/containers/bokeh/NdLayout.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/containers/bokeh/NdOverlay.ipynb` & `holoviews-1.9.5/examples/reference/containers/bokeh/NdOverlay.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/containers/bokeh/Overlay.ipynb` & `holoviews-1.9.5/examples/reference/containers/bokeh/Overlay.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/containers/matplotlib/DynamicMap.ipynb` & `holoviews-1.9.5/examples/reference/containers/matplotlib/DynamicMap.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/containers/matplotlib/GridSpace.ipynb` & `holoviews-1.9.5/examples/reference/containers/matplotlib/GridSpace.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/containers/matplotlib/HoloMap.ipynb` & `holoviews-1.9.5/examples/reference/containers/matplotlib/HoloMap.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/containers/matplotlib/Layout.ipynb` & `holoviews-1.9.5/examples/reference/containers/matplotlib/Layout.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/containers/matplotlib/NdLayout.ipynb` & `holoviews-1.9.5/examples/reference/containers/matplotlib/NdLayout.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/containers/matplotlib/NdOverlay.ipynb` & `holoviews-1.9.5/examples/reference/containers/matplotlib/NdOverlay.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/containers/matplotlib/Overlay.ipynb` & `holoviews-1.9.5/examples/reference/containers/matplotlib/Overlay.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/assets/penguins.png` & `holoviews-1.9.5/examples/reference/elements/assets/penguins.png`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/bokeh/Area.ipynb` & `holoviews-1.9.5/examples/reference/elements/bokeh/Area.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/bokeh/Arrow.ipynb` & `holoviews-1.9.5/examples/reference/elements/bokeh/Arrow.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/bokeh/Bars.ipynb` & `holoviews-1.9.5/examples/reference/elements/bokeh/Bars.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/bokeh/Bivariate.ipynb` & `holoviews-1.9.5/examples/reference/elements/bokeh/Bivariate.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/bokeh/Bounds.ipynb` & `holoviews-1.9.5/examples/reference/elements/bokeh/Bounds.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/bokeh/Box.ipynb` & `holoviews-1.9.5/examples/reference/elements/bokeh/Box.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/bokeh/BoxWhisker.ipynb` & `holoviews-1.9.5/examples/reference/elements/bokeh/BoxWhisker.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/bokeh/Contours.ipynb` & `holoviews-1.9.5/examples/reference/elements/bokeh/Contours.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/bokeh/Curve.ipynb` & `holoviews-1.9.5/examples/reference/elements/bokeh/Curve.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/bokeh/Distribution.ipynb` & `holoviews-1.9.5/examples/reference/elements/bokeh/Distribution.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/bokeh/Ellipse.ipynb` & `holoviews-1.9.5/examples/reference/elements/bokeh/Ellipse.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/bokeh/ErrorBars.ipynb` & `holoviews-1.9.5/examples/reference/elements/bokeh/ErrorBars.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/bokeh/Graph.ipynb` & `holoviews-1.9.5/examples/reference/elements/bokeh/Graph.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/bokeh/HeatMap.ipynb` & `holoviews-1.9.5/examples/reference/elements/bokeh/HeatMap.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/bokeh/Histogram.ipynb` & `holoviews-1.9.5/examples/reference/elements/bokeh/Histogram.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/bokeh/HLine.ipynb` & `holoviews-1.9.5/examples/reference/elements/bokeh/HLine.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/bokeh/HSV.ipynb` & `holoviews-1.9.5/examples/reference/elements/bokeh/HSV.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/bokeh/Image.ipynb` & `holoviews-1.9.5/examples/reference/elements/bokeh/Image.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/bokeh/ItemTable.ipynb` & `holoviews-1.9.5/examples/reference/elements/bokeh/ItemTable.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/bokeh/Path.ipynb` & `holoviews-1.9.5/examples/reference/elements/bokeh/Path.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/bokeh/Points.ipynb` & `holoviews-1.9.5/examples/reference/elements/bokeh/Points.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/bokeh/Polygons.ipynb` & `holoviews-1.9.5/examples/reference/elements/bokeh/Polygons.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/bokeh/QuadMesh.ipynb` & `holoviews-1.9.5/examples/reference/elements/bokeh/QuadMesh.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/bokeh/Raster.ipynb` & `holoviews-1.9.5/examples/reference/elements/bokeh/Raster.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/bokeh/RGB.ipynb` & `holoviews-1.9.5/examples/reference/elements/bokeh/RGB.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/bokeh/Scatter.ipynb` & `holoviews-1.9.5/examples/reference/elements/bokeh/Scatter.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/bokeh/Spikes.ipynb` & `holoviews-1.9.5/examples/reference/elements/bokeh/Spikes.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/bokeh/Spline.ipynb` & `holoviews-1.9.5/examples/reference/elements/bokeh/Spline.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/bokeh/Spread.ipynb` & `holoviews-1.9.5/examples/reference/elements/bokeh/Spread.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/bokeh/Table.ipynb` & `holoviews-1.9.5/examples/reference/elements/bokeh/Table.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/bokeh/Text.ipynb` & `holoviews-1.9.5/examples/reference/elements/bokeh/Text.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/bokeh/VectorField.ipynb` & `holoviews-1.9.5/examples/reference/elements/bokeh/VectorField.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/bokeh/VLine.ipynb` & `holoviews-1.9.5/examples/reference/elements/bokeh/VLine.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/matplotlib/Area.ipynb` & `holoviews-1.9.5/examples/reference/elements/matplotlib/Area.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/matplotlib/Arrow.ipynb` & `holoviews-1.9.5/examples/reference/elements/matplotlib/Arrow.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/matplotlib/Bars.ipynb` & `holoviews-1.9.5/examples/reference/elements/matplotlib/Bars.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/matplotlib/Bivariate.ipynb` & `holoviews-1.9.5/examples/reference/elements/matplotlib/Bivariate.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/matplotlib/Bounds.ipynb` & `holoviews-1.9.5/examples/reference/elements/matplotlib/Bounds.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/matplotlib/Box.ipynb` & `holoviews-1.9.5/examples/reference/elements/matplotlib/Box.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/matplotlib/BoxWhisker.ipynb` & `holoviews-1.9.5/examples/reference/elements/matplotlib/BoxWhisker.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/matplotlib/Contours.ipynb` & `holoviews-1.9.5/examples/reference/elements/matplotlib/Contours.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/matplotlib/Curve.ipynb` & `holoviews-1.9.5/examples/reference/elements/matplotlib/Curve.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/matplotlib/Distribution.ipynb` & `holoviews-1.9.5/examples/reference/elements/matplotlib/Distribution.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/matplotlib/Ellipse.ipynb` & `holoviews-1.9.5/examples/reference/elements/matplotlib/Ellipse.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/matplotlib/ErrorBars.ipynb` & `holoviews-1.9.5/examples/reference/elements/matplotlib/ErrorBars.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/matplotlib/Graph.ipynb` & `holoviews-1.9.5/examples/reference/elements/matplotlib/Graph.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/matplotlib/HeatMap.ipynb` & `holoviews-1.9.5/examples/reference/elements/matplotlib/HeatMap.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/matplotlib/Histogram.ipynb` & `holoviews-1.9.5/examples/reference/elements/matplotlib/Histogram.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/matplotlib/HLine.ipynb` & `holoviews-1.9.5/examples/reference/elements/matplotlib/HLine.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/matplotlib/HSV.ipynb` & `holoviews-1.9.5/examples/reference/elements/matplotlib/HSV.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/matplotlib/Image.ipynb` & `holoviews-1.9.5/examples/reference/elements/matplotlib/Image.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/matplotlib/ItemTable.ipynb` & `holoviews-1.9.5/examples/reference/elements/matplotlib/ItemTable.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/matplotlib/Path.ipynb` & `holoviews-1.9.5/examples/reference/elements/matplotlib/Path.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/matplotlib/Points.ipynb` & `holoviews-1.9.5/examples/reference/elements/matplotlib/Points.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/matplotlib/Polygons.ipynb` & `holoviews-1.9.5/examples/reference/elements/matplotlib/Polygons.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/matplotlib/QuadMesh.ipynb` & `holoviews-1.9.5/examples/reference/elements/matplotlib/QuadMesh.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/matplotlib/Raster.ipynb` & `holoviews-1.9.5/examples/reference/elements/matplotlib/Raster.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/matplotlib/RGB.ipynb` & `holoviews-1.9.5/examples/reference/elements/matplotlib/RGB.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/matplotlib/Scatter.ipynb` & `holoviews-1.9.5/examples/reference/elements/matplotlib/Scatter.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/matplotlib/Scatter3D.ipynb` & `holoviews-1.9.5/examples/reference/elements/matplotlib/Scatter3D.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/matplotlib/Spikes.ipynb` & `holoviews-1.9.5/examples/reference/elements/matplotlib/Spikes.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/matplotlib/Spline.ipynb` & `holoviews-1.9.5/examples/reference/elements/matplotlib/Spline.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/matplotlib/Spread.ipynb` & `holoviews-1.9.5/examples/reference/elements/matplotlib/Spread.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/matplotlib/Surface.ipynb` & `holoviews-1.9.5/examples/reference/elements/matplotlib/Surface.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/matplotlib/Table.ipynb` & `holoviews-1.9.5/examples/reference/elements/matplotlib/Table.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/matplotlib/Text.ipynb` & `holoviews-1.9.5/examples/reference/elements/matplotlib/Text.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/matplotlib/TriSurface.ipynb` & `holoviews-1.9.5/examples/reference/elements/matplotlib/TriSurface.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/matplotlib/VectorField.ipynb` & `holoviews-1.9.5/examples/reference/elements/matplotlib/VectorField.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/matplotlib/VLine.ipynb` & `holoviews-1.9.5/examples/reference/elements/matplotlib/VLine.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/plotly/BoxWhiskers.ipynb` & `holoviews-1.9.5/examples/reference/elements/plotly/BoxWhiskers.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/plotly/Curve.ipynb` & `holoviews-1.9.5/examples/reference/elements/plotly/Curve.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/plotly/Distribution.ipynb` & `holoviews-1.9.5/examples/reference/elements/plotly/Distribution.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/plotly/ErrorBars.ipynb` & `holoviews-1.9.5/examples/reference/elements/plotly/ErrorBars.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/plotly/HeatMap.ipynb` & `holoviews-1.9.5/examples/reference/elements/plotly/HeatMap.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/plotly/Image.ipynb` & `holoviews-1.9.5/examples/reference/elements/plotly/Image.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/plotly/ItemTable.ipynb` & `holoviews-1.9.5/examples/reference/elements/plotly/ItemTable.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/plotly/Points.ipynb` & `holoviews-1.9.5/examples/reference/elements/plotly/Points.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/plotly/Raster.ipynb` & `holoviews-1.9.5/examples/reference/elements/plotly/Raster.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/plotly/Scatter.ipynb` & `holoviews-1.9.5/examples/reference/elements/plotly/Scatter.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/plotly/Scatter3D.ipynb` & `holoviews-1.9.5/examples/reference/elements/plotly/Scatter3D.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/plotly/Surface.ipynb` & `holoviews-1.9.5/examples/reference/elements/plotly/Surface.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/plotly/Table.ipynb` & `holoviews-1.9.5/examples/reference/elements/plotly/Table.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/elements/plotly/TriSurface.ipynb` & `holoviews-1.9.5/examples/reference/elements/plotly/TriSurface.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/features/bokeh/table_hooks_example.ipynb` & `holoviews-1.9.5/examples/reference/features/bokeh/table_hooks_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/streams/bokeh/Bounds.ipynb` & `holoviews-1.9.5/examples/reference/streams/bokeh/Bounds.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/streams/bokeh/BoundsX.ipynb` & `holoviews-1.9.5/examples/reference/streams/bokeh/BoundsX.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/streams/bokeh/BoundsY.ipynb` & `holoviews-1.9.5/examples/reference/streams/bokeh/BoundsY.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/streams/bokeh/PointerX.ipynb` & `holoviews-1.9.5/examples/reference/streams/bokeh/PointerX.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/streams/bokeh/PointerXY.ipynb` & `holoviews-1.9.5/examples/reference/streams/bokeh/PointerXY.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/streams/bokeh/RangeXY.ipynb` & `holoviews-1.9.5/examples/reference/streams/bokeh/RangeXY.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/streams/bokeh/Selection1D.ipynb` & `holoviews-1.9.5/examples/reference/streams/bokeh/Selection1D.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/streams/bokeh/Selection1D_paired.ipynb` & `holoviews-1.9.5/examples/reference/streams/bokeh/Selection1D_paired.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/streams/bokeh/Selection1D_points.ipynb` & `holoviews-1.9.5/examples/reference/streams/bokeh/Selection1D_points.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/streams/bokeh/Selection1D_tap.ipynb` & `holoviews-1.9.5/examples/reference/streams/bokeh/Selection1D_tap.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/reference/streams/bokeh/Tap.ipynb` & `holoviews-1.9.5/examples/reference/streams/bokeh/Tap.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/topics/geometry/lsystems.ipynb` & `holoviews-1.9.5/examples/topics/geometry/lsystems.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/topics/geometry/square_limit.ipynb` & `holoviews-1.9.5/examples/topics/geometry/square_limit.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/topics/simulation/boids.ipynb` & `holoviews-1.9.5/examples/topics/simulation/boids.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/topics/simulation/hipster_dynamics.ipynb` & `holoviews-1.9.5/examples/topics/simulation/hipster_dynamics.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/topics/simulation/sri_model.ipynb` & `holoviews-1.9.5/examples/topics/simulation/sri_model.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/user_guide/01-Annotating_Data.ipynb` & `holoviews-1.9.5/examples/user_guide/01-Annotating_Data.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/user_guide/02-Composing_Elements.ipynb` & `holoviews-1.9.5/examples/user_guide/02-Composing_Elements.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/user_guide/03-Customizing_Plots.ipynb` & `holoviews-1.9.5/examples/user_guide/03-Customizing_Plots.ipynb`

 * *Files 2% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9848118279569893%*

 * *Differences: {"'cells'": "{13: {'source': ['Although it is as simple as possible, this format is tedious and "*

 * *            'verbose to use: HoloViews allows you to specify *all* your options separate from your '*

 * *            'elements in one specifiation which means there is a minimum possible complexity. For '*

 * *            'this reason, the most commonly used format is the succinct string format describe '*

 * *            "below, which is parsed into the dictionary format behind the scenes.']}, 14: "*

 * *            "{'source':  […]*

```diff
@@ -177,53 +177,93 @@
                 "layout"
             ]
         },
         {
             "cell_type": "markdown",
             "metadata": {},
             "source": [
-                "The straight line has no ``group`` and ``label`` so it gets 'blue' from the ``Curve`` level of specificity. The two sine curves are red as they both have the ``group`` specification of 'Sinusoid'. Lastly we has a sine squared curve with the same ``group`` label of 'Sinusoid' but it also has the ``label`` 'Squared' which is why it is green."
+                "The straight line has no ``group`` and ``label`` so it gets 'blue' from the ``Curve`` level of specificity. The two sine curves are red as they both have the ``group`` specification of 'Sinusoid'. Lastly we has a sine squared curve with the same ``group`` label of 'Sinusoid' but it also has the ``label`` 'Squared' which is why it is green.\n",
+                "\n",
+                "#### Dictionary format\n",
+                "\n",
+                "HoloViews avoids string parsing and special syntax (other than the basic operators described in [Composing Elements](./02-Composing_Elements.ipynb)) where possible. For this reason, all options are fundamentally reduced to a simple dictionary format. For example, here is the pure Python equivalent of the options shown above, using the ``opts`` method that will be described shortly:"
+            ]
+        },
+        {
+            "cell_type": "code",
+            "execution_count": null,
+            "metadata": {},
+            "outputs": [],
+            "source": [
+                "dict_spec = {'Curve': {'style':dict(color='blue')}, \n",
+                "             'Curve.Sinusoid': {'style':dict(color='red')}, \n",
+                "             'Curve.Sinusoid.Squared ': {'style':dict(color='green'),\n",
+                "                                         'plot':dict(interpolation='steps-mid')}}\n",
+                "\n",
+                "dcurve = hv.Curve((xs, xs/3))\n",
+                "dgroup_curve1 = hv.Curve((xs, np.sin(xs)), group='Sinusoid')\n",
+                "dgroup_curve2 = hv.Curve((xs, np.sin(xs+np.pi/4)), group='Sinusoid')\n",
+                "dlabel_curve = hv.Curve((xs, np.sin(xs)**2), group='Sinusoid', label='Squared')\n",
+                "dlayout = dcurve * dgroup_curve1 * dgroup_curve2 * dlabel_curve\n",
+                "dlayout.opts(dict_spec)"
             ]
         },
         {
             "cell_type": "markdown",
             "metadata": {},
             "source": [
-                "#### Dictionary format"
+                "Although it is as simple as possible, this format is tedious and verbose to use: HoloViews allows you to specify *all* your options separate from your elements in one specifiation which means there is a minimum possible complexity. For this reason, the most commonly used format is the succinct string format describe below, which is parsed into the dictionary format behind the scenes."
             ]
         },
         {
             "cell_type": "markdown",
             "metadata": {},
             "source": [
-                "HoloViews avoids string parsing and special syntax (other than the basic operators described in [Composing Elements](./02-Composing_Elements.ipynb)) where possible. For this reason, all options are fundamentally reduced to a simple dictionary format. For example, here is the pure Python equivalent of the options shown above, using the ``opts`` method that will be described shortly:"
+                "#### Simplified format"
+            ]
+        },
+        {
+            "cell_type": "markdown",
+            "metadata": {},
+            "source": [
+                "The dictionary format above can be quite cumbersome to work with, therefore HoloViews provides a simpler ``.options`` method, which automatically distinguishes between ``plot``, ``style`` and ``norm`` options. We can take advantage of this to easily apply a mixture of options:"
             ]
         },
         {
             "cell_type": "code",
             "execution_count": null,
             "metadata": {},
             "outputs": [],
             "source": [
-                "dict_spec = {'Curve':{'style':dict(color='blue')}, \n",
-                "             'Curve.Sinusoid':{'style':dict(color='red')}, \n",
-                "             'Curve.Sinusoid.Squared ': {'style':dict(color='green'), 'plot':dict(interpolation='steps-mid')}}\n",
-                "dcurve = hv.Curve((xs, xs/3))\n",
-                "dgroup_curve1 = hv.Curve((xs, np.sin(xs)), group='Sinusoid')\n",
-                "dgroup_curve2 = hv.Curve((xs, np.sin(xs+np.pi/4)), group='Sinusoid')\n",
-                "dlabel_curve = hv.Curve((xs, np.sin(xs)**2), group='Sinusoid', label='Squared')\n",
-                "dlayout = dcurve * dgroup_curve1 * dgroup_curve2 * dlabel_curve\n",
-                "dlayout.opts(dict_spec)"
+                "hv.Curve((xs, np.sin(xs))).options(width=500, color='red')"
             ]
         },
         {
             "cell_type": "markdown",
             "metadata": {},
             "source": [
-                "Although it is as simple as possible, this format is tedious and verbose to use: HoloViews allows you to specify *all* your options separate from your elements in one specifiation which means there is a minimum possible complexity. For this reason, the most commonly used format is the succinct string format describe below, which is parsed into the dictionary format behind the scenes."
+                "In a simple case like above where we are setting options that apply to the ``Curve`` element directly on a ``Curve`` we do not need to qualify further. However, when we are a composite object like an ``Overlay`` or ``Layout``, we have to be explicit about the object we are customizing, again using the ``type[[.group].label]`` specification."
+            ]
+        },
+        {
+            "cell_type": "code",
+            "execution_count": null,
+            "metadata": {},
+            "outputs": [],
+            "source": [
+                "curve = hv.Curve((xs, np.sin(xs+np.pi/4)))\n",
+                "stepped_curve = hv.Curve((xs, np.sin(xs)**2), group='Stepped')\n",
+                "area = hv.Area((xs, np.sin(xs)**2))\n",
+                "negative_area = hv.Area((xs, -(np.sin(xs)**2)), group='Negative')\n",
+                "\n",
+                "options = {'Curve': dict(width=500, color='red'),\n",
+                "           'Curve.Stepped': dict(color='green', interpolation='steps-mid'),\n",
+                "           'Area.Negative': dict(color='red')}\n",
+                "\n",
+                "(curve * stepped_curve + area * negative_area).options(options)"
             ]
         },
         {
             "cell_type": "markdown",
             "metadata": {},
             "source": [
                 "#### Yaml equivalent\n",
```

### Comparing `holoviews-1.9.4/examples/user_guide/04-Dimensioned_Containers.ipynb` & `holoviews-1.9.5/examples/user_guide/04-Dimensioned_Containers.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/user_guide/05-Building_Composite_Objects.ipynb` & `holoviews-1.9.5/examples/user_guide/05-Building_Composite_Objects.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/user_guide/06-Live_Data.ipynb` & `holoviews-1.9.5/examples/user_guide/06-Live_Data.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/user_guide/07-Tabular_Datasets.ipynb` & `holoviews-1.9.5/examples/user_guide/07-Tabular_Datasets.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/user_guide/08-Gridded_Datasets.ipynb` & `holoviews-1.9.5/examples/user_guide/08-Gridded_Datasets.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/user_guide/09-Indexing_and_Selecting_Data.ipynb` & `holoviews-1.9.5/examples/user_guide/09-Indexing_and_Selecting_Data.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/user_guide/10-Transforming_Elements.ipynb` & `holoviews-1.9.5/examples/user_guide/10-Transforming_Elements.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/user_guide/11-Responding_to_Events.ipynb` & `holoviews-1.9.5/examples/user_guide/11-Responding_to_Events.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/user_guide/12-Custom_Interactivity.ipynb` & `holoviews-1.9.5/examples/user_guide/12-Custom_Interactivity.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/user_guide/13-Data_Pipelines.ipynb` & `holoviews-1.9.5/examples/user_guide/13-Data_Pipelines.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/user_guide/14-Large_Data.ipynb` & `holoviews-1.9.5/examples/user_guide/14-Large_Data.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/user_guide/15-Streaming_Data.ipynb` & `holoviews-1.9.5/examples/user_guide/15-Streaming_Data.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/user_guide/16-Dashboards.ipynb` & `holoviews-1.9.5/examples/user_guide/16-Dashboards.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/user_guide/Continuous_Coordinates.ipynb` & `holoviews-1.9.5/examples/user_guide/Continuous_Coordinates.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/user_guide/Deploying_Bokeh_Apps.ipynb` & `holoviews-1.9.5/examples/user_guide/Deploying_Bokeh_Apps.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/user_guide/Exporting_and_Archiving.ipynb` & `holoviews-1.9.5/examples/user_guide/Exporting_and_Archiving.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/user_guide/Installing_and_Configuring.ipynb` & `holoviews-1.9.5/examples/user_guide/Installing_and_Configuring.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/user_guide/Network_Graphs.ipynb` & `holoviews-1.9.5/examples/user_guide/Network_Graphs.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/user_guide/Plots_and_Renderers.ipynb` & `holoviews-1.9.5/examples/user_guide/Plots_and_Renderers.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/user_guide/Plotting_with_Bokeh.ipynb` & `holoviews-1.9.5/examples/user_guide/Plotting_with_Bokeh.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/user_guide/Plotting_with_Matplotlib.ipynb` & `holoviews-1.9.5/examples/user_guide/Plotting_with_Matplotlib.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/examples/user_guide/Tips_and_Tricks.ipynb` & `holoviews-1.9.5/examples/user_guide/Tips_and_Tricks.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/__init__.py` & `holoviews-1.9.5/holoviews/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 
 from __future__ import print_function, absolute_import
 import os, pydoc
 
 import numpy as np # noqa (API import)
 import param
 
-__version__ = param.Version(release=(1,9,4), fpath=__file__,
+__version__ = param.Version(release=(1,9,5), fpath=__file__,
                             commit="$Format:%h$", reponame='holoviews')
 
 from .core import archive, config                        # noqa (API import)
 from .core.dimension import OrderedDict, Dimension       # noqa (API import)
 from .core.boundingregion import BoundingBox             # noqa (API import)
 from .core.options import (Options, Store, Cycle,        # noqa (API import)
                            Palette, StoreOptions)
```

### Comparing `holoviews-1.9.4/holoviews/core/__init__.py` & `holoviews-1.9.5/holoviews/core/__init__.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/core/boundingregion.py` & `holoviews-1.9.5/holoviews/core/boundingregion.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/core/data/__init__.py` & `holoviews-1.9.5/holoviews/core/data/__init__.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/core/data/array.py` & `holoviews-1.9.5/holoviews/core/data/array.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/core/data/dask.py` & `holoviews-1.9.5/holoviews/core/data/dask.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/core/data/dictionary.py` & `holoviews-1.9.5/holoviews/core/data/dictionary.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/core/data/grid.py` & `holoviews-1.9.5/holoviews/core/data/grid.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/core/data/image.py` & `holoviews-1.9.5/holoviews/core/data/image.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/core/data/interface.py` & `holoviews-1.9.5/holoviews/core/data/interface.py`

 * *Files 1% similar despite different names*

```diff
@@ -281,17 +281,20 @@
     @classmethod
     def range(cls, dataset, dimension):
         column = dataset.dimension_values(dimension)
         if column.dtype.kind == 'M':
             return column.min(), column.max()
         else:
             try:
+                assert column.dtype.kind not in 'SUO'
                 return (np.nanmin(column), np.nanmax(column))
-            except TypeError:
-                column.sort()
+            except (AssertionError, TypeError):
+                column = [v for v in util.python2sort(column) if v is not None]
+                if not len(column):
+                    return np.NaN, np.NaN
                 return column[0], column[-1]
 
     @classmethod
     def concatenate(cls, dataset, datatype=None):
         """
         Utility function to concatenate a list of Column objects,
         returning a new Dataset object. Note that this is unlike the
```

### Comparing `holoviews-1.9.4/holoviews/core/data/iris.py` & `holoviews-1.9.5/holoviews/core/data/iris.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/core/data/multipath.py` & `holoviews-1.9.5/holoviews/core/data/multipath.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/core/data/pandas.py` & `holoviews-1.9.5/holoviews/core/data/pandas.py`

 * *Files 1% similar despite different names*

```diff
@@ -122,14 +122,17 @@
         column = columns.data[columns.get_dimension(dimension, strict=True).name]
         if column.dtype.kind == 'O':
             if (not isinstance(columns.data, pd.DataFrame) or
                         LooseVersion(pd.__version__) < '0.17.0'):
                 column = column.sort(inplace=False)
             else:
                 column = column.sort_values()
+            column = column[~column.isin([None])]
+            if not len(column):
+                return np.NaN, np.NaN
             return column.iloc[0], column.iloc[-1]
         else:
             return (column.min(), column.max())
 
 
     @classmethod
     def concat(cls, columns_objs):
```

### Comparing `holoviews-1.9.4/holoviews/core/data/xarray.py` & `holoviews-1.9.5/holoviews/core/data/xarray.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/core/dimension.py` & `holoviews-1.9.5/holoviews/core/dimension.py`

 * *Files 3% similar despite different names*

```diff
@@ -1082,37 +1082,51 @@
 
     def __call__(self, options=None, **kwargs):
         if config.warn_options_call:
             self.warning('Use of __call__ to set options will be deprecated '
                          'in future. Use the equivalent opts method instead.')
         return self.opts(options, **kwargs)
 
-    def opts(self, options=None, **kwargs):
+    def opts(self, options=None, backend=None, clone=True, **kwargs):
         """
-        Apply the supplied options to a clone of the object which is
-        then returned. Note that if no options are supplied at all,
-        all ids are reset.
+        Applies options on an object or nested group of objects in a
+        by options group returning a new object with the options
+        applied. If the options are to be set directly on the object a
+        simple format may be used, e.g.:
+
+            obj.opts(style={'cmap': 'viridis'}, plot={'show_title': False})
+
+        If the object is nested the options must be qualified using
+        a type[.group][.label] specification, e.g.:
+
+            obj.opts({'Image': {'plot':  {'show_title': False},
+                                'style': {'cmap': 'viridis}}})
+
+        If no opts are supplied all options on the object will be reset.
+        Disabling clone will modify the object inplace.
         """
-        from ..util.parser import OptsSpec
+        backend = backend or Store.current_backend
         if isinstance(options, basestring):
+            from ..util.parser import OptsSpec
             try:
                 options = OptsSpec.parse(options)
             except SyntaxError:
                 options = OptsSpec.parse(
                     '{clsname} {options}'.format(clsname=self.__class__.__name__,
                                                  options=options))
 
-        groups = set(Store.options().groups.keys())
+        backend_options = Store.options(backend=backend)
+        groups = set(backend_options.groups.keys())
         if kwargs and set(kwargs) <= groups:
             if not all(isinstance(v, dict) for v in kwargs.values()):
                 raise Exception("The %s options must be specified using dictionary groups" %
                                 ','.join(repr(k) for k in kwargs.keys()))
 
             # Check whether the user is specifying targets (such as 'Image.Foo')
-            entries = Store.options().children
+            entries = backend_options.children
             targets = [k.split('.')[0] in entries for grp in kwargs.values() for k in grp]
             if any(targets) and not all(targets):
                 raise Exception("Cannot mix target specification keys such as 'Image' with non-target keywords.")
             elif not any(targets):
                 # Not targets specified - add current object as target
                 sanitized_group = group_sanitizer(self.group)
                 if self.label:
@@ -1122,20 +1136,62 @@
                 elif  sanitized_group != self.__class__.__name__:
                     identifier = '%s.%s' % (self.__class__.__name__, sanitized_group)
                 else:
                     identifier = self.__class__.__name__
 
                 kwargs = {k:{identifier:v} for k,v in kwargs.items()}
 
-        if options is None and kwargs=={}:
-            deep_clone = self.map(lambda x: x.clone(id=None))
-        else:
-            deep_clone = self.map(lambda x: x.clone(id=x.id))
-        StoreOptions.set_options(deep_clone, options, **kwargs)
-        return deep_clone
+        obj = self
+        if options is None and kwargs == {}:
+            if clone:
+                obj = self.map(lambda x: x.clone(id=None))
+            else:
+                self.map(lambda x: setattr(x, 'id', None))
+        elif clone:
+            obj = self.map(lambda x: x.clone(id=x.id))
+        StoreOptions.set_options(obj, options, backend=backend, **kwargs)
+        return obj
+
+
+    def options(self, options=None, backend=None, clone=True, **kwargs):
+        """
+        Applies options on an object or nested group of objects in a
+        flat format returning a new object with the options
+        applied. If the options are to be set directly on the object a
+        simple format may be used, e.g.:
+
+            obj.options(cmap='viridis', show_title=False)
+
+        If the object is nested the options must be qualified using
+        a type[.group][.label] specification, e.g.:
+
+            obj.options('Image', cmap='viridis', show_title=False)
+
+        or using:
+
+            obj.options({'Image': dict(cmap='viridis', show_title=False)})
+
+        If no options are supplied all options on the object will be reset.
+        Disabling clone will modify the object inplace.
+        """
+        if isinstance(options, basestring):
+            options = {options: kwargs}
+        elif options and kwargs:
+            raise ValueError("Options must be defined in one of two formats."
+                             "Either supply keywords defining the options for "
+                             "the current object, e.g. obj.options(cmap='viridis'), "
+                             "or explicitly define the type, e.g."
+                             "obj.options({'Image': {'cmap': 'viridis'}})."
+                             "Supplying both formats is not supported.")
+        elif kwargs:
+            options = {type(self).__name__: kwargs}
+
+        from ..util import opts
+        expanded = opts.expand_options(options, backend)
+        return self.opts(expanded, backend, clone)
 
 
 
 class ViewableElement(Dimensioned):
     """
     A ViewableElement is a dimensioned datastructure that may be
     associated with a corresponding atomic visualization. An atomic
```

### Comparing `holoviews-1.9.4/holoviews/core/element.py` & `holoviews-1.9.5/holoviews/core/element.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/core/io.py` & `holoviews-1.9.5/holoviews/core/io.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/core/layout.py` & `holoviews-1.9.5/holoviews/core/layout.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/core/ndmapping.py` & `holoviews-1.9.5/holoviews/core/ndmapping.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/core/operation.py` & `holoviews-1.9.5/holoviews/core/operation.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/core/options.py` & `holoviews-1.9.5/holoviews/core/options.py`

 * *Files 0% similar despite different names*

```diff
@@ -1322,21 +1322,21 @@
             for grp in tree[k].groups:
                 kwargs = tree[k].groups[grp].kwargs
                 if kwargs:
                     specs[spec_key][grp] = kwargs
         return specs
 
     @classmethod
-    def propagate_ids(cls, obj, match_id, new_id, applied_keys):
+    def propagate_ids(cls, obj, match_id, new_id, applied_keys, backend=None):
         """
         Recursively propagate an id through an object for components
         matching the applied_keys. This method can only be called if
         there is a tree with a matching id in Store.custom_options
         """
-        if not new_id in Store.custom_options():
+        if not new_id in Store.custom_options(backend=backend):
             raise AssertionError("The set_ids method requires "
                                  "Store.custom_options to contain"
                                  " a tree with id %d" % new_id)
         def propagate(o):
             if o.id == match_id or (o.__class__.__name__ == 'DynamicMap'):
                 setattr(o, 'id', new_id)
         obj.traverse(propagate, specs=set(applied_keys) | {'DynamicMap'})
@@ -1385,15 +1385,15 @@
         the specified backends by raising OptionError for invalid
         options. If backends is None, validates against all the
         currently loaded backend.
 
         Only useful when invalid keywords generate exceptions instead of
         skipping i.e Options.skip_invalid is False.
         """
-        loaded_backends =  Store.loaded_backends()if backends is None else backends
+        loaded_backends =  Store.loaded_backends() if backends is None else backends
 
         error_info     = {}
         backend_errors = defaultdict(set)
         for backend in loaded_backends:
             cls.start_recording_skipped()
             with options_policy(skip_invalid=True, warn_on_skip=False):
                 options = OptionTree(items=Store.options(backend).data.items(),
@@ -1403,14 +1403,15 @@
             for error in cls.stop_recording_skipped():
                 error_key = (error.invalid_keyword,
                              error.allowed_keywords.target,
                              error.group_name)
                 error_info[error_key+(backend,)] = error.allowed_keywords
                 backend_errors[error_key].add(backend)
 
+
         for ((keyword, target, group_name), backends) in backend_errors.items():
             # If the keyword failed for the target across all loaded backends...
             if set(backends) == set(loaded_backends):
                 key = (keyword, target, group_name, Store.current_backend)
                 raise OptionError(keyword,
                                   group_name=group_name,
                                   allowed_keywords=error_info[key])
@@ -1645,11 +1646,11 @@
         # syntax can also be used:
 
         # {'Image.Channel:{'plot':  Options(size=50),
         #                  'style': Options('style', cmap='Blues')]}
         options = cls.merge_options(Store.options(backend=backend).groups.keys(), options, **kwargs)
         spec, compositor_applied = cls.expand_compositor_keys(options)
         custom_trees, id_mapping = cls.create_custom_trees(obj, spec)
-        cls.update_backends(id_mapping, custom_trees)
+        cls.update_backends(id_mapping, custom_trees, backend=backend)
         for (match_id, new_id) in id_mapping:
-            cls.propagate_ids(obj, match_id, new_id, compositor_applied+list(spec.keys()))
+            cls.propagate_ids(obj, match_id, new_id, compositor_applied+list(spec.keys()), backend=backend)
         return obj
```

### Comparing `holoviews-1.9.4/holoviews/core/overlay.py` & `holoviews-1.9.5/holoviews/core/overlay.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/core/pprint.py` & `holoviews-1.9.5/holoviews/core/pprint.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/core/sheetcoords.py` & `holoviews-1.9.5/holoviews/core/sheetcoords.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/core/spaces.py` & `holoviews-1.9.5/holoviews/core/spaces.py`

 * *Files 1% similar despite different names*

```diff
@@ -853,28 +853,71 @@
             kwargs['memoization_hash'] = hash_items
 
         with dynamicmap_memoization(self.callback, self.streams):
             retval = self.callback(*args, **kwargs)
         return self._style(retval)
 
 
-    def opts(self, options=None, **kwargs):
+    def opts(self, options=None, backend=None, clone=True, **kwargs):
         """
-        Apply the supplied options to a clone of the DynamicMap which is
-        then returned. Note that if no options are supplied at all,
-        all ids are reset.
+        Applies options on an object or nested group of objects in a
+        by options group returning a new object with the options
+        applied. If the options are to be set directly on the object a
+        simple format may be used, e.g.:
+
+            obj.opts(style={'cmap': 'viridis'}, plot={'show_title': False})
+
+        If the object is nested the options must be qualified using
+        a type[.group][.label] specification, e.g.:
+
+            obj.opts({'Image': {'plot':  {'show_title': False},
+                                'style': {'cmap': 'viridis}}})
+
+        If no opts are supplied all options on the object will be reset.
+        Disabling clone will modify the object inplace.
         """
         from ..util import Dynamic
-        dmap = Dynamic(self, operation=lambda obj, **dynkwargs: obj.opts(options, **kwargs),
+        dmap = Dynamic(self, operation=lambda obj, **dynkwargs: obj.opts(options, backend,
+                                                                         clone, **kwargs),
                        streams=self.streams, link_inputs=True)
         dmap.data = OrderedDict([(k, v.opts(options, **kwargs))
                                  for k, v in self.data.items()])
         return dmap
 
 
+    def options(self, options=None, backend=None, clone=True, **kwargs):
+        """
+        Applies options on an object or nested group of objects in a
+        flat format returning a new object with the options
+        applied. If the options are to be set directly on the object a
+        simple format may be used, e.g.:
+
+            obj.options(cmap='viridis', show_title=False)
+
+        If the object is nested the options must be qualified using
+        a type[.group][.label] specification, e.g.:
+
+            obj.options('Image', cmap='viridis', show_title=False)
+
+        or using:
+
+            obj.options({'Image': dict(cmap='viridis', show_title=False)})
+
+        If no options are supplied all options on the object will be reset.
+        Disabling clone will modify the object inplace.
+        """
+        from ..util import Dynamic
+        dmap = Dynamic(self, operation=lambda obj, **dynkwargs: obj.options(options, backend,
+                                                                            clone, **kwargs),
+                       streams=self.streams, link_inputs=True)
+        dmap.data = OrderedDict([(k, v.options(options, backend, **kwargs))
+                                 for k, v in self.data.items()])
+        return dmap
+
+
     def clone(self, data=None, shared_data=True, new_type=None, link_inputs=True,
               *args, **overrides):
         """
         Clone method to adapt the slightly different signature of
         DynamicMap that also overrides Dimensioned clone to avoid
         checking items if data is unchanged.
         """
```

### Comparing `holoviews-1.9.4/holoviews/core/traversal.py` & `holoviews-1.9.5/holoviews/core/traversal.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/core/tree.py` & `holoviews-1.9.5/holoviews/core/tree.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/core/util.py` & `holoviews-1.9.5/holoviews/core/util.py`

 * *Files 0% similar despite different names*

```diff
@@ -712,15 +712,15 @@
         with warnings.catch_warnings():
             warnings.filterwarnings('ignore', r'All-NaN (slice|axis) encountered')
             values = [r for r in ranges for v in r if v is not None]
             if pd and all(isinstance(v, pd.Timestamp) for r in values for v in r):
                 values = [(v1.to_datetime64(), v2.to_datetime64()) for v1, v2 in values]
             arr = np.array(values)
             if arr.dtype.kind in 'OSU':
-                arr = np.sort([v for v in arr.flat if not is_nan(v)])
+                arr = list(python2sort([v for v in arr.flat if not is_nan(v) and v is not None]))
                 return arr[0], arr[-1]
             if arr.dtype.kind in 'M':
                 return arr[:, 0].min(), arr[:, 1].max()
             return (np.nanmin(arr[:, 0]), np.nanmax(arr[:, 1]))
     except:
         return (np.NaN, np.NaN)
```

### Comparing `holoviews-1.9.4/holoviews/element/__init__.py` & `holoviews-1.9.5/holoviews/element/__init__.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/element/annotation.py` & `holoviews-1.9.5/holoviews/element/annotation.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/element/chart.py` & `holoviews-1.9.5/holoviews/element/chart.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/element/chart3d.py` & `holoviews-1.9.5/holoviews/element/chart3d.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/element/comparison.py` & `holoviews-1.9.5/holoviews/element/comparison.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/element/graphs.py` & `holoviews-1.9.5/holoviews/element/graphs.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/element/path.py` & `holoviews-1.9.5/holoviews/element/path.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/element/raster.py` & `holoviews-1.9.5/holoviews/element/raster.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/element/stats.py` & `holoviews-1.9.5/holoviews/element/stats.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/element/tabular.py` & `holoviews-1.9.5/holoviews/element/tabular.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/element/util.py` & `holoviews-1.9.5/holoviews/element/util.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/assets/diseases.csv.gz` & `holoviews-1.9.5/holoviews/examples/assets/diseases.csv.gz`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/assets/fb_edges.csv` & `holoviews-1.9.5/holoviews/examples/assets/fb_edges.csv`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/assets/fb_nodes.csv` & `holoviews-1.9.5/holoviews/examples/assets/fb_nodes.csv`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/assets/hourly_taxi_data.npz` & `holoviews-1.9.5/holoviews/examples/assets/hourly_taxi_data.npz`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/assets/penguins.png` & `holoviews-1.9.5/holoviews/examples/assets/penguins.png`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/assets/spike_train.csv.gz` & `holoviews-1.9.5/holoviews/examples/assets/spike_train.csv.gz`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/assets/station_info.csv` & `holoviews-1.9.5/holoviews/examples/assets/station_info.csv`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/assets/twophoton.npz` & `holoviews-1.9.5/holoviews/examples/assets/twophoton.npz`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/apps/bokeh/crossfilter.py` & `holoviews-1.9.5/holoviews/examples/gallery/apps/bokeh/crossfilter.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/apps/bokeh/game_of_life.py` & `holoviews-1.9.5/holoviews/examples/gallery/apps/bokeh/game_of_life.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/apps/bokeh/gapminder.py` & `holoviews-1.9.5/holoviews/examples/gallery/apps/bokeh/gapminder.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/apps/bokeh/mandelbrot.py` & `holoviews-1.9.5/holoviews/examples/gallery/apps/bokeh/mandelbrot.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/apps/bokeh/nytaxi_hover.py` & `holoviews-1.9.5/holoviews/examples/gallery/apps/bokeh/nytaxi_hover.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/apps/bokeh/streaming_psutil.py` & `holoviews-1.9.5/holoviews/examples/gallery/apps/bokeh/streaming_psutil.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/area_chart.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/area_chart.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/autompg_histogram.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/autompg_histogram.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/bachelors_degrees_by_gender.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/bachelors_degrees_by_gender.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/bars_economic.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/bars_economic.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/boxplot_chart.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/boxplot_chart.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/dot_example.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/dot_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/dragon_curve.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/dragon_curve.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/dropdown_economic.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/dropdown_economic.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/histogram_example.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/histogram_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/iris_density_grid.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/iris_density_grid.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/iris_example.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/iris_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/iris_grouped_grid.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/iris_grouped_grid.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/iris_splom_example.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/iris_splom_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/legend_example.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/legend_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/lesmis_example.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/lesmis_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/lorenz_attractor_example.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/lorenz_attractor_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/mandelbrot_section.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/mandelbrot_section.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/measles_example.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/measles_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/network_graph.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/network_graph.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/quiver_demo.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/quiver_demo.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/scatter_economic.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/scatter_economic.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/square_limit.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/square_limit.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/step_chart.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/step_chart.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/stocks_example.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/stocks_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/texas_choropleth_example.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/texas_choropleth_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/topographic_hillshading.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/topographic_hillshading.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/us_unemployment.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/us_unemployment.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/bokeh/verhulst_mandelbrot.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/bokeh/verhulst_mandelbrot.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/area_chart.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/area_chart.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/autompg_histogram.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/autompg_histogram.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/bachelors_degrees_by_gender.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/bachelors_degrees_by_gender.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/bars_economic.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/bars_economic.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/boxplot_chart.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/boxplot_chart.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/dragon_curve.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/dragon_curve.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/dropdown_economic.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/dropdown_economic.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/histogram_example.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/histogram_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/iris_density_grid.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/iris_density_grid.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/iris_example.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/iris_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/iris_grouped_grid.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/iris_grouped_grid.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/iris_splom_example.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/iris_splom_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/legend_example.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/legend_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/lorenz_attractor_example.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/lorenz_attractor_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/mandelbrot_section.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/mandelbrot_section.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/measles_example.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/measles_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/network_graph.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/network_graph.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/polar_scatter_demo.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/polar_scatter_demo.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/quiver_demo.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/quiver_demo.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/scatter_economic.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/scatter_economic.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/square_limit.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/square_limit.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/step_chart.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/step_chart.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/stocks_example.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/stocks_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/surface_3d.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/surface_3d.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/texas_choropleth_example.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/texas_choropleth_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/topographic_hillshading.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/topographic_hillshading.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/trisurf3d_demo.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/trisurf3d_demo.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/us_unemployment.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/us_unemployment.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/matplotlib/verhulst_mandelbrot.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/matplotlib/verhulst_mandelbrot.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/plotly/surface_3d.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/plotly/surface_3d.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/gallery/demos/plotly/trisurf3d_demo.ipynb` & `holoviews-1.9.5/holoviews/examples/gallery/demos/plotly/trisurf3d_demo.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/getting_started/1-Introduction.ipynb` & `holoviews-1.9.5/holoviews/examples/getting_started/1-Introduction.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/getting_started/2-Customization.ipynb` & `holoviews-1.9.5/holoviews/examples/getting_started/2-Customization.ipynb`

 * *Files 8% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9819529291979949%*

 * *Differences: {"'cells'": "{13: {'source': {insert: [(6, '(curve + spikes).cols(1)')], delete: [6]}}, 14: "*

 * *            "{'source': {insert: [(17, 'As you can see, these tools allow significant "*

 * *            'customization of how our elements appear. HoloViews offers many other tools for '*

 * *            'setting options either locally or globally, including the ``%output`` and ``%opts`` '*

 * *            '*line magics*, the ``.opts`` and ``.options`` methods on all HoloViews objects and '*

 * *            'the ``hv.output`` and ``h […]*

```diff
@@ -133,15 +133,15 @@
             "source": [
                 "%%output size=150\n",
                 "%%opts Curve  [height=100 width=600 xaxis=None tools=['hover']]\n",
                 "%%opts Curve (color='red' line_width=1.5)\n",
                 "%%opts Spikes [height=100 width=600 yaxis=None] (color='grey' line_width=0.25)\n",
                 "curve  = hv.Curve( spike_train, 'milliseconds', 'Hertz')\n",
                 "spikes = hv.Spikes(spike_train, 'milliseconds', [])\n",
-                "(curve+spikes).cols(1)"
+                "(curve + spikes).cols(1)"
             ]
         },
         {
             "cell_type": "markdown",
             "metadata": {},
             "source": [
                 "Much better! It's the same underlying data, but now we can clearly see both the individual spike events and how they affect the moving average.  You can also see how the moving average trails the actual spiking, due to how the window function was defined.\n",
@@ -157,15 +157,57 @@
                 "\n",
                 "* The element type is specified following by special groups of keywords.\n",
                 "* The keywords in square brackets ``[...]`` are ***plot options*** that instruct HoloViews how to build that type of plot.\n",
                 "* The keywords in parentheses ``(...)`` are **style options** with keywords that are passed directly to the plotting library when rendering that type of plot.\n",
                 "\n",
                 "The corresponding [User Guide](../user_guide/03-Customizing_Plots.ipynb) entry explains the keywords used in detail, but a quick summary is that we have elongated the ``Curve`` and ``Scatter`` elements and toggled various axes with the ***plot options***. We have also specified the color and line widths of the [Bokeh glyphs](http://bokeh.pydata.org/en/latest/docs/user_guide/plotting.html) with the ***style options***.\n",
                 "\n",
-                "As you can see, these tools allow significant customization of how our elements appear. HoloViews offers many other tools for setting options either locally or globally, including the ``%output`` and ``%opts`` *line magics*, the ``.opts`` method on all HoloViews objects and the ``hv.output`` and ``hv.opts`` utilities. All these tools, how they work and details of the opts syntax can be found in the [User Guide](../user_guide/03-Customizing_Plots.ipynb)."
+                "As you can see, these tools allow significant customization of how our elements appear. HoloViews offers many other tools for setting options either locally or globally, including the ``%output`` and ``%opts`` *line magics*, the ``.opts`` and ``.options`` methods on all HoloViews objects and the ``hv.output`` and ``hv.opts`` utilities. We will briefly consider the ``.options`` based approach, which makes it possible to work outside the notebook. All these tools, how they work and details of the opts syntax can be found in the [User Guide](../user_guide/03-Customizing_Plots.ipynb)."
+            ]
+        },
+        {
+            "cell_type": "markdown",
+            "metadata": {},
+            "source": [
+                "# Outside the notebook\n",
+                "\n",
+                "When working inside the notebook environment using the ``%%opts`` magic is a very convenient and powerful way of working because it allows tab-completion of the options however outside the notebook and when you're are customizing a specific object it is often useful to set the options directly on an object. The simplest way of doing so is using the ``.options`` method, which will automatically deduce whether an option is a ``style``, ``plot`` or ``norm`` option.\n",
+                "\n",
+                "To demonstrate this we can reproduce the plot above by combining both the plot and style options above into a flat set of options:"
+            ]
+        },
+        {
+            "cell_type": "code",
+            "execution_count": null,
+            "metadata": {},
+            "outputs": [],
+            "source": [
+                "curve_opts = dict(height=100, width=600, xaxis=None, tools=['hover'], color='red', line_width=1.5)\n",
+                "spike_opts = dict(height=100, width=600, yaxis=None, color='grey', line_width=0.25)\n",
+                "\n",
+                "curve = hv.Curve(spike_train, 'milliseconds', 'Hertz')\n",
+                "spikes = hv.Spikes(spike_train, 'milliseconds', [])\n",
+                "\n",
+                "(curve.options(**curve_opts) + spikes.options(**spike_opts)).cols(1)"
+            ]
+        },
+        {
+            "cell_type": "markdown",
+            "metadata": {},
+            "source": [
+                "When using ``.options`` to apply options directly to an individual object we do not have to explicitly declare which object the options apply to, however often it is useful to set options on a composite object. In these cases the options can be declared as a dictionary of the type name and the options. The code below is therefore equivalent to the syntax we used above:"
+            ]
+        },
+        {
+            "cell_type": "code",
+            "execution_count": null,
+            "metadata": {},
+            "outputs": [],
+            "source": [
+                "layout = (curve + spikes).options({'Curve': curve_opts, 'Spikes': spike_opts}).cols(1)"
             ]
         },
         {
             "cell_type": "markdown",
             "metadata": {},
             "source": [
                 "# Switching to matplotlib\n",
```

### Comparing `holoviews-1.9.4/holoviews/examples/getting_started/3-Tabular_Datasets.ipynb` & `holoviews-1.9.5/holoviews/examples/getting_started/3-Tabular_Datasets.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/getting_started/4-Gridded_Datasets.ipynb` & `holoviews-1.9.5/holoviews/examples/getting_started/4-Gridded_Datasets.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/getting_started/5-Live_Data.ipynb` & `holoviews-1.9.5/holoviews/examples/getting_started/5-Live_Data.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/README.md` & `holoviews-1.9.5/holoviews/examples/README.md`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/apps/bokeh/player.py` & `holoviews-1.9.5/holoviews/examples/reference/apps/bokeh/player.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/apps/bokeh/selection_stream.py` & `holoviews-1.9.5/holoviews/examples/reference/apps/bokeh/selection_stream.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/apps/bokeh/sine.py` & `holoviews-1.9.5/holoviews/examples/reference/apps/bokeh/sine.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/containers/bokeh/DynamicMap.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/containers/bokeh/DynamicMap.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/containers/bokeh/GridSpace.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/containers/bokeh/GridSpace.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/containers/bokeh/HoloMap.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/containers/bokeh/HoloMap.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/containers/bokeh/Layout.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/containers/bokeh/Layout.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/containers/bokeh/NdLayout.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/containers/bokeh/NdLayout.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/containers/bokeh/NdOverlay.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/containers/bokeh/NdOverlay.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/containers/bokeh/Overlay.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/containers/bokeh/Overlay.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/containers/matplotlib/DynamicMap.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/containers/matplotlib/DynamicMap.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/containers/matplotlib/GridSpace.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/containers/matplotlib/GridSpace.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/containers/matplotlib/HoloMap.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/containers/matplotlib/HoloMap.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/containers/matplotlib/Layout.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/containers/matplotlib/Layout.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/containers/matplotlib/NdLayout.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/containers/matplotlib/NdLayout.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/containers/matplotlib/NdOverlay.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/containers/matplotlib/NdOverlay.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/containers/matplotlib/Overlay.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/containers/matplotlib/Overlay.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/assets/penguins.png` & `holoviews-1.9.5/holoviews/examples/reference/elements/assets/penguins.png`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Area.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Area.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Arrow.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Arrow.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Bars.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Bars.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Bivariate.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Bivariate.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Bounds.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Bounds.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Box.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Box.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/BoxWhisker.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/BoxWhisker.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Contours.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Contours.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Curve.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Curve.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Distribution.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Distribution.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Ellipse.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Ellipse.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/ErrorBars.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/ErrorBars.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Graph.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Graph.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/HeatMap.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/HeatMap.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Histogram.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Histogram.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/HLine.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/HLine.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/HSV.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/HSV.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Image.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Image.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/ItemTable.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/ItemTable.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Path.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Path.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Points.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Points.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Polygons.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Polygons.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/QuadMesh.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/QuadMesh.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Raster.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Raster.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/RGB.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/RGB.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Scatter.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Scatter.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Spikes.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Spikes.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Spline.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Spline.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Spread.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Spread.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Table.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Table.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/Text.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/Text.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/VectorField.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/VectorField.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/bokeh/VLine.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/bokeh/VLine.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Area.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Area.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Arrow.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Arrow.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Bars.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Bars.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Bivariate.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Bivariate.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Bounds.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Bounds.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Box.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Box.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/BoxWhisker.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/BoxWhisker.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Contours.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Contours.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Curve.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Curve.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Distribution.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Distribution.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Ellipse.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Ellipse.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/ErrorBars.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/ErrorBars.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Graph.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Graph.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/HeatMap.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/HeatMap.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Histogram.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Histogram.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/HLine.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/HLine.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/HSV.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/HSV.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Image.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Image.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/ItemTable.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/ItemTable.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Path.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Path.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Points.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Points.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Polygons.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Polygons.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/QuadMesh.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/QuadMesh.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Raster.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Raster.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/RGB.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/RGB.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Scatter.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Scatter.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Scatter3D.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Scatter3D.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Spikes.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Spikes.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Spline.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Spline.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Spread.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Spread.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Surface.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Surface.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Table.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Table.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/Text.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/Text.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/TriSurface.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/TriSurface.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/VectorField.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/VectorField.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/matplotlib/VLine.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/matplotlib/VLine.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/plotly/BoxWhiskers.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/plotly/BoxWhiskers.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/plotly/Curve.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/plotly/Curve.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/plotly/Distribution.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/plotly/Distribution.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/plotly/ErrorBars.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/plotly/ErrorBars.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/plotly/HeatMap.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/plotly/HeatMap.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/plotly/Image.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/plotly/Image.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/plotly/ItemTable.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/plotly/ItemTable.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/plotly/Points.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/plotly/Points.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/plotly/Raster.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/plotly/Raster.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/plotly/Scatter.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/plotly/Scatter.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/plotly/Scatter3D.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/plotly/Scatter3D.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/plotly/Surface.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/plotly/Surface.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/plotly/Table.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/plotly/Table.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/elements/plotly/TriSurface.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/elements/plotly/TriSurface.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/features/bokeh/table_hooks_example.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/features/bokeh/table_hooks_example.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/streams/bokeh/Bounds.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/streams/bokeh/Bounds.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/streams/bokeh/BoundsX.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/streams/bokeh/BoundsX.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/streams/bokeh/BoundsY.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/streams/bokeh/BoundsY.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/streams/bokeh/PointerX.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/streams/bokeh/PointerX.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/streams/bokeh/PointerXY.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/streams/bokeh/PointerXY.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/streams/bokeh/RangeXY.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/streams/bokeh/RangeXY.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/streams/bokeh/Selection1D.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/streams/bokeh/Selection1D.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/streams/bokeh/Selection1D_paired.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/streams/bokeh/Selection1D_paired.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/streams/bokeh/Selection1D_points.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/streams/bokeh/Selection1D_points.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/streams/bokeh/Selection1D_tap.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/streams/bokeh/Selection1D_tap.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/reference/streams/bokeh/Tap.ipynb` & `holoviews-1.9.5/holoviews/examples/reference/streams/bokeh/Tap.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/topics/geometry/lsystems.ipynb` & `holoviews-1.9.5/holoviews/examples/topics/geometry/lsystems.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/topics/geometry/square_limit.ipynb` & `holoviews-1.9.5/holoviews/examples/topics/geometry/square_limit.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/topics/simulation/boids.ipynb` & `holoviews-1.9.5/holoviews/examples/topics/simulation/boids.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/topics/simulation/hipster_dynamics.ipynb` & `holoviews-1.9.5/holoviews/examples/topics/simulation/hipster_dynamics.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/topics/simulation/sri_model.ipynb` & `holoviews-1.9.5/holoviews/examples/topics/simulation/sri_model.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/user_guide/01-Annotating_Data.ipynb` & `holoviews-1.9.5/holoviews/examples/user_guide/01-Annotating_Data.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/user_guide/02-Composing_Elements.ipynb` & `holoviews-1.9.5/holoviews/examples/user_guide/02-Composing_Elements.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/user_guide/03-Customizing_Plots.ipynb` & `holoviews-1.9.5/holoviews/examples/user_guide/03-Customizing_Plots.ipynb`

 * *Files 2% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9848118279569893%*

 * *Differences: {"'cells'": "{13: {'source': ['Although it is as simple as possible, this format is tedious and "*

 * *            'verbose to use: HoloViews allows you to specify *all* your options separate from your '*

 * *            'elements in one specifiation which means there is a minimum possible complexity. For '*

 * *            'this reason, the most commonly used format is the succinct string format describe '*

 * *            "below, which is parsed into the dictionary format behind the scenes.']}, 14: "*

 * *            "{'source':  […]*

```diff
@@ -177,53 +177,93 @@
                 "layout"
             ]
         },
         {
             "cell_type": "markdown",
             "metadata": {},
             "source": [
-                "The straight line has no ``group`` and ``label`` so it gets 'blue' from the ``Curve`` level of specificity. The two sine curves are red as they both have the ``group`` specification of 'Sinusoid'. Lastly we has a sine squared curve with the same ``group`` label of 'Sinusoid' but it also has the ``label`` 'Squared' which is why it is green."
+                "The straight line has no ``group`` and ``label`` so it gets 'blue' from the ``Curve`` level of specificity. The two sine curves are red as they both have the ``group`` specification of 'Sinusoid'. Lastly we has a sine squared curve with the same ``group`` label of 'Sinusoid' but it also has the ``label`` 'Squared' which is why it is green.\n",
+                "\n",
+                "#### Dictionary format\n",
+                "\n",
+                "HoloViews avoids string parsing and special syntax (other than the basic operators described in [Composing Elements](./02-Composing_Elements.ipynb)) where possible. For this reason, all options are fundamentally reduced to a simple dictionary format. For example, here is the pure Python equivalent of the options shown above, using the ``opts`` method that will be described shortly:"
+            ]
+        },
+        {
+            "cell_type": "code",
+            "execution_count": null,
+            "metadata": {},
+            "outputs": [],
+            "source": [
+                "dict_spec = {'Curve': {'style':dict(color='blue')}, \n",
+                "             'Curve.Sinusoid': {'style':dict(color='red')}, \n",
+                "             'Curve.Sinusoid.Squared ': {'style':dict(color='green'),\n",
+                "                                         'plot':dict(interpolation='steps-mid')}}\n",
+                "\n",
+                "dcurve = hv.Curve((xs, xs/3))\n",
+                "dgroup_curve1 = hv.Curve((xs, np.sin(xs)), group='Sinusoid')\n",
+                "dgroup_curve2 = hv.Curve((xs, np.sin(xs+np.pi/4)), group='Sinusoid')\n",
+                "dlabel_curve = hv.Curve((xs, np.sin(xs)**2), group='Sinusoid', label='Squared')\n",
+                "dlayout = dcurve * dgroup_curve1 * dgroup_curve2 * dlabel_curve\n",
+                "dlayout.opts(dict_spec)"
             ]
         },
         {
             "cell_type": "markdown",
             "metadata": {},
             "source": [
-                "#### Dictionary format"
+                "Although it is as simple as possible, this format is tedious and verbose to use: HoloViews allows you to specify *all* your options separate from your elements in one specifiation which means there is a minimum possible complexity. For this reason, the most commonly used format is the succinct string format describe below, which is parsed into the dictionary format behind the scenes."
             ]
         },
         {
             "cell_type": "markdown",
             "metadata": {},
             "source": [
-                "HoloViews avoids string parsing and special syntax (other than the basic operators described in [Composing Elements](./02-Composing_Elements.ipynb)) where possible. For this reason, all options are fundamentally reduced to a simple dictionary format. For example, here is the pure Python equivalent of the options shown above, using the ``opts`` method that will be described shortly:"
+                "#### Simplified format"
+            ]
+        },
+        {
+            "cell_type": "markdown",
+            "metadata": {},
+            "source": [
+                "The dictionary format above can be quite cumbersome to work with, therefore HoloViews provides a simpler ``.options`` method, which automatically distinguishes between ``plot``, ``style`` and ``norm`` options. We can take advantage of this to easily apply a mixture of options:"
             ]
         },
         {
             "cell_type": "code",
             "execution_count": null,
             "metadata": {},
             "outputs": [],
             "source": [
-                "dict_spec = {'Curve':{'style':dict(color='blue')}, \n",
-                "             'Curve.Sinusoid':{'style':dict(color='red')}, \n",
-                "             'Curve.Sinusoid.Squared ': {'style':dict(color='green'), 'plot':dict(interpolation='steps-mid')}}\n",
-                "dcurve = hv.Curve((xs, xs/3))\n",
-                "dgroup_curve1 = hv.Curve((xs, np.sin(xs)), group='Sinusoid')\n",
-                "dgroup_curve2 = hv.Curve((xs, np.sin(xs+np.pi/4)), group='Sinusoid')\n",
-                "dlabel_curve = hv.Curve((xs, np.sin(xs)**2), group='Sinusoid', label='Squared')\n",
-                "dlayout = dcurve * dgroup_curve1 * dgroup_curve2 * dlabel_curve\n",
-                "dlayout.opts(dict_spec)"
+                "hv.Curve((xs, np.sin(xs))).options(width=500, color='red')"
             ]
         },
         {
             "cell_type": "markdown",
             "metadata": {},
             "source": [
-                "Although it is as simple as possible, this format is tedious and verbose to use: HoloViews allows you to specify *all* your options separate from your elements in one specifiation which means there is a minimum possible complexity. For this reason, the most commonly used format is the succinct string format describe below, which is parsed into the dictionary format behind the scenes."
+                "In a simple case like above where we are setting options that apply to the ``Curve`` element directly on a ``Curve`` we do not need to qualify further. However, when we are a composite object like an ``Overlay`` or ``Layout``, we have to be explicit about the object we are customizing, again using the ``type[[.group].label]`` specification."
+            ]
+        },
+        {
+            "cell_type": "code",
+            "execution_count": null,
+            "metadata": {},
+            "outputs": [],
+            "source": [
+                "curve = hv.Curve((xs, np.sin(xs+np.pi/4)))\n",
+                "stepped_curve = hv.Curve((xs, np.sin(xs)**2), group='Stepped')\n",
+                "area = hv.Area((xs, np.sin(xs)**2))\n",
+                "negative_area = hv.Area((xs, -(np.sin(xs)**2)), group='Negative')\n",
+                "\n",
+                "options = {'Curve': dict(width=500, color='red'),\n",
+                "           'Curve.Stepped': dict(color='green', interpolation='steps-mid'),\n",
+                "           'Area.Negative': dict(color='red')}\n",
+                "\n",
+                "(curve * stepped_curve + area * negative_area).options(options)"
             ]
         },
         {
             "cell_type": "markdown",
             "metadata": {},
             "source": [
                 "#### Yaml equivalent\n",
```

### Comparing `holoviews-1.9.4/holoviews/examples/user_guide/04-Dimensioned_Containers.ipynb` & `holoviews-1.9.5/holoviews/examples/user_guide/04-Dimensioned_Containers.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/user_guide/05-Building_Composite_Objects.ipynb` & `holoviews-1.9.5/holoviews/examples/user_guide/05-Building_Composite_Objects.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/user_guide/06-Live_Data.ipynb` & `holoviews-1.9.5/holoviews/examples/user_guide/06-Live_Data.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/user_guide/07-Tabular_Datasets.ipynb` & `holoviews-1.9.5/holoviews/examples/user_guide/07-Tabular_Datasets.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/user_guide/08-Gridded_Datasets.ipynb` & `holoviews-1.9.5/holoviews/examples/user_guide/08-Gridded_Datasets.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/user_guide/09-Indexing_and_Selecting_Data.ipynb` & `holoviews-1.9.5/holoviews/examples/user_guide/09-Indexing_and_Selecting_Data.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/user_guide/10-Transforming_Elements.ipynb` & `holoviews-1.9.5/holoviews/examples/user_guide/10-Transforming_Elements.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/user_guide/11-Responding_to_Events.ipynb` & `holoviews-1.9.5/holoviews/examples/user_guide/11-Responding_to_Events.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/user_guide/12-Custom_Interactivity.ipynb` & `holoviews-1.9.5/holoviews/examples/user_guide/12-Custom_Interactivity.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/user_guide/13-Data_Pipelines.ipynb` & `holoviews-1.9.5/holoviews/examples/user_guide/13-Data_Pipelines.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/user_guide/14-Large_Data.ipynb` & `holoviews-1.9.5/holoviews/examples/user_guide/14-Large_Data.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/user_guide/15-Streaming_Data.ipynb` & `holoviews-1.9.5/holoviews/examples/user_guide/15-Streaming_Data.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/user_guide/16-Dashboards.ipynb` & `holoviews-1.9.5/holoviews/examples/user_guide/16-Dashboards.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/user_guide/Continuous_Coordinates.ipynb` & `holoviews-1.9.5/holoviews/examples/user_guide/Continuous_Coordinates.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/user_guide/Deploying_Bokeh_Apps.ipynb` & `holoviews-1.9.5/holoviews/examples/user_guide/Deploying_Bokeh_Apps.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/user_guide/Exporting_and_Archiving.ipynb` & `holoviews-1.9.5/holoviews/examples/user_guide/Exporting_and_Archiving.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/user_guide/Installing_and_Configuring.ipynb` & `holoviews-1.9.5/holoviews/examples/user_guide/Installing_and_Configuring.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/user_guide/Network_Graphs.ipynb` & `holoviews-1.9.5/holoviews/examples/user_guide/Network_Graphs.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/user_guide/Plots_and_Renderers.ipynb` & `holoviews-1.9.5/holoviews/examples/user_guide/Plots_and_Renderers.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/user_guide/Plotting_with_Bokeh.ipynb` & `holoviews-1.9.5/holoviews/examples/user_guide/Plotting_with_Bokeh.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/user_guide/Plotting_with_Matplotlib.ipynb` & `holoviews-1.9.5/holoviews/examples/user_guide/Plotting_with_Matplotlib.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/examples/user_guide/Tips_and_Tricks.ipynb` & `holoviews-1.9.5/holoviews/examples/user_guide/Tips_and_Tricks.ipynb`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/ipython/__init__.py` & `holoviews-1.9.5/holoviews/ipython/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -92,15 +92,15 @@
         format will be displayed).
 
         Although the 'html' format is supported across backends, other
         formats supported by the current backend (e.g 'png' and 'svg'
         using the matplotlib backend) may be used. This may be useful to
         export figures to other formats such as PDF with nbconvert. """)
 
-    case_sensitive_completion = param.Boolean(default=False, doc="""
+    case_sensitive_completion = param.Boolean(default=True, doc="""
        Whether to monkey patch IPython to use the correct tab-completion
        behavior. """)
 
     _loaded = False
 
     def __call__(self, *args, **params):
         super(notebook_extension, self).__call__(*args, **params)
```

### Comparing `holoviews-1.9.4/holoviews/ipython/archive.py` & `holoviews-1.9.5/holoviews/ipython/archive.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/ipython/display_hooks.py` & `holoviews-1.9.5/holoviews/ipython/display_hooks.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/ipython/load_notebook.html` & `holoviews-1.9.5/holoviews/ipython/load_notebook.html`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/ipython/magics.py` & `holoviews-1.9.5/holoviews/ipython/magics.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/ipython/preprocessors.py` & `holoviews-1.9.5/holoviews/ipython/preprocessors.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/ipython/widgets.py` & `holoviews-1.9.5/holoviews/ipython/widgets.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/operation/__init__.py` & `holoviews-1.9.5/holoviews/operation/__init__.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/operation/datashader.py` & `holoviews-1.9.5/holoviews/operation/datashader.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/operation/element.py` & `holoviews-1.9.5/holoviews/operation/element.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/operation/normalization.py` & `holoviews-1.9.5/holoviews/operation/normalization.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/operation/stats.py` & `holoviews-1.9.5/holoviews/operation/stats.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/operation/timeseries.py` & `holoviews-1.9.5/holoviews/operation/timeseries.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/__init__.py` & `holoviews-1.9.5/holoviews/plotting/__init__.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/bokeh/__init__.py` & `holoviews-1.9.5/holoviews/plotting/bokeh/__init__.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/bokeh/annotation.py` & `holoviews-1.9.5/holoviews/plotting/bokeh/annotation.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/bokeh/bokehwidgets.js` & `holoviews-1.9.5/holoviews/plotting/bokeh/bokehwidgets.js`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/bokeh/callbacks.py` & `holoviews-1.9.5/holoviews/plotting/bokeh/callbacks.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/bokeh/chart.py` & `holoviews-1.9.5/holoviews/plotting/bokeh/chart.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/bokeh/element.py` & `holoviews-1.9.5/holoviews/plotting/bokeh/element.py`

 * *Files 0% similar despite different names*

```diff
@@ -21,15 +21,16 @@
 from ...core.options import abbreviated_exception, SkipRendering
 from ...core import util
 from ...streams import Buffer
 from ..plot import GenericElementPlot, GenericOverlayPlot
 from ..util import dynamic_update, process_cmap
 from .plot import BokehPlot, TOOLS
 from .util import (mpl_to_bokeh, get_tab_title,  py2js_tickformatter,
-                   rgba_tuple, recursive_model_update, glyph_order)
+                   rgba_tuple, recursive_model_update, glyph_order,
+                   decode_bytes)
 
 property_prefixes = ['selection', 'nonselection', 'muted', 'hover']
 
 # Define shared style properties for bokeh plots
 line_properties = ['line_color', 'line_alpha', 'color', 'alpha', 'line_width',
                    'line_join', 'line_cap', 'line_dash']
 line_properties += ['_'.join([prefix, prop]) for prop in line_properties[:4]
@@ -567,15 +568,15 @@
                                      or np.isfinite(high)):
                 updates['end'] = (axis_range.end, high)
             for k, (old, new) in updates.items():
                 axis_range.update(**{k:new})
                 if streaming:
                     axis_range.trigger(k, old, new)
         elif isinstance(axis_range, FactorRange):
-            factors = list(factors)
+            factors = list(decode_bytes(factors))
             if invert: factors = factors[::-1]
             axis_range.factors = factors
 
 
     def _categorize_data(self, data, cols, dims):
         """
         Transforms non-string or integer types in datasource if the
@@ -1152,14 +1153,15 @@
                 opts['low'] = low
             if np.isfinite(high):
                 opts['high'] = high
             color_opts = [('NaN', 'nan_color'), ('max', 'high_color'), ('min', 'low_color')]
             opts.update({opt: colors[name] for name, opt in color_opts if name in colors})
         else:
             colormapper = CategoricalColorMapper
+            factors = decode_bytes(factors)
             opts = dict(factors=factors)
             if 'NaN' in colors:
                 opts['nan_color'] = colors['NaN']
         return colormapper, opts
 
 
     def _init_glyph(self, plot, mapping, properties):
```

### Comparing `holoviews-1.9.4/holoviews/plotting/bokeh/graphs.py` & `holoviews-1.9.5/holoviews/plotting/bokeh/graphs.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/bokeh/path.py` & `holoviews-1.9.5/holoviews/plotting/bokeh/path.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/bokeh/plot.py` & `holoviews-1.9.5/holoviews/plotting/bokeh/plot.py`

 * *Files 3% similar despite different names*

```diff
@@ -11,18 +11,20 @@
                      Empty, GridSpace, HoloMap, Element, DynamicMap)
 from ...core.util import basestring, wrap_tuple, unique_iterator
 from ...streams import Stream
 from ..plot import (DimensionedPlot, GenericCompositePlot, GenericLayoutPlot,
                     GenericElementPlot, GenericOverlayPlot)
 from ..util import attach_streams
 from .util import (layout_padding, pad_plots, filter_toolboxes, make_axis,
-                   update_shared_sources, empty_plot)
+                   update_shared_sources, empty_plot, decode_bytes,
+                   bokeh_version)
 
 from bokeh.layouts import gridplot
 from bokeh.plotting.helpers import _known_tools as known_tools
+from bokeh.util.serialization import convert_datetime_array
 
 TOOLS = {name: tool if isinstance(tool, basestring) else type(tool())
          for name, tool in known_tools.items()}
 
 
 class BokehPlot(DimensionedPlot):
     """
@@ -161,27 +163,54 @@
             plot.root = root
 
 
     def _init_datasource(self, data):
         """
         Initializes a data source to be passed into the bokeh glyph.
         """
+        data = {k: decode_bytes(vs) for k, vs in data.items()}
         return ColumnDataSource(data=data)
 
 
     def _update_datasource(self, source, data):
         """
         Update datasource with data for a new frame.
         """
+        data = {k: decode_bytes(vs) for k, vs in data.items()}
         if (self.streaming and self.streaming[0].data is self.current_frame.data
             and self._stream_data):
             stream = self.streaming[0]
             if stream._triggering:
                 data = {k: v[-stream._chunk_length:] for k, v in data.items()}
-                source.stream(data, stream.length)
+
+                # NOTE: Workaround for bug in bokeh 0.12.14, data conversion
+                # should be removed once fixed in bokeh (https://github.com/bokeh/bokeh/issues/7587)
+                converted_data = {}
+                for k, vals in data.items():
+                    cdata = source.data[k]
+                    odata = data[k]
+                    if (bokeh_version in ['0.12.14', '0.12.15dev1'] and
+                        isinstance(cdata, np.ndarray) and cdata.dtype.kind == 'M'
+                        and isinstance(vals, np.ndarray) and vals.dtype.kind == 'M'):
+                        cdata = convert_datetime_array(cdata)
+                        odata = convert_datetime_array(odata)
+                        if len(odata):
+                            cdata = np.concatenate([odata, cdata])
+                        converted_data[k] = cdata
+                if converted_data:
+                    for k, vals in data.items():
+                        cdata = source.data[k]
+                        odata = data[k]
+                        if k not in converted_data:
+                            if len(odata):
+                                cdata = np.concatenate([odata, cdata])
+                            converted_data[k] = cdata
+                    source.data.update(converted_data)
+                else:
+                    source.stream(data, stream.length)
         else:
             source.data.update(data)
 
     @property
     def state(self):
         """
         The plotting state that gets updated via the update method and
```

### Comparing `holoviews-1.9.4/holoviews/plotting/bokeh/raster.py` & `holoviews-1.9.5/holoviews/plotting/bokeh/raster.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/bokeh/renderer.py` & `holoviews-1.9.5/holoviews/plotting/bokeh/renderer.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/bokeh/stats.py` & `holoviews-1.9.5/holoviews/plotting/bokeh/stats.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/bokeh/tabular.py` & `holoviews-1.9.5/holoviews/plotting/bokeh/tabular.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/bokeh/util.py` & `holoviews-1.9.5/holoviews/plotting/bokeh/util.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-import inspect, re, time
+import inspect, re, time, sys
 from distutils.version import LooseVersion
 from collections import defaultdict
 import datetime as dt
 
 import numpy as np
 
 try:
@@ -62,14 +62,30 @@
     """
     if isinstance(rgba, tuple):
         return tuple(int(c*255) if i<3 else c for i, c in enumerate(rgba))
     else:
         return rgba
 
 
+def decode_bytes(array):
+    """
+    Decodes an array, list or tuple of bytestrings to avoid python 3
+    bokeh serialization errors
+    """
+    if (sys.version_info.major == 2 or not len(array) or
+        (isinstance(array, np.ndarray) and array.dtype.kind != 'O')):
+        return array
+    decoded = [v.decode('utf-8') if isinstance(v, bytes) else v for v in array]
+    if isinstance(array, np.ndarray):
+        return np.asarray(decoded)
+    elif isinstance(array, tuple):
+        return tuple(decoded)
+    return decoded
+
+
 def get_cmap(cmap):
     """
     Returns matplotlib cmap generated from bokeh palette or
     directly accessed from matplotlib.
     """
     with abbreviated_exception():
         rgb_vals = getattr(Palette, cmap, None)
```

### Comparing `holoviews-1.9.4/holoviews/plotting/bokeh/widgets.py` & `holoviews-1.9.5/holoviews/plotting/bokeh/widgets.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/comms.py` & `holoviews-1.9.5/holoviews/plotting/comms.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/mpl/__init__.py` & `holoviews-1.9.5/holoviews/plotting/mpl/__init__.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/mpl/annotation.py` & `holoviews-1.9.5/holoviews/plotting/mpl/annotation.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/mpl/chart.py` & `holoviews-1.9.5/holoviews/plotting/mpl/chart.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/mpl/chart3d.py` & `holoviews-1.9.5/holoviews/plotting/mpl/chart3d.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/mpl/comms.py` & `holoviews-1.9.5/holoviews/plotting/mpl/comms.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/mpl/default.mplstyle` & `holoviews-1.9.5/holoviews/plotting/mpl/default.mplstyle`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/mpl/default1.5.mplstyle` & `holoviews-1.9.5/holoviews/plotting/mpl/default1.5.mplstyle`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/mpl/element.py` & `holoviews-1.9.5/holoviews/plotting/mpl/element.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/mpl/graphs.py` & `holoviews-1.9.5/holoviews/plotting/mpl/graphs.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/mpl/mplwidgets.js` & `holoviews-1.9.5/holoviews/plotting/mpl/mplwidgets.js`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/mpl/path.py` & `holoviews-1.9.5/holoviews/plotting/mpl/path.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/mpl/plot.py` & `holoviews-1.9.5/holoviews/plotting/mpl/plot.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/mpl/raster.py` & `holoviews-1.9.5/holoviews/plotting/mpl/raster.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/mpl/renderer.py` & `holoviews-1.9.5/holoviews/plotting/mpl/renderer.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/mpl/stats.py` & `holoviews-1.9.5/holoviews/plotting/mpl/stats.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/mpl/tabular.py` & `holoviews-1.9.5/holoviews/plotting/mpl/tabular.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/mpl/util.py` & `holoviews-1.9.5/holoviews/plotting/mpl/util.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/mpl/widgets.py` & `holoviews-1.9.5/holoviews/plotting/mpl/widgets.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/plot.py` & `holoviews-1.9.5/holoviews/plotting/plot.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/plotly/__init__.py` & `holoviews-1.9.5/holoviews/plotting/plotly/__init__.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/plotly/chart.py` & `holoviews-1.9.5/holoviews/plotting/plotly/chart.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/plotly/chart3d.py` & `holoviews-1.9.5/holoviews/plotting/plotly/chart3d.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/plotly/element.py` & `holoviews-1.9.5/holoviews/plotting/plotly/element.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/plotly/plot.py` & `holoviews-1.9.5/holoviews/plotting/plotly/plot.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/plotly/plotlywidgets.js` & `holoviews-1.9.5/holoviews/plotting/plotly/plotlywidgets.js`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/plotly/raster.py` & `holoviews-1.9.5/holoviews/plotting/plotly/raster.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/plotly/renderer.py` & `holoviews-1.9.5/holoviews/plotting/plotly/renderer.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/plotly/tabular.py` & `holoviews-1.9.5/holoviews/plotting/plotly/tabular.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/plotly/util.py` & `holoviews-1.9.5/holoviews/plotting/plotly/util.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/plotly/widgets.py` & `holoviews-1.9.5/holoviews/plotting/plotly/widgets.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/renderer.py` & `holoviews-1.9.5/holoviews/plotting/renderer.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/util.py` & `holoviews-1.9.5/holoviews/plotting/util.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/widgets/__init__.py` & `holoviews-1.9.5/holoviews/plotting/widgets/__init__.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/widgets/jsscrubber.jinja` & `holoviews-1.9.5/holoviews/plotting/widgets/jsscrubber.jinja`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/widgets/jsslider.css` & `holoviews-1.9.5/holoviews/plotting/widgets/jsslider.css`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/widgets/jsslider.jinja` & `holoviews-1.9.5/holoviews/plotting/widgets/jsslider.jinja`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/plotting/widgets/widgets.js` & `holoviews-1.9.5/holoviews/plotting/widgets/widgets.js`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/streams.py` & `holoviews-1.9.5/holoviews/streams.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/util/__init__.py` & `holoviews-1.9.5/holoviews/util/__init__.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 import os, sys, inspect, shutil
 
 import param
 
 from ..core import DynamicMap, HoloMap, Dimensioned, ViewableElement, StoreOptions, Store
-from ..core.options import options_policy
+from ..core.options import options_policy, Keywords
 from ..core.operation import Operation
 from ..core.util import Aliases, basestring  # noqa (API import)
 from ..core.operation import OperationCallable
 from ..core.spaces import Callable
 from ..core import util
 from ..streams import Stream
 from .settings import OutputSettings, list_formats, list_backends
@@ -101,14 +101,100 @@
                 StoreOptions.apply_customizations(options, Store.options())
         elif not isinstance(obj, Dimensioned):
             return obj
         else:
             return StoreOptions.set_options(obj, options)
 
 
+    @classmethod
+    def expand_options(cls, options, backend=None):
+        """
+        Validates and expands a dictionaries of options indexed by
+        type[.group][.label] keys into separate style, plot and norm
+        options.
+
+            opts.expand_options({'Image': dict(cmap='viridis', show_title=False)})
+
+        returns
+
+            {'Image': {'plot': dict(show_title=False), 'style': dict(cmap='viridis')}}
+        """
+        current_backend = Store.current_backend
+        backend_options = Store.options(backend=backend or current_backend)
+        expanded = {}
+        for objspec, options in options.items():
+            objtype = objspec.split('.')[0]
+            if objtype not in backend_options:
+                raise ValueError('%s type not found, could not apply options.'
+                                 % objtype)
+            obj_options = backend_options[objtype]
+            expanded[objspec] = {g: {} for g in obj_options.groups}
+            for opt, value in options.items():
+                found = False
+                valid_options = []
+                for g, group_opts in obj_options.groups.items():
+                    if opt in group_opts.allowed_keywords:
+                        expanded[objspec][g][opt] = value
+                        found = True
+                        break
+                    valid_options += group_opts.allowed_keywords
+                if found: continue
+                cls._options_error(opt, objtype, backend, valid_options)
+        return expanded
+
+
+    @classmethod
+    def _options_error(cls, opt, objtype, backend, valid_options):
+        """
+        Generates an error message for an invalid option suggesting
+        similar options through fuzzy matching.
+        """
+        current_backend = Store.current_backend
+        loaded_backends = Store.loaded_backends()
+        kws = Keywords(values=valid_options)
+        matches = sorted(kws.fuzzy_match(opt))
+        if backend is not None:
+            if matches:
+                raise ValueError('Unexpected option %r for %s types '
+                                 'when using the %r extension. Similar '
+                                 'options are: %s.' %
+                                 (opt, objtype, backend, matches))
+            else:
+                raise ValueError('Unexpected option %r for %s types '
+                                 'when using the %r extension. No '
+                                 'similar options founds.' %
+                                 (opt, objtype, backend))
+
+        # Check option is invalid for all backends
+        found = []
+        for lb in [b for b in loaded_backends if b != backend]:
+            lb_options = Store.options(backend=lb).get(objtype)
+            if lb_options is None:
+                continue
+            for g, group_opts in lb_options.groups.items():
+                if opt in group_opts.allowed_keywords:
+                    found.append(lb)
+        if found:
+            param.main.warning('Option %r for %s type not valid '
+                               'for selected backend (%r). Option '
+                               'only applies to following backends: %r' %
+                               (opt, objtype, current_backend, found))
+            return
+
+        if matches:
+            raise ValueError('Unexpected option %r for %s types '
+                             'across all extensions. Similar options '
+                             'for current extension (%r) are: %s.' %
+                             (opt, objtype, current_backend, matches))
+        else:
+            raise ValueError('Unexpected option %r for %s types '
+                             'across all extensions. No similar options '
+                             'found.' % (opt, objtype))
+
+
 class output(param.ParameterizedFunction):
     """
     Utility function to set output either at the global level or on a
     specific object.
 
     To set output globally use:
```

### Comparing `holoviews-1.9.4/holoviews/util/command.py` & `holoviews-1.9.5/holoviews/util/command.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/util/parser.py` & `holoviews-1.9.5/holoviews/util/parser.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews/util/settings.py` & `holoviews-1.9.5/holoviews/util/settings.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/holoviews.egg-info/PKG-INFO` & `holoviews-1.9.5/holoviews.egg-info/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,15 +1,16 @@
 Metadata-Version: 1.1
 Name: holoviews
-Version: 1.9.4
+Version: 1.9.5
 Summary: Stop plotting your data - annotate your data and let it visualize itself.
 Home-page: http://www.holoviews.org
 Author: IOAM
 Author-email: holoviews@gmail.com
 License: BSD
+Description-Content-Type: UNKNOWN
 Description: 
         HoloViews is designed to make data analysis and visualization seamless and simple. With HoloViews, you can usually express what you want to do in very few lines of code, letting you focus on what you are trying to explore and convey, not on the process of plotting.
         
         Check out the `HoloViews web site <http://holoviews.org>`_ for extensive examples and documentation.
         
 Platform: Windows
 Platform: Mac OS X
```

### Comparing `holoviews-1.9.4/holoviews.egg-info/requires.txt` & `holoviews-1.9.5/holoviews.egg-info/requires.txt`

 * *Files 6% similar despite different names*

```diff
@@ -1,37 +1,37 @@
-param>=1.5.1,<2.0
+param<2.0,>=1.5.1
 numpy>=1.0
 
 [all]
 ipython
 pyzmq
 jinja2
 tornado
 jsonschema
 notebook
 pygments
 matplotlib
 pandas
 seaborn
-bokeh>=0.12.10, <0.12.12
+bokeh<0.12.12,>=0.12.10
 ipython
 pyzmq
 jinja2
 tornado
 jsonschema
 notebook
 pygments
 matplotlib
 cyordereddict
 nose
 
 [extras]
 pandas
 seaborn
-bokeh>=0.12.10, <0.12.12
+bokeh<0.12.12,>=0.12.10
 ipython
 pyzmq
 jinja2
 tornado
 jsonschema
 notebook
 pygments
```

### Comparing `holoviews-1.9.4/holoviews.egg-info/SOURCES.txt` & `holoviews-1.9.5/holoviews.egg-info/SOURCES.txt`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,11 @@
 CHANGELOG.md
 LICENSE.txt
 MANIFEST.in
+README.md
 setup.py
 doc/FAQ.rst
 doc/Homepage.ipynb
 doc/Makefile
 doc/about.rst
 doc/conf.py
 doc/features.rst
@@ -695,14 +696,16 @@
 tests/teststatselements.py
 tests/teststatsoperations.py
 tests/teststoreoptions.py
 tests/teststreams.py
 tests/testtimeseriesoperations.py
 tests/testtraversal.py
 tests/testutils.py
+tests/utils.py
+tests/core/testdimensioned.py
 tests/notebooks/test_opts_image_cell_magic.ipynb
 tests/notebooks/test_opts_image_cell_magic_offset.ipynb
 tests/notebooks/test_opts_image_line_magic.ipynb
 tests/notebooks/test_output_svg_line_magic.ipynb
 tests/operation/__init__.py
 tests/operation/testdatashader.py
 tests/plotting/__init__.py
```

### Comparing `holoviews-1.9.4/LICENSE.txt` & `holoviews-1.9.5/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/PKG-INFO` & `holoviews-1.9.5/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,15 +1,16 @@
 Metadata-Version: 1.1
 Name: holoviews
-Version: 1.9.4
+Version: 1.9.5
 Summary: Stop plotting your data - annotate your data and let it visualize itself.
 Home-page: http://www.holoviews.org
 Author: IOAM
 Author-email: holoviews@gmail.com
 License: BSD
+Description-Content-Type: UNKNOWN
 Description: 
         HoloViews is designed to make data analysis and visualization seamless and simple. With HoloViews, you can usually express what you want to do in very few lines of code, letting you focus on what you are trying to explore and convey, not on the process of plotting.
         
         Check out the `HoloViews web site <http://holoviews.org>`_ for extensive examples and documentation.
         
 Platform: Windows
 Platform: Mac OS X
```

### Comparing `holoviews-1.9.4/setup.py` & `holoviews-1.9.5/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -31,15 +31,15 @@
 HoloViews is designed to make data analysis and visualization seamless and simple. With HoloViews, you can usually express what you want to do in very few lines of code, letting you focus on what you are trying to explore and convey, not on the process of plotting.
 
 Check out the `HoloViews web site <http://holoviews.org>`_ for extensive examples and documentation.
 """
 
 setup_args.update(dict(
     name='holoviews',
-    version="1.9.4",
+    version="1.9.5",
     install_requires=install_requires,
     extras_require=extras_require,
     description='Stop plotting your data - annotate your data and let it visualize itself.',
     long_description=PYPI_BLURB,
     author="Jean-Luc Stevens and Philipp Rudiger",
     author_email="holoviews@gmail.com",
     maintainer="IOAM",
```

### Comparing `holoviews-1.9.4/tests/__init__.py` & `holoviews-1.9.5/tests/utils.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,20 +1,13 @@
 import os, sys
 import param
 import logging
 
 from holoviews.element.comparison import ComparisonTestCase
 
-try:
-    # Standardize backend due to random inconsistencies
-    from matplotlib import pyplot
-    pyplot.switch_backend('agg')
-except:
-    pass
-
 cwd = os.path.abspath(os.path.split(__file__)[0])
 sys.path.insert(0, os.path.join(cwd, '..'))
 
 
 class MockLoggingHandler(logging.Handler):
     """
     Mock logging handler to check for expected logs used by
```

### Comparing `holoviews-1.9.4/tests/operation/testdatashader.py` & `holoviews-1.9.5/tests/operation/testdatashader.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/plotting/bokeh/testserver.py` & `holoviews-1.9.5/tests/plotting/bokeh/testserver.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/plotting/bokeh/testtabular.py` & `holoviews-1.9.5/tests/plotting/bokeh/testtabular.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/plotting/testplotutils.py` & `holoviews-1.9.5/tests/plotting/testplotutils.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testaliases.py` & `holoviews-1.9.5/tests/testaliases.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testannotations.py` & `holoviews-1.9.5/tests/testannotations.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testapiconsistency.py` & `holoviews-1.9.5/tests/testapiconsistency.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testarchives.py` & `holoviews-1.9.5/tests/testarchives.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testbokehcallbacks.py` & `holoviews-1.9.5/tests/testbokehcallbacks.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testbokehgraphs.py` & `holoviews-1.9.5/tests/testbokehgraphs.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testbokehutils.py` & `holoviews-1.9.5/tests/testbokehutils.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testbokehwidgets.py` & `holoviews-1.9.5/tests/testbokehwidgets.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testboundingregion.py` & `holoviews-1.9.5/tests/testboundingregion.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testcallable.py` & `holoviews-1.9.5/tests/testcallable.py`

 * *Files 1% similar despite different names*

```diff
@@ -9,15 +9,15 @@
 from holoviews.element import Scatter
 from holoviews import streams
 from holoviews.core.spaces import Callable, Generator, DynamicMap
 from holoviews.core.operation import OperationCallable
 from holoviews.operation import contours
 from functools import partial
 
-from . import LoggingComparisonTestCase
+from ..utils import LoggingComparisonTestCase
 
 class CallableClass(object):
 
     @staticmethod
     def somestaticmethod(): pass
 
     @classmethod
```

### Comparing `holoviews-1.9.4/tests/testcollation.py` & `holoviews-1.9.5/tests/testcollation.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testcomms.py` & `holoviews-1.9.5/tests/testcomms.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testcomparisonchart.py` & `holoviews-1.9.5/tests/testcomparisonchart.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testcomparisoncomposite.py` & `holoviews-1.9.5/tests/testcomparisoncomposite.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testcomparisondimension.py` & `holoviews-1.9.5/tests/testcomparisondimension.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testcomparisonpath.py` & `holoviews-1.9.5/tests/testcomparisonpath.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testcomparisonraster.py` & `holoviews-1.9.5/tests/testcomparisonraster.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testcomparisonsimple.py` & `holoviews-1.9.5/tests/testcomparisonsimple.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testcomposites.py` & `holoviews-1.9.5/tests/testcomposites.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testcoreutils.py` & `holoviews-1.9.5/tests/testcoreutils.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testdataset.py` & `holoviews-1.9.5/tests/testdataset.py`

 * *Files 0% similar despite different names*

```diff
@@ -469,14 +469,18 @@
         test_df = pd.DataFrame({'x': range(10), 'y': range(0,20,2)})
         dataset = Dataset(test_df, kdims=[('x', 'X-label')], vdims=['y'])
         redim_df = pd.DataFrame({'X': range(10), 'y': range(0,20,2)})
         dataset_redim = Dataset(redim_df, kdims=['X'], vdims=['y'])
         self.assertEqual(dataset.redim(**{'X-label':'X'}), dataset_redim)
         self.assertEqual(dataset.redim(**{'x':'X'}), dataset_redim)
 
+    def test_dataset_mixed_type_range(self):
+        ds = Dataset((['A', 'B', 'C', None],), 'A')
+        self.assertEqual(ds.range(0), ('A', 'C'))
+
     def test_dataset_sort_vdim_ht(self):
         dataset = Dataset({'x':self.xs, 'y':-self.ys},
                           kdims=['x'], vdims=['y'])
         dataset_sorted = Dataset({'x': self.xs[::-1], 'y':-self.ys[::-1]},
                                  kdims=['x'], vdims=['y'])
         self.assertEqual(dataset.sort('y'), dataset_sorted)
```

### Comparing `holoviews-1.9.4/tests/testdimensions.py` & `holoviews-1.9.5/tests/testdimensions.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 """
 Test cases for Dimension and Dimensioned object behaviour.
 """
 from unittest import SkipTest
 from holoviews.core import Dimensioned, Dimension
 from holoviews.element.comparison import ComparisonTestCase
-from . import LoggingComparisonTestCase
+from .utils import LoggingComparisonTestCase
 
 import numpy as np
 try:
     import pandas as pd
 except:
     pd = None
```

### Comparing `holoviews-1.9.4/tests/testdimselect.py` & `holoviews-1.9.5/tests/testdimselect.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testdynamic.py` & `holoviews-1.9.5/tests/testdynamic.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testelementconstructors.py` & `holoviews-1.9.5/tests/testelementconstructors.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testelementindexing.py` & `holoviews-1.9.5/tests/testelementindexing.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testelementranges.py` & `holoviews-1.9.5/tests/testelementranges.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testelementutils.py` & `holoviews-1.9.5/tests/testelementutils.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testellipsis.py` & `holoviews-1.9.5/tests/testellipsis.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testgraphelement.py` & `holoviews-1.9.5/tests/testgraphelement.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testimageinterfaces.py` & `holoviews-1.9.5/tests/testimageinterfaces.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testimportexport.py` & `holoviews-1.9.5/tests/testimportexport.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testirisinterface.py` & `holoviews-1.9.5/tests/testirisinterface.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testlayers.py` & `holoviews-1.9.5/tests/testlayers.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testlayouts.py` & `holoviews-1.9.5/tests/testlayouts.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testmagics.py` & `holoviews-1.9.5/tests/testmagics.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testmplgraphs.py` & `holoviews-1.9.5/tests/testmplgraphs.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testmultiinterface.py` & `holoviews-1.9.5/tests/testmultiinterface.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testndmapping.py` & `holoviews-1.9.5/tests/testndmapping.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testnotebooks.py` & `holoviews-1.9.5/tests/testnotebooks.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testoperation.py` & `holoviews-1.9.5/tests/testoperation.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testoptions.py` & `holoviews-1.9.5/tests/testoptions.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testoptscompleter.py` & `holoviews-1.9.5/tests/testoptscompleter.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testparsers.py` & `holoviews-1.9.5/tests/testparsers.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testpaths.py` & `holoviews-1.9.5/tests/testpaths.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testplotinstantiation.py` & `holoviews-1.9.5/tests/testplotinstantiation.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testprettyprint.py` & `holoviews-1.9.5/tests/testprettyprint.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testraster.py` & `holoviews-1.9.5/tests/testraster.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testrenderclass.py` & `holoviews-1.9.5/tests/testrenderclass.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/teststatselements.py` & `holoviews-1.9.5/tests/teststatselements.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/teststatsoperations.py` & `holoviews-1.9.5/tests/teststatsoperations.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/teststoreoptions.py` & `holoviews-1.9.5/tests/teststoreoptions.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/teststreams.py` & `holoviews-1.9.5/tests/teststreams.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testtimeseriesoperations.py` & `holoviews-1.9.5/tests/testtimeseriesoperations.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testtraversal.py` & `holoviews-1.9.5/tests/testtraversal.py`

 * *Files identical despite different names*

### Comparing `holoviews-1.9.4/tests/testutils.py` & `holoviews-1.9.5/tests/testutils.py`

 * *Files identical despite different names*

