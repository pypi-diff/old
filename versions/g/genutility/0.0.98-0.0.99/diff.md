# Comparing `tmp/genutility-0.0.98.tar.gz` & `tmp/genutility-0.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "genutility-0.0.98.tar", last modified: Fri Mar 24 09:25:17 2023, max compression
+gzip compressed data, was "genutility-0.0.99.tar", last modified: Thu Apr  6 09:35:28 2023, max compression
```

## Comparing `genutility-0.0.98.tar` & `genutility-0.0.99.tar`

### file list

```diff
@@ -1,165 +1,166 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 09:25:17.190564 genutility-0.0.98/
--rw-r--r--   0 runner    (1001) docker     (123)      744 2023-03-24 09:25:09.000000 genutility-0.0.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     3242 2023-03-24 09:25:17.190564 genutility-0.0.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      310 2023-03-24 09:25:09.000000 genutility-0.0.98/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 09:25:17.190564 genutility-0.0.98/genutility/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2141 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/_files.py
--rw-r--r--   0 runner    (1001) docker     (123)      377 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/_func.py
--rw-r--r--   0 runner    (1001) docker     (123)     1637 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/algorithms.py
--rw-r--r--   0 runner    (1001) docker     (123)     5743 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/args.py
--rw-r--r--   0 runner    (1001) docker     (123)    15793 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/aria.py
--rw-r--r--   0 runner    (1001) docker     (123)     2869 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/asynchronous.py
--rw-r--r--   0 runner    (1001) docker     (123)     2432 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/atomic.py
--rw-r--r--   0 runner    (1001) docker     (123)      602 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/av.py
--rw-r--r--   0 runner    (1001) docker     (123)      943 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/bench.py
--rw-r--r--   0 runner    (1001) docker     (123)     1154 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/binary.py
--rw-r--r--   0 runner    (1001) docker     (123)     1485 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/browscap.py
--rw-r--r--   0 runner    (1001) docker     (123)      600 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/bs4.py
--rw-r--r--   0 runner    (1001) docker     (123)     2378 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/casedict.py
--rw-r--r--   0 runner    (1001) docker     (123)     1408 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/cholesky.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 09:25:17.190564 genutility-0.0.98/genutility/compat/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/compat/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1256 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/compat/math.py
--rw-r--r--   0 runner    (1001) docker     (123)    20754 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/concurrency.py
--rw-r--r--   0 runner    (1001) docker     (123)     2021 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/config.py
--rw-r--r--   0 runner    (1001) docker     (123)      270 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/constants_physics.py
--rw-r--r--   0 runner    (1001) docker     (123)     1448 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/constants_video.py
--rw-r--r--   0 runner    (1001) docker     (123)     1314 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/cpython.py
--rw-r--r--   0 runner    (1001) docker     (123)      271 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/crypto.py
--rw-r--r--   0 runner    (1001) docker     (123)     1201 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/csv.py
--rw-r--r--   0 runner    (1001) docker     (123)     1101 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/cv.py
--rw-r--r--   0 runner    (1001) docker     (123)     3926 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/datetime.py
--rw-r--r--   0 runner    (1001) docker     (123)       87 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/dbm.py
--rw-r--r--   0 runner    (1001) docker     (123)     4988 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/debug.py
--rw-r--r--   0 runner    (1001) docker     (123)     7720 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/dict.py
--rw-r--r--   0 runner    (1001) docker     (123)     6798 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/downloadmanager.py
--rw-r--r--   0 runner    (1001) docker     (123)     5416 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/encoder.py
--rw-r--r--   0 runner    (1001) docker     (123)      432 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/error.py
--rw-r--r--   0 runner    (1001) docker     (123)     4725 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     1220 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/factorial.py
--rw-r--r--   0 runner    (1001) docker     (123)    27966 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/file.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 09:25:17.190564 genutility-0.0.98/genutility/fileformats/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/fileformats/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2004 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/fileformats/heif.py
--rw-r--r--   0 runner    (1001) docker     (123)    10913 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/fileformats/jfif.py
--rw-r--r--   0 runner    (1001) docker     (123)    22821 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/fileformats/mp4.py
--rw-r--r--   0 runner    (1001) docker     (123)     6060 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/fileformats/png.py
--rw-r--r--   0 runner    (1001) docker     (123)     7224 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/fileformats/rar.py
--rw-r--r--   0 runner    (1001) docker     (123)     5067 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/fileformats/srt.py
--rw-r--r--   0 runner    (1001) docker     (123)     1286 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/fileformats/sub.py
--rw-r--r--   0 runner    (1001) docker     (123)    18900 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/filesdb.py
--rw-r--r--   0 runner    (1001) docker     (123)    30878 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/filesystem.py
--rw-r--r--   0 runner    (1001) docker     (123)     4528 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/fingerprinting.py
--rw-r--r--   0 runner    (1001) docker     (123)     1722 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/flask.py
--rw-r--r--   0 runner    (1001) docker     (123)     7522 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/func.py
--rw-r--r--   0 runner    (1001) docker     (123)     6666 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/gensim.py
--rw-r--r--   0 runner    (1001) docker     (123)     3838 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/geometry.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 09:25:17.190564 genutility-0.0.98/genutility/hardware/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/hardware/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    17697 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/hardware/ata.py
--rw-r--r--   0 runner    (1001) docker     (123)    10119 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/hardware/scsi.py
--rw-r--r--   0 runner    (1001) docker     (123)     1195 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/hardware/storport.py
--rw-r--r--   0 runner    (1001) docker     (123)     3522 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/hash.py
--rw-r--r--   0 runner    (1001) docker     (123)     2237 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/html.py
--rw-r--r--   0 runner    (1001) docker     (123)    10500 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/http.py
--rw-r--r--   0 runner    (1001) docker     (123)     3989 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/image.py
--rw-r--r--   0 runner    (1001) docker     (123)      253 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/imdb.py
--rw-r--r--   0 runner    (1001) docker     (123)      955 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/implementationdetail.py
--rw-r--r--   0 runner    (1001) docker     (123)     3240 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/indexing.py
--rw-r--r--   0 runner    (1001) docker     (123)    25574 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/iter.py
--rw-r--r--   0 runner    (1001) docker     (123)    16317 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/json.py
--rw-r--r--   0 runner    (1001) docker     (123)      132 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/latex.py
--rw-r--r--   0 runner    (1001) docker     (123)    19968 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/lda.py
--rw-r--r--   0 runner    (1001) docker     (123)     3084 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/logging.py
--rw-r--r--   0 runner    (1001) docker     (123)     1199 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/markdown.py
--rw-r--r--   0 runner    (1001) docker     (123)    11166 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/math.py
--rw-r--r--   0 runner    (1001) docker     (123)     2011 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/mediainfo.py
--rw-r--r--   0 runner    (1001) docker     (123)      628 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/metrics.py
--rw-r--r--   0 runner    (1001) docker     (123)    10829 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/metrictree.py
--rw-r--r--   0 runner    (1001) docker     (123)      365 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/mongo.py
--rw-r--r--   0 runner    (1001) docker     (123)     1020 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/msgpack.py
--rw-r--r--   0 runner    (1001) docker     (123)     2969 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/multihash.py
--rw-r--r--   0 runner    (1001) docker     (123)     1086 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/net.py
--rw-r--r--   0 runner    (1001) docker     (123)      919 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/networkx.py
--rw-r--r--   0 runner    (1001) docker     (123)     1864 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/nlp.py
--rw-r--r--   0 runner    (1001) docker     (123)      302 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/nltk.py
--rw-r--r--   0 runner    (1001) docker     (123)      695 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/numba.py
--rw-r--r--   0 runner    (1001) docker     (123)    24571 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/numpy.py
--rw-r--r--   0 runner    (1001) docker     (123)     2834 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/object.py
--rw-r--r--   0 runner    (1001) docker     (123)     1389 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/ops.py
--rw-r--r--   0 runner    (1001) docker     (123)     3049 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/os.py
--rw-r--r--   0 runner    (1001) docker     (123)       75 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/os_mac.py
--rw-r--r--   0 runner    (1001) docker     (123)      943 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/os_posix.py
--rw-r--r--   0 runner    (1001) docker     (123)      308 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/os_shared.py
--rw-r--r--   0 runner    (1001) docker     (123)     5840 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/os_win.py
--rw-r--r--   0 runner    (1001) docker     (123)     1904 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/pandas.py
--rw-r--r--   0 runner    (1001) docker     (123)     1575 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/parquet.py
--rw-r--r--   0 runner    (1001) docker     (123)     2800 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/pdf.py
--rw-r--r--   0 runner    (1001) docker     (123)     7820 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/pickle.py
--rw-r--r--   0 runner    (1001) docker     (123)     4655 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/pillow.py
--rw-r--r--   0 runner    (1001) docker     (123)      291 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/powerpoint.py
--rw-r--r--   0 runner    (1001) docker     (123)      296 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/profile.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/py.typed
--rw-r--r--   0 runner    (1001) docker     (123)      910 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/rand.py
--rw-r--r--   0 runner    (1001) docker     (123)    15737 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/rasa.py
--rw-r--r--   0 runner    (1001) docker     (123)     1412 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/regression.py
--rw-r--r--   0 runner    (1001) docker     (123)     2870 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/resizing.py
--rw-r--r--   0 runner    (1001) docker     (123)      972 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/rich.py
--rw-r--r--   0 runner    (1001) docker     (123)      833 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/ringlist.py
--rw-r--r--   0 runner    (1001) docker     (123)    25322 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/salesforce.py
--rw-r--r--   0 runner    (1001) docker     (123)     2265 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/scene_change_detection.py
--rw-r--r--   0 runner    (1001) docker     (123)     1475 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/scipy.py
--rw-r--r--   0 runner    (1001) docker     (123)     3527 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/scrapy.py
--rw-r--r--   0 runner    (1001) docker     (123)     3011 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/search.py
--rw-r--r--   0 runner    (1001) docker     (123)     1362 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/segment_tree.py
--rw-r--r--   0 runner    (1001) docker     (123)     4109 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/sequence.py
--rw-r--r--   0 runner    (1001) docker     (123)      143 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/set.py
--rw-r--r--   0 runner    (1001) docker     (123)     3321 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/signal.py
--rw-r--r--   0 runner    (1001) docker     (123)     6600 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/sort.py
--rw-r--r--   0 runner    (1001) docker     (123)     2104 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/spark.py
--rw-r--r--   0 runner    (1001) docker     (123)      715 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/sparql.py
--rw-r--r--   0 runner    (1001) docker     (123)     5534 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/sql.py
--rw-r--r--   0 runner    (1001) docker     (123)     3292 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/sqlite.py
--rw-r--r--   0 runner    (1001) docker     (123)      622 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/statistics.py
--rw-r--r--   0 runner    (1001) docker     (123)     3860 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/stdio.py
--rw-r--r--   0 runner    (1001) docker     (123)     8721 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/string.py
--rw-r--r--   0 runner    (1001) docker     (123)     9061 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/sudoku.py
--rw-r--r--   0 runner    (1001) docker     (123)       67 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/sys.py
--rw-r--r--   0 runner    (1001) docker     (123)      285 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/tensorflow.py
--rw-r--r--   0 runner    (1001) docker     (123)     9828 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/test.py
--rw-r--r--   0 runner    (1001) docker     (123)     3152 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/text.py
--rw-r--r--   0 runner    (1001) docker     (123)      171 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/text_segmentation.py
--rw-r--r--   0 runner    (1001) docker     (123)     2087 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/text_summarization.py
--rw-r--r--   0 runner    (1001) docker     (123)     4450 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/time.py
--rw-r--r--   0 runner    (1001) docker     (123)     2644 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/tls.py
--rw-r--r--   0 runner    (1001) docker     (123)      269 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/toml.py
--rw-r--r--   0 runner    (1001) docker     (123)      267 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/torch.py
--rw-r--r--   0 runner    (1001) docker     (123)    10623 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/torrent.py
--rw-r--r--   0 runner    (1001) docker     (123)     9181 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/tree.py
--rw-r--r--   0 runner    (1001) docker     (123)      344 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/twisted.py
--rw-r--r--   0 runner    (1001) docker     (123)     2788 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/twitch.py
--rw-r--r--   0 runner    (1001) docker     (123)     3171 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/typing.py
--rw-r--r--   0 runner    (1001) docker     (123)      460 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/unicode.py
--rw-r--r--   0 runner    (1001) docker     (123)      921 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/unqlite.py
--rw-r--r--   0 runner    (1001) docker     (123)     2139 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/url.py
--rw-r--r--   0 runner    (1001) docker     (123)    10254 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/videofile.py
--rw-r--r--   0 runner    (1001) docker     (123)     4110 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/widgets.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 09:25:17.190564 genutility-0.0.98/genutility/win/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/win/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9243 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/win/device.py
--rw-r--r--   0 runner    (1001) docker     (123)     4394 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/win/file.py
--rw-r--r--   0 runner    (1001) docker     (123)     1289 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/win/handle.py
--rw-r--r--   0 runner    (1001) docker     (123)     5500 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/win32.py
--rw-r--r--   0 runner    (1001) docker     (123)      705 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/wsgi.py
--rw-r--r--   0 runner    (1001) docker     (123)      429 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/xsl.py
--rw-r--r--   0 runner    (1001) docker     (123)      390 2023-03-24 09:25:09.000000 genutility-0.0.98/genutility/yaml.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 09:25:17.190564 genutility-0.0.98/genutility.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     3242 2023-03-24 09:25:16.000000 genutility-0.0.98/genutility.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     3520 2023-03-24 09:25:17.000000 genutility-0.0.98/genutility.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-24 09:25:16.000000 genutility-0.0.98/genutility.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)     2486 2023-03-24 09:25:16.000000 genutility-0.0.98/genutility.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       11 2023-03-24 09:25:16.000000 genutility-0.0.98/genutility.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)      714 2023-03-24 09:25:09.000000 genutility-0.0.98/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-24 09:25:17.190564 genutility-0.0.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     4004 2023-03-24 09:25:09.000000 genutility-0.0.98/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:35:28.914102 genutility-0.0.99/
+-rw-r--r--   0 runner    (1001) docker     (123)      744 2023-04-06 09:35:22.000000 genutility-0.0.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     3242 2023-04-06 09:35:28.914102 genutility-0.0.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      310 2023-04-06 09:35:22.000000 genutility-0.0.99/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:35:28.914102 genutility-0.0.99/genutility/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2141 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/_files.py
+-rw-r--r--   0 runner    (1001) docker     (123)      377 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/_func.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1637 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/algorithms.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5743 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/args.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16583 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/aria.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2869 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/asynchronous.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2432 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/atomic.py
+-rw-r--r--   0 runner    (1001) docker     (123)      602 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/av.py
+-rw-r--r--   0 runner    (1001) docker     (123)      943 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/bench.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1154 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/binary.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1485 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/browscap.py
+-rw-r--r--   0 runner    (1001) docker     (123)      600 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/bs4.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6097 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/cache.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2378 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/casedict.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1408 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/cholesky.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:35:28.914102 genutility-0.0.99/genutility/compat/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/compat/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1256 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/compat/math.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20754 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/concurrency.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2021 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)      270 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/constants_physics.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1448 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/constants_video.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1314 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/cpython.py
+-rw-r--r--   0 runner    (1001) docker     (123)      271 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/crypto.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1201 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/csv.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1101 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/cv.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3926 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/datetime.py
+-rw-r--r--   0 runner    (1001) docker     (123)       87 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/dbm.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4988 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/debug.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7720 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/dict.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6798 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/downloadmanager.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5416 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/encoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)      432 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/error.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4725 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1220 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/factorial.py
+-rw-r--r--   0 runner    (1001) docker     (123)    27966 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/file.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:35:28.914102 genutility-0.0.99/genutility/fileformats/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/fileformats/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2004 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/fileformats/heif.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10913 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/fileformats/jfif.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22821 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/fileformats/mp4.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6060 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/fileformats/png.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7224 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/fileformats/rar.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5067 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/fileformats/srt.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1286 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/fileformats/sub.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18900 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/filesdb.py
+-rw-r--r--   0 runner    (1001) docker     (123)    30878 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/filesystem.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4528 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/fingerprinting.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1722 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/flask.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7522 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/func.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6666 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/gensim.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3838 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/geometry.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:35:28.914102 genutility-0.0.99/genutility/hardware/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/hardware/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17697 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/hardware/ata.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10119 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/hardware/scsi.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1195 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/hardware/storport.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3522 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/hash.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2237 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/html.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10500 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/http.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3989 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/image.py
+-rw-r--r--   0 runner    (1001) docker     (123)      253 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/imdb.py
+-rw-r--r--   0 runner    (1001) docker     (123)      955 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/implementationdetail.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3240 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/indexing.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25574 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/iter.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13857 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/json.py
+-rw-r--r--   0 runner    (1001) docker     (123)      132 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/latex.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19968 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/lda.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3084 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/logging.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1199 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/markdown.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11166 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/math.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2011 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/mediainfo.py
+-rw-r--r--   0 runner    (1001) docker     (123)      628 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/metrics.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10829 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/metrictree.py
+-rw-r--r--   0 runner    (1001) docker     (123)      365 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/mongo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3289 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/msgpack.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2969 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/multihash.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1086 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/net.py
+-rw-r--r--   0 runner    (1001) docker     (123)      919 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/networkx.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1864 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/nlp.py
+-rw-r--r--   0 runner    (1001) docker     (123)      302 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/nltk.py
+-rw-r--r--   0 runner    (1001) docker     (123)      695 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/numba.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24571 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/numpy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2834 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/object.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1389 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/ops.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3049 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/os.py
+-rw-r--r--   0 runner    (1001) docker     (123)       75 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/os_mac.py
+-rw-r--r--   0 runner    (1001) docker     (123)      943 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/os_posix.py
+-rw-r--r--   0 runner    (1001) docker     (123)      308 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/os_shared.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5840 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/os_win.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1904 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/pandas.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1575 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/parquet.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2800 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/pdf.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3589 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/pickle.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4725 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/pillow.py
+-rw-r--r--   0 runner    (1001) docker     (123)      291 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/powerpoint.py
+-rw-r--r--   0 runner    (1001) docker     (123)      296 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/profile.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/py.typed
+-rw-r--r--   0 runner    (1001) docker     (123)      910 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/rand.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15737 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/rasa.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1412 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/regression.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2870 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/resizing.py
+-rw-r--r--   0 runner    (1001) docker     (123)      972 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/rich.py
+-rw-r--r--   0 runner    (1001) docker     (123)      833 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/ringlist.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25322 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/salesforce.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2265 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/scene_change_detection.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1475 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/scipy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3527 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/scrapy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3011 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/search.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1362 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/segment_tree.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4109 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/sequence.py
+-rw-r--r--   0 runner    (1001) docker     (123)      143 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/set.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3321 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/signal.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6600 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/sort.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2104 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/spark.py
+-rw-r--r--   0 runner    (1001) docker     (123)      715 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/sparql.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5534 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/sql.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3292 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/sqlite.py
+-rw-r--r--   0 runner    (1001) docker     (123)      622 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/statistics.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3860 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/stdio.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8721 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/string.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9061 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/sudoku.py
+-rw-r--r--   0 runner    (1001) docker     (123)       67 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/sys.py
+-rw-r--r--   0 runner    (1001) docker     (123)      285 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/tensorflow.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9828 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/test.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3152 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/text.py
+-rw-r--r--   0 runner    (1001) docker     (123)      171 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/text_segmentation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2087 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/text_summarization.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4450 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/time.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2644 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/tls.py
+-rw-r--r--   0 runner    (1001) docker     (123)      269 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/toml.py
+-rw-r--r--   0 runner    (1001) docker     (123)      267 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/torch.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10623 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/torrent.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9181 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/tree.py
+-rw-r--r--   0 runner    (1001) docker     (123)      344 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/twisted.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2788 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/twitch.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3171 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/typing.py
+-rw-r--r--   0 runner    (1001) docker     (123)      464 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/unicode.py
+-rw-r--r--   0 runner    (1001) docker     (123)      921 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/unqlite.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2139 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/url.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10254 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/videofile.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4110 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/widgets.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:35:28.914102 genutility-0.0.99/genutility/win/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/win/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9243 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/win/device.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4394 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/win/file.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1289 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/win/handle.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5500 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/win32.py
+-rw-r--r--   0 runner    (1001) docker     (123)      705 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/wsgi.py
+-rw-r--r--   0 runner    (1001) docker     (123)      429 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/xsl.py
+-rw-r--r--   0 runner    (1001) docker     (123)      390 2023-04-06 09:35:22.000000 genutility-0.0.99/genutility/yaml.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:35:28.914102 genutility-0.0.99/genutility.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     3242 2023-04-06 09:35:28.000000 genutility-0.0.99/genutility.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     3540 2023-04-06 09:35:28.000000 genutility-0.0.99/genutility.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 09:35:28.000000 genutility-0.0.99/genutility.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     2486 2023-04-06 09:35:28.000000 genutility-0.0.99/genutility.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       11 2023-04-06 09:35:28.000000 genutility-0.0.99/genutility.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      714 2023-04-06 09:35:22.000000 genutility-0.0.99/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 09:35:28.914102 genutility-0.0.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     4004 2023-04-06 09:35:22.000000 genutility-0.0.99/setup.py
```

### Comparing `genutility-0.0.98/LICENSE` & `genutility-0.0.99/LICENSE`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/PKG-INFO` & `genutility-0.0.99/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: genutility
-Version: 0.0.98
+Version: 0.0.99
 Summary: A collection of various Python utilities
 Home-page: https://github.com/Dobatymo/genutility
 Author: Dobatymo
 License: UNKNOWN
 Description: # genutility
         
         A collection of various Python utilities.
```

