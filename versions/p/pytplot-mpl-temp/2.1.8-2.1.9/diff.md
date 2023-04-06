# Comparing `tmp/pytplot-mpl-temp-2.1.8.tar.gz` & `tmp/pytplot-mpl-temp-2.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pytplot-mpl-temp-2.1.8.tar", last modified: Wed Nov  2 19:39:03 2022, max compression
+gzip compressed data, was "pytplot-mpl-temp-2.1.9.tar", last modified: Wed Dec  7 22:12:05 2022, max compression
```

## Comparing `pytplot-mpl-temp-2.1.8.tar` & `pytplot-mpl-temp-2.1.9.tar`

### file list

```diff
@@ -1,145 +1,134 @@
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-02 19:39:03.396355 pytplot-mpl-temp-2.1.8/
--rw-r--r--   0 eric       (501) staff       (20)     1065 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/LICENSE
--rw-r--r--   0 eric       (501) staff       (20)      363 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/MANIFEST.in
--rw-r--r--   0 eric       (501) staff       (20)     3177 2022-11-02 19:39:03.396459 pytplot-mpl-temp-2.1.8/PKG-INFO
--rw-r--r--   0 eric       (501) staff       (20)     2510 2022-11-02 18:48:51.000000 pytplot-mpl-temp-2.1.8/README.md
--rw-r--r--   0 eric       (501) staff       (20)     2889 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/README.rst
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-02 19:39:03.377474 pytplot-mpl-temp-2.1.8/docs/
--rw-r--r--   0 eric       (501) staff       (20)     8107 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/docs/pytplot_tutorial.html
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-02 19:39:03.380616 pytplot-mpl-temp-2.1.8/pytplot/
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-02 19:39:03.381058 pytplot-mpl-temp-2.1.8/pytplot/AncillaryPlots/
--rw-r--r--   0 eric       (501) staff       (20)        0 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/AncillaryPlots/__init__.py
--rw-r--r--   0 eric       (501) staff       (20)     5398 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/AncillaryPlots/position_mars_2d.py
--rw-r--r--   0 eric       (501) staff       (20)     5105 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/AncillaryPlots/position_mars_3d.py
--rw-r--r--   0 eric       (501) staff       (20)    11294 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/AncillaryPlots/spec_slicer.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-02 19:39:03.381761 pytplot-mpl-temp-2.1.8/pytplot/HTMLPlotter/
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-02 19:39:03.382073 pytplot-mpl-temp-2.1.8/pytplot/HTMLPlotter/CustomModels/
--rw-r--r--   0 eric       (501) staff       (20)        0 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/HTMLPlotter/CustomModels/__init__.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-02 19:39:03.382437 pytplot-mpl-temp-2.1.8/pytplot/HTMLPlotter/CustomModels/__pycache__/
--rw-r--r--   0 eric       (501) staff       (20)      158 2022-11-02 19:26:01.000000 pytplot-mpl-temp-2.1.8/pytplot/HTMLPlotter/CustomModels/__pycache__/__init__.cpython-310.pyc
--rw-r--r--   0 eric       (501) staff       (20)     3420 2022-11-02 19:26:01.000000 pytplot-mpl-temp-2.1.8/pytplot/HTMLPlotter/CustomModels/__pycache__/colorbarsidetitle.cpython-310.pyc
--rw-r--r--   0 eric       (501) staff       (20)     1899 2022-11-02 19:26:01.000000 pytplot-mpl-temp-2.1.8/pytplot/HTMLPlotter/CustomModels/__pycache__/timestamp.cpython-310.pyc
--rw-r--r--   0 eric       (501) staff       (20)     3400 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/HTMLPlotter/CustomModels/colorbarsidetitle.py
--rw-r--r--   0 eric       (501) staff       (20)     1875 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/HTMLPlotter/CustomModels/timestamp.py
--rw-r--r--   0 eric       (501) staff       (20)    16534 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/HTMLPlotter/TVarFigure1D.py
--rw-r--r--   0 eric       (501) staff       (20)    12622 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/HTMLPlotter/TVarFigureAlt.py
--rw-r--r--   0 eric       (501) staff       (20)    15233 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/HTMLPlotter/TVarFigureMap.py
--rw-r--r--   0 eric       (501) staff       (20)    18822 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/HTMLPlotter/TVarFigureSpec.py
--rw-r--r--   0 eric       (501) staff       (20)      496 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/HTMLPlotter/__init__.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-02 19:39:03.383123 pytplot-mpl-temp-2.1.8/pytplot/HTMLPlotter/__pycache__/
--rw-r--r--   0 eric       (501) staff       (20)    10091 2022-11-02 19:26:00.000000 pytplot-mpl-temp-2.1.8/pytplot/HTMLPlotter/__pycache__/TVarFigure1D.cpython-310.pyc
--rw-r--r--   0 eric       (501) staff       (20)     8857 2022-11-02 19:26:01.000000 pytplot-mpl-temp-2.1.8/pytplot/HTMLPlotter/__pycache__/TVarFigureAlt.cpython-310.pyc
--rw-r--r--   0 eric       (501) staff       (20)    10219 2022-11-02 19:26:01.000000 pytplot-mpl-temp-2.1.8/pytplot/HTMLPlotter/__pycache__/TVarFigureMap.cpython-310.pyc
--rw-r--r--   0 eric       (501) staff       (20)    12760 2022-11-02 19:26:01.000000 pytplot-mpl-temp-2.1.8/pytplot/HTMLPlotter/__pycache__/TVarFigureSpec.cpython-310.pyc
--rw-r--r--   0 eric       (501) staff       (20)      336 2022-11-02 19:26:00.000000 pytplot-mpl-temp-2.1.8/pytplot/HTMLPlotter/__pycache__/__init__.cpython-310.pyc
--rw-r--r--   0 eric       (501) staff       (20)     3001 2022-11-02 19:26:01.000000 pytplot-mpl-temp-2.1.8/pytplot/HTMLPlotter/__pycache__/generate.cpython-310.pyc
--rw-r--r--   0 eric       (501) staff       (20)     5558 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/HTMLPlotter/generate.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-02 19:39:03.383559 pytplot-mpl-temp-2.1.8/pytplot/MPLPlotter/
--rw-r--r--   0 eric       (501) staff       (20)        0 2022-11-02 18:48:51.000000 pytplot-mpl-temp-2.1.8/pytplot/MPLPlotter/__init__.py
--rw-r--r--   0 eric       (501) staff       (20)     7746 2022-11-02 18:48:51.000000 pytplot-mpl-temp-2.1.8/pytplot/MPLPlotter/lineplot.py
--rw-r--r--   0 eric       (501) staff       (20)     6316 2022-11-02 18:48:51.000000 pytplot-mpl-temp-2.1.8/pytplot/MPLPlotter/specplot.py
--rw-r--r--   0 eric       (501) staff       (20)    23874 2022-11-02 18:48:51.000000 pytplot-mpl-temp-2.1.8/pytplot/MPLPlotter/tplot.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-02 19:39:03.384496 pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-02 19:39:03.385048 pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/CustomAxis/
--rw-r--r--   0 eric       (501) staff       (20)    12637 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/CustomAxis/AxisItem.py
--rw-r--r--   0 eric       (501) staff       (20)      698 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/CustomAxis/BlankAxis.py
--rw-r--r--   0 eric       (501) staff       (20)     6673 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/CustomAxis/DateAxis.py
--rw-r--r--   0 eric       (501) staff       (20)     1028 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/CustomAxis/NonLinearAxis.py
--rw-r--r--   0 eric       (501) staff       (20)        0 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/CustomAxis/__init__.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-02 19:39:03.385367 pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/CustomImage/
--rw-r--r--   0 eric       (501) staff       (20)     3121 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/CustomImage/ColorbarImage.py
--rw-r--r--   0 eric       (501) staff       (20)    11843 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/CustomImage/UpdatingImage.py
--rw-r--r--   0 eric       (501) staff       (20)        0 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/CustomImage/__init__.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-02 19:39:03.385568 pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/CustomLegend/
--rw-r--r--   0 eric       (501) staff       (20)     1720 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/CustomLegend/CustomLegend.py
--rw-r--r--   0 eric       (501) staff       (20)        0 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/CustomLegend/__init__.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-02 19:39:03.385665 pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/CustomLinearRegionItem/
--rw-r--r--   0 eric       (501) staff       (20)      725 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/CustomLinearRegionItem/CustomLinearRegionItem.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-02 19:39:03.386001 pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/CustomViewBox/
--rw-r--r--   0 eric       (501) staff       (20)      114 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/CustomViewBox/CustomVB.py
--rw-r--r--   0 eric       (501) staff       (20)      262 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/CustomViewBox/NoPaddingPlot.py
--rw-r--r--   0 eric       (501) staff       (20)        0 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/CustomViewBox/__init__.py
--rw-r--r--   0 eric       (501) staff       (20)     5669 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/PyTPlot_Exporter.py
--rw-r--r--   0 eric       (501) staff       (20)    22697 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/TVarFigure1D.py
--rw-r--r--   0 eric       (501) staff       (20)    15469 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/TVarFigureAlt.py
--rw-r--r--   0 eric       (501) staff       (20)     2874 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/TVarFigureAxisOnly.py
--rw-r--r--   0 eric       (501) staff       (20)    19328 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/TVarFigureMap.py
--rw-r--r--   0 eric       (501) staff       (20)    22827 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/TVarFigureSpec.py
--rw-r--r--   0 eric       (501) staff       (20)      619 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/__init__.py
--rw-r--r--   0 eric       (501) staff       (20)     5885 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/generate.py
--rw-r--r--   0 eric       (501) staff       (20)     7386 2022-11-02 19:25:37.000000 pytplot-mpl-temp-2.1.8/pytplot/__init__.py
--rw-r--r--   0 eric       (501) staff       (20)     2405 2022-11-02 18:48:51.000000 pytplot-mpl-temp-2.1.8/pytplot/del_data.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-02 19:39:03.386288 pytplot-mpl-temp-2.1.8/pytplot/exporters/
--rw-r--r--   0 eric       (501) staff       (20)        0 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/exporters/__init__.py
--rw-r--r--   0 eric       (501) staff       (20)      793 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/exporters/tplot_ascii.py
--rw-r--r--   0 eric       (501) staff       (20)     2487 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/exporters/tplot_save.py
--rw-r--r--   0 eric       (501) staff       (20)     5287 2022-11-02 18:48:51.000000 pytplot-mpl-temp-2.1.8/pytplot/get_data.py
--rw-r--r--   0 eric       (501) staff       (20)     1275 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/get_timespan.py
--rw-r--r--   0 eric       (501) staff       (20)     1688 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/get_ylimits.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-02 19:39:03.386853 pytplot-mpl-temp-2.1.8/pytplot/importers/
--rw-r--r--   0 eric       (501) staff       (20)        0 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/importers/__init__.py
--rw-r--r--   0 eric       (501) staff       (20)    22621 2022-11-02 18:48:51.000000 pytplot-mpl-temp-2.1.8/pytplot/importers/cdf_to_tplot.py
--rw-r--r--   0 eric       (501) staff       (20)     6750 2022-11-02 18:48:51.000000 pytplot-mpl-temp-2.1.8/pytplot/importers/netcdf_to_tplot.py
--rw-r--r--   0 eric       (501) staff       (20)     7164 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/importers/sts_to_tplot.py
--rw-r--r--   0 eric       (501) staff       (20)     9525 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/importers/tplot_restore.py
--rw-r--r--   0 eric       (501) staff       (20)     1449 2022-11-02 18:48:51.000000 pytplot-mpl-temp-2.1.8/pytplot/link.py
--rw-r--r--   0 eric       (501) staff       (20)    27973 2022-11-02 18:48:51.000000 pytplot-mpl-temp-2.1.8/pytplot/options.py
--rw-r--r--   0 eric       (501) staff       (20)     1801 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/replace_data.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-02 19:39:03.386989 pytplot-mpl-temp-2.1.8/pytplot/sampledata/
--rw-r--r--   0 eric       (501) staff       (20)  6822180 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/sampledata/test_data.tplot
--rw-r--r--   0 eric       (501) staff       (20)     4471 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/spedas_colorbar.py
--rw-r--r--   0 eric       (501) staff       (20)    15425 2022-11-02 18:48:51.000000 pytplot-mpl-temp-2.1.8/pytplot/store_data.py
--rw-r--r--   0 eric       (501) staff       (20)     4540 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/timebar.py
--rw-r--r--   0 eric       (501) staff       (20)     1751 2022-11-02 18:48:51.000000 pytplot-mpl-temp-2.1.8/pytplot/timespan.py
--rw-r--r--   0 eric       (501) staff       (20)      997 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/timestamp.py
--rw-r--r--   0 eric       (501) staff       (20)     1068 2022-11-02 18:48:51.000000 pytplot-mpl-temp-2.1.8/pytplot/tlimit.py
--rw-r--r--   0 eric       (501) staff       (20)    16042 2022-11-02 18:48:51.000000 pytplot-mpl-temp-2.1.8/pytplot/tplot.py
--rw-r--r--   0 eric       (501) staff       (20)     2203 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/tplot_copy.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-02 19:39:03.393278 pytplot-mpl-temp-2.1.8/pytplot/tplot_math/
--rw-r--r--   0 eric       (501) staff       (20)      856 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/tplot_math/__init__.py
--rw-r--r--   0 eric       (501) staff       (20)     1939 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/tplot_math/add.py
--rw-r--r--   0 eric       (501) staff       (20)     4164 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/tplot_math/add_across.py
--rw-r--r--   0 eric       (501) staff       (20)     1517 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/tplot_math/avg_res_data.py
--rw-r--r--   0 eric       (501) staff       (20)     1733 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/tplot_math/clip.py
--rw-r--r--   0 eric       (501) staff       (20)     2497 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/tplot_math/crop.py
--rw-r--r--   0 eric       (501) staff       (20)     1699 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/tplot_math/deflag.py
--rw-r--r--   0 eric       (501) staff       (20)     2571 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/tplot_math/degap.py
--rw-r--r--   0 eric       (501) staff       (20)     1501 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/tplot_math/derive.py
--rw-r--r--   0 eric       (501) staff       (20)     1961 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/tplot_math/divide.py
--rw-r--r--   0 eric       (501) staff       (20)     4112 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/tplot_math/examples.py
--rw-r--r--   0 eric       (501) staff       (20)     2661 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/tplot_math/flatten.py
--rw-r--r--   0 eric       (501) staff       (20)     1730 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/tplot_math/interp_nan.py
--rw-r--r--   0 eric       (501) staff       (20)     3173 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/tplot_math/join_vec.py
--rw-r--r--   0 eric       (501) staff       (20)     1870 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/tplot_math/multiply.py
--rw-r--r--   0 eric       (501) staff       (20)     2365 2022-11-02 18:48:51.000000 pytplot-mpl-temp-2.1.8/pytplot/tplot_math/pwr_spec.py
--rw-r--r--   0 eric       (501) staff       (20)     1802 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/tplot_math/resample.py
--rw-r--r--   0 eric       (501) staff       (20)     1564 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/tplot_math/spec_mult.py
--rw-r--r--   0 eric       (501) staff       (20)     2655 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/tplot_math/split_vec.py
--rw-r--r--   0 eric       (501) staff       (20)     1901 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/tplot_math/subtract.py
--rw-r--r--   0 eric       (501) staff       (20)     1657 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/tplot_math/tinterp.py
--rw-r--r--   0 eric       (501) staff       (20)     2072 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/tplot_names.py
--rw-r--r--   0 eric       (501) staff       (20)     3130 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/tplot_options.py
--rw-r--r--   0 eric       (501) staff       (20)     1777 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/tplot_rename.py
--rw-r--r--   0 eric       (501) staff       (20)    29919 2022-11-02 18:48:51.000000 pytplot-mpl-temp-2.1.8/pytplot/tplot_utilities.py
--rw-r--r--   0 eric       (501) staff       (20)     6690 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/version.txt
--rw-r--r--   0 eric       (501) staff       (20)     1839 2022-11-02 18:48:51.000000 pytplot-mpl-temp-2.1.8/pytplot/xlim.py
--rw-r--r--   0 eric       (501) staff       (20)     1211 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/ylim.py
--rw-r--r--   0 eric       (501) staff       (20)     1380 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/pytplot/zlim.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-02 19:39:03.395264 pytplot-mpl-temp-2.1.8/pytplot_mpl_temp.egg-info/
--rw-r--r--   0 eric       (501) staff       (20)     3177 2022-11-02 19:39:03.000000 pytplot-mpl-temp-2.1.8/pytplot_mpl_temp.egg-info/PKG-INFO
--rw-r--r--   0 eric       (501) staff       (20)     4093 2022-11-02 19:39:03.000000 pytplot-mpl-temp-2.1.8/pytplot_mpl_temp.egg-info/SOURCES.txt
--rw-r--r--   0 eric       (501) staff       (20)        1 2022-11-02 19:39:03.000000 pytplot-mpl-temp-2.1.8/pytplot_mpl_temp.egg-info/dependency_links.txt
--rw-r--r--   0 eric       (501) staff       (20)       20 2022-11-02 19:39:03.000000 pytplot-mpl-temp-2.1.8/pytplot_mpl_temp.egg-info/entry_points.txt
--rw-r--r--   0 eric       (501) staff       (20)      154 2022-11-02 19:39:03.000000 pytplot-mpl-temp-2.1.8/pytplot_mpl_temp.egg-info/requires.txt
--rw-r--r--   0 eric       (501) staff       (20)       14 2022-11-02 19:39:03.000000 pytplot-mpl-temp-2.1.8/pytplot_mpl_temp.egg-info/top_level.txt
--rw-r--r--   0 eric       (501) staff       (20)     1474 2022-11-02 19:39:03.396831 pytplot-mpl-temp-2.1.8/setup.cfg
--rw-r--r--   0 eric       (501) staff       (20)     1311 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/setup.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-02 19:39:03.396243 pytplot-mpl-temp-2.1.8/tests/
--rw-r--r--   0 eric       (501) staff       (20)        0 2022-11-02 18:48:16.000000 pytplot-mpl-temp-2.1.8/tests/__init__.py
--rw-r--r--   0 eric       (501) staff       (20)      852 2022-11-02 18:48:51.000000 pytplot-mpl-temp-2.1.8/tests/test_alt_plot.py
--rw-r--r--   0 eric       (501) staff       (20)     1064 2022-11-02 18:48:51.000000 pytplot-mpl-temp-2.1.8/tests/test_cdf_to_tplot.py
--rw-r--r--   0 eric       (501) staff       (20)     1105 2022-11-02 18:48:51.000000 pytplot-mpl-temp-2.1.8/tests/test_maps.py
--rw-r--r--   0 eric       (501) staff       (20)    19106 2022-11-02 18:48:51.000000 pytplot-mpl-temp-2.1.8/tests/test_matplotlib.py
--rw-r--r--   0 eric       (501) staff       (20)      651 2022-11-02 18:48:51.000000 pytplot-mpl-temp-2.1.8/tests/test_netcdf_to_tplot.py
--rw-r--r--   0 eric       (501) staff       (20)      140 2022-11-02 18:48:51.000000 pytplot-mpl-temp-2.1.8/tests/test_qt_import.py
--rw-r--r--   0 eric       (501) staff       (20)     2764 2022-11-02 18:48:51.000000 pytplot-mpl-temp-2.1.8/tests/test_tplot_math.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-12-07 22:12:05.466220 pytplot-mpl-temp-2.1.9/
+-rw-rw-r--   0 eric       (501) staff       (20)     1065 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/LICENSE
+-rw-rw-r--   0 eric       (501) staff       (20)      363 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/MANIFEST.in
+-rw-r--r--   0 eric       (501) staff       (20)     3177 2022-12-07 22:12:05.466306 pytplot-mpl-temp-2.1.9/PKG-INFO
+-rw-rw-r--   0 eric       (501) staff       (20)     2510 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/README.md
+-rw-rw-r--   0 eric       (501) staff       (20)     2889 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/README.rst
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-12-07 22:12:05.443509 pytplot-mpl-temp-2.1.9/docs/
+-rw-rw-r--   0 eric       (501) staff       (20)     8107 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/docs/pytplot_tutorial.html
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-12-07 22:12:05.447947 pytplot-mpl-temp-2.1.9/pytplot/
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-12-07 22:12:05.448628 pytplot-mpl-temp-2.1.9/pytplot/AncillaryPlots/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/AncillaryPlots/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     5398 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/AncillaryPlots/position_mars_2d.py
+-rw-rw-r--   0 eric       (501) staff       (20)     5105 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/AncillaryPlots/position_mars_3d.py
+-rw-rw-r--   0 eric       (501) staff       (20)    11294 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/AncillaryPlots/spec_slicer.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-12-07 22:12:05.449696 pytplot-mpl-temp-2.1.9/pytplot/HTMLPlotter/
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-12-07 22:12:05.450092 pytplot-mpl-temp-2.1.9/pytplot/HTMLPlotter/CustomModels/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/HTMLPlotter/CustomModels/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3400 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/HTMLPlotter/CustomModels/colorbarsidetitle.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1875 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/HTMLPlotter/CustomModels/timestamp.py
+-rw-rw-r--   0 eric       (501) staff       (20)    16534 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/HTMLPlotter/TVarFigure1D.py
+-rw-rw-r--   0 eric       (501) staff       (20)    12622 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/HTMLPlotter/TVarFigureAlt.py
+-rw-rw-r--   0 eric       (501) staff       (20)    15233 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/HTMLPlotter/TVarFigureMap.py
+-rw-rw-r--   0 eric       (501) staff       (20)    18822 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/HTMLPlotter/TVarFigureSpec.py
+-rw-rw-r--   0 eric       (501) staff       (20)      496 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/HTMLPlotter/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     5558 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/HTMLPlotter/generate.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-12-07 22:12:05.450622 pytplot-mpl-temp-2.1.9/pytplot/MPLPlotter/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/MPLPlotter/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     7856 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/MPLPlotter/lineplot.py
+-rw-rw-r--   0 eric       (501) staff       (20)     6316 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/MPLPlotter/specplot.py
+-rw-rw-r--   0 eric       (501) staff       (20)    23874 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/MPLPlotter/tplot.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-12-07 22:12:05.451993 pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-12-07 22:12:05.452711 pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/CustomAxis/
+-rw-rw-r--   0 eric       (501) staff       (20)    12637 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/CustomAxis/AxisItem.py
+-rw-rw-r--   0 eric       (501) staff       (20)      698 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/CustomAxis/BlankAxis.py
+-rw-rw-r--   0 eric       (501) staff       (20)     6673 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/CustomAxis/DateAxis.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1028 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/CustomAxis/NonLinearAxis.py
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/CustomAxis/__init__.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-12-07 22:12:05.453110 pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/CustomImage/
+-rw-rw-r--   0 eric       (501) staff       (20)     3121 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/CustomImage/ColorbarImage.py
+-rw-rw-r--   0 eric       (501) staff       (20)    11843 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/CustomImage/UpdatingImage.py
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/CustomImage/__init__.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-12-07 22:12:05.453368 pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/CustomLegend/
+-rw-rw-r--   0 eric       (501) staff       (20)     1720 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/CustomLegend/CustomLegend.py
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/CustomLegend/__init__.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-12-07 22:12:05.453475 pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/CustomLinearRegionItem/
+-rw-rw-r--   0 eric       (501) staff       (20)      725 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/CustomLinearRegionItem/CustomLinearRegionItem.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-12-07 22:12:05.453920 pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/CustomViewBox/
+-rw-rw-r--   0 eric       (501) staff       (20)      114 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/CustomViewBox/CustomVB.py
+-rw-rw-r--   0 eric       (501) staff       (20)      262 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/CustomViewBox/NoPaddingPlot.py
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/CustomViewBox/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     5669 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/PyTPlot_Exporter.py
+-rw-rw-r--   0 eric       (501) staff       (20)    22697 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/TVarFigure1D.py
+-rw-rw-r--   0 eric       (501) staff       (20)    15469 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/TVarFigureAlt.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2874 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/TVarFigureAxisOnly.py
+-rw-rw-r--   0 eric       (501) staff       (20)    19328 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/TVarFigureMap.py
+-rw-rw-r--   0 eric       (501) staff       (20)    22827 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/TVarFigureSpec.py
+-rw-rw-r--   0 eric       (501) staff       (20)      619 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     5885 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/generate.py
+-rw-rw-r--   0 eric       (501) staff       (20)     7386 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2405 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/del_data.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-12-07 22:12:05.454258 pytplot-mpl-temp-2.1.9/pytplot/exporters/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/exporters/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      793 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/exporters/tplot_ascii.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2487 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/exporters/tplot_save.py
+-rw-rw-r--   0 eric       (501) staff       (20)     5287 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/get_data.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1275 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/get_timespan.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1688 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/get_ylimits.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-12-07 22:12:05.455046 pytplot-mpl-temp-2.1.9/pytplot/importers/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/importers/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)    22645 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/importers/cdf_to_tplot.py
+-rw-rw-r--   0 eric       (501) staff       (20)     6750 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/importers/netcdf_to_tplot.py
+-rw-rw-r--   0 eric       (501) staff       (20)     7164 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/importers/sts_to_tplot.py
+-rw-rw-r--   0 eric       (501) staff       (20)     9525 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/importers/tplot_restore.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1449 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/link.py
+-rw-rw-r--   0 eric       (501) staff       (20)    27973 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/options.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1801 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/replace_data.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-12-07 22:12:05.455195 pytplot-mpl-temp-2.1.9/pytplot/sampledata/
+-rw-rw-r--   0 eric       (501) staff       (20)  6822180 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/sampledata/test_data.tplot
+-rw-rw-r--   0 eric       (501) staff       (20)     4471 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/spedas_colorbar.py
+-rw-rw-r--   0 eric       (501) staff       (20)    15425 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/store_data.py
+-rw-rw-r--   0 eric       (501) staff       (20)     4540 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/timebar.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1751 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/timespan.py
+-rw-rw-r--   0 eric       (501) staff       (20)      997 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/timestamp.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1068 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/tlimit.py
+-rw-rw-r--   0 eric       (501) staff       (20)    16042 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/tplot.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2203 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/tplot_copy.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-12-07 22:12:05.463804 pytplot-mpl-temp-2.1.9/pytplot/tplot_math/
+-rw-rw-r--   0 eric       (501) staff       (20)      856 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/tplot_math/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1939 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/tplot_math/add.py
+-rw-rw-r--   0 eric       (501) staff       (20)     4164 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/tplot_math/add_across.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1517 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/tplot_math/avg_res_data.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1733 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/tplot_math/clip.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2497 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/tplot_math/crop.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1699 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/tplot_math/deflag.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2571 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/tplot_math/degap.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1501 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/tplot_math/derive.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1961 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/tplot_math/divide.py
+-rw-rw-r--   0 eric       (501) staff       (20)     4112 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/tplot_math/examples.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2661 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/tplot_math/flatten.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1730 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/tplot_math/interp_nan.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3173 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/tplot_math/join_vec.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1870 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/tplot_math/multiply.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2365 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/tplot_math/pwr_spec.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1802 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/tplot_math/resample.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1564 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/tplot_math/spec_mult.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2655 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/tplot_math/split_vec.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1901 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/tplot_math/subtract.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1657 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/tplot_math/tinterp.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2072 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/tplot_names.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3130 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/tplot_options.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1777 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/tplot_rename.py
+-rw-rw-r--   0 eric       (501) staff       (20)    29919 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/tplot_utilities.py
+-rw-rw-r--   0 eric       (501) staff       (20)     6690 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/version.txt
+-rw-rw-r--   0 eric       (501) staff       (20)     1839 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/xlim.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1211 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/ylim.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1380 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/pytplot/zlim.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-12-07 22:12:05.464512 pytplot-mpl-temp-2.1.9/pytplot_mpl_temp.egg-info/
+-rw-r--r--   0 eric       (501) staff       (20)     3177 2022-12-07 22:12:05.000000 pytplot-mpl-temp-2.1.9/pytplot_mpl_temp.egg-info/PKG-INFO
+-rw-r--r--   0 eric       (501) staff       (20)     3511 2022-12-07 22:12:05.000000 pytplot-mpl-temp-2.1.9/pytplot_mpl_temp.egg-info/SOURCES.txt
+-rw-r--r--   0 eric       (501) staff       (20)        1 2022-12-07 22:12:05.000000 pytplot-mpl-temp-2.1.9/pytplot_mpl_temp.egg-info/dependency_links.txt
+-rw-r--r--   0 eric       (501) staff       (20)       20 2022-12-07 22:12:05.000000 pytplot-mpl-temp-2.1.9/pytplot_mpl_temp.egg-info/entry_points.txt
+-rw-r--r--   0 eric       (501) staff       (20)      154 2022-12-07 22:12:05.000000 pytplot-mpl-temp-2.1.9/pytplot_mpl_temp.egg-info/requires.txt
+-rw-r--r--   0 eric       (501) staff       (20)       14 2022-12-07 22:12:05.000000 pytplot-mpl-temp-2.1.9/pytplot_mpl_temp.egg-info/top_level.txt
+-rw-rw-r--   0 eric       (501) staff       (20)     1474 2022-12-07 22:12:05.466719 pytplot-mpl-temp-2.1.9/setup.cfg
+-rw-rw-r--   0 eric       (501) staff       (20)     1311 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/setup.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-12-07 22:12:05.466030 pytplot-mpl-temp-2.1.9/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      852 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/tests/test_alt_plot.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1064 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/tests/test_cdf_to_tplot.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1105 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/tests/test_maps.py
+-rw-rw-r--   0 eric       (501) staff       (20)    19106 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/tests/test_matplotlib.py
+-rw-rw-r--   0 eric       (501) staff       (20)      651 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/tests/test_netcdf_to_tplot.py
+-rw-rw-r--   0 eric       (501) staff       (20)      140 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/tests/test_qt_import.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2764 2022-12-07 22:11:14.000000 pytplot-mpl-temp-2.1.9/tests/test_tplot_math.py
```

### Comparing `pytplot-mpl-temp-2.1.8/LICENSE` & `pytplot-mpl-temp-2.1.9/LICENSE`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/PKG-INFO` & `pytplot-mpl-temp-2.1.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pytplot-mpl-temp
-Version: 2.1.8
+Version: 2.1.9
 Summary: A python version of IDL tplot libraries
 Home-page: https://github.com/MAVENSDC/pytplot
 Author: MAVEN SDC
 Author-email: mavensdc@lasp.colorado.edu
 License: UNKNOWN
 Keywords: tplot,maven,lasp,IDL,spedas
 Platform: UNKNOWN
```