### Comparing `genutility-0.0.98/genutility/_files.py` & `genutility-0.0.99/genutility/_files.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/algorithms.py` & `genutility-0.0.99/genutility/algorithms.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/args.py` & `genutility-0.0.99/genutility/args.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/aria.py` & `genutility-0.0.99/genutility/aria.py`

 * *Files 2% similar despite different names*

```diff
@@ -313,14 +313,26 @@
             },
         )
 
         gid = self.query("add_uri", [uri], options)
         self.gids.add(gid)
         return gid
 
+    def block_x(
+        self,
+        num: int,
+        active_callback: Optional[CallbackFuncT] = None,
+        waiting_callback: Optional[CallbackFuncT] = None,
+    ) -> Tuple[Optional[str], Optional[str]]:
+        if self.managed_downloads() >= num:
+            finished_gid, path = self.block_one(active_callback, waiting_callback)
+            return finished_gid, path
+        else:
+            return None, None
+
     def download_x(
         self,
         num: int,
         uri: str,
         path: Optional[str] = None,
         filename: Optional[str] = None,
         headers: Optional[Union[SequenceT[str], MappingT[str, str]]] = None,
@@ -345,19 +357,16 @@
             continue_,
             retry_wait,
             max_tries,
             connect_timeout,
             timeout,
             no_netrc,
         )
-        if self.managed_downloads() >= num:
-            finished_gid, path = self.block_one(active_callback, waiting_callback)
-            return queued_gid, finished_gid, path
-
-        return queued_gid, None, None
+        finished_gid, path = self.block_x(num, active_callback, waiting_callback)
+        return queued_gid, finished_gid, path
 
 
 class DownloadManager:
 
     """To use from a single thread.
 
     State transitions:
@@ -428,19 +437,29 @@
         return self.block_uid(uid)
 
 
 if __name__ == "__main__":
     from argparse import ArgumentParser
 
     parser = ArgumentParser()
-    parser.add_argument("uris", metavar="URI", nargs="+", help="URLs to download")
+    parser.add_argument("action", choices=("download", "remove"))
+    parser.add_argument("--uris", metavar="URI", nargs="+", default=[], help="URLs to download")
     parser.add_argument("--outpath", default=".", help="Output directory")
     parser.add_argument("--max", default=2, type=int, help="Maximum concurrent downloads")
+    parser.add_argument("--gids", metavar="GID", nargs="+", default=[], help="GIDs")
     args = parser.parse_args()
 
     d = AriaDownloader()
-    for uri in args.uris:
-        path = d.download_x(args.max, uri, args.path)
-        print(f"Downloaded {uri} to {path}")
-
-    for a in d.block_all():
-        print(a)
+    if args.action == "download":
+        for uri in args.uris:
+            try:
+                queued_gid, finished_gid, path = d.download_x(args.max, uri, args.path)
+                print(f"Downloaded {uri} to {path}")
+            except DownloadFailed as e:
+                print("Download failed: %s", e)
+
+        for a in d.block_all():
+            print(a)
+
+    elif args.action == "remove":
+        for gid in args.gids:
+            d.query("remove", gid)
```