### Comparing `pytplot-mpl-temp-2.1.8/README.md` & `pytplot-mpl-temp-2.1.9/README.md`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/README.rst` & `pytplot-mpl-temp-2.1.9/README.rst`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/docs/pytplot_tutorial.html` & `pytplot-mpl-temp-2.1.9/docs/pytplot_tutorial.html`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/AncillaryPlots/position_mars_2d.py` & `pytplot-mpl-temp-2.1.9/pytplot/AncillaryPlots/position_mars_2d.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/AncillaryPlots/position_mars_3d.py` & `pytplot-mpl-temp-2.1.9/pytplot/AncillaryPlots/position_mars_3d.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/AncillaryPlots/spec_slicer.py` & `pytplot-mpl-temp-2.1.9/pytplot/AncillaryPlots/spec_slicer.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/HTMLPlotter/CustomModels/__pycache__/colorbarsidetitle.cpython-310.pyc` & `pytplot-mpl-temp-2.1.9/pytplot/HTMLPlotter/CustomModels/colorbarsidetitle.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,214 +1,213 @@
-00000000: 6f0d 0d0a 0000 0000 70bb 6263 480d 0000  o.......p.bcH...
-00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
-00000020: 0004 0000 0040 0000 0073 3000 0000 6400  .....@...s0...d.
-00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
-00000040: 6d03 5a03 0100 6403 5a04 4700 6404 6405  m.Z...d.Z.G.d.d.
-00000050: 8400 6405 6501 8303 5a05 6406 5300 2907  ..d.e...Z.d.S.).
-00000060: e900 0000 0029 01da 0843 6f6c 6f72 4261  .....)...ColorBa
-00000070: 7229 01da 0a54 7970 6553 6372 6970 7461  r)...TypeScripta
-00000080: 640b 0000 0a69 6d70 6f72 7420 7b43 6f6c  d....import {Col
-00000090: 6f72 4261 722c 2043 6f6c 6f72 4261 7256  orBar, ColorBarV
-000000a0: 6965 777d 2066 726f 6d20 226d 6f64 656c  iew} from "model
-000000b0: 732f 616e 6e6f 7461 7469 6f6e 732f 636f  s/annotations/co
-000000c0: 6c6f 725f 6261 7222 0a69 6d70 6f72 7420  lor_bar".import 
-000000d0: 2a20 6173 2070 2066 726f 6d20 2263 6f72  * as p from "cor
-000000e0: 652f 7072 6f70 6572 7469 6573 220a 696d  e/properties".im
-000000f0: 706f 7274 207b 436f 6e74 6578 7432 647d  port {Context2d}
-00000100: 2066 726f 6d20 2263 6f72 652f 7574 696c   from "core/util
-00000110: 2f63 616e 7661 7322 0a0a 636f 6e73 7420  /canvas"..const 
-00000120: 5348 4f52 545f 4449 4d20 3d20 3235 0a0a  SHORT_DIM = 25..
-00000130: 6578 706f 7274 2063 6c61 7373 2043 6f6c  export class Col
-00000140: 6f72 4261 7253 6964 6554 6974 6c65 5669  orBarSideTitleVi
-00000150: 6577 2065 7874 656e 6473 2043 6f6c 6f72  ew extends Color
-00000160: 4261 7256 6965 7720 7b0a 2020 6d6f 6465  BarView {.  mode
-00000170: 6c3a 2043 6f6c 6f72 4261 7253 6964 6554  l: ColorBarSideT
-00000180: 6974 6c65 0a20 2070 726f 7465 6374 6564  itle.  protected
-00000190: 2069 6d61 6765 3a20 4854 4d4c 4361 6e76   image: HTMLCanv
-000001a0: 6173 456c 656d 656e 740a 0a20 2063 6f6d  asElement..  com
-000001b0: 7075 7465 5f6c 6567 656e 645f 6469 6d65  pute_legend_dime
-000001c0: 6e73 696f 6e73 2829 3a20 7b77 6964 7468  nsions(): {width
-000001d0: 3a20 6e75 6d62 6572 2c20 6865 6967 6874  : number, height
-000001e0: 3a20 6e75 6d62 6572 7d20 7b0a 2020 2020  : number} {.    
-000001f0: 636f 6e73 7420 696d 6167 655f 6469 6d65  const image_dime
-00000200: 6e73 696f 6e73 203d 2074 6869 732e 5f63  nsions = this._c
-00000210: 6f6d 7075 7465 645f 696d 6167 655f 6469  omputed_image_di
-00000220: 6d65 6e73 696f 6e73 2829 0a20 2020 2063  mensions().    c
-00000230: 6f6e 7374 205b 696d 6167 655f 6865 6967  onst [image_heig
-00000240: 6874 2c20 696d 6167 655f 7769 6474 685d  ht, image_width]
-00000250: 203d 205b 696d 6167 655f 6469 6d65 6e73   = [image_dimens
-00000260: 696f 6e73 2e68 6569 6768 742c 2069 6d61  ions.height, ima
-00000270: 6765 5f64 696d 656e 7369 6f6e 732e 7769  ge_dimensions.wi
-00000280: 6474 685d 0a0a 2020 2020 636f 6e73 7420  dth]..    const 
-00000290: 6c61 6265 6c5f 6578 7465 6e74 203d 2074  label_extent = t
-000002a0: 6869 732e 5f67 6574 5f6c 6162 656c 5f65  his._get_label_e
-000002b0: 7874 656e 7428 290a 2020 2020 636f 6e73  xtent().    cons
-000002c0: 7420 7469 746c 655f 6578 7465 6e74 203d  t title_extent =
-000002d0: 2074 6869 732e 5f74 6974 6c65 5f65 7874   this._title_ext
-000002e0: 656e 7428 290a 2020 2020 636f 6e73 7420  ent().    const 
-000002f0: 7469 636b 5f65 7874 656e 7420 3d20 7468  tick_extent = th
-00000300: 6973 2e5f 7469 636b 5f65 7874 656e 7428  is._tick_extent(
-00000310: 290a 2020 2020 636f 6e73 7420 7b70 6164  ).    const {pad
-00000320: 6469 6e67 7d20 3d20 7468 6973 2e6d 6f64  ding} = this.mod
-00000330: 656c 0a0a 2020 2020 6c65 7420 6c65 6765  el..    let lege
-00000340: 6e64 5f68 6569 6768 743a 206e 756d 6265  nd_height: numbe
-00000350: 722c 206c 6567 656e 645f 7769 6474 683a  r, legend_width:
-00000360: 206e 756d 6265 720a 2020 2020 6c65 6765   number.    lege
-00000370: 6e64 5f68 6569 6768 7420 3d20 696d 6167  nd_height = imag
-00000380: 655f 6865 6967 6874 0a20 2020 206c 6567  e_height.    leg
-00000390: 656e 645f 7769 6474 6820 3d20 696d 6167  end_width = imag
-000003a0: 655f 7769 6474 6820 2b20 7469 636b 5f65  e_width + tick_e
-000003b0: 7874 656e 7420 2b20 6c61 6265 6c5f 6578  xtent + label_ex
-000003c0: 7465 6e74 202b 2074 6974 6c65 5f65 7874  tent + title_ext
-000003d0: 656e 7420 2b20 322a 7061 6464 696e 670a  ent + 2*padding.
-000003e0: 0a20 2020 2072 6574 7572 6e20 7b77 6964  .    return {wid
-000003f0: 7468 3a20 6c65 6765 6e64 5f77 6964 7468  th: legend_width
-00000400: 2c20 6865 6967 6874 3a20 6c65 6765 6e64  , height: legend
-00000410: 5f68 6569 6768 747d 0a20 207d 0a0a 2020  _height}.  }..  
-00000420: 7072 6f74 6563 7465 6420 5f64 7261 775f  protected _draw_
-00000430: 696d 6167 6528 6374 783a 2043 6f6e 7465  image(ctx: Conte
-00000440: 7874 3264 293a 2076 6f69 6420 7b0a 2020  xt2d): void {.  
-00000450: 2020 636f 6e73 7420 696d 6167 6520 3d20    const image = 
-00000460: 7468 6973 2e5f 636f 6d70 7574 6564 5f69  this._computed_i
-00000470: 6d61 6765 5f64 696d 656e 7369 6f6e 7328  mage_dimensions(
-00000480: 290a 2020 2020 6374 782e 7361 7665 2829  ).    ctx.save()
-00000490: 0a20 2020 2063 7478 2e73 6574 496d 6167  .    ctx.setImag
-000004a0: 6553 6d6f 6f74 6869 6e67 456e 6162 6c65  eSmoothingEnable
-000004b0: 6428 6661 6c73 6529 0a20 2020 2063 7478  d(false).    ctx
-000004c0: 2e67 6c6f 6261 6c41 6c70 6861 203d 2074  .globalAlpha = t
-000004d0: 6869 732e 6d6f 6465 6c2e 7363 616c 655f  his.model.scale_
-000004e0: 616c 7068 610a 2020 2020 6374 782e 6472  alpha.    ctx.dr
-000004f0: 6177 496d 6167 6528 7468 6973 2e69 6d61  awImage(this.ima
-00000500: 6765 2c20 302c 2030 2c20 696d 6167 652e  ge, 0, 0, image.
-00000510: 7769 6474 682c 2069 6d61 6765 2e68 6569  width, image.hei
-00000520: 6768 7429 0a20 2020 2069 6620 2874 6869  ght).    if (thi
-00000530: 732e 7669 7375 616c 732e 6261 725f 6c69  s.visuals.bar_li
-00000540: 6e65 2e64 6f69 7429 207b 0a20 2020 2020  ne.doit) {.     
-00000550: 2074 6869 732e 7669 7375 616c 732e 6261   this.visuals.ba
-00000560: 725f 6c69 6e65 2e73 6574 5f76 616c 7565  r_line.set_value
-00000570: 2863 7478 290a 2020 2020 2020 6374 782e  (ctx).      ctx.
-00000580: 7374 726f 6b65 5265 6374 2830 2c20 302c  strokeRect(0, 0,
-00000590: 2069 6d61 6765 2e77 6964 7468 2c20 696d   image.width, im
-000005a0: 6167 652e 6865 6967 6874 290a 2020 2020  age.height).    
-000005b0: 7d0a 2020 2020 6374 782e 7265 7374 6f72  }.    ctx.restor
-000005c0: 6528 290a 2020 7d0a 0a20 2070 726f 7465  e().  }..  prote
-000005d0: 6374 6564 205f 6472 6177 5f74 6974 6c65  cted _draw_title
-000005e0: 2863 7478 3a20 436f 6e74 6578 7432 6429  (ctx: Context2d)
-000005f0: 3a20 766f 6964 207b 0a20 2020 2069 6620  : void {.    if 
-00000600: 2821 7468 6973 2e76 6973 7561 6c73 2e74  (!this.visuals.t
-00000610: 6974 6c65 5f74 6578 742e 646f 6974 290a  itle_text.doit).
-00000620: 2020 2020 2020 7265 7475 726e 0a20 2020        return.   
-00000630: 2063 6f6e 7374 206c 6162 656c 5f65 7874   const label_ext
-00000640: 656e 7420 3d20 7468 6973 2e5f 6765 745f  ent = this._get_
-00000650: 6c61 6265 6c5f 6578 7465 6e74 2829 0a20  label_extent(). 
-00000660: 2020 2063 6f6e 7374 2074 6963 6b5f 6578     const tick_ex
-00000670: 7465 6e74 203d 2074 6869 732e 5f74 6963  tent = this._tic
-00000680: 6b5f 6578 7465 6e74 2829 0a20 2020 2063  k_extent().    c
-00000690: 6f6e 7374 207b 7061 6464 696e 677d 203d  onst {padding} =
-000006a0: 2074 6869 732e 6d6f 6465 6c0a 2020 2020   this.model.    
-000006b0: 6374 782e 7361 7665 2829 0a20 2020 2074  ctx.save().    t
-000006c0: 6869 732e 7669 7375 616c 732e 7469 746c  his.visuals.titl
-000006d0: 655f 7465 7874 2e73 6574 5f76 616c 7565  e_text.set_value
-000006e0: 2863 7478 290a 2020 2020 6374 782e 726f  (ctx).    ctx.ro
-000006f0: 7461 7465 282d 4d61 7468 2e50 492f 3229  tate(-Math.PI/2)
-00000700: 0a20 2020 2063 7478 2e66 696c 6c54 6578  .    ctx.fillTex
-00000710: 7428 7468 6973 2e6d 6f64 656c 2e74 6974  t(this.model.tit
-00000720: 6c65 2c20 2d74 6869 732e 706c 6f74 5f76  le, -this.plot_v
-00000730: 6965 772e 6672 616d 652e 5f68 6569 6768  iew.frame._heigh
-00000740: 742e 7661 6c75 6520 2a20 302e 3520 2c20  t.value * 0.5 , 
-00000750: 7468 6973 2e69 6d61 6765 2e77 6964 7468  this.image.width
-00000760: 202b 2074 6963 6b5f 6578 7465 6e74 202b   + tick_extent +
-00000770: 206c 6162 656c 5f65 7874 656e 7420 2b20   label_extent + 
-00000780: 342a 7061 6464 696e 6729 0a20 2020 2063  4*padding).    c
-00000790: 7478 2e74 6578 7441 6c69 676e 3d22 6365  tx.textAlign="ce
-000007a0: 6e74 6572 220a 2020 2020 6374 782e 7265  nter".    ctx.re
-000007b0: 7374 6f72 6528 290a 2020 7d0a 0a20 202f  store().  }..  /
-000007c0: 2a70 726f 7465 6374 6564 2a2f 205f 6765  *protected*/ _ge
-000007d0: 745f 696d 6167 655f 6f66 6673 6574 2829  t_image_offset()
-000007e0: 3a20 7b78 3a20 6e75 6d62 6572 2c20 793a  : {x: number, y:
-000007f0: 206e 756d 6265 727d 207b 0a20 2020 202f   number} {.    /
-00000800: 2f20 5265 7475 726e 7320 696d 6167 6520  / Returns image 
-00000810: 6f66 6673 6574 2072 656c 6174 6976 6520  offset relative 
-00000820: 746f 206c 6567 656e 6420 626f 756e 6469  to legend boundi
-00000830: 6e67 2062 6f78 0a20 2020 2063 6f6e 7374  ng box.    const
-00000840: 2078 203d 2074 6869 732e 6d6f 6465 6c2e   x = this.model.
-00000850: 7061 6464 696e 670a 2020 2020 636f 6e73  padding.    cons
-00000860: 7420 7920 3d20 300a 2020 2020 7265 7475  t y = 0.    retu
-00000870: 726e 207b 782c 2079 7d0a 2020 7d0a 0a20  rn {x, y}.  }.. 
-00000880: 205f 636f 6d70 7574 6564 5f69 6d61 6765   _computed_image
-00000890: 5f64 696d 656e 7369 6f6e 7328 293a 207b  _dimensions(): {
-000008a0: 6865 6967 6874 3a20 6e75 6d62 6572 2c20  height: number, 
-000008b0: 7769 6474 683a 206e 756d 6265 727d 207b  width: number} {
-000008c0: 0a20 2020 2063 6f6e 7374 2066 7261 6d65  .    const frame
-000008d0: 5f68 6569 6768 7420 3d20 7468 6973 2e70  _height = this.p
-000008e0: 6c6f 745f 7669 6577 2e66 7261 6d65 2e5f  lot_view.frame._
-000008f0: 6865 6967 6874 2e76 616c 7565 0a20 2020  height.value.   
-00000900: 206c 6574 2068 6569 6768 743a 206e 756d   let height: num
-00000910: 6265 722c 2077 6964 7468 3a20 6e75 6d62  ber, width: numb
-00000920: 6572 0a20 2020 2069 6620 2874 6869 732e  er.    if (this.
-00000930: 6d6f 6465 6c2e 6865 6967 6874 203d 3d20  model.height == 
-00000940: 2761 7574 6f27 2920 7b0a 2020 2020 2020  'auto') {.      
-00000950: 2020 6865 6967 6874 203d 2066 7261 6d65    height = frame
-00000960: 5f68 6569 6768 740a 2020 2020 7d20 656c  _height.    } el
-00000970: 7365 0a20 2020 2068 6569 6768 7420 3d20  se.    height = 
-00000980: 7468 6973 2e6d 6f64 656c 2e68 6569 6768  this.model.heigh
-00000990: 740a 0a20 2020 2077 6964 7468 203d 2074  t..    width = t
-000009a0: 6869 732e 6d6f 6465 6c2e 7769 6474 6820  his.model.width 
-000009b0: 3d3d 2027 6175 746f 2720 3f20 5348 4f52  == 'auto' ? SHOR
-000009c0: 545f 4449 4d20 3a20 7468 6973 2e6d 6f64  T_DIM : this.mod
-000009d0: 656c 2e77 6964 7468 0a0a 2020 2020 7265  el.width..    re
-000009e0: 7475 726e 207b 7769 6474 682c 2068 6569  turn {width, hei
-000009f0: 6768 747d 0a20 207d 0a0a 2020 2f2f 207d  ght}.  }..  // }
-00000a00: 7d7d 0a7d 0a0a 6578 706f 7274 206e 616d  }}.}..export nam
-00000a10: 6573 7061 6365 2043 6f6c 6f72 4261 7253  espace ColorBarS
-00000a20: 6964 6554 6974 6c65 207b 0a20 2065 7870  ideTitle {.  exp
-00000a30: 6f72 7420 7479 7065 2041 7474 7273 203d  ort type Attrs =
-00000a40: 2070 2e41 7474 7273 4f66 3c50 726f 7073   p.AttrsOf<Props
-00000a50: 3e0a 0a20 2065 7870 6f72 7420 7479 7065  >..  export type
-00000a60: 2050 726f 7073 203d 2043 6f6c 6f72 4261   Props = ColorBa
-00000a70: 722e 5072 6f70 730a 7d0a 0a65 7870 6f72  r.Props.}..expor
-00000a80: 7420 696e 7465 7266 6163 6520 436f 6c6f  t interface Colo
-00000a90: 7242 6172 5369 6465 5469 746c 6520 6578  rBarSideTitle ex
-00000aa0: 7465 6e64 7320 436f 6c6f 7242 6172 5369  tends ColorBarSi
-00000ab0: 6465 5469 746c 652e 4174 7472 7320 7b7d  deTitle.Attrs {}
-00000ac0: 0a0a 6578 706f 7274 2063 6c61 7373 2043  ..export class C
-00000ad0: 6f6c 6f72 4261 7253 6964 6554 6974 6c65  olorBarSideTitle
-00000ae0: 2065 7874 656e 6473 2043 6f6c 6f72 4261   extends ColorBa
-00000af0: 7220 7b0a 2020 7072 6f70 6572 7469 6573  r {.  properties
-00000b00: 3a20 436f 6c6f 7242 6172 5369 6465 5469  : ColorBarSideTi
-00000b10: 746c 652e 5072 6f70 730a 2020 0a20 2063  tle.Props.  .  c
-00000b20: 6f6e 7374 7275 6374 6f72 2861 7474 7273  onstructor(attrs
-00000b30: 3f3a 2050 6172 7469 616c 3c43 6f6c 6f72  ?: Partial<Color
-00000b40: 4261 7253 6964 6554 6974 6c65 2e41 7474  BarSideTitle.Att
-00000b50: 7273 3e29 207b 0a20 2020 2073 7570 6572  rs>) {.    super
-00000b60: 2861 7474 7273 290a 2020 7d0a 0a20 2073  (attrs).  }..  s
-00000b70: 7461 7469 6320 696e 6974 436c 6173 7328  tatic initClass(
-00000b80: 293a 2076 6f69 6420 7b0a 2020 2020 7468  ): void {.    th
-00000b90: 6973 2e70 726f 746f 7479 7065 2e64 6566  is.prototype.def
-00000ba0: 6175 6c74 5f76 6965 7720 3d20 436f 6c6f  ault_view = Colo
-00000bb0: 7242 6172 5369 6465 5469 746c 6556 6965  rBarSideTitleVie
-00000bc0: 770a 2020 7d0a 7d0a 0a43 6f6c 6f72 4261  w.  }.}..ColorBa
-00000bd0: 7253 6964 6554 6974 6c65 2e69 6e69 7443  rSideTitle.initC
-00000be0: 6c61 7373 2829 0a0a 6300 0000 0000 0000  lass()..c.......
-00000bf0: 0000 0000 0000 0000 0002 0000 0040 0000  .............@..
-00000c00: 0073 1400 0000 6500 5a01 6400 5a02 6503  .s....e.Z.d.Z.e.
-00000c10: 6504 8301 5a05 6401 5300 2902 da11 436f  e...Z.d.S.)...Co
-00000c20: 6c6f 7242 6172 5369 6465 5469 746c 654e  lorBarSideTitleN
-00000c30: 2906 da08 5f5f 6e61 6d65 5f5f da0a 5f5f  )...__name__..__
-00000c40: 6d6f 6475 6c65 5f5f da0c 5f5f 7175 616c  module__..__qual
-00000c50: 6e61 6d65 5f5f 7203 0000 00da 0774 735f  name__r......ts_
-00000c60: 636f 6465 da12 5f5f 696d 706c 656d 656e  code..__implemen
-00000c70: 7461 7469 6f6e 5f5f a900 720a 0000 0072  tation__..r....r
-00000c80: 0a00 0000 fa4a 2f55 7365 7273 2f65 7269  .....J/Users/eri
-00000c90: 632f 5079 5470 6c6f 7432 2f70 7974 706c  c/PyTplot2/pytpl
-00000ca0: 6f74 2f48 544d 4c50 6c6f 7474 6572 2f43  ot/HTMLPlotter/C
-00000cb0: 7573 746f 6d4d 6f64 656c 732f 636f 6c6f  ustomModels/colo
-00000cc0: 7262 6172 7369 6465 7469 746c 652e 7079  rbarsidetitle.py
-00000cd0: 7204 0000 006f 0000 0073 0400 0000 0800  r....o...s......
-00000ce0: 0c01 7204 0000 004e 2906 5a18 626f 6b65  ..r....N).Z.boke
-00000cf0: 682e 6d6f 6465 6c73 2e61 6e6e 6f74 6174  h.models.annotat
-00000d00: 696f 6e73 7202 0000 005a 1362 6f6b 6568  ionsr....Z.bokeh
-00000d10: 2e75 7469 6c2e 636f 6d70 696c 6572 7203  .util.compilerr.
-00000d20: 0000 0072 0800 0000 7204 0000 0072 0a00  ...r....r....r..
-00000d30: 0000 720a 0000 0072 0a00 0000 720b 0000  ..r....r....r...
-00000d40: 00da 083c 6d6f 6475 6c65 3e01 0000 0073  ...<module>....s
-00000d50: 0800 0000 0c05 0c01 0402 1466            ...........f
+00000000: 2320 436f 7079 7269 6768 7420 3230 3138  # Copyright 2018
+00000010: 2052 6567 656e 7473 206f 6620 7468 6520   Regents of the 
+00000020: 556e 6976 6572 7369 7479 206f 6620 436f  University of Co
+00000030: 6c6f 7261 646f 2e20 416c 6c20 5269 6768  lorado. All Righ
+00000040: 7473 2052 6573 6572 7665 642e 0a23 2052  ts Reserved..# R
+00000050: 656c 6561 7365 6420 756e 6465 7220 7468  eleased under th
+00000060: 6520 4d49 5420 6c69 6365 6e73 652e 0a23  e MIT license..#
+00000070: 2054 6869 7320 736f 6674 7761 7265 2077   This software w
+00000080: 6173 2064 6576 656c 6f70 6564 2061 7420  as developed at 
+00000090: 7468 6520 556e 6976 6572 7369 7479 206f  the University o
+000000a0: 6620 436f 6c6f 7261 646f 2773 204c 6162  f Colorado's Lab
+000000b0: 6f72 6174 6f72 7920 666f 7220 4174 6d6f  oratory for Atmo
+000000c0: 7370 6865 7269 6320 616e 6420 5370 6163  spheric and Spac
+000000d0: 6520 5068 7973 6963 732e 0a23 2056 6572  e Physics..# Ver
+000000e0: 6966 7920 6375 7272 656e 7420 7665 7273  ify current vers
+000000f0: 696f 6e20 6265 666f 7265 2075 7365 2061  ion before use a
+00000100: 743a 2068 7474 7073 3a2f 2f67 6974 6875  t: https://githu
+00000110: 622e 636f 6d2f 4d41 5645 4e53 4443 2f50  b.com/MAVENSDC/P
+00000120: 7954 706c 6f74 0a0a 6672 6f6d 2062 6f6b  yTplot..from bok
+00000130: 6568 2e6d 6f64 656c 732e 616e 6e6f 7461  eh.models.annota
+00000140: 7469 6f6e 7320 696d 706f 7274 2043 6f6c  tions import Col
+00000150: 6f72 4261 720a 6672 6f6d 2062 6f6b 6568  orBar.from bokeh
+00000160: 2e75 7469 6c2e 636f 6d70 696c 6572 2069  .util.compiler i
+00000170: 6d70 6f72 7420 5479 7065 5363 7269 7074  mport TypeScript
+00000180: 0a0a 7473 5f63 6f64 6520 3d20 2727 270a  ..ts_code = '''.
+00000190: 696d 706f 7274 207b 436f 6c6f 7242 6172  import {ColorBar
+000001a0: 2c20 436f 6c6f 7242 6172 5669 6577 7d20  , ColorBarView} 
+000001b0: 6672 6f6d 2022 6d6f 6465 6c73 2f61 6e6e  from "models/ann
+000001c0: 6f74 6174 696f 6e73 2f63 6f6c 6f72 5f62  otations/color_b
+000001d0: 6172 220a 696d 706f 7274 202a 2061 7320  ar".import * as 
+000001e0: 7020 6672 6f6d 2022 636f 7265 2f70 726f  p from "core/pro
+000001f0: 7065 7274 6965 7322 0a69 6d70 6f72 7420  perties".import 
+00000200: 7b43 6f6e 7465 7874 3264 7d20 6672 6f6d  {Context2d} from
+00000210: 2022 636f 7265 2f75 7469 6c2f 6361 6e76   "core/util/canv
+00000220: 6173 220a 0a63 6f6e 7374 2053 484f 5254  as"..const SHORT
+00000230: 5f44 494d 203d 2032 350a 0a65 7870 6f72  _DIM = 25..expor
+00000240: 7420 636c 6173 7320 436f 6c6f 7242 6172  t class ColorBar
+00000250: 5369 6465 5469 746c 6556 6965 7720 6578  SideTitleView ex
+00000260: 7465 6e64 7320 436f 6c6f 7242 6172 5669  tends ColorBarVi
+00000270: 6577 207b 0a20 206d 6f64 656c 3a20 436f  ew {.  model: Co
+00000280: 6c6f 7242 6172 5369 6465 5469 746c 650a  lorBarSideTitle.
+00000290: 2020 7072 6f74 6563 7465 6420 696d 6167    protected imag
+000002a0: 653a 2048 544d 4c43 616e 7661 7345 6c65  e: HTMLCanvasEle
+000002b0: 6d65 6e74 0a0a 2020 636f 6d70 7574 655f  ment..  compute_
+000002c0: 6c65 6765 6e64 5f64 696d 656e 7369 6f6e  legend_dimension
+000002d0: 7328 293a 207b 7769 6474 683a 206e 756d  s(): {width: num
+000002e0: 6265 722c 2068 6569 6768 743a 206e 756d  ber, height: num
+000002f0: 6265 727d 207b 0a20 2020 2063 6f6e 7374  ber} {.    const
+00000300: 2069 6d61 6765 5f64 696d 656e 7369 6f6e   image_dimension
+00000310: 7320 3d20 7468 6973 2e5f 636f 6d70 7574  s = this._comput
+00000320: 6564 5f69 6d61 6765 5f64 696d 656e 7369  ed_image_dimensi
+00000330: 6f6e 7328 290a 2020 2020 636f 6e73 7420  ons().    const 
+00000340: 5b69 6d61 6765 5f68 6569 6768 742c 2069  [image_height, i
+00000350: 6d61 6765 5f77 6964 7468 5d20 3d20 5b69  mage_width] = [i
+00000360: 6d61 6765 5f64 696d 656e 7369 6f6e 732e  mage_dimensions.
+00000370: 6865 6967 6874 2c20 696d 6167 655f 6469  height, image_di
+00000380: 6d65 6e73 696f 6e73 2e77 6964 7468 5d0a  mensions.width].
+00000390: 0a20 2020 2063 6f6e 7374 206c 6162 656c  .    const label
+000003a0: 5f65 7874 656e 7420 3d20 7468 6973 2e5f  _extent = this._
+000003b0: 6765 745f 6c61 6265 6c5f 6578 7465 6e74  get_label_extent
+000003c0: 2829 0a20 2020 2063 6f6e 7374 2074 6974  ().    const tit
+000003d0: 6c65 5f65 7874 656e 7420 3d20 7468 6973  le_extent = this
+000003e0: 2e5f 7469 746c 655f 6578 7465 6e74 2829  ._title_extent()
+000003f0: 0a20 2020 2063 6f6e 7374 2074 6963 6b5f  .    const tick_
+00000400: 6578 7465 6e74 203d 2074 6869 732e 5f74  extent = this._t
+00000410: 6963 6b5f 6578 7465 6e74 2829 0a20 2020  ick_extent().   
+00000420: 2063 6f6e 7374 207b 7061 6464 696e 677d   const {padding}
+00000430: 203d 2074 6869 732e 6d6f 6465 6c0a 0a20   = this.model.. 
+00000440: 2020 206c 6574 206c 6567 656e 645f 6865     let legend_he
+00000450: 6967 6874 3a20 6e75 6d62 6572 2c20 6c65  ight: number, le
+00000460: 6765 6e64 5f77 6964 7468 3a20 6e75 6d62  gend_width: numb
+00000470: 6572 0a20 2020 206c 6567 656e 645f 6865  er.    legend_he
+00000480: 6967 6874 203d 2069 6d61 6765 5f68 6569  ight = image_hei
+00000490: 6768 740a 2020 2020 6c65 6765 6e64 5f77  ght.    legend_w
+000004a0: 6964 7468 203d 2069 6d61 6765 5f77 6964  idth = image_wid
+000004b0: 7468 202b 2074 6963 6b5f 6578 7465 6e74  th + tick_extent
+000004c0: 202b 206c 6162 656c 5f65 7874 656e 7420   + label_extent 
+000004d0: 2b20 7469 746c 655f 6578 7465 6e74 202b  + title_extent +
+000004e0: 2032 2a70 6164 6469 6e67 0a0a 2020 2020   2*padding..    
+000004f0: 7265 7475 726e 207b 7769 6474 683a 206c  return {width: l
+00000500: 6567 656e 645f 7769 6474 682c 2068 6569  egend_width, hei
+00000510: 6768 743a 206c 6567 656e 645f 6865 6967  ght: legend_heig
+00000520: 6874 7d0a 2020 7d0a 0a20 2070 726f 7465  ht}.  }..  prote
+00000530: 6374 6564 205f 6472 6177 5f69 6d61 6765  cted _draw_image
+00000540: 2863 7478 3a20 436f 6e74 6578 7432 6429  (ctx: Context2d)
+00000550: 3a20 766f 6964 207b 0a20 2020 2063 6f6e  : void {.    con
+00000560: 7374 2069 6d61 6765 203d 2074 6869 732e  st image = this.
+00000570: 5f63 6f6d 7075 7465 645f 696d 6167 655f  _computed_image_
+00000580: 6469 6d65 6e73 696f 6e73 2829 0a20 2020  dimensions().   
+00000590: 2063 7478 2e73 6176 6528 290a 2020 2020   ctx.save().    
+000005a0: 6374 782e 7365 7449 6d61 6765 536d 6f6f  ctx.setImageSmoo
+000005b0: 7468 696e 6745 6e61 626c 6564 2866 616c  thingEnabled(fal
+000005c0: 7365 290a 2020 2020 6374 782e 676c 6f62  se).    ctx.glob
+000005d0: 616c 416c 7068 6120 3d20 7468 6973 2e6d  alAlpha = this.m
+000005e0: 6f64 656c 2e73 6361 6c65 5f61 6c70 6861  odel.scale_alpha
+000005f0: 0a20 2020 2063 7478 2e64 7261 7749 6d61  .    ctx.drawIma
+00000600: 6765 2874 6869 732e 696d 6167 652c 2030  ge(this.image, 0
+00000610: 2c20 302c 2069 6d61 6765 2e77 6964 7468  , 0, image.width
+00000620: 2c20 696d 6167 652e 6865 6967 6874 290a  , image.height).
+00000630: 2020 2020 6966 2028 7468 6973 2e76 6973      if (this.vis
+00000640: 7561 6c73 2e62 6172 5f6c 696e 652e 646f  uals.bar_line.do
+00000650: 6974 2920 7b0a 2020 2020 2020 7468 6973  it) {.      this
+00000660: 2e76 6973 7561 6c73 2e62 6172 5f6c 696e  .visuals.bar_lin
+00000670: 652e 7365 745f 7661 6c75 6528 6374 7829  e.set_value(ctx)
+00000680: 0a20 2020 2020 2063 7478 2e73 7472 6f6b  .      ctx.strok
+00000690: 6552 6563 7428 302c 2030 2c20 696d 6167  eRect(0, 0, imag
+000006a0: 652e 7769 6474 682c 2069 6d61 6765 2e68  e.width, image.h
+000006b0: 6569 6768 7429 0a20 2020 207d 0a20 2020  eight).    }.   
+000006c0: 2063 7478 2e72 6573 746f 7265 2829 0a20   ctx.restore(). 
+000006d0: 207d 0a0a 2020 7072 6f74 6563 7465 6420   }..  protected 
+000006e0: 5f64 7261 775f 7469 746c 6528 6374 783a  _draw_title(ctx:
+000006f0: 2043 6f6e 7465 7874 3264 293a 2076 6f69   Context2d): voi
+00000700: 6420 7b0a 2020 2020 6966 2028 2174 6869  d {.    if (!thi
+00000710: 732e 7669 7375 616c 732e 7469 746c 655f  s.visuals.title_
+00000720: 7465 7874 2e64 6f69 7429 0a20 2020 2020  text.doit).     
+00000730: 2072 6574 7572 6e0a 2020 2020 636f 6e73   return.    cons
+00000740: 7420 6c61 6265 6c5f 6578 7465 6e74 203d  t label_extent =
+00000750: 2074 6869 732e 5f67 6574 5f6c 6162 656c   this._get_label
+00000760: 5f65 7874 656e 7428 290a 2020 2020 636f  _extent().    co
+00000770: 6e73 7420 7469 636b 5f65 7874 656e 7420  nst tick_extent 
+00000780: 3d20 7468 6973 2e5f 7469 636b 5f65 7874  = this._tick_ext
+00000790: 656e 7428 290a 2020 2020 636f 6e73 7420  ent().    const 
+000007a0: 7b70 6164 6469 6e67 7d20 3d20 7468 6973  {padding} = this
+000007b0: 2e6d 6f64 656c 0a20 2020 2063 7478 2e73  .model.    ctx.s
+000007c0: 6176 6528 290a 2020 2020 7468 6973 2e76  ave().    this.v
+000007d0: 6973 7561 6c73 2e74 6974 6c65 5f74 6578  isuals.title_tex
+000007e0: 742e 7365 745f 7661 6c75 6528 6374 7829  t.set_value(ctx)
+000007f0: 0a20 2020 2063 7478 2e72 6f74 6174 6528  .    ctx.rotate(
+00000800: 2d4d 6174 682e 5049 2f32 290a 2020 2020  -Math.PI/2).    
+00000810: 6374 782e 6669 6c6c 5465 7874 2874 6869  ctx.fillText(thi
+00000820: 732e 6d6f 6465 6c2e 7469 746c 652c 202d  s.model.title, -
+00000830: 7468 6973 2e70 6c6f 745f 7669 6577 2e66  this.plot_view.f
+00000840: 7261 6d65 2e5f 6865 6967 6874 2e76 616c  rame._height.val
+00000850: 7565 202a 2030 2e35 202c 2074 6869 732e  ue * 0.5 , this.
+00000860: 696d 6167 652e 7769 6474 6820 2b20 7469  image.width + ti
+00000870: 636b 5f65 7874 656e 7420 2b20 6c61 6265  ck_extent + labe
+00000880: 6c5f 6578 7465 6e74 202b 2034 2a70 6164  l_extent + 4*pad
+00000890: 6469 6e67 290a 2020 2020 6374 782e 7465  ding).    ctx.te
+000008a0: 7874 416c 6967 6e3d 2263 656e 7465 7222  xtAlign="center"
+000008b0: 0a20 2020 2063 7478 2e72 6573 746f 7265  .    ctx.restore
+000008c0: 2829 0a20 207d 0a0a 2020 2f2a 7072 6f74  ().  }..  /*prot
+000008d0: 6563 7465 642a 2f20 5f67 6574 5f69 6d61  ected*/ _get_ima
+000008e0: 6765 5f6f 6666 7365 7428 293a 207b 783a  ge_offset(): {x:
+000008f0: 206e 756d 6265 722c 2079 3a20 6e75 6d62   number, y: numb
+00000900: 6572 7d20 7b0a 2020 2020 2f2f 2052 6574  er} {.    // Ret
+00000910: 7572 6e73 2069 6d61 6765 206f 6666 7365  urns image offse
+00000920: 7420 7265 6c61 7469 7665 2074 6f20 6c65  t relative to le
+00000930: 6765 6e64 2062 6f75 6e64 696e 6720 626f  gend bounding bo
+00000940: 780a 2020 2020 636f 6e73 7420 7820 3d20  x.    const x = 
+00000950: 7468 6973 2e6d 6f64 656c 2e70 6164 6469  this.model.paddi
+00000960: 6e67 0a20 2020 2063 6f6e 7374 2079 203d  ng.    const y =
+00000970: 2030 0a20 2020 2072 6574 7572 6e20 7b78   0.    return {x
+00000980: 2c20 797d 0a20 207d 0a0a 2020 5f63 6f6d  , y}.  }..  _com
+00000990: 7075 7465 645f 696d 6167 655f 6469 6d65  puted_image_dime
+000009a0: 6e73 696f 6e73 2829 3a20 7b68 6569 6768  nsions(): {heigh
+000009b0: 743a 206e 756d 6265 722c 2077 6964 7468  t: number, width
+000009c0: 3a20 6e75 6d62 6572 7d20 7b0a 2020 2020  : number} {.    
+000009d0: 636f 6e73 7420 6672 616d 655f 6865 6967  const frame_heig
+000009e0: 6874 203d 2074 6869 732e 706c 6f74 5f76  ht = this.plot_v
+000009f0: 6965 772e 6672 616d 652e 5f68 6569 6768  iew.frame._heigh
+00000a00: 742e 7661 6c75 650a 2020 2020 6c65 7420  t.value.    let 
+00000a10: 6865 6967 6874 3a20 6e75 6d62 6572 2c20  height: number, 
+00000a20: 7769 6474 683a 206e 756d 6265 720a 2020  width: number.  
+00000a30: 2020 6966 2028 7468 6973 2e6d 6f64 656c    if (this.model
+00000a40: 2e68 6569 6768 7420 3d3d 2027 6175 746f  .height == 'auto
+00000a50: 2729 207b 0a20 2020 2020 2020 2068 6569  ') {.        hei
+00000a60: 6768 7420 3d20 6672 616d 655f 6865 6967  ght = frame_heig
+00000a70: 6874 0a20 2020 207d 2065 6c73 650a 2020  ht.    } else.  
+00000a80: 2020 6865 6967 6874 203d 2074 6869 732e    height = this.
+00000a90: 6d6f 6465 6c2e 6865 6967 6874 0a0a 2020  model.height..  
+00000aa0: 2020 7769 6474 6820 3d20 7468 6973 2e6d    width = this.m
+00000ab0: 6f64 656c 2e77 6964 7468 203d 3d20 2761  odel.width == 'a
+00000ac0: 7574 6f27 203f 2053 484f 5254 5f44 494d  uto' ? SHORT_DIM
+00000ad0: 203a 2074 6869 732e 6d6f 6465 6c2e 7769   : this.model.wi
+00000ae0: 6474 680a 0a20 2020 2072 6574 7572 6e20  dth..    return 
+00000af0: 7b77 6964 7468 2c20 6865 6967 6874 7d0a  {width, height}.
+00000b00: 2020 7d0a 0a20 202f 2f20 7d7d 7d0a 7d0a    }..  // }}}.}.
+00000b10: 0a65 7870 6f72 7420 6e61 6d65 7370 6163  .export namespac
+00000b20: 6520 436f 6c6f 7242 6172 5369 6465 5469  e ColorBarSideTi
+00000b30: 746c 6520 7b0a 2020 6578 706f 7274 2074  tle {.  export t
+00000b40: 7970 6520 4174 7472 7320 3d20 702e 4174  ype Attrs = p.At
+00000b50: 7472 734f 663c 5072 6f70 733e 0a0a 2020  trsOf<Props>..  
+00000b60: 6578 706f 7274 2074 7970 6520 5072 6f70  export type Prop
+00000b70: 7320 3d20 436f 6c6f 7242 6172 2e50 726f  s = ColorBar.Pro
+00000b80: 7073 0a7d 0a0a 6578 706f 7274 2069 6e74  ps.}..export int
+00000b90: 6572 6661 6365 2043 6f6c 6f72 4261 7253  erface ColorBarS
+00000ba0: 6964 6554 6974 6c65 2065 7874 656e 6473  ideTitle extends
+00000bb0: 2043 6f6c 6f72 4261 7253 6964 6554 6974   ColorBarSideTit
+00000bc0: 6c65 2e41 7474 7273 207b 7d0a 0a65 7870  le.Attrs {}..exp
+00000bd0: 6f72 7420 636c 6173 7320 436f 6c6f 7242  ort class ColorB
+00000be0: 6172 5369 6465 5469 746c 6520 6578 7465  arSideTitle exte
+00000bf0: 6e64 7320 436f 6c6f 7242 6172 207b 0a20  nds ColorBar {. 
+00000c00: 2070 726f 7065 7274 6965 733a 2043 6f6c   properties: Col
+00000c10: 6f72 4261 7253 6964 6554 6974 6c65 2e50  orBarSideTitle.P
+00000c20: 726f 7073 0a20 200a 2020 636f 6e73 7472  rops.  .  constr
+00000c30: 7563 746f 7228 6174 7472 733f 3a20 5061  uctor(attrs?: Pa
+00000c40: 7274 6961 6c3c 436f 6c6f 7242 6172 5369  rtial<ColorBarSi
+00000c50: 6465 5469 746c 652e 4174 7472 733e 2920  deTitle.Attrs>) 
+00000c60: 7b0a 2020 2020 7375 7065 7228 6174 7472  {.    super(attr
+00000c70: 7329 0a20 207d 0a0a 2020 7374 6174 6963  s).  }..  static
+00000c80: 2069 6e69 7443 6c61 7373 2829 3a20 766f   initClass(): vo
+00000c90: 6964 207b 0a20 2020 2074 6869 732e 7072  id {.    this.pr
+00000ca0: 6f74 6f74 7970 652e 6465 6661 756c 745f  ototype.default_
+00000cb0: 7669 6577 203d 2043 6f6c 6f72 4261 7253  view = ColorBarS
+00000cc0: 6964 6554 6974 6c65 5669 6577 0a20 207d  ideTitleView.  }
+00000cd0: 0a7d 0a0a 436f 6c6f 7242 6172 5369 6465  .}..ColorBarSide
+00000ce0: 5469 746c 652e 696e 6974 436c 6173 7328  Title.initClass(
+00000cf0: 290a 0a27 2727 0a0a 0a63 6c61 7373 2043  )..'''...class C
+00000d00: 6f6c 6f72 4261 7253 6964 6554 6974 6c65  olorBarSideTitle
+00000d10: 2843 6f6c 6f72 4261 7229 3a0a 2020 2020  (ColorBar):.    
+00000d20: 5f5f 696d 706c 656d 656e 7461 7469 6f6e  __implementation
+00000d30: 5f5f 203d 2054 7970 6553 6372 6970 7428  __ = TypeScript(
+00000d40: 7473 5f63 6f64 6529                      ts_code)
```

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/HTMLPlotter/CustomModels/__pycache__/timestamp.cpython-310.pyc` & `pytplot-mpl-temp-2.1.9/pytplot/HTMLPlotter/CustomModels/timestamp.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,119 +1,118 @@
-00000000: 6f0d 0d0a 0000 0000 70bb 6263 5307 0000  o.......p.bcS...
-00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
-00000020: 0004 0000 0040 0000 0073 3c00 0000 6400  .....@...s<...d.
-00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
-00000040: 6d03 5a03 0100 6400 6403 6c04 6d05 5a05  m.Z...d.d.l.m.Z.
-00000050: 0100 6404 5a06 4700 6405 6406 8400 6406  ..d.Z.G.d.d...d.
-00000060: 6503 8303 5a07 6407 5300 2908 e900 0000  e...Z.d.S.).....
-00000070: 0029 01da 0653 7472 696e 6729 01da 094c  .)...String)...L
-00000080: 6179 6f75 7444 4f4d 2901 da0a 5479 7065  ayoutDOM)...Type
-00000090: 5363 7269 7074 612f 0500 000a 696d 706f  Scripta/....impo
-000000a0: 7274 202a 2061 7320 7020 6672 6f6d 2022  rt * as p from "
-000000b0: 636f 7265 2f70 726f 7065 7274 6965 7322  core/properties"
-000000c0: 0a69 6d70 6f72 7420 7b64 6976 2c20 656d  .import {div, em
-000000d0: 7074 797d 2066 726f 6d20 2263 6f72 652f  pty} from "core/
-000000e0: 646f 6d22 0a69 6d70 6f72 7420 7b4c 6179  dom".import {Lay
-000000f0: 6f75 7444 4f4d 2c20 4c61 796f 7574 444f  outDOM, LayoutDO
-00000100: 4d56 6965 777d 2066 726f 6d20 226d 6f64  MView} from "mod
-00000110: 656c 732f 6c61 796f 7574 732f 6c61 796f  els/layouts/layo
-00000120: 7574 5f64 6f6d 220a 696d 706f 7274 207b  ut_dom".import {
-00000130: 4c61 796f 7574 4974 656d 7d20 6672 6f6d  LayoutItem} from
-00000140: 2022 636f 7265 2f6c 6179 6f75 7422 0a0a   "core/layout"..
-00000150: 6578 706f 7274 2063 6c61 7373 2054 696d  export class Tim
-00000160: 6553 7461 6d70 5669 6577 2065 7874 656e  eStampView exten
-00000170: 6473 204c 6179 6f75 7444 4f4d 5669 6577  ds LayoutDOMView
-00000180: 207b 0a20 2020 206d 6f64 656c 3a20 5469   {.    model: Ti
-00000190: 6d65 5374 616d 700a 2020 2020 0a20 2020  meStamp.    .   
-000001a0: 2069 6e69 7469 616c 697a 6528 293a 2076   initialize(): v
-000001b0: 6f69 6420 7b0a 2020 2020 2020 2020 7375  oid {.        su
-000001c0: 7065 722e 696e 6974 6961 6c69 7a65 2829  per.initialize()
-000001d0: 0a20 2020 207d 0a20 2020 2072 656e 6465  .    }.    rende
-000001e0: 7228 293a 2076 6f69 6420 7b0a 2020 2020  r(): void {.    
-000001f0: 2020 2020 656d 7074 7928 7468 6973 2e65      empty(this.e
-00000200: 6c29 0a20 2020 2020 2020 2074 6869 732e  l).        this.
-00000210: 656c 2e61 7070 656e 6443 6869 6c64 2864  el.appendChild(d
-00000220: 6976 287b 0a20 2020 2020 2020 2020 2073  iv({.          s
-00000230: 7479 6c65 3a20 7b0a 2020 2020 2020 2020  tyle: {.        
-00000240: 2020 2020 2777 6964 7468 273a 2027 3830      'width': '80
-00000250: 3070 7827 2c0a 2020 2020 2020 2020 2020  0px',.          
-00000260: 2020 2777 6f72 642d 7370 6163 696e 6727    'word-spacing'
-00000270: 3a20 2731 3070 7827 2c0a 2020 2020 2020  : '10px',.      
-00000280: 2020 2020 2020 2766 6f6e 742d 7369 7a65        'font-size
-00000290: 273a 2027 3131 7078 272c 0a20 2020 2020  ': '11px',.     
-000002a0: 2020 2020 2020 2027 636f 6c6f 7227 3a20         'color': 
-000002b0: 2723 3030 3030 3030 272c 0a20 2020 2020  '#000000',.     
-000002c0: 2020 2020 2020 2027 6261 636b 6772 6f75         'backgrou
-000002d0: 6e64 2d63 6f6c 6f72 273a 2027 2366 6666  nd-color': '#fff
-000002e0: 6666 6627 2c0a 2020 2020 2020 2020 2020  fff',.          
-000002f0: 2020 7d2c 0a20 2020 2020 2020 207d 2c20    },.        }, 
-00000300: 6024 7b74 6869 732e 6d6f 6465 6c2e 7465  `${this.model.te
-00000310: 7874 7d60 2929 0a20 2020 207d 0a20 2020  xt}`)).    }.   
-00000320: 200a 2020 2020 5f75 7064 6174 655f 6c61   .    _update_la
-00000330: 796f 7574 2829 3a20 766f 6964 207b 0a20  yout(): void {. 
-00000340: 2020 2020 2020 2074 6869 732e 6c61 796f         this.layo
-00000350: 7574 203d 206e 6577 204c 6179 6f75 7449  ut = new LayoutI
-00000360: 7465 6d28 290a 2020 2020 2020 2020 7468  tem().        th
-00000370: 6973 2e6c 6179 6f75 742e 7365 745f 7369  is.layout.set_si
-00000380: 7a69 6e67 2874 6869 732e 626f 785f 7369  zing(this.box_si
-00000390: 7a69 6e67 2829 290a 2020 2020 7d0a 2020  zing()).    }.  
-000003a0: 2020 0a20 2020 2067 6574 2063 6869 6c64    .    get child
-000003b0: 5f6d 6f64 656c 7328 293a 204c 6179 6f75  _models(): Layou
-000003c0: 7444 4f4d 5b5d 207b 0a20 2020 2020 2020  tDOM[] {.       
-000003d0: 2072 6574 7572 6e20 5b5d 0a20 2020 2020   return [].     
-000003e0: 207d 0a7d 0a0a 0a65 7870 6f72 7420 6e61   }.}...export na
-000003f0: 6d65 7370 6163 6520 5469 6d65 5374 616d  mespace TimeStam
-00000400: 7020 7b0a 2020 6578 706f 7274 2074 7970  p {.  export typ
-00000410: 6520 4174 7472 7320 3d20 702e 4174 7472  e Attrs = p.Attr
-00000420: 734f 663c 5072 6f70 733e 0a0a 2020 6578  sOf<Props>..  ex
-00000430: 706f 7274 2074 7970 6520 5072 6f70 7320  port type Props 
-00000440: 3d20 4c61 796f 7574 444f 4d2e 5072 6f70  = LayoutDOM.Prop
-00000450: 7320 2620 7b0a 2020 2020 7465 7874 3a20  s & {.    text: 
-00000460: 702e 5072 6f70 6572 7479 3c73 7472 696e  p.Property<strin
-00000470: 673e 0a20 207d 0a7d 0a0a 6578 706f 7274  g>.  }.}..export
-00000480: 2069 6e74 6572 6661 6365 2054 696d 6553   interface TimeS
-00000490: 7461 6d70 2065 7874 656e 6473 2054 696d  tamp extends Tim
-000004a0: 6553 7461 6d70 2e41 7474 7273 207b 7d0a  eStamp.Attrs {}.
-000004b0: 0a65 7870 6f72 7420 636c 6173 7320 5469  .export class Ti
-000004c0: 6d65 5374 616d 7020 6578 7465 6e64 7320  meStamp extends 
-000004d0: 4c61 796f 7574 444f 4d20 7b0a 2020 2020  LayoutDOM {.    
-000004e0: 7072 6f70 6572 7469 6573 3a20 5469 6d65  properties: Time
-000004f0: 5374 616d 702e 5072 6f70 730a 2020 2020  Stamp.Props.    
-00000500: 7374 6174 6963 2069 6e69 7443 6c61 7373  static initClass
-00000510: 2829 3a20 766f 6964 207b 0a20 2020 200a  (): void {.    .
-00000520: 2020 2020 2020 2020 7468 6973 2e70 726f          this.pro
-00000530: 746f 7479 7065 2e64 6566 6175 6c74 5f76  totype.default_v
-00000540: 6965 7720 3d20 5469 6d65 5374 616d 7056  iew = TimeStampV
-00000550: 6965 770a 2020 2020 0a20 2020 2020 2020  iew.    .       
-00000560: 2074 6869 732e 6465 6669 6e65 3c54 696d   this.define<Tim
-00000570: 6553 7461 6d70 2e50 726f 7073 3e28 7b0a  eStamp.Props>({.
-00000580: 2020 2020 2020 2020 2020 2020 7465 7874              text
-00000590: 3a20 5b20 702e 5374 7269 6e67 205d 0a20  : [ p.String ]. 
-000005a0: 2020 2020 2020 207d 290a 2020 2020 7d0a         }).    }.
-000005b0: 7d0a 0a54 696d 6553 7461 6d70 2e69 6e69  }..TimeStamp.ini
-000005c0: 7443 6c61 7373 2829 0a0a 6300 0000 0000  tClass()..c.....
-000005d0: 0000 0000 0000 0000 0000 0003 0000 0040  ...............@
-000005e0: 0000 0073 1e00 0000 6500 5a01 6400 5a02  ...s....e.Z.d.Z.
-000005f0: 6503 6504 8301 5a05 6506 6401 6402 8d01  e.e...Z.e.d.d...
-00000600: 5a07 6403 5300 2904 da09 5469 6d65 5374  Z.d.S.)...TimeSt
-00000610: 616d 705a 0754 6573 7469 6e67 2901 da07  ampZ.Testing)...
-00000620: 6465 6661 756c 744e 2908 da08 5f5f 6e61  defaultN)...__na
-00000630: 6d65 5f5f da0a 5f5f 6d6f 6475 6c65 5f5f  me__..__module__
-00000640: da0c 5f5f 7175 616c 6e61 6d65 5f5f 7204  ..__qualname__r.
-00000650: 0000 00da 074a 535f 434f 4445 da12 5f5f  .....JS_CODE..__
-00000660: 696d 706c 656d 656e 7461 7469 6f6e 5f5f  implementation__
-00000670: 7202 0000 00da 0474 6578 74a9 0072 0d00  r......text..r..
-00000680: 0000 720d 0000 00fa 422f 5573 6572 732f  ..r.....B/Users/
-00000690: 6572 6963 2f50 7954 706c 6f74 322f 7079  eric/PyTplot2/py
-000006a0: 7470 6c6f 742f 4854 4d4c 506c 6f74 7465  tplot/HTMLPlotte
-000006b0: 722f 4375 7374 6f6d 4d6f 6465 6c73 2f74  r/CustomModels/t
-000006c0: 696d 6573 7461 6d70 2e70 7972 0500 0000  imestamp.pyr....
-000006d0: 4900 0000 7306 0000 0008 0008 010e 0172  I...s..........r
-000006e0: 0500 0000 4e29 085a 1562 6f6b 6568 2e63  ....N).Z.bokeh.c
-000006f0: 6f72 652e 7072 6f70 6572 7469 6573 7202  ore.propertiesr.
-00000700: 0000 00da 0c62 6f6b 6568 2e6d 6f64 656c  .....bokeh.model
-00000710: 7372 0300 0000 5a13 626f 6b65 682e 7574  sr....Z.bokeh.ut
-00000720: 696c 2e63 6f6d 7069 6c65 7272 0400 0000  il.compilerr....
-00000730: 720a 0000 0072 0500 0000 720d 0000 0072  r....r....r....r
-00000740: 0d00 0000 720d 0000 0072 0e00 0000 da08  ....r....r......
-00000750: 3c6d 6f64 756c 653e 0100 0000 730a 0000  <module>....s...
-00000760: 000c 050c 010c 0104 0214 3f              ..........?
+00000000: 2320 436f 7079 7269 6768 7420 3230 3138  # Copyright 2018
+00000010: 2052 6567 656e 7473 206f 6620 7468 6520   Regents of the 
+00000020: 556e 6976 6572 7369 7479 206f 6620 436f  University of Co
+00000030: 6c6f 7261 646f 2e20 416c 6c20 5269 6768  lorado. All Righ
+00000040: 7473 2052 6573 6572 7665 642e 0a23 2052  ts Reserved..# R
+00000050: 656c 6561 7365 6420 756e 6465 7220 7468  eleased under th
+00000060: 6520 4d49 5420 6c69 6365 6e73 652e 0a23  e MIT license..#
+00000070: 2054 6869 7320 736f 6674 7761 7265 2077   This software w
+00000080: 6173 2064 6576 656c 6f70 6564 2061 7420  as developed at 
+00000090: 7468 6520 556e 6976 6572 7369 7479 206f  the University o
+000000a0: 6620 436f 6c6f 7261 646f 2773 204c 6162  f Colorado's Lab
+000000b0: 6f72 6174 6f72 7920 666f 7220 4174 6d6f  oratory for Atmo
+000000c0: 7370 6865 7269 6320 616e 6420 5370 6163  spheric and Spac
+000000d0: 6520 5068 7973 6963 732e 0a23 2056 6572  e Physics..# Ver
+000000e0: 6966 7920 6375 7272 656e 7420 7665 7273  ify current vers
+000000f0: 696f 6e20 6265 666f 7265 2075 7365 2061  ion before use a
+00000100: 743a 2068 7474 7073 3a2f 2f67 6974 6875  t: https://githu
+00000110: 622e 636f 6d2f 4d41 5645 4e53 4443 2f50  b.com/MAVENSDC/P
+00000120: 7954 706c 6f74 0a0a 6672 6f6d 2062 6f6b  yTplot..from bok
+00000130: 6568 2e63 6f72 652e 7072 6f70 6572 7469  eh.core.properti
+00000140: 6573 2069 6d70 6f72 7420 5374 7269 6e67  es import String
+00000150: 0a66 726f 6d20 626f 6b65 682e 6d6f 6465  .from bokeh.mode
+00000160: 6c73 2069 6d70 6f72 7420 4c61 796f 7574  ls import Layout
+00000170: 444f 4d0a 6672 6f6d 2062 6f6b 6568 2e75  DOM.from bokeh.u
+00000180: 7469 6c2e 636f 6d70 696c 6572 2069 6d70  til.compiler imp
+00000190: 6f72 7420 5479 7065 5363 7269 7074 0a0a  ort TypeScript..
+000001a0: 4a53 5f43 4f44 4520 3d20 2727 270a 696d  JS_CODE = '''.im
+000001b0: 706f 7274 202a 2061 7320 7020 6672 6f6d  port * as p from
+000001c0: 2022 636f 7265 2f70 726f 7065 7274 6965   "core/propertie
+000001d0: 7322 0a69 6d70 6f72 7420 7b64 6976 2c20  s".import {div, 
+000001e0: 656d 7074 797d 2066 726f 6d20 2263 6f72  empty} from "cor
+000001f0: 652f 646f 6d22 0a69 6d70 6f72 7420 7b4c  e/dom".import {L
+00000200: 6179 6f75 7444 4f4d 2c20 4c61 796f 7574  ayoutDOM, Layout
+00000210: 444f 4d56 6965 777d 2066 726f 6d20 226d  DOMView} from "m
+00000220: 6f64 656c 732f 6c61 796f 7574 732f 6c61  odels/layouts/la
+00000230: 796f 7574 5f64 6f6d 220a 696d 706f 7274  yout_dom".import
+00000240: 207b 4c61 796f 7574 4974 656d 7d20 6672   {LayoutItem} fr
+00000250: 6f6d 2022 636f 7265 2f6c 6179 6f75 7422  om "core/layout"
+00000260: 0a0a 6578 706f 7274 2063 6c61 7373 2054  ..export class T
+00000270: 696d 6553 7461 6d70 5669 6577 2065 7874  imeStampView ext
+00000280: 656e 6473 204c 6179 6f75 7444 4f4d 5669  ends LayoutDOMVi
+00000290: 6577 207b 0a20 2020 206d 6f64 656c 3a20  ew {.    model: 
+000002a0: 5469 6d65 5374 616d 700a 2020 2020 0a20  TimeStamp.    . 
+000002b0: 2020 2069 6e69 7469 616c 697a 6528 293a     initialize():
+000002c0: 2076 6f69 6420 7b0a 2020 2020 2020 2020   void {.        
+000002d0: 7375 7065 722e 696e 6974 6961 6c69 7a65  super.initialize
+000002e0: 2829 0a20 2020 207d 0a20 2020 2072 656e  ().    }.    ren
+000002f0: 6465 7228 293a 2076 6f69 6420 7b0a 2020  der(): void {.  
+00000300: 2020 2020 2020 656d 7074 7928 7468 6973        empty(this
+00000310: 2e65 6c29 0a20 2020 2020 2020 2074 6869  .el).        thi
+00000320: 732e 656c 2e61 7070 656e 6443 6869 6c64  s.el.appendChild
+00000330: 2864 6976 287b 0a20 2020 2020 2020 2020  (div({.         
+00000340: 2073 7479 6c65 3a20 7b0a 2020 2020 2020   style: {.      
+00000350: 2020 2020 2020 2777 6964 7468 273a 2027        'width': '
+00000360: 3830 3070 7827 2c0a 2020 2020 2020 2020  800px',.        
+00000370: 2020 2020 2777 6f72 642d 7370 6163 696e      'word-spacin
+00000380: 6727 3a20 2731 3070 7827 2c0a 2020 2020  g': '10px',.    
+00000390: 2020 2020 2020 2020 2766 6f6e 742d 7369          'font-si
+000003a0: 7a65 273a 2027 3131 7078 272c 0a20 2020  ze': '11px',.   
+000003b0: 2020 2020 2020 2020 2027 636f 6c6f 7227           'color'
+000003c0: 3a20 2723 3030 3030 3030 272c 0a20 2020  : '#000000',.   
+000003d0: 2020 2020 2020 2020 2027 6261 636b 6772           'backgr
+000003e0: 6f75 6e64 2d63 6f6c 6f72 273a 2027 2366  ound-color': '#f
+000003f0: 6666 6666 6627 2c0a 2020 2020 2020 2020  fffff',.        
+00000400: 2020 2020 7d2c 0a20 2020 2020 2020 207d      },.        }
+00000410: 2c20 6024 7b74 6869 732e 6d6f 6465 6c2e  , `${this.model.
+00000420: 7465 7874 7d60 2929 0a20 2020 207d 0a20  text}`)).    }. 
+00000430: 2020 200a 2020 2020 5f75 7064 6174 655f     .    _update_
+00000440: 6c61 796f 7574 2829 3a20 766f 6964 207b  layout(): void {
+00000450: 0a20 2020 2020 2020 2074 6869 732e 6c61  .        this.la
+00000460: 796f 7574 203d 206e 6577 204c 6179 6f75  yout = new Layou
+00000470: 7449 7465 6d28 290a 2020 2020 2020 2020  tItem().        
+00000480: 7468 6973 2e6c 6179 6f75 742e 7365 745f  this.layout.set_
+00000490: 7369 7a69 6e67 2874 6869 732e 626f 785f  sizing(this.box_
+000004a0: 7369 7a69 6e67 2829 290a 2020 2020 7d0a  sizing()).    }.
+000004b0: 2020 2020 0a20 2020 2067 6574 2063 6869      .    get chi
+000004c0: 6c64 5f6d 6f64 656c 7328 293a 204c 6179  ld_models(): Lay
+000004d0: 6f75 7444 4f4d 5b5d 207b 0a20 2020 2020  outDOM[] {.     
+000004e0: 2020 2072 6574 7572 6e20 5b5d 0a20 2020     return [].   
+000004f0: 2020 207d 0a7d 0a0a 0a65 7870 6f72 7420     }.}...export 
+00000500: 6e61 6d65 7370 6163 6520 5469 6d65 5374  namespace TimeSt
+00000510: 616d 7020 7b0a 2020 6578 706f 7274 2074  amp {.  export t
+00000520: 7970 6520 4174 7472 7320 3d20 702e 4174  ype Attrs = p.At
+00000530: 7472 734f 663c 5072 6f70 733e 0a0a 2020  trsOf<Props>..  
+00000540: 6578 706f 7274 2074 7970 6520 5072 6f70  export type Prop
+00000550: 7320 3d20 4c61 796f 7574 444f 4d2e 5072  s = LayoutDOM.Pr
+00000560: 6f70 7320 2620 7b0a 2020 2020 7465 7874  ops & {.    text
+00000570: 3a20 702e 5072 6f70 6572 7479 3c73 7472  : p.Property<str
+00000580: 696e 673e 0a20 207d 0a7d 0a0a 6578 706f  ing>.  }.}..expo
+00000590: 7274 2069 6e74 6572 6661 6365 2054 696d  rt interface Tim
+000005a0: 6553 7461 6d70 2065 7874 656e 6473 2054  eStamp extends T
+000005b0: 696d 6553 7461 6d70 2e41 7474 7273 207b  imeStamp.Attrs {
+000005c0: 7d0a 0a65 7870 6f72 7420 636c 6173 7320  }..export class 
+000005d0: 5469 6d65 5374 616d 7020 6578 7465 6e64  TimeStamp extend
+000005e0: 7320 4c61 796f 7574 444f 4d20 7b0a 2020  s LayoutDOM {.  
+000005f0: 2020 7072 6f70 6572 7469 6573 3a20 5469    properties: Ti
+00000600: 6d65 5374 616d 702e 5072 6f70 730a 2020  meStamp.Props.  
+00000610: 2020 7374 6174 6963 2069 6e69 7443 6c61    static initCla
+00000620: 7373 2829 3a20 766f 6964 207b 0a20 2020  ss(): void {.   
+00000630: 200a 2020 2020 2020 2020 7468 6973 2e70   .        this.p
+00000640: 726f 746f 7479 7065 2e64 6566 6175 6c74  rototype.default
+00000650: 5f76 6965 7720 3d20 5469 6d65 5374 616d  _view = TimeStam
+00000660: 7056 6965 770a 2020 2020 0a20 2020 2020  pView.    .     
+00000670: 2020 2074 6869 732e 6465 6669 6e65 3c54     this.define<T
+00000680: 696d 6553 7461 6d70 2e50 726f 7073 3e28  imeStamp.Props>(
+00000690: 7b0a 2020 2020 2020 2020 2020 2020 7465  {.            te
+000006a0: 7874 3a20 5b20 702e 5374 7269 6e67 205d  xt: [ p.String ]
+000006b0: 0a20 2020 2020 2020 207d 290a 2020 2020  .        }).    
+000006c0: 7d0a 7d0a 0a54 696d 6553 7461 6d70 2e69  }.}..TimeStamp.i
+000006d0: 6e69 7443 6c61 7373 2829 0a0a 2727 270a  nitClass()..'''.
+000006e0: 0a0a 636c 6173 7320 5469 6d65 5374 616d  ..class TimeStam
+000006f0: 7028 4c61 796f 7574 444f 4d29 3a0a 2020  p(LayoutDOM):.  
+00000700: 2020 5f5f 696d 706c 656d 656e 7461 7469    __implementati
+00000710: 6f6e 5f5f 203d 2054 7970 6553 6372 6970  on__ = TypeScrip
+00000720: 7428 4a53 5f43 4f44 4529 0a20 2020 2074  t(JS_CODE).    t
+00000730: 6578 7420 3d20 5374 7269 6e67 2864 6566  ext = String(def
+00000740: 6175 6c74 203d 2022 5465 7374 696e 6722  ault = "Testing"
+00000750: 290a 0a                                  )..
```

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/HTMLPlotter/TVarFigure1D.py` & `pytplot-mpl-temp-2.1.9/pytplot/HTMLPlotter/TVarFigure1D.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/HTMLPlotter/TVarFigureAlt.py` & `pytplot-mpl-temp-2.1.9/pytplot/HTMLPlotter/TVarFigureAlt.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/HTMLPlotter/TVarFigureMap.py` & `pytplot-mpl-temp-2.1.9/pytplot/HTMLPlotter/TVarFigureMap.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/HTMLPlotter/TVarFigureSpec.py` & `pytplot-mpl-temp-2.1.9/pytplot/HTMLPlotter/TVarFigureSpec.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/HTMLPlotter/generate.py` & `pytplot-mpl-temp-2.1.9/pytplot/HTMLPlotter/generate.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/MPLPlotter/lineplot.py` & `pytplot-mpl-temp-2.1.9/pytplot/MPLPlotter/lineplot.py`

 * *Files 9% similar despite different names*

```diff
@@ -71,20 +71,20 @@
             colors = [plot_extras['line_color'][pseudo_plot_num]]
 
         # check the color size vs. the size of the data
         # colors should already be an array at this point
         colors = np.array(colors)
         if len(colors.shape) == 1:
             if len(colors) != num_lines:
-                print('Problem with the number of line colors specified')
+                print('Incorrect number of line colors specified; expected: ' + str(num_lines) + '; got: ' + str(len(colors)))
                 return
         else:
             # time varying symbol colors, not supported yet
             if colors.shape[1] != num_lines:
-                print('Problem with the number of line colors specified')
+                print('Incorrect number of line colors specified; expected: ' + str(num_lines) + '; got: ' + str(colors.shape[1]))
                 return
     else:
         if style is None:
             if num_lines == 3:
                 colors = ['b', 'g', 'r']
             elif num_lines == 4:
                 colors = ['b', 'g', 'r', 'k']
```

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/MPLPlotter/specplot.py` & `pytplot-mpl-temp-2.1.9/pytplot/MPLPlotter/specplot.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/MPLPlotter/tplot.py` & `pytplot-mpl-temp-2.1.9/pytplot/MPLPlotter/tplot.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/CustomAxis/AxisItem.py` & `pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/CustomAxis/AxisItem.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/CustomAxis/BlankAxis.py` & `pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/CustomAxis/BlankAxis.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/CustomAxis/DateAxis.py` & `pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/CustomAxis/DateAxis.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/CustomAxis/NonLinearAxis.py` & `pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/CustomAxis/NonLinearAxis.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/CustomImage/ColorbarImage.py` & `pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/CustomImage/ColorbarImage.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/CustomImage/UpdatingImage.py` & `pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/CustomImage/UpdatingImage.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/CustomLegend/CustomLegend.py` & `pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/CustomLegend/CustomLegend.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/CustomLinearRegionItem/CustomLinearRegionItem.py` & `pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/CustomLinearRegionItem/CustomLinearRegionItem.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/PyTPlot_Exporter.py` & `pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/PyTPlot_Exporter.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/TVarFigure1D.py` & `pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/TVarFigure1D.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/TVarFigureAlt.py` & `pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/TVarFigureAlt.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/TVarFigureAxisOnly.py` & `pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/TVarFigureAxisOnly.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/TVarFigureMap.py` & `pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/TVarFigureMap.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/TVarFigureSpec.py` & `pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/TVarFigureSpec.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/__init__.py` & `pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/__init__.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/QtPlotter/generate.py` & `pytplot-mpl-temp-2.1.9/pytplot/QtPlotter/generate.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/__init__.py` & `pytplot-mpl-temp-2.1.9/pytplot/__init__.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/del_data.py` & `pytplot-mpl-temp-2.1.9/pytplot/del_data.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/exporters/tplot_ascii.py` & `pytplot-mpl-temp-2.1.9/pytplot/exporters/tplot_ascii.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/exporters/tplot_save.py` & `pytplot-mpl-temp-2.1.9/pytplot/exporters/tplot_save.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/get_data.py` & `pytplot-mpl-temp-2.1.9/pytplot/get_data.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/get_timespan.py` & `pytplot-mpl-temp-2.1.9/pytplot/get_timespan.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/get_ylimits.py` & `pytplot-mpl-temp-2.1.9/pytplot/get_ylimits.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/importers/cdf_to_tplot.py` & `pytplot-mpl-temp-2.1.9/pytplot/importers/cdf_to_tplot.py`

 * *Files 1% similar despite different names*