### Comparing `genutility-0.0.98/genutility/asynchronous.py` & `genutility-0.0.99/genutility/asynchronous.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/atomic.py` & `genutility-0.0.99/genutility/atomic.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/av.py` & `genutility-0.0.99/genutility/av.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/bench.py` & `genutility-0.0.99/genutility/bench.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/binary.py` & `genutility-0.0.99/genutility/binary.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/browscap.py` & `genutility-0.0.99/genutility/browscap.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/bs4.py` & `genutility-0.0.99/genutility/bs4.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/casedict.py` & `genutility-0.0.99/genutility/casedict.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/cholesky.py` & `genutility-0.0.99/genutility/cholesky.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/compat/math.py` & `genutility-0.0.99/genutility/compat/math.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/concurrency.py` & `genutility-0.0.99/genutility/concurrency.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/config.py` & `genutility-0.0.99/genutility/config.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/constants_video.py` & `genutility-0.0.99/genutility/constants_video.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/cpython.py` & `genutility-0.0.99/genutility/cpython.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/csv.py` & `genutility-0.0.99/genutility/csv.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/cv.py` & `genutility-0.0.99/genutility/cv.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/datetime.py` & `genutility-0.0.99/genutility/datetime.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/debug.py` & `genutility-0.0.99/genutility/debug.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/dict.py` & `genutility-0.0.99/genutility/dict.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/downloadmanager.py` & `genutility-0.0.99/genutility/downloadmanager.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/encoder.py` & `genutility-0.0.99/genutility/encoder.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/exceptions.py` & `genutility-0.0.99/genutility/exceptions.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/factorial.py` & `genutility-0.0.99/genutility/factorial.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/file.py` & `genutility-0.0.99/genutility/file.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/fileformats/heif.py` & `genutility-0.0.99/genutility/fileformats/heif.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/fileformats/jfif.py` & `genutility-0.0.99/genutility/fileformats/jfif.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/fileformats/mp4.py` & `genutility-0.0.99/genutility/fileformats/mp4.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/fileformats/png.py` & `genutility-0.0.99/genutility/fileformats/png.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/fileformats/rar.py` & `genutility-0.0.99/genutility/fileformats/rar.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/fileformats/srt.py` & `genutility-0.0.99/genutility/fileformats/srt.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/fileformats/sub.py` & `genutility-0.0.99/genutility/fileformats/sub.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/filesdb.py` & `genutility-0.0.99/genutility/filesdb.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/filesystem.py` & `genutility-0.0.99/genutility/filesystem.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/fingerprinting.py` & `genutility-0.0.99/genutility/fingerprinting.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/flask.py` & `genutility-0.0.99/genutility/flask.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/func.py` & `genutility-0.0.99/genutility/func.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/gensim.py` & `genutility-0.0.99/genutility/gensim.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/geometry.py` & `genutility-0.0.99/genutility/geometry.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/hardware/ata.py` & `genutility-0.0.99/genutility/hardware/ata.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/hardware/scsi.py` & `genutility-0.0.99/genutility/hardware/scsi.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/hardware/storport.py` & `genutility-0.0.99/genutility/hardware/storport.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/hash.py` & `genutility-0.0.99/genutility/hash.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/html.py` & `genutility-0.0.99/genutility/html.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/http.py` & `genutility-0.0.99/genutility/http.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/image.py` & `genutility-0.0.99/genutility/image.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/implementationdetail.py` & `genutility-0.0.99/genutility/implementationdetail.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/indexing.py` & `genutility-0.0.99/genutility/indexing.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/iter.py` & `genutility-0.0.99/genutility/iter.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/json.py` & `genutility-0.0.99/genutility/json.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,24 +1,22 @@
 import csv
 import datetime
 import json
 import logging
-from functools import partial, wraps
+from functools import partial
 from itertools import islice
 from pathlib import Path
 from types import ModuleType
 from typing import IO, Any, Callable, Dict, FrozenSet, Iterable, Iterator, Optional, Sequence, Tuple, Type, Union
 
 from typing_extensions import TypedDict  # typing.TypedDict is available in Python 3.8+
 
-from .atomic import TransactionalCreateFile, sopen
+from .atomic import sopen
 from .datetime import datetime_from_utc_timestamp_ms, now
 from .file import copen
-from .filesystem import mdatetime
-from .object import args_to_key
 
 PathStr = Union[Path, str]
 JsonDict = Dict[str, Any]
 
 logger = logging.getLogger(__name__)
 
 
@@ -54,14 +52,16 @@
 
 class BuiltinRoundtripEncoder(json.JSONEncoder):
     def default(self, obj):
         if isinstance(obj, datetime.timedelta):
             return {"$timedelta": (obj.days, obj.seconds, obj.microseconds)}
         elif isinstance(obj, datetime.datetime):
             return {"$datetime": obj.isoformat()}
+        elif isinstance(obj, datetime.date):
+            return {"$dateobj": obj.isoformat()}
         elif isinstance(obj, set):
             return {"$set": tuple(obj)}
         elif isinstance(obj, frozenset):
             return {"$frozenset": tuple(obj)}
 
         return json.JSONEncoder.default(self, obj)
 