```diff
@@ -426,31 +426,31 @@
         except ValueError:
             continue
 
         if var_name not in stored_variables:
             stored_variables.append(var_name)
 
         if metadata.get(var_name) is not None:
-            if metadata[var_name]['display_type'] == "spectrogram":
+            if metadata[var_name]['display_type'].lower() == "spectrogram":
                 options(var_name, 'spec', 1)
             if metadata[var_name]['scale_type'] == 'log':
-                if metadata[var_name]['display_type'] == "spectrogram":
+                if metadata[var_name]['display_type'].lower() == "spectrogram":
                     options(var_name, 'zlog', 1)
                 else:
                     options(var_name, 'ylog', 1)
             if metadata[var_name].get('y_spec_scale_type') is not None:
                 if metadata[var_name]['y_spec_scale_type'] == 'log':
                     options(var_name, 'ylog', 1)
             if metadata[var_name].get('y_spec_units') is not None:
                 options(var_name, 'ysubtitle', '[' + metadata[var_name].get('y_spec_units') + ']')
             if metadata[var_name].get('var_attrs') is not None:
                 if metadata[var_name]['var_attrs'].get('LABLAXIS') is not None:
                     options(var_name, 'ytitle', metadata[var_name]['var_attrs']['LABLAXIS'])
                 if metadata[var_name]['var_attrs'].get('UNITS') is not None:
-                    if metadata[var_name]['display_type'] == 'spectrogram':
+                    if metadata[var_name]['display_type'].lower() == 'spectrogram':
                         options(var_name, 'ztitle', '[' + metadata[var_name]['var_attrs']['UNITS'] + ']')
                     else:
                         options(var_name, 'ysubtitle', '[' + metadata[var_name]['var_attrs']['UNITS'] + ']')
 
             # Gather up all options in the variable attribute section, toss them into options and see what sticks
             options(var_name, opt_dict=metadata[var_name]['var_attrs'])
```

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/importers/netcdf_to_tplot.py` & `pytplot-mpl-temp-2.1.9/pytplot/importers/netcdf_to_tplot.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/importers/sts_to_tplot.py` & `pytplot-mpl-temp-2.1.9/pytplot/importers/sts_to_tplot.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/importers/tplot_restore.py` & `pytplot-mpl-temp-2.1.9/pytplot/importers/tplot_restore.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/link.py` & `pytplot-mpl-temp-2.1.9/pytplot/link.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/options.py` & `pytplot-mpl-temp-2.1.9/pytplot/options.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/replace_data.py` & `pytplot-mpl-temp-2.1.9/pytplot/replace_data.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/sampledata/test_data.tplot` & `pytplot-mpl-temp-2.1.9/pytplot/sampledata/test_data.tplot`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/spedas_colorbar.py` & `pytplot-mpl-temp-2.1.9/pytplot/spedas_colorbar.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/store_data.py` & `pytplot-mpl-temp-2.1.9/pytplot/store_data.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/timebar.py` & `pytplot-mpl-temp-2.1.9/pytplot/timebar.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/timespan.py` & `pytplot-mpl-temp-2.1.9/pytplot/timespan.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/timestamp.py` & `pytplot-mpl-temp-2.1.9/pytplot/timestamp.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/tlimit.py` & `pytplot-mpl-temp-2.1.9/pytplot/tlimit.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/tplot.py` & `pytplot-mpl-temp-2.1.9/pytplot/tplot.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/tplot_copy.py` & `pytplot-mpl-temp-2.1.9/pytplot/tplot_copy.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/tplot_math/__init__.py` & `pytplot-mpl-temp-2.1.9/pytplot/tplot_math/__init__.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/tplot_math/add.py` & `pytplot-mpl-temp-2.1.9/pytplot/tplot_math/add.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/tplot_math/add_across.py` & `pytplot-mpl-temp-2.1.9/pytplot/tplot_math/add_across.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/tplot_math/avg_res_data.py` & `pytplot-mpl-temp-2.1.9/pytplot/tplot_math/avg_res_data.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/tplot_math/clip.py` & `pytplot-mpl-temp-2.1.9/pytplot/tplot_math/clip.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/tplot_math/crop.py` & `pytplot-mpl-temp-2.1.9/pytplot/tplot_math/crop.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/tplot_math/deflag.py` & `pytplot-mpl-temp-2.1.9/pytplot/tplot_math/deflag.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/tplot_math/degap.py` & `pytplot-mpl-temp-2.1.9/pytplot/tplot_math/degap.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/tplot_math/derive.py` & `pytplot-mpl-temp-2.1.9/pytplot/tplot_math/derive.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/tplot_math/divide.py` & `pytplot-mpl-temp-2.1.9/pytplot/tplot_math/divide.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/tplot_math/examples.py` & `pytplot-mpl-temp-2.1.9/pytplot/tplot_math/examples.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/tplot_math/flatten.py` & `pytplot-mpl-temp-2.1.9/pytplot/tplot_math/flatten.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/tplot_math/interp_nan.py` & `pytplot-mpl-temp-2.1.9/pytplot/tplot_math/interp_nan.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/tplot_math/join_vec.py` & `pytplot-mpl-temp-2.1.9/pytplot/tplot_math/join_vec.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/tplot_math/multiply.py` & `pytplot-mpl-temp-2.1.9/pytplot/tplot_math/multiply.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/tplot_math/pwr_spec.py` & `pytplot-mpl-temp-2.1.9/pytplot/tplot_math/pwr_spec.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/tplot_math/resample.py` & `pytplot-mpl-temp-2.1.9/pytplot/tplot_math/resample.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/tplot_math/spec_mult.py` & `pytplot-mpl-temp-2.1.9/pytplot/tplot_math/spec_mult.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/tplot_math/split_vec.py` & `pytplot-mpl-temp-2.1.9/pytplot/tplot_math/split_vec.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/tplot_math/subtract.py` & `pytplot-mpl-temp-2.1.9/pytplot/tplot_math/subtract.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/tplot_math/tinterp.py` & `pytplot-mpl-temp-2.1.9/pytplot/tplot_math/tinterp.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/tplot_names.py` & `pytplot-mpl-temp-2.1.9/pytplot/tplot_names.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/tplot_options.py` & `pytplot-mpl-temp-2.1.9/pytplot/tplot_options.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/tplot_rename.py` & `pytplot-mpl-temp-2.1.9/pytplot/tplot_rename.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/tplot_utilities.py` & `pytplot-mpl-temp-2.1.9/pytplot/tplot_utilities.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/version.txt` & `pytplot-mpl-temp-2.1.9/pytplot/version.txt`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/xlim.py` & `pytplot-mpl-temp-2.1.9/pytplot/xlim.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/ylim.py` & `pytplot-mpl-temp-2.1.9/pytplot/ylim.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot/zlim.py` & `pytplot-mpl-temp-2.1.9/pytplot/zlim.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/pytplot_mpl_temp.egg-info/PKG-INFO` & `pytplot-mpl-temp-2.1.9/pytplot_mpl_temp.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pytplot-mpl-temp
-Version: 2.1.8
+Version: 2.1.9
 Summary: A python version of IDL tplot libraries
 Home-page: https://github.com/MAVENSDC/pytplot
 Author: MAVEN SDC
 Author-email: mavensdc@lasp.colorado.edu
 License: UNKNOWN
 Keywords: tplot,maven,lasp,IDL,spedas
 Platform: UNKNOWN
```

### Comparing `pytplot-mpl-temp-2.1.8/pytplot_mpl_temp.egg-info/SOURCES.txt` & `pytplot-mpl-temp-2.1.9/pytplot_mpl_temp.egg-info/SOURCES.txt`

 * *Files 3% similar despite different names*

```diff
@@ -38,23 +38,14 @@
 pytplot/HTMLPlotter/TVarFigureMap.py
 pytplot/HTMLPlotter/TVarFigureSpec.py
 pytplot/HTMLPlotter/__init__.py
 pytplot/HTMLPlotter/generate.py
 pytplot/HTMLPlotter/CustomModels/__init__.py
 pytplot/HTMLPlotter/CustomModels/colorbarsidetitle.py
 pytplot/HTMLPlotter/CustomModels/timestamp.py
-pytplot/HTMLPlotter/CustomModels/__pycache__/__init__.cpython-310.pyc
-pytplot/HTMLPlotter/CustomModels/__pycache__/colorbarsidetitle.cpython-310.pyc
-pytplot/HTMLPlotter/CustomModels/__pycache__/timestamp.cpython-310.pyc
-pytplot/HTMLPlotter/__pycache__/TVarFigure1D.cpython-310.pyc
-pytplot/HTMLPlotter/__pycache__/TVarFigureAlt.cpython-310.pyc
-pytplot/HTMLPlotter/__pycache__/TVarFigureMap.cpython-310.pyc
-pytplot/HTMLPlotter/__pycache__/TVarFigureSpec.cpython-310.pyc
-pytplot/HTMLPlotter/__pycache__/__init__.cpython-310.pyc
-pytplot/HTMLPlotter/__pycache__/generate.cpython-310.pyc
 pytplot/MPLPlotter/__init__.py
 pytplot/MPLPlotter/lineplot.py
 pytplot/MPLPlotter/specplot.py
 pytplot/MPLPlotter/tplot.py
 pytplot/QtPlotter/PyTPlot_Exporter.py
 pytplot/QtPlotter/TVarFigure1D.py
 pytplot/QtPlotter/TVarFigureAlt.py