@@ -75,29 +75,34 @@
             key, value = next(iter(obj.items()))
             if key == "$timedelta":
                 return datetime.timedelta(*value)
             elif key == "$datetime":
                 return datetime.datetime.fromisoformat(value)
             elif key == "$date":  # for compatibility with bson.json_util
                 return datetime_from_utc_timestamp_ms(value)
+            elif key == "$dateobj":
+                return datetime.date.fromisoformat(value)
             elif key == "$set":
                 return set(value)
             elif key == "$frozenset":
                 return frozenset(value)
 
         return obj
 
 
 def read_json_schema(path: PathStr) -> JsonDict:
     with open(path, encoding="utf-8") as fr:
         return json.load(fr)
 
 
 def read_json(
-    path: PathStr, schema: Optional[Union[str, JsonDict]] = None, cls: Any = None, object_hook: Any = None
+    path: PathStr,
+    schema: Optional[Union[str, JsonDict]] = None,
+    cls: Optional[Type[json.JSONDecoder]] = None,
+    object_hook: Any = None,
 ) -> Any:
     """Read the json file at `path` and optionally validates the input according to `schema`.
     The validation requires `jsonschema`.
     `schema` can either be a path as well, or a Python dict which represents the schema.
     `cls` and `object_hook` is passed through to `json.load`.
     """
 
@@ -325,134 +330,57 @@
             self.write(obj)
 
     def close(self) -> None:
         if self.doclose:
             self.f.close()
 
 
-def read_json_lines(file: PathStr, object_hook: Optional[Callable] = None) -> Iterator[Any]:
+def read_json_lines(
+    file: PathStr, cls: Optional[Type[json.JSONDecoder]] = None, object_hook: Optional[Callable] = None
+) -> Iterator[Any]:
     """Iterate over a JSON Lines `file` object by object.
     `object_hook` is passed through to `json.load`.
     """
 
-    with json_lines.from_path(file, mode="rt", object_hook=object_hook) as fr:
+    with json_lines.from_path(file, mode="rt", cls=cls, object_hook=object_hook) as fr:
         yield from fr
 
 
+def write_json_lines(
+    it: Iterable[Any],
+    path,
+    ensure_ascii: bool = False,
+    sort_keys: bool = False,
+    default: Optional[Callable] = None,
+    safe: bool = False,
+) -> Iterator[Any]:
+    with sopen(path, "wt", encoding="utf-8", safe=safe) as fw:
+        with json_lines.from_stream(fw, ensure_ascii=ensure_ascii, sort_keys=sort_keys, default=default) as fw:
+            for obj in it:
+                fw.write(obj)
+                yield obj
+
+
 def jl_to_csv(jlpath: PathStr, csvpath: str, keyfunc: Callable[[JsonDict], Sequence[str]], mode: str = "xt") -> None:
     with json_lines.from_path(jlpath, "rt") as fr:
         with open(csvpath, mode, encoding="utf-8", newline="") as csvfile:
             fw = csv.writer(csvfile)
             for obj in fr:
                 fw.writerow(keyfunc(obj))
 
 
-def key_to_hash(key: Any, default: Optional[Callable] = None) -> str:
+def key_to_hash(
+    key: Any, ensure_ascii: bool = False, sort_keys: bool = False, default: Optional[Callable] = None
+) -> str:
     from hashlib import md5
 