```

### Comparing `pytplot-mpl-temp-2.1.8/setup.cfg` & `pytplot-mpl-temp-2.1.9/setup.cfg`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = pytplot-mpl-temp
-version = 2.1.8
+version = 2.1.9
 author = MAVEN SDC
 author_email = mavensdc@lasp.colorado.edu
 description = A python version of IDL tplot libraries
 url = https://github.com/MAVENSDC/pytplot
 keywords = 
 	tplot
 	maven
```

### Comparing `pytplot-mpl-temp-2.1.8/setup.py` & `pytplot-mpl-temp-2.1.9/setup.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/tests/test_alt_plot.py` & `pytplot-mpl-temp-2.1.9/tests/test_alt_plot.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/tests/test_cdf_to_tplot.py` & `pytplot-mpl-temp-2.1.9/tests/test_cdf_to_tplot.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/tests/test_maps.py` & `pytplot-mpl-temp-2.1.9/tests/test_maps.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/tests/test_matplotlib.py` & `pytplot-mpl-temp-2.1.9/tests/test_matplotlib.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/tests/test_netcdf_to_tplot.py` & `pytplot-mpl-temp-2.1.9/tests/test_netcdf_to_tplot.py`

 * *Files identical despite different names*

### Comparing `pytplot-mpl-temp-2.1.8/tests/test_tplot_math.py` & `pytplot-mpl-temp-2.1.9/tests/test_tplot_math.py`

 * *Files identical despite different names*