-    binary = json.dumps(key, default=default).encode("utf-8")
+    binary = json.dumps(key, ensure_ascii=ensure_ascii, sort_keys=sort_keys, default=default).encode("utf-8")
     return md5(binary).hexdigest()  # nosec
 
 
-def cache(
-    path: Path,
-    duration: Optional[datetime.timedelta] = None,
-    ensure_ascii: bool = False,
-    indent: Optional[Union[str, int]] = None,
-    sort_keys: bool = False,
-    default: Optional[Callable] = None,
-    object_hook: Optional[Callable] = None,
-) -> Callable:
-    """Decorator to cache results of function to json files at `path` for `duration`.
-    The remaining parameters are passed through to `json.dump`.
-    """
-
-    if duration is None:
-        _duration = datetime.timedelta.max
-    else:
-        _duration = duration
-
-    def decorator(func: Callable) -> Callable:
-        @wraps(func)
-        def inner(*args, **kwargs):
-            hash = key_to_hash(args_to_key(args, kwargs, {}), default=default)
-            fullpath = path / hash
-
-            try:
-                invalid = now() - mdatetime(fullpath) > _duration
-            except FileNotFoundError:
-                invalid = True
-
-            if invalid:
-                path.mkdir(parents=True, exist_ok=True)
-                ret = func(*args, **kwargs)
-                write_json(
-                    ret,
-                    fullpath,
-                    ensure_ascii=ensure_ascii,
-                    indent=indent,
-                    sort_keys=sort_keys,
-                    default=default,
-                    safe=True,
-                )
-                return ret
-            else:
-                return read_json(fullpath, object_hook=object_hook)
-
-        return inner
-
-    return decorator
-
-
-def jsonlines_cache(
-    path: Path,
-    duration: Optional[datetime.timedelta] = None,
-    ensure_ascii: bool = False,
-    sort_keys: bool = False,
-    default: Optional[Callable] = None,
-    object_hook: Optional[Callable] = None,
-) -> Callable:
-    """Decorator to cache results of function to jsonlines files at `path` for `duration`.
-    The remaining parameters are passed through to `json_lines.from_path`.
-    """
-
-    duration = duration or datetime.timedelta.max
-
-    def decorator(func: Callable) -> Callable:
-        @wraps(func)
-        def inner(*args, **kwargs):
-            hash = key_to_hash(args_to_key(args, kwargs, {}), default=default)
-            fullpath = path / hash
-
-            try:
-                invalid = now() - mdatetime(fullpath) > duration
-            except FileNotFoundError:
-                invalid = True
-
-            if invalid:
-                path.mkdir(parents=True, exist_ok=True)
-                with TransactionalCreateFile(fullpath, "wt") as stream:
-                    with json_lines.from_stream(
-                        stream, ensure_ascii=ensure_ascii, sort_keys=sort_keys, default=default
-                    ) as fw:
-                        # if `func` raises, TransactionalCreateFile makes sure that the original
-                        # cache file remains unmodified and that temporary files are deleted
-                        for obj in func(*args, **kwargs):
-                            fw.write(obj)
-                            yield obj
-            else:
-                with json_lines.from_path(fullpath, "rt", object_hook=object_hook) as fr:
-                    for obj in fr:
-                        yield obj
-
-        return inner
-
-    return decorator
-
-
 class JsonLinesFormatter(logging.Formatter):
 
     """A JSON Lines formatter for the Python logging library.
     It expects a `dict` as logging message.
     For example:
             logger = logging.getLogger("jsonlines-test")
             handler = logging.StreamHandler()
```

### Comparing `genutility-0.0.98/genutility/lda.py` & `genutility-0.0.99/genutility/lda.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/logging.py` & `genutility-0.0.99/genutility/logging.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/markdown.py` & `genutility-0.0.99/genutility/markdown.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/math.py` & `genutility-0.0.99/genutility/math.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/mediainfo.py` & `genutility-0.0.99/genutility/mediainfo.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/metrics.py` & `genutility-0.0.99/genutility/metrics.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/metrictree.py` & `genutility-0.0.99/genutility/metrictree.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/multihash.py` & `genutility-0.0.99/genutility/multihash.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/net.py` & `genutility-0.0.99/genutility/net.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/networkx.py` & `genutility-0.0.99/genutility/networkx.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/nlp.py` & `genutility-0.0.99/genutility/nlp.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/numba.py` & `genutility-0.0.99/genutility/numba.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/numpy.py` & `genutility-0.0.99/genutility/numpy.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/object.py` & `genutility-0.0.99/genutility/object.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/ops.py` & `genutility-0.0.99/genutility/ops.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/os.py` & `genutility-0.0.99/genutility/os.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/os_posix.py` & `genutility-0.0.99/genutility/os_posix.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/os_win.py` & `genutility-0.0.99/genutility/os_win.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/pandas.py` & `genutility-0.0.99/genutility/pandas.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/parquet.py` & `genutility-0.0.99/genutility/parquet.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/pdf.py` & `genutility-0.0.99/genutility/pdf.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/pillow.py` & `genutility-0.0.99/genutility/pillow.py`

 * *Files 6% similar despite different names*

```diff
@@ -125,27 +125,27 @@
     text_with_outline(d, pos, text, font, fillcolor, outlinecolor, 2)
 
 
 def _fix_orientation(img: Image.Image, orientation: int) -> Image.Image:
     if orientation == 1:
         raise NoActionNeeded("File already properly rotated")
     elif orientation == 2:
-        img = img.transpose(Image.FLIP_LEFT_RIGHT)
+        img = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
     elif orientation == 3:
-        img = img.transpose(Image.ROTATE_180)
+        img = img.transpose(Image.Transpose.ROTATE_180)
     elif orientation == 4:
-        img = img.transpose(Image.FLIP_TOP_BOTTOM)
+        img = img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
     elif orientation == 5:
-        img = img.transpose(Image.TRANSPOSE)
+        img = img.transpose(Image.Transpose.TRANSPOSE)
     elif orientation == 6:
-        img = img.transpose(Image.ROTATE_270)
+        img = img.transpose(Image.Transpose.ROTATE_270)
     elif orientation == 7:
-        img = img.transpose(Image.TRANSVERSE)
+        img = img.transpose(Image.Transpose.TRANSVERSE)
     elif orientation == 8:
-        img = img.transpose(Image.ROTATE_90)
+        img = img.transpose(Image.Transpose.ROTATE_90)
     else:
         raise ValueError("Unsupported orientation")
 
     return img
 
 
 def fix_orientation(img: Image.Image, exif: dict) -> Image.Image:
```

### Comparing `genutility-0.0.98/genutility/rand.py` & `genutility-0.0.99/genutility/rand.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/rasa.py` & `genutility-0.0.99/genutility/rasa.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/regression.py` & `genutility-0.0.99/genutility/regression.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/resizing.py` & `genutility-0.0.99/genutility/resizing.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/rich.py` & `genutility-0.0.99/genutility/rich.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/ringlist.py` & `genutility-0.0.99/genutility/ringlist.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/salesforce.py` & `genutility-0.0.99/genutility/salesforce.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/scene_change_detection.py` & `genutility-0.0.99/genutility/scene_change_detection.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/scipy.py` & `genutility-0.0.99/genutility/scipy.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/scrapy.py` & `genutility-0.0.99/genutility/scrapy.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/search.py` & `genutility-0.0.99/genutility/search.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/segment_tree.py` & `genutility-0.0.99/genutility/segment_tree.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/sequence.py` & `genutility-0.0.99/genutility/sequence.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/signal.py` & `genutility-0.0.99/genutility/signal.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/sort.py` & `genutility-0.0.99/genutility/sort.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/spark.py` & `genutility-0.0.99/genutility/spark.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/sparql.py` & `genutility-0.0.99/genutility/sparql.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/sql.py` & `genutility-0.0.99/genutility/sql.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/sqlite.py` & `genutility-0.0.99/genutility/sqlite.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/statistics.py` & `genutility-0.0.99/genutility/statistics.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/stdio.py` & `genutility-0.0.99/genutility/stdio.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/string.py` & `genutility-0.0.99/genutility/string.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/sudoku.py` & `genutility-0.0.99/genutility/sudoku.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/test.py` & `genutility-0.0.99/genutility/test.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/text.py` & `genutility-0.0.99/genutility/text.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/text_summarization.py` & `genutility-0.0.99/genutility/text_summarization.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/time.py` & `genutility-0.0.99/genutility/time.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/tls.py` & `genutility-0.0.99/genutility/tls.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/torrent.py` & `genutility-0.0.99/genutility/torrent.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/tree.py` & `genutility-0.0.99/genutility/tree.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/twitch.py` & `genutility-0.0.99/genutility/twitch.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/typing.py` & `genutility-0.0.99/genutility/typing.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/unqlite.py` & `genutility-0.0.99/genutility/unqlite.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/url.py` & `genutility-0.0.99/genutility/url.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/videofile.py` & `genutility-0.0.99/genutility/videofile.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/widgets.py` & `genutility-0.0.99/genutility/widgets.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/win/device.py` & `genutility-0.0.99/genutility/win/device.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/win/file.py` & `genutility-0.0.99/genutility/win/file.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/win/handle.py` & `genutility-0.0.99/genutility/win/handle.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/win32.py` & `genutility-0.0.99/genutility/win32.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility/wsgi.py` & `genutility-0.0.99/genutility/wsgi.py`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/genutility.egg-info/PKG-INFO` & `genutility-0.0.99/genutility.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: genutility
-Version: 0.0.98
+Version: 0.0.99
 Summary: A collection of various Python utilities
 Home-page: https://github.com/Dobatymo/genutility
 Author: Dobatymo
 License: UNKNOWN
 Description: # genutility
         
         A collection of various Python utilities.
```

### Comparing `genutility-0.0.98/genutility.egg-info/SOURCES.txt` & `genutility-0.0.99/genutility.egg-info/SOURCES.txt`

 * *Files 0% similar despite different names*

```diff
@@ -11,14 +11,15 @@
 genutility/asynchronous.py
 genutility/atomic.py
 genutility/av.py
 genutility/bench.py
 genutility/binary.py
 genutility/browscap.py
 genutility/bs4.py
+genutility/cache.py
 genutility/casedict.py
 genutility/cholesky.py
 genutility/concurrency.py
 genutility/config.py
 genutility/constants_physics.py
 genutility/constants_video.py
 genutility/cpython.py
```

### Comparing `genutility-0.0.98/genutility.egg-info/requires.txt` & `genutility-0.0.99/genutility.egg-info/requires.txt`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/pyproject.toml` & `genutility-0.0.99/pyproject.toml`

 * *Files identical despite different names*

### Comparing `genutility-0.0.98/setup.py` & `genutility-0.0.99/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -114,15 +114,15 @@
 }
 
 extras_require["all"] = sorted(set(chain.from_iterable(extras_require.values())))
 
 setup(
     author="Dobatymo",
     name="genutility",
-    version="0.0.98",
+    version="0.0.99",
     url="https://github.com/Dobatymo/genutility",
     description="A collection of various Python utilities",
     long_description=long_description,
     long_description_content_type="text/markdown",
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: ISC License (ISCL)",
```

