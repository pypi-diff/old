# Comparing `tmp/tlux-0.0.8.tar.gz` & `tmp/tlux-0.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "tlux-0.0.8.tar", last modified: Sun Mar 20 17:38:43 2022, max compression
+gzip compressed data, was "tlux-0.0.9.tar", last modified: Wed Mar 30 15:57:31 2022, max compression
```

## Comparing `tlux-0.0.8.tar` & `tlux-0.0.9.tar`

### file list

```diff
@@ -1,75 +1,77 @@
-drwxr-xr-x   0 thomaslux   (501) staff       (20)        0 2022-03-20 17:38:43.320042 tlux-0.0.8/
--rw-r--r--   0 thomaslux   (501) staff       (20)     1056 2022-02-05 17:54:06.000000 tlux-0.0.8/LICENSE.txt
--rw-r--r--   0 thomaslux   (501) staff       (20)       25 2022-03-20 17:38:36.000000 tlux-0.0.8/MANIFEST.in
--rw-r--r--   0 thomaslux   (501) staff       (20)      525 2022-03-20 17:38:43.320234 tlux-0.0.8/PKG-INFO
--rw-r--r--   0 thomaslux   (501) staff       (20)      108 2022-03-20 17:38:43.321035 tlux-0.0.8/setup.cfg
--rw-r--r--   0 thomaslux   (501) staff       (20)     2864 2022-02-06 16:48:22.000000 tlux-0.0.8/setup.py
-drwxr-xr-x   0 thomaslux   (501) staff       (20)        0 2022-03-20 17:38:43.270616 tlux-0.0.8/tlux/
--rw-r--r--   0 thomaslux   (501) staff       (20)      247 2022-02-05 17:57:41.000000 tlux-0.0.8/tlux/__init__.py
--rw-r--r--   0 thomaslux   (501) staff       (20)      334 2022-02-05 17:59:31.000000 tlux-0.0.8/tlux/__main__.py
-drwxr-xr-x   0 thomaslux   (501) staff       (20)        0 2022-03-20 17:38:43.277489 tlux-0.0.8/tlux/about/
--rw-r--r--   0 thomaslux   (501) staff       (20)       47 2022-02-05 17:54:06.000000 tlux-0.0.8/tlux/about/author.txt
--rw-r--r--   0 thomaslux   (501) staff       (20)      139 2022-02-05 18:13:26.000000 tlux-0.0.8/tlux/about/classifiers.txt
--rw-r--r--   0 thomaslux   (501) staff       (20)       11 2022-02-05 18:10:24.000000 tlux-0.0.8/tlux/about/description.txt
--rw-r--r--   0 thomaslux   (501) staff       (20)       15 2022-02-05 17:54:06.000000 tlux-0.0.8/tlux/about/keywords.txt
--rw-r--r--   0 thomaslux   (501) staff       (20)        5 2022-02-05 18:09:11.000000 tlux-0.0.8/tlux/about/on_pypi.txt
--rw-r--r--   0 thomaslux   (501) staff       (20)        5 2022-02-05 17:57:27.000000 tlux-0.0.8/tlux/about/package_name.txt
--rw-r--r--   0 thomaslux   (501) staff       (20)       42 2022-02-12 17:36:17.000000 tlux-0.0.8/tlux/about/requirements.txt
--rw-r--r--   0 thomaslux   (501) staff       (20)        6 2022-03-12 15:07:12.000000 tlux-0.0.8/tlux/about/version.txt
--rw-r--r--   0 thomaslux   (501) staff       (20)     1005 2022-03-20 17:38:36.000000 tlux-0.0.8/tlux/about/version_history.md
-drwxr-xr-x   0 thomaslux   (501) staff       (20)        0 2022-03-20 17:38:43.278537 tlux-0.0.8/tlux/approximate/
-drwxr-xr-x   0 thomaslux   (501) staff       (20)        0 2022-03-20 17:38:43.281073 tlux-0.0.8/tlux/approximate/apos/
--rw-r--r--   0 thomaslux   (501) staff       (20)        4 2022-03-20 17:34:57.000000 tlux-0.0.8/tlux/approximate/apos/.gitignore
--rw-r--r--   0 thomaslux   (501) staff       (20)    34819 2022-03-18 18:34:07.000000 tlux-0.0.8/tlux/approximate/apos/__init__.py
-drwxr-xr-x   0 thomaslux   (501) staff       (20)        0 2022-03-20 17:38:43.291935 tlux-0.0.8/tlux/approximate/apos/apos/
--rw-r--r--   0 thomaslux   (501) staff       (20)    65761 2022-03-15 20:22:12.000000 tlux-0.0.8/tlux/approximate/apos/apos/__init__.py
--rw-r--r--   0 thomaslux   (501) staff       (20)    63691 2022-03-20 17:37:49.000000 tlux-0.0.8/tlux/approximate/apos/apos/apos.f90
--rw-r--r--   0 thomaslux   (501) staff       (20)     3724 2022-03-15 20:22:00.000000 tlux-0.0.8/tlux/approximate/apos/apos/apos.mod
--rwxr-xr-x   0 thomaslux   (501) staff       (20)   398064 2022-03-15 20:22:21.000000 tlux-0.0.8/tlux/approximate/apos/apos/apos.x86_64.so
--rw-r--r--   0 thomaslux   (501) staff       (20)   264367 2022-03-15 20:22:12.000000 tlux-0.0.8/tlux/approximate/apos/apos/apos_c_wrapper.f90
--rw-r--r--   0 thomaslux   (501) staff       (20)    65761 2022-03-15 20:22:12.000000 tlux-0.0.8/tlux/approximate/apos/apos/apos_python_wrapper.py
--rw-r--r--   0 thomaslux   (501) staff       (20)     6676 2022-03-15 20:22:19.000000 tlux-0.0.8/tlux/approximate/apos/apos/c_apos.mod
--rw-r--r--   0 thomaslux   (501) staff       (20)      923 2022-03-15 20:22:19.000000 tlux-0.0.8/tlux/approximate/apos/apos/c_matrix_operations.mod
--rw-r--r--   0 thomaslux   (501) staff       (20)      747 2022-03-15 20:22:00.000000 tlux-0.0.8/tlux/approximate/apos/apos/matrix_operations.mod
--rw-r--r--   0 thomaslux   (501) staff       (20)    63691 2022-03-20 17:37:49.000000 tlux-0.0.8/tlux/approximate/apos/apos.f90
-drwxr-xr-x   0 thomaslux   (501) staff       (20)        0 2022-03-20 17:38:43.293794 tlux-0.0.8/tlux/approximate/apos/test/
--rw-r--r--   0 thomaslux   (501) staff       (20)     5244 2022-03-06 02:04:26.000000 tlux-0.0.8/tlux/approximate/apos/test/argselect.f90
--rw-r--r--   0 thomaslux   (501) staff       (20)      418 2022-03-06 02:04:12.000000 tlux-0.0.8/tlux/approximate/apos/test/test_argselect.py
--rw-r--r--   0 thomaslux   (501) staff       (20)     6926 2022-02-13 01:42:27.000000 tlux-0.0.8/tlux/approximate/base.py
-drwxr-xr-x   0 thomaslux   (501) staff       (20)        0 2022-03-20 17:38:43.303461 tlux-0.0.8/tlux/approximate/delaunay/
--rw-r--r--   0 thomaslux   (501) staff       (20)      814 2022-02-13 17:59:33.000000 tlux-0.0.8/tlux/approximate/delaunay/__init__.py
--rwxr-xr-x   0 thomaslux   (501) staff       (20)    62855 2022-02-13 17:31:00.000000 tlux-0.0.8/tlux/approximate/delaunay/blas.f
--rw-r--r--   0 thomaslux   (501) staff       (20)     3566 2022-02-13 17:54:30.000000 tlux-0.0.8/tlux/approximate/delaunay/delfort.py
-drwxr-xr-x   0 thomaslux   (501) staff       (20)        0 2022-03-20 17:38:43.315104 tlux-0.0.8/tlux/approximate/delaunay/delsparse/
--rw-r--r--   0 thomaslux   (501) staff       (20)    39995 2022-02-13 17:44:52.000000 tlux-0.0.8/tlux/approximate/delaunay/delsparse/__init__.py
--rw-r--r--   0 thomaslux   (501) staff       (20)     1081 2022-02-13 17:44:58.000000 tlux-0.0.8/tlux/approximate/delaunay/delsparse/c_delsparse_mod.mod
--rw-r--r--   0 thomaslux   (501) staff       (20)      320 2022-02-13 17:44:58.000000 tlux-0.0.8/tlux/approximate/delaunay/delsparse/c_real_precision.mod
--rw-r--r--   0 thomaslux   (501) staff       (20)   112928 2022-02-13 17:31:00.000000 tlux-0.0.8/tlux/approximate/delaunay/delsparse/delsparse.f90
--rwxr-xr-x   0 thomaslux   (501) staff       (20)   479304 2022-02-13 17:45:06.000000 tlux-0.0.8/tlux/approximate/delaunay/delsparse/delsparse.x86_64.so
--rw-r--r--   0 thomaslux   (501) staff       (20)   127062 2022-02-13 17:44:52.000000 tlux-0.0.8/tlux/approximate/delaunay/delsparse/delsparse_c_wrapper.f90
--rw-r--r--   0 thomaslux   (501) staff       (20)     1110 2022-02-13 17:44:33.000000 tlux-0.0.8/tlux/approximate/delaunay/delsparse/delsparse_mod.mod
--rw-r--r--   0 thomaslux   (501) staff       (20)    39995 2022-02-13 17:44:52.000000 tlux-0.0.8/tlux/approximate/delaunay/delsparse/delsparse_python_wrapper.py
--rw-r--r--   0 thomaslux   (501) staff       (20)      334 2022-02-13 17:44:33.000000 tlux-0.0.8/tlux/approximate/delaunay/delsparse/real_precision.mod
--rw-r--r--   0 thomaslux   (501) staff       (20)   174771 2022-02-13 17:31:00.000000 tlux-0.0.8/tlux/approximate/delaunay/delsparse/slatec.f
--rw-r--r--   0 thomaslux   (501) staff       (20)   112928 2022-02-13 17:31:00.000000 tlux-0.0.8/tlux/approximate/delaunay/delsparse.f90
--rwxr-xr-x   0 thomaslux   (501) staff       (20)   529450 2022-02-13 17:31:22.000000 tlux-0.0.8/tlux/approximate/delaunay/lapack.f
--rw-r--r--   0 thomaslux   (501) staff       (20)     3517 2022-02-13 17:58:43.000000 tlux-0.0.8/tlux/approximate/delaunay/qhull.py
--rw-r--r--   0 thomaslux   (501) staff       (20)   174771 2022-02-13 17:31:00.000000 tlux-0.0.8/tlux/approximate/delaunay/slatec.f
--rw-r--r--   0 thomaslux   (501) staff       (20)     1380 2022-02-13 22:23:55.000000 tlux-0.0.8/tlux/approximate/nearest_neighbor.py
-drwxr-xr-x   0 thomaslux   (501) staff       (20)        0 2022-03-20 17:38:43.319028 tlux-0.0.8/tlux/math/
--rw-r--r--   0 thomaslux   (501) staff       (20)     2922 2022-03-20 17:31:42.000000 tlux-0.0.8/tlux/math/__init__.py
--rw-r--r--   0 thomaslux   (501) staff       (20)     1069 2022-03-01 23:22:59.000000 tlux-0.0.8/tlux/math/fast_sort.mod
--rw-r--r--   0 thomaslux   (501) staff       (20)     3812 2022-03-15 02:53:05.000000 tlux-0.0.8/tlux/math/fmath.f90
--rw-r--r--   0 thomaslux   (501) staff       (20)    13459 2022-03-11 04:51:36.000000 tlux-0.0.8/tlux/math/fraction.py
--rw-r--r--   0 thomaslux   (501) staff       (20)    16342 2022-03-01 23:27:01.000000 tlux-0.0.8/tlux/math/fsort.f90
--rw-r--r--   0 thomaslux   (501) staff       (20)    31098 2022-03-11 05:00:30.000000 tlux-0.0.8/tlux/math/polynomial.py
--rw-r--r--   0 thomaslux   (501) staff       (20)    96001 2022-02-13 23:30:50.000000 tlux-0.0.8/tlux/plot.py
--rw-r--r--   0 thomaslux   (501) staff       (20)     5087 2022-03-12 15:43:35.000000 tlux-0.0.8/tlux/random.py
--rw-r--r--   0 thomaslux   (501) staff       (20)     3172 2022-02-06 16:47:11.000000 tlux-0.0.8/tlux/readme.md
--rw-r--r--   0 thomaslux   (501) staff       (20)      403 2022-03-20 17:31:25.000000 tlux-0.0.8/tlux/setup.py
-drwxr-xr-x   0 thomaslux   (501) staff       (20)        0 2022-03-20 17:38:43.272485 tlux-0.0.8/tlux.egg-info/
--rw-r--r--   0 thomaslux   (501) staff       (20)      525 2022-03-20 17:38:43.000000 tlux-0.0.8/tlux.egg-info/PKG-INFO
--rw-r--r--   0 thomaslux   (501) staff       (20)     2067 2022-03-20 17:38:43.000000 tlux-0.0.8/tlux.egg-info/SOURCES.txt
--rw-r--r--   0 thomaslux   (501) staff       (20)        1 2022-03-20 17:38:43.000000 tlux-0.0.8/tlux.egg-info/dependency_links.txt
--rw-r--r--   0 thomaslux   (501) staff       (20)       42 2022-03-20 17:38:43.000000 tlux-0.0.8/tlux.egg-info/requires.txt
--rw-r--r--   0 thomaslux   (501) staff       (20)        5 2022-03-20 17:38:43.000000 tlux-0.0.8/tlux.egg-info/top_level.txt
+drwxr-xr-x   0 thomaslux   (501) staff       (20)        0 2022-03-30 15:57:31.776912 tlux-0.0.9/
+-rw-r--r--   0 thomaslux   (501) staff       (20)       25 2022-03-30 15:57:28.000000 tlux-0.0.9/MANIFEST.in
+-rw-r--r--   0 thomaslux   (501) staff       (20)      525 2022-03-30 15:57:31.776985 tlux-0.0.9/PKG-INFO
+-rw-r--r--   0 thomaslux   (501) staff       (20)      108 2022-03-30 15:57:31.777227 tlux-0.0.9/setup.cfg
+-rw-r--r--   0 thomaslux   (501) staff       (20)     2864 2022-03-18 19:21:28.000000 tlux-0.0.9/setup.py
+drwxr-xr-x   0 thomaslux   (501) staff       (20)        0 2022-03-30 15:57:31.763099 tlux-0.0.9/tlux/
+-rw-r--r--   0 thomaslux   (501) staff       (20)      247 2022-03-18 19:21:28.000000 tlux-0.0.9/tlux/__init__.py
+-rw-r--r--   0 thomaslux   (501) staff       (20)      334 2022-03-18 19:21:28.000000 tlux-0.0.9/tlux/__main__.py
+drwxr-xr-x   0 thomaslux   (501) staff       (20)        0 2022-03-30 15:57:31.764930 tlux-0.0.9/tlux/about/
+-rw-r--r--   0 thomaslux   (501) staff       (20)       47 2022-03-18 19:21:28.000000 tlux-0.0.9/tlux/about/author.txt
+-rw-r--r--   0 thomaslux   (501) staff       (20)      139 2022-03-18 19:21:28.000000 tlux-0.0.9/tlux/about/classifiers.txt
+-rw-r--r--   0 thomaslux   (501) staff       (20)       11 2022-03-18 19:21:28.000000 tlux-0.0.9/tlux/about/description.txt
+-rw-r--r--   0 thomaslux   (501) staff       (20)       15 2022-03-18 19:21:28.000000 tlux-0.0.9/tlux/about/keywords.txt
+-rw-r--r--   0 thomaslux   (501) staff       (20)        5 2022-03-18 19:21:28.000000 tlux-0.0.9/tlux/about/on_pypi.txt
+-rw-r--r--   0 thomaslux   (501) staff       (20)        5 2022-03-18 19:21:28.000000 tlux-0.0.9/tlux/about/package_name.txt
+-rw-r--r--   0 thomaslux   (501) staff       (20)       42 2022-03-18 19:21:28.000000 tlux-0.0.9/tlux/about/requirements.txt
+-rw-r--r--   0 thomaslux   (501) staff       (20)        6 2022-03-21 03:54:13.000000 tlux-0.0.9/tlux/about/version.txt
+-rw-r--r--   0 thomaslux   (501) staff       (20)     1233 2022-03-30 15:57:28.000000 tlux-0.0.9/tlux/about/version_history.md
+drwxr-xr-x   0 thomaslux   (501) staff       (20)        0 2022-03-30 15:57:31.765387 tlux-0.0.9/tlux/approximate/
+drwxr-xr-x   0 thomaslux   (501) staff       (20)        0 2022-03-30 15:57:31.766636 tlux-0.0.9/tlux/approximate/apos/
+-rw-r--r--   0 thomaslux   (501) staff       (20)        4 2022-03-21 03:54:13.000000 tlux-0.0.9/tlux/approximate/apos/.gitignore
+-rw-r--r--   0 thomaslux   (501) staff       (20)    34212 2022-03-30 15:56:55.000000 tlux-0.0.9/tlux/approximate/apos/__init__.py
+drwxr-xr-x   0 thomaslux   (501) staff       (20)        0 2022-03-30 15:57:31.768919 tlux-0.0.9/tlux/approximate/apos/apos/
+-rw-r--r--   0 thomaslux   (501) staff       (20)    92751 2022-03-30 15:52:34.000000 tlux-0.0.9/tlux/approximate/apos/apos/__init__.py
+-rwxr-xr-x   0 thomaslux   (501) staff       (20)   303146 2022-03-30 15:52:40.000000 tlux-0.0.9/tlux/approximate/apos/apos/apos.arm64.so
+-rw-r--r--   0 thomaslux   (501) staff       (20)   102753 2022-03-30 15:56:55.000000 tlux-0.0.9/tlux/approximate/apos/apos/apos.f90
+-rw-r--r--   0 thomaslux   (501) staff       (20)     4951 2022-03-30 15:52:25.000000 tlux-0.0.9/tlux/approximate/apos/apos/apos.mod
+-rw-r--r--   0 thomaslux   (501) staff       (20)   270441 2022-03-30 15:52:34.000000 tlux-0.0.9/tlux/approximate/apos/apos/apos_c_wrapper.f90
+-rw-r--r--   0 thomaslux   (501) staff       (20)    92751 2022-03-30 15:52:34.000000 tlux-0.0.9/tlux/approximate/apos/apos/apos_python_wrapper.py
+-rw-r--r--   0 thomaslux   (501) staff       (20)    11161 2022-03-30 15:52:39.000000 tlux-0.0.9/tlux/approximate/apos/apos/c_apos.mod
+-rw-r--r--   0 thomaslux   (501) staff       (20)     1489 2022-03-30 15:52:38.000000 tlux-0.0.9/tlux/approximate/apos/apos/c_matrix_operations.mod
+-rw-r--r--   0 thomaslux   (501) staff       (20)      965 2022-03-30 15:52:38.000000 tlux-0.0.9/tlux/approximate/apos/apos/c_sort_and_select.mod
+-rw-r--r--   0 thomaslux   (501) staff       (20)     1309 2022-03-30 15:52:25.000000 tlux-0.0.9/tlux/approximate/apos/apos/matrix_operations.mod
+-rw-r--r--   0 thomaslux   (501) staff       (20)      820 2022-03-24 17:40:40.000000 tlux-0.0.9/tlux/approximate/apos/apos/sort_and_select.mod
+-rw-r--r--   0 thomaslux   (501) staff       (20)   102753 2022-03-30 15:56:55.000000 tlux-0.0.9/tlux/approximate/apos/apos.f90
+-rw-r--r--   0 thomaslux   (501) staff       (20)     4951 2022-03-30 15:43:37.000000 tlux-0.0.9/tlux/approximate/apos/apos.mod
+-rw-r--r--   0 thomaslux   (501) staff       (20)     1321 2022-03-30 10:22:19.000000 tlux-0.0.9/tlux/approximate/apos/matrix_operations.mod
+-rw-r--r--   0 thomaslux   (501) staff       (20)      820 2022-03-24 17:40:40.000000 tlux-0.0.9/tlux/approximate/apos/sort_and_select.mod
+drwxr-xr-x   0 thomaslux   (501) staff       (20)        0 2022-03-30 15:57:31.769560 tlux-0.0.9/tlux/approximate/apos/test/
+-rw-r--r--   0 thomaslux   (501) staff       (20)     5244 2022-03-18 19:21:28.000000 tlux-0.0.9/tlux/approximate/apos/test/argselect.f90
+-rw-r--r--   0 thomaslux   (501) staff       (20)      418 2022-03-18 19:21:28.000000 tlux-0.0.9/tlux/approximate/apos/test/test_argselect.py
+-rw-r--r--   0 thomaslux   (501) staff       (20)     7812 2022-03-30 15:56:55.000000 tlux-0.0.9/tlux/approximate/apos/test/test_argsort.f90
+-rw-r--r--   0 thomaslux   (501) staff       (20)      568 2022-03-30 15:56:55.000000 tlux-0.0.9/tlux/approximate/apos/test/test_clock.f90
+-rw-r--r--   0 thomaslux   (501) staff       (20)     6926 2022-03-18 19:21:28.000000 tlux-0.0.9/tlux/approximate/base.py
+drwxr-xr-x   0 thomaslux   (501) staff       (20)        0 2022-03-30 15:57:31.772123 tlux-0.0.9/tlux/approximate/delaunay/
+-rw-r--r--   0 thomaslux   (501) staff       (20)      814 2022-03-18 19:21:28.000000 tlux-0.0.9/tlux/approximate/delaunay/__init__.py
+-rwxr-xr-x   0 thomaslux   (501) staff       (20)    62855 2022-03-18 19:21:28.000000 tlux-0.0.9/tlux/approximate/delaunay/blas.f
+-rw-r--r--   0 thomaslux   (501) staff       (20)     3566 2022-03-18 19:21:28.000000 tlux-0.0.9/tlux/approximate/delaunay/delfort.py
+drwxr-xr-x   0 thomaslux   (501) staff       (20)        0 2022-03-30 15:57:31.775337 tlux-0.0.9/tlux/approximate/delaunay/delsparse/
+-rw-r--r--   0 thomaslux   (501) staff       (20)    39995 2022-03-18 19:21:28.000000 tlux-0.0.9/tlux/approximate/delaunay/delsparse/__init__.py
+-rw-r--r--   0 thomaslux   (501) staff       (20)   112928 2022-03-18 19:21:28.000000 tlux-0.0.9/tlux/approximate/delaunay/delsparse/delsparse.f90
+-rwxr-xr-x   0 thomaslux   (501) staff       (20)   479304 2022-03-18 19:21:28.000000 tlux-0.0.9/tlux/approximate/delaunay/delsparse/delsparse.x86_64.so
+-rw-r--r--   0 thomaslux   (501) staff       (20)   127062 2022-03-18 19:21:28.000000 tlux-0.0.9/tlux/approximate/delaunay/delsparse/delsparse_c_wrapper.f90
+-rw-r--r--   0 thomaslux   (501) staff       (20)    39995 2022-03-18 19:21:28.000000 tlux-0.0.9/tlux/approximate/delaunay/delsparse/delsparse_python_wrapper.py
+-rw-r--r--   0 thomaslux   (501) staff       (20)   174771 2022-03-18 19:21:28.000000 tlux-0.0.9/tlux/approximate/delaunay/delsparse/slatec.f
+-rw-r--r--   0 thomaslux   (501) staff       (20)   112928 2022-03-18 19:21:28.000000 tlux-0.0.9/tlux/approximate/delaunay/delsparse.f90
+-rwxr-xr-x   0 thomaslux   (501) staff       (20)   529450 2022-03-18 19:21:28.000000 tlux-0.0.9/tlux/approximate/delaunay/lapack.f
+-rw-r--r--   0 thomaslux   (501) staff       (20)     3517 2022-03-18 19:21:28.000000 tlux-0.0.9/tlux/approximate/delaunay/qhull.py
+-rw-r--r--   0 thomaslux   (501) staff       (20)   174771 2022-03-18 19:21:28.000000 tlux-0.0.9/tlux/approximate/delaunay/slatec.f
+-rw-r--r--   0 thomaslux   (501) staff       (20)     1380 2022-03-18 19:21:28.000000 tlux-0.0.9/tlux/approximate/nearest_neighbor.py
+drwxr-xr-x   0 thomaslux   (501) staff       (20)        0 2022-03-30 15:57:31.776696 tlux-0.0.9/tlux/math/
+-rw-r--r--   0 thomaslux   (501) staff       (20)        6 2022-03-21 03:54:13.000000 tlux-0.0.9/tlux/math/.gitignore
+-rw-r--r--   0 thomaslux   (501) staff       (20)     2922 2022-03-21 03:54:13.000000 tlux-0.0.9/tlux/math/__init__.py
+-rw-r--r--   0 thomaslux   (501) staff       (20)     3812 2022-03-21 03:54:13.000000 tlux-0.0.9/tlux/math/fmath.f90
+-rw-r--r--   0 thomaslux   (501) staff       (20)    13459 2022-03-18 19:21:28.000000 tlux-0.0.9/tlux/math/fraction.py
+-rw-r--r--   0 thomaslux   (501) staff       (20)    16342 2022-03-18 19:21:28.000000 tlux-0.0.9/tlux/math/fsort.f90
+-rw-r--r--   0 thomaslux   (501) staff       (20)    31098 2022-03-18 19:21:28.000000 tlux-0.0.9/tlux/math/polynomial.py
+-rw-r--r--   0 thomaslux   (501) staff       (20)    96001 2022-03-18 19:21:28.000000 tlux-0.0.9/tlux/plot.py
+-rw-r--r--   0 thomaslux   (501) staff       (20)     5087 2022-03-18 19:21:28.000000 tlux-0.0.9/tlux/random.py
+-rw-r--r--   0 thomaslux   (501) staff       (20)     3172 2022-03-18 19:21:28.000000 tlux-0.0.9/tlux/readme.md
+-rw-r--r--   0 thomaslux   (501) staff       (20)      619 2022-03-21 03:54:13.000000 tlux-0.0.9/tlux/setup.py
+drwxr-xr-x   0 thomaslux   (501) staff       (20)        0 2022-03-30 15:57:31.763860 tlux-0.0.9/tlux.egg-info/
+-rw-r--r--   0 thomaslux   (501) staff       (20)      525 2022-03-30 15:57:31.000000 tlux-0.0.9/tlux.egg-info/PKG-INFO
+-rw-r--r--   0 thomaslux   (501) staff       (20)     2128 2022-03-30 15:57:31.000000 tlux-0.0.9/tlux.egg-info/SOURCES.txt
+-rw-r--r--   0 thomaslux   (501) staff       (20)        1 2022-03-30 15:57:31.000000 tlux-0.0.9/tlux.egg-info/dependency_links.txt
+-rw-r--r--   0 thomaslux   (501) staff       (20)       42 2022-03-30 15:57:31.000000 tlux-0.0.9/tlux.egg-info/requires.txt
+-rw-r--r--   0 thomaslux   (501) staff       (20)        5 2022-03-30 15:57:31.000000 tlux-0.0.9/tlux.egg-info/top_level.txt
```

### Comparing `tlux-0.0.8/PKG-INFO` & `tlux-0.0.9/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,16 +1,16 @@
 Metadata-Version: 1.2
 Name: tlux
-Version: 0.0.8
+Version: 0.0.9
 Summary: A package.
 Home-page: https://github.com/tchlux/tlux
 Author: Thomas C.H. Lux
 Author-email: thomas.ch.lux@gmail.com
 License: MIT
-Download-URL: https://github.com/tchlux/tlux/archive/0.0.8.tar.gz
+Download-URL: https://github.com/tchlux/tlux/archive/0.0.9.tar.gz
 Description: UNKNOWN
 Keywords: python,python3
 Platform: UNKNOWN
 Classifier: Development Status :: 3 - Alpha
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
```

### Comparing `tlux-0.0.8/setup.py` & `tlux-0.0.9/setup.py`

 * *Files identical despite different names*

### Comparing `tlux-0.0.8/tlux/about/version_history.md` & `tlux-0.0.9/tlux/about/version_history.md`

 * *Files 10% similar despite different names*

```diff
@@ -8,7 +8,8 @@
 | 0.0.2<br>February 2022 | Fixing pip install errors. |
 | 0.0.3<br>February 2022 | Added well spaced random designs over the box and <br> ball. |
 | 0.0.4<br>February 2022 | Added 'approximate' and support for generic surface <br> points in 'Plot.add_function'. |
 | 0.0.5<br>March 2022 | APOS model added to library. |
 | 0.0.6<br>March 2022 | Added math library utilities, included update ratio <br> in APOS model training record. |
 | 0.0.7<br>March 2022 | Added missing import to random box function. |
 | 0.0.8<br>March 2022 | Updating setup script to attempt Fortran compilation <br> early. |
+| 0.0.9<br>March 2022 | Updated memory layout and incorporated SVD into data <br> normalization. Modified adaptive parameter update to <br> use a sliding linear number of parameters instead of <br> the binary search protocol. |
```

### Comparing `tlux-0.0.8/tlux/approximate/apos/__init__.py` & `tlux-0.0.9/tlux/approximate/apos/__init__.py`

 * *Files 8% similar despite different names*

```diff
@@ -8,154 +8,174 @@
     # Make the string function return the unpacked model.
     def __str__(self): return str(self.model_unpacked())
 
     # Initialize a new APOS model.
     def __init__(self, **kwargs):
         try:
             import fmodpy
-            # f_compiler_args = "-fPIC -shared -O3 -lblas -llapack -fopenmp -fcheck=bounds"
+            f_compiler_args = "-fPIC -shared -O3 -lblas -llapack -fopenmp -fcheck=bounds"
             apos = fmodpy.fimport(_source_code, blas=True,
                                   lapack=True, omp=True, wrap=True,
                                   verbose=False, output_dir=_this_dir,
-                                  # f_compiler_args=f_compiler_args)
+                                  f_compiler_args=f_compiler_args,
             )
             # Store the Fortran module as an attribute.
             self.APOS = apos.apos
         except:
             # TODO:
             #  - python fallback that supports the basic evaluation of
             #    a model (but no support for training new models).
             raise(NotImplementedError("The Fortran source was not loaded successfully."))
         # Set defaults for standard internal parameters.
         self.steps = 1000
         self.seed = None
+        self.num_threads = None
         self.config = None
         self.model = np.zeros(0, dtype="float32")
         self.record = np.zeros(0, dtype="float32")
         # Default descriptors for categorical inputs.
-        self.xi_map = []
-        self.xi_sizes = []
-        self.xi_starts = []
         self.axi_map = []
         self.axi_sizes = []
         self.axi_starts = []
+        self.xi_map = []
+        self.xi_sizes = []
+        self.xi_starts = []
         self.yi_map = []
         self.yi_sizes = []
         self.yi_starts = []
         # Initialize the attributes of the model that can be initialized.
         self._init_model(**kwargs)
 
 
     # Initialize a model, if possible.
     def _init_model(self, **kwargs):
-        # Model parameters.
-        mdi = kwargs.pop("mdi", None)
-        mdo = kwargs.pop("mdo", None)
-        mds = kwargs.pop("mds", None)
-        mns = kwargs.pop("mns", None)
-        mde = kwargs.pop("mde", None)
-        mne = kwargs.pop("mne", None)
         # Apositional model parameters.
-        adi = kwargs.pop("adi", 0)
+        adn = kwargs.pop("adn", 0)
         ado = kwargs.pop("ado", None)
         ads = kwargs.pop("ads", None)
         ans = kwargs.pop("ans", None)
         ade = kwargs.pop("ade", None)
         ane = kwargs.pop("ane", None)
+        # Model parameters.
+        mdn = kwargs.pop("mdn", None)
+        mdo = kwargs.pop("mdo", None)
+        mds = kwargs.pop("mds", None)
+        mns = kwargs.pop("mns", None)
+        mde = kwargs.pop("mde", None)
+        mne = kwargs.pop("mne", None)
         # Number of threads.
-        num_threads = kwargs.pop("num_threads", None)
+        self.num_threads = kwargs.pop("num_threads", self.num_threads)
         self.seed = kwargs.pop("seed", self.seed)
         self.steps = kwargs.pop("steps", self.steps)
         # Initialize if enough arguments were provided.
-        if (None not in {mdi, mdo, adi}):
+        if (None not in {adn, mdn, mdo}):
             self.config = self.APOS.new_model_config(
-                mdi=mdi, mdo=mdo, mds=mds, mns=mns, mne=mne, mde=mde,
-                adi=adi, ado=ado, ads=ads, ans=ans, ane=ane, ade=ade,
-                num_threads=num_threads)
+                adn=adn, ado=ado, ads=ads, ans=ans, ane=ane, ade=ade,
+                mdn=mdn, mdo=mdo, mds=mds, mns=mns, mne=mne, mde=mde,
+                num_threads=self.num_threads)
             # Set any configuration keyword arguments given at initialization
             #  that were not passed to "new_model_config".
             for n in ({n for (n,t) in self.config._fields_} & set(kwargs)):
                 setattr(self.config, n, kwargs[n])
             # Set all internal arrays and initialize the model.
             self.model = np.zeros(self.config.total_size, dtype="float32")
             self.APOS.init_model(self.config, self.model, seed=self.seed)
 
 
+    # Generate the string containing all the configuration information for this model.
+    def config_str(self):
+        s = ""
+        max_n_len = max(map(len,(n for (n,t) in self.config._fields_)))
+        max_t_len = max(map(len,(str(t).split("'")[1].split('.')[1]
+                                 for (n,t) in self.config._fields_)))
+        for (n,t) in self.config._fields_:
+            t = str(t).split("'")[1].split('.')[1]
+            s += f"  {str(t):{max_t_len}s}  {n:{max_n_len}s}  =  {getattr(self.config,n)}\n"
+        return s
+
+
     # Unpack the model (which is in one array) into it's constituent parts.
     def model_unpacked(self):
         # If there is no model or configuration, return None.
         if (self.config is None) or (self.model is None):
             return None
         # Build a class that contains pointers to the model internals.
-        class ModelUnpacked:
+        class AposModel:
             config = self.config
             model  = self.model
-            m_embeddings   = self.model[self.config.msev-1:self.config.meev].reshape(self.config.mde, self.config.mne, order="F")
-            m_input_vecs   = self.model[self.config.msiv-1:self.config.meiv].reshape(self.config.mdi, self.config.mds, order="F")
-            m_input_shift  = self.model[self.config.msis-1:self.config.meis].reshape(self.config.mds, order="F")
-            m_state_vecs   = self.model[self.config.mssv-1:self.config.mesv].reshape(self.config.mds, self.config.mds, max(0,self.config.mns-1), order="F")
-            m_state_shift  = self.model[self.config.msss-1:self.config.mess].reshape(self.config.mds, self.config.mns-1, order="F")
-            m_output_vecs  = self.model[self.config.msov-1:self.config.meov].reshape(self.config.mds, self.config.mdo, order="F")
-            a_embeddings   = self.model[self.config.asev-1:self.config.aeev].reshape(self.config.ade, self.config.ane, order="F")
-            a_input_vecs   = self.model[self.config.asiv-1:self.config.aeiv].reshape(self.config.adi, self.config.ads, order="F")
-            a_input_shift  = self.model[self.config.asis-1:self.config.aeis].reshape(self.config.ads, order="F")
-            a_state_vecs   = self.model[self.config.assv-1:self.config.aesv].reshape(self.config.ads, self.config.ads, max(0,self.config.ans-1), order="F")
-            a_state_shift  = self.model[self.config.asss-1:self.config.aess].reshape(self.config.ads, max(0,self.config.ans-1), order="F")
-            a_output_vecs  = self.model[self.config.asov-1:self.config.aeov].reshape(self.config.ads, self.config.ado, order="F")
+            a_embeddings  = self.model[self.config.asev-1:self.config.aeev].reshape(self.config.ade, self.config.ane, order="F")
+            a_input_vecs  = self.model[self.config.asiv-1:self.config.aeiv].reshape(self.config.adi, self.config.ads, order="F")
+            a_input_shift = self.model[self.config.asis-1:self.config.aeis].reshape(self.config.ads, order="F")
+            a_state_vecs  = self.model[self.config.assv-1:self.config.aesv].reshape(self.config.ads, self.config.ads, max(0,self.config.ans-1), order="F")
+            a_state_shift = self.model[self.config.asss-1:self.config.aess].reshape(self.config.ads, max(0,self.config.ans-1), order="F")
+            a_output_vecs = self.model[self.config.asov-1:self.config.aeov].reshape(self.config.ads, self.config.ado, order="F")
+            m_embeddings  = self.model[self.config.msev-1:self.config.meev].reshape(self.config.mde, self.config.mne, order="F")
+            m_input_vecs  = self.model[self.config.msiv-1:self.config.meiv].reshape(self.config.mdi, self.config.mds, order="F")
+            m_input_shift = self.model[self.config.msis-1:self.config.meis].reshape(self.config.mds, order="F")
+            m_state_vecs  = self.model[self.config.mssv-1:self.config.mesv].reshape(self.config.mds, self.config.mds, max(0,self.config.mns-1), order="F")
+            m_state_shift = self.model[self.config.msss-1:self.config.mess].reshape(self.config.mds, self.config.mns-1, order="F")
+            m_output_vecs = self.model[self.config.msov-1:self.config.meov].reshape(self.config.mds, self.config.mdo, order="F")
 
             def __getitem__(self, *args, **kwargs):
                 return getattr(self, *args, **kwargs)
             def __str__(self, vecs=False):
+                # A function for creating a byte-size string from an integer.
+                def _byte_str(byte_size):
+                    if (byte_size < 2**10):
+                        byte_size = f"{byte_size} bytes"
+                    elif (byte_size < 2**20):
+                        byte_size = f"{byte_size//2**10:.1f}KB"
+                    elif (byte_size < 2**30):
+                        byte_size = f"{byte_size//2**20:.1f}MB"
+                    else:
+                        byte_size = f"{byte_size//2**30:.1f}GB"
+                    return byte_size
                 # Calculate the byte size of this model (excluding python descriptors).
                 byte_size = len(self.config._fields_)*4 + self.model.dtype.itemsize*self.model.size
-                if (byte_size < 2**10):
-                    byte_size = f"{byte_size} bytes"
-                elif (byte_size < 2**20):
-                    byte_size = f"{byte_size//2**10:.1f}KB"
-                elif (byte_size < 2**30):
-                    byte_size = f"{byte_size//2**20:.1f}MB"
-                else:
-                    byte_size = f"{byte_size//2**30:.1f}GB"
+                byte_size = _byte_str(byte_size)
+                if (self.config.rwork_size+self.config.iwork_size > 0):
+                    work_size = self.config.rwork_size*4 + self.config.iwork_size*4
+                    byte_size += " + "+_byte_str(work_size)+" work space"
                 # Create a function that prints the actual contents of the arrays.
                 if vecs: to_str = lambda arr: "\n    " + "\n    ".join(str(arr).split("\n")) + "\n"
                 else:    to_str = lambda arr: "\n"
                 # Provide details (and some values where possible).
                 return (
                     f"APOS model ({self.config.total_size} parameters) [{byte_size}]\n"+
                      " apositional model\n"+
-                    f"  input dimension  {self.config.adi}\n"+
+                    f"  input dimension  {self.config.adn}\n"+
                     f"  output dimension {self.config.ado}\n"+
                     f"  state dimension  {self.config.ads}\n"+
                     f"  number of states {self.config.ans}\n"+
                    (f"  embedding dimension  {self.config.ade}\n"+
                     f"  number of embeddings {self.config.ane}\n"
                      if self.config.ane > 0 else "")+
                     f"  embeddings   {self.a_embeddings.shape}  "+to_str(self.a_embeddings)+
                     f"  input vecs   {self.a_input_vecs.shape}  "+to_str(self.a_input_vecs)+
                     f"  input shift  {self.a_input_shift.shape} "+to_str(self.a_input_shift)+
                     f"  state vecs   {self.a_state_vecs.shape}  "+to_str(self.a_state_vecs)+
                     f"  state shift  {self.a_state_shift.shape} "+to_str(self.a_state_shift)+
                     f"  output vecs  {self.a_output_vecs.shape} "+to_str(self.a_output_vecs)+
                      "\n"+
                      " positional model\n"+
-                    f"  input dimension  {self.config.mdi}\n"+
+                    f"  input dimension  {self.config.mdn}\n"+
                     f"  output dimension {self.config.mdo}\n"+
                     f"  state dimension  {self.config.mds}\n"+
                     f"  number of states {self.config.mns}\n"+
                    (f"  embedding dimension  {self.config.mde}\n"+
                     f"  number of embeddings {self.config.mne}\n"
                      if self.config.mne > 0 else "")+
                     f"  embeddings   {self.m_embeddings.shape}  "+to_str(self.m_embeddings)+
                     f"  input vecs   {self.m_input_vecs.shape}  "+to_str(self.m_input_vecs)+
                     f"  input shift  {self.m_input_shift.shape} "+to_str(self.m_input_shift)+
                     f"  state vecs   {self.m_state_vecs.shape}  "+to_str(self.m_state_vecs)+
                     f"  state shift  {self.m_state_shift.shape} "+to_str(self.m_state_shift)+
                     f"  output vecs  {self.m_output_vecs.shape} "+to_str(self.m_output_vecs)
                 )
-        return ModelUnpacked()
+        return AposModel()
 
 
     # Given a categorical input array, construct a dictionary for
     #  mapping the unique values in the columns of the array to integers.
     def _i_map(self, xi):
         if (len(xi.dtype) > 0):
             xi_map = [np.unique(xi[n]) for n in xi.dtype.names]
@@ -188,35 +208,35 @@
             _xi[:,i] = val_indices[eq_val]
         return _xi
 
 
     # Convert all inputs to the APOS model into the expected numpy format.
     def _to_array(self, y, yi, x, xi, ax, axi, sizes):
         # Get the number of inputs.
-        if   (y  is not None): mn = len(y)
-        elif (yi is not None): mn = len(yi)
-        elif (x  is not None): mn = len(x)
-        elif (xi is not None): mn = len(xi)
-        elif (sizes is not None): mn = len(sizes)
+        if   (y  is not None): nm = len(y)
+        elif (yi is not None): nm = len(yi)
+        elif (x  is not None): nm = len(x)
+        elif (xi is not None): nm = len(xi)
+        elif (sizes is not None): nm = len(sizes)
         # Make sure that all inputs are numpy arrays.
         if (y is not None):  y = np.asarray(y, dtype="float32", order="C")
-        else:                y = np.zeros((mn,0), dtype="float32", order="C") 
+        else:                y = np.zeros((nm,0), dtype="float32", order="C") 
         if (yi is not None): yi = np.asarray(yi)
-        else:                yi = np.zeros((mn,0), dtype="int32", order="C")
+        else:                yi = np.zeros((nm,0), dtype="int32", order="C")
         if (x is not None): x = np.asarray(x, dtype="float32", order="C")
-        else:               x = np.zeros((mn,0), dtype="float32", order="C")
+        else:               x = np.zeros((nm,0), dtype="float32", order="C")
         if (xi is not None): xi = np.asarray(xi)
-        else:                xi = np.zeros((mn,0), dtype="int32", order="C")
+        else:                xi = np.zeros((nm,0), dtype="int32", order="C")
         if (sizes is not None): sizes = np.asarray(sizes, dtype="int32")
         else:                   sizes = np.zeros(0, dtype="int32")
-        an = sizes.sum()
+        na = sizes.sum()
         if (ax is not None): ax = np.asarray(ax, dtype="float32", order="C")
-        else:                ax = np.zeros((an,0), dtype="float32", order="C")
+        else:                ax = np.zeros((na,0), dtype="float32", order="C")
         if (axi is not None): axi = np.asarray(axi)
-        else:                 axi = np.zeros((an,0), dtype="int32", order="C")
+        else:                 axi = np.zeros((na,0), dtype="int32", order="C")
         # Make sure that all inputs have the expected shape.
         assert (len(y.shape) in {1,2}), f"Bad y shape {y.shape}, should be 1D or 2D matrix."
         assert (len(yi.shape) in {1,2}), f"Bad yi shape {yi.shape}, should be 1D or 2D matrix."
         assert (len(x.shape) in {1,2}), f"Bad x shape {x.shape}, should be 1D or 2D matrix."
         assert (len(xi.shape) in {1,2}), f"Bad xi shape {xi.shape}, should be 1D or 2D matrix."
         assert (len(ax.shape) in {1,2}), f"Bad ax shape {ax.shape}, should be 1D or 2D matrix."
         assert (len(axi.shape) in {1,2}), f"Bad axi shape {axi.shape}, should be 1D or 2D matrix."
@@ -225,16 +245,16 @@
         if (len(y.shape) == 1): y = y.reshape((-1,1))
         if (len(yi.shape) == 1) and (len(yi.dtype) == 0): yi = yi.reshape((-1,1))
         if (len(x.shape) == 1): x = x.reshape((-1,1))
         if (len(xi.shape) == 1) and (len(xi.dtype) == 0): xi = xi.reshape((-1,1))
         if (len(ax.shape) == 1): ax = ax.reshape((-1,1))
         if ((len(axi.shape) == 1) and (len(axi.dtype) == 0)): axi = axi.reshape((-1,1))
         mdo = y.shape[1]
-        mdi = x.shape[1]
-        adi = ax.shape[1]
+        mdn = x.shape[1]
+        adn = ax.shape[1]
         # Handle mapping "xi" into integer encodings.
         xi_cols = len(xi.dtype) or xi.shape[1]
         if (xi_cols > 0):
             if (len(self.xi_map) == 0):
                 self.xi_map, self.xi_sizes, self.xi_starts = self._i_map(xi)
             else:
                 assert (xi_cols == len(self.xi_map)), f"Bad number of columns in 'xi', {xi_cols}, expected {len(self.xi_map)} columns."
@@ -262,77 +282,81 @@
             yne = sum(self.yi_sizes)
         else: yne = 0
         # Handle mapping integer encoded "yi" into a single real valued y.
         if (yne > 0):
             embedded = np.concatenate((
                 np.zeros((1,yne), dtype="float32"),
                 np.identity(yne, dtype="float32")), axis=0)
-            _y = np.zeros((mn, mdo+yne), dtype="float32")
+            _y = np.zeros((nm, mdo+yne), dtype="float32")
             _y[:,:mdo] = y[:,:]
             for i in range(yi.shape[1]):
                 _y[:,mdo:] += embedded[yi[:,i]]
             y = _y
             mdo += yne
         # Return all the shapes and numpy formatted inputs.
-        return mn, an, mdi, mne, mdo, adi, ane, yne, y, x, xi, ax, axi, sizes
+        return nm, na, mdn, mne, mdo, adn, ane, yne, y, x, xi, ax, axi, sizes
 
 
     # Fit this model.
     def fit(self, x=None, y=None, yi=None, xi=None, ax=None, axi=None,
             sizes=None, new_model=False, **kwargs):
         # Ensure that 'y' values were provided.
         assert ((y is not None) or (yi is not None)), "APOS.fit requires 'y' or 'yi' values, but neitherwere provided (use keyword argument 'y=<values>' or 'yi=<values>')."
         # Make sure that 'sizes' were provided for apositional (aggregate) inputs.
         if ((ax is not None) or (axi is not None)):
             assert (sizes is not None), "APOS.fit requires 'sizes' to be provided for apositional input sets (ax and axi)."
         # Get all inputs as arrays.
-        mn, an, mdi, mne, mdo, adi, ane, yne, y, x, xi, ax, axi, sizes = (
+        nm, na, mdn, mne, mdo, adn, ane, yne, y, x, xi, ax, axi, sizes = (
             self._to_array(y, yi, x, xi, ax, axi, sizes)
         )
-        # ------------------------------------------------------------
-        # If the shape of the model does not match the data, reinitialize.
-        check_shape = lambda: self.APOS.check_shape(self.config, self.model, y.T, x.T, xi.T, ax.T, axi.T, sizes)
-        if (new_model or (self.config is None) or (check_shape() != 0)):
-            # Store any existing configurations.
-            if (self.config is not None):
-                kwargs.update({
-                    "mne": kwargs.get("mne",self.config.mne),
-                    "mns": kwargs.get("mns",self.config.mns),
-                    "mds": kwargs.get("mds",self.config.mds),
-                    "ane": kwargs.get("ane",self.config.ane),
-                    "ans": kwargs.get("ans",self.config.ans),
-                    "ads": kwargs.get("ads",self.config.ads),
-                    "ado": kwargs.get("ado",self.config.ado),
-                })
-                import warnings
-                warnings.warn(f"Creating new model config because 'check_shape' failed. Only keeping sizes, dropping all custom configurations.")
+        # Configure this model if requested (or not already done).
+        if (new_model or (self.config is None)):
             # Ensure that the config is compatible with the data.
             kwargs.update({
-                "mdi":mdi,
-                "mdo":mdo,
-                "adi":adi,
+                "adn":adn,
                 "ane":max(ane, kwargs.get("ane",0)),
+                "mdn":mdn,
                 "mne":max(mne, kwargs.get("mne",0)),
+                "mdo":mdo,
             })
             self._init_model(**kwargs)
+        # If there are integer embeddings, expand "x" and "ax" to have space to hold those embeddings.
+        if (self.config.mde > 0) or (self.config.ado > 0):
+            _x = np.zeros((x.shape[0],self.config.mdi), dtype="float32", order="C")
+            _x[:,:x.shape[1]] = x
+            x, _x = _x, x
+        if (self.config.ade > 0):
+            _ax = np.zeros((ax.shape[0],ax.shape[1]+self.config.ade), dtype="float32", order="C")
+            _ax[:,:ax.shape[1]] = ax
+            ax, _ax = _ax, ax
+        # ------------------------------------------------------------
         # If a random seed is provided, then only 2 threads can be used
         #  because nondeterministic behavior comes from reordered addition.
         if (self.seed is not None):
             if (self.config.num_threads > 2):
                 import warnings
                 warnings.warn("Seeding an APOS model will deterministically initialize weights, but num_threads > 2 will result in a nondeterministic model fit.")
         # Get the number of steps for training.
         steps = kwargs.get("steps", self.steps)
         # ------------------------------------------------------------
+        # Set up new work space for this minimization process.
+        self.APOS.new_fit_config(nm, na, self.config)
+        rwork = np.zeros(self.config.rwork_size, dtype="float32")
+        iwork = np.zeros(self.config.iwork_size, dtype="int32")
         # Minimize the mean squared error.
-        self.record = np.zeros((steps,4), dtype="float32", order="C")
-        result = self.APOS.minimize_mse(self.config, self.model,
-                                        y.T, x.T, xi.T, ax.T, axi.T, sizes,
+        self.record = np.zeros((steps,6), dtype="float32", order="C")
+        result = self.APOS.minimize_mse(self.config, self.model, rwork, iwork,
+                                        ax.T, axi.T, sizes, x.T, xi.T, y.T, 
                                         steps=steps, record=self.record.T)
         assert (result[-1] == 0), f"APOS.minimize_mse returned nonzero exit code {result[-1]}."
+        # Copy the updated values back into the input arrays (for transparency).
+        if (self.config.mde > 0):
+            _x[:,:] = x[:,:_x.shape[1]]
+        if (self.config.ade > 0):
+            _ax[:,:] = ax[:,:_ax.shape[1]]
 
 
     # Calling this model is an alias for 'APOS.predict'.
     def __call__(self, *args, **kwargs):
         return self.predict(*args, **kwargs)
 
 
@@ -341,46 +365,54 @@
                 embedding=False, save_states=False, **kwargs):
         # Evaluate the model at all data.
         assert ((x is not None) or (xi is not None) or (sizes is not None)), "APOS.predict requires at least one of 'x', 'xi', or 'sizes' to not be None."
         # Make sure that 'sizes' were provided for apositional (aggregate) inputs.
         if ((ax is not None) or (axi is not None)):
             assert (sizes is not None), "APOS.predict requires 'sizes' to be provided for apositional input sets (ax and axi)."
         # Make sure that all inputs are numpy arrays.
-        mn, an, mdi, mne, mdo, adi, ane, yne, _, x, xi, ax, axi, sizes = (
+        nm, na, mdn, mne, mdo, adn, ane, yne, _, x, xi, ax, axi, sizes = (
             self._to_array(None, None, x, xi, ax, axi, sizes)
         )
         # Embed the inputs into the purely positional form.
         ade = self.config.ade
         ads = self.config.ads
         ado = self.config.ado
         mde = self.config.mde
         mds = self.config.mds
         mdo = self.config.mdo
         # Compute the true real-vector input dimensions given embeddings.
-        adi += ade
-        mdi += mde + ado
+        adn += ade
+        mdn += mde + ado
+        # ------------------------------------------------------------
         # Initialize storage for all arrays needed at evaluation time.
-        y = np.zeros((mn, mdo), dtype="float32", order="C")
-        xxi = np.zeros((mn, mdi), dtype="float32", order="C")
-        axxi = np.zeros((an, adi), dtype="float32", order="C")
+        #   If there are integer embeddings, expand "ax" and "x" to have
+        #   space to hold those embeddings.
+        if (self.config.ade > 0):
+            _ax = np.zeros((ax.shape[0],ax.shape[1]+self.config.ade), dtype="float32", order="C")
+            _ax[:,:ax.shape[1]] = ax
+            ax = _ax
+        ay = np.zeros((na, ado), dtype="float32", order="F")
+        if (self.config.mde > 0):
+            _x = np.zeros((x.shape[0],x.shape[1]+self.config.mde+self.config.ado), dtype="float32", order="C")
+            _x[:,:x.shape[1]] = x
+            x = _x
+        y = np.zeros((nm, mdo), dtype="float32", order="C")
         if (save_states):
-            mns = self.config.mns
-            m_states = np.zeros((mn, mds, mns), dtype="float32", order="F")
-            ans = self.config.ans
-            a_states = np.zeros((an, ads, ans), dtype="float32", order="F")
+            m_states = np.zeros((nm, mds, self.config.mns), dtype="float32", order="F")
+            a_states = np.zeros((na, ads, self.config.ans), dtype="float32", order="F")
         else:
-            m_states = np.zeros((mn, mds, 2), dtype="float32", order="F")
-            a_states = np.zeros((an, ads, 2), dtype="float32", order="F")
-        ay = np.zeros((an, ado), dtype="float32", order="F")
+            m_states = np.zeros((nm, mds, 2), dtype="float32", order="F")
+            a_states = np.zeros((na, ads, 2), dtype="float32", order="F")
+        # ------------------------------------------------------------
         # Call the unerlying library.
-        info = self.APOS.check_shape(self.config, self.model, y.T, x.T, xi.T, ax.T, axi.T, sizes)
+        info = self.APOS.check_shape(self.config, self.model, ax.T, axi.T, sizes, x.T, xi.T, y.T)
         assert (info == 0), f"APOS.predict encountered nonzero exit code {info} when calling APOS.check_shape."
-        self.APOS.embed(self.config, self.model, x.T, xi.T, ax.T, axi.T, xxi.T, axxi.T)
-        result = self.APOS.evaluate(self.config, self.model, y.T, xxi.T, axxi.T,
-                                    sizes, m_states, a_states, ay, info, **kwargs)
+        self.APOS.embed(self.config, self.model, axi.T, xi.T, ax.T, x.T)
+        result = self.APOS.evaluate(self.config, self.model, ax.T, ay, sizes,
+                                    x.T, y.T, a_states, m_states, info)
         assert (result[-1] == 0), f"APOS.evaluate returned nonzero exit code {result[-1]}."
         # Save the states if that's 
         if (save_states):
             self.m_states = m_states
             self.a_states = a_states
         # If there are embedded y values in the output, return them to the format at training time.
         if (len(self.yi_map) > 0) and (not embedding):
@@ -388,18 +420,19 @@
             _y = [y[:,i] for i in range(y.shape[1]-yne)]
             for i in range(len(self.yi_map)):
                 start = self.yi_starts[i]
                 size = self.yi_sizes[i]
                 _y.append(
                     self.yi_map[i][np.argmax(y[:,start:start+size], axis=1)]
                 )
-            y = np.asarray(_y).T
+            return np.asarray(_y).T
         elif (embedding and (len(self.yi_map) == 0)):
-            return m_states[:,:,0]            
-        return y
+            return m_states[:,:,-2]
+        else:
+            return y
 
 
     # Save this model to a path.
     def save(self, path):
         import json
         with open(path, "w") as f:
             # Get the config as a Python type.
@@ -452,235 +485,196 @@
 
     from tlux.plot import Plot
     from tlux.random import well_spaced_ball, well_spaced_box
 
     # TODO: test saving and loading with unique value maps
     # TODO: design concise test function that has meaningful signal
     #       in each of "ax", "axi", "x", "xi", test all combinations
-    # TODO: make visualization optional for all of the tests
 
     # A function for testing approximation algorithms.
     def f(x):
         x = x.reshape((-1,2))
         x, y = x[:,0], x[:,1]
         return 3*x + np.cos(8*x)/2 + np.sin(5*y)
-    seed = 1
+
+    n = 100
+    seed = 2
     layer_dim = 32
-    num_layers = 8
-    steps = 100
+    num_layers = 4
+    steps = 1000
     num_threads = None
     np.random.seed(seed)
 
-
     TEST_SAVE_LOAD = False
-    TEST_INT_INPUT = True
-    TEST_APOSITIONAL = False
+    TEST_INT_INPUT = False
+    TEST_APOSITIONAL = True
     TEST_VARIED_SIZE = False
+    SHOW_VISUALS = True
 
+    if (not SHOW_VISUALS):
+        class Plot:
+            def __init__(self, *args, **kwargs): pass
+            def __getattr__(self, *args, **kwargs):
+                return lambda *args, **kwargs: None
 
     if TEST_SAVE_LOAD:
         # Try saving an untrained model.
         m = APOS()
         print("Empty model:")
         print("  str(model) =", str(m))
         print()
         m.save("testing_empty_save.json")
         m.load("testing_empty_save.json")
         from util.approximate import PLRM
-        m = APOS(mdi=2, mds=layer_dim, mns=num_layers, mdo=1, seed=seed,
+        m = APOS(mdn=2, mds=layer_dim, mns=num_layers, mdo=1, seed=seed,
                  num_threads=num_threads, steps=steps, 
                  ) # discontinuity=-1000.0) # initial_step=0.01)
         print("Initialized model:")
         print(m)
         print()
         # Create the test plot.
-        x = well_spaced_box(100, 2)
-        y = f(x)
-        # Normalize the data.
-        x -= x.mean(axis=0)
-        x /= x.var(axis=0)
-        x_min_max = np.vstack((np.min(x,axis=0), np.max(x, axis=0))).T
-        y -= y.mean(axis=0)
-        y /= y.var(axis=0)
+        x = np.asarray(well_spaced_box(n, 2), dtype="float32", order="C")
+        # x[:,0] /= 2
+        y = f(x).astype("float32")
         # Fit the model.
-        m.fit(x, y)
+        m.fit(x.copy(), y.copy())
         # Add the data and the surface of the model to the plot.
         p = Plot()
+        x_min_max = np.asarray([x.min(axis=0), x.max(axis=0)]).T
         p.add("Data", *x.T, y)
+        # p.add("Normalized data", *x_fit.T, y_fit)
         p.add_func("Fit", m, *x_min_max, vectorized=True)
         # Try saving the trained model and applying it after loading.
         print("Saving model:")
         print(m)
         print()
         m.save("testing_real_save.json")
         m.load("testing_real_save.json")
         print("Loaded model:")
         print(m)
         # print(str(m)[:str(m).index("\n\n")])
         print()
-        p.add("Loaded values", *x.T, m(x)+0.05, color=1, marker_size=4)
+        p.add("Loaded values", *x.T, m(x)[:,0]+0.05, color=1, marker_size=4)
         p.plot(show=(m.record.size == 0))
-        # Add plot showing the training loss.
-        if (m.record.size > 0):
-            print("Generating loss plot..")
-            p = type(p)("Mean squared error")
-            # Rescale the columns of the record for visualization.
-            record = m.record
-            p.add("MSE", list(range(record.shape[0])), record[:,0], color=1, mode="lines")
-            p.add("Step factors", list(range(record.shape[0])), record[:,1], color=2, mode="lines")
-            p.add("Step sizes", list(range(record.shape[0])), record[:,2], color=3, mode="lines")
-            p.add("Update ratio", list(range(record.shape[0])), record[:,3], color=4, mode="lines")
-            p.show(append=True, show=True)
-            print("", "done.", flush=True)
         # Remove the save files.
         import os
         try: os.remove("testing_empty_save.json")
         except: pass
         try: os.remove("testing_real_save.json")
         except: pass
 
 
     if TEST_INT_INPUT:
         print("Building model..")
-        x = well_spaced_box(100, 2)
+        x = well_spaced_box(n, 2)
         x_min_max = np.vstack((np.min(x,axis=0), np.max(x, axis=0))).T
         y = f(x)
         # Initialize a new model.
-        m = APOS(mdi=2, mds=layer_dim, mns=num_layers, mdo=1, mne=2, seed=seed, steps=steps, num_threads=num_threads)
+        m = APOS(mdn=2, mds=layer_dim, mns=num_layers, mdo=1, mne=2, seed=seed, steps=steps, num_threads=num_threads)
         all_x = np.concatenate((x, x), axis=0)
         all_y = np.concatenate((y, np.cos(np.linalg.norm(x,axis=1))), axis=0)
         all_xi = np.concatenate((np.ones(len(x)),2*np.ones(len(x)))).reshape((-1,1)).astype("int32")
-        m.fit(x=all_x, y=all_y, xi=all_xi)
-        # Create an evaluation set that evaluates the model that was built over two differnt functions.
-        xi1 = np.ones((len(x),1),dtype="int32")
-        y1 = m(x, xi=xi1)
-        y2 = m(x, xi=2*xi1)
-        print("Adding to plot..")
-        p = Plot()
-        p.add("xi=1 true", *x.T, all_y[:len(all_y)//2], color=0)
-        p.add("xi=2 true", *x.T, all_y[len(all_y)//2:], color=1)
-        p.add_func("xi=1", lambda x: m(x, xi=np.ones(len(x), dtype="int32").reshape((-1,1))), [0,1], [0,1], vectorized=True, color=3, shade=True)
-        p.add_func("xi=2", lambda x: m(x, xi=2*np.ones(len(x), dtype="int32").reshape((-1,1))), [0,1], [0,1], vectorized=True, color=2, shade=True)
-
-        # Generate the visual.
-        print("Generating surface plot..")
-        p.show(show=False)
-        print("Generating loss plot..")
-        p = type(p)("Mean squared error")
-        # Rescale the columns of the record for visualization.
-        record = m.record
-        p.add("MSE", list(range(record.shape[0])), record[:,0], color=1, mode="lines")
-        p.add("Step factors", list(range(record.shape[0])), record[:,1], color=2, mode="lines")
-        p.add("Step sizes", list(range(record.shape[0])), record[:,2], color=3, mode="lines")
-        p.add("Update ratio", list(range(record.shape[0])), record[:,3], color=4, mode="lines")
-        p.show(append=True, show=True)
-        print("", "done.", flush=True)
+        x_fit = np.array(all_x, dtype="float32", order="C")
+        m.fit(x=x_fit, xi=all_xi, y=all_y.copy())
 
-        
-    if TEST_INT_INPUT:
-        print("Building model..")
-        x = well_spaced_box(100, 2)
-        x_min_max = np.vstack((np.min(x,axis=0), np.max(x, axis=0))).T
-        y = f(x)
-        # Initialize a new model.
-        m = APOS(mdi=2, mds=layer_dim, mns=num_layers, mdo=1, mne=2, seed=seed, steps=steps, num_threads=num_threads)
-        all_x = np.concatenate((x, x), axis=0)
-        all_y = np.concatenate((y, np.cos(np.linalg.norm(x,axis=1))), axis=0)
-        all_xi = np.concatenate((np.ones(len(x)),2*np.ones(len(x)))).reshape((-1,1)).astype("int32")
-        m.fit(x=all_x, y=all_y, xi=all_xi)
         # Create an evaluation set that evaluates the model that was built over two differnt functions.
         xi1 = np.ones((len(x),1),dtype="int32")
         y1 = m(x, xi=xi1)
         y2 = m(x, xi=2*xi1)
         print("Adding to plot..")
         p = Plot()
+        # p.add("x fit", *x_fit.T, all_y[:], color=0)
         p.add("xi=1 true", *x.T, all_y[:len(all_y)//2], color=0)
         p.add("xi=2 true", *x.T, all_y[len(all_y)//2:], color=1)
-        p.add_func("xi=1", lambda x: m(x, xi=np.ones(len(x), dtype="int32").reshape((-1,1))), [0,1], [0,1], vectorized=True, color=3, shade=True)
-        p.add_func("xi=2", lambda x: m(x, xi=2*np.ones(len(x), dtype="int32").reshape((-1,1))), [0,1], [0,1], vectorized=True, color=2, shade=True)
-
+        p.add_func("xi=1", lambda x: m(x.copy(), xi=np.ones(len(x), dtype="int32").reshape((-1,1))), *x_min_max, vectorized=True, color=3, shade=True)
+        p.add_func("xi=2", lambda x: m(x.copy(), xi=2*np.ones(len(x), dtype="int32").reshape((-1,1))), *x_min_max, vectorized=True, color=2, shade=True)
         # Generate the visual.
         print("Generating surface plot..")
         p.show(show=False)
-        print("Generating loss plot..")
-        p = type(p)("Mean squared error")
-        # Rescale the columns of the record for visualization.
-        record = m.record
-        p.add("MSE", list(range(record.shape[0])), record[:,0], color=1, mode="lines")
-        p.add("Step factors", list(range(record.shape[0])), record[:,1], color=2, mode="lines")
-        p.add("Step sizes", list(range(record.shape[0])), record[:,2], color=3, mode="lines")
-        p.add("Update ratio", list(range(record.shape[0])), record[:,3], color=4, mode="lines")
-        p.show(append=True, show=True)
-        print("", "done.", flush=True)
 
 
     if TEST_APOSITIONAL:
         print("Building model..")
-        x = well_spaced_box(100, 2)
+        x = well_spaced_box(n, 2)
         x_min_max = np.vstack((np.min(x,axis=0), np.max(x, axis=0))).T
         y = f(x)
-        # Initialize a new model.
-        m = APOS(adi=1, ane=2, mne=2, mdi=0, mdo=1, seed=seed, steps=steps, num_threads=num_threads)
+        # Create all data.
         all_x = np.concatenate((x, x), axis=0)
-        all_y = np.concatenate((y, np.cos(np.linalg.norm(x,axis=1))), axis=0)
         all_xi = np.concatenate((np.ones(len(x)),2*np.ones(len(x)))).reshape((-1,1)).astype("int32")
         ax = all_x.reshape((-1,1)).copy()
         axi = (np.ones(all_x.shape, dtype="int32") * (np.arange(all_x.shape[1])+1)).reshape(-1,1)
         sizes = np.ones(all_x.shape[0], dtype="int32") * 2
-        temp_x = np.zeros((all_x.shape[0],0), dtype="float32")
-        m.fit(x=temp_x, y=all_y, xi=all_xi, ax=ax, axi=axi, sizes=sizes, steps=1000)
-
+        all_y = np.concatenate((y, np.cos(np.linalg.norm(x,axis=1))), axis=0)
+        all_y = all_y.reshape((all_y.shape[0],-1))
+        # Initialize a new model.
+        m = APOS(mdn=0, adn=ax.shape[1], mdo=all_y.shape[1],
+                 ads=layer_dim, ans=num_layers, mds=layer_dim, mns=num_layers,
+                 ane=len(np.unique(axi.flatten())), mne=len(np.unique(all_xi.flatten())),
+                 num_threads=num_threads, seed=seed)
+        print("Fitting model..")
+        m.fit(ax=ax.copy(), axi=axi, sizes=sizes, xi=all_xi, y=all_y.copy(), 
+              steps=1000, num_threads=num_threads, seed=seed)
         # Create an evaluation set that evaluates the model that was built over two differnt functions.
         xi1 = np.ones((len(x),1),dtype="int32")
         ax = x.reshape((-1,1)).copy()
         axi = (np.ones(x.shape, dtype="int32") * (np.arange(x.shape[1])+1)).reshape(-1,1)
         sizes = np.ones(x.shape[0], dtype="int32") * 2
         temp_x = np.zeros((x.shape[0],0), dtype="float32")
         y1 = m(x=temp_x, xi=xi1, ax=ax, axi=axi, sizes=sizes)
         y2 = m(x=temp_x, xi=2*xi1, ax=ax, axi=axi, sizes=sizes)
         print("Adding to plot..")
         p = Plot()
-        p.add("xi=1 true", *x.T, all_y[:len(all_y)//2], color=0)
-        p.add("xi=2 true", *x.T, all_y[len(all_y)//2:], color=1)
+        p.add("xi=1 true", *x.T, all_y[:len(all_y)//2,0], color=0, group=0)
+        p.add("xi=2 true", *x.T, all_y[len(all_y)//2:,0], color=1, group=1)
         def fhat(x, i=1):
             xi = i * np.ones((len(x),1),dtype="int32")
             ax = x.reshape((-1,1)).copy()
             axi = (np.ones(x.shape, dtype="int32") * (np.arange(x.shape[1])+1)).reshape(-1,1)
             sizes = np.ones(x.shape[0], dtype="int32") * 2
             temp_x = np.zeros((x.shape[0],0), dtype="float32")
             return m(x=temp_x, xi=xi, ax=ax, axi=axi, sizes=sizes)
-        p.add_func("xi=1", lambda x: fhat(x, 1), [0,1], [0,1], vectorized=True, color=3, mode="markers", shade=True)
-        p.add_func("xi=2", lambda x: fhat(x, 2), [0,1], [0,1], vectorized=True, color=2, mode="markers", shade=True)
+        p.add_func("xi=1", lambda x: fhat(x, 1), [0,1], [0,1], vectorized=True, color=3, opacity=0.8, group=0) #, mode="markers", shade=True)
+        p.add_func("xi=2", lambda x: fhat(x, 2), [0,1], [0,1], vectorized=True, color=2, opacity=0.8, group=1) #, mode="markers", shade=True)
         # Generate the visual.
         print("Generating surface plot..")
         p.show(show=False)
+
+    print("Final model:")
+    print(m)
+
+    # Generate a visual of the loss function.
+    if (SHOW_VISUALS and (len(getattr(globals().get("m",None), "record", [])) > 0)):
+        print()
         print("Generating loss plot..")
-        p = type(p)("Mean squared error")
+        p = Plot("Mean squared error")
         # Rescale the columns of the record for visualization.
         record = m.record
-        p.add("MSE", list(range(record.shape[0])), record[:,0], color=1, mode="lines")
-        p.add("Step factors", list(range(record.shape[0])), record[:,1], color=2, mode="lines")
-        p.add("Step sizes", list(range(record.shape[0])), record[:,2], color=3, mode="lines")
-        p.add("Update ratio", list(range(record.shape[0])), record[:,3], color=4, mode="lines")
+        for i in range(0, record.shape[0], max(1,record.shape[0] // 400)):
+            step_indices = list(range(i))
+            p.add("MSE", step_indices, record[:i,0], color=1, mode="lines", frame=i)
+            p.add("Step factors", step_indices, record[:i,1], color=2, mode="lines", frame=i)
+            p.add("Step sizes", step_indices, record[:i,2], color=3, mode="lines", frame=i)
+            p.add("Update ratio", step_indices, record[:i,3], color=4, mode="lines", frame=i)
+            p.add("Eval utilization", step_indices, record[:i,4], color=5, mode="lines", frame=i)
+            p.add("Grad utilization", step_indices, record[:i,5], color=6, mode="lines", frame=i)
         p.show(append=True, show=True)
-        print("", "done.", flush=True)
+    print("", "done.", flush=True)
 
 
     if TEST_VARIED_SIZE:
         print("Creating data..")
         for test in range(100):
             print("sizes test: ", test, end="\r")
             sizes = np.random.randint(5,20,size=(10))
-            an = sizes.sum()
-            mn = sizes.size
-            ax = np.random.random(size=(an,2))
-            x = well_spaced_box(mn, 2)
+            na = sizes.sum()
+            nm = sizes.size
+            ax = np.random.random(size=(na,2))
+            x = well_spaced_box(nm, 2)
             y = f(x)
             start = 0
             for i in range(len(sizes)):
                 end = start + sizes[i]
                 y[i] += ax[start:end].max()
                 start = end
             # Fit a model.
             m = APOS(seed=seed, num_threads=num_threads, steps=1)
-            m.fit(x=x, y=y, ax=ax, sizes=sizes)
-
+            m.fit(x=x.copy(), y=y.copy(), ax=ax.copy(), sizes=sizes)
```

### Comparing `tlux-0.0.8/tlux/approximate/apos/apos/__init__.py` & `tlux-0.0.9/tlux/approximate/apos/apos/__init__.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,42 +1,37 @@
 '''This Python code is an automatically generated wrapper
 for Fortran code made by 'fmodpy'. The original documentation
 for the Fortran source code follows.
 
 ! TODO:
 !
-! - Unify memory allocation so that threads don't have to allocate their
-!   own temporary space.
+! - Thoroughly test NORMALIZE (make sure data is correctly normalized in all use cases).
+!   Particularly, check that the initialization of the apositional output scale is working.
 !
-! - Enable a model that has no internal states (for linear regression).
+! - Reset convention to be order of processing (AX, AXI, AY, SIZES, X, XI, Y)
+! - Enable a model that has no internal states for linear regression (*NS=0).
+! - Enable a apositional without a following model (MDO=0) (no apositional shifting).
 !
-! - Enable a apositional without a following model.
+! - Update Python testing code to test all combinations of AX, AXI, AY, X, XI, and Y.
+! - Update Python testing code to attempt different edge-case model sizes
+!    (linear regression, no apositional, no model).
 !
-! - Center and fit inputs and outputs to spherical points (unit length).
+! - Make data normalization use the same work space as the fit procedure
+!   (since these are not needed at the same time).
+! - Pull normalization code out and have it be called separately from 'FIT'.
+!   (decide how to handle encoding the normalization into the model, function?)
+!   Goal is to achieve near-zero losses for doing a few steps at a time in
+!   Python (allowing for easier cancellation, progress updates, ...).
 !
-! - Change initialization of shift terms to be based on the assumption
-!   that input data has spherical shape. Internal shift terms use
-!   previous shift and weight matrices to estimate value ranges for
-!   each basis function, with largest functions getting most negative
-!   shift and smallest functions getting most positive shift.
-!
-! - Create 'condition_model' subroutine that takes values and gradients
-!   at all internal states, uses linear transformations to identify and
-!   remove redundant basis functions and initialize new basis functions
-!   that align most with the error function.
-!
-! - Get stats on the internal values within the network during training.
-!   - step size progression
-!   - shift values
-!   - vector magnitudes for each node
-!   - output weights magnitude for each node
-!   - internal node contributions to MSE
-!   - data distributions at internal nodes (% less and greater than 0)
+! - Use LAPACK to do linear regression, implement simple SVD + gradient descent method
+!   in MATRIX_OPERATIONS, compare speed of both methodologies.
+! - Implement and test Fortran intrinsic version of matrix multiplication.
+! - Implement and test Fortran intrinsic version of SSYRK (manually do loop).
 !
-
+! ---------------------------------------------------------------------------
 
 ! Module for matrix multiplication (absolutely crucial for APOS speed).
 '''
 
 import os
 import ctypes
 import platform
@@ -46,15 +41,15 @@
 #               CONFIGURATION
 # 
 _verbose = True
 _fort_compiler = "gfortran"
 _shared_object_name = "apos." + platform.machine() + ".so"
 _this_directory = os.path.dirname(os.path.abspath(__file__))
 _path_to_lib = os.path.join(_this_directory, _shared_object_name)
-_compile_options = ['-fPIC', '-shared', '-O3', '-lblas', '-fopenmp', '-fcheck=bounds', '-llapack']
+_compile_options = ['-fPIC', '-shared', '-O3', '-lblas', '-llapack', '-fopenmp', '-fcheck=bounds']
 _ordered_dependencies = ['apos.f90', 'apos_c_wrapper.f90']
 # 
 # --------------------------------------------------------------------
 #               AUTO-COMPILING
 #
 # Try to import the existing object. If that fails, recompile and then try.
 try:
@@ -194,138 +189,630 @@
     
         # Call C-accessible Fortran wrapper.
         clib.c_random_unit_vectors(ctypes.byref(column_vectors_dim_1), ctypes.byref(column_vectors_dim_2), ctypes.c_void_p(column_vectors.ctypes.data))
     
         # Return final results, 'INTENT(OUT)' arguments only.
         return column_vectors
 
+    
+    # ----------------------------------------------
+    # Wrapper for the Fortran subroutine ORTHOGONALIZE
+    
+    def orthogonalize(self, a, lengths=None, rank=None, order=None):
+        '''! Orthogonalize and normalize column vectors of A with pivoting.'''
+        
+        # Setting up "a"
+        if ((not issubclass(type(a), numpy.ndarray)) or
+            (not numpy.asarray(a).flags.f_contiguous) or
+            (not (a.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 'a' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            a = numpy.asarray(a, dtype=ctypes.c_float, order='F')
+        a_dim_1 = ctypes.c_int(a.shape[0])
+        a_dim_2 = ctypes.c_int(a.shape[1])
+        
+        # Setting up "lengths"
+        if (lengths is None):
+            lengths = numpy.zeros(shape=(a.shape[1]), dtype=ctypes.c_float, order='F')
+        elif ((not issubclass(type(lengths), numpy.ndarray)) or
+              (not numpy.asarray(lengths).flags.f_contiguous) or
+              (not (lengths.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 'lengths' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            lengths = numpy.asarray(lengths, dtype=ctypes.c_float, order='F')
+        lengths_dim_1 = ctypes.c_int(lengths.shape[0])
+        
+        # Setting up "rank"
+        rank_present = ctypes.c_bool(True)
+        if (rank is None):
+            rank_present = ctypes.c_bool(False)
+            rank = ctypes.c_int()
+        else:
+            rank = ctypes.c_int(rank)
+        
+        # Setting up "order"
+        order_present = ctypes.c_bool(True)
+        if (order is None):
+            order_present = ctypes.c_bool(False)
+            order = numpy.zeros(shape=(1), dtype=ctypes.c_int, order='F')
+        elif (type(order) == bool) and (order):
+            order = numpy.zeros(shape=(a.shape[1]), dtype=ctypes.c_int, order='F')
+        elif ((not issubclass(type(order), numpy.ndarray)) or
+              (not numpy.asarray(order).flags.f_contiguous) or
+              (not (order.dtype == numpy.dtype(ctypes.c_int)))):
+            import warnings
+            warnings.warn("The provided argument 'order' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
+            order = numpy.asarray(order, dtype=ctypes.c_int, order='F')
+        if (order_present):
+            order_dim_1 = ctypes.c_int(order.shape[0])
+        else:
+            order_dim_1 = ctypes.c_int()
+    
+        # Call C-accessible Fortran wrapper.
+        clib.c_orthogonalize(ctypes.byref(a_dim_1), ctypes.byref(a_dim_2), ctypes.c_void_p(a.ctypes.data), ctypes.byref(lengths_dim_1), ctypes.c_void_p(lengths.ctypes.data), ctypes.byref(rank_present), ctypes.byref(rank), ctypes.byref(order_present), ctypes.byref(order_dim_1), ctypes.c_void_p(order.ctypes.data))
+    
+        # Return final results, 'INTENT(OUT)' arguments only.
+        return a, lengths, (rank.value if rank_present else None), (order if order_present else None)
+
+    
+    # ----------------------------------------------
+    # Wrapper for the Fortran subroutine SVD
+    
+    def svd(self, a, s=None, vt=None, rank=None, steps=None, bias=None):
+        '''! Compute the singular values and right singular vectors for matrix A.'''
+        
+        # Setting up "a"
+        if ((not issubclass(type(a), numpy.ndarray)) or
+            (not numpy.asarray(a).flags.f_contiguous) or
+            (not (a.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 'a' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            a = numpy.asarray(a, dtype=ctypes.c_float, order='F')
+        a_dim_1 = ctypes.c_int(a.shape[0])
+        a_dim_2 = ctypes.c_int(a.shape[1])
+        
+        # Setting up "s"
+        if (s is None):
+            s = numpy.zeros(shape=(min(a.shape[0],a.shape[1])), dtype=ctypes.c_float, order='F')
+        elif ((not issubclass(type(s), numpy.ndarray)) or
+              (not numpy.asarray(s).flags.f_contiguous) or
+              (not (s.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 's' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            s = numpy.asarray(s, dtype=ctypes.c_float, order='F')
+        s_dim_1 = ctypes.c_int(s.shape[0])
+        
+        # Setting up "vt"
+        if (vt is None):
+            vt = numpy.zeros(shape=(min(a.shape[0],a.shape[1]), min(a.shape[0],a.shape[1])), dtype=ctypes.c_float, order='F')
+        elif ((not issubclass(type(vt), numpy.ndarray)) or
+              (not numpy.asarray(vt).flags.f_contiguous) or
+              (not (vt.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 'vt' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            vt = numpy.asarray(vt, dtype=ctypes.c_float, order='F')
+        vt_dim_1 = ctypes.c_int(vt.shape[0])
+        vt_dim_2 = ctypes.c_int(vt.shape[1])
+        
+        # Setting up "rank"
+        rank_present = ctypes.c_bool(True)
+        if (rank is None):
+            rank_present = ctypes.c_bool(False)
+            rank = ctypes.c_int()
+        else:
+            rank = ctypes.c_int(rank)
+        
+        # Setting up "steps"
+        steps_present = ctypes.c_bool(True)
+        if (steps is None):
+            steps_present = ctypes.c_bool(False)
+            steps = ctypes.c_int()
+        else:
+            steps = ctypes.c_int(steps)
+        if (type(steps) is not ctypes.c_int): steps = ctypes.c_int(steps)
+        
+        # Setting up "bias"
+        bias_present = ctypes.c_bool(True)
+        if (bias is None):
+            bias_present = ctypes.c_bool(False)
+            bias = ctypes.c_float()
+        else:
+            bias = ctypes.c_float(bias)
+        if (type(bias) is not ctypes.c_float): bias = ctypes.c_float(bias)
+    
+        # Call C-accessible Fortran wrapper.
+        clib.c_svd(ctypes.byref(a_dim_1), ctypes.byref(a_dim_2), ctypes.c_void_p(a.ctypes.data), ctypes.byref(s_dim_1), ctypes.c_void_p(s.ctypes.data), ctypes.byref(vt_dim_1), ctypes.byref(vt_dim_2), ctypes.c_void_p(vt.ctypes.data), ctypes.byref(rank_present), ctypes.byref(rank), ctypes.byref(steps_present), ctypes.byref(steps), ctypes.byref(bias_present), ctypes.byref(bias))
+    
+        # Return final results, 'INTENT(OUT)' arguments only.
+        return s, vt, (rank.value if rank_present else None)
+
+    
+    # ----------------------------------------------
+    # Wrapper for the Fortran subroutine RADIALIZE
+    
+    def radialize(self, x, shift, vecs, invert_result=None, steps=None):
+        '''! If there are at least as many data points as dimension, then
+! compute the principal components and rescale the data by
+! projecting onto those and rescaling so that each component has
+! identical singular values (this makes the data more "radially
+! symmetric").'''
+        
+        # Setting up "x"
+        if ((not issubclass(type(x), numpy.ndarray)) or
+            (not numpy.asarray(x).flags.f_contiguous) or
+            (not (x.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 'x' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            x = numpy.asarray(x, dtype=ctypes.c_float, order='F')
+        x_dim_1 = ctypes.c_int(x.shape[0])
+        x_dim_2 = ctypes.c_int(x.shape[1])
+        
+        # Setting up "shift"
+        if ((not issubclass(type(shift), numpy.ndarray)) or
+            (not numpy.asarray(shift).flags.f_contiguous) or
+            (not (shift.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 'shift' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            shift = numpy.asarray(shift, dtype=ctypes.c_float, order='F')
+        shift_dim_1 = ctypes.c_int(shift.shape[0])
+        
+        # Setting up "vecs"
+        if ((not issubclass(type(vecs), numpy.ndarray)) or
+            (not numpy.asarray(vecs).flags.f_contiguous) or
+            (not (vecs.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 'vecs' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            vecs = numpy.asarray(vecs, dtype=ctypes.c_float, order='F')
+        vecs_dim_1 = ctypes.c_int(vecs.shape[0])
+        vecs_dim_2 = ctypes.c_int(vecs.shape[1])
+        
+        # Setting up "invert_result"
+        invert_result_present = ctypes.c_bool(True)
+        if (invert_result is None):
+            invert_result_present = ctypes.c_bool(False)
+            invert_result = ctypes.c_int()
+        else:
+            invert_result = ctypes.c_int(invert_result)
+        if (type(invert_result) is not ctypes.c_int): invert_result = ctypes.c_int(invert_result)
+        
+        # Setting up "steps"
+        steps_present = ctypes.c_bool(True)
+        if (steps is None):
+            steps_present = ctypes.c_bool(False)
+            steps = ctypes.c_int()
+        else:
+            steps = ctypes.c_int(steps)
+        if (type(steps) is not ctypes.c_int): steps = ctypes.c_int(steps)
+    
+        # Call C-accessible Fortran wrapper.
+        clib.c_radialize(ctypes.byref(x_dim_1), ctypes.byref(x_dim_2), ctypes.c_void_p(x.ctypes.data), ctypes.byref(shift_dim_1), ctypes.c_void_p(shift.ctypes.data), ctypes.byref(vecs_dim_1), ctypes.byref(vecs_dim_2), ctypes.c_void_p(vecs.ctypes.data), ctypes.byref(invert_result_present), ctypes.byref(invert_result), ctypes.byref(steps_present), ctypes.byref(steps))
+    
+        # Return final results, 'INTENT(OUT)' arguments only.
+        return x, shift, vecs
+
 matrix_operations = matrix_operations()
 
 
+class sort_and_select:
+    '''! A module for fast sorting and selecting of data.'''
+
+    
+    # ----------------------------------------------
+    # Wrapper for the Fortran subroutine SWAP_INT
+    
+    def swap_int(self, v1, v2):
+        '''! Swap the values of two integers.'''
+        
+        # Setting up "v1"
+        if (type(v1) is not ctypes.c_int): v1 = ctypes.c_int(v1)
+        
+        # Setting up "v2"
+        if (type(v2) is not ctypes.c_int): v2 = ctypes.c_int(v2)
+    
+        # Call C-accessible Fortran wrapper.
+        clib.c_swap_int(ctypes.byref(v1), ctypes.byref(v2))
+    
+        # Return final results, 'INTENT(OUT)' arguments only.
+        return v1.value, v2.value
+
+    
+    # ----------------------------------------------
+    # Wrapper for the Fortran subroutine ARGSELECT
+    
+    def argselect(self, values, k, indices, divisor=None, max_size=None, recursing=None):
+        '''!                       FastSelect method
+!
+! Given VALUES list of numbers, rearrange the elements of INDICES
+! such that the element of VALUES at INDICES(K) has rank K (holds
+! its same location as if all of VALUES were sorted in INDICES).
+! All elements of VALUES at INDICES(:K-1) are less than or equal,
+! while all elements of VALUES at INDICES(K+1:) are greater or equal.
+!
+! This algorithm uses a recursive approach to exponentially shrink
+! the number of indices that have to be considered to find the
+! element of desired rank, while simultaneously pivoting values
+! that are less than the target rank left and larger right.
+!
+! Arguments:
+!
+!   VALUES   --  A 1D array of real numbers. Will not be modified.
+!   K        --  A positive integer for the rank index about which
+!                VALUES should be rearranged.
+! Optional:
+!
+!   DIVISOR  --  A positive integer >= 2 that represents the
+!                division factor used for large VALUES arrays.
+!   MAX_SIZE --  An integer >= DIVISOR that represents the largest
+!                sized VALUES for which the worst-case pivot value
+!                selection is tolerable. A worst-case pivot causes
+!                O( SIZE(VALUES)^2 ) runtime. This value should be
+!                determined heuristically based on compute hardware.
+! Output:
+!
+!   INDICES  --  A 1D array of original indices for elements of VALUES.
+!
+!   The elements of the array INDICES are rearranged such that the
+!   element at position VALUES(INDICES(K)) is in the same location
+!   it would be if all of VALUES were referenced in sorted order in
+!   INDICES. Also known as, VALUES(INDICES(K)) has rank K.
+!
+! Arguments'''
+        
+        # Setting up "values"
+        if ((not issubclass(type(values), numpy.ndarray)) or
+            (not numpy.asarray(values).flags.f_contiguous) or
+            (not (values.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 'values' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            values = numpy.asarray(values, dtype=ctypes.c_float, order='F')
+        values_dim_1 = ctypes.c_int(values.shape[0])
+        
+        # Setting up "k"
+        if (type(k) is not ctypes.c_int): k = ctypes.c_int(k)
+        
+        # Setting up "indices"
+        if ((not issubclass(type(indices), numpy.ndarray)) or
+            (not numpy.asarray(indices).flags.f_contiguous) or
+            (not (indices.dtype == numpy.dtype(ctypes.c_int)))):
+            import warnings
+            warnings.warn("The provided argument 'indices' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
+            indices = numpy.asarray(indices, dtype=ctypes.c_int, order='F')
+        indices_dim_1 = ctypes.c_int(indices.shape[0])
+        
+        # Setting up "divisor"
+        divisor_present = ctypes.c_bool(True)
+        if (divisor is None):
+            divisor_present = ctypes.c_bool(False)
+            divisor = ctypes.c_int()
+        else:
+            divisor = ctypes.c_int(divisor)
+        if (type(divisor) is not ctypes.c_int): divisor = ctypes.c_int(divisor)
+        
+        # Setting up "max_size"
+        max_size_present = ctypes.c_bool(True)
+        if (max_size is None):
+            max_size_present = ctypes.c_bool(False)
+            max_size = ctypes.c_int()
+        else:
+            max_size = ctypes.c_int(max_size)
+        if (type(max_size) is not ctypes.c_int): max_size = ctypes.c_int(max_size)
+        
+        # Setting up "recursing"
+        recursing_present = ctypes.c_bool(True)
+        if (recursing is None):
+            recursing_present = ctypes.c_bool(False)
+            recursing = ctypes.c_int()
+        else:
+            recursing = ctypes.c_int(recursing)
+        if (type(recursing) is not ctypes.c_int): recursing = ctypes.c_int(recursing)
+    
+        # Call C-accessible Fortran wrapper.
+        clib.c_argselect(ctypes.byref(values_dim_1), ctypes.c_void_p(values.ctypes.data), ctypes.byref(k), ctypes.byref(indices_dim_1), ctypes.c_void_p(indices.ctypes.data), ctypes.byref(divisor_present), ctypes.byref(divisor), ctypes.byref(max_size_present), ctypes.byref(max_size), ctypes.byref(recursing_present), ctypes.byref(recursing))
+    
+        # Return final results, 'INTENT(OUT)' arguments only.
+        return indices
+
+    
+    # ----------------------------------------------
+    # Wrapper for the Fortran subroutine ARGSORT
+    
+    def argsort(self, values, indices, min_size=None, init_inds=None):
+        '''!                         FastSort
+!
+! This routine uses a combination of QuickSort (with modestly
+! intelligent pivot selection) and Insertion Sort (for small arrays)
+! to achieve very fast average case sort times for both random and
+! partially sorted data. The pivot is selected for QuickSort as the
+! median of the first, middle, and last values in the array.
+!
+! Arguments:
+!
+!   VALUES   --  A 1D array of real numbers.
+!   INDICES  --  A 1D array of original indices for elements of VALUES.
+!
+! Optional:
+!
+!   MIN_SIZE --  An positive integer that represents the largest
+!                sized VALUES for which a partition about a pivot
+!                is used to reduce the size of a an unsorted array.
+!                Any size less than this will result in the use of
+!                INSERTION_ARGSORT instead of ARGPARTITION.
+!
+! Output:
+!
+!   The elements of the array INDICES contain ths sorted order of VALUES.'''
+        
+        # Setting up "values"
+        if ((not issubclass(type(values), numpy.ndarray)) or
+            (not numpy.asarray(values).flags.f_contiguous) or
+            (not (values.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 'values' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            values = numpy.asarray(values, dtype=ctypes.c_float, order='F')
+        values_dim_1 = ctypes.c_int(values.shape[0])
+        
+        # Setting up "indices"
+        if ((not issubclass(type(indices), numpy.ndarray)) or
+            (not numpy.asarray(indices).flags.f_contiguous) or
+            (not (indices.dtype == numpy.dtype(ctypes.c_int)))):
+            import warnings
+            warnings.warn("The provided argument 'indices' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
+            indices = numpy.asarray(indices, dtype=ctypes.c_int, order='F')
+        indices_dim_1 = ctypes.c_int(indices.shape[0])
+        
+        # Setting up "min_size"
+        min_size_present = ctypes.c_bool(True)
+        if (min_size is None):
+            min_size_present = ctypes.c_bool(False)
+            min_size = ctypes.c_int()
+        else:
+            min_size = ctypes.c_int(min_size)
+        if (type(min_size) is not ctypes.c_int): min_size = ctypes.c_int(min_size)
+        
+        # Setting up "init_inds"
+        init_inds_present = ctypes.c_bool(True)
+        if (init_inds is None):
+            init_inds_present = ctypes.c_bool(False)
+            init_inds = ctypes.c_int()
+        else:
+            init_inds = ctypes.c_int(init_inds)
+        if (type(init_inds) is not ctypes.c_int): init_inds = ctypes.c_int(init_inds)
+    
+        # Call C-accessible Fortran wrapper.
+        clib.c_argsort(ctypes.byref(values_dim_1), ctypes.c_void_p(values.ctypes.data), ctypes.byref(indices_dim_1), ctypes.c_void_p(indices.ctypes.data), ctypes.byref(min_size_present), ctypes.byref(min_size), ctypes.byref(init_inds_present), ctypes.byref(init_inds))
+    
+        # Return final results, 'INTENT(OUT)' arguments only.
+        return indices
+
+    
+    # ----------------------------------------------
+    # Wrapper for the Fortran subroutine INSERTION_ARGSORT
+    
+    def insertion_argsort(self, values, indices):
+        '''! Insertion sort (best for small lists).'''
+        
+        # Setting up "values"
+        if ((not issubclass(type(values), numpy.ndarray)) or
+            (not numpy.asarray(values).flags.f_contiguous) or
+            (not (values.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 'values' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            values = numpy.asarray(values, dtype=ctypes.c_float, order='F')
+        values_dim_1 = ctypes.c_int(values.shape[0])
+        
+        # Setting up "indices"
+        if ((not issubclass(type(indices), numpy.ndarray)) or
+            (not numpy.asarray(indices).flags.f_contiguous) or
+            (not (indices.dtype == numpy.dtype(ctypes.c_int)))):
+            import warnings
+            warnings.warn("The provided argument 'indices' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
+            indices = numpy.asarray(indices, dtype=ctypes.c_int, order='F')
+        indices_dim_1 = ctypes.c_int(indices.shape[0])
+    
+        # Call C-accessible Fortran wrapper.
+        clib.c_insertion_argsort(ctypes.byref(values_dim_1), ctypes.c_void_p(values.ctypes.data), ctypes.byref(indices_dim_1), ctypes.c_void_p(indices.ctypes.data))
+    
+        # Return final results, 'INTENT(OUT)' arguments only.
+        return indices
+
+    
+    # ----------------------------------------------
+    # Wrapper for the Fortran subroutine ARGPARTITION
+    
+    def argpartition(self, values, indices):
+        '''! This function efficiently partitions values based on the median
+! of the first, middle, and last elements of the VALUES array. This
+! function returns the index of the pivot.'''
+        
+        # Setting up "values"
+        if ((not issubclass(type(values), numpy.ndarray)) or
+            (not numpy.asarray(values).flags.f_contiguous) or
+            (not (values.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 'values' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            values = numpy.asarray(values, dtype=ctypes.c_float, order='F')
+        values_dim_1 = ctypes.c_int(values.shape[0])
+        
+        # Setting up "indices"
+        if ((not issubclass(type(indices), numpy.ndarray)) or
+            (not numpy.asarray(indices).flags.f_contiguous) or
+            (not (indices.dtype == numpy.dtype(ctypes.c_int)))):
+            import warnings
+            warnings.warn("The provided argument 'indices' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
+            indices = numpy.asarray(indices, dtype=ctypes.c_int, order='F')
+        indices_dim_1 = ctypes.c_int(indices.shape[0])
+        
+        # Setting up "left"
+        left = ctypes.c_int()
+    
+        # Call C-accessible Fortran wrapper.
+        clib.c_argpartition(ctypes.byref(values_dim_1), ctypes.c_void_p(values.ctypes.data), ctypes.byref(indices_dim_1), ctypes.c_void_p(indices.ctypes.data), ctypes.byref(left))
+    
+        # Return final results, 'INTENT(OUT)' arguments only.
+        return indices, left.value
+
+sort_and_select = sort_and_select()
+
+
 class apos:
     '''! An apositional (/aggregate) and positional piecewise linear regression model.'''
     
     # This defines a C structure that can be used to hold this defined type.
     class MODEL_CONFIG(ctypes.Structure):
         # (name, ctype) fields for this structure.
-        _fields_ = [("mdi", ctypes.c_int), ("mds", ctypes.c_int), ("mns", ctypes.c_int), ("mdo", ctypes.c_int), ("mne", ctypes.c_int), ("mde", ctypes.c_int), ("adi", ctypes.c_int), ("ads", ctypes.c_int), ("ans", ctypes.c_int), ("ado", ctypes.c_int), ("ane", ctypes.c_int), ("ade", ctypes.c_int), ("total_size", ctypes.c_int), ("num_vars", ctypes.c_int), ("msiv", ctypes.c_int), ("meiv", ctypes.c_int), ("msis", ctypes.c_int), ("meis", ctypes.c_int), ("mssv", ctypes.c_int), ("mesv", ctypes.c_int), ("msss", ctypes.c_int), ("mess", ctypes.c_int), ("msov", ctypes.c_int), ("meov", ctypes.c_int), ("msev", ctypes.c_int), ("meev", ctypes.c_int), ("asiv", ctypes.c_int), ("aeiv", ctypes.c_int), ("asis", ctypes.c_int), ("aeis", ctypes.c_int), ("assv", ctypes.c_int), ("aesv", ctypes.c_int), ("asss", ctypes.c_int), ("aess", ctypes.c_int), ("asov", ctypes.c_int), ("aeov", ctypes.c_int), ("asev", ctypes.c_int), ("aeev", ctypes.c_int), ("miss", ctypes.c_int), ("mise", ctypes.c_int), ("moss", ctypes.c_int), ("mose", ctypes.c_int), ("aiss", ctypes.c_int), ("aise", ctypes.c_int), ("discontinuity", ctypes.c_float), ("initial_shift_range", ctypes.c_float), ("initial_output_scale", ctypes.c_float), ("initial_step", ctypes.c_float), ("initial_step_mean_change", ctypes.c_float), ("initial_step_curv_change", ctypes.c_float), ("faster_rate", ctypes.c_float), ("slower_rate", ctypes.c_float), ("min_steps_to_stability", ctypes.c_int), ("num_threads", ctypes.c_int), ("keep_best", ctypes.c_bool), ("early_stop", ctypes.c_bool)]
+        _fields_ = [("adn", ctypes.c_int), ("adi", ctypes.c_int), ("ads", ctypes.c_int), ("ans", ctypes.c_int), ("ado", ctypes.c_int), ("ane", ctypes.c_int), ("ade", ctypes.c_int), ("mdn", ctypes.c_int), ("mdi", ctypes.c_int), ("mds", ctypes.c_int), ("mns", ctypes.c_int), ("mdo", ctypes.c_int), ("mne", ctypes.c_int), ("mde", ctypes.c_int), ("total_size", ctypes.c_int), ("num_vars", ctypes.c_int), ("asiv", ctypes.c_int), ("aeiv", ctypes.c_int), ("asis", ctypes.c_int), ("aeis", ctypes.c_int), ("assv", ctypes.c_int), ("aesv", ctypes.c_int), ("asss", ctypes.c_int), ("aess", ctypes.c_int), ("asov", ctypes.c_int), ("aeov", ctypes.c_int), ("asev", ctypes.c_int), ("aeev", ctypes.c_int), ("msiv", ctypes.c_int), ("meiv", ctypes.c_int), ("msis", ctypes.c_int), ("meis", ctypes.c_int), ("mssv", ctypes.c_int), ("mesv", ctypes.c_int), ("msss", ctypes.c_int), ("mess", ctypes.c_int), ("msov", ctypes.c_int), ("meov", ctypes.c_int), ("msev", ctypes.c_int), ("meev", ctypes.c_int), ("aiss", ctypes.c_int), ("aise", ctypes.c_int), ("aoss", ctypes.c_int), ("aose", ctypes.c_int), ("miss", ctypes.c_int), ("mise", ctypes.c_int), ("moss", ctypes.c_int), ("mose", ctypes.c_int), ("discontinuity", ctypes.c_float), ("initial_shift_range", ctypes.c_float), ("initial_output_scale", ctypes.c_float), ("step_factor", ctypes.c_float), ("step_mean_change", ctypes.c_float), ("step_curv_change", ctypes.c_float), ("faster_rate", ctypes.c_float), ("slower_rate", ctypes.c_float), ("min_update_ratio", ctypes.c_float), ("min_steps_to_stability", ctypes.c_int), ("num_threads", ctypes.c_int), ("print_delay_sec", ctypes.c_int), ("steps_taken", ctypes.c_int), ("logging_step_frequency", ctypes.c_int), ("num_to_update", ctypes.c_int), ("ax_normalized", ctypes.c_bool), ("axi_normalized", ctypes.c_bool), ("ay_normalized", ctypes.c_bool), ("x_normalized", ctypes.c_bool), ("xi_normalized", ctypes.c_bool), ("y_normalized", ctypes.c_bool), ("encode_normalization", ctypes.c_bool), ("apply_shift", ctypes.c_bool), ("keep_best", ctypes.c_bool), ("early_stop", ctypes.c_bool), ("rwork_size", ctypes.c_int), ("iwork_size", ctypes.c_int), ("na", ctypes.c_int), ("nm", ctypes.c_int), ("smg", ctypes.c_int), ("emg", ctypes.c_int), ("smgm", ctypes.c_int), ("emgm", ctypes.c_int), ("smgc", ctypes.c_int), ("emgc", ctypes.c_int), ("sbm", ctypes.c_int), ("ebm", ctypes.c_int), ("sfma", ctypes.c_int), ("efma", ctypes.c_int), ("saxs", ctypes.c_int), ("eaxs", ctypes.c_int), ("saxg", ctypes.c_int), ("eaxg", ctypes.c_int), ("saa", ctypes.c_int), ("eaa", ctypes.c_int), ("say", ctypes.c_int), ("eay", ctypes.c_int), ("sxt", ctypes.c_int), ("ext", ctypes.c_int), ("sayg", ctypes.c_int), ("eayg", ctypes.c_int), ("smxs", ctypes.c_int), ("emxs", ctypes.c_int), ("smxg", ctypes.c_int), ("emxg", ctypes.c_int), ("sma", ctypes.c_int), ("ema", ctypes.c_int), ("syg", ctypes.c_int), ("eyg", ctypes.c_int), ("saxr", ctypes.c_int), ("eaxr", ctypes.c_int), ("saxis", ctypes.c_int), ("eaxis", ctypes.c_int), ("saxir", ctypes.c_int), ("eaxir", ctypes.c_int), ("sayr", ctypes.c_int), ("eayr", ctypes.c_int), ("smxr", ctypes.c_int), ("emxr", ctypes.c_int), ("smxis", ctypes.c_int), ("emxis", ctypes.c_int), ("smxir", ctypes.c_int), ("emxir", ctypes.c_int), ("syr", ctypes.c_int), ("eyr", ctypes.c_int), ("sui", ctypes.c_int), ("eui", ctypes.c_int), ("sbas", ctypes.c_int), ("ebas", ctypes.c_int), ("sbae", ctypes.c_int), ("ebae", ctypes.c_int), ("sbms", ctypes.c_int), ("ebms", ctypes.c_int), ("sbme", ctypes.c_int), ("ebme", ctypes.c_int)]
         # Define an "__init__" that can take a class or keyword arguments as input.
         def __init__(self, value=0, **kwargs):
             # From whatever object (or dictionary) was given, assign internal values.
-            self.mdi = kwargs.get("mdi", getattr(value, "mdi", value))
-            self.mds = kwargs.get("mds", getattr(value, "mds", value))
-            self.mns = kwargs.get("mns", getattr(value, "mns", value))
-            self.mdo = kwargs.get("mdo", getattr(value, "mdo", value))
-            self.mne = kwargs.get("mne", getattr(value, "mne", value))
-            self.mde = kwargs.get("mde", getattr(value, "mde", value))
+            self.adn = kwargs.get("adn", getattr(value, "adn", value))
             self.adi = kwargs.get("adi", getattr(value, "adi", value))
             self.ads = kwargs.get("ads", getattr(value, "ads", value))
             self.ans = kwargs.get("ans", getattr(value, "ans", value))
             self.ado = kwargs.get("ado", getattr(value, "ado", value))
             self.ane = kwargs.get("ane", getattr(value, "ane", value))
             self.ade = kwargs.get("ade", getattr(value, "ade", value))
+            self.mdn = kwargs.get("mdn", getattr(value, "mdn", value))
+            self.mdi = kwargs.get("mdi", getattr(value, "mdi", value))
+            self.mds = kwargs.get("mds", getattr(value, "mds", value))
+            self.mns = kwargs.get("mns", getattr(value, "mns", value))
+            self.mdo = kwargs.get("mdo", getattr(value, "mdo", value))
+            self.mne = kwargs.get("mne", getattr(value, "mne", value))
+            self.mde = kwargs.get("mde", getattr(value, "mde", value))
             self.total_size = kwargs.get("total_size", getattr(value, "total_size", value))
             self.num_vars = kwargs.get("num_vars", getattr(value, "num_vars", value))
-            self.msiv = kwargs.get("msiv", getattr(value, "msiv", value))
-            self.meiv = kwargs.get("meiv", getattr(value, "meiv", value))
-            self.msis = kwargs.get("msis", getattr(value, "msis", value))
-            self.meis = kwargs.get("meis", getattr(value, "meis", value))
-            self.mssv = kwargs.get("mssv", getattr(value, "mssv", value))
-            self.mesv = kwargs.get("mesv", getattr(value, "mesv", value))
-            self.msss = kwargs.get("msss", getattr(value, "msss", value))
-            self.mess = kwargs.get("mess", getattr(value, "mess", value))
-            self.msov = kwargs.get("msov", getattr(value, "msov", value))
-            self.meov = kwargs.get("meov", getattr(value, "meov", value))
-            self.msev = kwargs.get("msev", getattr(value, "msev", value))
-            self.meev = kwargs.get("meev", getattr(value, "meev", value))
             self.asiv = kwargs.get("asiv", getattr(value, "asiv", value))
             self.aeiv = kwargs.get("aeiv", getattr(value, "aeiv", value))
             self.asis = kwargs.get("asis", getattr(value, "asis", value))
             self.aeis = kwargs.get("aeis", getattr(value, "aeis", value))
             self.assv = kwargs.get("assv", getattr(value, "assv", value))
             self.aesv = kwargs.get("aesv", getattr(value, "aesv", value))
             self.asss = kwargs.get("asss", getattr(value, "asss", value))
             self.aess = kwargs.get("aess", getattr(value, "aess", value))
             self.asov = kwargs.get("asov", getattr(value, "asov", value))
             self.aeov = kwargs.get("aeov", getattr(value, "aeov", value))
             self.asev = kwargs.get("asev", getattr(value, "asev", value))
             self.aeev = kwargs.get("aeev", getattr(value, "aeev", value))
+            self.msiv = kwargs.get("msiv", getattr(value, "msiv", value))
+            self.meiv = kwargs.get("meiv", getattr(value, "meiv", value))
+            self.msis = kwargs.get("msis", getattr(value, "msis", value))
+            self.meis = kwargs.get("meis", getattr(value, "meis", value))
+            self.mssv = kwargs.get("mssv", getattr(value, "mssv", value))
+            self.mesv = kwargs.get("mesv", getattr(value, "mesv", value))
+            self.msss = kwargs.get("msss", getattr(value, "msss", value))
+            self.mess = kwargs.get("mess", getattr(value, "mess", value))
+            self.msov = kwargs.get("msov", getattr(value, "msov", value))
+            self.meov = kwargs.get("meov", getattr(value, "meov", value))
+            self.msev = kwargs.get("msev", getattr(value, "msev", value))
+            self.meev = kwargs.get("meev", getattr(value, "meev", value))
+            self.aiss = kwargs.get("aiss", getattr(value, "aiss", value))
+            self.aise = kwargs.get("aise", getattr(value, "aise", value))
+            self.aoss = kwargs.get("aoss", getattr(value, "aoss", value))
+            self.aose = kwargs.get("aose", getattr(value, "aose", value))
             self.miss = kwargs.get("miss", getattr(value, "miss", value))
             self.mise = kwargs.get("mise", getattr(value, "mise", value))
             self.moss = kwargs.get("moss", getattr(value, "moss", value))
             self.mose = kwargs.get("mose", getattr(value, "mose", value))
-            self.aiss = kwargs.get("aiss", getattr(value, "aiss", value))
-            self.aise = kwargs.get("aise", getattr(value, "aise", value))
             self.discontinuity = kwargs.get("discontinuity", getattr(value, "discontinuity", value))
             self.initial_shift_range = kwargs.get("initial_shift_range", getattr(value, "initial_shift_range", value))
             self.initial_output_scale = kwargs.get("initial_output_scale", getattr(value, "initial_output_scale", value))
-            self.initial_step = kwargs.get("initial_step", getattr(value, "initial_step", value))
-            self.initial_step_mean_change = kwargs.get("initial_step_mean_change", getattr(value, "initial_step_mean_change", value))
-            self.initial_step_curv_change = kwargs.get("initial_step_curv_change", getattr(value, "initial_step_curv_change", value))
+            self.step_factor = kwargs.get("step_factor", getattr(value, "step_factor", value))
+            self.step_mean_change = kwargs.get("step_mean_change", getattr(value, "step_mean_change", value))
+            self.step_curv_change = kwargs.get("step_curv_change", getattr(value, "step_curv_change", value))
             self.faster_rate = kwargs.get("faster_rate", getattr(value, "faster_rate", value))
             self.slower_rate = kwargs.get("slower_rate", getattr(value, "slower_rate", value))
+            self.min_update_ratio = kwargs.get("min_update_ratio", getattr(value, "min_update_ratio", value))
             self.min_steps_to_stability = kwargs.get("min_steps_to_stability", getattr(value, "min_steps_to_stability", value))
             self.num_threads = kwargs.get("num_threads", getattr(value, "num_threads", value))
+            self.print_delay_sec = kwargs.get("print_delay_sec", getattr(value, "print_delay_sec", value))
+            self.steps_taken = kwargs.get("steps_taken", getattr(value, "steps_taken", value))
+            self.logging_step_frequency = kwargs.get("logging_step_frequency", getattr(value, "logging_step_frequency", value))
+            self.num_to_update = kwargs.get("num_to_update", getattr(value, "num_to_update", value))
+            self.ax_normalized = kwargs.get("ax_normalized", getattr(value, "ax_normalized", value))
+            self.axi_normalized = kwargs.get("axi_normalized", getattr(value, "axi_normalized", value))
+            self.ay_normalized = kwargs.get("ay_normalized", getattr(value, "ay_normalized", value))
+            self.x_normalized = kwargs.get("x_normalized", getattr(value, "x_normalized", value))
+            self.xi_normalized = kwargs.get("xi_normalized", getattr(value, "xi_normalized", value))
+            self.y_normalized = kwargs.get("y_normalized", getattr(value, "y_normalized", value))
+            self.encode_normalization = kwargs.get("encode_normalization", getattr(value, "encode_normalization", value))
+            self.apply_shift = kwargs.get("apply_shift", getattr(value, "apply_shift", value))
             self.keep_best = kwargs.get("keep_best", getattr(value, "keep_best", value))
             self.early_stop = kwargs.get("early_stop", getattr(value, "early_stop", value))
+            self.rwork_size = kwargs.get("rwork_size", getattr(value, "rwork_size", value))
+            self.iwork_size = kwargs.get("iwork_size", getattr(value, "iwork_size", value))
+            self.na = kwargs.get("na", getattr(value, "na", value))
+            self.nm = kwargs.get("nm", getattr(value, "nm", value))
+            self.smg = kwargs.get("smg", getattr(value, "smg", value))
+            self.emg = kwargs.get("emg", getattr(value, "emg", value))
+            self.smgm = kwargs.get("smgm", getattr(value, "smgm", value))
+            self.emgm = kwargs.get("emgm", getattr(value, "emgm", value))
+            self.smgc = kwargs.get("smgc", getattr(value, "smgc", value))
+            self.emgc = kwargs.get("emgc", getattr(value, "emgc", value))
+            self.sbm = kwargs.get("sbm", getattr(value, "sbm", value))
+            self.ebm = kwargs.get("ebm", getattr(value, "ebm", value))
+            self.sfma = kwargs.get("sfma", getattr(value, "sfma", value))
+            self.efma = kwargs.get("efma", getattr(value, "efma", value))
+            self.saxs = kwargs.get("saxs", getattr(value, "saxs", value))
+            self.eaxs = kwargs.get("eaxs", getattr(value, "eaxs", value))
+            self.saxg = kwargs.get("saxg", getattr(value, "saxg", value))
+            self.eaxg = kwargs.get("eaxg", getattr(value, "eaxg", value))
+            self.saa = kwargs.get("saa", getattr(value, "saa", value))
+            self.eaa = kwargs.get("eaa", getattr(value, "eaa", value))
+            self.say = kwargs.get("say", getattr(value, "say", value))
+            self.eay = kwargs.get("eay", getattr(value, "eay", value))
+            self.sxt = kwargs.get("sxt", getattr(value, "sxt", value))
+            self.ext = kwargs.get("ext", getattr(value, "ext", value))
+            self.sayg = kwargs.get("sayg", getattr(value, "sayg", value))
+            self.eayg = kwargs.get("eayg", getattr(value, "eayg", value))
+            self.smxs = kwargs.get("smxs", getattr(value, "smxs", value))
+            self.emxs = kwargs.get("emxs", getattr(value, "emxs", value))
+            self.smxg = kwargs.get("smxg", getattr(value, "smxg", value))
+            self.emxg = kwargs.get("emxg", getattr(value, "emxg", value))
+            self.sma = kwargs.get("sma", getattr(value, "sma", value))
+            self.ema = kwargs.get("ema", getattr(value, "ema", value))
+            self.syg = kwargs.get("syg", getattr(value, "syg", value))
+            self.eyg = kwargs.get("eyg", getattr(value, "eyg", value))
+            self.saxr = kwargs.get("saxr", getattr(value, "saxr", value))
+            self.eaxr = kwargs.get("eaxr", getattr(value, "eaxr", value))
+            self.saxis = kwargs.get("saxis", getattr(value, "saxis", value))
+            self.eaxis = kwargs.get("eaxis", getattr(value, "eaxis", value))
+            self.saxir = kwargs.get("saxir", getattr(value, "saxir", value))
+            self.eaxir = kwargs.get("eaxir", getattr(value, "eaxir", value))
+            self.sayr = kwargs.get("sayr", getattr(value, "sayr", value))
+            self.eayr = kwargs.get("eayr", getattr(value, "eayr", value))
+            self.smxr = kwargs.get("smxr", getattr(value, "smxr", value))
+            self.emxr = kwargs.get("emxr", getattr(value, "emxr", value))
+            self.smxis = kwargs.get("smxis", getattr(value, "smxis", value))
+            self.emxis = kwargs.get("emxis", getattr(value, "emxis", value))
+            self.smxir = kwargs.get("smxir", getattr(value, "smxir", value))
+            self.emxir = kwargs.get("emxir", getattr(value, "emxir", value))
+            self.syr = kwargs.get("syr", getattr(value, "syr", value))
+            self.eyr = kwargs.get("eyr", getattr(value, "eyr", value))
+            self.sui = kwargs.get("sui", getattr(value, "sui", value))
+            self.eui = kwargs.get("eui", getattr(value, "eui", value))
+            self.sbas = kwargs.get("sbas", getattr(value, "sbas", value))
+            self.ebas = kwargs.get("ebas", getattr(value, "ebas", value))
+            self.sbae = kwargs.get("sbae", getattr(value, "sbae", value))
+            self.ebae = kwargs.get("ebae", getattr(value, "ebae", value))
+            self.sbms = kwargs.get("sbms", getattr(value, "sbms", value))
+            self.ebms = kwargs.get("ebms", getattr(value, "ebms", value))
+            self.sbme = kwargs.get("sbme", getattr(value, "sbme", value))
+            self.ebme = kwargs.get("ebme", getattr(value, "ebme", value))
     
 
     
     # ----------------------------------------------
     # Wrapper for the Fortran subroutine NEW_MODEL_CONFIG
     
-    def new_model_config(self, mdi, mdo, adi, mds=None, mns=None, mne=None, mde=None, ado=None, ads=None, ans=None, ane=None, ade=None, num_threads=None):
+    def new_model_config(self, adn, mdn, mdo, ado=None, ads=None, ans=None, ane=None, ade=None, mds=None, mns=None, mne=None, mde=None, num_threads=None):
         '''! Generate a model configuration given state parameters for the model.
 ! Size related parameters.'''
         MODEL_CONFIG = apos.MODEL_CONFIG
         
-        # Setting up "mdi"
-        if (type(mdi) is not ctypes.c_int): mdi = ctypes.c_int(mdi)
-        
-        # Setting up "mdo"
-        if (type(mdo) is not ctypes.c_int): mdo = ctypes.c_int(mdo)
-        
-        # Setting up "mds"
-        mds_present = ctypes.c_bool(True)
-        if (mds is None):
-            mds_present = ctypes.c_bool(False)
-            mds = ctypes.c_int()
-        else:
-            mds = ctypes.c_int(mds)
-        if (type(mds) is not ctypes.c_int): mds = ctypes.c_int(mds)
-        
-        # Setting up "mns"
-        mns_present = ctypes.c_bool(True)
-        if (mns is None):
-            mns_present = ctypes.c_bool(False)
-            mns = ctypes.c_int()
-        else:
-            mns = ctypes.c_int(mns)
-        if (type(mns) is not ctypes.c_int): mns = ctypes.c_int(mns)
-        
-        # Setting up "mne"
-        mne_present = ctypes.c_bool(True)
-        if (mne is None):
-            mne_present = ctypes.c_bool(False)
-            mne = ctypes.c_int()
-        else:
-            mne = ctypes.c_int(mne)
-        if (type(mne) is not ctypes.c_int): mne = ctypes.c_int(mne)
-        
-        # Setting up "mde"
-        mde_present = ctypes.c_bool(True)
-        if (mde is None):
-            mde_present = ctypes.c_bool(False)
-            mde = ctypes.c_int()
-        else:
-            mde = ctypes.c_int(mde)
-        if (type(mde) is not ctypes.c_int): mde = ctypes.c_int(mde)
-        
-        # Setting up "adi"
-        if (type(adi) is not ctypes.c_int): adi = ctypes.c_int(adi)
+        # Setting up "adn"
+        if (type(adn) is not ctypes.c_int): adn = ctypes.c_int(adn)
         
         # Setting up "ado"
         ado_present = ctypes.c_bool(True)
         if (ado is None):
             ado_present = ctypes.c_bool(False)
             ado = ctypes.c_int()
         else:
@@ -364,28 +851,95 @@
         if (ade is None):
             ade_present = ctypes.c_bool(False)
             ade = ctypes.c_int()
         else:
             ade = ctypes.c_int(ade)
         if (type(ade) is not ctypes.c_int): ade = ctypes.c_int(ade)
         
+        # Setting up "mdn"
+        if (type(mdn) is not ctypes.c_int): mdn = ctypes.c_int(mdn)
+        
+        # Setting up "mdo"
+        if (type(mdo) is not ctypes.c_int): mdo = ctypes.c_int(mdo)
+        
+        # Setting up "mds"
+        mds_present = ctypes.c_bool(True)
+        if (mds is None):
+            mds_present = ctypes.c_bool(False)
+            mds = ctypes.c_int()
+        else:
+            mds = ctypes.c_int(mds)
+        if (type(mds) is not ctypes.c_int): mds = ctypes.c_int(mds)
+        
+        # Setting up "mns"
+        mns_present = ctypes.c_bool(True)
+        if (mns is None):
+            mns_present = ctypes.c_bool(False)
+            mns = ctypes.c_int()
+        else:
+            mns = ctypes.c_int(mns)
+        if (type(mns) is not ctypes.c_int): mns = ctypes.c_int(mns)
+        
+        # Setting up "mne"
+        mne_present = ctypes.c_bool(True)
+        if (mne is None):
+            mne_present = ctypes.c_bool(False)
+            mne = ctypes.c_int()
+        else:
+            mne = ctypes.c_int(mne)
+        if (type(mne) is not ctypes.c_int): mne = ctypes.c_int(mne)
+        
+        # Setting up "mde"
+        mde_present = ctypes.c_bool(True)
+        if (mde is None):
+            mde_present = ctypes.c_bool(False)
+            mde = ctypes.c_int()
+        else:
+            mde = ctypes.c_int(mde)
+        if (type(mde) is not ctypes.c_int): mde = ctypes.c_int(mde)
+        
         # Setting up "num_threads"
         num_threads_present = ctypes.c_bool(True)
         if (num_threads is None):
             num_threads_present = ctypes.c_bool(False)
             num_threads = ctypes.c_int()
         else:
             num_threads = ctypes.c_int(num_threads)
         if (type(num_threads) is not ctypes.c_int): num_threads = ctypes.c_int(num_threads)
         
         # Setting up "config"
         config = MODEL_CONFIG()
     
         # Call C-accessible Fortran wrapper.
-        clib.c_new_model_config(ctypes.byref(mdi), ctypes.byref(mdo), ctypes.byref(mds_present), ctypes.byref(mds), ctypes.byref(mns_present), ctypes.byref(mns), ctypes.byref(mne_present), ctypes.byref(mne), ctypes.byref(mde_present), ctypes.byref(mde), ctypes.byref(adi), ctypes.byref(ado_present), ctypes.byref(ado), ctypes.byref(ads_present), ctypes.byref(ads), ctypes.byref(ans_present), ctypes.byref(ans), ctypes.byref(ane_present), ctypes.byref(ane), ctypes.byref(ade_present), ctypes.byref(ade), ctypes.byref(num_threads_present), ctypes.byref(num_threads), ctypes.byref(config))
+        clib.c_new_model_config(ctypes.byref(adn), ctypes.byref(ado_present), ctypes.byref(ado), ctypes.byref(ads_present), ctypes.byref(ads), ctypes.byref(ans_present), ctypes.byref(ans), ctypes.byref(ane_present), ctypes.byref(ane), ctypes.byref(ade_present), ctypes.byref(ade), ctypes.byref(mdn), ctypes.byref(mdo), ctypes.byref(mds_present), ctypes.byref(mds), ctypes.byref(mns_present), ctypes.byref(mns), ctypes.byref(mne_present), ctypes.byref(mne), ctypes.byref(mde_present), ctypes.byref(mde), ctypes.byref(num_threads_present), ctypes.byref(num_threads), ctypes.byref(config))
+    
+        # Return final results, 'INTENT(OUT)' arguments only.
+        return config
+
+    
+    # ----------------------------------------------
+    # Wrapper for the Fortran subroutine NEW_FIT_CONFIG
+    
+    def new_fit_config(self, nm, na, config):
+        '''! Given a number of X points "NM", and a number of apositional X points
+! "NA", update the "RWORK_SIZE" and "IWORK_SIZE" attributes in "CONFIG"
+! as well as all related work indices for that size data.'''
+        MODEL_CONFIG = apos.MODEL_CONFIG
+        
+        # Setting up "nm"
+        if (type(nm) is not ctypes.c_int): nm = ctypes.c_int(nm)
+        
+        # Setting up "na"
+        if (type(na) is not ctypes.c_int): na = ctypes.c_int(na)
+        
+        # Setting up "config"
+        if (type(config) is not MODEL_CONFIG): config = MODEL_CONFIG(config)
+    
+        # Call C-accessible Fortran wrapper.
+        clib.c_new_fit_config(ctypes.byref(nm), ctypes.byref(na), ctypes.byref(config))
     
         # Return final results, 'INTENT(OUT)' arguments only.
         return config
 
     
     # ----------------------------------------------
     # Wrapper for the Fortran subroutine INIT_MODEL
@@ -421,15 +975,15 @@
         # Return final results, 'INTENT(OUT)' arguments only.
         return model
 
     
     # ----------------------------------------------
     # Wrapper for the Fortran subroutine CHECK_SHAPE
     
-    def check_shape(self, config, model, y, x, xi, ax, axi, sizes):
+    def check_shape(self, config, model, ax, axi, sizes, x, xi, y):
         '''! Returnn nonzero INFO if any shapes or values do not match expectations.'''
         MODEL_CONFIG = apos.MODEL_CONFIG
         
         # Setting up "config"
         if (type(config) is not MODEL_CONFIG): config = MODEL_CONFIG(config)
         
         # Setting up "model"
@@ -437,44 +991,14 @@
             (not numpy.asarray(model).flags.f_contiguous) or
             (not (model.dtype == numpy.dtype(ctypes.c_float)))):
             import warnings
             warnings.warn("The provided argument 'model' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
             model = numpy.asarray(model, dtype=ctypes.c_float, order='F')
         model_dim_1 = ctypes.c_int(model.shape[0])
         
-        # Setting up "y"
-        if ((not issubclass(type(y), numpy.ndarray)) or
-            (not numpy.asarray(y).flags.f_contiguous) or
-            (not (y.dtype == numpy.dtype(ctypes.c_float)))):
-            import warnings
-            warnings.warn("The provided argument 'y' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
-            y = numpy.asarray(y, dtype=ctypes.c_float, order='F')
-        y_dim_1 = ctypes.c_int(y.shape[0])
-        y_dim_2 = ctypes.c_int(y.shape[1])
-        
-        # Setting up "x"
-        if ((not issubclass(type(x), numpy.ndarray)) or
-            (not numpy.asarray(x).flags.f_contiguous) or
-            (not (x.dtype == numpy.dtype(ctypes.c_float)))):
-            import warnings
-            warnings.warn("The provided argument 'x' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
-            x = numpy.asarray(x, dtype=ctypes.c_float, order='F')
-        x_dim_1 = ctypes.c_int(x.shape[0])
-        x_dim_2 = ctypes.c_int(x.shape[1])
-        
-        # Setting up "xi"
-        if ((not issubclass(type(xi), numpy.ndarray)) or
-            (not numpy.asarray(xi).flags.f_contiguous) or
-            (not (xi.dtype == numpy.dtype(ctypes.c_int)))):
-            import warnings
-            warnings.warn("The provided argument 'xi' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
-            xi = numpy.asarray(xi, dtype=ctypes.c_int, order='F')
-        xi_dim_1 = ctypes.c_int(xi.shape[0])
-        xi_dim_2 = ctypes.c_int(xi.shape[1])
-        
         # Setting up "ax"
         if ((not issubclass(type(ax), numpy.ndarray)) or
             (not numpy.asarray(ax).flags.f_contiguous) or
             (not (ax.dtype == numpy.dtype(ctypes.c_float)))):
             import warnings
             warnings.warn("The provided argument 'ax' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
             ax = numpy.asarray(ax, dtype=ctypes.c_float, order='F')
@@ -496,44 +1020,14 @@
             (not numpy.asarray(sizes).flags.f_contiguous) or
             (not (sizes.dtype == numpy.dtype(ctypes.c_int)))):
             import warnings
             warnings.warn("The provided argument 'sizes' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
             sizes = numpy.asarray(sizes, dtype=ctypes.c_int, order='F')
         sizes_dim_1 = ctypes.c_int(sizes.shape[0])
         
-        # Setting up "info"
-        info = ctypes.c_int()
-    
-        # Call C-accessible Fortran wrapper.
-        clib.c_check_shape(ctypes.byref(config), ctypes.byref(model_dim_1), ctypes.c_void_p(model.ctypes.data), ctypes.byref(y_dim_1), ctypes.byref(y_dim_2), ctypes.c_void_p(y.ctypes.data), ctypes.byref(x_dim_1), ctypes.byref(x_dim_2), ctypes.c_void_p(x.ctypes.data), ctypes.byref(xi_dim_1), ctypes.byref(xi_dim_2), ctypes.c_void_p(xi.ctypes.data), ctypes.byref(ax_dim_1), ctypes.byref(ax_dim_2), ctypes.c_void_p(ax.ctypes.data), ctypes.byref(axi_dim_1), ctypes.byref(axi_dim_2), ctypes.c_void_p(axi.ctypes.data), ctypes.byref(sizes_dim_1), ctypes.c_void_p(sizes.ctypes.data), ctypes.byref(info))
-    
-        # Return final results, 'INTENT(OUT)' arguments only.
-        return info.value
-
-    
-    # ----------------------------------------------
-    # Wrapper for the Fortran subroutine EMBED
-    
-    def embed(self, config, model, x, xi, ax, axi, xxi, axxi):
-        '''! Given a model and mixed real and integer inputs, embed the inputs
-!  into their appropriate real-value-only formats.'''
-        MODEL_CONFIG = apos.MODEL_CONFIG
-        
-        # Setting up "config"
-        if (type(config) is not MODEL_CONFIG): config = MODEL_CONFIG(config)
-        
-        # Setting up "model"
-        if ((not issubclass(type(model), numpy.ndarray)) or
-            (not numpy.asarray(model).flags.f_contiguous) or
-            (not (model.dtype == numpy.dtype(ctypes.c_float)))):
-            import warnings
-            warnings.warn("The provided argument 'model' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
-            model = numpy.asarray(model, dtype=ctypes.c_float, order='F')
-        model_dim_1 = ctypes.c_int(model.shape[0])
-        
         # Setting up "x"
         if ((not issubclass(type(x), numpy.ndarray)) or
             (not numpy.asarray(x).flags.f_contiguous) or
             (not (x.dtype == numpy.dtype(ctypes.c_float)))):
             import warnings
             warnings.warn("The provided argument 'x' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
             x = numpy.asarray(x, dtype=ctypes.c_float, order='F')
@@ -546,253 +1040,277 @@
             (not (xi.dtype == numpy.dtype(ctypes.c_int)))):
             import warnings
             warnings.warn("The provided argument 'xi' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
             xi = numpy.asarray(xi, dtype=ctypes.c_int, order='F')
         xi_dim_1 = ctypes.c_int(xi.shape[0])
         xi_dim_2 = ctypes.c_int(xi.shape[1])
         
-        # Setting up "ax"
-        if ((not issubclass(type(ax), numpy.ndarray)) or
-            (not numpy.asarray(ax).flags.f_contiguous) or
-            (not (ax.dtype == numpy.dtype(ctypes.c_float)))):
-            import warnings
-            warnings.warn("The provided argument 'ax' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
-            ax = numpy.asarray(ax, dtype=ctypes.c_float, order='F')
-        ax_dim_1 = ctypes.c_int(ax.shape[0])
-        ax_dim_2 = ctypes.c_int(ax.shape[1])
-        
-        # Setting up "axi"
-        if ((not issubclass(type(axi), numpy.ndarray)) or
-            (not numpy.asarray(axi).flags.f_contiguous) or
-            (not (axi.dtype == numpy.dtype(ctypes.c_int)))):
-            import warnings
-            warnings.warn("The provided argument 'axi' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
-            axi = numpy.asarray(axi, dtype=ctypes.c_int, order='F')
-        axi_dim_1 = ctypes.c_int(axi.shape[0])
-        axi_dim_2 = ctypes.c_int(axi.shape[1])
-        
-        # Setting up "xxi"
-        if ((not issubclass(type(xxi), numpy.ndarray)) or
-            (not numpy.asarray(xxi).flags.f_contiguous) or
-            (not (xxi.dtype == numpy.dtype(ctypes.c_float)))):
+        # Setting up "y"
+        if ((not issubclass(type(y), numpy.ndarray)) or
+            (not numpy.asarray(y).flags.f_contiguous) or
+            (not (y.dtype == numpy.dtype(ctypes.c_float)))):
             import warnings
-            warnings.warn("The provided argument 'xxi' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
-            xxi = numpy.asarray(xxi, dtype=ctypes.c_float, order='F')
-        xxi_dim_1 = ctypes.c_int(xxi.shape[0])
-        xxi_dim_2 = ctypes.c_int(xxi.shape[1])
+            warnings.warn("The provided argument 'y' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            y = numpy.asarray(y, dtype=ctypes.c_float, order='F')
+        y_dim_1 = ctypes.c_int(y.shape[0])
+        y_dim_2 = ctypes.c_int(y.shape[1])
         
-        # Setting up "axxi"
-        if ((not issubclass(type(axxi), numpy.ndarray)) or
-            (not numpy.asarray(axxi).flags.f_contiguous) or
-            (not (axxi.dtype == numpy.dtype(ctypes.c_float)))):
-            import warnings
-            warnings.warn("The provided argument 'axxi' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
-            axxi = numpy.asarray(axxi, dtype=ctypes.c_float, order='F')
-        axxi_dim_1 = ctypes.c_int(axxi.shape[0])
-        axxi_dim_2 = ctypes.c_int(axxi.shape[1])
+        # Setting up "info"
+        info = ctypes.c_int()
     
         # Call C-accessible Fortran wrapper.
-        clib.c_embed(ctypes.byref(config), ctypes.byref(model_dim_1), ctypes.c_void_p(model.ctypes.data), ctypes.byref(x_dim_1), ctypes.byref(x_dim_2), ctypes.c_void_p(x.ctypes.data), ctypes.byref(xi_dim_1), ctypes.byref(xi_dim_2), ctypes.c_void_p(xi.ctypes.data), ctypes.byref(ax_dim_1), ctypes.byref(ax_dim_2), ctypes.c_void_p(ax.ctypes.data), ctypes.byref(axi_dim_1), ctypes.byref(axi_dim_2), ctypes.c_void_p(axi.ctypes.data), ctypes.byref(xxi_dim_1), ctypes.byref(xxi_dim_2), ctypes.c_void_p(xxi.ctypes.data), ctypes.byref(axxi_dim_1), ctypes.byref(axxi_dim_2), ctypes.c_void_p(axxi.ctypes.data))
+        clib.c_check_shape(ctypes.byref(config), ctypes.byref(model_dim_1), ctypes.c_void_p(model.ctypes.data), ctypes.byref(ax_dim_1), ctypes.byref(ax_dim_2), ctypes.c_void_p(ax.ctypes.data), ctypes.byref(axi_dim_1), ctypes.byref(axi_dim_2), ctypes.c_void_p(axi.ctypes.data), ctypes.byref(sizes_dim_1), ctypes.c_void_p(sizes.ctypes.data), ctypes.byref(x_dim_1), ctypes.byref(x_dim_2), ctypes.c_void_p(x.ctypes.data), ctypes.byref(xi_dim_1), ctypes.byref(xi_dim_2), ctypes.c_void_p(xi.ctypes.data), ctypes.byref(y_dim_1), ctypes.byref(y_dim_2), ctypes.c_void_p(y.ctypes.data), ctypes.byref(info))
     
         # Return final results, 'INTENT(OUT)' arguments only.
-        return xxi, axxi
+        return info.value
 
     
     # ----------------------------------------------
     # Wrapper for the Fortran subroutine COMPUTE_BATCHES
     
-    def compute_batches(self, num_batches, x, ax, sizes, batcha, batchm, info):
+    def compute_batches(self, num_batches, nm, na, sizes, batcha_starts, batcha_ends, batchm_starts, batchm_ends, info):
         '''! Given a number of batches, compute the batch start and ends for
 !  the apositional and positional inputs. Store in (2,_) arrays.'''
         MODEL_CONFIG = apos.MODEL_CONFIG
         
         # Setting up "num_batches"
         if (type(num_batches) is not ctypes.c_int): num_batches = ctypes.c_int(num_batches)
         
-        # Setting up "x"
-        if ((not issubclass(type(x), numpy.ndarray)) or
-            (not numpy.asarray(x).flags.f_contiguous) or
-            (not (x.dtype == numpy.dtype(ctypes.c_float)))):
-            import warnings
-            warnings.warn("The provided argument 'x' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
-            x = numpy.asarray(x, dtype=ctypes.c_float, order='F')
-        x_dim_1 = ctypes.c_int(x.shape[0])
-        x_dim_2 = ctypes.c_int(x.shape[1])
+        # Setting up "nm"
+        if (type(nm) is not ctypes.c_int): nm = ctypes.c_int(nm)
         
-        # Setting up "ax"
-        if ((not issubclass(type(ax), numpy.ndarray)) or
-            (not numpy.asarray(ax).flags.f_contiguous) or
-            (not (ax.dtype == numpy.dtype(ctypes.c_float)))):
-            import warnings
-            warnings.warn("The provided argument 'ax' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
-            ax = numpy.asarray(ax, dtype=ctypes.c_float, order='F')
-        ax_dim_1 = ctypes.c_int(ax.shape[0])
-        ax_dim_2 = ctypes.c_int(ax.shape[1])
+        # Setting up "na"
+        if (type(na) is not ctypes.c_int): na = ctypes.c_int(na)
         
         # Setting up "sizes"
         if ((not issubclass(type(sizes), numpy.ndarray)) or
             (not numpy.asarray(sizes).flags.f_contiguous) or
             (not (sizes.dtype == numpy.dtype(ctypes.c_int)))):
             import warnings
             warnings.warn("The provided argument 'sizes' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
             sizes = numpy.asarray(sizes, dtype=ctypes.c_int, order='F')
         sizes_dim_1 = ctypes.c_int(sizes.shape[0])
         
-        # Setting up "batcha"
-        if ((not issubclass(type(batcha), numpy.ndarray)) or
-            (not numpy.asarray(batcha).flags.f_contiguous) or
-            (not (batcha.dtype == numpy.dtype(ctypes.c_int)))):
-            import warnings
-            warnings.warn("The provided argument 'batcha' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
-            batcha = numpy.asarray(batcha, dtype=ctypes.c_int, order='F')
-        batcha_dim_1 = ctypes.c_int(batcha.shape[0])
-        batcha_dim_2 = ctypes.c_int(batcha.shape[1])
-        
-        # Setting up "batchm"
-        if ((not issubclass(type(batchm), numpy.ndarray)) or
-            (not numpy.asarray(batchm).flags.f_contiguous) or
-            (not (batchm.dtype == numpy.dtype(ctypes.c_int)))):
-            import warnings
-            warnings.warn("The provided argument 'batchm' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
-            batchm = numpy.asarray(batchm, dtype=ctypes.c_int, order='F')
-        batchm_dim_1 = ctypes.c_int(batchm.shape[0])
-        batchm_dim_2 = ctypes.c_int(batchm.shape[1])
+        # Setting up "batcha_starts"
+        if ((not issubclass(type(batcha_starts), numpy.ndarray)) or
+            (not numpy.asarray(batcha_starts).flags.f_contiguous) or
+            (not (batcha_starts.dtype == numpy.dtype(ctypes.c_int)))):
+            import warnings
+            warnings.warn("The provided argument 'batcha_starts' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
+            batcha_starts = numpy.asarray(batcha_starts, dtype=ctypes.c_int, order='F')
+        batcha_starts_dim_1 = ctypes.c_int(batcha_starts.shape[0])
+        
+        # Setting up "batcha_ends"
+        if ((not issubclass(type(batcha_ends), numpy.ndarray)) or
+            (not numpy.asarray(batcha_ends).flags.f_contiguous) or
+            (not (batcha_ends.dtype == numpy.dtype(ctypes.c_int)))):
+            import warnings
+            warnings.warn("The provided argument 'batcha_ends' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
+            batcha_ends = numpy.asarray(batcha_ends, dtype=ctypes.c_int, order='F')
+        batcha_ends_dim_1 = ctypes.c_int(batcha_ends.shape[0])
+        
+        # Setting up "batchm_starts"
+        if ((not issubclass(type(batchm_starts), numpy.ndarray)) or
+            (not numpy.asarray(batchm_starts).flags.f_contiguous) or
+            (not (batchm_starts.dtype == numpy.dtype(ctypes.c_int)))):
+            import warnings
+            warnings.warn("The provided argument 'batchm_starts' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
+            batchm_starts = numpy.asarray(batchm_starts, dtype=ctypes.c_int, order='F')
+        batchm_starts_dim_1 = ctypes.c_int(batchm_starts.shape[0])
+        
+        # Setting up "batchm_ends"
+        if ((not issubclass(type(batchm_ends), numpy.ndarray)) or
+            (not numpy.asarray(batchm_ends).flags.f_contiguous) or
+            (not (batchm_ends.dtype == numpy.dtype(ctypes.c_int)))):
+            import warnings
+            warnings.warn("The provided argument 'batchm_ends' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
+            batchm_ends = numpy.asarray(batchm_ends, dtype=ctypes.c_int, order='F')
+        batchm_ends_dim_1 = ctypes.c_int(batchm_ends.shape[0])
         
         # Setting up "info"
         if (type(info) is not ctypes.c_int): info = ctypes.c_int(info)
     
         # Call C-accessible Fortran wrapper.
-        clib.c_compute_batches(ctypes.byref(num_batches), ctypes.byref(x_dim_1), ctypes.byref(x_dim_2), ctypes.c_void_p(x.ctypes.data), ctypes.byref(ax_dim_1), ctypes.byref(ax_dim_2), ctypes.c_void_p(ax.ctypes.data), ctypes.byref(sizes_dim_1), ctypes.c_void_p(sizes.ctypes.data), ctypes.byref(batcha_dim_1), ctypes.byref(batcha_dim_2), ctypes.c_void_p(batcha.ctypes.data), ctypes.byref(batchm_dim_1), ctypes.byref(batchm_dim_2), ctypes.c_void_p(batchm.ctypes.data), ctypes.byref(info))
+        clib.c_compute_batches(ctypes.byref(num_batches), ctypes.byref(nm), ctypes.byref(na), ctypes.byref(sizes_dim_1), ctypes.c_void_p(sizes.ctypes.data), ctypes.byref(batcha_starts_dim_1), ctypes.c_void_p(batcha_starts.ctypes.data), ctypes.byref(batcha_ends_dim_1), ctypes.c_void_p(batcha_ends.ctypes.data), ctypes.byref(batchm_starts_dim_1), ctypes.c_void_p(batchm_starts.ctypes.data), ctypes.byref(batchm_ends_dim_1), ctypes.c_void_p(batchm_ends.ctypes.data), ctypes.byref(info))
     
         # Return final results, 'INTENT(OUT)' arguments only.
-        return batcha, batchm, info.value
+        return batcha_starts, batcha_ends, batchm_starts, batchm_ends, info.value
 
     
     # ----------------------------------------------
-    # Wrapper for the Fortran subroutine EVALUATE
+    # Wrapper for the Fortran subroutine EMBED
     
-    def evaluate(self, config, model, y, x, ax, sizes, m_states, a_states, ay, info, shift=None, threads=None):
-        '''! Evaluate the piecewise linear regression model, assume already-embedded inputs.'''
+    def embed(self, config, model, axi, xi, ax, x):
+        '''! Given a model and mixed real and integer inputs, embed the integer
+!  inputs into their appropriate real-value-only formats.'''
         MODEL_CONFIG = apos.MODEL_CONFIG
         
         # Setting up "config"
         if (type(config) is not MODEL_CONFIG): config = MODEL_CONFIG(config)
         
         # Setting up "model"
         if ((not issubclass(type(model), numpy.ndarray)) or
             (not numpy.asarray(model).flags.f_contiguous) or
             (not (model.dtype == numpy.dtype(ctypes.c_float)))):
             import warnings
             warnings.warn("The provided argument 'model' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
             model = numpy.asarray(model, dtype=ctypes.c_float, order='F')
         model_dim_1 = ctypes.c_int(model.shape[0])
         
-        # Setting up "y"
-        if ((not issubclass(type(y), numpy.ndarray)) or
-            (not numpy.asarray(y).flags.f_contiguous) or
-            (not (y.dtype == numpy.dtype(ctypes.c_float)))):
+        # Setting up "axi"
+        if ((not issubclass(type(axi), numpy.ndarray)) or
+            (not numpy.asarray(axi).flags.f_contiguous) or
+            (not (axi.dtype == numpy.dtype(ctypes.c_int)))):
             import warnings
-            warnings.warn("The provided argument 'y' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
-            y = numpy.asarray(y, dtype=ctypes.c_float, order='F')
-        y_dim_1 = ctypes.c_int(y.shape[0])
-        y_dim_2 = ctypes.c_int(y.shape[1])
+            warnings.warn("The provided argument 'axi' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
+            axi = numpy.asarray(axi, dtype=ctypes.c_int, order='F')
+        axi_dim_1 = ctypes.c_int(axi.shape[0])
+        axi_dim_2 = ctypes.c_int(axi.shape[1])
+        
+        # Setting up "xi"
+        if ((not issubclass(type(xi), numpy.ndarray)) or
+            (not numpy.asarray(xi).flags.f_contiguous) or
+            (not (xi.dtype == numpy.dtype(ctypes.c_int)))):
+            import warnings
+            warnings.warn("The provided argument 'xi' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
+            xi = numpy.asarray(xi, dtype=ctypes.c_int, order='F')
+        xi_dim_1 = ctypes.c_int(xi.shape[0])
+        xi_dim_2 = ctypes.c_int(xi.shape[1])
+        
+        # Setting up "ax"
+        if ((not issubclass(type(ax), numpy.ndarray)) or
+            (not numpy.asarray(ax).flags.f_contiguous) or
+            (not (ax.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 'ax' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            ax = numpy.asarray(ax, dtype=ctypes.c_float, order='F')
+        ax_dim_1 = ctypes.c_int(ax.shape[0])
+        ax_dim_2 = ctypes.c_int(ax.shape[1])
         
         # Setting up "x"
         if ((not issubclass(type(x), numpy.ndarray)) or
             (not numpy.asarray(x).flags.f_contiguous) or
             (not (x.dtype == numpy.dtype(ctypes.c_float)))):
             import warnings
             warnings.warn("The provided argument 'x' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
             x = numpy.asarray(x, dtype=ctypes.c_float, order='F')
         x_dim_1 = ctypes.c_int(x.shape[0])
         x_dim_2 = ctypes.c_int(x.shape[1])
+    
+        # Call C-accessible Fortran wrapper.
+        clib.c_embed(ctypes.byref(config), ctypes.byref(model_dim_1), ctypes.c_void_p(model.ctypes.data), ctypes.byref(axi_dim_1), ctypes.byref(axi_dim_2), ctypes.c_void_p(axi.ctypes.data), ctypes.byref(xi_dim_1), ctypes.byref(xi_dim_2), ctypes.c_void_p(xi.ctypes.data), ctypes.byref(ax_dim_1), ctypes.byref(ax_dim_2), ctypes.c_void_p(ax.ctypes.data), ctypes.byref(x_dim_1), ctypes.byref(x_dim_2), ctypes.c_void_p(x.ctypes.data))
+    
+        # Return final results, 'INTENT(OUT)' arguments only.
+        return ax, x
+
+    
+    # ----------------------------------------------
+    # Wrapper for the Fortran subroutine EVALUATE
+    
+    def evaluate(self, config, model, ax, ay, sizes, x, y, a_states, m_states, info):
+        '''! Evaluate the piecewise linear regression model, assume already-embedded inputs.'''
+        MODEL_CONFIG = apos.MODEL_CONFIG
+        
+        # Setting up "config"
+        if (type(config) is not MODEL_CONFIG): config = MODEL_CONFIG(config)
+        
+        # Setting up "model"
+        if ((not issubclass(type(model), numpy.ndarray)) or
+            (not numpy.asarray(model).flags.f_contiguous) or
+            (not (model.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 'model' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            model = numpy.asarray(model, dtype=ctypes.c_float, order='F')
+        model_dim_1 = ctypes.c_int(model.shape[0])
         
         # Setting up "ax"
         if ((not issubclass(type(ax), numpy.ndarray)) or
             (not numpy.asarray(ax).flags.f_contiguous) or
             (not (ax.dtype == numpy.dtype(ctypes.c_float)))):
             import warnings
             warnings.warn("The provided argument 'ax' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
             ax = numpy.asarray(ax, dtype=ctypes.c_float, order='F')
         ax_dim_1 = ctypes.c_int(ax.shape[0])
         ax_dim_2 = ctypes.c_int(ax.shape[1])
         
+        # Setting up "ay"
+        if ((not issubclass(type(ay), numpy.ndarray)) or
+            (not numpy.asarray(ay).flags.f_contiguous) or
+            (not (ay.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 'ay' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            ay = numpy.asarray(ay, dtype=ctypes.c_float, order='F')
+        ay_dim_1 = ctypes.c_int(ay.shape[0])
+        ay_dim_2 = ctypes.c_int(ay.shape[1])
+        
         # Setting up "sizes"
         if ((not issubclass(type(sizes), numpy.ndarray)) or
             (not numpy.asarray(sizes).flags.f_contiguous) or
             (not (sizes.dtype == numpy.dtype(ctypes.c_int)))):
             import warnings
             warnings.warn("The provided argument 'sizes' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
             sizes = numpy.asarray(sizes, dtype=ctypes.c_int, order='F')
         sizes_dim_1 = ctypes.c_int(sizes.shape[0])
         
-        # Setting up "m_states"
-        if ((not issubclass(type(m_states), numpy.ndarray)) or
-            (not numpy.asarray(m_states).flags.f_contiguous) or
-            (not (m_states.dtype == numpy.dtype(ctypes.c_float)))):
+        # Setting up "x"
+        if ((not issubclass(type(x), numpy.ndarray)) or
+            (not numpy.asarray(x).flags.f_contiguous) or
+            (not (x.dtype == numpy.dtype(ctypes.c_float)))):
             import warnings
-            warnings.warn("The provided argument 'm_states' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
-            m_states = numpy.asarray(m_states, dtype=ctypes.c_float, order='F')
-        m_states_dim_1 = ctypes.c_int(m_states.shape[0])
-        m_states_dim_2 = ctypes.c_int(m_states.shape[1])
-        m_states_dim_3 = ctypes.c_int(m_states.shape[2])
+            warnings.warn("The provided argument 'x' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            x = numpy.asarray(x, dtype=ctypes.c_float, order='F')
+        x_dim_1 = ctypes.c_int(x.shape[0])
+        x_dim_2 = ctypes.c_int(x.shape[1])
+        
+        # Setting up "y"
+        if ((not issubclass(type(y), numpy.ndarray)) or
+            (not numpy.asarray(y).flags.f_contiguous) or
+            (not (y.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 'y' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            y = numpy.asarray(y, dtype=ctypes.c_float, order='F')
+        y_dim_1 = ctypes.c_int(y.shape[0])
+        y_dim_2 = ctypes.c_int(y.shape[1])
         
         # Setting up "a_states"
         if ((not issubclass(type(a_states), numpy.ndarray)) or
             (not numpy.asarray(a_states).flags.f_contiguous) or
             (not (a_states.dtype == numpy.dtype(ctypes.c_float)))):
             import warnings
             warnings.warn("The provided argument 'a_states' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
             a_states = numpy.asarray(a_states, dtype=ctypes.c_float, order='F')
         a_states_dim_1 = ctypes.c_int(a_states.shape[0])
         a_states_dim_2 = ctypes.c_int(a_states.shape[1])
         a_states_dim_3 = ctypes.c_int(a_states.shape[2])
         
-        # Setting up "ay"
-        if ((not issubclass(type(ay), numpy.ndarray)) or
-            (not numpy.asarray(ay).flags.f_contiguous) or
-            (not (ay.dtype == numpy.dtype(ctypes.c_float)))):
+        # Setting up "m_states"
+        if ((not issubclass(type(m_states), numpy.ndarray)) or
+            (not numpy.asarray(m_states).flags.f_contiguous) or
+            (not (m_states.dtype == numpy.dtype(ctypes.c_float)))):
             import warnings
-            warnings.warn("The provided argument 'ay' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
-            ay = numpy.asarray(ay, dtype=ctypes.c_float, order='F')
-        ay_dim_1 = ctypes.c_int(ay.shape[0])
-        ay_dim_2 = ctypes.c_int(ay.shape[1])
+            warnings.warn("The provided argument 'm_states' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            m_states = numpy.asarray(m_states, dtype=ctypes.c_float, order='F')
+        m_states_dim_1 = ctypes.c_int(m_states.shape[0])
+        m_states_dim_2 = ctypes.c_int(m_states.shape[1])
+        m_states_dim_3 = ctypes.c_int(m_states.shape[2])
         
         # Setting up "info"
         if (type(info) is not ctypes.c_int): info = ctypes.c_int(info)
-        
-        # Setting up "shift"
-        shift_present = ctypes.c_bool(True)
-        if (shift is None):
-            shift_present = ctypes.c_bool(False)
-            shift = ctypes.c_bool()
-        else:
-            shift = ctypes.c_bool(shift)
-        if (type(shift) is not ctypes.c_bool): shift = ctypes.c_bool(shift)
-        
-        # Setting up "threads"
-        threads_present = ctypes.c_bool(True)
-        if (threads is None):
-            threads_present = ctypes.c_bool(False)
-            threads = ctypes.c_int()
-        else:
-            threads = ctypes.c_int(threads)
-        if (type(threads) is not ctypes.c_int): threads = ctypes.c_int(threads)
     
         # Call C-accessible Fortran wrapper.
-        clib.c_evaluate(ctypes.byref(config), ctypes.byref(model_dim_1), ctypes.c_void_p(model.ctypes.data), ctypes.byref(y_dim_1), ctypes.byref(y_dim_2), ctypes.c_void_p(y.ctypes.data), ctypes.byref(x_dim_1), ctypes.byref(x_dim_2), ctypes.c_void_p(x.ctypes.data), ctypes.byref(ax_dim_1), ctypes.byref(ax_dim_2), ctypes.c_void_p(ax.ctypes.data), ctypes.byref(sizes_dim_1), ctypes.c_void_p(sizes.ctypes.data), ctypes.byref(m_states_dim_1), ctypes.byref(m_states_dim_2), ctypes.byref(m_states_dim_3), ctypes.c_void_p(m_states.ctypes.data), ctypes.byref(a_states_dim_1), ctypes.byref(a_states_dim_2), ctypes.byref(a_states_dim_3), ctypes.c_void_p(a_states.ctypes.data), ctypes.byref(ay_dim_1), ctypes.byref(ay_dim_2), ctypes.c_void_p(ay.ctypes.data), ctypes.byref(info), ctypes.byref(shift_present), ctypes.byref(shift), ctypes.byref(threads_present), ctypes.byref(threads))
+        clib.c_evaluate(ctypes.byref(config), ctypes.byref(model_dim_1), ctypes.c_void_p(model.ctypes.data), ctypes.byref(ax_dim_1), ctypes.byref(ax_dim_2), ctypes.c_void_p(ax.ctypes.data), ctypes.byref(ay_dim_1), ctypes.byref(ay_dim_2), ctypes.c_void_p(ay.ctypes.data), ctypes.byref(sizes_dim_1), ctypes.c_void_p(sizes.ctypes.data), ctypes.byref(x_dim_1), ctypes.byref(x_dim_2), ctypes.c_void_p(x.ctypes.data), ctypes.byref(y_dim_1), ctypes.byref(y_dim_2), ctypes.c_void_p(y.ctypes.data), ctypes.byref(a_states_dim_1), ctypes.byref(a_states_dim_2), ctypes.byref(a_states_dim_3), ctypes.c_void_p(a_states.ctypes.data), ctypes.byref(m_states_dim_1), ctypes.byref(m_states_dim_2), ctypes.byref(m_states_dim_3), ctypes.c_void_p(m_states.ctypes.data), ctypes.byref(info))
     
         # Return final results, 'INTENT(OUT)' arguments only.
-        return y, x, ax, m_states, a_states, ay, info.value
+        return ax, ay, x, y, a_states, m_states, info.value
 
     
     # ----------------------------------------------
     # Wrapper for the Fortran subroutine BASIS_GRADIENT
     
-    def basis_gradient(self, config, model, y, x, ax, sizes, m_states, a_states, ay, grad, skip_embeddings=None):
+    def basis_gradient(self, config, model, y, x, ax, sizes, m_states, a_states, ay, grad):
         '''! Given the values at all internal states in the model and an output
 !  gradient, propogate the output gradient through the model and
 !  return the gradient of all basis functions.'''
         MODEL_CONFIG = apos.MODEL_CONFIG
         
         # Setting up "config"
         if (type(config) is not MODEL_CONFIG): config = MODEL_CONFIG(config)
@@ -881,26 +1399,17 @@
         if ((not issubclass(type(grad), numpy.ndarray)) or
             (not numpy.asarray(grad).flags.f_contiguous) or
             (not (grad.dtype == numpy.dtype(ctypes.c_float)))):
             import warnings
             warnings.warn("The provided argument 'grad' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
             grad = numpy.asarray(grad, dtype=ctypes.c_float, order='F')
         grad_dim_1 = ctypes.c_int(grad.shape[0])
-        
-        # Setting up "skip_embeddings"
-        skip_embeddings_present = ctypes.c_bool(True)
-        if (skip_embeddings is None):
-            skip_embeddings_present = ctypes.c_bool(False)
-            skip_embeddings = ctypes.c_bool()
-        else:
-            skip_embeddings = ctypes.c_bool(skip_embeddings)
-        if (type(skip_embeddings) is not ctypes.c_bool): skip_embeddings = ctypes.c_bool(skip_embeddings)
     
         # Call C-accessible Fortran wrapper.
-        clib.c_basis_gradient(ctypes.byref(config), ctypes.byref(model_dim_1), ctypes.c_void_p(model.ctypes.data), ctypes.byref(y_dim_1), ctypes.byref(y_dim_2), ctypes.c_void_p(y.ctypes.data), ctypes.byref(x_dim_1), ctypes.byref(x_dim_2), ctypes.c_void_p(x.ctypes.data), ctypes.byref(ax_dim_1), ctypes.byref(ax_dim_2), ctypes.c_void_p(ax.ctypes.data), ctypes.byref(sizes_dim_1), ctypes.c_void_p(sizes.ctypes.data), ctypes.byref(m_states_dim_1), ctypes.byref(m_states_dim_2), ctypes.byref(m_states_dim_3), ctypes.c_void_p(m_states.ctypes.data), ctypes.byref(a_states_dim_1), ctypes.byref(a_states_dim_2), ctypes.byref(a_states_dim_3), ctypes.c_void_p(a_states.ctypes.data), ctypes.byref(ay_dim_1), ctypes.byref(ay_dim_2), ctypes.c_void_p(ay.ctypes.data), ctypes.byref(grad_dim_1), ctypes.c_void_p(grad.ctypes.data), ctypes.byref(skip_embeddings_present), ctypes.byref(skip_embeddings))
+        clib.c_basis_gradient(ctypes.byref(config), ctypes.byref(model_dim_1), ctypes.c_void_p(model.ctypes.data), ctypes.byref(y_dim_1), ctypes.byref(y_dim_2), ctypes.c_void_p(y.ctypes.data), ctypes.byref(x_dim_1), ctypes.byref(x_dim_2), ctypes.c_void_p(x.ctypes.data), ctypes.byref(ax_dim_1), ctypes.byref(ax_dim_2), ctypes.c_void_p(ax.ctypes.data), ctypes.byref(sizes_dim_1), ctypes.c_void_p(sizes.ctypes.data), ctypes.byref(m_states_dim_1), ctypes.byref(m_states_dim_2), ctypes.byref(m_states_dim_3), ctypes.c_void_p(m_states.ctypes.data), ctypes.byref(a_states_dim_1), ctypes.byref(a_states_dim_2), ctypes.byref(a_states_dim_3), ctypes.c_void_p(a_states.ctypes.data), ctypes.byref(ay_dim_1), ctypes.byref(ay_dim_2), ctypes.c_void_p(ay.ctypes.data), ctypes.byref(grad_dim_1), ctypes.c_void_p(grad.ctypes.data))
     
         # Return final results, 'INTENT(OUT)' arguments only.
         return x, ax, m_states, a_states, ay, grad
 
     
     # ----------------------------------------------
     # Wrapper for the Fortran subroutine EMBEDDING_GRADIENT
@@ -950,88 +1459,17 @@
         clib.c_embedding_gradient(ctypes.byref(mde), ctypes.byref(mne), ctypes.byref(int_inputs_dim_1), ctypes.byref(int_inputs_dim_2), ctypes.c_void_p(int_inputs.ctypes.data), ctypes.byref(grad_dim_1), ctypes.byref(grad_dim_2), ctypes.c_void_p(grad.ctypes.data), ctypes.byref(embedding_grad_dim_1), ctypes.byref(embedding_grad_dim_2), ctypes.c_void_p(embedding_grad.ctypes.data))
     
         # Return final results, 'INTENT(OUT)' arguments only.
         return embedding_grad
 
     
     # ----------------------------------------------
-    # Wrapper for the Fortran subroutine SQUARED_ERROR_GRADIENT
-    
-    def squared_error_gradient(self, targets, outputs):
-        '''! Compute the sum of squared error, store the gradient in the OUTPUTS.
-!   TARGETS - row vectors containing target values
-!   OUTPUTS - column vectors containing model predictions'''
-        MODEL_CONFIG = apos.MODEL_CONFIG
-        
-        # Setting up "targets"
-        if ((not issubclass(type(targets), numpy.ndarray)) or
-            (not numpy.asarray(targets).flags.f_contiguous) or
-            (not (targets.dtype == numpy.dtype(ctypes.c_float)))):
-            import warnings
-            warnings.warn("The provided argument 'targets' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
-            targets = numpy.asarray(targets, dtype=ctypes.c_float, order='F')
-        targets_dim_1 = ctypes.c_int(targets.shape[0])
-        targets_dim_2 = ctypes.c_int(targets.shape[1])
-        
-        # Setting up "outputs"
-        if ((not issubclass(type(outputs), numpy.ndarray)) or
-            (not numpy.asarray(outputs).flags.f_contiguous) or
-            (not (outputs.dtype == numpy.dtype(ctypes.c_float)))):
-            import warnings
-            warnings.warn("The provided argument 'outputs' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
-            outputs = numpy.asarray(outputs, dtype=ctypes.c_float, order='F')
-        outputs_dim_1 = ctypes.c_int(outputs.shape[0])
-        outputs_dim_2 = ctypes.c_int(outputs.shape[1])
-    
-        # Call C-accessible Fortran wrapper.
-        clib.c_squared_error_gradient(ctypes.byref(targets_dim_1), ctypes.byref(targets_dim_2), ctypes.c_void_p(targets.ctypes.data), ctypes.byref(outputs_dim_1), ctypes.byref(outputs_dim_2), ctypes.c_void_p(outputs.ctypes.data))
-    
-        # Return final results, 'INTENT(OUT)' arguments only.
-        return outputs
-
-    
-    # ----------------------------------------------
-    # Wrapper for the Fortran subroutine TRUE_VALUE_GRADIENT
-    
-    def true_value_gradient(self, targets, outputs):
-        '''! Produce the true values as the gradient (which will show large
-!  magnitudes for parameters in the model that align with values).'''
-        MODEL_CONFIG = apos.MODEL_CONFIG
-        
-        # Setting up "targets"
-        if ((not issubclass(type(targets), numpy.ndarray)) or
-            (not numpy.asarray(targets).flags.f_contiguous) or
-            (not (targets.dtype == numpy.dtype(ctypes.c_float)))):
-            import warnings
-            warnings.warn("The provided argument 'targets' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
-            targets = numpy.asarray(targets, dtype=ctypes.c_float, order='F')
-        targets_dim_1 = ctypes.c_int(targets.shape[0])
-        targets_dim_2 = ctypes.c_int(targets.shape[1])
-        
-        # Setting up "outputs"
-        if ((not issubclass(type(outputs), numpy.ndarray)) or
-            (not numpy.asarray(outputs).flags.f_contiguous) or
-            (not (outputs.dtype == numpy.dtype(ctypes.c_float)))):
-            import warnings
-            warnings.warn("The provided argument 'outputs' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
-            outputs = numpy.asarray(outputs, dtype=ctypes.c_float, order='F')
-        outputs_dim_1 = ctypes.c_int(outputs.shape[0])
-        outputs_dim_2 = ctypes.c_int(outputs.shape[1])
-    
-        # Call C-accessible Fortran wrapper.
-        clib.c_true_value_gradient(ctypes.byref(targets_dim_1), ctypes.byref(targets_dim_2), ctypes.c_void_p(targets.ctypes.data), ctypes.byref(outputs_dim_1), ctypes.byref(outputs_dim_2), ctypes.c_void_p(outputs.ctypes.data))
-    
-        # Return final results, 'INTENT(OUT)' arguments only.
-        return outputs
-
-    
-    # ----------------------------------------------
     # Wrapper for the Fortran subroutine MINIMIZE_MSE
     
-    def minimize_mse(self, config, model, y, x, xi, ax, axi, sizes, steps, record=None):
+    def minimize_mse(self, config, model, rwork, iwork, ax, axi, sizes, x, xi, y, steps, record=None):
         '''! Fit input / output pairs by minimizing mean squared error.'''
         MODEL_CONFIG = apos.MODEL_CONFIG
         
         # Setting up "config"
         if (type(config) is not MODEL_CONFIG): config = MODEL_CONFIG(config)
         
         # Setting up "model"
@@ -1039,43 +1477,31 @@
             (not numpy.asarray(model).flags.f_contiguous) or
             (not (model.dtype == numpy.dtype(ctypes.c_float)))):
             import warnings
             warnings.warn("The provided argument 'model' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
             model = numpy.asarray(model, dtype=ctypes.c_float, order='F')
         model_dim_1 = ctypes.c_int(model.shape[0])
         
-        # Setting up "y"
-        if ((not issubclass(type(y), numpy.ndarray)) or
-            (not numpy.asarray(y).flags.f_contiguous) or
-            (not (y.dtype == numpy.dtype(ctypes.c_float)))):
-            import warnings
-            warnings.warn("The provided argument 'y' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
-            y = numpy.asarray(y, dtype=ctypes.c_float, order='F')
-        y_dim_1 = ctypes.c_int(y.shape[0])
-        y_dim_2 = ctypes.c_int(y.shape[1])
-        
-        # Setting up "x"
-        if ((not issubclass(type(x), numpy.ndarray)) or
-            (not numpy.asarray(x).flags.f_contiguous) or
-            (not (x.dtype == numpy.dtype(ctypes.c_float)))):
-            import warnings
-            warnings.warn("The provided argument 'x' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
-            x = numpy.asarray(x, dtype=ctypes.c_float, order='F')
-        x_dim_1 = ctypes.c_int(x.shape[0])
-        x_dim_2 = ctypes.c_int(x.shape[1])
-        
-        # Setting up "xi"
-        if ((not issubclass(type(xi), numpy.ndarray)) or
-            (not numpy.asarray(xi).flags.f_contiguous) or
-            (not (xi.dtype == numpy.dtype(ctypes.c_int)))):
-            import warnings
-            warnings.warn("The provided argument 'xi' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
-            xi = numpy.asarray(xi, dtype=ctypes.c_int, order='F')
-        xi_dim_1 = ctypes.c_int(xi.shape[0])
-        xi_dim_2 = ctypes.c_int(xi.shape[1])
+        # Setting up "rwork"
+        if ((not issubclass(type(rwork), numpy.ndarray)) or
+            (not numpy.asarray(rwork).flags.f_contiguous) or
+            (not (rwork.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 'rwork' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            rwork = numpy.asarray(rwork, dtype=ctypes.c_float, order='F')
+        rwork_dim_1 = ctypes.c_int(rwork.shape[0])
+        
+        # Setting up "iwork"
+        if ((not issubclass(type(iwork), numpy.ndarray)) or
+            (not numpy.asarray(iwork).flags.f_contiguous) or
+            (not (iwork.dtype == numpy.dtype(ctypes.c_int)))):
+            import warnings
+            warnings.warn("The provided argument 'iwork' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
+            iwork = numpy.asarray(iwork, dtype=ctypes.c_int, order='F')
+        iwork_dim_1 = ctypes.c_int(iwork.shape[0])
         
         # Setting up "ax"
         if ((not issubclass(type(ax), numpy.ndarray)) or
             (not numpy.asarray(ax).flags.f_contiguous) or
             (not (ax.dtype == numpy.dtype(ctypes.c_float)))):
             import warnings
             warnings.warn("The provided argument 'ax' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
@@ -1098,44 +1524,74 @@
             (not numpy.asarray(sizes).flags.f_contiguous) or
             (not (sizes.dtype == numpy.dtype(ctypes.c_int)))):
             import warnings
             warnings.warn("The provided argument 'sizes' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
             sizes = numpy.asarray(sizes, dtype=ctypes.c_int, order='F')
         sizes_dim_1 = ctypes.c_int(sizes.shape[0])
         
+        # Setting up "x"
+        if ((not issubclass(type(x), numpy.ndarray)) or
+            (not numpy.asarray(x).flags.f_contiguous) or
+            (not (x.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 'x' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            x = numpy.asarray(x, dtype=ctypes.c_float, order='F')
+        x_dim_1 = ctypes.c_int(x.shape[0])
+        x_dim_2 = ctypes.c_int(x.shape[1])
+        
+        # Setting up "xi"
+        if ((not issubclass(type(xi), numpy.ndarray)) or
+            (not numpy.asarray(xi).flags.f_contiguous) or
+            (not (xi.dtype == numpy.dtype(ctypes.c_int)))):
+            import warnings
+            warnings.warn("The provided argument 'xi' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
+            xi = numpy.asarray(xi, dtype=ctypes.c_int, order='F')
+        xi_dim_1 = ctypes.c_int(xi.shape[0])
+        xi_dim_2 = ctypes.c_int(xi.shape[1])
+        
+        # Setting up "y"
+        if ((not issubclass(type(y), numpy.ndarray)) or
+            (not numpy.asarray(y).flags.f_contiguous) or
+            (not (y.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 'y' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            y = numpy.asarray(y, dtype=ctypes.c_float, order='F')
+        y_dim_1 = ctypes.c_int(y.shape[0])
+        y_dim_2 = ctypes.c_int(y.shape[1])
+        
         # Setting up "steps"
         if (type(steps) is not ctypes.c_int): steps = ctypes.c_int(steps)
         
-        # Setting up "sum_squared_error"
-        sum_squared_error = ctypes.c_float()
-        
         # Setting up "record"
         record_present = ctypes.c_bool(True)
         if (record is None):
             record_present = ctypes.c_bool(False)
             record = numpy.zeros(shape=(1,1), dtype=ctypes.c_float, order='F')
         elif (type(record) == bool) and (record):
-            record = numpy.zeros(shape=(4, steps), dtype=ctypes.c_float, order='F')
+            record = numpy.zeros(shape=(6, steps), dtype=ctypes.c_float, order='F')
         elif ((not issubclass(type(record), numpy.ndarray)) or
               (not numpy.asarray(record).flags.f_contiguous) or
               (not (record.dtype == numpy.dtype(ctypes.c_float)))):
             import warnings
             warnings.warn("The provided argument 'record' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
             record = numpy.asarray(record, dtype=ctypes.c_float, order='F')
         if (record_present):
             record_dim_1 = ctypes.c_int(record.shape[0])
             record_dim_2 = ctypes.c_int(record.shape[1])
         else:
             record_dim_1 = ctypes.c_int()
             record_dim_2 = ctypes.c_int()
         
+        # Setting up "sum_squared_error"
+        sum_squared_error = ctypes.c_float()
+        
         # Setting up "info"
         info = ctypes.c_int()
     
         # Call C-accessible Fortran wrapper.
-        clib.c_minimize_mse(ctypes.byref(config), ctypes.byref(model_dim_1), ctypes.c_void_p(model.ctypes.data), ctypes.byref(y_dim_1), ctypes.byref(y_dim_2), ctypes.c_void_p(y.ctypes.data), ctypes.byref(x_dim_1), ctypes.byref(x_dim_2), ctypes.c_void_p(x.ctypes.data), ctypes.byref(xi_dim_1), ctypes.byref(xi_dim_2), ctypes.c_void_p(xi.ctypes.data), ctypes.byref(ax_dim_1), ctypes.byref(ax_dim_2), ctypes.c_void_p(ax.ctypes.data), ctypes.byref(axi_dim_1), ctypes.byref(axi_dim_2), ctypes.c_void_p(axi.ctypes.data), ctypes.byref(sizes_dim_1), ctypes.c_void_p(sizes.ctypes.data), ctypes.byref(steps), ctypes.byref(sum_squared_error), ctypes.byref(record_present), ctypes.byref(record_dim_1), ctypes.byref(record_dim_2), ctypes.c_void_p(record.ctypes.data), ctypes.byref(info))
+        clib.c_minimize_mse(ctypes.byref(config), ctypes.byref(model_dim_1), ctypes.c_void_p(model.ctypes.data), ctypes.byref(rwork_dim_1), ctypes.c_void_p(rwork.ctypes.data), ctypes.byref(iwork_dim_1), ctypes.c_void_p(iwork.ctypes.data), ctypes.byref(ax_dim_1), ctypes.byref(ax_dim_2), ctypes.c_void_p(ax.ctypes.data), ctypes.byref(axi_dim_1), ctypes.byref(axi_dim_2), ctypes.c_void_p(axi.ctypes.data), ctypes.byref(sizes_dim_1), ctypes.c_void_p(sizes.ctypes.data), ctypes.byref(x_dim_1), ctypes.byref(x_dim_2), ctypes.c_void_p(x.ctypes.data), ctypes.byref(xi_dim_1), ctypes.byref(xi_dim_2), ctypes.c_void_p(xi.ctypes.data), ctypes.byref(y_dim_1), ctypes.byref(y_dim_2), ctypes.c_void_p(y.ctypes.data), ctypes.byref(steps), ctypes.byref(record_present), ctypes.byref(record_dim_1), ctypes.byref(record_dim_2), ctypes.c_void_p(record.ctypes.data), ctypes.byref(sum_squared_error), ctypes.byref(info))
     
         # Return final results, 'INTENT(OUT)' arguments only.
-        return model, y, x, ax, sum_squared_error.value, (record if record_present else None), info.value
+        return config, model, rwork, iwork, ax, x, y, (record if record_present else None), sum_squared_error.value, info.value
 
 apos = apos()
```

### Comparing `tlux-0.0.8/tlux/approximate/apos/apos/apos.f90` & `tlux-0.0.9/tlux/approximate/apos/apos/apos.f90`

 * *Files 26% similar despite different names*

```diff
@@ -1,38 +1,33 @@
 ! TODO:
 ! 
-! - Unify memory allocation so that threads don't have to allocate their
-!   own temporary space.
+! - Thoroughly test NORMALIZE (make sure data is correctly normalized in all use cases).
+!   Particularly, check that the initialization of the apositional output scale is working.
 ! 
-! - Enable a model that has no internal states (for linear regression).
+! - Reset convention to be order of processing (AX, AXI, AY, SIZES, X, XI, Y)
+! - Enable a model that has no internal states for linear regression (*NS=0).
+! - Enable a apositional without a following model (MDO=0) (no apositional shifting).
+!
+! - Update Python testing code to test all combinations of AX, AXI, AY, X, XI, and Y.
+! - Update Python testing code to attempt different edge-case model sizes
+!    (linear regression, no apositional, no model).
 ! 
-! - Enable a apositional without a following model.
+! - Make data normalization use the same work space as the fit procedure
+!   (since these are not needed at the same time).
+! - Pull normalization code out and have it be called separately from 'FIT'.
+!   (decide how to handle encoding the normalization into the model, function?)
+!   Goal is to achieve near-zero losses for doing a few steps at a time in
+!   Python (allowing for easier cancellation, progress updates, ...).
 ! 
-! - Center and fit inputs and outputs to spherical points (unit length).
+! - Use LAPACK to do linear regression, implement simple SVD + gradient descent method
+!   in MATRIX_OPERATIONS, compare speed of both methodologies.
+! - Implement and test Fortran intrinsic version of matrix multiplication.
+! - Implement and test Fortran intrinsic version of SSYRK (manually do loop).
 ! 
-! - Change initialization of shift terms to be based on the assumption
-!   that input data has spherical shape. Internal shift terms use
-!   previous shift and weight matrices to estimate value ranges for
-!   each basis function, with largest functions getting most negative
-!   shift and smallest functions getting most positive shift.
-! 
-! - Create 'condition_model' subroutine that takes values and gradients
-!   at all internal states, uses linear transformations to identify and
-!   remove redundant basis functions and initialize new basis functions
-!   that align most with the error function.
-! 
-! - Get stats on the internal values within the network during training.
-!   - step size progression
-!   - shift values
-!   - vector magnitudes for each node
-!   - output weights magnitude for each node
-!   - internal node contributions to MSE
-!   - data distributions at internal nodes (% less and greater than 0)
-! 
-
+! ---------------------------------------------------------------------------
 
 ! Module for matrix multiplication (absolutely crucial for APOS speed).
 MODULE MATRIX_OPERATIONS
   USE ISO_FORTRAN_ENV, ONLY: RT => REAL32
   IMPLICIT NONE
 
 CONTAINS
@@ -67,32 +62,29 @@
     !    ELSE
     !       C(:,:) = C(:,:) + AB_MULT * MATMUL(TRANSPOSE(A(:,:)), TRANSPOSE(B(:,:)))
     !    END IF
     ! END IF
   END SUBROUTINE GEMM
 
   ! Orthogonalize and normalize column vectors of A in order.
-  SUBROUTINE ORTHONORMALIZE(A, RANK)
+  SUBROUTINE ORTHONORMALIZE(A)
     REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: A
-    INTEGER, INTENT(OUT), OPTIONAL :: RANK
     REAL(KIND=RT), DIMENSION(SIZE(A,2)) :: MULTIPLIERS
     REAL(KIND=RT) :: LEN
     INTEGER :: I, J
-    IF (PRESENT(RANK)) RANK = 0
     DO I = 1, SIZE(A,2)
        LEN = NORM2(A(:,I))
        IF (LEN .GT. 0.0_RT) THEN
           A(:,I) = A(:,I) / LEN
-          IF (PRESENT(RANK)) RANK = RANK + 1
-       END IF
-       IF ((LEN .GT. 0.0_RT) .AND. (I .LT. SIZE(A,2))) THEN
-          MULTIPLIERS(I+1:) = MATMUL(A(:,I), A(:,I+1:))
-          DO J = I+1, SIZE(A,2)
-             A(:,J) = A(:,J) - MULTIPLIERS(J) * A(:,I)
-          END DO
+          IF (I .LT. SIZE(A,2)) THEN
+             MULTIPLIERS(I+1:) = MATMUL(A(:,I), A(:,I+1:))
+             DO J = I+1, SIZE(A,2)
+                A(:,J) = A(:,J) - MULTIPLIERS(J) * A(:,I)
+             END DO
+          END IF
        END IF
     END DO
   END SUBROUTINE ORTHONORMALIZE
 
   ! Generate randomly distributed vectors on the N-sphere.
   SUBROUTINE RANDOM_UNIT_VECTORS(COLUMN_VECTORS)
     REAL(KIND=RT), INTENT(OUT), DIMENSION(:,:) :: COLUMN_VECTORS
@@ -115,186 +107,674 @@
     END IF
     ! Orthonormalize the first components of the column
     !  vectors to ensure those are well spaced.
     I = MIN(SIZE(COLUMN_VECTORS,1), SIZE(COLUMN_VECTORS,2))
     IF (I .GT. 1) CALL ORTHONORMALIZE(COLUMN_VECTORS(:,1:I))
   END SUBROUTINE RANDOM_UNIT_VECTORS
 
+  ! Orthogonalize and normalize column vectors of A with pivoting.
+  SUBROUTINE ORTHOGONALIZE(A, LENGTHS, RANK, ORDER)
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: A
+    REAL(KIND=RT), INTENT(OUT), DIMENSION(SIZE(A,2)) :: LENGTHS
+    INTEGER, INTENT(OUT), OPTIONAL :: RANK
+    INTEGER, INTENT(OUT), DIMENSION(SIZE(A,2)), OPTIONAL :: ORDER
+    REAL(KIND=RT) :: L, VEC(SIZE(A,1)) 
+    INTEGER :: I, J, K
+    IF (PRESENT(RANK)) RANK = 0
+    IF (PRESENT(ORDER)) THEN
+       FORALL (I=1:SIZE(A,2)) ORDER(I) = I
+    END IF
+    column_orthogonolization : DO I = 1, SIZE(A,2)
+       LENGTHS(I:) = SUM(A(:,I:)**2, 1)
+       ! Pivot the largest magnitude vector to the front.
+       J = I-1+MAXLOC(LENGTHS(I:),1)
+       IF (J .NE. I) THEN
+          IF (PRESENT(ORDER)) THEN
+             K = ORDER(I)
+             ORDER(I) = ORDER(J)
+             ORDER(J) = K
+          END IF
+          L = LENGTHS(I)
+          LENGTHS(I) = LENGTHS(J)
+          LENGTHS(J) = L
+          VEC(:) = A(:,I)
+          A(:,I) = A(:,J)
+          A(:,J) = VEC(:)
+       END IF
+       ! Subtract the first vector from all others.
+       IF (LENGTHS(I) .GT. EPSILON(1.0_RT)) THEN
+          LENGTHS(I) = SQRT(LENGTHS(I))
+          A(:,I) = A(:,I) / LENGTHS(I)
+          IF (I .LT. SIZE(A,2)) THEN
+             LENGTHS(I+1:) = MATMUL(A(:,I), A(:,I+1:))
+             DO J = I+1, SIZE(A,2)
+                A(:,J) = A(:,J) - LENGTHS(J) * A(:,I)
+             END DO
+          END IF
+          IF (PRESENT(RANK)) RANK = RANK + 1
+       ELSE
+          LENGTHS(I:) = 0.0_RT
+          EXIT column_orthogonolization
+       END IF
+    END DO column_orthogonolization
+  END SUBROUTINE ORTHOGONALIZE
+
+  ! Compute the singular values and right singular vectors for matrix A.
+  SUBROUTINE SVD(A, S, VT, RANK, STEPS, BIAS)
+    IMPLICIT NONE
+    REAL(KIND=RT), INTENT(IN), DIMENSION(:,:) :: A
+    REAL(KIND=RT), INTENT(OUT), DIMENSION(MIN(SIZE(A,1),SIZE(A,2))) :: S
+    REAL(KIND=RT), INTENT(OUT), DIMENSION(MIN(SIZE(A,1),SIZE(A,2)),MIN(SIZE(A,1),SIZE(A,2))) :: VT
+    INTEGER, INTENT(OUT), OPTIONAL :: RANK
+    INTEGER, INTENT(IN), OPTIONAL :: STEPS
+    REAL(KIND=RT), INTENT(IN), OPTIONAL :: BIAS
+    ! Local variables.
+    REAL(KIND=RT), DIMENSION(MIN(SIZE(A,1),SIZE(A,2)),MIN(SIZE(A,1),SIZE(A,2))) :: ATA, Q
+    INTEGER :: I, J, K, NUM_STEPS
+    REAL(KIND=RT) :: MULTIPLIER
+    EXTERNAL :: SSYRK
+    ! Set the number of steps.
+    IF (PRESENT(STEPS)) THEN
+       NUM_STEPS = STEPS
+    ELSE
+       NUM_STEPS = 1
+    END IF
+    ! Set "K" (the number of components).
+    K = MIN(SIZE(A,1),SIZE(A,2))
+    ! Find the multiplier on A.
+    MULTIPLIER = MAXVAL(ABS(A(:,:)))
+    IF (MULTIPLIER .EQ. 0.0_RT) THEN
+       S(:) = 0.0_RT
+       VT(:,:) = 0.0_RT
+       RETURN
+    END IF
+    IF (PRESENT(BIAS)) MULTIPLIER = MULTIPLIER / BIAS
+    MULTIPLIER = 1.0_RT / MULTIPLIER
+    ! Compute ATA.
+    IF (SIZE(A,1) .LE. SIZE(A,2)) THEN
+       ! ATA(:,:) = MATMUL(AT(:,:), TRANSPOSE(AT(:,:)))
+       CALL SSYRK('U', 'N', K, SIZE(A,2), MULTIPLIER**2, A(:,:), &
+            SIZE(A,1), 0.0_RT, ATA(:,:), K)
+    ELSE
+       ! ATA(:,:) = MATMUL(TRANSPOSE(A(:,:)), A(:,:))
+       CALL SSYRK('U', 'T', K, SIZE(A,1), MULTIPLIER**2, A(:,:), &
+            SIZE(A,1), 0.0_RT, ATA(:,:), K)
+    END IF
+    ! Copy the upper diagnoal portion into the lower diagonal portion.
+    DO I = 1, K
+       ATA(I+1:,I) = ATA(I,I+1:)
+    END DO
+    ! Compute initial right singular vectors.
+    VT(:,:) = ATA(:,:)
+    ! Orthogonalize and reorder by magnitudes.
+    CALL ORTHOGONALIZE(VT(:,:), S(:), RANK)
+    ! Do power iterations.
+    power_iteration : DO I = 1, NUM_STEPS
+       Q(:,:) = VT(:,:)
+       ! Q(:,:) = MATMUL(TRANSPOSE(ATA(:,:)), QTEMP(:,:))
+       CALL GEMM('N', 'N', K, K, K, 1.0_RT, &
+            ATA(:,:), K, Q(:,:), K, 0.0_RT, &
+            VT(:,:), K)
+       CALL ORTHOGONALIZE(VT(:,:), S(:), RANK)
+    END DO power_iteration
+    ! Compute the singular values.
+    WHERE (S(:) .NE. 0.0_RT)
+       S(:) = SQRT(S(:)) / MULTIPLIER
+    END WHERE
+  END SUBROUTINE SVD
+
+  ! If there are at least as many data points as dimension, then
+  ! compute the principal components and rescale the data by
+  ! projecting onto those and rescaling so that each component has
+  ! identical singular values (this makes the data more "radially
+  ! symmetric").
+  SUBROUTINE RADIALIZE(X, SHIFT, VECS, INVERT_RESULT, STEPS)
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: X
+    REAL(KIND=RT), INTENT(OUT), DIMENSION(:) :: SHIFT
+    REAL(KIND=RT), INTENT(OUT), DIMENSION(:,:) :: VECS
+    LOGICAL, INTENT(IN), OPTIONAL :: INVERT_RESULT
+    INTEGER, INTENT(IN), OPTIONAL :: STEPS
+    ! Local variables.
+    LOGICAL :: INVERSE
+    REAL(KIND=RT), DIMENSION(SIZE(VECS,1),SIZE(VECS,2)) :: TEMP_VECS
+    REAL(KIND=RT), DIMENSION(SIZE(X,1)) :: VALS
+    REAL(KIND=RT), DIMENSION(SIZE(X,1), SIZE(X,2)) :: X1
+    REAL(KIND=RT) :: RN
+    INTEGER :: I, D
+    ! Set the default value for "INVERSE".
+    IF (PRESENT(INVERT_RESULT)) THEN
+       INVERSE = INVERT_RESULT
+    ELSE
+       INVERSE = .FALSE.
+    END IF
+    ! Shift the data to be be centered about the origin.
+    D = SIZE(X,1)
+    RN = REAL(SIZE(X,2),RT)
+    SHIFT(:) = -SUM(X(:,:),2) / RN
+    DO I = 1, D
+       X(I,:) = X(I,:) + SHIFT(I)
+    END DO
+    ! Set the unused portion of the "VECS" matrix to the identity.
+    VECS(D+1:,D+1:) = 0.0_RT
+    DO I = D+1, SIZE(VECS,1)
+       VECS(I,I) = 1.0_RT
+    END DO
+    ! Find the directions along which the data is most elongated.
+    IF (PRESENT(STEPS)) THEN
+       CALL SVD(X, VALS, VECS(:D,:D), STEPS=STEPS)
+    ELSE
+       CALL SVD(X, VALS, VECS(:D,:D), STEPS=10)
+    END IF
+    ! Normalize the values to make the output componentwise unit mean squared magnitude.
+    VALS(:) = VALS(:) / SQRT(RN)
+    ! For all nonzero vectors, rescale them so that 
+    !  the average distance from zero is exactly 1.
+    DO I = 1, D
+       IF (VALS(I) .GT. 0.0_RT) THEN
+          VECS(:,I) = VECS(:,I) / VALS(I)
+       END IF
+    END DO
+    ! Apply the column vectors to the data to make it radially symmetric.
+    X1(:,:) = X(:,:)
+    CALL GEMM('T', 'N', D, SIZE(X,2), D, 1.0_RT, &
+         VECS(:D,:D), D, &
+         X1(:,:), D, &
+         0.0_RT, X(:,:), D)
+    ! Compute the inverse of the transformation if requested.
+    IF (INVERSE) THEN
+       VALS(:) = VALS(:)**2
+       DO I = 1, D
+          IF (VALS(I) .GT. 0.0_RT) THEN
+             VECS(:D,I) = VECS(:D,I) * VALS(I)
+          END IF
+       END DO
+       VECS(:D,:D) = TRANSPOSE(VECS(:D,:D))
+       SHIFT(:) = -SHIFT(:)
+    END IF
+  END SUBROUTINE RADIALIZE
+
 END MODULE MATRIX_OPERATIONS
 
+! ---------------------------------------------------------------------------
+
+! A module for fast sorting and selecting of data.
+MODULE SORT_AND_SELECT
+  USE ISO_FORTRAN_ENV, ONLY: RT => REAL32
+  IMPLICIT NONE
+
+CONTAINS
+
+  ! Swap the values of two integers.
+  SUBROUTINE SWAP_INT(V1, V2)
+    INTEGER, INTENT(INOUT) :: V1, V2
+    INTEGER :: TEMP
+    TEMP = V1
+    V1 = V2
+    V2 = TEMP
+  END SUBROUTINE SWAP_INT
+
+  !                       FastSelect method
+  ! 
+  ! Given VALUES list of numbers, rearrange the elements of INDICES
+  ! such that the element of VALUES at INDICES(K) has rank K (holds
+  ! its same location as if all of VALUES were sorted in INDICES).
+  ! All elements of VALUES at INDICES(:K-1) are less than or equal,
+  ! while all elements of VALUES at INDICES(K+1:) are greater or equal.
+  ! 
+  ! This algorithm uses a recursive approach to exponentially shrink
+  ! the number of indices that have to be considered to find the
+  ! element of desired rank, while simultaneously pivoting values
+  ! that are less than the target rank left and larger right.
+  ! 
+  ! Arguments:
+  ! 
+  !   VALUES   --  A 1D array of real numbers. Will not be modified.
+  !   K        --  A positive integer for the rank index about which
+  !                VALUES should be rearranged.
+  ! Optional:
+  ! 
+  !   DIVISOR  --  A positive integer >= 2 that represents the
+  !                division factor used for large VALUES arrays.
+  !   MAX_SIZE --  An integer >= DIVISOR that represents the largest
+  !                sized VALUES for which the worst-case pivot value
+  !                selection is tolerable. A worst-case pivot causes
+  !                O( SIZE(VALUES)^2 ) runtime. This value should be
+  !                determined heuristically based on compute hardware.
+  ! Output:
+  ! 
+  !   INDICES  --  A 1D array of original indices for elements of VALUES.
+  ! 
+  !   The elements of the array INDICES are rearranged such that the
+  !   element at position VALUES(INDICES(K)) is in the same location 
+  !   it would be if all of VALUES were referenced in sorted order in
+  !   INDICES. Also known as, VALUES(INDICES(K)) has rank K.
+  ! 
+  RECURSIVE SUBROUTINE ARGSELECT(VALUES, K, INDICES, DIVISOR, MAX_SIZE, RECURSING)
+    ! Arguments
+    REAL(KIND=RT), INTENT(IN), DIMENSION(:) :: VALUES
+    INTEGER, INTENT(IN) :: K
+    INTEGER, INTENT(INOUT), DIMENSION(:) :: INDICES
+    INTEGER, INTENT(IN), OPTIONAL :: DIVISOR, MAX_SIZE
+    LOGICAL, INTENT(IN), OPTIONAL :: RECURSING
+    ! Locals
+    INTEGER :: LEFT, RIGHT, L, R, MS, D, I
+    REAL(KIND=RT) :: P
+    ! Initialize the divisor (for making subsets).
+    IF (PRESENT(DIVISOR)) THEN ; D = DIVISOR
+    ELSE IF (SIZE(INDICES) .GE. 8388608) THEN ; D = 32 ! 2**5 ! 2**23
+    ELSE IF (SIZE(INDICES) .GE. 1048576) THEN ; D = 8  ! 2**3 ! 2**20
+    ELSE                                      ; D = 4  ! 2**2
+    END IF
+    ! Initialize the max size (before subsets are created).
+    IF (PRESENT(MAX_SIZE)) THEN ; MS = MAX_SIZE
+    ELSE                        ; MS = 1024 ! 2**10
+    END IF
+    ! When not recursing, set the INDICES to default values.
+    IF (.NOT. PRESENT(RECURSING)) THEN
+       FORALL(I=1:SIZE(INDICES)) INDICES(I) = I
+    END IF
+    ! Initialize LEFT and RIGHT to be the entire array.
+    LEFT = 1
+    RIGHT = SIZE(INDICES)
+    ! Loop until done finding the K-th element.
+    DO WHILE (LEFT .LT. RIGHT)
+       ! Use SELECT recursively to improve the quality of the
+       ! selected pivot value for large arrays.
+       IF (RIGHT - LEFT .GT. MS) THEN
+          ! Compute how many elements should be left and right of K
+          ! to maintain the same percentile in a subset.
+          L = K - K / D
+          R = L + (SIZE(INDICES) / D)
+          ! Perform fast select on an array a fraction of the size about K.
+          CALL ARGSELECT(VALUES(:), K - L + 1, INDICES(L:R), &
+               DIVISOR=D, MAX_SIZE=MS, RECURSING=.TRUE.)
+       END IF
+       ! Pick a partition element at position K.
+       P = VALUES(INDICES(K))
+       L = LEFT
+       R = RIGHT
+       ! Move the partition element to the front of the list.
+       CALL SWAP_INT(INDICES(LEFT), INDICES(K))
+       ! Pre-swap the left and right elements (temporarily putting a
+       ! larger element on the left) before starting the partition loop.
+       IF (VALUES(INDICES(RIGHT)) .GT. P) THEN
+          CALL SWAP_INT(INDICES(LEFT), INDICES(RIGHT))
+       END IF
+       ! Now partition the elements about the pivot value "P".
+       DO WHILE (L .LT. R)
+          CALL SWAP_INT(INDICES(L), INDICES(R))
+          L = L + 1
+          R = R - 1
+          DO WHILE (VALUES(INDICES(L)) .LT. P) ; L = L + 1 ; END DO
+          DO WHILE (VALUES(INDICES(R)) .GT. P) ; R = R - 1 ; END DO
+       END DO
+       ! Place the pivot element back into its appropriate place.
+       IF (VALUES(INDICES(LEFT)) .EQ. P) THEN
+          CALL SWAP_INT(INDICES(LEFT), INDICES(R))
+       ELSE
+          R = R + 1
+          CALL SWAP_INT(INDICES(R), INDICES(RIGHT))
+       END IF
+       ! adjust left and right towards the boundaries of the subset
+       ! containing the (k - left + 1)th smallest element
+       IF (R .LE. K) LEFT = R + 1
+       IF (K .LE. R) RIGHT = R - 1
+    END DO
+  END SUBROUTINE ARGSELECT
+  
+  !                         FastSort
+  ! 
+  ! This routine uses a combination of QuickSort (with modestly
+  ! intelligent pivot selection) and Insertion Sort (for small arrays)
+  ! to achieve very fast average case sort times for both random and
+  ! partially sorted data. The pivot is selected for QuickSort as the
+  ! median of the first, middle, and last values in the array.
+  ! 
+  ! Arguments:
+  ! 
+  !   VALUES   --  A 1D array of real numbers.
+  !   INDICES  --  A 1D array of original indices for elements of VALUES.
+  ! 
+  ! Optional:
+  ! 
+  !   MIN_SIZE --  An positive integer that represents the largest
+  !                sized VALUES for which a partition about a pivot
+  !                is used to reduce the size of a an unsorted array.
+  !                Any size less than this will result in the use of
+  !                INSERTION_ARGSORT instead of ARGPARTITION.
+  ! 
+  ! Output:
+  ! 
+  !   The elements of the array INDICES contain ths sorted order of VALUES.
+  ! 
+  RECURSIVE SUBROUTINE ARGSORT(VALUES, INDICES, MIN_SIZE, INIT_INDS)
+    REAL(KIND=RT), INTENT(IN),    DIMENSION(:) :: VALUES
+    INTEGER,       INTENT(INOUT), DIMENSION(:) :: INDICES
+    INTEGER,       INTENT(IN), OPTIONAL        :: MIN_SIZE
+    LOGICAL,       INTENT(IN), OPTIONAL        :: INIT_INDS
+    ! Local variables
+    LOGICAL :: INIT
+    INTEGER :: I, MS
+    IF (PRESENT(MIN_SIZE)) THEN ; MS = MIN_SIZE
+    ELSE                        ; MS = 2**6
+    END IF
+    IF (PRESENT(INIT_INDS)) THEN ; INIT = INIT_INDS
+    ELSE                         ; INIT = .TRUE.
+    END IF
+    ! Initialize all indices (for the first call).
+    IF (INIT) THEN
+       FORALL (I=1:SIZE(INDICES)) INDICES(I) = I
+    END IF
+    ! Base case, return.
+    IF (SIZE(INDICES) .LT. MS) THEN
+       CALL INSERTION_ARGSORT(VALUES, INDICES)
+    ! Call this function recursively after pivoting about the median.
+    ELSE
+       ! ---------------------------------------------------------------
+       ! If you are having slow runtime with the selection of pivot values 
+       ! provided by ARGPARTITION, then consider using ARGSELECT instead.
+       I = ARGPARTITION(VALUES, INDICES)
+       ! ---------------------------------------------------------------
+       ! I = SIZE(INDICES) / 2
+       ! CALL ARGSELECT(VALUES, INDICES, I)
+       ! ---------------------------------------------------------------
+       CALL ARGSORT(VALUES(:), INDICES(:I-1), MS, INIT_INDS=.FALSE.)
+       CALL ARGSORT(VALUES(:), INDICES(I+1:), MS, INIT_INDS=.FALSE.)
+    END IF
+  END SUBROUTINE ARGSORT
+
+  ! This function efficiently partitions values based on the median
+  ! of the first, middle, and last elements of the VALUES array. This
+  ! function returns the index of the pivot.
+  FUNCTION ARGPARTITION(VALUES, INDICES) RESULT(LEFT)
+    REAL(KIND=RT), INTENT(IN),    DIMENSION(:) :: VALUES
+    INTEGER,       INTENT(INOUT), DIMENSION(:) :: INDICES
+    INTEGER :: LEFT, MID, RIGHT
+    REAL(KIND=RT) :: PIVOT
+    ! Use the median of the first, middle, and last element as the
+    ! pivot. Place the pivot at the end of the array.
+    MID = (1 + SIZE(INDICES)) / 2
+    ! Swap the first and last elements (if the last is smaller).
+    IF (VALUES(INDICES(SIZE(INDICES))) < VALUES(INDICES(1))) THEN
+       CALL SWAP_INT(INDICES(1), INDICES(SIZE(INDICES)))
+    END IF
+    ! Swap the middle and first elements (if the middle is smaller).
+    IF (VALUES(INDICES(MID)) < VALUES(INDICES(SIZE(INDICES)))) THEN
+       CALL SWAP_INT(INDICES(MID), INDICES(SIZE(INDICES)))       
+       ! Swap the last and first elements (if the last is smaller).
+       IF (VALUES(INDICES(SIZE(INDICES))) < VALUES(INDICES(1))) THEN
+          CALL SWAP_INT(INDICES(1), INDICES(SIZE(INDICES)))
+       END IF
+    END IF
+    ! Set the pivot, LEFT index and RIGHT index (skip the smallest,
+    ! which is in location 1, and the pivot at the end).
+    PIVOT = VALUES(INDICES(SIZE(INDICES)))
+    LEFT  = 2
+    RIGHT = SIZE(INDICES) - 1
+    ! Partition all elements to the left and right side of the pivot
+    ! (left if they are smaller, right if they are bigger).
+    DO WHILE (LEFT < RIGHT)
+       ! Loop left until we find a value that is greater or equal to pivot.
+       DO WHILE (VALUES(INDICES(LEFT)) < PIVOT)
+          LEFT = LEFT + 1
+       END DO
+       ! Loop right until we find a value that is less or equal to pivot (or LEFT).
+       DO WHILE (RIGHT .NE. LEFT)
+          IF (VALUES(INDICES(RIGHT)) .LT. PIVOT) EXIT
+          RIGHT = RIGHT - 1
+       END DO
+       ! Now we know that [VALUES(RIGHT) < PIVOT < VALUES(LEFT)], so swap them.
+       CALL SWAP_INT(INDICES(LEFT), INDICES(RIGHT))
+    END DO
+    ! The last swap was done even though LEFT == RIGHT, we need to undo.
+    CALL SWAP_INT(INDICES(LEFT), INDICES(RIGHT))
+    ! Finally, we put the pivot back into its proper location.
+    CALL SWAP_INT(INDICES(LEFT), INDICES(SIZE(INDICES)))
+  END FUNCTION ARGPARTITION
+
+  ! Insertion sort (best for small lists).
+  SUBROUTINE INSERTION_ARGSORT(VALUES, INDICES)
+    REAL(KIND=RT), INTENT(IN),    DIMENSION(:) :: VALUES
+    INTEGER,       INTENT(INOUT), DIMENSION(:) :: INDICES
+    ! Local variables.
+    REAL(KIND=RT)   :: TEMP_VAL
+    INTEGER :: I, BEFORE, AFTER, TEMP_IND
+    ! Return for the base case.
+    IF (SIZE(INDICES) .LE. 1) RETURN
+    ! Put the smallest value at the front of the list.
+    I = MINLOC(VALUES(INDICES(:)),1)
+    CALL SWAP_INT(INDICES(1), INDICES(I))
+    ! Insertion sort the rest of the array.
+    DO I = 3, SIZE(INDICES)
+       TEMP_IND = INDICES(I)
+       TEMP_VAL = VALUES(TEMP_IND)
+       ! Search backwards in the list, 
+       BEFORE = I - 1
+       AFTER  = I
+       DO WHILE (TEMP_VAL .LT. VALUES(INDICES(BEFORE)))
+          INDICES(AFTER) = INDICES(BEFORE)
+          BEFORE = BEFORE - 1
+          AFTER  = AFTER - 1
+       END DO
+       ! Put the value into its place (where it is greater than the
+       ! element before it, but less than all values after it).
+       INDICES(AFTER) = TEMP_IND
+    END DO
+  END SUBROUTINE INSERTION_ARGSORT
+
+END MODULE SORT_AND_SELECT
+
+
+! ---------------------------------------------------------------------------
+
 
 ! An apositional (/aggregate) and positional piecewise linear regression model.
 MODULE APOS
-  USE ISO_FORTRAN_ENV, ONLY: RT => REAL32
-  USE MATRIX_OPERATIONS, ONLY: GEMM, ORTHONORMALIZE, RANDOM_UNIT_VECTORS
+  USE ISO_FORTRAN_ENV, ONLY: RT => REAL32, INT64, INT8
+  USE MATRIX_OPERATIONS, ONLY: GEMM, RANDOM_UNIT_VECTORS, ORTHOGONALIZE, RADIALIZE
+  USE SORT_AND_SELECT, ONLY: ARGSORT, ARGSELECT
+
   IMPLICIT NONE
 
   PRIVATE :: MODEL_GRADIENT
 
   ! Model configuration, internal sizes and fit parameters.
   TYPE, BIND(C) :: MODEL_CONFIG
-     ! (Positional) model configuration.
-     INTEGER :: MDI      ! model dimension of input
-     INTEGER :: MDS = 32 ! model dimension of state
-     INTEGER :: MNS = 8  ! model number of states
-     INTEGER :: MDO      ! model dimension of output
-     INTEGER :: MNE = 0  ! model number of embeddings
-     INTEGER :: MDE = 0  ! model dimension of embeddings
      ! Apositional model configuration.
+     INTEGER :: ADN      ! apositional dimension numeric (input)
      INTEGER :: ADI      ! apositional dimension of input
      INTEGER :: ADS = 32 ! apositional dimension of state
      INTEGER :: ANS = 8  ! apositional number of states
      INTEGER :: ADO = 32 ! apositional dimension of output
      INTEGER :: ANE = 0  ! apositional number of embeddings
      INTEGER :: ADE = 0  ! apositional dimension of embeddings
+     ! (Positional) model configuration.
+     INTEGER :: MDN      ! model dimension numeric (input)
+     INTEGER :: MDI      ! model dimension of input
+     INTEGER :: MDS = 32 ! model dimension of state
+     INTEGER :: MNS = 8  ! model number of states
+     INTEGER :: MDO      ! model dimension of output
+     INTEGER :: MNE = 0  ! model number of embeddings
+     INTEGER :: MDE = 0  ! model dimension of embeddings
      ! Summary numbers that are computed.
      INTEGER :: TOTAL_SIZE
      INTEGER :: NUM_VARS
      ! Index subsets of total size vector naming scheme:
      !   M___ -> model,   A___ -> apositional (/ aggregate) model
      !   _S__ -> start,   _E__ -> end
      !   __I_ -> input,   __S_ -> states, __O_ -> output, __E_ -> embedding
      !   ___V -> vectors, ___S -> shifts
-     INTEGER :: MSIV, MEIV, MSIS, MEIS ! model input
-     INTEGER :: MSSV, MESV, MSSS, MESS ! model states
-     INTEGER :: MSOV, MEOV             ! model output
-     INTEGER :: MSEV, MEEV             ! model embedding
      INTEGER :: ASIV, AEIV, ASIS, AEIS ! apositional input
      INTEGER :: ASSV, AESV, ASSS, AESS ! apositional states
      INTEGER :: ASOV, AEOV             ! apositional output
      INTEGER :: ASEV, AEEV             ! apositional embedding
+     INTEGER :: MSIV, MEIV, MSIS, MEIS ! model input
+     INTEGER :: MSSV, MESV, MSSS, MESS ! model states
+     INTEGER :: MSOV, MEOV             ! model output
+     INTEGER :: MSEV, MEEV             ! model embedding
      ! Index subsets for input and output shifts.
      ! M___ -> model,       A___ -> apositional (/ aggregate) model
      ! _IS_ -> input shift, _OS_ -> output shift
      ! ___S -> start,       ___E -> end
+     INTEGER :: AISS, AISE, AOSS, AOSE
      INTEGER :: MISS, MISE, MOSS, MOSE
-     INTEGER :: AISS, AISE
      ! Function parameter.
      REAL(KIND=RT) :: DISCONTINUITY = 0.0_RT
      ! Initialization related parameters.
      REAL(KIND=RT) :: INITIAL_SHIFT_RANGE = 1.0_RT
      REAL(KIND=RT) :: INITIAL_OUTPUT_SCALE = 0.1_RT
-     REAL(KIND=RT) :: INITIAL_STEP = 0.001_RT
-     REAL(KIND=RT) :: INITIAL_STEP_MEAN_CHANGE = 0.1_RT
-     REAL(KIND=RT) :: INITIAL_STEP_CURV_CHANGE = 0.01_RT
      ! Optimization related parameters.
+     REAL(KIND=RT) :: STEP_FACTOR = 0.001_RT
+     REAL(KIND=RT) :: STEP_MEAN_CHANGE = 0.1_RT
+     REAL(KIND=RT) :: STEP_CURV_CHANGE = 0.01_RT
      REAL(KIND=RT) :: FASTER_RATE = 1.01_RT
      REAL(KIND=RT) :: SLOWER_RATE = 0.99_RT
-     INTEGER       :: MIN_STEPS_TO_STABILITY = 1
-     INTEGER       :: NUM_THREADS = 1
-     LOGICAL       :: KEEP_BEST = .TRUE.
-     LOGICAL       :: EARLY_STOP = .TRUE.
+     REAL(KIND=RT) :: MIN_UPDATE_RATIO = 0.05_RT
+     INTEGER :: MIN_STEPS_TO_STABILITY = 1
+     INTEGER :: NUM_THREADS = 1
+     INTEGER :: PRINT_DELAY_SEC = 3
+     INTEGER :: STEPS_TAKEN = 0
+     INTEGER :: LOGGING_STEP_FREQUENCY = 10
+     INTEGER :: NUM_TO_UPDATE = HUGE(0)
+     LOGICAL(KIND=INT8) :: AX_NORMALIZED = .FALSE.
+     LOGICAL(KIND=INT8) :: AXI_NORMALIZED = .FALSE.
+     LOGICAL(KIND=INT8) :: AY_NORMALIZED = .FALSE.
+     LOGICAL(KIND=INT8) :: X_NORMALIZED = .FALSE.
+     LOGICAL(KIND=INT8) :: XI_NORMALIZED = .FALSE.
+     LOGICAL(KIND=INT8) :: Y_NORMALIZED = .FALSE.
+     LOGICAL(KIND=INT8) :: ENCODE_NORMALIZATION = .TRUE.
+     LOGICAL(KIND=INT8) :: APPLY_SHIFT = .TRUE.
+     LOGICAL(KIND=INT8) :: KEEP_BEST = .TRUE.
+     LOGICAL(KIND=INT8) :: EARLY_STOP = .TRUE.
+     ! Descriptions of the number of points that can be in one batch.
+     INTEGER :: RWORK_SIZE = 0
+     INTEGER :: IWORK_SIZE = 0
+     INTEGER :: NA = 0
+     INTEGER :: NM = 0
+     ! Optimization work space start and end indices.
+     INTEGER :: SMG, EMG ! MODEL_GRAD(NUM_VARS)
+     INTEGER :: SMGM, EMGM ! MODEL_GRAD_MEAN(NUM_VARS)
+     INTEGER :: SMGC, EMGC ! MODEL_GRAD_CURV(NUM_VARS)
+     INTEGER :: SBM, EBM ! BEST_MODEL(NUM_VARS)
+
+     INTEGER :: SFMA, EFMA ! FULL_MODEL_ALIGN(NUM_VARS,NUM_THREADS)
+     
+     INTEGER :: SAXS, EAXS ! A_STATES(NA,ADS,ANS+1)
+     INTEGER :: SAXG, EAXG ! A_GRADS(NA,ADS,ANS+1)
+     INTEGER :: SAA, EAA ! A_ALIGN(ADS,ANS)
+     INTEGER :: SAY, EAY ! AY(NA,ADO)
+
+     INTEGER :: SXT, EXT ! X_TEMP(CONFIG%MDE+CONFIG%ADO,NM,NUM_THREADS)
+
+     INTEGER :: SAYG, EAYG ! AY_GRAD(NA,ADO)
+     INTEGER :: SMXS, EMXS ! M_STATES(NM,MDS,MNS+1)
+     INTEGER :: SMXG, EMXG ! M_GRADS(NM,MDS,MNS+1)
+     INTEGER :: SMA, EMA ! M_ALIGN(MDS,MNS)
+     INTEGER :: SYG, EYG ! Y_GRADIENT(MDO,NM)
+     INTEGER :: SAXR, EAXR ! AX_RESCALE(ADN,ADN)
+     INTEGER :: SAXIS, EAXIS ! AXI_SHIFT(ADE)
+     INTEGER :: SAXIR, EAXIR ! AXI_RESCALE(ADE,ADE)
+     INTEGER :: SAYR, EAYR ! AY_RESCALE(ADO)
+     INTEGER :: SMXR, EMXR ! X_RESCALE(MDN,MDN)
+     INTEGER :: SMXIS, EMXIS ! XI_SHIFT(MDE)
+     INTEGER :: SMXIR, EMXIR ! XI_RESCALE(MDE,MDE)
+     INTEGER :: SYR, EYR ! Y_RESCALE(MDO,MDO)
+     ! Integer workspace (for optimization).
+     INTEGER :: SUI, EUI ! UPDATE_INDICES(NUM_VARS)
+     INTEGER :: SBAS, EBAS ! BATCHA_STARTS(NUM_THREADS)
+     INTEGER :: SBAE, EBAE ! BATCHA_ENDS(NUM_THREADS)
+     INTEGER :: SBMS, EBMS ! BATCHM_STARTS(NUM_THREADS)
+     INTEGER :: SBME, EBME ! BATCHM_ENDS(NUM_THREADS)
   END TYPE MODEL_CONFIG
 
   ! Function that is defined by OpenMP.
   INTERFACE
      FUNCTION OMP_GET_MAX_THREADS()
        INTEGER :: OMP_GET_MAX_THREADS
      END FUNCTION OMP_GET_MAX_THREADS
   END INTERFACE
 
 CONTAINS
 
   ! Generate a model configuration given state parameters for the model.
-  SUBROUTINE NEW_MODEL_CONFIG(MDI, MDO, MDS, MNS, MNE, MDE, &
-       ADI, ADO, ADS, ANS, ANE, ADE, NUM_THREADS, CONFIG)
+  SUBROUTINE NEW_MODEL_CONFIG(ADN, ADO, ADS, ANS, ANE, ADE, &
+       MDN, MDO, MDS, MNS, MNE, MDE, NUM_THREADS, CONFIG)
      ! Size related parameters.
-     INTEGER, INTENT(IN) :: MDI, ADI
+     INTEGER, INTENT(IN) :: ADN, MDN
      INTEGER, INTENT(IN) :: MDO
      INTEGER, OPTIONAL, INTENT(IN) :: ADO
-     INTEGER, OPTIONAL, INTENT(IN) :: MDS, ADS
-     INTEGER, OPTIONAL, INTENT(IN) :: MNS, ANS
-     INTEGER, OPTIONAL, INTENT(IN) :: MNE, ANE
-     INTEGER, OPTIONAL, INTENT(IN) :: MDE, ADE
+     INTEGER, OPTIONAL, INTENT(IN) :: ADS, MDS
+     INTEGER, OPTIONAL, INTENT(IN) :: ANS, MNS
+     INTEGER, OPTIONAL, INTENT(IN) :: ANE, MNE
+     INTEGER, OPTIONAL, INTENT(IN) :: ADE, MDE
      INTEGER, OPTIONAL, INTENT(IN) :: NUM_THREADS
      ! Output
      TYPE(MODEL_CONFIG), INTENT(OUT) :: CONFIG
      ! ---------------------------------------------------------------
-     ! MDS
-     IF (PRESENT(MDS)) CONFIG%MDS = MDS
-     ! MNS
-     IF (PRESENT(MNS)) CONFIG%MNS = MNS
-     ! MNE
-     IF (PRESENT(MNE)) CONFIG%MNE = MNE
-     ! MDE
-     IF (PRESENT(MDE)) THEN
-        CONFIG%MDE = MDE
-     ELSE IF (CONFIG%MNE .GT. 0) THEN
+     ! ANE
+     IF (PRESENT(ANE)) CONFIG%ANE = ANE
+     ! ADE
+     IF (PRESENT(ADE)) THEN
+        CONFIG%ADE = ADE
+     ELSE IF (CONFIG%ANE .GT. 0) THEN
         ! Compute a reasonable default dimension (tied to volume of space).
-        CONFIG%MDE = MAX(1, 1 + CEILING(LOG(REAL(CONFIG%MNE,RT)) / LOG(2.0_RT)))
-        IF (CONFIG%MNE .GT. 2) CONFIG%MDE = CONFIG%MDE + 1
+        CONFIG%ADE = MAX(1, 1 + CEILING(LOG(REAL(CONFIG%ANE,RT)) / LOG(2.0_RT)))
+        IF (CONFIG%ANE .GT. 2) CONFIG%ADE = CONFIG%ADE + 1
      END IF
-     ! ---------------------------------------------------------------
+     ! ADN, ADI
+     CONFIG%ADN = ADN
+     CONFIG%ADI = CONFIG%ADN + CONFIG%ADE
      ! ADO
      IF (PRESENT(ADO)) THEN
         CONFIG%ADO = ADO
-     ELSE IF (ADI .EQ. 0) THEN
+     ELSE IF (CONFIG%ADI .EQ. 0) THEN
         CONFIG%ADO = 0
      END IF
      ! ADS
      IF (PRESENT(ADS)) THEN
         CONFIG%ADS = ADS
-     ELSE IF (ADI .EQ. 0) THEN
+     ELSE IF (CONFIG%ADI .EQ. 0) THEN
         CONFIG%ADS = 0
      END IF
      ! ANS
      IF (PRESENT(ANS)) THEN
         CONFIG%ANS = ANS
-     ELSE IF (ADI .EQ. 0) THEN
+     ELSE IF (CONFIG%ADI .EQ. 0) THEN
         CONFIG%ANS = 0
      END IF
-     ! ANE
-     IF (PRESENT(ANE)) CONFIG%ANE = ANE
-     ! ADE
-     IF (PRESENT(ADE)) THEN
-        CONFIG%ADE = ADE
-     ELSE IF (CONFIG%ANE .GT. 0) THEN
+     ! ---------------------------------------------------------------
+     ! MDO
+     CONFIG%MDO = MDO
+     ! MDS
+     IF (PRESENT(MDS)) CONFIG%MDS = MDS
+     ! MNS
+     IF (PRESENT(MNS)) CONFIG%MNS = MNS
+     ! MNE
+     IF (PRESENT(MNE)) CONFIG%MNE = MNE
+     ! MDE
+     IF (PRESENT(MDE)) THEN
+        CONFIG%MDE = MDE
+     ELSE IF (CONFIG%MNE .GT. 0) THEN
         ! Compute a reasonable default dimension (tied to volume of space).
-        CONFIG%ADE = MAX(1, 1 + CEILING(LOG(REAL(CONFIG%ANE,RT)) / LOG(2.0_RT)))
-        IF (CONFIG%ANE .GT. 2) CONFIG%ADE = CONFIG%ADE + 1
+        CONFIG%MDE = MAX(1, 1 + CEILING(LOG(REAL(CONFIG%MNE,RT)) / LOG(2.0_RT)))
+        IF (CONFIG%MNE .GT. 2) CONFIG%MDE = CONFIG%MDE + 1
      END IF
+     ! MDN, MDI
+     CONFIG%MDN = MDN
+     CONFIG%MDI = CONFIG%MDN + CONFIG%MDE + CONFIG%ADO
      ! ---------------------------------------------------------------
      ! NUM_THREADS
      IF (PRESENT(NUM_THREADS)) THEN
         CONFIG%NUM_THREADS = NUM_THREADS
      ELSE
         CONFIG%NUM_THREADS = OMP_GET_MAX_THREADS()
      END IF
-     ! Declare all required configurations.
-     CONFIG%ADI = ADI + CONFIG%ADE
-     CONFIG%MDI = MDI + CONFIG%MDE + CONFIG%ADO
-     CONFIG%MDO = MDO
      ! Compute indices related to the parameter vector for this model.
      CONFIG%TOTAL_SIZE = 0
      ! ---------------------------------------------------------------
-     !   model input vecs
-     CONFIG%MSIV = 1 + CONFIG%TOTAL_SIZE
-     CONFIG%MEIV = CONFIG%MSIV-1  +  CONFIG%MDI * CONFIG%MDS
-     CONFIG%TOTAL_SIZE = CONFIG%MEIV
-     !   model input shift
-     CONFIG%MSIS = 1 + CONFIG%TOTAL_SIZE
-     CONFIG%MEIS = CONFIG%MSIS-1  +  CONFIG%MDS
-     CONFIG%TOTAL_SIZE = CONFIG%MEIS
-     !   model state vecs
-     CONFIG%MSSV = 1 + CONFIG%TOTAL_SIZE
-     CONFIG%MESV = CONFIG%MSSV-1  +  CONFIG%MDS * CONFIG%MDS * (CONFIG%MNS-1)
-     CONFIG%TOTAL_SIZE = CONFIG%MESV
-     !   model state shift
-     CONFIG%MSSS = 1 + CONFIG%TOTAL_SIZE
-     CONFIG%MESS = CONFIG%MSSS-1  +  CONFIG%MDS * (CONFIG%MNS-1)
-     CONFIG%TOTAL_SIZE = CONFIG%MESS
-     !   model output vecs
-     CONFIG%MSOV = 1 + CONFIG%TOTAL_SIZE
-     CONFIG%MEOV = CONFIG%MSOV-1  +  CONFIG%MDS * CONFIG%MDO
-     CONFIG%TOTAL_SIZE = CONFIG%MEOV
-     !   model embedding vecs
-     CONFIG%MSEV = 1 + CONFIG%TOTAL_SIZE
-     CONFIG%MEEV = CONFIG%MSEV-1  +  CONFIG%MDE * CONFIG%MNE
-     CONFIG%TOTAL_SIZE = CONFIG%MEEV
-     ! ---------------------------------------------------------------
      !   apositional input vecs
      CONFIG%ASIV = 1 + CONFIG%TOTAL_SIZE
      CONFIG%AEIV = CONFIG%ASIV-1  +  CONFIG%ADI * CONFIG%ADS
      CONFIG%TOTAL_SIZE = CONFIG%AEIV
      !   apositional input shift
      CONFIG%ASIS = 1 + CONFIG%TOTAL_SIZE
      CONFIG%AEIS = CONFIG%ASIS-1  +  CONFIG%ADS
@@ -312,31 +792,187 @@
      CONFIG%AEOV = CONFIG%ASOV-1  +  CONFIG%ADS * CONFIG%ADO
      CONFIG%TOTAL_SIZE = CONFIG%AEOV
      !   apositional embedding vecs
      CONFIG%ASEV = 1 + CONFIG%TOTAL_SIZE
      CONFIG%AEEV = CONFIG%ASEV-1  +  CONFIG%ADE * CONFIG%ANE
      CONFIG%TOTAL_SIZE = CONFIG%AEEV
      ! ---------------------------------------------------------------
+     !   model input vecs
+     CONFIG%MSIV = 1 + CONFIG%TOTAL_SIZE
+     CONFIG%MEIV = CONFIG%MSIV-1  +  CONFIG%MDI * CONFIG%MDS
+     CONFIG%TOTAL_SIZE = CONFIG%MEIV
+     !   model input shift
+     CONFIG%MSIS = 1 + CONFIG%TOTAL_SIZE
+     CONFIG%MEIS = CONFIG%MSIS-1  +  CONFIG%MDS
+     CONFIG%TOTAL_SIZE = CONFIG%MEIS
+     !   model state vecs
+     CONFIG%MSSV = 1 + CONFIG%TOTAL_SIZE
+     CONFIG%MESV = CONFIG%MSSV-1  +  CONFIG%MDS * CONFIG%MDS * (CONFIG%MNS-1)
+     CONFIG%TOTAL_SIZE = CONFIG%MESV
+     !   model state shift
+     CONFIG%MSSS = 1 + CONFIG%TOTAL_SIZE
+     CONFIG%MESS = CONFIG%MSSS-1  +  CONFIG%MDS * (CONFIG%MNS-1)
+     CONFIG%TOTAL_SIZE = CONFIG%MESS
+     !   model output vecs
+     CONFIG%MSOV = 1 + CONFIG%TOTAL_SIZE
+     CONFIG%MEOV = CONFIG%MSOV-1  +  CONFIG%MDS * CONFIG%MDO
+     CONFIG%TOTAL_SIZE = CONFIG%MEOV
+     !   model embedding vecs
+     CONFIG%MSEV = 1 + CONFIG%TOTAL_SIZE
+     CONFIG%MEEV = CONFIG%MSEV-1  +  CONFIG%MDE * CONFIG%MNE
+     CONFIG%TOTAL_SIZE = CONFIG%MEEV
+     ! ---------------------------------------------------------------
      !   number of variables
      CONFIG%NUM_VARS = CONFIG%TOTAL_SIZE
      ! ---------------------------------------------------------------
+     !   apositional input shift
+     CONFIG%AISS = 1 + CONFIG%TOTAL_SIZE
+     CONFIG%AISE = CONFIG%AISS-1 + CONFIG%ADN
+     CONFIG%TOTAL_SIZE = CONFIG%AISE
+     !   apositional output shift
+     CONFIG%AOSS = 1 + CONFIG%TOTAL_SIZE
+     CONFIG%AOSE = CONFIG%AOSS-1 + CONFIG%ADO
+     CONFIG%TOTAL_SIZE = CONFIG%AOSE
      !   model input shift
      CONFIG%MISS = 1 + CONFIG%TOTAL_SIZE
-     CONFIG%MISE = CONFIG%MISS-1 + CONFIG%MDI-CONFIG%ADO-CONFIG%MDE
+     CONFIG%MISE = CONFIG%MISS-1 + CONFIG%MDN
      CONFIG%TOTAL_SIZE = CONFIG%MISE
      !   model output shift
      CONFIG%MOSS = 1 + CONFIG%TOTAL_SIZE
      CONFIG%MOSE = CONFIG%MOSS-1 + CONFIG%MDO
      CONFIG%TOTAL_SIZE = CONFIG%MOSE
-     !   apositional input shift
-     CONFIG%AISS = 1 + CONFIG%TOTAL_SIZE
-     CONFIG%AISE = CONFIG%AISS-1 + CONFIG%ADI-CONFIG%ADE
-     CONFIG%TOTAL_SIZE = CONFIG%AISE
   END SUBROUTINE NEW_MODEL_CONFIG
 
+  ! Given a number of X points "NM", and a number of apositional X points
+  ! "NA", update the "RWORK_SIZE" and "IWORK_SIZE" attributes in "CONFIG"
+  ! as well as all related work indices for that size data.
+  SUBROUTINE NEW_FIT_CONFIG(NM, NA, CONFIG)
+    INTEGER, INTENT(IN) :: NM, NA
+    TYPE(MODEL_CONFIG), INTENT(INOUT) :: CONFIG
+    CONFIG%NM = NM
+    CONFIG%NA = NA
+    ! ------------------------------------------------------------
+    ! Set up the real valued work array.
+    CONFIG%RWORK_SIZE = 0
+    ! model gradient
+    CONFIG%SMG = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EMG = CONFIG%SMG-1 + CONFIG%NUM_VARS
+    CONFIG%RWORK_SIZE = CONFIG%EMG
+    ! model gradient mean
+    CONFIG%SMGM = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EMGM = CONFIG%SMGM-1 + CONFIG%NUM_VARS
+    CONFIG%RWORK_SIZE = CONFIG%EMGM
+    ! model gradient curvature
+    CONFIG%SMGC = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EMGC = CONFIG%SMGC-1 + CONFIG%NUM_VARS
+    CONFIG%RWORK_SIZE = CONFIG%EMGC
+    ! best model
+    CONFIG%SBM = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EBM = CONFIG%SBM-1 + CONFIG%NUM_VARS
+    CONFIG%RWORK_SIZE = CONFIG%EBM
+    ! apositional states
+    CONFIG%SAXS = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EAXS = CONFIG%SAXS-1 + CONFIG%NA * CONFIG%ADS * (CONFIG%ANS+1)
+    CONFIG%RWORK_SIZE = CONFIG%EAXS
+    ! apositional model gradients at states
+    CONFIG%SAXG = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EAXG = CONFIG%SAXG-1 + CONFIG%NA * CONFIG%ADS * (CONFIG%ANS+1)
+    CONFIG%RWORK_SIZE = CONFIG%EAXG
+    ! apositional model (internal state) alignment
+    CONFIG%SAA = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EAA = CONFIG%SAA-1 + CONFIG%ADS * CONFIG%ANS
+    CONFIG%RWORK_SIZE = CONFIG%EAA
+    ! AY
+    CONFIG%SAY = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EAY = CONFIG%SAY-1 + CONFIG%NA * CONFIG%ADO
+    CONFIG%RWORK_SIZE = CONFIG%EAY
+    ! AY gradient
+    CONFIG%SAYG = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EAYG = CONFIG%SAYG-1 + CONFIG%NA * CONFIG%ADO
+    CONFIG%RWORK_SIZE = CONFIG%EAYG
+    ! model states
+    CONFIG%SMXS = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EMXS = CONFIG%SMXS-1 + CONFIG%NM * CONFIG%MDS * (CONFIG%MNS+1)
+    CONFIG%RWORK_SIZE = CONFIG%EMXS
+    ! model gradients at states
+    CONFIG%SMXG = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EMXG = CONFIG%SMXG-1 + CONFIG%NM * CONFIG%MDS * (CONFIG%MNS+1)
+    CONFIG%RWORK_SIZE = CONFIG%EMXG
+    ! (positional) model (internal state) alignment
+    CONFIG%SMA = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EMA = CONFIG%SMA-1 + CONFIG%MDS * CONFIG%MNS
+    CONFIG%RWORK_SIZE = CONFIG%EMA
+    ! Y gradient
+    CONFIG%SYG = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EYG = CONFIG%SYG-1 + CONFIG%MDO * CONFIG%NM
+    CONFIG%RWORK_SIZE = CONFIG%EYG
+    ! AX rescale
+    CONFIG%SAXR = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EAXR = CONFIG%SAXR-1 + CONFIG%ADN * CONFIG%ADN
+    CONFIG%RWORK_SIZE = CONFIG%EAXR
+    ! AXI shift
+    CONFIG%SAXIS = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EAXIS = CONFIG%SAXIS-1 + CONFIG%ADE
+    CONFIG%RWORK_SIZE = CONFIG%EAXIS
+    ! AXI rescale
+    CONFIG%SAXIR = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EAXIR = CONFIG%SAXIR-1 + CONFIG%ADE * CONFIG%ADE
+    CONFIG%RWORK_SIZE = CONFIG%EAXIR
+    ! AY rescale
+    CONFIG%SAYR = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EAYR = CONFIG%SAYR-1 + CONFIG%ADO
+    CONFIG%RWORK_SIZE = CONFIG%EAYR
+    ! X rescale
+    CONFIG%SMXR = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EMXR = CONFIG%SMXR-1 + CONFIG%MDN * CONFIG%MDN
+    CONFIG%RWORK_SIZE = CONFIG%EMXR
+    ! XI shift
+    CONFIG%SMXIS = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EMXIS = CONFIG%SMXIS-1 + CONFIG%MDE
+    CONFIG%RWORK_SIZE = CONFIG%EMXIS
+    ! XI rescale
+    CONFIG%SMXIR = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EMXIR = CONFIG%SMXIR-1 + CONFIG%MDE * CONFIG%MDE
+    CONFIG%RWORK_SIZE = CONFIG%EMXIR
+    ! Y rescale
+    CONFIG%SYR = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EYR = CONFIG%SYR-1 + CONFIG%MDO * CONFIG%MDO
+    CONFIG%RWORK_SIZE = CONFIG%EYR
+    ! MODEL ALIGN
+    CONFIG%SFMA = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EFMA = CONFIG%SFMA-1 + CONFIG%NUM_VARS * CONFIG%NUM_THREADS
+    CONFIG%RWORK_SIZE = CONFIG%EFMA
+    ! X_TEMP
+    CONFIG%SXT = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EXT = CONFIG%SXT-1 + (CONFIG%MDE + CONFIG%ADO) * CONFIG%NM * CONFIG%NUM_THREADS
+    CONFIG%RWORK_SIZE = CONFIG%EXT
+    ! ------------------------------------------------------------
+    ! Set up the integer valued work array.
+    CONFIG%IWORK_SIZE = 0
+    ! update indices of model 
+    CONFIG%SUI = 1 + CONFIG%IWORK_SIZE
+    CONFIG%EUI = CONFIG%SUI-1 + CONFIG%NUM_VARS
+    CONFIG%IWORK_SIZE = CONFIG%EUI
+    ! apositional batch starts
+    CONFIG%SBAS = 1 + CONFIG%IWORK_SIZE
+    CONFIG%EBAS = CONFIG%SBAS-1 + CONFIG%NUM_THREADS
+    CONFIG%IWORK_SIZE = CONFIG%EBAS
+    ! apositional batch ends
+    CONFIG%SBAE = 1 + CONFIG%IWORK_SIZE
+    CONFIG%EBAE = CONFIG%SBAE-1 + CONFIG%NUM_THREADS
+    CONFIG%IWORK_SIZE = CONFIG%EBAE
+    ! model batch starts
+    CONFIG%SBMS = 1 + CONFIG%IWORK_SIZE
+    CONFIG%EBMS = CONFIG%SBMS-1 + CONFIG%NUM_THREADS
+    CONFIG%IWORK_SIZE = CONFIG%EBMS
+    ! model batchm ends
+    CONFIG%SBME = 1 + CONFIG%IWORK_SIZE
+    CONFIG%EBME = CONFIG%SBME-1 + CONFIG%NUM_THREADS
+    CONFIG%IWORK_SIZE = CONFIG%EBME
+  END SUBROUTINE NEW_FIT_CONFIG
 
   ! Initialize the weights for a model, optionally provide a random seed.
   SUBROUTINE INIT_MODEL(CONFIG, MODEL, SEED)
     TYPE(MODEL_CONFIG), INTENT(IN) :: CONFIG
     REAL(KIND=RT), INTENT(INOUT), DIMENSION(:) :: MODEL
     INTEGER, INTENT(IN), OPTIONAL :: SEED
     !  Storage for seeding the random number generator (for repeatability).
@@ -382,252 +1018,241 @@
       INTEGER, INTENT(IN) :: MDI, MDS, MNS, MDO, MDE, MNE
       REAL(KIND=RT), DIMENSION(MDI, MDS) :: INPUT_VECS
       REAL(KIND=RT), DIMENSION(MDS) :: INPUT_SHIFT
       REAL(KIND=RT), DIMENSION(MDS, MDS, MNS-1) :: STATE_VECS
       REAL(KIND=RT), DIMENSION(MDS, MNS-1) :: STATE_SHIFT
       REAL(KIND=RT), DIMENSION(MDS, MDO) :: OUTPUT_VECS
       REAL(KIND=RT), DIMENSION(MDE, MNE) :: EMBEDDINGS
+      ! Local holder for "origin" at each layer.
+      REAL(KIND=RT), DIMENSION(MDS) :: ORIGIN
+      INTEGER,       DIMENSION(MDS) :: ORDER
+      INTEGER :: I, J
       ! Generate well spaced random unit-length vectors (no scaling biases)
       ! for all initial variables in the input, internal, output, and embedings.
       CALL RANDOM_UNIT_VECTORS(INPUT_VECS(:,:))
       DO I = 1, MNS-1
          CALL RANDOM_UNIT_VECTORS(STATE_VECS(:,:,I))
       END DO
       CALL RANDOM_UNIT_VECTORS(OUTPUT_VECS(:,:))
       CALL RANDOM_UNIT_VECTORS(EMBEDDINGS(:,:))
       ! Make the output vectors have very small magnitude initially.
       OUTPUT_VECS(:,:) = OUTPUT_VECS(:,:) * CONFIG%INITIAL_OUTPUT_SCALE
       ! Generate random shifts for inputs and internal layers, zero
       !  shift for the output layer (first two will be rescaled).
       DO I = 1, MDS
-         INPUT_SHIFT(I) = 2.0_RT * CONFIG%INITIAL_SHIFT_RANGE * &    ! 2 * shift *
-              (REAL(I-1,RT) / MAX(1.0_RT, REAL(MDS-1, RT))) & ! range [0, 1]
-              - CONFIG%INITIAL_SHIFT_RANGE                           ! - shift
-         STATE_SHIFT(I,:) = INPUT_SHIFT(I) ! range [-shift, shift]
+         INPUT_SHIFT(I) = 2.0_RT * CONFIG%INITIAL_SHIFT_RANGE * & ! 2 * shift *
+              (REAL(I-1,RT) / MAX(1.0_RT, REAL(MDS-1, RT))) &     ! range [0, 1]
+              - CONFIG%INITIAL_SHIFT_RANGE                        ! - shift
+      END DO
+      ! Set the state shifts based on translation of the origin, always try
+      !  to apply translations to bring the origin back closer to center
+      !  (to prevent terrible conditioning of models with many layers).
+      ORIGIN(:) = INPUT_SHIFT(:)
+      DO J = 1, MNS-1
+         ORIGIN(:) = MATMUL(ORIGIN(:), STATE_VECS(:,:,J))
+         ! Argsort the values of origin, adding the most to the smallest values.
+         CALL ARGSORT(ORIGIN(:), ORDER(:))
+         DO I = 1, MDS
+            STATE_SHIFT(ORDER(MDS-I+1),J) = INPUT_SHIFT(I) ! range [-shift, shift]
+         END DO
+         ORIGIN(:) = ORIGIN(:) + STATE_SHIFT(:,J)
       END DO
     END SUBROUTINE UNPACKED_INIT_MODEL
   END SUBROUTINE INIT_MODEL
 
 
   ! Returnn nonzero INFO if any shapes or values do not match expectations.
-  SUBROUTINE CHECK_SHAPE(CONFIG, MODEL, Y, X, XI, AX, AXI, SIZES, INFO)
+  SUBROUTINE CHECK_SHAPE(CONFIG, MODEL, AX, AXI, SIZES, X, XI, Y, INFO)
     TYPE(MODEL_CONFIG), INTENT(IN) :: CONFIG
     REAL(KIND=RT), INTENT(IN), DIMENSION(:) :: MODEL
-    REAL(KIND=RT), INTENT(IN), DIMENSION(:,:) :: Y
-    REAL(KIND=RT), INTENT(IN), DIMENSION(:,:) :: X
-    INTEGER,       INTENT(IN), DIMENSION(:,:) :: XI
     REAL(KIND=RT), INTENT(IN), DIMENSION(:,:) :: AX
     INTEGER,       INTENT(IN), DIMENSION(:,:) :: AXI
     INTEGER,       INTENT(IN), DIMENSION(:) :: SIZES
+    REAL(KIND=RT), INTENT(IN), DIMENSION(:,:) :: X
+    INTEGER,       INTENT(IN), DIMENSION(:,:) :: XI
+    REAL(KIND=RT), INTENT(IN), DIMENSION(:,:) :: Y
     INTEGER,       INTENT(OUT) :: INFO
     INFO = 0
     ! Compute whether the shape matches the CONFIG.
     IF (SIZE(MODEL) .NE. CONFIG%TOTAL_SIZE) THEN
        INFO = 1 ! Model size does not match model configuration.
     ELSE IF (SIZE(X,2) .NE. SIZE(Y,2)) THEN
        INFO = 2 ! Input arrays do not match in size.
-    ELSE IF (SIZE(X,1) + CONFIG%MDE + CONFIG%ADO .NE. CONFIG%MDI) THEN
+    ELSE IF (SIZE(X,1) .NE. CONFIG%MDI) THEN
        INFO = 3 ! X input dimension is bad.
     ELSE IF (SIZE(Y,1) .NE. CONFIG%MDO) THEN
        INFO = 4 ! Output dimension is bad.
     ELSE IF ((CONFIG%MNE .GT. 0) .AND. (SIZE(XI,2) .NE. SIZE(X,2))) THEN
-       INFO = 5 ! Input integer X size does not match.
+       INFO = 5 ! Input integer XI size does not match X.
     ELSE IF ((MINVAL(XI) .LT. 0) .OR. (MAXVAL(XI) .GT. CONFIG%MNE)) THEN
        INFO = 6 ! Input integer X index out of range.
-    ELSE IF ((CONFIG%ADI .GT. 0) .AND. (SIZE(X,2) .NE. SIZE(SIZES))) THEN
-       INFO = 7 ! X and SIZES do not match.
+    ELSE IF ((CONFIG%ADI .GT. 0) .AND. (SIZE(SIZES) .NE. SIZE(Y,2))) THEN
+       INFO = 7 ! SIZES has wrong size.
     ELSE IF (SIZE(AX,2) .NE. SUM(SIZES)) THEN
        INFO = 8 ! AX and SUM(SIZES) do not match.
-    ELSE IF (SIZE(AX,1) + CONFIG%ADE .NE. CONFIG%ADI) THEN
+    ELSE IF (SIZE(AX,1) .NE. CONFIG%ADI) THEN
        INFO = 9 ! AX input dimension is bad.
     ELSE IF (SIZE(AXI,2) .NE. SIZE(AX,2)) THEN
-       INFO = 10 ! Input integer AX size does not match.
+       INFO = 10 ! Input integer AXI size does not match AX.
     ELSE IF ((MINVAL(AXI) .LT. 0) .OR. (MAXVAL(AXI) .GT. CONFIG%ANE)) THEN
        INFO = 11 ! Input integer AX index out of range.
     END IF
   END SUBROUTINE CHECK_SHAPE
 
  
-  ! Given a model and mixed real and integer inputs, embed the inputs
-  !  into their appropriate real-value-only formats.
-  SUBROUTINE EMBED(CONFIG, MODEL, X, XI, AX, AXI, XXI, AXXI)
-    TYPE(MODEL_CONFIG), INTENT(IN) :: CONFIG
-    REAL(KIND=RT), INTENT(IN),  DIMENSION(:) :: MODEL
-    REAL(KIND=RT), INTENT(IN),  DIMENSION(:,:) :: X
-    INTEGER,       INTENT(IN),  DIMENSION(:,:) :: XI
-    REAL(KIND=RT), INTENT(IN),  DIMENSION(:,:) :: AX
-    INTEGER,       INTENT(IN),  DIMENSION(:,:) :: AXI
-    REAL(KIND=RT), INTENT(OUT), DIMENSION(:,:) :: XXI  ! MDI, SIZE(X,2)
-    REAL(KIND=RT), INTENT(OUT), DIMENSION(:,:) :: AXXI ! ADI, SIZE(AX,2)
-    ! Add the real inputs to the front of each vector before apositional outputs.
-    XXI(1:SIZE(X,1),:) = X(:,:)
-    ! If there is XInteger input, unpack it into end of XXI.
-    CALL UNPACK_EMBEDDINGS(CONFIG%MDE, CONFIG%MNE, &
-         MODEL(CONFIG%MSEV:CONFIG%MEEV), &
-         XI(:,:), XXI(SIZE(X,1)+1:SIZE(X,1)+CONFIG%MDE,:))
-    ! Add the real inputs to the front of each vector.
-    AXXI(1:SIZE(AX,1),:) = AX(:,:)
-    ! If there is AXInteger input, unpack it into XXI.
-    CALL UNPACK_EMBEDDINGS(CONFIG%ADE, CONFIG%ANE, &
-         MODEL(CONFIG%ASEV:CONFIG%AEEV), &
-         AXI(:,:), AXXI(SIZE(AX,1)+1:,:))
-  CONTAINS
-    ! Given integer inputs and embedding vectors, put embeddings in
-    !  place of integer inputs inside of a real matrix.
-    SUBROUTINE UNPACK_EMBEDDINGS(MDE, MNE, EMBEDDINGS, INT_INPUTS, EMBEDDED)
-      INTEGER, INTENT(IN) :: MDE, MNE
-      REAL(KIND=RT), INTENT(IN), DIMENSION(MDE, MNE) :: EMBEDDINGS
-      INTEGER, INTENT(IN), DIMENSION(:,:) :: INT_INPUTS
-      REAL(KIND=RT), INTENT(OUT), DIMENSION(:,:) :: EMBEDDED
-      INTEGER :: N, D, E
-      REAL(KIND=RT) :: RD
-      RD = REAL(SIZE(INT_INPUTS,1),RT)
-      ! Add together appropriate embedding vectors based on integer inputs.
-      EMBEDDED(:,:) = 0.0_RT
-      DO N = 1, SIZE(INT_INPUTS,2)
-         DO D = 1, SIZE(INT_INPUTS,1)
-            E = INT_INPUTS(D,N)
-            IF (E .GT. 0) THEN
-               EMBEDDED(:,N) = EMBEDDED(:,N) + EMBEDDINGS(:,E)
-            END IF
-         END DO
-         EMBEDDED(:,N) = EMBEDDED(:,N) / RD
-      END DO
-    END SUBROUTINE UNPACK_EMBEDDINGS
-  END SUBROUTINE EMBED
-
-
   ! Given a number of batches, compute the batch start and ends for
   !  the apositional and positional inputs. Store in (2,_) arrays.
-  SUBROUTINE COMPUTE_BATCHES(NUM_BATCHES, X, AX, SIZES, BATCHA, BATCHM, INFO)
-    INTEGER,       INTENT(IN) :: NUM_BATCHES
-    REAL(KIND=RT), INTENT(IN),  DIMENSION(:,:) :: X
-    REAL(KIND=RT), INTENT(IN),  DIMENSION(:,:) :: AX
+  SUBROUTINE COMPUTE_BATCHES(NUM_BATCHES, NM, NA, SIZES, &
+       BATCHA_STARTS, BATCHA_ENDS, BATCHM_STARTS, BATCHM_ENDS, INFO)
+    INTEGER,       INTENT(IN) :: NUM_BATCHES, NM, NA
     INTEGER,       INTENT(IN),  DIMENSION(:)   :: SIZES
-    INTEGER,       INTENT(OUT), DIMENSION(:,:) :: BATCHA, BATCHM
+    INTEGER,       INTENT(OUT), DIMENSION(:) :: BATCHA_STARTS, BATCHA_ENDS
+    INTEGER,       INTENT(OUT), DIMENSION(:) :: BATCHM_STARTS, BATCHM_ENDS
     INTEGER,       INTENT(INOUT) :: INFO
     ! Local variables.
-    INTEGER :: BATCH, BE, BN, BS, I, MN, AN
-    ! Compute sizes of inputs.
-    IF ((SIZE(SIZES) .GT. 0) .OR. (SIZE(AX,2) .GT. 0)) THEN
-       MN = SIZE(SIZES)
-    ELSE
-       MN = SIZE(X,2)
-    END IF
-    AN = SUM(SIZES(:))
+    INTEGER :: BATCH, BE, BN, BS, I
     ! Check for errors.
-    IF (SIZE(X,2) .NE. MN) THEN
-       PRINT *, 'ERROR (COMPUTE_BATCHES): Sizes of X and SIZES do not match.', SIZE(X,2), SIZE(SIZES)
+    IF (NUM_BATCHES .GT. NM) THEN
+       PRINT *, 'ERROR (COMPUTE_BATCHES): Requested number of batches is too large.', NUM_BATCHES, NM, NA
        INFO = -1
-    ELSE IF (SIZE(AX,2) .NE. AN) THEN
-       PRINT *, 'ERROR (COMPUTE_BATCHES): Size of AX and sum of SIZES do not match.', SIZE(AX,2), AN
+       RETURN
+    ELSE IF (NUM_BATCHES .NE. SIZE(BATCHA_STARTS)) THEN
+       PRINT *, 'ERROR (COMPUTE_BATCHES): Number of batches does not match BATCHA.', NUM_BATCHES, SIZE(BATCHA_STARTS)
        INFO = -2
-    ELSE IF (NUM_BATCHES .GT. MN) THEN
-       PRINT *, 'ERROR (COMPUTE_BATCHES): Requested number of batches is too large.', NUM_BATCHES, MN, AN
+       RETURN
+    ELSE IF (NUM_BATCHES .NE. SIZE(BATCHM_STARTS)) THEN
+       PRINT *, 'ERROR (COMPUTE_BATCHES): Number of batches does not match BATCHM.', NUM_BATCHES, SIZE(BATCHM_STARTS)
        INFO = -3
-    ELSE IF (NUM_BATCHES .NE. SIZE(BATCHA,2)) THEN
-       PRINT *, 'ERROR (COMPUTE_BATCHES): Number of batches does not match BATCHA.', NUM_BATCHES, SIZE(BATCHA,2)
+       RETURN
+    ELSE IF (NUM_BATCHES .LT. 1) THEN
+       PRINT *, 'ERROR (COMPUTE_BATCHES): Number of batches is negative.', NUM_BATCHES
        INFO = -4
-    ELSE IF (NUM_BATCHES .NE. SIZE(BATCHM,2)) THEN
-       PRINT *, 'ERROR (COMPUTE_BATCHES): Number of batches does not match BATCHM.', NUM_BATCHES, SIZE(BATCHM,2)
-       INFO = -5
+       RETURN
     END IF
-    IF (INFO .NE. 0) RETURN
     ! Construct batches for data sets with apositional inputs.
-    IF (AN .GT. 0) THEN
+    IF (NA .GT. 0) THEN
        IF (NUM_BATCHES .EQ. 1) THEN
-          BATCHA(1,1) = 1
-          BATCHA(2,1) = AN
-          BATCHM(1,1) = 1
-          BATCHM(2,1) = MN
+          BATCHA_STARTS(1) = 1
+          BATCHA_ENDS(1) = NA
+          BATCHM_STARTS(1) = 1
+          BATCHM_ENDS(1) = NM
        ELSE
-          BN = (AN + NUM_BATCHES - 1) / NUM_BATCHES ! = CEIL(AN / NUM_BATCHES)
+          BN = (NA + NUM_BATCHES - 1) / NUM_BATCHES ! = CEIL(NA / NUM_BATCHES)
           ! Compute how many X points are associated with each Y.
           BS = 1
           BE = SIZES(1)
           BATCH = 1
-          BATCHM(1,BATCH) = 1
-          DO I = 2, MN
+          BATCHM_STARTS(BATCH) = 1
+          DO I = 2, NM
              ! If a fair share of the points have been aggregated, OR
              !   there are only as many sets left as there are batches.
-             IF ((BE-BS .GT. BN) .OR. (1+MN-I .LE. (NUM_BATCHES-BATCH))) THEN
-                BATCHM(2,BATCH) = I-1
-                BATCHA(1,BATCH) = BS
-                BATCHA(2,BATCH) = BE
+             IF ((BE-BS .GT. BN) .OR. (1+NM-I .LE. (NUM_BATCHES-BATCH))) THEN
+                BATCHM_ENDS(BATCH) = I-1
+                BATCHA_STARTS(BATCH) = BS
+                BATCHA_ENDS(BATCH) = BE
                 BATCH = BATCH+1
-                BATCHM(1,BATCH) = I
+                BATCHM_STARTS(BATCH) = I
                 BS = BE+1
                 BE = BS - 1
              END IF
              BE = BE + SIZES(I)
           END DO
-          BATCHM(2,BATCH) = MN
-          BATCHA(1,BATCH) = BS
-          BATCHA(2,BATCH) = BE
+          BATCHM_ENDS(BATCH) = NM
+          BATCHA_STARTS(BATCH) = BS
+          BATCHA_ENDS(BATCH) = BE
        END IF
     ! Construct batches for data sets that only have positional inputs.
     ELSE
-       BN = (MN + NUM_BATCHES - 1) / NUM_BATCHES ! = CEIL(MN / NUM_BATCHES)
+       BN = (NM + NUM_BATCHES - 1) / NUM_BATCHES ! = CEIL(NM / NUM_BATCHES)
        DO BATCH = 1, NUM_BATCHES
-          BATCHM(1,BATCH) = BN*(BATCH-1) + 1
-          BATCHM(2,BATCH) = MIN(MN, BN*BATCH)
+          BATCHM_STARTS(BATCH) = BN*(BATCH-1) + 1
+          BATCHM_ENDS(BATCH) = MIN(NM, BN*BATCH)
        END DO
-       BATCHA(1,:) = 0
-       BATCHA(2,:) = -1
+       BATCHA_STARTS(:) = 0
+       BATCHA_ENDS(:) = -1
     END IF
   END SUBROUTINE COMPUTE_BATCHES
 
 
+  ! Given a model and mixed real and integer inputs, embed the integer
+  !  inputs into their appropriate real-value-only formats.
+  SUBROUTINE EMBED(CONFIG, MODEL, AXI, XI, AX, X)
+    TYPE(MODEL_CONFIG), INTENT(IN) :: CONFIG
+    REAL(KIND=RT), INTENT(IN),  DIMENSION(:) :: MODEL
+    INTEGER,       INTENT(IN),  DIMENSION(:,:) :: AXI
+    INTEGER,       INTENT(IN),  DIMENSION(:,:) :: XI
+    REAL(KIND=RT), INTENT(OUT), DIMENSION(:,:) :: AX ! ADI, SIZE(AX,2)
+    REAL(KIND=RT), INTENT(OUT), DIMENSION(:,:) :: X  ! MDI, SIZE(X,2)
+    ! If there is AXInteger input, unpack it into X.
+    CALL UNPACK_EMBEDDINGS(CONFIG%ADE, CONFIG%ANE, &
+         MODEL(CONFIG%ASEV:CONFIG%AEEV), &
+         AXI(:,:), AX(CONFIG%ADI-CONFIG%ADE+1:,:))
+    ! If there is XInteger input, unpack it into end of X.
+    CALL UNPACK_EMBEDDINGS(CONFIG%MDE, CONFIG%MNE, &
+         MODEL(CONFIG%MSEV:CONFIG%MEEV), &
+         XI(:,:), X(CONFIG%MDI-CONFIG%MDE-CONFIG%ADO+1:CONFIG%MDI-CONFIG%ADO,:))
+  CONTAINS
+    ! Given integer inputs and embedding vectors, put embeddings in
+    !  place of integer inputs inside of a real matrix.
+    SUBROUTINE UNPACK_EMBEDDINGS(MDE, MNE, EMBEDDINGS, INT_INPUTS, EMBEDDED)
+      INTEGER, INTENT(IN) :: MDE, MNE
+      REAL(KIND=RT), INTENT(IN), DIMENSION(MDE, MNE) :: EMBEDDINGS
+      INTEGER, INTENT(IN), DIMENSION(:,:) :: INT_INPUTS
+      REAL(KIND=RT), INTENT(OUT), DIMENSION(:,:) :: EMBEDDED
+      INTEGER :: N, D, E
+      REAL(KIND=RT) :: RD
+      RD = REAL(SIZE(INT_INPUTS,1),RT)
+      ! Add together appropriate embedding vectors based on integer inputs.
+      EMBEDDED(:,:) = 0.0_RT
+      DO N = 1, SIZE(INT_INPUTS,2)
+         DO D = 1, SIZE(INT_INPUTS,1)
+            E = INT_INPUTS(D,N)
+            IF (E .GT. 0) THEN
+               EMBEDDED(:,N) = EMBEDDED(:,N) + EMBEDDINGS(:,E)
+            END IF
+         END DO
+         EMBEDDED(:,N) = EMBEDDED(:,N) / RD
+      END DO
+    END SUBROUTINE UNPACK_EMBEDDINGS
+  END SUBROUTINE EMBED
+
+
   ! Evaluate the piecewise linear regression model, assume already-embedded inputs.
-  SUBROUTINE EVALUATE(CONFIG, MODEL, Y, X, AX, SIZES, M_STATES, &
-       A_STATES, AY, INFO, SHIFT, THREADS)
+  SUBROUTINE EVALUATE(CONFIG, MODEL, AX, AY, SIZES, X, Y, A_STATES, M_STATES, INFO)
     TYPE(MODEL_CONFIG), INTENT(IN) :: CONFIG
     REAL(KIND=RT), INTENT(IN),  DIMENSION(:) :: MODEL
-    REAL(KIND=RT), INTENT(OUT),   DIMENSION(:,:) :: Y
-    REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: X
     REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: AX
+    REAL(KIND=RT), INTENT(OUT),   DIMENSION(:,:) :: AY
     INTEGER,       INTENT(IN),    DIMENSION(:)   :: SIZES
-    REAL(KIND=RT), INTENT(OUT),   DIMENSION(:,:,:) :: M_STATES ! SIZE(X, 2), MDS, (MNS|2)
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: X
+    REAL(KIND=RT), INTENT(OUT),   DIMENSION(:,:) :: Y
     REAL(KIND=RT), INTENT(OUT),   DIMENSION(:,:,:) :: A_STATES ! SIZE(AX,2), ADS, (ANS|2)
-    REAL(KIND=RT), INTENT(OUT),   DIMENSION(:,:) :: AY ! SIZE(AX,2), ADO
+    REAL(KIND=RT), INTENT(OUT),   DIMENSION(:,:,:) :: M_STATES ! SIZE(X, 2), MDS, (MNS|2)
     INTEGER, INTENT(INOUT) :: INFO
-    LOGICAL, INTENT(IN), OPTIONAL :: SHIFT
-    INTEGER, INTENT(IN), OPTIONAL :: THREADS
     ! Internal values.
-    LOGICAL :: APPLY_SHIFT
     INTEGER :: I, BATCH, NB, BN, BS, BE, BT, GS, GE, NT
-    INTEGER, DIMENSION(:,:), ALLOCATABLE :: BATCHA, BATCHM
-    ! Set default for shifting data.
-    IF (PRESENT(SHIFT)) THEN
-       APPLY_SHIFT = SHIFT
-    ELSE
-       APPLY_SHIFT = .TRUE.
-    END IF
-    ! Set default for the number of threads.
-    IF (PRESENT(THREADS)) THEN
-       NT = THREADS
-    ELSE
-       NT = CONFIG%NUM_THREADS
-    END IF
+    INTEGER, DIMENSION(:), ALLOCATABLE :: BATCHA_STARTS, BATCHA_ENDS, BATCHM_STARTS, BATCHM_ENDS
     ! Set up batching for parallelization.
-    NB = MIN(SIZE(Y,2), NT)
-    ALLOCATE(BATCHA(2,NB), BATCHM(2,NB))
+    NB = MIN(SIZE(Y,2), CONFIG%NUM_THREADS)
+    NT = MIN(CONFIG%NUM_THREADS, NB)
     ! Compute the batch start and end indices.
-    CALL COMPUTE_BATCHES(NB, X, AX, SIZES, BATCHA, BATCHM, INFO)
+    ALLOCATE(BATCHA_STARTS(NB), BATCHA_ENDS(NB), BATCHM_STARTS(NB), BATCHM_ENDS(NB))
+    CALL COMPUTE_BATCHES(NB, SIZE(X,2), SIZE(AX,2), SIZES, &
+         BATCHA_STARTS, BATCHA_ENDS, BATCHM_STARTS, BATCHM_ENDS, INFO)
     IF (INFO .NE. 0) RETURN
-    !$OMP PARALLEL DO NUM_THREADS(NT) PRIVATE(I, BS, BE, BT) IF(NB > 1)
+    !$OMP PARALLEL DO NUM_THREADS(NT) PRIVATE(I, BS, BE, BT, GS, GE) IF(NB > 1)
     batch_evaluation : DO BATCH = 1, NB
        ! If there is an apositional model, apply it.
        IF (CONFIG%ADI .GT. 0) THEN
-          BS = BATCHA(1,BATCH)
-          BE = BATCHA(2,BATCH)
+          BS = BATCHA_STARTS(BATCH)
+          BE = BATCHA_ENDS(BATCH)
           BT = BE-BS+1
           IF (BT .EQ. 0) CYCLE batch_evaluation
           ! Apply shift terms to apositional inputs.
-          IF (APPLY_SHIFT) THEN
+          IF (CONFIG%APPLY_SHIFT) THEN
              GE = CONFIG%ADI-CONFIG%ADE
              IF (GE .GT. 0) THEN
                 DO I = BS, BE
                    AX(:GE,I) = AX(:GE,I) + MODEL(CONFIG%AISS:CONFIG%AISE)
                 END DO
              END IF
           END IF
@@ -637,57 +1262,76 @@
                MODEL(CONFIG%ASIV:CONFIG%AEIV), &
                MODEL(CONFIG%ASIS:CONFIG%AEIS), &
                MODEL(CONFIG%ASSV:CONFIG%AESV), &
                MODEL(CONFIG%ASSS:CONFIG%AESS), &
                MODEL(CONFIG%ASOV:CONFIG%AEOV), &
                AX(:,BS:BE), AY(BS:BE,:), A_STATES(BS:BE,:,:), YTRANS=.TRUE.)
           ! Aggregate the outputs from the apositional model.
-          BT = SIZE(X,1)-CONFIG%ADO+1 ! <- reuse this variable name
+          BT = CONFIG%MDN+CONFIG%MDE+1 ! <- reuse to be "start of apositional output"
           GS = BS
-          DO I = BATCHM(1,BATCH), BATCHM(2,BATCH)
+          ! Always apply shift terms to apositional model outputs.
+          DO I = 1, CONFIG%ADO
+             AY(BS:BE,I) = AY(BS:BE,I) + MODEL(CONFIG%AOSS + I-1)
+          END DO
+          ! Take the mean of all outputs from the apositional model.
+          DO I = BATCHM_STARTS(BATCH), BATCHM_ENDS(BATCH)
              GE = GS + SIZES(I) - 1
              X(BT:,I) = SUM(AY(GS:GE,:), 1) / REAL(SIZES(I),RT) 
              GS = GE + 1
           END DO
-          BS = BATCHM(1,BATCH)
-          BE = BATCHM(2,BATCH)
+          ! Unapply shift terms to apositional inputs.
+          IF (CONFIG%APPLY_SHIFT) THEN
+             GE = CONFIG%ADI-CONFIG%ADE
+             IF (GE .GT. 0) THEN
+                DO I = BS, BE
+                   AX(:GE,I) = AX(:GE,I) - MODEL(CONFIG%AISS:CONFIG%AISE)
+                END DO
+             END IF
+          END IF
+          ! Update "BS", "BE", and "BT" to coincide with the model.
+          BS = BATCHM_STARTS(BATCH)
+          BE = BATCHM_ENDS(BATCH)
           BT = BE-BS+1
        ELSE
-          BS = BATCHM(1,BATCH)
-          BE = BATCHM(2,BATCH)
+          BS = BATCHM_STARTS(BATCH)
+          BE = BATCHM_ENDS(BATCH)
           BT = BE-BS+1
           IF (BT .EQ. 0) CYCLE batch_evaluation
        END IF
-       ! Apply shift terms to model inputs.
-       IF (APPLY_SHIFT) THEN
-          GE = CONFIG%MDI-CONFIG%MDE-CONFIG%ADO
-          IF (GE .GT. 0) THEN
+       ! Regular model forward pass.
+       IF (CONFIG%MDI .GT. 0) THEN
+          ! Apply shift terms to model inputs.
+          IF ((CONFIG%APPLY_SHIFT) .AND. (CONFIG%MDN .GT. 0)) THEN
              DO I = BS, BE
-                X(:GE,I) = X(:GE,I) + MODEL(CONFIG%MISS:CONFIG%MISE)
+                X(:CONFIG%MDN,I) = X(:CONFIG%MDN,I) + MODEL(CONFIG%MISS:CONFIG%MISE)
+             END DO
+          END IF
+          ! Run the positional model.
+          CALL UNPACKED_EVALUATE(BT, &
+               CONFIG%MDI, CONFIG%MDS, CONFIG%MNS, CONFIG%MDO, &
+               MODEL(CONFIG%MSIV:CONFIG%MEIV), &
+               MODEL(CONFIG%MSIS:CONFIG%MEIS), &
+               MODEL(CONFIG%MSSV:CONFIG%MESV), &
+               MODEL(CONFIG%MSSS:CONFIG%MESS), &
+               MODEL(CONFIG%MSOV:CONFIG%MEOV), &
+               X(:,BS:BE), Y(:,BS:BE), M_STATES(BS:BE,:,:), YTRANS=.FALSE.)
+          ! Apply shift terms to model outputs.
+          IF (CONFIG%APPLY_SHIFT) THEN
+             DO I = BS, BE
+                Y(:,I) = Y(:,I) + MODEL(CONFIG%MOSS:CONFIG%MOSE)
+             END DO
+             ! Unapply the X shifts.
+             DO I = BS, BE
+                X(:CONFIG%MDN,I) = X(:CONFIG%MDN,I) - MODEL(CONFIG%MISS:CONFIG%MISE)
              END DO
           END IF
-       END IF
-       ! Run the positional model.
-       CALL UNPACKED_EVALUATE(BT, &
-            CONFIG%MDI, CONFIG%MDS, CONFIG%MNS, CONFIG%MDO, &
-            MODEL(CONFIG%MSIV:CONFIG%MEIV), &
-            MODEL(CONFIG%MSIS:CONFIG%MEIS), &
-            MODEL(CONFIG%MSSV:CONFIG%MESV), &
-            MODEL(CONFIG%MSSS:CONFIG%MESS), &
-            MODEL(CONFIG%MSOV:CONFIG%MEOV), &
-            X(:,BS:BE), Y(:,BS:BE), M_STATES(BS:BE,:,:))
-       ! Apply shift terms to model outputs.
-       IF (APPLY_SHIFT) THEN
-          DO I = BS, BE
-             Y(:,I) = Y(:,I) + MODEL(CONFIG%MOSS:CONFIG%MOSE)
-          END DO
        END IF
     END DO batch_evaluation
     !$OMP END PARALLEL DO
-    DEALLOCATE(BATCHA, BATCHM)
+    DEALLOCATE(BATCHA_STARTS, BATCHA_ENDS, BATCHM_STARTS, BATCHM_ENDS)
 
   CONTAINS
 
     SUBROUTINE UNPACKED_EVALUATE(N, MDI, MDS, MNS, MDO, INPUT_VECS, &
          INPUT_SHIFT, STATE_VECS, STATE_SHIFT, OUTPUT_VECS, X, Y, &
          STATES, YTRANS)
       INTEGER, INTENT(IN) :: N, MDI, MDS, MNS, MDO
@@ -695,61 +1339,52 @@
       REAL(KIND=RT), INTENT(IN),  DIMENSION(MDS) :: INPUT_SHIFT
       REAL(KIND=RT), INTENT(IN),  DIMENSION(MDS, MDS, MNS-1) :: STATE_VECS
       REAL(KIND=RT), INTENT(IN),  DIMENSION(MDS, MNS-1) :: STATE_SHIFT
       REAL(KIND=RT), INTENT(IN),  DIMENSION(MDS, MDO) :: OUTPUT_VECS
       REAL(KIND=RT), INTENT(IN),  DIMENSION(:,:) :: X
       REAL(KIND=RT), INTENT(OUT), DIMENSION(:,:) :: Y
       REAL(KIND=RT), INTENT(OUT), DIMENSION(:,:,:) :: STATES
-      LOGICAL, INTENT(IN), OPTIONAL :: YTRANS
+      LOGICAL, INTENT(IN) :: YTRANS
       ! Local variables to evaluating a single batch.
       INTEGER :: D, L, S1, S2, S3
-      LOGICAL :: REUSE_STATES, YT
-      IF (PRESENT(YTRANS)) THEN
-         YT = YTRANS
-      ELSE
-         YT = .FALSE.
-      END IF
+      LOGICAL :: REUSE_STATES
       REUSE_STATES = (SIZE(STATES,3) .LT. MNS)
       ! Compute the input transformation.
       CALL GEMM('T', 'N', N, MDS, MDI, 1.0_RT, &
            X(:,:), SIZE(X,1), &
            INPUT_VECS(:,:), SIZE(INPUT_VECS,1), &
            0.0_RT, STATES(:,:,1), N)
       ! Apply the rectification.
       DO D = 1, MDS
          STATES(:,D,1) = MAX(STATES(:,D,1) + INPUT_SHIFT(D), CONFIG%DISCONTINUITY)
       END DO
       ! Compute the next set of internal values with a rectified activation.
       DO L = 1, MNS-1
          ! Determine the storage locations of values based on number of states.
-         IF (REUSE_STATES) THEN
-            S1 = 1 ; S2 = 2   ; S3 = 1
-         ELSE
-            S1 = L ; S2 = L+1 ; S3 = L+1
+         IF (REUSE_STATES) THEN ; S1 = 1 ; S2 = 2   ; S3 = 1
+         ELSE                   ; S1 = L ; S2 = L+1 ; S3 = L+1
          END IF
          ! Compute all vectors.
          CALL GEMM('N', 'N', N, MDS, MDS, 1.0_RT, &
               STATES(:,:,S1), N, &
               STATE_VECS(:,:,L), SIZE(STATE_VECS,1), &
               0.0_RT, STATES(:,:,S2), N)
          ! Compute all piecewise linear functions and apply the rectification.
          DO D = 1, MDS
             STATES(:,D,S3) = MAX(STATES(:,D,S2) + STATE_SHIFT(D,L), CONFIG%DISCONTINUITY)
          END DO
       END DO
       ! Set the location of the "previous state output".
-      IF (REUSE_STATES) THEN
-         S3 = 1
-      ELSE
-         S3 = MNS
+      IF (REUSE_STATES) THEN ; S3 = 1
+      ELSE                   ; S3 = MNS
       END IF
       ! Return the final output (default to assuming Y is contiguous
       !   by component unless PRESENT(YTRANS) and YTRANS = .TRUE.
       !   then assume it is contiguous by individual sample).
-      IF (YT) THEN
+      IF (YTRANS) THEN
          CALL GEMM('N', 'N', N, MDO, MDS, 1.0_RT, &
               STATES(:,:,S3), N, &
               OUTPUT_VECS(:,:), SIZE(OUTPUT_VECS,1), &
               0.0_RT, Y(:,:), SIZE(Y,1))
       ELSE
          CALL GEMM('T', 'T', MDO, N, MDS, 1.0_RT, &
               OUTPUT_VECS(:,:), SIZE(OUTPUT_VECS,1), &
@@ -762,43 +1397,43 @@
 
   ! Given the values at all internal states in the model and an output
   !  gradient, propogate the output gradient through the model and
   !  return the gradient of all basis functions.
   SUBROUTINE BASIS_GRADIENT(CONFIG, MODEL, Y, X, AX, SIZES, &
        M_STATES, A_STATES, AY, GRAD)
     TYPE(MODEL_CONFIG), INTENT(IN) :: CONFIG
-    REAL(KIND=RT), INTENT(IN),  DIMENSION(:) :: MODEL
-    REAL(KIND=RT), INTENT(IN), DIMENSION(:,:) :: Y
-    REAL(KIND=RT), INTENT(INOUT),  DIMENSION(:,:) :: X
-    REAL(KIND=RT), INTENT(INOUT),  DIMENSION(:,:) :: AX
-    INTEGER,       INTENT(IN),  DIMENSION(:)   :: SIZES
+    REAL(KIND=RT), INTENT(IN),    DIMENSION(:) :: MODEL
+    REAL(KIND=RT), INTENT(IN),    DIMENSION(:,:) :: Y
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: X
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: AX
+    INTEGER,       INTENT(IN),    DIMENSION(:) :: SIZES
     REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:,:) :: M_STATES ! SIZE(X, 2), MDS, MNS+1
     REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:,:) :: A_STATES ! SIZE(AX,2), ADS, ANS+1
     REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: AY ! SIZE(AX,2), ADO
-    REAL(KIND=RT), INTENT(OUT), DIMENSION(:) :: GRAD ! model gradient
+    REAL(KIND=RT), INTENT(OUT),   DIMENSION(:) :: GRAD
     ! Set the dimension of the X gradient that should be calculated.
     INTEGER :: I, J, GS, GE, XDG
+    XDG = CONFIG%MDE
     IF (CONFIG%ADI .GT. 0) THEN
-       XDG = CONFIG%ADO + CONFIG%MDE
-    ELSE
-       XDG = CONFIG%MDE
+       XDG = XDG + CONFIG%ADO
     END IF
     ! Do the backward gradient calculation assuming "Y" contains output gradient.
     CALL UNPACKED_BASIS_GRADIENT( Y(:,:), M_STATES(:,:,:), X(:,:), &
          CONFIG%MDI, CONFIG%MDS, CONFIG%MNS, CONFIG%MDO, XDG, &
          MODEL(CONFIG%MSIV:CONFIG%MEIV), &
          MODEL(CONFIG%MSIS:CONFIG%MEIS), &
          MODEL(CONFIG%MSSV:CONFIG%MESV), &
          MODEL(CONFIG%MSSS:CONFIG%MESS), &
          MODEL(CONFIG%MSOV:CONFIG%MEOV), &
          GRAD(CONFIG%MSIV:CONFIG%MEIV), &
          GRAD(CONFIG%MSIS:CONFIG%MEIS), &
          GRAD(CONFIG%MSSV:CONFIG%MESV), &
          GRAD(CONFIG%MSSS:CONFIG%MESS), &
-         GRAD(CONFIG%MSOV:CONFIG%MEOV))
+         GRAD(CONFIG%MSOV:CONFIG%MEOV), &
+         YTRANS=.FALSE.) ! Y is in COLUMN vector format.
     ! Propogate the gradient form X into the aggregate outputs.
     IF (CONFIG%ADI .GT. 0) THEN
        XDG = SIZE(X,1) - CONFIG%ADO + 1
        GS = 1
        DO I = 1, SIZE(SIZES)
           GE = GS + SIZES(I) - 1
           DO J = GS, GE
@@ -814,15 +1449,16 @@
             MODEL(CONFIG%ASSV:CONFIG%AESV), &
             MODEL(CONFIG%ASSS:CONFIG%AESS), &
             MODEL(CONFIG%ASOV:CONFIG%AEOV), &
             GRAD(CONFIG%ASIV:CONFIG%AEIV), &
             GRAD(CONFIG%ASIS:CONFIG%AEIS), &
             GRAD(CONFIG%ASSV:CONFIG%AESV), &
             GRAD(CONFIG%ASSS:CONFIG%AESS), &
-            GRAD(CONFIG%ASOV:CONFIG%AEOV), YTRANS=.TRUE.)
+            GRAD(CONFIG%ASOV:CONFIG%AEOV), &
+            YTRANS=.TRUE.) ! AY is in ROW vector format.
     END IF
 
   CONTAINS
     ! Compute the model gradient.
     SUBROUTINE UNPACKED_BASIS_GRADIENT( Y, STATES, X, &
          MDI, MDS, MNS, MDO, MDE, &
          INPUT_VECS, INPUT_SHIFT, &
@@ -842,33 +1478,27 @@
       REAL(KIND=RT), INTENT(IN), DIMENSION(MDS,MDO) :: OUTPUT_VECS
       ! Model variable gradients.
       REAL(KIND=RT), INTENT(INOUT), DIMENSION(MDI,MDS) :: INPUT_VECS_GRADIENT
       REAL(KIND=RT), INTENT(INOUT), DIMENSION(MDS) :: INPUT_SHIFT_GRADIENT
       REAL(KIND=RT), INTENT(INOUT), DIMENSION(MDS,MDS,MNS-1) :: STATE_VECS_GRADIENT
       REAL(KIND=RT), INTENT(INOUT), DIMENSION(MDS,MNS-1) :: STATE_SHIFT_GRADIENT
       REAL(KIND=RT), INTENT(INOUT), DIMENSION(MDS,MDO) :: OUTPUT_VECS_GRADIENT
-      LOGICAL, INTENT(IN), OPTIONAL :: YTRANS
+      LOGICAL, INTENT(IN) :: YTRANS
       ! D   - dimension index
       ! L   - layer index
       ! LP1 - layer index "plus 1" -> "P1"
       INTEGER :: D, L, LP1
       CHARACTER :: YT
       ! Number of points.
       REAL(KIND=RT) :: N, NORM
       ! Get the number of points.
       N = REAL(SIZE(X,2), RT)
       ! Set default for assuming Y is transposed (row vectors).
-      IF (PRESENT(YTRANS)) THEN
-         IF (YTRANS) THEN
-            YT = 'N'
-         ELSE
-            YT = 'T'
-         END IF
-      ELSE
-         YT = 'T'
+      IF (YTRANS) THEN ; YT = 'N'
+      ELSE             ; YT = 'T'
       END IF
       ! Compute the gradient of variables with respect to the "output gradient"
       CALL GEMM('T', YT, MDS, MDO, SIZE(X,2), 1.0_RT / N, &
            STATES(:,:,MNS), SIZE(STATES,1), &
            Y(:,:), SIZE(Y,1), &
            1.0_RT, OUTPUT_VECS_GRADIENT(:,:), SIZE(OUTPUT_VECS_GRADIENT,1))
       ! Propogate the gradient back to the last internal vector space.
@@ -959,363 +1589,671 @@
        END IF
     END DO
   END SUBROUTINE EMBEDDING_GRADIENT
 
 
   ! Compute the gradient of the sum of squared error of this regression
   ! model with respect to its variables given input and output pairs.
-  SUBROUTINE MODEL_GRADIENT(CONFIG, MODEL, Y, X, XI, AX, AXI, SIZES, &
-       SUM_SQUARED_GRADIENT, MODEL_GRAD, ERROR_GRADIENT, INFO, SHIFT, THREADS)
+  SUBROUTINE MODEL_GRADIENT(CONFIG, MODEL, AX, AXI, AY, SIZES, X, XI, Y, &
+       SUM_SQUARED_GRADIENT, MODEL_GRAD, A_ALIGN, M_ALIGN, MODEL_ALIGN, &
+       X_TEMP, AY_GRAD, Y_GRADIENT, A_STATES, A_GRADS, M_STATES, M_GRADS, &
+       INFO)
     TYPE(MODEL_CONFIG), INTENT(IN) :: CONFIG
     REAL(KIND=RT), INTENT(IN), DIMENSION(:) :: MODEL
-    REAL(KIND=RT), INTENT(IN), DIMENSION(:,:) :: Y
-    REAL(KIND=RT), INTENT(IN), DIMENSION(:,:) :: X
-    INTEGER,       INTENT(IN), DIMENSION(:,:) :: XI
-    REAL(KIND=RT), INTENT(IN), DIMENSION(:,:) :: AX
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: AX
     INTEGER,       INTENT(IN), DIMENSION(:,:) :: AXI
-    INTEGER,       INTENT(IN), DIMENSION(:)   :: SIZES
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: AY
+    INTEGER,       INTENT(IN), DIMENSION(:) :: SIZES
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: X
+    INTEGER,       INTENT(IN), DIMENSION(:,:) :: XI
+    REAL(KIND=RT), INTENT(IN), DIMENSION(:,:) :: Y
     ! Sum (over all data) squared error (summed over dimensions).
     REAL(KIND=RT), INTENT(INOUT) :: SUM_SQUARED_GRADIENT
     ! Gradient of the model parameters.
     REAL(KIND=RT), INTENT(OUT), DIMENSION(:) :: MODEL_GRAD
-    ! Interface to subroutine that computes the error gradient given outputs and targets.
-    INTERFACE
-       SUBROUTINE ERROR_GRADIENT(TARGETS, OUTPUTS)
-         USE ISO_FORTRAN_ENV, ONLY: RT => REAL32
-         REAL(KIND=RT), INTENT(IN),    DIMENSION(:,:) :: TARGETS
-         REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: OUTPUTS
-       END SUBROUTINE ERROR_GRADIENT
-    END INTERFACE
+    REAL(KIND=RT), INTENT(OUT), DIMENSION(:,:) :: A_ALIGN, M_ALIGN
+    ! Work space.
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(SIZE(MODEL_GRAD)) :: MODEL_ALIGN
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(CONFIG%MDE+CONFIG%ADO, SIZE(X,2)) :: X_TEMP
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(SIZE(AX,2),CONFIG%ADO) :: AY_GRAD
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(CONFIG%MDO,SIZE(Y,2)) :: Y_GRADIENT
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(SIZE(X,2),CONFIG%MDS,CONFIG%MNS+1) :: M_STATES, M_GRADS
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(SIZE(AX,2),CONFIG%ADS,CONFIG%ANS+1) :: A_STATES, A_GRADS
+    ! Output and optional inputs.
     INTEGER, INTENT(INOUT) :: INFO
-    LOGICAL, INTENT(IN), OPTIONAL :: SHIFT
-    INTEGER, INTENT(IN), OPTIONAL :: THREADS
-    ! Local allocations for computing gradient.
-    REAL(KIND=RT), DIMENSION(CONFIG%MDI,SIZE(X,2)) :: XXI
-    REAL(KIND=RT), DIMENSION(CONFIG%ADI,SIZE(AX,2)) :: AXXI
-    REAL(KIND=RT), DIMENSION(CONFIG%MDO,SIZE(Y,2)) :: Y_GRADIENT
-    REAL(KIND=RT), DIMENSION(SIZE(X,2),CONFIG%MDS,CONFIG%MNS+1) :: M_STATES
-    REAL(KIND=RT), DIMENSION(SIZE(AX,2),CONFIG%ADS,CONFIG%ANS+1) :: A_STATES
-    REAL(KIND=RT), DIMENSION(SIZE(AX,2),CONFIG%ADO) :: AY
+    INTEGER :: L, D
     ! Embed all integer inputs into real matrix inputs.
-    CALL EMBED(CONFIG, MODEL, X, XI, AX, AXI, XXI, AXXI)
+    CALL EMBED(CONFIG, MODEL, AXI, XI, AX, X)
     ! Evaluate the model, storing internal states (for gradient calculation).
-    CALL EVALUATE(CONFIG, MODEL, Y_GRADIENT, XXI, AXXI, SIZES, &
-         M_STATES, A_STATES, AY, INFO, SHIFT=SHIFT, THREADS=THREADS)
+    CALL EVALUATE(CONFIG, MODEL, AX, AY, SIZES, X, Y_GRADIENT, A_STATES, M_STATES, INFO)
+    ! --------------------------------------------------------------------------
+    ! Measure model alignmnt with function.
+    X_TEMP(:,:) = X(CONFIG%MDI-SIZE(X_TEMP,1)+1:,:)
+    A_GRADS(:,:,:) = A_STATES(:,:,:)
+    AY_GRAD(:,:) = AY(:,:)
+    M_GRADS(:,:,:) = M_STATES(:,:,:)
+    CALL BASIS_GRADIENT(CONFIG, MODEL, Y, X, AX, &
+         SIZES, M_GRADS, A_GRADS, AY_GRAD, MODEL_ALIGN)
+    ! Compute the "alignment" by summing the gradient over output vectors.
+    CALL UNPACKED_COMPUTE_ALIGNMENT( &
+         CONFIG%MDS, CONFIG%MNS, CONFIG%MDO, &
+         MODEL_ALIGN(CONFIG%MSSV:CONFIG%MESV), &
+         MODEL_ALIGN(CONFIG%MSOV:CONFIG%MEOV), &
+         M_ALIGN(:,:))
+    CALL UNPACKED_COMPUTE_ALIGNMENT( &
+         CONFIG%ADS, CONFIG%ANS, CONFIG%ADO, &
+         MODEL_ALIGN(CONFIG%ASSV:CONFIG%AESV), &
+         MODEL_ALIGN(CONFIG%ASOV:CONFIG%AEOV), &
+         A_ALIGN(:,:))
+    ! Reset X values (embedding values and apositional outputs).
+    X(CONFIG%MDI-SIZE(X_TEMP,1)+1:,:) = X_TEMP(:,:)
+    ! --------------------------------------------------------------------------
     ! Compute the gradient of the model outputs, overwriting "Y_GRADIENT"
-    CALL ERROR_GRADIENT(Y, Y_GRADIENT)
+    Y_GRADIENT(:,:) = Y_GRADIENT(:,:) - Y(:,:) ! squared error gradient
     SUM_SQUARED_GRADIENT = SUM_SQUARED_GRADIENT + SUM(Y_GRADIENT(:,:)**2)
+    ! Copy the state values into holders for the gradients.
+    A_GRADS(:,:,:) = A_STATES(:,:,:)
+    AY_GRAD(:,:) = AY(:,:)
+    M_GRADS(:,:,:) = M_STATES(:,:,:)
     ! Compute the gradient with respect to the model basis functions.
-    CALL BASIS_GRADIENT(CONFIG, MODEL, Y_GRADIENT, XXI, AXXI, &
-         SIZES, M_STATES, A_STATES, AY, MODEL_GRAD)
+    CALL BASIS_GRADIENT(CONFIG, MODEL, Y_GRADIENT, X, AX, &
+         SIZES, M_GRADS, A_GRADS, AY_GRAD, MODEL_GRAD)
     ! Convert the computed input gradients into average gradients for each embedding.
-    IF (SIZE(XI,1) .GT. 0) THEN
+    IF (CONFIG%MDE .GT. 0) THEN
        CALL EMBEDDING_GRADIENT(CONFIG%MDE, CONFIG%MNE, &
-            XI, XXI(CONFIG%ADO+SIZE(X,1)+1:,:), &
+            XI, X(CONFIG%MDI-CONFIG%ADO-CONFIG%MDE+1:CONFIG%MDI-CONFIG%ADO,:), &
             MODEL_GRAD(CONFIG%MSEV:CONFIG%MEEV))
     END IF
     ! Convert the computed input gradients into average gradients for each embedding.
-    IF (SIZE(AXI,1) .GT. 0) THEN
+    IF (CONFIG%ADE .GT. 0) THEN
        CALL EMBEDDING_GRADIENT(CONFIG%ADE, CONFIG%ANE, &
-            AXI, AXXI(SIZE(AX,1)+1:,:), &
+            AXI, AX(CONFIG%ADI-CONFIG%ADE+1:CONFIG%ADI,:), &
             MODEL_GRAD(CONFIG%ASEV:CONFIG%AEEV))
     END IF
-  END SUBROUTINE MODEL_GRADIENT
 
+  CONTAINS
+    ! Sum the output alignments for each internal state.
+    SUBROUTINE UNPACKED_COMPUTE_ALIGNMENT(MDS, MNS, MDO, &
+         STATE_VECS, OUTPUT_VECS, ALIGNMENT)
+      INTEGER, INTENT(IN) :: MDS, MNS, MDO
+      REAL(KIND=RT), INTENT(IN), DIMENSION(MDS,MDS,MNS-1) :: STATE_VECS
+      REAL(KIND=RT), INTENT(IN), DIMENSION(MDS,MDO) :: OUTPUT_VECS
+      REAL(KIND=RT), INTENT(OUT), DIMENSION(MDS,MNS) :: ALIGNMENT
+      INTEGER :: L
+      IF (MNS .GT. 0) THEN
+         DO L = 1, MNS-1
+            ALIGNMENT(:,L) = ALIGNMENT(:,L) + SUM(STATE_VECS(:,:,L), 2)
+         END DO
+         ALIGNMENT(:,MNS) = ALIGNMENT(:,MNS) + SUM(OUTPUT_VECS(:,:), 2)
+      END IF
+    END SUBROUTINE UNPACKED_COMPUTE_ALIGNMENT
 
-  ! Compute the sum of squared error, store the gradient in the OUTPUTS.
-  !   TARGETS - row vectors containing target values
-  !   OUTPUTS - column vectors containing model predictions
-  SUBROUTINE SQUARED_ERROR_GRADIENT(TARGETS, OUTPUTS)
-    REAL(KIND=RT), INTENT(IN),    DIMENSION(:,:) :: TARGETS
-    REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: OUTPUTS
-    INTEGER :: D
-    OUTPUTS(:,:) = OUTPUTS(:,:) - TARGETS(:,:)
-  END SUBROUTINE SQUARED_ERROR_GRADIENT
-
-
-  ! Produce the true values as the gradient (which will show large
-  !  magnitudes for parameters in the model that align with values).
-  SUBROUTINE TRUE_VALUE_GRADIENT(TARGETS, OUTPUTS)
-    REAL(KIND=RT), INTENT(IN),    DIMENSION(:,:) :: TARGETS
-    REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: OUTPUTS
-    INTEGER :: D
-    OUTPUTS(:,:) = TARGETS(:,:)
-  END SUBROUTINE TRUE_VALUE_GRADIENT
+  END SUBROUTINE MODEL_GRADIENT
 
 
   ! Fit input / output pairs by minimizing mean squared error.
-  SUBROUTINE MINIMIZE_MSE(CONFIG, MODEL, Y, X, XI, AX, AXI, SIZES, &
-       STEPS, SUM_SQUARED_ERROR, RECORD, INFO)
-    TYPE(MODEL_CONFIG), INTENT(IN) :: CONFIG
+  SUBROUTINE MINIMIZE_MSE(CONFIG, MODEL, RWORK, IWORK, &
+       AX, AXI, SIZES, X, XI, Y, &
+       STEPS, RECORD, SUM_SQUARED_ERROR, INFO)
+    TYPE(MODEL_CONFIG), INTENT(INOUT) :: CONFIG
     REAL(KIND=RT), INTENT(INOUT), DIMENSION(:) :: MODEL
-    REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: Y
-    REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: X
-    INTEGER,       INTENT(IN), DIMENSION(:,:) :: XI
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(:) :: RWORK
+    INTEGER,       INTENT(INOUT), DIMENSION(:) :: IWORK
     REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: AX
-    INTEGER,       INTENT(IN), DIMENSION(:,:) :: AXI
-    INTEGER,       INTENT(IN), DIMENSION(:) :: SIZES
+    INTEGER,       INTENT(IN),    DIMENSION(:,:) :: AXI
+    INTEGER,       INTENT(IN),    DIMENSION(:) :: SIZES
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: X
+    INTEGER,       INTENT(IN),    DIMENSION(:,:) :: XI
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: Y
     INTEGER,       INTENT(IN) :: STEPS
+    REAL(KIND=RT), INTENT(OUT), DIMENSION(6,STEPS), OPTIONAL :: RECORD
     REAL(KIND=RT), INTENT(OUT) :: SUM_SQUARED_ERROR
-    REAL(KIND=RT), INTENT(OUT), DIMENSION(4,STEPS), OPTIONAL :: RECORD
     INTEGER,       INTENT(OUT) :: INFO
-    !  Local variables.
-    !    gradient step arrays, 4 copies of model + (num threads - 1)
-    REAL(KIND=RT), DIMENSION(CONFIG%NUM_VARS) :: &
-         MODEL_GRAD, MODEL_GRAD_MEAN, MODEL_GRAD_CURV, BEST_MODEL
-    REAL(KIND=RT), DIMENSION(CONFIG%MDI-CONFIG%MDE-CONFIG%ADO) :: X_SCALE
-    REAL(KIND=RT), DIMENSION(CONFIG%ADI-CONFIG%ADE) :: AX_SCALE
-    REAL(KIND=RT), DIMENSION(CONFIG%MDO) :: Y_SCALE
-    !    batch start and end indices for parallelization
-    INTEGER, DIMENSION(2,CONFIG%NUM_THREADS) :: BATCHA, BATCHM
+    ! Local variables.
+    !    measured gradient contribution of all input points
+    REAL(KIND=RT), DIMENSION(SIZE(AX,2)) :: AX_CONTRIB
+    REAL(KIND=RT), DIMENSION(SIZE(X,2)) :: X_CONTRIB
+    !    count of how many steps have been taken since last usage
+    INTEGER, DIMENSION(SIZE(AX,2)) :: AX_UNUSED_STEPS
+    INTEGER, DIMENSION(SIZE(X,2)) :: X_UNUSED_STEPS
+    !    indices (used for sorting and selecting points for gradient computation)
+    INTEGER, DIMENSION(SIZE(AX,2)) :: AX_INDICES
+    INTEGER, DIMENSION(SIZE(X,2)) :: X_INDICES
     !    "backspace" character array for printing to the same line repeatedly
     CHARACTER(LEN=*), PARAMETER :: RESET_LINE = REPEAT(CHAR(8),25)
-    !    singletons
-    LOGICAL :: REVERT_TO_BEST, DID_PRINT
-    INTEGER :: BN, I, NB, NS, NY, BATCH, SS, SE
-    INTEGER :: UPDATE_INDICES(CONFIG%NUM_VARS), NUM_TO_UPDATE
-    REAL(KIND=RT) :: RNY, BATCHES, PREV_MSE, MSE, BEST_MSE
-    REAL(KIND=RT) :: STEP_FACTOR, STEP_MEAN_CHANGE, STEP_MEAN_REMAIN, &
-         STEP_CURV_CHANGE, STEP_CURV_REMAIN
-    REAL :: LAST_PRINT_TIME, CURRENT_TIME, WAIT_TIME
-    ! Check for a valid data shape given the model.
-    INFO = 0
-    CALL CHECK_SHAPE(CONFIG, MODEL, Y, X, XI, AX, AXI, SIZES, INFO)
-    IF (INFO .NE. 0) RETURN
-    ! Number of points.
-    NY = SIZE(Y,2)
-    RNY = REAL(NY, RT)
-    ! Set the step factor.
-    STEP_FACTOR = CONFIG%INITIAL_STEP
-    ! Set the initial "number of steps taken since best" counter.
-    NS = 0
-    ! Set the batch N (BN) and num batches (NB).
-    NB = MIN(CONFIG%NUM_THREADS, NY)
-    BN = (NY + NB - 1) / NB
-    CALL COMPUTE_BATCHES(NB, X, AX, SIZES, BATCHA, BATCHM, INFO)
-    IF (INFO .NE. 0) THEN
-       Y(:,:) = 0.0_RT
-       RETURN
-    END IF
-    ! Only "revert" to the best model seen if some steps are taken.
-    REVERT_TO_BEST = CONFIG%KEEP_BEST .AND. (STEPS .GT. 0)
-    ! Store the start time of this routine (to make sure updates can
-    !    be shown to the user at a reasonable frequency).
-    CALL CPU_TIME(LAST_PRINT_TIME)
-    DID_PRINT = .FALSE.
-    WAIT_TIME = 2.0 * NB ! 2 seconds (times number of threads)
-    ! Set the initial number of variables to update at the whole model.
-    NUM_TO_UPDATE = CONFIG%NUM_VARS
-    ! Initial rates of change of mean and variance values.
-    STEP_MEAN_CHANGE = CONFIG%INITIAL_STEP_MEAN_CHANGE
-    STEP_MEAN_REMAIN = 1.0_RT - STEP_MEAN_CHANGE
-    STEP_CURV_CHANGE = CONFIG%INITIAL_STEP_CURV_CHANGE
-    STEP_CURV_REMAIN = 1.0_RT - STEP_CURV_CHANGE
-    ! Initial mean squared error is "max representable value".
-    PREV_MSE = HUGE(PREV_MSE)
-    BEST_MSE = HUGE(BEST_MSE)
-    ! Set the average step sizes.
-    MODEL_GRAD_MEAN(:) = 0.0_RT
-    ! Set the estiamted curvature in steps.
-    MODEL_GRAD_CURV(:) = 0.0_RT
-    ! Set the default size start and end indices for when it is absent.
-    IF (SIZE(SIZES) .EQ. 0) THEN
-       SS = 1
-       SE = -1
-    END IF
-    ! Set shift terms to center all inputs and outputs.
-    MODEL(CONFIG%MISS:CONFIG%MISE) = -SUM(X(:,:),2) / RNY
-    MODEL(CONFIG%AISS:CONFIG%AISE) = -SUM(AX(:,:),2) / RNY
-    MODEL(CONFIG%MOSS:CONFIG%MOSE) =  SUM(Y(:,:),2) / RNY
-    IF (SIZE(X,1) .GT. 0) THEN
-       DO I = 1, SIZE(X,2)
-          X(:,I) = X(:,I) + MODEL(CONFIG%MISS:CONFIG%MISE)
-       END DO
-    END IF
-    IF (SIZE(AX,1) .GT. 0) THEN
-       DO I = 1, SIZE(AX,2)
-          AX(:,I) = AX(:,I) + MODEL(CONFIG%AISS:CONFIG%AISE)
-       END DO
-    END IF
-    DO I = 1, SIZE(Y,2)
-       Y(:,I) = Y(:,I) - MODEL(CONFIG%MOSS:CONFIG%MOSE)
-    END DO
-    ! Make inputs and outputs componentwise unit deviation.
-    !   X
-    X_SCALE(:)  = NORM2(X(:,:),2) / SQRT(RNY)
-    WHERE ( X_SCALE(:) .LT. EPSILON(1.0_RT))  X_SCALE(:) = 1.0_RT
-    IF (SIZE(X,1) .GT. 0) THEN
-       DO I = 1, SIZE(X,2)
-          X(:,I) = X(:,I) / X_SCALE(:)
-       END DO
-    END IF
-    !   AX
-    AX_SCALE(:) = NORM2(AX(:,:),2)
-    IF (SIZE(AX,2) .GT. 0) AX_SCALE(:) = AX_SCALE(:) / SQRT(REAL(SIZE(AX,2),RT))
-    WHERE (AX_SCALE(:) .LT. EPSILON(1.0_RT)) AX_SCALE(:) = 1.0_RT
-    IF (SIZE(AX,1) .GT. 0) THEN
-       DO I = 1, SIZE(AX,2)
-          AX(:,I) = AX(:,I) / AX_SCALE(:)
-       END DO
-    END IF
-    !   Y
-    Y_SCALE(:)  = NORM2(Y(:,:),2) / SQRT(RNY)
-    WHERE ( Y_SCALE(:) .LT. EPSILON(1.0_RT))  Y_SCALE(:) = 1.0_RT
-    DO I = 1, SIZE(Y,2)
-       Y(:,I) = Y(:,I) / Y_SCALE(:)
-    END DO
-    ! Iterate, taking steps with the average gradient over all data.
-    fit_loop : DO I = 1, STEPS
-       ! Compute the average gradient over all points.
-       SUM_SQUARED_ERROR = 0.0_RT
-       ! Set gradients to zero initially.
-       MODEL_GRAD(:) = 0.0_RT
-       !$OMP PARALLEL DO NUM_THREADS(NB) PRIVATE(BATCH) FIRSTPRIVATE(SS, SE) &
-       !$OMP& REDUCTION(+: SUM_SQUARED_ERROR, MODEL_GRAD)
-       DO BATCH = 1, NB
-          ! Set the size start and end.
-          IF (CONFIG%ADI .GT. 0) THEN
-             SS = BATCHM(1,BATCH)
-             SE = BATCHM(2,BATCH)
-          END IF
-          ! Sum the gradient over all data batches.
-          CALL MODEL_GRADIENT(CONFIG, MODEL(:), &
-               Y(:,BATCHM(1,BATCH):BATCHM(2,BATCH)), &
-               X(:,BATCHM(1,BATCH):BATCHM(2,BATCH)), &
-               XI(:,BATCHM(1,BATCH):BATCHM(2,BATCH)), &
-               AX(:,BATCHA(1,BATCH):BATCHA(2,BATCH)), &
-               AXI(:,BATCHA(1,BATCH):BATCHA(2,BATCH)), &
-               SIZES(SS:SE), SUM_SQUARED_ERROR, MODEL_GRAD(:), &
-               SQUARED_ERROR_GRADIENT, INFO, SHIFT=.FALSE., THREADS=1)
-       END DO
-       !$OMP END PARALLEL DO
-       IF (INFO .NE. 0) RETURN
-       ! Convert the sum of squared errors into the mean squared error.
-       MSE = SUM_SQUARED_ERROR / REAL(SIZE(Y),RT) ! RNY * SIZE(Y,1)
-       ! Update the step factor based on model improvement.
-       IF (MSE .LE. PREV_MSE) THEN
-          STEP_FACTOR = STEP_FACTOR * CONFIG%FASTER_RATE
-          STEP_MEAN_CHANGE = STEP_MEAN_CHANGE * CONFIG%SLOWER_RATE
-          STEP_MEAN_REMAIN = 1.0_RT - STEP_MEAN_CHANGE
-          STEP_CURV_CHANGE = STEP_CURV_CHANGE * CONFIG%SLOWER_RATE
-          STEP_CURV_REMAIN = 1.0_RT - STEP_CURV_CHANGE
-          NUM_TO_UPDATE = MIN(CONFIG%NUM_VARS, &
-               NUM_TO_UPDATE + (CONFIG%NUM_VARS - NUM_TO_UPDATE) / 2)
-       ELSE
-          STEP_FACTOR = STEP_FACTOR * CONFIG%SLOWER_RATE
-          STEP_MEAN_CHANGE = STEP_MEAN_CHANGE * CONFIG%FASTER_RATE
-          STEP_MEAN_REMAIN = 1.0_RT - STEP_MEAN_CHANGE
-          STEP_CURV_CHANGE = STEP_CURV_CHANGE * CONFIG%FASTER_RATE
-          STEP_CURV_REMAIN = 1.0_RT - STEP_CURV_CHANGE
-          NUM_TO_UPDATE = MAX(1, NUM_TO_UPDATE / 2)
-       END IF
-       ! Store the previous error for tracking the best-so-far.
-       PREV_MSE = MSE
+    !    temporary holders for overwritten CONFIG attributes
+    LOGICAL :: APPLY_SHIFT
+    INTEGER :: NUM_THREADS
+    !    miscellaneous (hard to concisely categorize)
+    LOGICAL :: DID_PRINT
+    INTEGER :: STEP, BATCH, NB, NS, SS, SE, MIN_TO_UPDATE, D, VS, VE
+    INTEGER :: TOTAL_RANK, TOTAL_EVAL_RANK, TOTAL_GRAD_RANK
+    INTEGER(KIND=INT64) :: CURRENT_TIME, CLOCK_RATE, CLOCK_MAX, LAST_PRINT_TIME, WAIT_TIME
+    REAL(KIND=RT) :: MSE, PREV_MSE, BEST_MSE
+    REAL(KIND=RT) :: STEP_MEAN_REMAIN, STEP_CURV_REMAIN
+
+    ! Unpack all of the work storage into the expected shapes.
+    CALL UNPACKED_MINIZE_MSE(&
+         RWORK(CONFIG%SMG : CONFIG%EMG), & ! MODEL_GRAD(NUM_VARS)
+         RWORK(CONFIG%SMGM : CONFIG%EMGM), & ! MODEL_GRAD_MEAN(NUM_VARS)
+         RWORK(CONFIG%SMGC : CONFIG%EMGC), & ! MODEL_GRAD_CURV(NUM_VARS)
+         RWORK(CONFIG%SBM : CONFIG%EBM), & ! BEST_MODEL(NUM_VARS)
+         RWORK(CONFIG%SMA : CONFIG%EMA), & ! M_ALIGN(MDS,MNS)
+         RWORK(CONFIG%SAA : CONFIG%EAA), & ! A_ALIGN(ADS,ANS)
+         RWORK(CONFIG%SYG : CONFIG%EYG), & ! Y_GRADIENT(MDO,NM)
+         RWORK(CONFIG%SMXS : CONFIG%EMXS), & ! M_STATES(NM,MDS,MNS+1)
+         RWORK(CONFIG%SMXG : CONFIG%EMXG), & ! M_GRADS(NM,MDS,MNS+1)
+         RWORK(CONFIG%SAXS : CONFIG%EAXS), & ! A_STATES(NA,ADS,ANS+1)
+         RWORK(CONFIG%SAXG : CONFIG%EAXG), & ! A_GRADS(NA,ADS,ANS+1)
+         RWORK(CONFIG%SAY : CONFIG%EAY), & ! AY(NA,ADO)
+         RWORK(CONFIG%SAYG : CONFIG%EAYG), & ! AY_GRAD(NA,ADO)
+         RWORK(CONFIG%SMXR : CONFIG%EMXR), & ! X_RESCALE(MDN,MDN)
+         RWORK(CONFIG%SMXIS : CONFIG%EMXIS), & ! XI_SHIFT(MDE)
+         RWORK(CONFIG%SMXIR : CONFIG%EMXIR), & ! XI_RESCALE(MDE,MDE)
+         RWORK(CONFIG%SAXR : CONFIG%EAXR), & ! AX_RESCALE(ADN,ADN)
+         RWORK(CONFIG%SAXIS : CONFIG%EAXIS), & ! AXI_SHIFT(ADE)
+         RWORK(CONFIG%SAXIR : CONFIG%EAXIR), & ! AXI_RESCALE(ADE,ADE)
+         RWORK(CONFIG%SAYR : CONFIG%EAYR), & ! AY_RESCALE(ADO)
+         RWORK(CONFIG%SYR : CONFIG%EYR), & ! Y_RESCALE(MDO,MDO)
+         RWORK(CONFIG%SFMA : CONFIG%EFMA), & ! MODEL_ALIGN(NUM_VARS,NUM_THREADS)
+         RWORK(CONFIG%SXT : CONFIG%EXT), & ! X_TEMP(MDE+ADO,NM,NUM_THREADS)
+         MODEL(CONFIG%ASIV : CONFIG%AEIV), & ! APOSITIONAL_INPUT_VECS
+         MODEL(CONFIG%MSIV : CONFIG%MEIV), & ! MODEL_INPUT_VECS
+         MODEL(CONFIG%ASOV : CONFIG%AEOV), & ! APOSITIONAL_OUTPUT_VECS
+         MODEL(CONFIG%MSOV : CONFIG%MEOV), & ! APOSITIONAL_OUTPUT_VECS
+         IWORK(CONFIG%SUI : CONFIG%EUI), & ! UPDATE_INDICES(NUM_VARS)
+         IWORK(CONFIG%SBAS : CONFIG%EBAS), & ! BATCHA_STARTS(NUM_THREADS)
+         IWORK(CONFIG%SBAE : CONFIG%EBAE), & ! BATCHA_ENDS(NUM_THREADS)
+         IWORK(CONFIG%SBMS : CONFIG%EBMS), & ! BATCHM_STARTS(NUM_THREADS)
+         IWORK(CONFIG%SBME : CONFIG%EBME)) ! BATCHM_ENDS(NUM_THREADS)
 
-       ! Record that a step was taken.
-       NS = NS + 1
-       ! Update the saved "best" model based on error.
-       IF (MSE .LT. BEST_MSE) THEN
-          NS = 0
-          BEST_MSE = MSE
-          IF (REVERT_TO_BEST) THEN
-             BEST_MODEL(:) = MODEL(1:CONFIG%NUM_VARS)
-          END IF
-       ! Early stop if we don't expect to see a better solution
-       !  by the time the fit operation is complete.
-       ELSE IF (CONFIG%EARLY_STOP .AND. (NS .GT. STEPS - I)) THEN
-          EXIT fit_loop
-       END IF
+  CONTAINS
 
-       ! Convert the summed gradients to average gradients.
-       MODEL_GRAD(:) = MODEL_GRAD(:) / REAL(NB,RT)
-       MODEL_GRAD_MEAN(:) = STEP_MEAN_REMAIN * MODEL_GRAD_MEAN(:) &
-            + STEP_MEAN_CHANGE * MODEL_GRAD(:)
-       MODEL_GRAD_CURV(:) = STEP_CURV_REMAIN * MODEL_GRAD_CURV(:) &
-            + STEP_CURV_CHANGE * (MODEL_GRAD_MEAN(:) - MODEL_GRAD(:))**2
-       MODEL_GRAD_CURV(:) = MAX(MODEL_GRAD_CURV(:), EPSILON(STEP_FACTOR))
-       ! Set the step as the mean direction (over the past few steps).
-       MODEL_GRAD(:) = MODEL_GRAD_MEAN(:)
-       ! Start scaling by step magnitude by curvature once enough data is collected.
-       IF (I .GE. CONFIG%MIN_STEPS_TO_STABILITY) THEN
-          MODEL_GRAD(:) = MODEL_GRAD(:) / SQRT(MODEL_GRAD_CURV(:))
-       END IF
-       ! Update as many parameters as it seems safe to update (and still converge).
-       IF (NUM_TO_UPDATE .LT. CONFIG%NUM_VARS) THEN
-          ! Identify the subset of components that will be updapted this step.
-          CALL ARGSELECT(-ABS(MODEL_GRAD(:)), NUM_TO_UPDATE, UPDATE_INDICES(:))
-          ! Take the gradient steps (based on the computed "step" above).
-          MODEL(UPDATE_INDICES(1:NUM_TO_UPDATE)) = MODEL(UPDATE_INDICES(1:NUM_TO_UPDATE)) &
-               - MODEL_GRAD(UPDATE_INDICES(1:NUM_TO_UPDATE)) * STEP_FACTOR
-       ELSE
-          ! Take the gradient steps (based on the computed "step" above).
-          MODEL(1:CONFIG%NUM_VARS) = MODEL(1:CONFIG%NUM_VARS) - MODEL_GRAD(:) * STEP_FACTOR
-       END IF
+    ! Unpack the work arrays into the proper shapes.
+    SUBROUTINE UNPACKED_MINIZE_MSE(&
+         MODEL_GRAD, MODEL_GRAD_MEAN, MODEL_GRAD_CURV, BEST_MODEL, &
+         M_ALIGN, A_ALIGN, Y_GRADIENT, M_STATES, M_GRADS, A_STATES, A_GRADS, &
+         AY, AY_GRAD, X_RESCALE, XI_SHIFT, XI_RESCALE, &
+         AX_RESCALE, AXI_SHIFT, AXI_RESCALE, AY_RESCALE, &
+         Y_RESCALE, MODEL_ALIGN, X_TEMP, &
+         A_IN_VECS, M_IN_VECS, A_OUT_VECS, M_OUT_VECS, &
+         UPDATE_INDICES, BATCHA_STARTS, BATCHA_ENDS, BATCHM_STARTS, BATCHM_ENDS)
+      ! Definition of unpacked work storage.
+      REAL(KIND=RT), DIMENSION(CONFIG%NUM_VARS) :: &
+           MODEL_GRAD, MODEL_GRAD_MEAN, MODEL_GRAD_CURV, BEST_MODEL
+      REAL(KIND=RT), DIMENSION(CONFIG%NA, CONFIG%ADS, CONFIG%ANS+1) :: A_STATES, A_GRADS
+      REAL(KIND=RT), DIMENSION(CONFIG%NM, CONFIG%MDS, CONFIG%MNS+1) :: M_STATES, M_GRADS
+      REAL(KIND=RT), DIMENSION(CONFIG%ADS, CONFIG%ANS) :: A_ALIGN
+      REAL(KIND=RT), DIMENSION(CONFIG%NA, CONFIG%ADO) :: AY, AY_GRAD
+      REAL(KIND=RT), DIMENSION(CONFIG%MDS, CONFIG%MNS) :: M_ALIGN
+      REAL(KIND=RT), DIMENSION(CONFIG%MDO, CONFIG%NM) :: Y_GRADIENT
+      REAL(KIND=RT), DIMENSION(CONFIG%ADN, CONFIG%ADN) :: AX_RESCALE
+      REAL(KIND=RT), DIMENSION(CONFIG%ADE) :: AXI_SHIFT
+      REAL(KIND=RT), DIMENSION(CONFIG%ADE, CONFIG%ADE) :: AXI_RESCALE
+      REAL(KIND=RT), DIMENSION(CONFIG%ADO) :: AY_RESCALE
+      REAL(KIND=RT), DIMENSION(CONFIG%MDN, CONFIG%MDN) :: X_RESCALE
+      REAL(KIND=RT), DIMENSION(CONFIG%MDE) :: XI_SHIFT
+      REAL(KIND=RT), DIMENSION(CONFIG%MDE, CONFIG%MDE) :: XI_RESCALE
+      REAL(KIND=RT), DIMENSION(CONFIG%MDO, CONFIG%MDO) :: Y_RESCALE
+      REAL(KIND=RT), DIMENSION(CONFIG%NUM_VARS, CONFIG%NUM_THREADS) :: MODEL_ALIGN
+      REAL(KIND=RT), DIMENSION(CONFIG%MDE+CONFIG%ADO, CONFIG%NM, CONFIG%NUM_THREADS) :: X_TEMP
+      REAL(KIND=RT), DIMENSION(CONFIG%ADI, CONFIG%ADS) :: A_IN_VECS
+      REAL(KIND=RT), DIMENSION(CONFIG%MDI, CONFIG%MDS) :: M_IN_VECS
+      REAL(KIND=RT), DIMENSION(CONFIG%ADS, CONFIG%ADO) :: A_OUT_VECS
+      REAL(KIND=RT), DIMENSION(CONFIG%MDS, CONFIG%MDO) :: M_OUT_VECS
+      INTEGER, DIMENSION(CONFIG%NUM_VARS) :: UPDATE_INDICES
+      INTEGER, DIMENSION(CONFIG%NUM_THREADS) :: &
+           BATCHA_STARTS, BATCHA_ENDS, BATCHM_STARTS, BATCHM_ENDS
+      ! Check for a valid data shape given the model.
+      INFO = 0
+      ! Check the shape of all inputs (to make sure they match this model).
+      CALL CHECK_SHAPE(CONFIG, MODEL, AX, AXI, SIZES, X, XI, Y, INFO)
+      ! Do shape checks on the work space provided.
+      IF (SIZE(RWORK) .LT. CONFIG%RWORK_SIZE) THEN
+         INFO = 12
+      ELSE IF (SIZE(IWORK) .LT. CONFIG%IWORK_SIZE) THEN
+         INFO = 13
+      ELSE IF ((CONFIG%ADI .GT. 0) .AND. (CONFIG%NA .LT. 1)) THEN
+         INFO = 14
+      ELSE IF ((CONFIG%MDI .GT. 0) .AND. (CONFIG%NM .LT. 1)) THEN
+         INFO = 15
+      END IF
+      IF (INFO .NE. 0) RETURN
+      ! 
+      ! ----------------------------------------------------------------
+      !                 Initialization and preparation
+      ! 
+      ! Set the "total rank", the number of internal state components.
+      TOTAL_RANK = CONFIG%MDS*CONFIG%MNS + CONFIG%ADS*CONFIG%ANS
+      ! Compute the minimum number of model parameters to update.
+      MIN_TO_UPDATE = MAX(1,INT(CONFIG%MIN_UPDATE_RATIO * REAL(CONFIG%NUM_VARS,RT)))
+      ! Set the initial "number of steps taken since best" counter.
+      NS = 0
+      ! Set the num batches (NB).
+      NB = MIN(CONFIG%NUM_THREADS, SIZE(Y,2))
+      CALL COMPUTE_BATCHES(NB, SIZE(X,2), SIZE(AX,2), SIZES, &
+           BATCHA_STARTS, BATCHA_ENDS, BATCHM_STARTS, BATCHM_ENDS, INFO)
+      IF (INFO .NE. 0) THEN
+         Y(:,:) = 0.0_RT
+         RETURN
+      END IF
+      ! Store the start time of this routine (to make sure updates can
+      !  be shown to the user at a reasonable frequency).
+      CALL SYSTEM_CLOCK(LAST_PRINT_TIME, CLOCK_RATE, CLOCK_MAX)
+      WAIT_TIME = CLOCK_RATE * CONFIG%PRINT_DELAY_SEC
+      DID_PRINT = .FALSE.
+      ! Initial rates of change of mean and variance values.
+      STEP_MEAN_REMAIN = 1.0_RT - CONFIG%STEP_MEAN_CHANGE
+      STEP_CURV_REMAIN = 1.0_RT - CONFIG%STEP_CURV_CHANGE
+      ! Initial mean squared error is "max representable value".
+      PREV_MSE = HUGE(PREV_MSE)
+      BEST_MSE = HUGE(BEST_MSE)
+      ! Set the default size start and end indices for when it is absent.
+      IF (SIZE(SIZES) .EQ. 0) THEN
+         SS = 1
+         SE = -1
+      END IF
+      ! Disable the application of SHIFT (since data is / will be normalized).
+      APPLY_SHIFT = CONFIG%APPLY_SHIFT
+      CONFIG%APPLY_SHIFT = .FALSE.
+      ! Normalize the data.
+      CALL NORMALIZE_DATA(CONFIG, MODEL, AX, AXI, AY, SIZES, X, XI, Y, &
+           AX_RESCALE, AXI_SHIFT, AXI_RESCALE, AY_RESCALE, X_RESCALE, &
+           XI_SHIFT, XI_RESCALE, Y_RESCALE, A_STATES, &
+           MODEL(CONFIG%MSEV:CONFIG%MEEV), &
+           MODEL(CONFIG%ASEV:CONFIG%AEEV), &
+           MODEL(CONFIG%ASOV:CONFIG%AEOV))
+      ! Set the number of threads to 1 to prevent nested parallelization.
+      NUM_THREADS = CONFIG%NUM_THREADS
+      CONFIG%NUM_THREADS = 1
+      ! 
+      ! ----------------------------------------------------------------
+      !                    Minimizing mean squared error
+      ! 
+      ! Iterate, taking steps with the average gradient over all data.
+      fit_loop : DO STEP = 1, STEPS
+         ! 
+         ! - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
+         !                       Compute model gradient 
+         ! 
+         ! Compute the average gradient over all points.
+         SUM_SQUARED_ERROR = 0.0_RT
+         ! Set gradients to zero initially.
+         MODEL_GRAD(:) = 0.0_RT
+         M_ALIGN(:,:) = 0.0_RT
+         A_ALIGN(:,:) = 0.0_RT
+         !$OMP PARALLEL DO NUM_THREADS(NB) PRIVATE(BATCH) FIRSTPRIVATE(SS, SE) &
+         !$OMP& REDUCTION(+: SUM_SQUARED_ERROR, MODEL_GRAD, M_ALIGN, A_ALIGN)
+         DO BATCH = 1, NB
+            ! Set the size start and end.
+            IF (CONFIG%ADI .GT. 0) THEN
+               SS = BATCHM_STARTS(BATCH)
+               SE = BATCHM_ENDS(BATCH)
+            END IF
+            ! Sum the gradient over all data batches.
+            CALL MODEL_GRADIENT(CONFIG, MODEL(:), &
+                 AX(:,BATCHA_STARTS(BATCH):BATCHA_ENDS(BATCH)), &
+                 AXI(:,BATCHA_STARTS(BATCH):BATCHA_ENDS(BATCH)), &
+                 AY(BATCHA_STARTS(BATCH):BATCHA_ENDS(BATCH),:), &
+                 SIZES(SS:SE), &
+                 X(:,BATCHM_STARTS(BATCH):BATCHM_ENDS(BATCH)), &
+                 XI(:,BATCHM_STARTS(BATCH):BATCHM_ENDS(BATCH)), &
+                 Y(:,BATCHM_STARTS(BATCH):BATCHM_ENDS(BATCH)), &
+                 SUM_SQUARED_ERROR, MODEL_GRAD(:), &
+                 A_ALIGN(:,:), M_ALIGN(:,:), &
+                 MODEL_ALIGN(:,BATCH), &
+                 X_TEMP(:,:,BATCH), &
+                 AY_GRAD(BATCHA_STARTS(BATCH):BATCHA_ENDS(BATCH),:), &
+                 Y_GRADIENT(:,BATCHM_STARTS(BATCH):BATCHM_ENDS(BATCH)), &
+                 A_STATES(BATCHA_STARTS(BATCH):BATCHA_ENDS(BATCH),:,:), &
+                 A_GRADS(BATCHA_STARTS(BATCH):BATCHA_ENDS(BATCH),:,:), &
+                 M_STATES(BATCHM_STARTS(BATCH):BATCHM_ENDS(BATCH),:,:), &
+                 M_GRADS(BATCHM_STARTS(BATCH):BATCHM_ENDS(BATCH),:,:), &
+                 INFO)
+         END DO
+         !$OMP END PARALLEL DO
+         IF (INFO .NE. 0) RETURN
+         ! 
+         ! - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
+         !           Update the step factors, early stop if appropaite.
+         ! 
+         ! Convert the sum of squared errors into the mean squared error.
+         MSE = SUM_SQUARED_ERROR / REAL(SIZE(Y),RT) ! RNY * SIZE(Y,1)
+         ! Adjust exponential sliding windows based on change in error.
+         IF (MSE .LE. PREV_MSE) THEN
+            CONFIG%STEP_FACTOR = CONFIG%STEP_FACTOR * CONFIG%FASTER_RATE
+            CONFIG%STEP_MEAN_CHANGE = CONFIG%STEP_MEAN_CHANGE * CONFIG%SLOWER_RATE
+            STEP_MEAN_REMAIN = 1.0_RT - CONFIG%STEP_MEAN_CHANGE
+            CONFIG%STEP_CURV_CHANGE = CONFIG%STEP_CURV_CHANGE * CONFIG%SLOWER_RATE
+            STEP_CURV_REMAIN = 1.0_RT - CONFIG%STEP_CURV_CHANGE
+            CONFIG%NUM_TO_UPDATE = CONFIG%NUM_TO_UPDATE + INT(0.05_RT * REAL(CONFIG%NUM_VARS,RT))
+         ELSE
+            CONFIG%STEP_FACTOR = CONFIG%STEP_FACTOR * CONFIG%SLOWER_RATE
+            CONFIG%STEP_MEAN_CHANGE = CONFIG%STEP_MEAN_CHANGE * CONFIG%FASTER_RATE
+            STEP_MEAN_REMAIN = 1.0_RT - CONFIG%STEP_MEAN_CHANGE
+            CONFIG%STEP_CURV_CHANGE = CONFIG%STEP_CURV_CHANGE * CONFIG%FASTER_RATE
+            STEP_CURV_REMAIN = 1.0_RT - CONFIG%STEP_CURV_CHANGE
+            CONFIG%NUM_TO_UPDATE = CONFIG%NUM_TO_UPDATE - INT(0.05_RT * REAL(CONFIG%NUM_VARS,RT))
+         END IF
+         ! Project the number of variables to update into allowable bounds.
+         CONFIG%NUM_TO_UPDATE = MIN(CONFIG%NUM_VARS, MAX(MIN_TO_UPDATE, CONFIG%NUM_TO_UPDATE))
+         ! Store the previous error for tracking the best-so-far.
+         PREV_MSE = MSE
+         ! Record that a step was taken.
+         NS = NS + 1
+         ! Update the saved "best" model based on error.
+         IF (MSE .LT. BEST_MSE) THEN
+            NS = 0
+            BEST_MSE = MSE
+            IF (CONFIG%KEEP_BEST) THEN
+               BEST_MODEL(:) = MODEL(1:CONFIG%NUM_VARS)
+            END IF
+            ! Early stop if we don't expect to see a better solution
+            !  by the time the fit operation is complete.
+         ELSE IF (CONFIG%EARLY_STOP .AND. (NS .GT. STEPS - STEP)) THEN
+            EXIT fit_loop
+         END IF
 
-       ! Record the 2-norm of the step that was taken (the GRAD variables were updated).
-       IF (PRESENT(RECORD)) THEN
-          ! Store the mean squared error at this iteration.
-          RECORD(1,I) = MSE
-          ! Store the current multiplier on the step.
-          RECORD(2,I) = STEP_FACTOR
-          ! Store the norm of the step that was taken.
-          RECORD(3,I) = SQRT(MAX(EPSILON(0.0_RT), SUM(MODEL_GRAD(:)**2)))
-          ! Store the percentage of parameters updated in this step.
-          RECORD(4,I) = REAL(NUM_TO_UPDATE,RT) / REAL(CONFIG%NUM_VARS)
-       END IF
+         ! - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
+         !              Modify the model parameters (take step).
+         ! 
+         ! Convert the summed gradients to average gradients.
+         MODEL_GRAD(:) = MODEL_GRAD(:) / REAL(NB,RT)
+         MODEL_GRAD_MEAN(:) = STEP_MEAN_REMAIN * MODEL_GRAD_MEAN(:) &
+              + CONFIG%STEP_MEAN_CHANGE * MODEL_GRAD(:)
+         MODEL_GRAD_CURV(:) = STEP_CURV_REMAIN * MODEL_GRAD_CURV(:) &
+              + CONFIG%STEP_CURV_CHANGE * (MODEL_GRAD_MEAN(:) - MODEL_GRAD(:))**2
+         MODEL_GRAD_CURV(:) = MAX(MODEL_GRAD_CURV(:), EPSILON(CONFIG%STEP_FACTOR))
+         ! Set the step as the mean direction (over the past few steps).
+         MODEL_GRAD(:) = MODEL_GRAD_MEAN(:)
+         ! Start scaling by step magnitude by curvature once enough data is collected.
+         IF (STEP .GE. CONFIG%MIN_STEPS_TO_STABILITY) THEN
+            MODEL_GRAD(:) = MODEL_GRAD(:) / SQRT(MODEL_GRAD_CURV(:))
+         END IF
+         ! Update as many parameters as it seems safe to update (and still converge).
+         IF (CONFIG%NUM_TO_UPDATE .LT. CONFIG%NUM_VARS) THEN
+            ! Identify the subset of components that will be updapted this step.
+            CALL ARGSELECT(-ABS(MODEL_GRAD(:)), &
+                 CONFIG%NUM_TO_UPDATE, UPDATE_INDICES(:))
+            ! Take the gradient steps (based on the computed "step" above).
+            MODEL(UPDATE_INDICES(1:CONFIG%NUM_TO_UPDATE)) = &
+                 MODEL(UPDATE_INDICES(1:CONFIG%NUM_TO_UPDATE)) &
+                 - MODEL_GRAD(UPDATE_INDICES(1:CONFIG%NUM_TO_UPDATE)) &
+                 * CONFIG%STEP_FACTOR
+         ELSE
+            ! Take the gradient steps (based on the computed "step" above).
+            MODEL(1:CONFIG%NUM_VARS) = MODEL(1:CONFIG%NUM_VARS) &
+                 - MODEL_GRAD(:) * CONFIG%STEP_FACTOR
+         END IF
+         CONFIG%STEPS_TAKEN = CONFIG%STEPS_TAKEN + 1
+         ! - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
+         ! Rescale internal vectors to have a maximum 2-norm of 1.
+         ! Center the outputs of the apositional model about the origin.
+         ! (for I = 1, rescale last layer of apositional model to unit variance)
+         CALL CONDITION_MODEL(CONFIG, CONFIG%STEPS_TAKEN, &
+              M_STATES(:,:,:), A_STATES(:,:,:), M_GRADS(:,:,:), A_GRADS(:,:,:), &
+              AY(:,:))
+         ! - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
+         ! Record various statistics that are currently of interest (for research).
+         IF (PRESENT(RECORD)) THEN
+            ! Store the mean squared error at this iteration.
+            RECORD(1,STEP) = MSE
+            ! Store the current multiplier on the step.
+            RECORD(2,STEP) = CONFIG%STEP_FACTOR
+            ! Store the norm of the step that was taken (intermittently).
+            IF (MOD(CONFIG%STEPS_TAKEN-1,CONFIG%LOGGING_STEP_FREQUENCY) .EQ. 0) THEN
+               RECORD(3,STEP) = SQRT(MAX(EPSILON(0.0_RT), SUM(MODEL_GRAD(:)**2))) / SQRT(REAL(CONFIG%NUM_VARS,RT))
+            ELSE
+               RECORD(3,STEP) = RECORD(3,STEP-1)
+            END IF
+            ! Store the percentage of parameters updated in this step.
+            RECORD(4,STEP) = REAL(CONFIG%NUM_TO_UPDATE,RT) / REAL(CONFIG%NUM_VARS)
+            ! Store the evaluative utilization rate (total data rank over full rank)
+            RECORD(5,STEP) = REAL(TOTAL_EVAL_RANK,RT) / REAL(TOTAL_RANK,RT)
+            ! Store the gradient utilization rate (total gradient rank over full rank)
+            RECORD(6,STEP) = REAL(TOTAL_GRAD_RANK,RT) / REAL(CONFIG%MDS*CONFIG%MNS + CONFIG%ADS*CONFIG%ANS,RT)
+         END IF
+         ! - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
+         ! Write an update about step and convergence to the command line.
+         CALL SYSTEM_CLOCK(CURRENT_TIME, CLOCK_RATE, CLOCK_MAX)
+         IF (CURRENT_TIME - LAST_PRINT_TIME .GT. WAIT_TIME) THEN
+            IF (DID_PRINT) WRITE (*,'(A)',ADVANCE='NO') RESET_LINE
+            WRITE (*,'(I6,"  (",F6.3,") [",F6.3,"]")', ADVANCE='NO') STEP, MSE, BEST_MSE
+            LAST_PRINT_TIME = CURRENT_TIME
+            DID_PRINT = .TRUE.
+         END IF
+      END DO fit_loop
+      ! 
+      ! ----------------------------------------------------------------
+      !                 Finalization, prepare for return.
+      ! 
+      ! Restore the best model seen so far (if enough steps were taken).
+      IF (CONFIG%KEEP_BEST .AND. (STEPS .GT. 0)) THEN
+         MSE                      = BEST_MSE
+         MODEL(1:CONFIG%NUM_VARS) = BEST_MODEL(:)
+      END IF
+      ! 
+      ! Apply the data normalizing scaling factors to the weight
+      !  matrices to embed normalization into the model.
+      IF (CONFIG%ENCODE_NORMALIZATION) THEN
+         IF (CONFIG%ADN .GT. 0) &
+              CALL SCALE_BASIS(A_IN_VECS(:CONFIG%ADN,:), AX_RESCALE(:,:))
+         IF (CONFIG%MDN .GT. 0) &
+              CALL SCALE_BASIS(M_IN_VECS(:CONFIG%MDN,:), X_RESCALE(:,:))
+         CALL SCALE_BASIS(M_OUT_VECS(:,:), Y_RESCALE(:,:))
+      END IF
+      ! 
+      ! Erase the printed message if one was produced.
+      IF (DID_PRINT) WRITE (*,'(A)',ADVANCE='NO') RESET_LINE
+      ! 
+      ! Reset configuration settings that were modified.
+      CONFIG%APPLY_SHIFT = APPLY_SHIFT
+      CONFIG%NUM_THREADS = NUM_THREADS
+    END SUBROUTINE UNPACKED_MINIZE_MSE
 
-       ! TODO: Replace with a more general "condition_model" routine that takes
-       !       the values and gradients for a model, then updates and replaces
-       !       bad basis functions, as well as normalizing them all.
-       !       Must orthogonalize outputs of basis functions when ranking,
-       !       ensure that highly redundant functions are removed in favor
-       !       of single (more information-unique) basis functions.
-       !       Use the expected decrease in loss (gradient * step) to
-       !       determine when a replacement can be made.
-       ! 
-       ! Maintain a constant max-norm across the magnitue of input and internal vectors.
-       CALL UNIT_MAX_NORM(CONFIG%MDI, CONFIG%MDS, CONFIG%MNS, &
-            MODEL(CONFIG%MSIV:CONFIG%MEIV), &
-            MODEL(CONFIG%MSSV:CONFIG%MESV))
-       IF (CONFIG%ADI .GT. 0) THEN
-          CALL UNIT_MAX_NORM(CONFIG%ADI, CONFIG%ADS, CONFIG%ANS, &
-               MODEL(CONFIG%ASIV:CONFIG%AEIV), &
-               MODEL(CONFIG%ASSV:CONFIG%AESV))
-       END IF
 
-       ! Write an update about step and convergence to the command line.
-       CALL CPU_TIME(CURRENT_TIME)
-       IF (CURRENT_TIME - LAST_PRINT_TIME .GT. WAIT_TIME) THEN
-          IF (DID_PRINT) WRITE (*,'(A)',ADVANCE='NO') RESET_LINE
-          WRITE (*,'(I6,"  (",F6.3,") [",F6.3,"]")', ADVANCE='NO') I, MSE, BEST_MSE
-          LAST_PRINT_TIME = CURRENT_TIME
-          DID_PRINT = .TRUE.
-       END IF
+    ! Make inputs and outputs radially symmetric (to make initialization
+    !  more well spaced and lower the curvature of the error gradient).
+    ! 
+    SUBROUTINE NORMALIZE_DATA(CONFIG, MODEL, AX, AXI, AY, SIZES, X, XI, Y, &
+         AX_RESCALE, AXI_SHIFT, AXI_RESCALE, AY_RESCALE, X_RESCALE, &
+         XI_SHIFT, XI_RESCALE, Y_RESCALE, &
+         A_STATES, A_EMB_VECS, M_EMB_VECS, A_OUT_VECS)
+      TYPE(MODEL_CONFIG), INTENT(INOUT) :: CONFIG
+      REAL(KIND=RT), INTENT(INOUT), DIMENSION(:) :: MODEL
+      REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: AX
+      INTEGER,       INTENT(IN),    DIMENSION(:,:) :: AXI
+      REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: AY
+      INTEGER,       INTENT(IN),    DIMENSION(:) :: SIZES
+      REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: X
+      INTEGER,       INTENT(IN),    DIMENSION(:,:) :: XI
+      REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: Y
+      REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: AX_RESCALE
+      REAL(KIND=RT), INTENT(INOUT), DIMENSION(:) :: AXI_SHIFT
+      REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: AXI_RESCALE
+      REAL(KIND=RT), INTENT(INOUT), DIMENSION(:) :: AY_RESCALE
+      REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: X_RESCALE
+      REAL(KIND=RT), INTENT(INOUT), DIMENSION(:) :: XI_SHIFT
+      REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: XI_RESCALE
+      REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: Y_RESCALE
+      REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:,:) :: A_STATES
+      REAL(KIND=RT), INTENT(INOUT), DIMENSION(CONFIG%ADE,CONFIG%ADE) :: A_EMB_VECS
+      REAL(KIND=RT), INTENT(INOUT), DIMENSION(CONFIG%MDE,CONFIG%MNE) :: M_EMB_VECS
+      REAL(KIND=RT), INTENT(INOUT), DIMENSION(CONFIG%ADS,CONFIG%ADO) :: A_OUT_VECS
+      INTEGER :: D
+      ! Encode embeddings if the are provided.
+      IF ((CONFIG%MDE + CONFIG%ADE .GT. 0) .AND. (&
+           (.NOT. CONFIG%XI_NORMALIZED) .OR. (.NOT. CONFIG%AXI_NORMALIZED))) THEN
+         CALL EMBED(CONFIG, MODEL, AXI, XI, AX, X)
+      END IF
+      ! 
+      !$OMP PARALLEL NUM_THREADS(5)
+      !$OMP SECTIONS PRIVATE(D)
+      !$OMP SECTION
+      IF ((.NOT. CONFIG%X_NORMALIZED) .AND. (CONFIG%MDN .GT. 0)) THEN
+         CALL RADIALIZE(X(:CONFIG%MDN,:), MODEL(CONFIG%MISS:CONFIG%MISE), X_RESCALE(:,:))
+         CONFIG%X_NORMALIZED = .TRUE.
+      ELSE IF (CONFIG%MDN .GT. 0) THEN
+         MODEL(CONFIG%MISS:CONFIG%MISE) = 0.0_RT
+         X_RESCALE(:,:) = 0.0_RT
+         FORALL (D=1:CONFIG%MDN) X_RESCALE(D,D) = 1.0_RT
+      END IF
+      !$OMP SECTION
+      IF ((.NOT. CONFIG%XI_NORMALIZED) .AND. (CONFIG%MDE .GT. 0)) THEN
+         CALL RADIALIZE(X(CONFIG%MDN+1:CONFIG%MDN+CONFIG%MDE,:), &
+              XI_SHIFT(:), XI_RESCALE(:,:))
+         ! Apply the shift to the source embeddings.
+         DO D = 1, CONFIG%MDE
+            M_EMB_VECS(D,:) = M_EMB_VECS(D,:) + XI_SHIFT(D)
+         END DO
+         ! Apply the transformation to the source embeddings.
+         M_EMB_VECS(:,:) = MATMUL(TRANSPOSE(XI_RESCALE(:,:)), M_EMB_VECS(:,:))
+         CONFIG%XI_NORMALIZED = .TRUE.
+      END IF
+      !$OMP SECTION
+      IF ((.NOT. CONFIG%AX_NORMALIZED) .AND. (CONFIG%ADN .GT. 0)) THEN
+         CALL RADIALIZE(AX(:CONFIG%ADN,:), &
+              MODEL(CONFIG%AISS:CONFIG%AISE), AX_RESCALE(:,:))
+         CONFIG%AX_NORMALIZED = .TRUE.
+      ELSE IF (CONFIG%ADN .GT. 0) THEN
+         MODEL(CONFIG%AISS:CONFIG%AISE) = 0.0_RT
+         AX_RESCALE(:,:) = 0.0_RT
+         FORALL (D=1:CONFIG%ADN) AX_RESCALE(D,D) = 1.0_RT
+      END IF
+      !$OMP SECTION
+      IF ((.NOT. CONFIG%AXI_NORMALIZED) .AND. (CONFIG%ADE .GT. 0)) THEN
+         CALL RADIALIZE(AX(CONFIG%ADN+1:CONFIG%ADN+CONFIG%ADE,:), &
+              XI_SHIFT(:), XI_RESCALE(:,:))
+         ! Apply the shift to the source embeddings.
+         DO D = 1, CONFIG%ADE
+            A_EMB_VECS(D,:) = A_EMB_VECS(D,:) + XI_SHIFT(D)
+         END DO
+         ! Apply the transformation to the source embeddings.
+         A_EMB_VECS(:,:) = MATMUL(TRANSPOSE(XI_RESCALE(:,:)), A_EMB_VECS(:,:))
+         CONFIG%AXI_NORMALIZED = .TRUE.
+      END IF
+      !$OMP SECTION
+      IF (.NOT. CONFIG%Y_NORMALIZED) THEN
+         CALL RADIALIZE(Y(:,:), MODEL(CONFIG%MOSS:CONFIG%MOSE), &
+              Y_RESCALE(:,:), INVERT_RESULT=.TRUE.)
+         CONFIG%Y_NORMALIZED = .TRUE.
+      ELSE
+         MODEL(CONFIG%MOSS:CONFIG%MOSE) = 0.0_RT
+         Y_RESCALE(:,:) = 0.0_RT
+         FORALL (D=1:CONFIG%MDO) Y_RESCALE(D,D) = 1.0_RT
+      END IF
+      !$OMP END SECTIONS
+      !$OMP END PARALLEL
+      ! 
+      ! Normalize AY outside the parallel region (AX must be normalized).
+      IF ((.NOT. CONFIG%AY_NORMALIZED) .AND. (CONFIG%ADO .GT. 0)) THEN
+         ! Disable "model" evaluation for this forward pass.
+         !   (Reuse "A_STATES" for the "M_STATES" argument, since it will be unused.)
+         D = CONFIG%MDI ; CONFIG%MDI = 0
+         CALL EVALUATE(CONFIG, MODEL, AX, AY, SIZES, X, Y, A_STATES, A_STATES, INFO)
+         CONFIG%MDI = D
+         ! Compute AY shift as the mean, apply it.
+         MODEL(CONFIG%AOSS:CONFIG%AOSE) = -SUM(AY(:,:),1) / REAL(SIZE(AY,1),RT)
+         DO D = 1, CONFIG%ADO
+            AY(:,D) = AY(:,D) + MODEL(CONFIG%AOSS + D-1)
+         END DO
+         ! Compute the AY scale as the standard deviation.
+         AY(1,:) = SUM(AY(:,:)**2,1)
+         WHERE (AY(1,:) .GT. 0.0_RT)
+            AY(1,:) = SQRT(AY(1,:))
+         ELSEWHERE
+            AY(1,:) = 1.0_RT
+         END WHERE
+         ! Apply the factor to the output vectors.
+         DO D = 1, CONFIG%ADO
+            A_OUT_VECS(:,D) = A_OUT_VECS(:,D) / AY(1,D)
+         END DO
+         CONFIG%AY_NORMALIZED = .TRUE.
+      END IF
+    END SUBROUTINE NORMALIZE_DATA
 
-    END DO fit_loop
 
-    ! Restore the best model seen so far (if enough steps were taken).
-    IF (REVERT_TO_BEST) THEN
-       MSE                      = BEST_MSE
-       MODEL(1:CONFIG%NUM_VARS) = BEST_MODEL(:)
-    END IF
-
-    ! Apply the data normalizing scaling factors to the weight matrices.
-    IF (SIZE(X,1) .GT. 0) &
-         CALL SCALE_BASIS(CONFIG%MDI, CONFIG%MDS, &
-         MODEL(CONFIG%MSIV:CONFIG%MEIV), 1.0_RT / X_SCALE(:))
-    IF (SIZE(AX,1) .GT. 0) &
-         CALL SCALE_BASIS(CONFIG%ADI, CONFIG%ADS, &
-         MODEL(CONFIG%ASIV:CONFIG%AEIV), 1.0_RT / AX_SCALE(:))
-    CALL SCALE_BASIS(CONFIG%MDS, CONFIG%MDO, &
-         MODEL(CONFIG%MSOV:CONFIG%MEOV), Y_SCALE(:), TRANS=.TRUE.)
+    ! Performing conditioning related operations on this model 
+    !  (ensure that mean squared error is effectively reduced).
+    SUBROUTINE CONDITION_MODEL(CONFIG, FIT_STEP, M_STATES, A_STATES, M_GRADS, A_GRADS, AY)
+      TYPE(MODEL_CONFIG), INTENT(IN) :: CONFIG
+      INTEGER, INTENT(IN) :: FIT_STEP
+      REAL(KIND=RT), DIMENSION(:,:,:) :: M_STATES, A_STATES, M_GRADS, A_GRADS
+      REAL(KIND=RT), DIMENSION(:,:) :: AY 
+      ! Local variables.
+      INTEGER :: I, VS, VE, J, R
+      REAL(KIND=RT) :: M_LENGTHS(SIZE(M_STATES,2)), A_LENGTHS(SIZE(A_STATES,2))
+      REAL(KIND=RT) :: M_STATE_TEMP(SIZE(M_STATES,1), SIZE(M_STATES,2))
+      REAL(KIND=RT) :: A_STATE_TEMP(SIZE(A_STATES,1), SIZE(A_STATES,2))
+      INTEGER :: M_ORDER(CONFIG%MDS), A_ORDER(CONFIG%ADS)
+      ! Maintain a constant max-norm across the magnitue of input and internal vectors.
+      CALL UNIT_MAX_NORM(CONFIG%MDI, CONFIG%MDS, CONFIG%MNS, &
+           MODEL(CONFIG%MSIV:CONFIG%MEIV), &
+           MODEL(CONFIG%MSSV:CONFIG%MESV))
+      IF (CONFIG%ADI .GT. 0) THEN
+         CALL UNIT_MAX_NORM(CONFIG%ADI, CONFIG%ADS, CONFIG%ANS, &
+              MODEL(CONFIG%ASIV:CONFIG%AEIV), &
+              MODEL(CONFIG%ASSV:CONFIG%AESV))
+      END IF
 
-    ! Erase the printed message if one was produced.
-    IF (DID_PRINT) WRITE (*,'(A)',ADVANCE='NO') RESET_LINE
+      ! Update the apositional model output shift to 
+      !  produce componentwise mean-zero values (prevent divergence).
+      IF (CONFIG%ADO .GT. 0) THEN
+         MODEL(CONFIG%AOSS:CONFIG%AOSE) = -SUM(AY(:,:),1) / REAL(SIZE(AY,1),RT)
+      END IF
+
+      ! -------------------------------------------------------------
+      ! TODO:
+      !  - Using the computed rank of values and gradients, delete the
+      !    least aligned basis functions and initialize with a combination
+      !    of aligning previous layer values with gradients (first nonzero
+      !    gradient components, then remaining nonzero input components).
+      ! 
+      ! - When measuring alignment of two vectors come up with way to
+      !   quickly find the "most aligned" shift term (the shift that
+      !   maximizes the dot product of the vectors assuming rectification).
+      ! 
+      IF (MOD(FIT_STEP-1,CONFIG%LOGGING_STEP_FREQUENCY) .EQ. 0) THEN
+         TOTAL_EVAL_RANK = 0
+         TOTAL_GRAD_RANK = 0
+         ! Check the rank of all internal apositional states.
+         J = CONFIG%ANS+1
+         !$OMP PARALLEL DO PRIVATE(A_ORDER,A_STATE_TEMP,A_LENGTHS,R) &
+         !$OMP& REDUCTION(+: TOTAL_EVAL_RANK, TOTAL_GRAD_RANK)
+         DO I = 1, CONFIG%ANS-1
+            ! Compute model state rank.
+            A_STATE_TEMP(:,:) = A_STATES(:,:,I)
+            CALL ORTHOGONALIZE(A_STATE_TEMP(:,:), A_LENGTHS(:), R)
+            TOTAL_EVAL_RANK = TOTAL_EVAL_RANK + R
+            ! Compute grad state rank.
+            A_STATE_TEMP(:,:) = A_GRADS(:,:,I)
+            CALL ORTHOGONALIZE(A_STATE_TEMP(:,:), A_LENGTHS(:), R)
+            TOTAL_GRAD_RANK = TOTAL_GRAD_RANK + R
+         END DO
+         !$OMP END PARALLEL DO
+         ! 
+         ! Check the rank of all internal model states.
+         J = CONFIG%MNS+1
+         !$OMP PARALLEL DO PRIVATE(M_ORDER,M_STATE_TEMP,M_LENGTHS,R) &
+         !$OMP& REDUCTION(+: TOTAL_EVAL_RANK, TOTAL_GRAD_RANK)
+         DO I = 1, CONFIG%MNS-1
+            ! Compute model state rank.
+            M_STATE_TEMP(:,:) = M_STATES(:,:,I)
+            CALL ORTHOGONALIZE(M_STATE_TEMP(:,:), M_LENGTHS(:), R, M_ORDER(:))
+            TOTAL_EVAL_RANK = TOTAL_EVAL_RANK + R
+            ! Compute grad state rank.
+            M_STATE_TEMP(:,:) = M_GRADS(:,:,I)
+            CALL ORTHOGONALIZE(M_STATE_TEMP(:,:), M_LENGTHS(:), R, M_ORDER(:))
+            TOTAL_GRAD_RANK = TOTAL_GRAD_RANK + R
+         END DO
+         !$OMP END PARALLEL DO
+      END IF
+
+    END SUBROUTINE CONDITION_MODEL
 
-  CONTAINS
 
     ! Set the input vectors and the state vectors to 
     SUBROUTINE UNIT_MAX_NORM(MDI, MDS, MNS, INPUT_VECS, STATE_VECS)
       INTEGER, INTENT(IN) :: MDI, MDS, MNS
       REAL(KIND=RT), INTENT(INOUT), DIMENSION(MDI,MDS)       :: INPUT_VECS
       REAL(KIND=RT), INTENT(INOUT), DIMENSION(MDS,MDS,MNS-1) :: STATE_VECS
       REAL(KIND=RT) :: SCALAR
@@ -1326,157 +2264,40 @@
       DO L = 1, SIZE(STATE_VECS,3)
          SCALAR = SQRT(MAXVAL(SUM(STATE_VECS(:,:,L)**2, 1)))
          STATE_VECS(:,:,L) = STATE_VECS(:,:,L) / SCALAR
       END DO
       !$OMP END PARALLEL DO
     END SUBROUTINE UNIT_MAX_NORM
 
+
     ! Scale a set of basis functions by "weights".
-    SUBROUTINE SCALE_BASIS(M, N, MATRIX, WEIGHTS, TRANS)
-      INTEGER, INTENT(IN) :: M, N
-      REAL(KIND=RT), INTENT(INOUT), DIMENSION(M,N) :: MATRIX
-      REAL(KIND=RT), INTENT(IN), DIMENSION(:) :: WEIGHTS
-      LOGICAL, INTENT(IN), OPTIONAL :: TRANS
-      LOGICAL :: T
-      INTEGER :: I
-      IF (PRESENT(TRANS)) THEN ; T = TRANS
-      ELSE                     ; T = .FALSE.
-      END IF
-      IF (T) THEN
-         DO I = 1, SIZE(WEIGHTS)
-            MATRIX(:,I) = MATRIX(:,I) * WEIGHTS(I)
-         END DO
-      ELSE
-         DO I = 1, SIZE(WEIGHTS)
-            MATRIX(I,:) = MATRIX(I,:) * WEIGHTS(I)
-         END DO
+    SUBROUTINE SCALE_BASIS(MATRIX, TRANSFORMATION)
+      REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: MATRIX
+      REAL(KIND=RT), INTENT(IN), DIMENSION(:,:) :: TRANSFORMATION
+      ! Local variables.
+      REAL(KIND=RT), DIMENSION(SIZE(MATRIX,1),SIZE(MATRIX,2)) :: MATRIX_TEMP
+      INTEGER :: I, M, N
+      M = SIZE(MATRIX,1)
+      N = SIZE(MATRIX,2)
+      ! Create a copy of the matrix.
+      MATRIX_TEMP(:,:) = MATRIX(:,:)
+      IF (SIZE(TRANSFORMATION,1) .EQ. M) THEN
+         ! Multiply the transformation on the left.
+         CALL GEMM('N', 'N', M, N, M, 1.0_RT, &
+              TRANSFORMATION(:,:), M, &
+              MATRIX_TEMP(:,:), M, &
+              0.0_RT, MATRIX(:,:), M)
+      ELSE IF (SIZE(TRANSFORMATION,1) .EQ. N) THEN
+         ! Multiply the transformation on the right.
+         CALL GEMM('N', 'N', M, N, N, 1.0_RT, &
+              MATRIX_TEMP(:,:), M, &
+              TRANSFORMATION(:,:), N, &
+              0.0_RT, MATRIX(:,:), M)
       END IF
     END SUBROUTINE SCALE_BASIS
 
-    
-    ! ------------------------------------------------------------------
-    !                       FastSelect method
-    ! 
-    ! Given VALUES list of numbers, rearrange the elements of INDICES
-    ! such that the element of VALUES at INDICES(K) has rank K (holds
-    ! its same location as if all of VALUES were sorted in INDICES).
-    ! All elements of VALUES at INDICES(:K-1) are less than or equal,
-    ! while all elements of VALUES at INDICES(K+1:) are greater or equal.
-    ! 
-    ! This algorithm uses a recursive approach to exponentially shrink
-    ! the number of indices that have to be considered to find the
-    ! element of desired rank, while simultaneously pivoting values
-    ! that are less than the target rank left and larger right.
-    ! 
-    ! Arguments:
-    ! 
-    !   VALUES   --  A 1D array of real numbers. Will not be modified.
-    !   K        --  A positive integer for the rank index about which
-    !                VALUES should be rearranged.
-    ! Optional:
-    ! 
-    !   DIVISOR  --  A positive integer >= 2 that represents the
-    !                division factor used for large VALUES arrays.
-    !   MAX_SIZE --  An integer >= DIVISOR that represents the largest
-    !                sized VALUES for which the worst-case pivot value
-    !                selection is tolerable. A worst-case pivot causes
-    !                O( SIZE(VALUES)^2 ) runtime. This value should be
-    !                determined heuristically based on compute hardware.
-    ! Output:
-    ! 
-    !   INDICES  --  A 1D array of original indices for elements of VALUES.
-    ! 
-    !   The elements of the array INDICES are rearranged such that the
-    !   element at position VALUES(INDICES(K)) is in the same location 
-    !   it would be if all of VALUES were referenced in sorted order in
-    !   INDICES. Also known as, VALUES(INDICES(K)) has rank K.
-    ! 
-    RECURSIVE SUBROUTINE ARGSELECT(VALUES, K, INDICES, DIVISOR, MAX_SIZE, RECURSING)
-      USE ISO_FORTRAN_ENV, ONLY: RT => REAL32
-      IMPLICIT NONE
-      ! Arguments
-      REAL(KIND=RT), INTENT(IN), DIMENSION(:) :: VALUES
-      INTEGER, INTENT(IN) :: K
-      INTEGER, INTENT(INOUT), DIMENSION(:) :: INDICES
-      INTEGER, INTENT(IN), OPTIONAL :: DIVISOR, MAX_SIZE
-      LOGICAL, INTENT(IN), OPTIONAL :: RECURSING
-      ! Locals
-      INTEGER :: LEFT, RIGHT, L, R, MS, D, I
-      REAL(KIND=RT) :: P
-      ! Initialize the divisor (for making subsets).
-      IF (PRESENT(DIVISOR)) THEN ; D = DIVISOR
-      ELSE IF (SIZE(INDICES) .GE. 8388608) THEN ; D = 32 ! 2**5 ! 2**23
-      ELSE IF (SIZE(INDICES) .GE. 1048576) THEN ; D = 8  ! 2**3 ! 2**20
-      ELSE                                      ; D = 4  ! 2**2
-      END IF
-      ! Initialize the max size (before subsets are created).
-      IF (PRESENT(MAX_SIZE)) THEN ; MS = MAX_SIZE
-      ELSE                        ; MS = 1024 ! 2**10
-      END IF
-      ! When not recursing, set the INDICES to default values.
-      IF (.NOT. PRESENT(RECURSING)) THEN
-         FORALL(I=1:SIZE(INDICES)) INDICES(I) = I
-      END IF
-      ! Initialize LEFT and RIGHT to be the entire array.
-      LEFT = 1
-      RIGHT = SIZE(INDICES)
-      ! Loop until done finding the K-th element.
-      DO WHILE (LEFT .LT. RIGHT)
-         ! Use SELECT recursively to improve the quality of the
-         ! selected pivot value for large arrays.
-         IF (RIGHT - LEFT .GT. MS) THEN
-            ! Compute how many elements should be left and right of K
-            ! to maintain the same percentile in a subset.
-            L = K - K / D
-            R = L + (SIZE(INDICES) / D)
-            ! Perform fast select on an array a fraction of the size about K.
-            CALL ARGSELECT(VALUES(:), K - L + 1, INDICES(L:R), &
-                 DIVISOR=D, MAX_SIZE=MS, RECURSING=.TRUE.)
-         END IF
-         ! Pick a partition element at position K.
-         P = VALUES(INDICES(K))
-         L = LEFT
-         R = RIGHT
-         ! Move the partition element to the front of the list.
-         CALL SWAP_INT(INDICES(LEFT), INDICES(K))
-         ! Pre-swap the left and right elements (temporarily putting a
-         ! larger element on the left) before starting the partition loop.
-         IF (VALUES(INDICES(RIGHT)) .GT. P) THEN
-            CALL SWAP_INT(INDICES(LEFT), INDICES(RIGHT))
-         END IF
-         ! Now partition the elements about the pivot value "P".
-         DO WHILE (L .LT. R)
-            CALL SWAP_INT(INDICES(L), INDICES(R))
-            L = L + 1
-            R = R - 1
-            DO WHILE (VALUES(INDICES(L)) .LT. P) ; L = L + 1 ; END DO
-            DO WHILE (VALUES(INDICES(R)) .GT. P) ; R = R - 1 ; END DO
-         END DO
-         ! Place the pivot element back into its appropriate place.
-         IF (VALUES(INDICES(LEFT)) .EQ. P) THEN
-            CALL SWAP_INT(INDICES(LEFT), INDICES(R))
-         ELSE
-            R = R + 1
-            CALL SWAP_INT(INDICES(R), INDICES(RIGHT))
-         END IF
-         ! adjust left and right towards the boundaries of the subset
-         ! containing the (k - left + 1)th smallest element
-         IF (R .LE. K) LEFT = R + 1
-         IF (K .LE. R) RIGHT = R - 1
-      END DO
-    END SUBROUTINE ARGSELECT
-
-    SUBROUTINE SWAP_INT(V1, V2)
-      IMPLICIT NONE
-      INTEGER, INTENT(INOUT) :: V1, V2
-      INTEGER :: TEMP
-      TEMP = V1
-      V1 = V2
-      V2 = TEMP
-    END SUBROUTINE SWAP_INT
-
 
   END SUBROUTINE MINIMIZE_MSE
 
 
 END MODULE APOS
```

### Comparing `tlux-0.0.8/tlux/approximate/apos/apos/apos_c_wrapper.f90` & `tlux-0.0.9/tlux/approximate/apos/apos/apos_c_wrapper.f90`

 * *Files 24% similar despite different names*

```diff
@@ -60,4882 +60,5141 @@
     INTEGER, INTENT(IN) :: COLUMN_VECTORS_DIM_1
     INTEGER, INTENT(IN) :: COLUMN_VECTORS_DIM_2
     REAL(KIND=RT), INTENT(OUT), DIMENSION(COLUMN_VECTORS_DIM_1,COLUMN_VECTORS_DIM_2) :: COLUMN_VECTORS
   
     CALL RANDOM_UNIT_VECTORS(COLUMN_VECTORS)
   END SUBROUTINE C_RANDOM_UNIT_VECTORS
   
+
+  
+  SUBROUTINE C_ORTHOGONALIZE(A_DIM_1, A_DIM_2, A, LENGTHS_DIM_1, LENGTHS, RANK_PRESENT, RANK, ORDER_PRESENT, ORDER_DIM_1, ORDER) BI&
+&ND(C)
+    USE MATRIX_OPERATIONS, ONLY: ORTHOGONALIZE
+    IMPLICIT NONE
+    INTEGER, INTENT(IN) :: A_DIM_1
+    INTEGER, INTENT(IN) :: A_DIM_2
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(A_DIM_1,A_DIM_2) :: A
+    INTEGER, INTENT(IN) :: LENGTHS_DIM_1
+    REAL(KIND=RT), INTENT(OUT), DIMENSION(LENGTHS_DIM_1) :: LENGTHS
+    LOGICAL, INTENT(IN) :: RANK_PRESENT
+    INTEGER, INTENT(OUT) :: RANK
+    LOGICAL, INTENT(IN) :: ORDER_PRESENT
+    INTEGER, INTENT(IN) :: ORDER_DIM_1
+    INTEGER, INTENT(OUT), DIMENSION(ORDER_DIM_1) :: ORDER
+  
+    IF (RANK_PRESENT) THEN
+      IF (ORDER_PRESENT) THEN
+        CALL ORTHOGONALIZE(A=A, LENGTHS=LENGTHS, RANK=RANK, ORDER=ORDER)
+      ELSE
+        CALL ORTHOGONALIZE(A=A, LENGTHS=LENGTHS, RANK=RANK)
+      END IF
+    ELSE
+      IF (ORDER_PRESENT) THEN
+        CALL ORTHOGONALIZE(A=A, LENGTHS=LENGTHS, ORDER=ORDER)
+      ELSE
+        CALL ORTHOGONALIZE(A=A, LENGTHS=LENGTHS)
+      END IF
+    END IF
+  END SUBROUTINE C_ORTHOGONALIZE
+  
+
+  
+  SUBROUTINE C_SVD(A_DIM_1, A_DIM_2, A, S_DIM_1, S, VT_DIM_1, VT_DIM_2, VT, RANK_PRESENT, RANK, STEPS_PRESENT, STEPS, BIAS_PRESENT,&
+& BIAS) BIND(C)
+    USE MATRIX_OPERATIONS, ONLY: SVD
+    IMPLICIT NONE
+    INTEGER, INTENT(IN) :: A_DIM_1
+    INTEGER, INTENT(IN) :: A_DIM_2
+    REAL(KIND=RT), INTENT(IN), DIMENSION(A_DIM_1,A_DIM_2) :: A
+    INTEGER, INTENT(IN) :: S_DIM_1
+    REAL(KIND=RT), INTENT(OUT), DIMENSION(S_DIM_1) :: S
+    INTEGER, INTENT(IN) :: VT_DIM_1
+    INTEGER, INTENT(IN) :: VT_DIM_2
+    REAL(KIND=RT), INTENT(OUT), DIMENSION(VT_DIM_1,VT_DIM_2) :: VT
+    LOGICAL, INTENT(IN) :: RANK_PRESENT
+    INTEGER, INTENT(OUT) :: RANK
+    LOGICAL, INTENT(IN) :: STEPS_PRESENT
+    INTEGER, INTENT(IN) :: STEPS
+    LOGICAL, INTENT(IN) :: BIAS_PRESENT
+    REAL(KIND=RT), INTENT(IN) :: BIAS
+  
+    IF (RANK_PRESENT) THEN
+      IF (STEPS_PRESENT) THEN
+        IF (BIAS_PRESENT) THEN
+          CALL SVD(A=A, S=S, VT=VT, RANK=RANK, STEPS=STEPS, BIAS=BIAS)
+        ELSE
+          CALL SVD(A=A, S=S, VT=VT, RANK=RANK, STEPS=STEPS)
+        END IF
+      ELSE
+        IF (BIAS_PRESENT) THEN
+          CALL SVD(A=A, S=S, VT=VT, RANK=RANK, BIAS=BIAS)
+        ELSE
+          CALL SVD(A=A, S=S, VT=VT, RANK=RANK)
+        END IF
+      END IF
+    ELSE
+      IF (STEPS_PRESENT) THEN
+        IF (BIAS_PRESENT) THEN
+          CALL SVD(A=A, S=S, VT=VT, STEPS=STEPS, BIAS=BIAS)
+        ELSE
+          CALL SVD(A=A, S=S, VT=VT, STEPS=STEPS)
+        END IF
+      ELSE
+        IF (BIAS_PRESENT) THEN
+          CALL SVD(A=A, S=S, VT=VT, BIAS=BIAS)
+        ELSE
+          CALL SVD(A=A, S=S, VT=VT)
+        END IF
+      END IF
+    END IF
+  END SUBROUTINE C_SVD
+  
+
+  
+  SUBROUTINE C_RADIALIZE(X_DIM_1, X_DIM_2, X, SHIFT_DIM_1, SHIFT, VECS_DIM_1, VECS_DIM_2, VECS, INVERT_RESULT_PRESENT, INVERT_RESUL&
+&T, STEPS_PRESENT, STEPS) BIND(C)
+    USE MATRIX_OPERATIONS, ONLY: RADIALIZE
+    IMPLICIT NONE
+    INTEGER, INTENT(IN) :: X_DIM_1
+    INTEGER, INTENT(IN) :: X_DIM_2
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(X_DIM_1,X_DIM_2) :: X
+    INTEGER, INTENT(IN) :: SHIFT_DIM_1
+    REAL(KIND=RT), INTENT(OUT), DIMENSION(SHIFT_DIM_1) :: SHIFT
+    INTEGER, INTENT(IN) :: VECS_DIM_1
+    INTEGER, INTENT(IN) :: VECS_DIM_2
+    REAL(KIND=RT), INTENT(OUT), DIMENSION(VECS_DIM_1,VECS_DIM_2) :: VECS
+    LOGICAL, INTENT(IN) :: INVERT_RESULT_PRESENT
+    LOGICAL, INTENT(IN) :: INVERT_RESULT
+    LOGICAL, INTENT(IN) :: STEPS_PRESENT
+    INTEGER, INTENT(IN) :: STEPS
+  
+    IF (INVERT_RESULT_PRESENT) THEN
+      IF (STEPS_PRESENT) THEN
+        CALL RADIALIZE(X=X, SHIFT=SHIFT, VECS=VECS, INVERT_RESULT=INVERT_RESULT, STEPS=STEPS)
+      ELSE
+        CALL RADIALIZE(X=X, SHIFT=SHIFT, VECS=VECS, INVERT_RESULT=INVERT_RESULT)
+      END IF
+    ELSE
+      IF (STEPS_PRESENT) THEN
+        CALL RADIALIZE(X=X, SHIFT=SHIFT, VECS=VECS, STEPS=STEPS)
+      ELSE
+        CALL RADIALIZE(X=X, SHIFT=SHIFT, VECS=VECS)
+      END IF
+    END IF
+  END SUBROUTINE C_RADIALIZE
+  
 END MODULE C_MATRIX_OPERATIONS
 
 
-MODULE C_APOS
+MODULE C_SORT_AND_SELECT
 USE ISO_FORTRAN_ENV , ONLY : RT => REAL32
-USE MATRIX_OPERATIONS , ONLY : GEMM , ORTHONORMALIZE , RANDOM_UNIT_VECTORS
+  IMPLICIT NONE
+
+
+CONTAINS
+
+
+  
+  SUBROUTINE C_SWAP_INT(V1, V2) BIND(C)
+    USE SORT_AND_SELECT, ONLY: SWAP_INT
+    IMPLICIT NONE
+    INTEGER, INTENT(INOUT) :: V1
+    INTEGER, INTENT(INOUT) :: V2
+  
+    CALL SWAP_INT(V1, V2)
+  END SUBROUTINE C_SWAP_INT
+  
+
+  
+  SUBROUTINE C_ARGSELECT(VALUES_DIM_1, VALUES, K, INDICES_DIM_1, INDICES, DIVISOR_PRESENT, DIVISOR, MAX_SIZE_PRESENT, MAX_SIZE, REC&
+&URSING_PRESENT, RECURSING) BIND(C)
+    USE SORT_AND_SELECT, ONLY: ARGSELECT
+    IMPLICIT NONE
+    INTEGER, INTENT(IN) :: VALUES_DIM_1
+    REAL(KIND=RT), INTENT(IN), DIMENSION(VALUES_DIM_1) :: VALUES
+    INTEGER, INTENT(IN) :: K
+    INTEGER, INTENT(IN) :: INDICES_DIM_1
+    INTEGER, INTENT(INOUT), DIMENSION(INDICES_DIM_1) :: INDICES
+    LOGICAL, INTENT(IN) :: DIVISOR_PRESENT
+    INTEGER, INTENT(IN) :: DIVISOR
+    LOGICAL, INTENT(IN) :: MAX_SIZE_PRESENT
+    INTEGER, INTENT(IN) :: MAX_SIZE
+    LOGICAL, INTENT(IN) :: RECURSING_PRESENT
+    LOGICAL, INTENT(IN) :: RECURSING
+  
+    IF (DIVISOR_PRESENT) THEN
+      IF (MAX_SIZE_PRESENT) THEN
+        IF (RECURSING_PRESENT) THEN
+          CALL ARGSELECT(VALUES=VALUES, K=K, INDICES=INDICES, DIVISOR=DIVISOR, MAX_SIZE=MAX_SIZE, RECURSING=RECURSING)
+        ELSE
+          CALL ARGSELECT(VALUES=VALUES, K=K, INDICES=INDICES, DIVISOR=DIVISOR, MAX_SIZE=MAX_SIZE)
+        END IF
+      ELSE
+        IF (RECURSING_PRESENT) THEN
+          CALL ARGSELECT(VALUES=VALUES, K=K, INDICES=INDICES, DIVISOR=DIVISOR, RECURSING=RECURSING)
+        ELSE
+          CALL ARGSELECT(VALUES=VALUES, K=K, INDICES=INDICES, DIVISOR=DIVISOR)
+        END IF
+      END IF
+    ELSE
+      IF (MAX_SIZE_PRESENT) THEN
+        IF (RECURSING_PRESENT) THEN
+          CALL ARGSELECT(VALUES=VALUES, K=K, INDICES=INDICES, MAX_SIZE=MAX_SIZE, RECURSING=RECURSING)
+        ELSE
+          CALL ARGSELECT(VALUES=VALUES, K=K, INDICES=INDICES, MAX_SIZE=MAX_SIZE)
+        END IF
+      ELSE
+        IF (RECURSING_PRESENT) THEN
+          CALL ARGSELECT(VALUES=VALUES, K=K, INDICES=INDICES, RECURSING=RECURSING)
+        ELSE
+          CALL ARGSELECT(VALUES=VALUES, K=K, INDICES=INDICES)
+        END IF
+      END IF
+    END IF
+  END SUBROUTINE C_ARGSELECT
+  
+
+  
+  SUBROUTINE C_ARGSORT(VALUES_DIM_1, VALUES, INDICES_DIM_1, INDICES, MIN_SIZE_PRESENT, MIN_SIZE, INIT_INDS_PRESENT, INIT_INDS) BIND&
+&(C)
+    USE SORT_AND_SELECT, ONLY: ARGSORT
+    IMPLICIT NONE
+    INTEGER, INTENT(IN) :: VALUES_DIM_1
+    REAL(KIND=RT), INTENT(IN), DIMENSION(VALUES_DIM_1) :: VALUES
+    INTEGER, INTENT(IN) :: INDICES_DIM_1
+    INTEGER, INTENT(INOUT), DIMENSION(INDICES_DIM_1) :: INDICES
+    LOGICAL, INTENT(IN) :: MIN_SIZE_PRESENT
+    INTEGER, INTENT(IN) :: MIN_SIZE
+    LOGICAL, INTENT(IN) :: INIT_INDS_PRESENT
+    LOGICAL, INTENT(IN) :: INIT_INDS
+  
+    IF (MIN_SIZE_PRESENT) THEN
+      IF (INIT_INDS_PRESENT) THEN
+        CALL ARGSORT(VALUES=VALUES, INDICES=INDICES, MIN_SIZE=MIN_SIZE, INIT_INDS=INIT_INDS)
+      ELSE
+        CALL ARGSORT(VALUES=VALUES, INDICES=INDICES, MIN_SIZE=MIN_SIZE)
+      END IF
+    ELSE
+      IF (INIT_INDS_PRESENT) THEN
+        CALL ARGSORT(VALUES=VALUES, INDICES=INDICES, INIT_INDS=INIT_INDS)
+      ELSE
+        CALL ARGSORT(VALUES=VALUES, INDICES=INDICES)
+      END IF
+    END IF
+  END SUBROUTINE C_ARGSORT
+  
+
+  
+  SUBROUTINE C_INSERTION_ARGSORT(VALUES_DIM_1, VALUES, INDICES_DIM_1, INDICES) BIND(C)
+    USE SORT_AND_SELECT, ONLY: INSERTION_ARGSORT
+    IMPLICIT NONE
+    INTEGER, INTENT(IN) :: VALUES_DIM_1
+    REAL(KIND=RT), INTENT(IN), DIMENSION(VALUES_DIM_1) :: VALUES
+    INTEGER, INTENT(IN) :: INDICES_DIM_1
+    INTEGER, INTENT(INOUT), DIMENSION(INDICES_DIM_1) :: INDICES
+  
+    CALL INSERTION_ARGSORT(VALUES, INDICES)
+  END SUBROUTINE C_INSERTION_ARGSORT
+  
+
+  
+  SUBROUTINE C_ARGPARTITION(VALUES_DIM_1, VALUES, INDICES_DIM_1, INDICES, LEFT) BIND(C)
+    USE SORT_AND_SELECT, ONLY: ARGPARTITION
+    IMPLICIT NONE
+    INTEGER, INTENT(IN) :: VALUES_DIM_1
+    REAL(KIND=RT), INTENT(IN), DIMENSION(VALUES_DIM_1) :: VALUES
+    INTEGER, INTENT(IN) :: INDICES_DIM_1
+    INTEGER, INTENT(INOUT), DIMENSION(INDICES_DIM_1) :: INDICES
+    INTEGER :: LEFT
+  
+    LEFT = ARGPARTITION(VALUES, INDICES)
+  END SUBROUTINE C_ARGPARTITION
+  
+END MODULE C_SORT_AND_SELECT
+
+
+MODULE C_APOS
+USE ISO_FORTRAN_ENV , ONLY : RT => REAL32 , INT64 , INT8
+USE MATRIX_OPERATIONS , ONLY : GEMM , RANDOM_UNIT_VECTORS , ORTHOGONALIZE , RADIALIZE
+USE SORT_AND_SELECT , ONLY : ARGSORT , ARGSELECT
   IMPLICIT NONE
 
 
   INTERFACE
     FUNCTION OMP_GET_MAX_THREADS()
       INTEGER :: OMP_GET_MAX_THREADS
     END FUNCTION OMP_GET_MAX_THREADS
   END INTERFACE
 
 CONTAINS
 
 
   
-  SUBROUTINE C_NEW_MODEL_CONFIG(MDI, MDO, MDS_PRESENT, MDS, MNS_PRESENT, MNS, MNE_PRESENT, MNE, MDE_PRESENT, MDE, ADI, ADO_PRESENT,&
-& ADO, ADS_PRESENT, ADS, ANS_PRESENT, ANS, ANE_PRESENT, ANE, ADE_PRESENT, ADE, NUM_THREADS_PRESENT, NUM_THREADS, CONFIG) BIND(C)
+  SUBROUTINE C_NEW_MODEL_CONFIG(ADN, ADO_PRESENT, ADO, ADS_PRESENT, ADS, ANS_PRESENT, ANS, ANE_PRESENT, ANE, ADE_PRESENT, ADE, MDN,&
+& MDO, MDS_PRESENT, MDS, MNS_PRESENT, MNS, MNE_PRESENT, MNE, MDE_PRESENT, MDE, NUM_THREADS_PRESENT, NUM_THREADS, CONFIG) BIND(C)
     USE APOS, ONLY: NEW_MODEL_CONFIG
     USE APOS, ONLY: MODEL_CONFIG
     IMPLICIT NONE
-    INTEGER, INTENT(IN) :: MDI
-    INTEGER, INTENT(IN) :: MDO
-    LOGICAL, INTENT(IN) :: MDS_PRESENT
-    INTEGER, INTENT(IN) :: MDS
-    LOGICAL, INTENT(IN) :: MNS_PRESENT
-    INTEGER, INTENT(IN) :: MNS
-    LOGICAL, INTENT(IN) :: MNE_PRESENT
-    INTEGER, INTENT(IN) :: MNE
-    LOGICAL, INTENT(IN) :: MDE_PRESENT
-    INTEGER, INTENT(IN) :: MDE
-    INTEGER, INTENT(IN) :: ADI
+    INTEGER, INTENT(IN) :: ADN
     LOGICAL, INTENT(IN) :: ADO_PRESENT
     INTEGER, INTENT(IN) :: ADO
     LOGICAL, INTENT(IN) :: ADS_PRESENT
     INTEGER, INTENT(IN) :: ADS
     LOGICAL, INTENT(IN) :: ANS_PRESENT
     INTEGER, INTENT(IN) :: ANS
     LOGICAL, INTENT(IN) :: ANE_PRESENT
     INTEGER, INTENT(IN) :: ANE
     LOGICAL, INTENT(IN) :: ADE_PRESENT
     INTEGER, INTENT(IN) :: ADE
+    INTEGER, INTENT(IN) :: MDN
+    INTEGER, INTENT(IN) :: MDO
+    LOGICAL, INTENT(IN) :: MDS_PRESENT
+    INTEGER, INTENT(IN) :: MDS
+    LOGICAL, INTENT(IN) :: MNS_PRESENT
+    INTEGER, INTENT(IN) :: MNS
+    LOGICAL, INTENT(IN) :: MNE_PRESENT
+    INTEGER, INTENT(IN) :: MNE
+    LOGICAL, INTENT(IN) :: MDE_PRESENT
+    INTEGER, INTENT(IN) :: MDE
     LOGICAL, INTENT(IN) :: NUM_THREADS_PRESENT
     INTEGER, INTENT(IN) :: NUM_THREADS
     TYPE(MODEL_CONFIG), INTENT(OUT) :: CONFIG
   
-    IF (MDS_PRESENT) THEN
-      IF (MNS_PRESENT) THEN
-        IF (MNE_PRESENT) THEN
-          IF (MDE_PRESENT) THEN
-            IF (ADO_PRESENT) THEN
-              IF (ADS_PRESENT) THEN
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+    IF (ADO_PRESENT) THEN
+      IF (ADS_PRESENT) THEN
+        IF (ANS_PRESENT) THEN
+          IF (ANE_PRESENT) THEN
+            IF (ADE_PRESENT) THEN
+              IF (MDS_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO&
-&, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+&, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO&
-&, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+&, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO&
-&, ADS=ADS, ANS=ANS, ANE=ANE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+&, MDS=MDS, MNS=MNS, MNE=MNE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO&
-&, ADS=ADS, ANS=ANS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+&, MDS=MDS, MNS=MNS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO&
-&, ADS=ADS, ANS=ANS, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+&, MDS=MDS, MNS=MNS, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO&
-&, ADS=ADS, ANS=ANS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+&, MDS=MDS, MNS=MNS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO&
-&, ADS=ADS, ANS=ANS, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+&, MDS=MDS, MNS=MNS, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO&
-&, ADS=ADS, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+&, MDS=MDS, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO&
-&, ADS=ADS, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+&, MDS=MDS, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO&
-&, ADS=ADS, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+&, MDS=MDS, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO&
-&, ADS=ADS, ANE=ANE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+&, MDS=MDS, MNE=MNE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO&
-&, ADS=ADS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+&, MDS=MDS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO&
-&, ADS=ADS, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+&, MDS=MDS, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO&
-&, ADS=ADS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+&, MDS=MDS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO&
-&, ADS=ADS, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+&, MDS=MDS, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO&
-&, ADS=ADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+&, MDS=MDS)
                       END IF
                     END IF
                   END IF
                 END IF
               ELSE
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO&
-&, ANS=ANS, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+&, MNS=MNS, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO&
-&, ANS=ANS, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+&, MNS=MNS, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO&
-&, ANS=ANS, ANE=ANE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+&, MNS=MNS, MNE=MNE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO&
-&, ANS=ANS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+&, MNS=MNS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO&
-&, ANS=ANS, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+&, MNS=MNS, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO&
-&, ANS=ANS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+&, MNS=MNS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO&
-&, ANS=ANS, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+&, MNS=MNS, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO&
-&, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+&, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO&
-&, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+&, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO&
-&, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+&, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO&
-&, ANE=ANE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+&, MNE=MNE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO&
-&, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+&, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
 &)
                       END IF
                     END IF
                   END IF
                 END IF
               END IF
             ELSE
-              IF (ADS_PRESENT) THEN
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+              IF (MDS_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADS=ADS&
-&, ANS=ANS, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, MDS=MDS&
+&, MNS=MNS, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADS=ADS&
-&, ANS=ANS, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, MDS=MDS&
+&, MNS=MNS, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADS=ADS&
-&, ANS=ANS, ANE=ANE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, MDS=MDS&
+&, MNS=MNS, MNE=MNE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADS=ADS&
-&, ANS=ANS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, MDS=MDS&
+&, MNS=MNS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADS=ADS&
-&, ANS=ANS, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, MDS=MDS&
+&, MNS=MNS, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADS=ADS&
-&, ANS=ANS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, MDS=MDS&
+&, MNS=MNS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADS=ADS&
-&, ANS=ANS, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, MDS=MDS&
+&, MNS=MNS, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADS=ADS&
-&, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, MDS=MDS&
+&, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADS=ADS&
-&, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, MDS=MDS&
+&, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADS=ADS&
-&, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, MDS=MDS&
+&, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADS=ADS&
-&, ANE=ANE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, MDS=MDS&
+&, MNE=MNE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADS=ADS&
-&, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, MDS=MDS&
+&, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADS=ADS&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, MDS=MDS&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADS=ADS&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, MDS=MDS&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADS=ADS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, MDS=MDS&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADS=ADS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, MDS=MDS&
 &)
                       END IF
                     END IF
                   END IF
                 END IF
               ELSE
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ANS=ANS&
-&, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, MNS=MNS&
+&, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ANS=ANS&
-&, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, MNS=MNS&
+&, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ANS=ANS&
-&, ANE=ANE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, MNS=MNS&
+&, MNE=MNE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ANS=ANS&
-&, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, MNS=MNS&
+&, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ANS=ANS&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, MNS=MNS&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ANS=ANS&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, MNS=MNS&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ANS=ANS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, MNS=MNS&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ANS=ANS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, MNS=MNS&
 &)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ANE=ANE&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, MNE=MNE&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ANE=ANE&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, MNE=MNE&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, MNE=MNE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, MNE=MNE&
 &)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE)
                       END IF
                     END IF
                   END IF
                 END IF
               END IF
             END IF
           ELSE
-            IF (ADO_PRESENT) THEN
-              IF (ADS_PRESENT) THEN
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+            IF (ADE_PRESENT) THEN
+              IF (MDS_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADO=ADO, ADS=ADS&
-&, ANS=ANS, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE, MDS=MDS&
+&, MNS=MNS, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADO=ADO, ADS=ADS&
-&, ANS=ANS, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE, MDS=MDS&
+&, MNS=MNS, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADO=ADO, ADS=ADS&
-&, ANS=ANS, ANE=ANE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE, MDS=MDS&
+&, MNS=MNS, MNE=MNE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADO=ADO, ADS=ADS&
-&, ANS=ANS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE, MDS=MDS&
+&, MNS=MNS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADO=ADO, ADS=ADS&
-&, ANS=ANS, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE, MDS=MDS&
+&, MNS=MNS, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADO=ADO, ADS=ADS&
-&, ANS=ANS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE, MDS=MDS&
+&, MNS=MNS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADO=ADO, ADS=ADS&
-&, ANS=ANS, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE, MDS=MDS&
+&, MNS=MNS, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADO=ADO, ADS=ADS&
-&, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE, MDS=MDS&
+&, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADO=ADO, ADS=ADS&
-&, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE, MDS=MDS&
+&, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADO=ADO, ADS=ADS&
-&, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE, MDS=MDS&
+&, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADO=ADO, ADS=ADS&
-&, ANE=ANE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE, MDS=MDS&
+&, MNE=MNE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADO=ADO, ADS=ADS&
-&, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE, MDS=MDS&
+&, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADO=ADO, ADS=ADS&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE, MDS=MDS&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADO=ADO, ADS=ADS&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE, MDS=MDS&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADO=ADO, ADS=ADS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE, MDS=MDS&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADO=ADO, ADS=ADS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE, MDS=MDS&
 &)
                       END IF
                     END IF
                   END IF
                 END IF
               ELSE
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADO=ADO, ANS=ANS&
-&, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE, MNS=MNS&
+&, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADO=ADO, ANS=ANS&
-&, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE, MNS=MNS&
+&, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADO=ADO, ANS=ANS&
-&, ANE=ANE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE, MNS=MNS&
+&, MNE=MNE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADO=ADO, ANS=ANS&
-&, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE, MNS=MNS&
+&, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADO=ADO, ANS=ANS&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE, MNS=MNS&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADO=ADO, ANS=ANS&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE, MNS=MNS&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADO=ADO, ANS=ANS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE, MNS=MNS&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADO=ADO, ANS=ANS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE, MNS=MNS&
 &)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADO=ADO, ANE=ANE&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE, MNE=MNE&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADO=ADO, ANE=ANE&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE, MNE=MNE&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADO=ADO, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE, MNE=MNE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADO=ADO, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE, MNE=MNE&
 &)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADO=ADO, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADO=ADO, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADO=ADO, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADO=ADO)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE)
                       END IF
                     END IF
                   END IF
                 END IF
               END IF
             ELSE
-              IF (ADS_PRESENT) THEN
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+              IF (MDS_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADS=ADS, ANS=ANS&
-&, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, MDS=MDS, MNS=MNS&
+&, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADS=ADS, ANS=ANS&
-&, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, MDS=MDS, MNS=MNS&
+&, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADS=ADS, ANS=ANS&
-&, ANE=ANE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, MDS=MDS, MNS=MNS&
+&, MNE=MNE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADS=ADS, ANS=ANS&
-&, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, MDS=MDS, MNS=MNS&
+&, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADS=ADS, ANS=ANS&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, MDS=MDS, MNS=MNS&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADS=ADS, ANS=ANS&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, MDS=MDS, MNS=MNS&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADS=ADS, ANS=ANS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, MDS=MDS, MNS=MNS&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADS=ADS, ANS=ANS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, MDS=MDS, MNS=MNS&
 &)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADS=ADS, ANE=ANE&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, MDS=MDS, MNE=MNE&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADS=ADS, ANE=ANE&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, MDS=MDS, MNE=MNE&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADS=ADS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, MDS=MDS, MNE=MNE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADS=ADS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, MDS=MDS, MNE=MNE&
 &)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADS=ADS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, MDS=MDS, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADS=ADS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, MDS=MDS, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADS=ADS, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, MDS=MDS, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADS=ADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, MDS=MDS)
                       END IF
                     END IF
                   END IF
                 END IF
               ELSE
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ANS=ANS, ANE=ANE&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, MNS=MNS, MNE=MNE&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ANS=ANS, ANE=ANE&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, MNS=MNS, MNE=MNE&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, MNS=MNS, MNE=MNE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, MNS=MNS, MNE=MNE&
 &)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, MNS=MNS, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, MNS=MNS, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ANS=ANS, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, MNS=MNS, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, MNE=MNE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, MNE=MNE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ANE=ANE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, MNE=MNE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS)
                       END IF
                     END IF
                   END IF
                 END IF
               END IF
             END IF
           END IF
         ELSE
-          IF (MDE_PRESENT) THEN
-            IF (ADO_PRESENT) THEN
-              IF (ADS_PRESENT) THEN
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+          IF (ANE_PRESENT) THEN
+            IF (ADE_PRESENT) THEN
+              IF (MDS_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ANS=ANS, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MNS=MNS, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ANS=ANS, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MNS=MNS, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ANS=ANS, ANE=ANE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MNS=MNS, MNE=MNE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ANS=ANS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MNS=MNS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ANS=ANS, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MNS=MNS, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ANS=ANS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MNS=MNS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ANS=ANS, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MNS=MNS, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ANE=ANE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MNE=MNE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADO=ADO, ADS=ADS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE, MDS=MDS&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADO=ADO, ADS=ADS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE, MDS=MDS&
 &)
                       END IF
                     END IF
                   END IF
                 END IF
               ELSE
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADO=ADO, ANS=ANS&
-&, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE, MNS=MNS&
+&, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADO=ADO, ANS=ANS&
-&, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE, MNS=MNS&
+&, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADO=ADO, ANS=ANS&
-&, ANE=ANE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE, MNS=MNS&
+&, MNE=MNE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADO=ADO, ANS=ANS&
-&, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE, MNS=MNS&
+&, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADO=ADO, ANS=ANS&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE, MNS=MNS&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADO=ADO, ANS=ANS&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE, MNS=MNS&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADO=ADO, ANS=ANS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE, MNS=MNS&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADO=ADO, ANS=ANS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE, MNS=MNS&
 &)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADO=ADO, ANE=ANE&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE, MNE=MNE&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADO=ADO, ANE=ANE&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE, MNE=MNE&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADO=ADO, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE, MNE=MNE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADO=ADO, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE, MNE=MNE&
 &)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADO=ADO, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADO=ADO, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADO=ADO, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADO=ADO)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE)
                       END IF
                     END IF
                   END IF
                 END IF
               END IF
             ELSE
-              IF (ADS_PRESENT) THEN
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+              IF (MDS_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADS=ADS, ANS=ANS&
-&, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, MDS=MDS, MNS=MNS&
+&, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADS=ADS, ANS=ANS&
-&, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, MDS=MDS, MNS=MNS&
+&, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADS=ADS, ANS=ANS&
-&, ANE=ANE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, MDS=MDS, MNS=MNS&
+&, MNE=MNE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADS=ADS, ANS=ANS&
-&, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, MDS=MDS, MNS=MNS&
+&, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADS=ADS, ANS=ANS&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, MDS=MDS, MNS=MNS&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADS=ADS, ANS=ANS&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, MDS=MDS, MNS=MNS&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADS=ADS, ANS=ANS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, MDS=MDS, MNS=MNS&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADS=ADS, ANS=ANS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, MDS=MDS, MNS=MNS&
 &)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADS=ADS, ANE=ANE&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, MDS=MDS, MNE=MNE&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADS=ADS, ANE=ANE&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, MDS=MDS, MNE=MNE&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADS=ADS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, MDS=MDS, MNE=MNE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADS=ADS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, MDS=MDS, MNE=MNE&
 &)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADS=ADS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, MDS=MDS, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADS=ADS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, MDS=MDS, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADS=ADS, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, MDS=MDS, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADS=ADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, MDS=MDS)
                       END IF
                     END IF
                   END IF
                 END IF
               ELSE
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ANS=ANS, ANE=ANE&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, MNS=MNS, MNE=MNE&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ANS=ANS, ANE=ANE&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, MNS=MNS, MNE=MNE&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, MNS=MNS, MNE=MNE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, MNS=MNS, MNE=MNE&
 &)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, MNS=MNS, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, MNS=MNS, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ANS=ANS, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, MNS=MNS, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, MNE=MNE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, MNE=MNE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ANE=ANE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, MNE=MNE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE)
                       END IF
                     END IF
                   END IF
                 END IF
               END IF
             END IF
           ELSE
-            IF (ADO_PRESENT) THEN
-              IF (ADS_PRESENT) THEN
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+            IF (ADE_PRESENT) THEN
+              IF (MDS_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADO=ADO, ADS=ADS, ANS=ANS&
-&, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ADE=ADE, MDS=MDS, MNS=MNS&
+&, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADO=ADO, ADS=ADS, ANS=ANS&
-&, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ADE=ADE, MDS=MDS, MNS=MNS&
+&, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADO=ADO, ADS=ADS, ANS=ANS&
-&, ANE=ANE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ADE=ADE, MDS=MDS, MNS=MNS&
+&, MNE=MNE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADO=ADO, ADS=ADS, ANS=ANS&
-&, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ADE=ADE, MDS=MDS, MNS=MNS&
+&, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADO=ADO, ADS=ADS, ANS=ANS&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ADE=ADE, MDS=MDS, MNS=MNS&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADO=ADO, ADS=ADS, ANS=ANS&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ADE=ADE, MDS=MDS, MNS=MNS&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADO=ADO, ADS=ADS, ANS=ANS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ADE=ADE, MDS=MDS, MNS=MNS&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADO=ADO, ADS=ADS, ANS=ANS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ADE=ADE, MDS=MDS, MNS=MNS&
 &)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADO=ADO, ADS=ADS, ANE=ANE&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ADE=ADE, MDS=MDS, MNE=MNE&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADO=ADO, ADS=ADS, ANE=ANE&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ADE=ADE, MDS=MDS, MNE=MNE&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADO=ADO, ADS=ADS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ADE=ADE, MDS=MDS, MNE=MNE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADO=ADO, ADS=ADS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ADE=ADE, MDS=MDS, MNE=MNE&
 &)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADO=ADO, ADS=ADS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ADE=ADE, MDS=MDS, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADO=ADO, ADS=ADS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ADE=ADE, MDS=MDS, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADO=ADO, ADS=ADS, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ADE=ADE, MDS=MDS, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADO=ADO, ADS=ADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ADE=ADE, MDS=MDS)
                       END IF
                     END IF
                   END IF
                 END IF
               ELSE
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADO=ADO, ANS=ANS, ANE=ANE&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ADE=ADE, MNS=MNS, MNE=MNE&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADO=ADO, ANS=ANS, ANE=ANE&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ADE=ADE, MNS=MNS, MNE=MNE&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADO=ADO, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ADE=ADE, MNS=MNS, MNE=MNE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADO=ADO, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ADE=ADE, MNS=MNS, MNE=MNE&
 &)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADO=ADO, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ADE=ADE, MNS=MNS, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADO=ADO, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ADE=ADE, MNS=MNS, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADO=ADO, ANS=ANS, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ADE=ADE, MNS=MNS, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADO=ADO, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ADE=ADE, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADO=ADO, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ADE=ADE, MNE=MNE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADO=ADO, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ADE=ADE, MNE=MNE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADO=ADO, ANE=ANE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ADE=ADE, MNE=MNE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADO=ADO, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ADE=ADE, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADO=ADO, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ADE=ADE, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADO=ADO, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ADE=ADE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADO=ADO, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ADE=ADE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADO=ADO)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ADE=ADE)
                       END IF
                     END IF
                   END IF
                 END IF
               END IF
             ELSE
-              IF (ADS_PRESENT) THEN
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+              IF (MDS_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADS=ADS, ANS=ANS, ANE=ANE&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, MDS=MDS, MNS=MNS, MNE=MNE&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADS=ADS, ANS=ANS, ANE=ANE&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, MDS=MDS, MNS=MNS, MNE=MNE&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADS=ADS, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, MDS=MDS, MNS=MNS, MNE=MNE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADS=ADS, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, MDS=MDS, MNS=MNS, MNE=MNE&
 &)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADS=ADS, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, MDS=MDS, MNS=MNS, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADS=ADS, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, MDS=MDS, MNS=MNS, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADS=ADS, ANS=ANS, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, MDS=MDS, MNS=MNS, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADS=ADS, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, MDS=MDS, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADS=ADS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, MDS=MDS, MNE=MNE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADS=ADS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, MDS=MDS, MNE=MNE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADS=ADS, ANE=ANE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, MDS=MDS, MNE=MNE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADS=ADS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, MDS=MDS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADS=ADS, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, MDS=MDS, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADS=ADS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, MDS=MDS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADS=ADS, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, MDS=MDS, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADS=ADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, MDS=MDS)
                       END IF
                     END IF
                   END IF
                 END IF
               ELSE
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ANS=ANS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, MNS=MNS, MNE=MNE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ANS=ANS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, MNS=MNS, MNE=MNE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ANS=ANS, ANE=ANE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, MNS=MNS, MNE=MNE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ANS=ANS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, MNS=MNS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ANS=ANS, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, MNS=MNS, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ANS=ANS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, MNS=MNS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ANS=ANS, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, MNS=MNS, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ANE=ANE, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, MNE=MNE, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ANE=ANE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, MNE=MNE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADE=ADE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, MDE=MDE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNS=MNS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADS=ADS)
                       END IF
                     END IF
                   END IF
                 END IF
               END IF
             END IF
           END IF
         END IF
       ELSE
-        IF (MNE_PRESENT) THEN
-          IF (MDE_PRESENT) THEN
-            IF (ADO_PRESENT) THEN
-              IF (ADS_PRESENT) THEN
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+        IF (ANS_PRESENT) THEN
+          IF (ANE_PRESENT) THEN
+            IF (ADE_PRESENT) THEN
+              IF (MDS_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ANS=ANS, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MNS=MNS, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ANS=ANS, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MNS=MNS, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ANS=ANS, ANE=ANE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MNS=MNS, MNE=MNE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ANS=ANS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MNS=MNS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ANS=ANS, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MNS=MNS, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ANS=ANS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MNS=MNS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ANS=ANS, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MNS=MNS, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ANE=ANE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MNE=MNE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS&
 &)
                       END IF
                     END IF
                   END IF
                 END IF
               ELSE
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADO=ADO, ANS=ANS&
-&, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE, MNS=MNS&
+&, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADO=ADO, ANS=ANS&
-&, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE, MNS=MNS&
+&, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADO=ADO, ANS=ANS&
-&, ANE=ANE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE, MNS=MNS&
+&, MNE=MNE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADO=ADO, ANS=ANS&
-&, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE, MNS=MNS&
+&, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADO=ADO, ANS=ANS&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE, MNS=MNS&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADO=ADO, ANS=ANS&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE, MNS=MNS&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADO=ADO, ANS=ANS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE, MNS=MNS&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADO=ADO, ANS=ANS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE, MNS=MNS&
 &)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADO=ADO, ANE=ANE&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE, MNE=MNE&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADO=ADO, ANE=ANE&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE, MNE=MNE&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADO=ADO, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE, MNE=MNE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADO=ADO, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE, MNE=MNE&
 &)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADO=ADO, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADO=ADO, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADO=ADO, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADO=ADO)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE)
                       END IF
                     END IF
                   END IF
                 END IF
               END IF
             ELSE
-              IF (ADS_PRESENT) THEN
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+              IF (MDS_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADS=ADS, ANS=ANS&
-&, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, MDS=MDS, MNS=MNS&
+&, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADS=ADS, ANS=ANS&
-&, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, MDS=MDS, MNS=MNS&
+&, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADS=ADS, ANS=ANS&
-&, ANE=ANE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, MDS=MDS, MNS=MNS&
+&, MNE=MNE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADS=ADS, ANS=ANS&
-&, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, MDS=MDS, MNS=MNS&
+&, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADS=ADS, ANS=ANS&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, MDS=MDS, MNS=MNS&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADS=ADS, ANS=ANS&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, MDS=MDS, MNS=MNS&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADS=ADS, ANS=ANS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, MDS=MDS, MNS=MNS&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADS=ADS, ANS=ANS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, MDS=MDS, MNS=MNS&
 &)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADS=ADS, ANE=ANE&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, MDS=MDS, MNE=MNE&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADS=ADS, ANE=ANE&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, MDS=MDS, MNE=MNE&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADS=ADS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, MDS=MDS, MNE=MNE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADS=ADS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, MDS=MDS, MNE=MNE&
 &)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADS=ADS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, MDS=MDS, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADS=ADS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, MDS=MDS, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADS=ADS, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, MDS=MDS, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADS=ADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, MDS=MDS)
                       END IF
                     END IF
                   END IF
                 END IF
               ELSE
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ANS=ANS, ANE=ANE&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, MNS=MNS, MNE=MNE&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ANS=ANS, ANE=ANE&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, MNS=MNS, MNE=MNE&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, MNS=MNS, MNE=MNE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, MNS=MNS, MNE=MNE&
 &)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, MNS=MNS, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, MNS=MNS, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ANS=ANS, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, MNS=MNS, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, MNE=MNE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, MNE=MNE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ANE=ANE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, MNE=MNE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE)
                       END IF
                     END IF
                   END IF
                 END IF
               END IF
             END IF
           ELSE
-            IF (ADO_PRESENT) THEN
-              IF (ADS_PRESENT) THEN
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+            IF (ADE_PRESENT) THEN
+              IF (MDS_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADO=ADO, ADS=ADS, ANS=ANS&
-&, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ADE=ADE, MDS=MDS, MNS=MNS&
+&, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADO=ADO, ADS=ADS, ANS=ANS&
-&, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ADE=ADE, MDS=MDS, MNS=MNS&
+&, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADO=ADO, ADS=ADS, ANS=ANS&
-&, ANE=ANE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ADE=ADE, MDS=MDS, MNS=MNS&
+&, MNE=MNE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADO=ADO, ADS=ADS, ANS=ANS&
-&, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ADE=ADE, MDS=MDS, MNS=MNS&
+&, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADO=ADO, ADS=ADS, ANS=ANS&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ADE=ADE, MDS=MDS, MNS=MNS&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADO=ADO, ADS=ADS, ANS=ANS&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ADE=ADE, MDS=MDS, MNS=MNS&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADO=ADO, ADS=ADS, ANS=ANS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ADE=ADE, MDS=MDS, MNS=MNS&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADO=ADO, ADS=ADS, ANS=ANS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ADE=ADE, MDS=MDS, MNS=MNS&
 &)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADO=ADO, ADS=ADS, ANE=ANE&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ADE=ADE, MDS=MDS, MNE=MNE&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADO=ADO, ADS=ADS, ANE=ANE&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ADE=ADE, MDS=MDS, MNE=MNE&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADO=ADO, ADS=ADS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ADE=ADE, MDS=MDS, MNE=MNE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADO=ADO, ADS=ADS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ADE=ADE, MDS=MDS, MNE=MNE&
 &)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADO=ADO, ADS=ADS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ADE=ADE, MDS=MDS, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADO=ADO, ADS=ADS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ADE=ADE, MDS=MDS, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADO=ADO, ADS=ADS, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ADE=ADE, MDS=MDS, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADO=ADO, ADS=ADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ADE=ADE, MDS=MDS)
                       END IF
                     END IF
                   END IF
                 END IF
               ELSE
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADO=ADO, ANS=ANS, ANE=ANE&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ADE=ADE, MNS=MNS, MNE=MNE&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADO=ADO, ANS=ANS, ANE=ANE&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ADE=ADE, MNS=MNS, MNE=MNE&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADO=ADO, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ADE=ADE, MNS=MNS, MNE=MNE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADO=ADO, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ADE=ADE, MNS=MNS, MNE=MNE&
 &)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADO=ADO, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ADE=ADE, MNS=MNS, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADO=ADO, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ADE=ADE, MNS=MNS, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADO=ADO, ANS=ANS, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ADE=ADE, MNS=MNS, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADO=ADO, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ADE=ADE, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADO=ADO, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ADE=ADE, MNE=MNE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADO=ADO, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ADE=ADE, MNE=MNE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADO=ADO, ANE=ANE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ADE=ADE, MNE=MNE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADO=ADO, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ADE=ADE, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADO=ADO, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ADE=ADE, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADO=ADO, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ADE=ADE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADO=ADO, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ADE=ADE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADO=ADO)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ADE=ADE)
                       END IF
                     END IF
                   END IF
                 END IF
               END IF
             ELSE
-              IF (ADS_PRESENT) THEN
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+              IF (MDS_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADS=ADS, ANS=ANS, ANE=ANE&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, MDS=MDS, MNS=MNS, MNE=MNE&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADS=ADS, ANS=ANS, ANE=ANE&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, MDS=MDS, MNS=MNS, MNE=MNE&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADS=ADS, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, MDS=MDS, MNS=MNS, MNE=MNE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADS=ADS, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, MDS=MDS, MNS=MNS, MNE=MNE&
 &)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADS=ADS, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, MDS=MDS, MNS=MNS, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADS=ADS, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, MDS=MDS, MNS=MNS, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADS=ADS, ANS=ANS, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, MDS=MDS, MNS=MNS, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADS=ADS, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, MDS=MDS, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADS=ADS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, MDS=MDS, MNE=MNE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADS=ADS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, MDS=MDS, MNE=MNE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADS=ADS, ANE=ANE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, MDS=MDS, MNE=MNE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADS=ADS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, MDS=MDS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADS=ADS, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, MDS=MDS, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADS=ADS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, MDS=MDS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADS=ADS, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, MDS=MDS, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADS=ADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, MDS=MDS)
                       END IF
                     END IF
                   END IF
                 END IF
               ELSE
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ANS=ANS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, MNS=MNS, MNE=MNE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ANS=ANS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, MNS=MNS, MNE=MNE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ANS=ANS, ANE=ANE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, MNS=MNS, MNE=MNE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ANS=ANS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, MNS=MNS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ANS=ANS, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, MNS=MNS, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ANS=ANS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, MNS=MNS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ANS=ANS, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, MNS=MNS, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ANE=ANE, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, MNE=MNE, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ANE=ANE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, MNE=MNE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADE=ADE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, MDE=MDE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MNE=MNE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANS=ANS)
                       END IF
                     END IF
                   END IF
                 END IF
               END IF
             END IF
           END IF
         ELSE
-          IF (MDE_PRESENT) THEN
-            IF (ADO_PRESENT) THEN
-              IF (ADS_PRESENT) THEN
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+          IF (ANE_PRESENT) THEN
+            IF (ADE_PRESENT) THEN
+              IF (MDS_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADO=ADO, ADS=ADS, ANS=ANS&
-&, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, ADE=ADE, MDS=MDS, MNS=MNS&
+&, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADO=ADO, ADS=ADS, ANS=ANS&
-&, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, ADE=ADE, MDS=MDS, MNS=MNS&
+&, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADO=ADO, ADS=ADS, ANS=ANS&
-&, ANE=ANE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, ADE=ADE, MDS=MDS, MNS=MNS&
+&, MNE=MNE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADO=ADO, ADS=ADS, ANS=ANS&
-&, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, ADE=ADE, MDS=MDS, MNS=MNS&
+&, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADO=ADO, ADS=ADS, ANS=ANS&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, ADE=ADE, MDS=MDS, MNS=MNS&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADO=ADO, ADS=ADS, ANS=ANS&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, ADE=ADE, MDS=MDS, MNS=MNS&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADO=ADO, ADS=ADS, ANS=ANS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, ADE=ADE, MDS=MDS, MNS=MNS&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADO=ADO, ADS=ADS, ANS=ANS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, ADE=ADE, MDS=MDS, MNS=MNS&
 &)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADO=ADO, ADS=ADS, ANE=ANE&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, ADE=ADE, MDS=MDS, MNE=MNE&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADO=ADO, ADS=ADS, ANE=ANE&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, ADE=ADE, MDS=MDS, MNE=MNE&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADO=ADO, ADS=ADS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, ADE=ADE, MDS=MDS, MNE=MNE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADO=ADO, ADS=ADS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, ADE=ADE, MDS=MDS, MNE=MNE&
 &)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADO=ADO, ADS=ADS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, ADE=ADE, MDS=MDS, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADO=ADO, ADS=ADS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, ADE=ADE, MDS=MDS, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADO=ADO, ADS=ADS, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, ADE=ADE, MDS=MDS, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADO=ADO, ADS=ADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, ADE=ADE, MDS=MDS)
                       END IF
                     END IF
                   END IF
                 END IF
               ELSE
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADO=ADO, ANS=ANS, ANE=ANE&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, ADE=ADE, MNS=MNS, MNE=MNE&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADO=ADO, ANS=ANS, ANE=ANE&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, ADE=ADE, MNS=MNS, MNE=MNE&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADO=ADO, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, ADE=ADE, MNS=MNS, MNE=MNE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADO=ADO, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, ADE=ADE, MNS=MNS, MNE=MNE&
 &)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADO=ADO, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, ADE=ADE, MNS=MNS, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADO=ADO, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, ADE=ADE, MNS=MNS, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADO=ADO, ANS=ANS, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, ADE=ADE, MNS=MNS, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADO=ADO, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, ADE=ADE, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADO=ADO, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, ADE=ADE, MNE=MNE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADO=ADO, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, ADE=ADE, MNE=MNE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADO=ADO, ANE=ANE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, ADE=ADE, MNE=MNE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADO=ADO, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, ADE=ADE, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADO=ADO, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, ADE=ADE, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADO=ADO, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, ADE=ADE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADO=ADO, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADO=ADO)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, ADE=ADE)
                       END IF
                     END IF
                   END IF
                 END IF
               END IF
             ELSE
-              IF (ADS_PRESENT) THEN
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+              IF (MDS_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADS=ADS, ANS=ANS, ANE=ANE&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, MDS=MDS, MNS=MNS, MNE=MNE&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADS=ADS, ANS=ANS, ANE=ANE&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, MDS=MDS, MNS=MNS, MNE=MNE&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADS=ADS, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, MDS=MDS, MNS=MNS, MNE=MNE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADS=ADS, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, MDS=MDS, MNS=MNS, MNE=MNE&
 &)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADS=ADS, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, MDS=MDS, MNS=MNS, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADS=ADS, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, MDS=MDS, MNS=MNS, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADS=ADS, ANS=ANS, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, MDS=MDS, MNS=MNS, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADS=ADS, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, MDS=MDS, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADS=ADS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, MDS=MDS, MNE=MNE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADS=ADS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, MDS=MDS, MNE=MNE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADS=ADS, ANE=ANE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, MDS=MDS, MNE=MNE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADS=ADS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, MDS=MDS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADS=ADS, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, MDS=MDS, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADS=ADS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, MDS=MDS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADS=ADS, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, MDS=MDS, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADS=ADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, MDS=MDS)
                       END IF
                     END IF
                   END IF
                 END IF
               ELSE
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ANS=ANS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, MNS=MNS, MNE=MNE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ANS=ANS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, MNS=MNS, MNE=MNE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ANS=ANS, ANE=ANE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, MNS=MNS, MNE=MNE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ANS=ANS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, MNS=MNS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ANS=ANS, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, MNS=MNS, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ANS=ANS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, MNS=MNS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ANS=ANS, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, MNS=MNS, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ANE=ANE, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, MNE=MNE, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ANE=ANE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, MNE=MNE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADE=ADE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, MDE=MDE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, MDE=MDE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ANE=ANE)
                       END IF
                     END IF
                   END IF
                 END IF
               END IF
             END IF
           ELSE
-            IF (ADO_PRESENT) THEN
-              IF (ADS_PRESENT) THEN
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+            IF (ADE_PRESENT) THEN
+              IF (MDS_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADE=ADE, MDS=MDS, MNS=MNS, MNE=MNE&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADE=ADE, MDS=MDS, MNS=MNS, MNE=MNE&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADE=ADE, MDS=MDS, MNS=MNS, MNE=MNE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADE=ADE, MDS=MDS, MNS=MNS, MNE=MNE&
 &)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADE=ADE, MDS=MDS, MNS=MNS, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADE=ADE, MDS=MDS, MNS=MNS, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADO=ADO, ADS=ADS, ANS=ANS, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADE=ADE, MDS=MDS, MNS=MNS, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADO=ADO, ADS=ADS, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADE=ADE, MDS=MDS, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADE=ADE, MDS=MDS, MNE=MNE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADE=ADE, MDS=MDS, MNE=MNE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADO=ADO, ADS=ADS, ANE=ANE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADE=ADE, MDS=MDS, MNE=MNE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADO=ADO, ADS=ADS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADE=ADE, MDS=MDS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADO=ADO, ADS=ADS, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADE=ADE, MDS=MDS, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADO=ADO, ADS=ADS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADE=ADE, MDS=MDS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADO=ADO, ADS=ADS, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADE=ADE, MDS=MDS, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADO=ADO, ADS=ADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADE=ADE, MDS=MDS)
                       END IF
                     END IF
                   END IF
                 END IF
               ELSE
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADE=ADE, MNS=MNS, MNE=MNE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADE=ADE, MNS=MNS, MNE=MNE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADO=ADO, ANS=ANS, ANE=ANE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADE=ADE, MNS=MNS, MNE=MNE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADO=ADO, ANS=ANS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADE=ADE, MNS=MNS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADO=ADO, ANS=ANS, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADE=ADE, MNS=MNS, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADO=ADO, ANS=ANS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADE=ADE, MNS=MNS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADO=ADO, ANS=ANS, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADE=ADE, MNS=MNS, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADO=ADO, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADE=ADE, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADO=ADO, ANE=ANE, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADE=ADE, MNE=MNE, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADO=ADO, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADE=ADE, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADO=ADO, ANE=ANE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADE=ADE, MNE=MNE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADO=ADO, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADE=ADE, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADO=ADO, ADE=ADE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADE=ADE, MDE=MDE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADO=ADO, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADE=ADE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADO=ADO, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADE=ADE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADO=ADO)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, ADE=ADE)
                       END IF
                     END IF
                   END IF
                 END IF
               END IF
             ELSE
-              IF (ADS_PRESENT) THEN
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+              IF (MDS_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADS=ADS, ANS=ANS, ANE=ANE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, MDS=MDS, MNS=MNS, MNE=MNE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADS=ADS, ANS=ANS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, MDS=MDS, MNS=MNS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADS=ADS, ANS=ANS, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, MDS=MDS, MNS=MNS, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADS=ADS, ANS=ANS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, MDS=MDS, MNS=MNS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADS=ADS, ANS=ANS, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, MDS=MDS, MNS=MNS, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADS=ADS, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, MDS=MDS, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADS=ADS, ANE=ANE, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, MDS=MDS, MNE=MNE, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADS=ADS, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, MDS=MDS, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADS=ADS, ANE=ANE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, MDS=MDS, MNE=MNE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADS=ADS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, MDS=MDS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADS=ADS, ADE=ADE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, MDS=MDS, MDE=MDE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADS=ADS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, MDS=MDS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADS=ADS, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, MDS=MDS, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADS=ADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, MDS=MDS)
                       END IF
                     END IF
                   END IF
                 END IF
               ELSE
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ANS=ANS, ANE=ANE, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, MNS=MNS, MNE=MNE, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ANS=ANS, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, MNS=MNS, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ANS=ANS, ANE=ANE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, MNS=MNS, MNE=MNE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ANS=ANS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, MNS=MNS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ANS=ANS, ADE=ADE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, MNS=MNS, MDE=MDE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ANS=ANS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, MNS=MNS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ANS=ANS, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, MNS=MNS, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ANE=ANE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, MNE=MNE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDS=MDS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADO=ADO)
                       END IF
                     END IF
                   END IF
                 END IF
               END IF
             END IF
           END IF
         END IF
       END IF
     ELSE
-      IF (MNS_PRESENT) THEN
-        IF (MNE_PRESENT) THEN
-          IF (MDE_PRESENT) THEN
-            IF (ADO_PRESENT) THEN
-              IF (ADS_PRESENT) THEN
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+      IF (ADS_PRESENT) THEN
+        IF (ANS_PRESENT) THEN
+          IF (ANE_PRESENT) THEN
+            IF (ADE_PRESENT) THEN
+              IF (MDS_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ANS=ANS, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MNS=MNS, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ANS=ANS, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MNS=MNS, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ANS=ANS, ANE=ANE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MNS=MNS, MNE=MNE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ANS=ANS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MNS=MNS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ANS=ANS, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MNS=MNS, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ANS=ANS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MNS=MNS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ANS=ANS, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MNS=MNS, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ANE=ANE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MNE=MNE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS&
 &)
                       END IF
                     END IF
                   END IF
                 END IF
               ELSE
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO, ANS=ANS&
-&, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE, MNS=MNS&
+&, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO, ANS=ANS&
-&, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE, MNS=MNS&
+&, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO, ANS=ANS&
-&, ANE=ANE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE, MNS=MNS&
+&, MNE=MNE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO, ANS=ANS&
-&, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE, MNS=MNS&
+&, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO, ANS=ANS&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE, MNS=MNS&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO, ANS=ANS&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE, MNS=MNS&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO, ANS=ANS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE, MNS=MNS&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO, ANS=ANS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE, MNS=MNS&
 &)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO, ANE=ANE&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE, MNE=MNE&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO, ANE=ANE&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE, MNE=MNE&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE, MNE=MNE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE, MNE=MNE&
 &)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADO=ADO)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE)
                       END IF
                     END IF
                   END IF
                 END IF
               END IF
             ELSE
-              IF (ADS_PRESENT) THEN
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+              IF (MDS_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADS=ADS, ANS=ANS&
-&, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, MDS=MDS, MNS=MNS&
+&, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADS=ADS, ANS=ANS&
-&, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, MDS=MDS, MNS=MNS&
+&, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADS=ADS, ANS=ANS&
-&, ANE=ANE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, MDS=MDS, MNS=MNS&
+&, MNE=MNE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADS=ADS, ANS=ANS&
-&, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, MDS=MDS, MNS=MNS&
+&, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADS=ADS, ANS=ANS&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, MDS=MDS, MNS=MNS&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADS=ADS, ANS=ANS&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, MDS=MDS, MNS=MNS&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADS=ADS, ANS=ANS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, MDS=MDS, MNS=MNS&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADS=ADS, ANS=ANS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, MDS=MDS, MNS=MNS&
 &)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADS=ADS, ANE=ANE&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, MDS=MDS, MNE=MNE&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADS=ADS, ANE=ANE&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, MDS=MDS, MNE=MNE&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADS=ADS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, MDS=MDS, MNE=MNE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADS=ADS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, MDS=MDS, MNE=MNE&
 &)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADS=ADS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, MDS=MDS, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADS=ADS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, MDS=MDS, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADS=ADS, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, MDS=MDS, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADS=ADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, MDS=MDS)
                       END IF
                     END IF
                   END IF
                 END IF
               ELSE
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ANS=ANS, ANE=ANE&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, MNS=MNS, MNE=MNE&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ANS=ANS, ANE=ANE&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, MNS=MNS, MNE=MNE&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, MNS=MNS, MNE=MNE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, MNS=MNS, MNE=MNE&
 &)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, MNS=MNS, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, MNS=MNS, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ANS=ANS, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, MNS=MNS, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, MNE=MNE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, MNE=MNE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ANE=ANE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, MNE=MNE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE)
                       END IF
                     END IF
                   END IF
                 END IF
               END IF
             END IF
           ELSE
-            IF (ADO_PRESENT) THEN
-              IF (ADS_PRESENT) THEN
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+            IF (ADE_PRESENT) THEN
+              IF (MDS_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADO=ADO, ADS=ADS, ANS=ANS&
-&, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ADE=ADE, MDS=MDS, MNS=MNS&
+&, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADO=ADO, ADS=ADS, ANS=ANS&
-&, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ADE=ADE, MDS=MDS, MNS=MNS&
+&, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADO=ADO, ADS=ADS, ANS=ANS&
-&, ANE=ANE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ADE=ADE, MDS=MDS, MNS=MNS&
+&, MNE=MNE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADO=ADO, ADS=ADS, ANS=ANS&
-&, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ADE=ADE, MDS=MDS, MNS=MNS&
+&, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADO=ADO, ADS=ADS, ANS=ANS&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ADE=ADE, MDS=MDS, MNS=MNS&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADO=ADO, ADS=ADS, ANS=ANS&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ADE=ADE, MDS=MDS, MNS=MNS&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADO=ADO, ADS=ADS, ANS=ANS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ADE=ADE, MDS=MDS, MNS=MNS&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADO=ADO, ADS=ADS, ANS=ANS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ADE=ADE, MDS=MDS, MNS=MNS&
 &)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADO=ADO, ADS=ADS, ANE=ANE&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ADE=ADE, MDS=MDS, MNE=MNE&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADO=ADO, ADS=ADS, ANE=ANE&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ADE=ADE, MDS=MDS, MNE=MNE&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADO=ADO, ADS=ADS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ADE=ADE, MDS=MDS, MNE=MNE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADO=ADO, ADS=ADS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ADE=ADE, MDS=MDS, MNE=MNE&
 &)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADO=ADO, ADS=ADS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ADE=ADE, MDS=MDS, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADO=ADO, ADS=ADS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ADE=ADE, MDS=MDS, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADO=ADO, ADS=ADS, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ADE=ADE, MDS=MDS, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADO=ADO, ADS=ADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ADE=ADE, MDS=MDS)
                       END IF
                     END IF
                   END IF
                 END IF
               ELSE
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADO=ADO, ANS=ANS, ANE=ANE&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ADE=ADE, MNS=MNS, MNE=MNE&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADO=ADO, ANS=ANS, ANE=ANE&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ADE=ADE, MNS=MNS, MNE=MNE&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADO=ADO, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ADE=ADE, MNS=MNS, MNE=MNE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADO=ADO, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ADE=ADE, MNS=MNS, MNE=MNE&
 &)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADO=ADO, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ADE=ADE, MNS=MNS, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADO=ADO, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ADE=ADE, MNS=MNS, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADO=ADO, ANS=ANS, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ADE=ADE, MNS=MNS, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADO=ADO, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ADE=ADE, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADO=ADO, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ADE=ADE, MNE=MNE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADO=ADO, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ADE=ADE, MNE=MNE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADO=ADO, ANE=ANE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ADE=ADE, MNE=MNE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADO=ADO, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ADE=ADE, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADO=ADO, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ADE=ADE, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADO=ADO, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ADE=ADE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADO=ADO, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ADE=ADE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADO=ADO)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ADE=ADE)
                       END IF
                     END IF
                   END IF
                 END IF
               END IF
             ELSE
-              IF (ADS_PRESENT) THEN
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+              IF (MDS_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADS=ADS, ANS=ANS, ANE=ANE&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, MDS=MDS, MNS=MNS, MNE=MNE&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADS=ADS, ANS=ANS, ANE=ANE&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, MDS=MDS, MNS=MNS, MNE=MNE&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADS=ADS, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, MDS=MDS, MNS=MNS, MNE=MNE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADS=ADS, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, MDS=MDS, MNS=MNS, MNE=MNE&
 &)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADS=ADS, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, MDS=MDS, MNS=MNS, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADS=ADS, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, MDS=MDS, MNS=MNS, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADS=ADS, ANS=ANS, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, MDS=MDS, MNS=MNS, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADS=ADS, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, MDS=MDS, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADS=ADS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, MDS=MDS, MNE=MNE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADS=ADS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, MDS=MDS, MNE=MNE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADS=ADS, ANE=ANE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, MDS=MDS, MNE=MNE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADS=ADS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, MDS=MDS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADS=ADS, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, MDS=MDS, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADS=ADS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, MDS=MDS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADS=ADS, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, MDS=MDS, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADS=ADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, MDS=MDS)
                       END IF
                     END IF
                   END IF
                 END IF
               ELSE
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ANS=ANS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, MNS=MNS, MNE=MNE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ANS=ANS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, MNS=MNS, MNE=MNE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ANS=ANS, ANE=ANE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, MNS=MNS, MNE=MNE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ANS=ANS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, MNS=MNS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ANS=ANS, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, MNS=MNS, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ANS=ANS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, MNS=MNS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ANS=ANS, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, MNS=MNS, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ANE=ANE, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, MNE=MNE, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ANE=ANE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, MNE=MNE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADE=ADE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, MDE=MDE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MNE=MNE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANS=ANS)
                       END IF
                     END IF
                   END IF
                 END IF
               END IF
             END IF
           END IF
         ELSE
-          IF (MDE_PRESENT) THEN
-            IF (ADO_PRESENT) THEN
-              IF (ADS_PRESENT) THEN
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+          IF (ANE_PRESENT) THEN
+            IF (ADE_PRESENT) THEN
+              IF (MDS_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADO=ADO, ADS=ADS, ANS=ANS&
-&, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, ADE=ADE, MDS=MDS, MNS=MNS&
+&, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADO=ADO, ADS=ADS, ANS=ANS&
-&, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, ADE=ADE, MDS=MDS, MNS=MNS&
+&, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADO=ADO, ADS=ADS, ANS=ANS&
-&, ANE=ANE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, ADE=ADE, MDS=MDS, MNS=MNS&
+&, MNE=MNE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADO=ADO, ADS=ADS, ANS=ANS&
-&, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, ADE=ADE, MDS=MDS, MNS=MNS&
+&, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADO=ADO, ADS=ADS, ANS=ANS&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, ADE=ADE, MDS=MDS, MNS=MNS&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADO=ADO, ADS=ADS, ANS=ANS&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, ADE=ADE, MDS=MDS, MNS=MNS&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADO=ADO, ADS=ADS, ANS=ANS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, ADE=ADE, MDS=MDS, MNS=MNS&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADO=ADO, ADS=ADS, ANS=ANS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, ADE=ADE, MDS=MDS, MNS=MNS&
 &)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADO=ADO, ADS=ADS, ANE=ANE&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, ADE=ADE, MDS=MDS, MNE=MNE&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADO=ADO, ADS=ADS, ANE=ANE&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, ADE=ADE, MDS=MDS, MNE=MNE&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADO=ADO, ADS=ADS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, ADE=ADE, MDS=MDS, MNE=MNE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADO=ADO, ADS=ADS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, ADE=ADE, MDS=MDS, MNE=MNE&
 &)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADO=ADO, ADS=ADS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, ADE=ADE, MDS=MDS, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADO=ADO, ADS=ADS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, ADE=ADE, MDS=MDS, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADO=ADO, ADS=ADS, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, ADE=ADE, MDS=MDS, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADO=ADO, ADS=ADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, ADE=ADE, MDS=MDS)
                       END IF
                     END IF
                   END IF
                 END IF
               ELSE
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADO=ADO, ANS=ANS, ANE=ANE&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, ADE=ADE, MNS=MNS, MNE=MNE&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADO=ADO, ANS=ANS, ANE=ANE&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, ADE=ADE, MNS=MNS, MNE=MNE&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADO=ADO, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, ADE=ADE, MNS=MNS, MNE=MNE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADO=ADO, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, ADE=ADE, MNS=MNS, MNE=MNE&
 &)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADO=ADO, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, ADE=ADE, MNS=MNS, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADO=ADO, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, ADE=ADE, MNS=MNS, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADO=ADO, ANS=ANS, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, ADE=ADE, MNS=MNS, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADO=ADO, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, ADE=ADE, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADO=ADO, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, ADE=ADE, MNE=MNE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADO=ADO, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, ADE=ADE, MNE=MNE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADO=ADO, ANE=ANE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, ADE=ADE, MNE=MNE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADO=ADO, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, ADE=ADE, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADO=ADO, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, ADE=ADE, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADO=ADO, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, ADE=ADE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADO=ADO, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADO=ADO)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, ADE=ADE)
                       END IF
                     END IF
                   END IF
                 END IF
               END IF
             ELSE
-              IF (ADS_PRESENT) THEN
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+              IF (MDS_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADS=ADS, ANS=ANS, ANE=ANE&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, MDS=MDS, MNS=MNS, MNE=MNE&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADS=ADS, ANS=ANS, ANE=ANE&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, MDS=MDS, MNS=MNS, MNE=MNE&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADS=ADS, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, MDS=MDS, MNS=MNS, MNE=MNE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADS=ADS, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, MDS=MDS, MNS=MNS, MNE=MNE&
 &)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADS=ADS, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, MDS=MDS, MNS=MNS, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADS=ADS, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, MDS=MDS, MNS=MNS, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADS=ADS, ANS=ANS, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, MDS=MDS, MNS=MNS, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADS=ADS, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, MDS=MDS, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADS=ADS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, MDS=MDS, MNE=MNE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADS=ADS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, MDS=MDS, MNE=MNE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADS=ADS, ANE=ANE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, MDS=MDS, MNE=MNE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADS=ADS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, MDS=MDS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADS=ADS, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, MDS=MDS, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADS=ADS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, MDS=MDS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADS=ADS, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, MDS=MDS, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADS=ADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, MDS=MDS)
                       END IF
                     END IF
                   END IF
                 END IF
               ELSE
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ANS=ANS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, MNS=MNS, MNE=MNE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ANS=ANS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, MNS=MNS, MNE=MNE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ANS=ANS, ANE=ANE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, MNS=MNS, MNE=MNE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ANS=ANS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, MNS=MNS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ANS=ANS, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, MNS=MNS, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ANS=ANS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, MNS=MNS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ANS=ANS, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, MNS=MNS, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ANE=ANE, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, MNE=MNE, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ANE=ANE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, MNE=MNE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADE=ADE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, MDE=MDE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, MDE=MDE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ANE=ANE)
                       END IF
                     END IF
                   END IF
                 END IF
               END IF
             END IF
           ELSE
-            IF (ADO_PRESENT) THEN
-              IF (ADS_PRESENT) THEN
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+            IF (ADE_PRESENT) THEN
+              IF (MDS_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ADE=ADE, MDS=MDS, MNS=MNS, MNE=MNE&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ADE=ADE, MDS=MDS, MNS=MNS, MNE=MNE&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ADE=ADE, MDS=MDS, MNS=MNS, MNE=MNE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ADE=ADE, MDS=MDS, MNS=MNS, MNE=MNE&
 &)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ADE=ADE, MDS=MDS, MNS=MNS, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ADE=ADE, MDS=MDS, MNS=MNS, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADO=ADO, ADS=ADS, ANS=ANS, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ADE=ADE, MDS=MDS, MNS=MNS, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADO=ADO, ADS=ADS, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ADE=ADE, MDS=MDS, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ADE=ADE, MDS=MDS, MNE=MNE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ADE=ADE, MDS=MDS, MNE=MNE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADO=ADO, ADS=ADS, ANE=ANE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ADE=ADE, MDS=MDS, MNE=MNE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADO=ADO, ADS=ADS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ADE=ADE, MDS=MDS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADO=ADO, ADS=ADS, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ADE=ADE, MDS=MDS, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADO=ADO, ADS=ADS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ADE=ADE, MDS=MDS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADO=ADO, ADS=ADS, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ADE=ADE, MDS=MDS, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADO=ADO, ADS=ADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ADE=ADE, MDS=MDS)
                       END IF
                     END IF
                   END IF
                 END IF
               ELSE
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ADE=ADE, MNS=MNS, MNE=MNE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ADE=ADE, MNS=MNS, MNE=MNE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADO=ADO, ANS=ANS, ANE=ANE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ADE=ADE, MNS=MNS, MNE=MNE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADO=ADO, ANS=ANS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ADE=ADE, MNS=MNS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADO=ADO, ANS=ANS, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ADE=ADE, MNS=MNS, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADO=ADO, ANS=ANS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ADE=ADE, MNS=MNS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADO=ADO, ANS=ANS, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ADE=ADE, MNS=MNS, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADO=ADO, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ADE=ADE, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADO=ADO, ANE=ANE, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ADE=ADE, MNE=MNE, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADO=ADO, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ADE=ADE, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADO=ADO, ANE=ANE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ADE=ADE, MNE=MNE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADO=ADO, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ADE=ADE, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADO=ADO, ADE=ADE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ADE=ADE, MDE=MDE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADO=ADO, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ADE=ADE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADO=ADO, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ADE=ADE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADO=ADO)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, ADE=ADE)
                       END IF
                     END IF
                   END IF
                 END IF
               END IF
             ELSE
-              IF (ADS_PRESENT) THEN
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+              IF (MDS_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADS=ADS, ANS=ANS, ANE=ANE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, MDS=MDS, MNS=MNS, MNE=MNE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADS=ADS, ANS=ANS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, MDS=MDS, MNS=MNS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADS=ADS, ANS=ANS, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, MDS=MDS, MNS=MNS, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADS=ADS, ANS=ANS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, MDS=MDS, MNS=MNS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADS=ADS, ANS=ANS, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, MDS=MDS, MNS=MNS, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADS=ADS, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, MDS=MDS, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADS=ADS, ANE=ANE, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, MDS=MDS, MNE=MNE, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADS=ADS, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, MDS=MDS, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADS=ADS, ANE=ANE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, MDS=MDS, MNE=MNE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADS=ADS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, MDS=MDS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADS=ADS, ADE=ADE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, MDS=MDS, MDE=MDE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADS=ADS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, MDS=MDS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADS=ADS, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, MDS=MDS, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADS=ADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, MDS=MDS)
                       END IF
                     END IF
                   END IF
                 END IF
               ELSE
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ANS=ANS, ANE=ANE, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, MNS=MNS, MNE=MNE, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ANS=ANS, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, MNS=MNS, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ANS=ANS, ANE=ANE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, MNS=MNS, MNE=MNE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ANS=ANS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, MNS=MNS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ANS=ANS, ADE=ADE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, MNS=MNS, MDE=MDE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ANS=ANS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, MNS=MNS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ANS=ANS, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, MNS=MNS, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ANE=ANE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, MNE=MNE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNS=MNS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADS=ADS)
                       END IF
                     END IF
                   END IF
                 END IF
               END IF
             END IF
           END IF
         END IF
       ELSE
-        IF (MNE_PRESENT) THEN
-          IF (MDE_PRESENT) THEN
-            IF (ADO_PRESENT) THEN
-              IF (ADS_PRESENT) THEN
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+        IF (ANS_PRESENT) THEN
+          IF (ANE_PRESENT) THEN
+            IF (ADE_PRESENT) THEN
+              IF (MDS_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS, ANS=ANS&
-&, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS, MNS=MNS&
+&, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS, ANS=ANS&
-&, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS, MNS=MNS&
+&, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS, ANS=ANS&
-&, ANE=ANE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS, MNS=MNS&
+&, MNE=MNE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS, ANS=ANS&
-&, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS, MNS=MNS&
+&, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS, ANS=ANS&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS, MNS=MNS&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS, ANS=ANS&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS, MNS=MNS&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS, ANS=ANS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS, MNS=MNS&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS, ANS=ANS&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS, MNS=MNS&
 &)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS, ANE=ANE&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS, MNE=MNE&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS, ANE=ANE&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS, MNE=MNE&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS, MNE=MNE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS, MNE=MNE&
 &)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADO=ADO, ADS=ADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, ADE=ADE, MDS=MDS)
                       END IF
                     END IF
                   END IF
                 END IF
               ELSE
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADO=ADO, ANS=ANS, ANE=ANE&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, ADE=ADE, MNS=MNS, MNE=MNE&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADO=ADO, ANS=ANS, ANE=ANE&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, ADE=ADE, MNS=MNS, MNE=MNE&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADO=ADO, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, ADE=ADE, MNS=MNS, MNE=MNE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADO=ADO, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, ADE=ADE, MNS=MNS, MNE=MNE&
 &)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADO=ADO, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, ADE=ADE, MNS=MNS, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADO=ADO, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, ADE=ADE, MNS=MNS, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADO=ADO, ANS=ANS, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, ADE=ADE, MNS=MNS, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADO=ADO, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, ADE=ADE, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADO=ADO, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, ADE=ADE, MNE=MNE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADO=ADO, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, ADE=ADE, MNE=MNE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADO=ADO, ANE=ANE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, ADE=ADE, MNE=MNE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADO=ADO, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, ADE=ADE, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADO=ADO, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, ADE=ADE, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADO=ADO, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, ADE=ADE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADO=ADO, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADO=ADO)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, ADE=ADE)
                       END IF
                     END IF
                   END IF
                 END IF
               END IF
             ELSE
-              IF (ADS_PRESENT) THEN
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+              IF (MDS_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADS=ADS, ANS=ANS, ANE=ANE&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, MDS=MDS, MNS=MNS, MNE=MNE&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADS=ADS, ANS=ANS, ANE=ANE&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, MDS=MDS, MNS=MNS, MNE=MNE&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADS=ADS, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, MDS=MDS, MNS=MNS, MNE=MNE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADS=ADS, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, MDS=MDS, MNS=MNS, MNE=MNE&
 &)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADS=ADS, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, MDS=MDS, MNS=MNS, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADS=ADS, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, MDS=MDS, MNS=MNS, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADS=ADS, ANS=ANS, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, MDS=MDS, MNS=MNS, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADS=ADS, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, MDS=MDS, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADS=ADS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, MDS=MDS, MNE=MNE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADS=ADS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, MDS=MDS, MNE=MNE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADS=ADS, ANE=ANE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, MDS=MDS, MNE=MNE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADS=ADS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, MDS=MDS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADS=ADS, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, MDS=MDS, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADS=ADS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, MDS=MDS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADS=ADS, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, MDS=MDS, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADS=ADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, MDS=MDS)
                       END IF
                     END IF
                   END IF
                 END IF
               ELSE
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ANS=ANS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, MNS=MNS, MNE=MNE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ANS=ANS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, MNS=MNS, MNE=MNE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ANS=ANS, ANE=ANE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, MNS=MNS, MNE=MNE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ANS=ANS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, MNS=MNS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ANS=ANS, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, MNS=MNS, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ANS=ANS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, MNS=MNS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ANS=ANS, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, MNS=MNS, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ANE=ANE, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, MNE=MNE, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ANE=ANE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, MNE=MNE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADE=ADE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, MDE=MDE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, MDE=MDE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ANE=ANE)
                       END IF
                     END IF
                   END IF
                 END IF
               END IF
             END IF
           ELSE
-            IF (ADO_PRESENT) THEN
-              IF (ADS_PRESENT) THEN
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+            IF (ADE_PRESENT) THEN
+              IF (MDS_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ADE=ADE, MDS=MDS, MNS=MNS, MNE=MNE&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ADE=ADE, MDS=MDS, MNS=MNS, MNE=MNE&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ADE=ADE, MDS=MDS, MNS=MNS, MNE=MNE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ADE=ADE, MDS=MDS, MNS=MNS, MNE=MNE&
 &)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ADE=ADE, MDS=MDS, MNS=MNS, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ADE=ADE, MDS=MDS, MNS=MNS, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADO=ADO, ADS=ADS, ANS=ANS, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ADE=ADE, MDS=MDS, MNS=MNS, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADO=ADO, ADS=ADS, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ADE=ADE, MDS=MDS, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ADE=ADE, MDS=MDS, MNE=MNE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ADE=ADE, MDS=MDS, MNE=MNE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADO=ADO, ADS=ADS, ANE=ANE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ADE=ADE, MDS=MDS, MNE=MNE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADO=ADO, ADS=ADS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ADE=ADE, MDS=MDS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADO=ADO, ADS=ADS, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ADE=ADE, MDS=MDS, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADO=ADO, ADS=ADS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ADE=ADE, MDS=MDS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADO=ADO, ADS=ADS, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ADE=ADE, MDS=MDS, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADO=ADO, ADS=ADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ADE=ADE, MDS=MDS)
                       END IF
                     END IF
                   END IF
                 END IF
               ELSE
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ADE=ADE, MNS=MNS, MNE=MNE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ADE=ADE, MNS=MNS, MNE=MNE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADO=ADO, ANS=ANS, ANE=ANE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ADE=ADE, MNS=MNS, MNE=MNE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADO=ADO, ANS=ANS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ADE=ADE, MNS=MNS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADO=ADO, ANS=ANS, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ADE=ADE, MNS=MNS, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADO=ADO, ANS=ANS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ADE=ADE, MNS=MNS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADO=ADO, ANS=ANS, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ADE=ADE, MNS=MNS, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADO=ADO, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ADE=ADE, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADO=ADO, ANE=ANE, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ADE=ADE, MNE=MNE, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADO=ADO, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ADE=ADE, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADO=ADO, ANE=ANE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ADE=ADE, MNE=MNE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADO=ADO, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ADE=ADE, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADO=ADO, ADE=ADE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ADE=ADE, MDE=MDE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADO=ADO, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ADE=ADE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADO=ADO, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ADE=ADE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADO=ADO)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, ADE=ADE)
                       END IF
                     END IF
                   END IF
                 END IF
               END IF
             ELSE
-              IF (ADS_PRESENT) THEN
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+              IF (MDS_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADS=ADS, ANS=ANS, ANE=ANE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, MDS=MDS, MNS=MNS, MNE=MNE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADS=ADS, ANS=ANS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, MDS=MDS, MNS=MNS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADS=ADS, ANS=ANS, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, MDS=MDS, MNS=MNS, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADS=ADS, ANS=ANS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, MDS=MDS, MNS=MNS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADS=ADS, ANS=ANS, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, MDS=MDS, MNS=MNS, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADS=ADS, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, MDS=MDS, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADS=ADS, ANE=ANE, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, MDS=MDS, MNE=MNE, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADS=ADS, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, MDS=MDS, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADS=ADS, ANE=ANE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, MDS=MDS, MNE=MNE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADS=ADS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, MDS=MDS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADS=ADS, ADE=ADE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, MDS=MDS, MDE=MDE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADS=ADS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, MDS=MDS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADS=ADS, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, MDS=MDS, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADS=ADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, MDS=MDS)
                       END IF
                     END IF
                   END IF
                 END IF
               ELSE
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ANS=ANS, ANE=ANE, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, MNS=MNS, MNE=MNE, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ANS=ANS, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, MNS=MNS, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ANS=ANS, ANE=ANE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, MNS=MNS, MNE=MNE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ANS=ANS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, MNS=MNS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ANS=ANS, ADE=ADE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, MNS=MNS, MDE=MDE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ANS=ANS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, MNS=MNS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ANS=ANS, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, MNS=MNS, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ANE=ANE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, MNE=MNE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MNE=MNE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANS=ANS)
                       END IF
                     END IF
                   END IF
                 END IF
               END IF
             END IF
           END IF
         ELSE
-          IF (MDE_PRESENT) THEN
-            IF (ADO_PRESENT) THEN
-              IF (ADS_PRESENT) THEN
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+          IF (ANE_PRESENT) THEN
+            IF (ADE_PRESENT) THEN
+              IF (MDS_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE&
-&, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, ADE=ADE, MDS=MDS, MNS=MNS, MNE=MNE&
+&, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE&
-&, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, ADE=ADE, MDS=MDS, MNS=MNS, MNE=MNE&
+&, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, ADE=ADE, MDS=MDS, MNS=MNS, MNE=MNE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, ADE=ADE, MDS=MDS, MNS=MNS, MNE=MNE&
 &)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, ADE=ADE, MDS=MDS, MNS=MNS, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, ADE=ADE, MDS=MDS, MNS=MNS, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADO=ADO, ADS=ADS, ANS=ANS, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, ADE=ADE, MDS=MDS, MNS=MNS, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADO=ADO, ADS=ADS, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, ADE=ADE, MDS=MDS, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, ADE=ADE, MDS=MDS, MNE=MNE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, ADE=ADE, MDS=MDS, MNE=MNE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADO=ADO, ADS=ADS, ANE=ANE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, ADE=ADE, MDS=MDS, MNE=MNE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADO=ADO, ADS=ADS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, ADE=ADE, MDS=MDS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADO=ADO, ADS=ADS, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, ADE=ADE, MDS=MDS, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADO=ADO, ADS=ADS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, ADE=ADE, MDS=MDS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADO=ADO, ADS=ADS, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, ADE=ADE, MDS=MDS, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADO=ADO, ADS=ADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, ADE=ADE, MDS=MDS)
                       END IF
                     END IF
                   END IF
                 END IF
               ELSE
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, ADE=ADE, MNS=MNS, MNE=MNE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, ADE=ADE, MNS=MNS, MNE=MNE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADO=ADO, ANS=ANS, ANE=ANE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, ADE=ADE, MNS=MNS, MNE=MNE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADO=ADO, ANS=ANS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, ADE=ADE, MNS=MNS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADO=ADO, ANS=ANS, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, ADE=ADE, MNS=MNS, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADO=ADO, ANS=ANS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, ADE=ADE, MNS=MNS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADO=ADO, ANS=ANS, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, ADE=ADE, MNS=MNS, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADO=ADO, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, ADE=ADE, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADO=ADO, ANE=ANE, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, ADE=ADE, MNE=MNE, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADO=ADO, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, ADE=ADE, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADO=ADO, ANE=ANE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, ADE=ADE, MNE=MNE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADO=ADO, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, ADE=ADE, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADO=ADO, ADE=ADE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, ADE=ADE, MDE=MDE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADO=ADO, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, ADE=ADE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADO=ADO, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADO=ADO)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, ADE=ADE)
                       END IF
                     END IF
                   END IF
                 END IF
               END IF
             ELSE
-              IF (ADS_PRESENT) THEN
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+              IF (MDS_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADS=ADS, ANS=ANS, ANE=ANE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, MDS=MDS, MNS=MNS, MNE=MNE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADS=ADS, ANS=ANS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, MDS=MDS, MNS=MNS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADS=ADS, ANS=ANS, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, MDS=MDS, MNS=MNS, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADS=ADS, ANS=ANS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, MDS=MDS, MNS=MNS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADS=ADS, ANS=ANS, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, MDS=MDS, MNS=MNS, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADS=ADS, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, MDS=MDS, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADS=ADS, ANE=ANE, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, MDS=MDS, MNE=MNE, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADS=ADS, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, MDS=MDS, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADS=ADS, ANE=ANE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, MDS=MDS, MNE=MNE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADS=ADS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, MDS=MDS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADS=ADS, ADE=ADE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, MDS=MDS, MDE=MDE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADS=ADS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, MDS=MDS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADS=ADS, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, MDS=MDS, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADS=ADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, MDS=MDS)
                       END IF
                     END IF
                   END IF
                 END IF
               ELSE
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ANS=ANS, ANE=ANE, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, MNS=MNS, MNE=MNE, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ANS=ANS, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, MNS=MNS, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ANS=ANS, ANE=ANE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, MNS=MNS, MNE=MNE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ANS=ANS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, MNS=MNS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ANS=ANS, ADE=ADE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, MNS=MNS, MDE=MDE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ANS=ANS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, MNS=MNS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ANS=ANS, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, MNS=MNS, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ANE=ANE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, MNE=MNE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, MDE=MDE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ANE=ANE)
                       END IF
                     END IF
                   END IF
                 END IF
               END IF
             END IF
           ELSE
-            IF (ADO_PRESENT) THEN
-              IF (ADS_PRESENT) THEN
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+            IF (ADE_PRESENT) THEN
+              IF (MDS_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADE=ADE, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE&
 &, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADE=ADE, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE&
 &)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADE=ADE, MDS=MDS, MNS=MNS, MNE=MNE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADE=ADE, MDS=MDS, MNS=MNS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADE=ADE, MDS=MDS, MNS=MNS, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADE=ADE, MDS=MDS, MNS=MNS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADE=ADE, MDS=MDS, MNS=MNS, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADE=ADE, MDS=MDS, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADE=ADE, MDS=MDS, MNE=MNE, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADE=ADE, MDS=MDS, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADE=ADE, MDS=MDS, MNE=MNE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADE=ADE, MDS=MDS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ADE=ADE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADE=ADE, MDS=MDS, MDE=MDE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADO=ADO, ADS=ADS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADE=ADE, MDS=MDS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADO=ADO, ADS=ADS, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADE=ADE, MDS=MDS, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADO=ADO, ADS=ADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADE=ADE, MDS=MDS)
                       END IF
                     END IF
                   END IF
                 END IF
               ELSE
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADE=ADE, MNS=MNS, MNE=MNE, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADE=ADE, MNS=MNS, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADE=ADE, MNS=MNS, MNE=MNE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADE=ADE, MNS=MNS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ADE=ADE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADE=ADE, MNS=MNS, MDE=MDE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADO=ADO, ANS=ANS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADE=ADE, MNS=MNS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADO=ADO, ANS=ANS, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADE=ADE, MNS=MNS, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADO=ADO, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADE=ADE, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADO=ADO, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADE=ADE, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADO=ADO, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADE=ADE, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADO=ADO, ANE=ANE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADE=ADE, MNE=MNE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADO=ADO, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADE=ADE, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADO=ADO, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADE=ADE, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADO=ADO, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADE=ADE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADO=ADO, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADE=ADE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADO=ADO)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, ADE=ADE)
                       END IF
                     END IF
                   END IF
                 END IF
               END IF
             ELSE
-              IF (ADS_PRESENT) THEN
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+              IF (MDS_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE, NUM_THR&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE, NUM_THR&
 &EADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ADE=ADE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADS=ADS, ANS=ANS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, MDS=MDS, MNS=MNS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADS=ADS, ANS=ANS, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, MDS=MDS, MNS=MNS, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADS=ADS, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, MDS=MDS, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADS=ADS, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADS=ADS, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, MDS=MDS, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADS=ADS, ANE=ANE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, MDS=MDS, MNE=MNE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADS=ADS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, MDS=MDS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADS=ADS, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, MDS=MDS, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADS=ADS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, MDS=MDS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADS=ADS, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, MDS=MDS, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADS=ADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, MDS=MDS)
                       END IF
                     END IF
                   END IF
                 END IF
               ELSE
-                IF (ANS_PRESENT) THEN
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                IF (MNS_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ANS=ANS, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_&
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_&
 &THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ANS=ANS, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, MNS=MNS, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ANS=ANS, ANE=ANE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, MNS=MNS, MNE=MNE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ANS=ANS, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, MNS=MNS, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ANS=ANS, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, MNS=MNS, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ANS=ANS, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, MNS=MNS, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ANS=ANS, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, MNS=MNS, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ANS=ANS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, MNS=MNS)
                       END IF
                     END IF
                   END IF
                 ELSE
-                  IF (ANE_PRESENT) THEN
-                    IF (ADE_PRESENT) THEN
+                  IF (MNE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ANE=ANE, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, MNE=MNE, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ANE=ANE, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, MNE=MNE, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ANE=ANE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, MNE=MNE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ANE=ANE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, MNE=MNE)
                       END IF
                     END IF
                   ELSE
-                    IF (ADE_PRESENT) THEN
+                    IF (MDE_PRESENT) THEN
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADE=ADE, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, MDE=MDE, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, ADE=ADE)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, MDE=MDE)
                       END IF
                     ELSE
                       IF (NUM_THREADS_PRESENT) THEN
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG, NUM_THREADS=NUM_THREADS)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG, NUM_THREADS=NUM_THREADS)
                       ELSE
-                        CALL NEW_MODEL_CONFIG(MDI=MDI, MDO=MDO, ADI=ADI, CONFIG=CONFIG)
+                        CALL NEW_MODEL_CONFIG(ADN=ADN, MDN=MDN, MDO=MDO, CONFIG=CONFIG)
                       END IF
                     END IF
                   END IF
                 END IF
               END IF
             END IF
           END IF
         END IF
       END IF
     END IF
   END SUBROUTINE C_NEW_MODEL_CONFIG
   
 
   
+  SUBROUTINE C_NEW_FIT_CONFIG(NM, NA, CONFIG) BIND(C)
+    USE APOS, ONLY: NEW_FIT_CONFIG
+    USE APOS, ONLY: MODEL_CONFIG
+    IMPLICIT NONE
+    INTEGER, INTENT(IN) :: NM
+    INTEGER, INTENT(IN) :: NA
+    TYPE(MODEL_CONFIG), INTENT(INOUT) :: CONFIG
+  
+    CALL NEW_FIT_CONFIG(NM, NA, CONFIG)
+  END SUBROUTINE C_NEW_FIT_CONFIG
+  
+
+  
   SUBROUTINE C_INIT_MODEL(CONFIG, MODEL_DIM_1, MODEL, SEED_PRESENT, SEED) BIND(C)
     USE APOS, ONLY: INIT_MODEL
     USE APOS, ONLY: MODEL_CONFIG
     IMPLICIT NONE
     TYPE(MODEL_CONFIG), INTENT(IN) :: CONFIG
     INTEGER, INTENT(IN) :: MODEL_DIM_1
     REAL(KIND=RT), INTENT(INOUT), DIMENSION(MODEL_DIM_1) :: MODEL
@@ -4947,165 +5206,137 @@
     ELSE
       CALL INIT_MODEL(CONFIG=CONFIG, MODEL=MODEL)
     END IF
   END SUBROUTINE C_INIT_MODEL
   
 
   
-  SUBROUTINE C_CHECK_SHAPE(CONFIG, MODEL_DIM_1, MODEL, Y_DIM_1, Y_DIM_2, Y, X_DIM_1, X_DIM_2, X, XI_DIM_1, XI_DIM_2, XI, AX_DIM_1, &
-&AX_DIM_2, AX, AXI_DIM_1, AXI_DIM_2, AXI, SIZES_DIM_1, SIZES, INFO) BIND(C)
+  SUBROUTINE C_CHECK_SHAPE(CONFIG, MODEL_DIM_1, MODEL, AX_DIM_1, AX_DIM_2, AX, AXI_DIM_1, AXI_DIM_2, AXI, SIZES_DIM_1, SIZES, X_DIM&
+&_1, X_DIM_2, X, XI_DIM_1, XI_DIM_2, XI, Y_DIM_1, Y_DIM_2, Y, INFO) BIND(C)
     USE APOS, ONLY: CHECK_SHAPE
     USE APOS, ONLY: MODEL_CONFIG
     IMPLICIT NONE
     TYPE(MODEL_CONFIG), INTENT(IN) :: CONFIG
     INTEGER, INTENT(IN) :: MODEL_DIM_1
     REAL(KIND=RT), INTENT(IN), DIMENSION(MODEL_DIM_1) :: MODEL
-    INTEGER, INTENT(IN) :: Y_DIM_1
-    INTEGER, INTENT(IN) :: Y_DIM_2
-    REAL(KIND=RT), INTENT(IN), DIMENSION(Y_DIM_1,Y_DIM_2) :: Y
-    INTEGER, INTENT(IN) :: X_DIM_1
-    INTEGER, INTENT(IN) :: X_DIM_2
-    REAL(KIND=RT), INTENT(IN), DIMENSION(X_DIM_1,X_DIM_2) :: X
-    INTEGER, INTENT(IN) :: XI_DIM_1
-    INTEGER, INTENT(IN) :: XI_DIM_2
-    INTEGER, INTENT(IN), DIMENSION(XI_DIM_1,XI_DIM_2) :: XI
     INTEGER, INTENT(IN) :: AX_DIM_1
     INTEGER, INTENT(IN) :: AX_DIM_2
     REAL(KIND=RT), INTENT(IN), DIMENSION(AX_DIM_1,AX_DIM_2) :: AX
     INTEGER, INTENT(IN) :: AXI_DIM_1
     INTEGER, INTENT(IN) :: AXI_DIM_2
     INTEGER, INTENT(IN), DIMENSION(AXI_DIM_1,AXI_DIM_2) :: AXI
     INTEGER, INTENT(IN) :: SIZES_DIM_1
     INTEGER, INTENT(IN), DIMENSION(SIZES_DIM_1) :: SIZES
+    INTEGER, INTENT(IN) :: X_DIM_1
+    INTEGER, INTENT(IN) :: X_DIM_2
+    REAL(KIND=RT), INTENT(IN), DIMENSION(X_DIM_1,X_DIM_2) :: X
+    INTEGER, INTENT(IN) :: XI_DIM_1
+    INTEGER, INTENT(IN) :: XI_DIM_2
+    INTEGER, INTENT(IN), DIMENSION(XI_DIM_1,XI_DIM_2) :: XI
+    INTEGER, INTENT(IN) :: Y_DIM_1
+    INTEGER, INTENT(IN) :: Y_DIM_2
+    REAL(KIND=RT), INTENT(IN), DIMENSION(Y_DIM_1,Y_DIM_2) :: Y
     INTEGER, INTENT(OUT) :: INFO
   
-    CALL CHECK_SHAPE(CONFIG, MODEL, Y, X, XI, AX, AXI, SIZES, INFO)
+    CALL CHECK_SHAPE(CONFIG, MODEL, AX, AXI, SIZES, X, XI, Y, INFO)
   END SUBROUTINE C_CHECK_SHAPE
   
 
   
-  SUBROUTINE C_EMBED(CONFIG, MODEL_DIM_1, MODEL, X_DIM_1, X_DIM_2, X, XI_DIM_1, XI_DIM_2, XI, AX_DIM_1, AX_DIM_2, AX, AXI_DIM_1, AX&
-&I_DIM_2, AXI, XXI_DIM_1, XXI_DIM_2, XXI, AXXI_DIM_1, AXXI_DIM_2, AXXI) BIND(C)
+  SUBROUTINE C_COMPUTE_BATCHES(NUM_BATCHES, NM, NA, SIZES_DIM_1, SIZES, BATCHA_STARTS_DIM_1, BATCHA_STARTS, BATCHA_ENDS_DIM_1, BATC&
+&HA_ENDS, BATCHM_STARTS_DIM_1, BATCHM_STARTS, BATCHM_ENDS_DIM_1, BATCHM_ENDS, INFO) BIND(C)
+    USE APOS, ONLY: COMPUTE_BATCHES
+    IMPLICIT NONE
+    INTEGER, INTENT(IN) :: NUM_BATCHES
+    INTEGER, INTENT(IN) :: NM
+    INTEGER, INTENT(IN) :: NA
+    INTEGER, INTENT(IN) :: SIZES_DIM_1
+    INTEGER, INTENT(IN), DIMENSION(SIZES_DIM_1) :: SIZES
+    INTEGER, INTENT(IN) :: BATCHA_STARTS_DIM_1
+    INTEGER, INTENT(OUT), DIMENSION(BATCHA_STARTS_DIM_1) :: BATCHA_STARTS
+    INTEGER, INTENT(IN) :: BATCHA_ENDS_DIM_1
+    INTEGER, INTENT(OUT), DIMENSION(BATCHA_ENDS_DIM_1) :: BATCHA_ENDS
+    INTEGER, INTENT(IN) :: BATCHM_STARTS_DIM_1
+    INTEGER, INTENT(OUT), DIMENSION(BATCHM_STARTS_DIM_1) :: BATCHM_STARTS
+    INTEGER, INTENT(IN) :: BATCHM_ENDS_DIM_1
+    INTEGER, INTENT(OUT), DIMENSION(BATCHM_ENDS_DIM_1) :: BATCHM_ENDS
+    INTEGER, INTENT(INOUT) :: INFO
+  
+    CALL COMPUTE_BATCHES(NUM_BATCHES, NM, NA, SIZES, BATCHA_STARTS, BATCHA_ENDS, BATCHM_STARTS, BATCHM_ENDS, INFO)
+  END SUBROUTINE C_COMPUTE_BATCHES
+  
+
+  
+  SUBROUTINE C_EMBED(CONFIG, MODEL_DIM_1, MODEL, AXI_DIM_1, AXI_DIM_2, AXI, XI_DIM_1, XI_DIM_2, XI, AX_DIM_1, AX_DIM_2, AX, X_DIM_1&
+&, X_DIM_2, X) BIND(C)
     USE APOS, ONLY: EMBED
     USE APOS, ONLY: MODEL_CONFIG
     IMPLICIT NONE
     TYPE(MODEL_CONFIG), INTENT(IN) :: CONFIG
     INTEGER, INTENT(IN) :: MODEL_DIM_1
     REAL(KIND=RT), INTENT(IN), DIMENSION(MODEL_DIM_1) :: MODEL
-    INTEGER, INTENT(IN) :: X_DIM_1
-    INTEGER, INTENT(IN) :: X_DIM_2
-    REAL(KIND=RT), INTENT(IN), DIMENSION(X_DIM_1,X_DIM_2) :: X
+    INTEGER, INTENT(IN) :: AXI_DIM_1
+    INTEGER, INTENT(IN) :: AXI_DIM_2
+    INTEGER, INTENT(IN), DIMENSION(AXI_DIM_1,AXI_DIM_2) :: AXI
     INTEGER, INTENT(IN) :: XI_DIM_1
     INTEGER, INTENT(IN) :: XI_DIM_2
     INTEGER, INTENT(IN), DIMENSION(XI_DIM_1,XI_DIM_2) :: XI
     INTEGER, INTENT(IN) :: AX_DIM_1
     INTEGER, INTENT(IN) :: AX_DIM_2
-    REAL(KIND=RT), INTENT(IN), DIMENSION(AX_DIM_1,AX_DIM_2) :: AX
-    INTEGER, INTENT(IN) :: AXI_DIM_1
-    INTEGER, INTENT(IN) :: AXI_DIM_2
-    INTEGER, INTENT(IN), DIMENSION(AXI_DIM_1,AXI_DIM_2) :: AXI
-    INTEGER, INTENT(IN) :: XXI_DIM_1
-    INTEGER, INTENT(IN) :: XXI_DIM_2
-    REAL(KIND=RT), INTENT(OUT), DIMENSION(XXI_DIM_1,XXI_DIM_2) :: XXI
-    INTEGER, INTENT(IN) :: AXXI_DIM_1
-    INTEGER, INTENT(IN) :: AXXI_DIM_2
-    REAL(KIND=RT), INTENT(OUT), DIMENSION(AXXI_DIM_1,AXXI_DIM_2) :: AXXI
-  
-    CALL EMBED(CONFIG, MODEL, X, XI, AX, AXI, XXI, AXXI)
-  END SUBROUTINE C_EMBED
-  
-
-  
-  SUBROUTINE C_COMPUTE_BATCHES(NUM_BATCHES, X_DIM_1, X_DIM_2, X, AX_DIM_1, AX_DIM_2, AX, SIZES_DIM_1, SIZES, BATCHA_DIM_1, BATCHA_D&
-&IM_2, BATCHA, BATCHM_DIM_1, BATCHM_DIM_2, BATCHM, INFO) BIND(C)
-    USE APOS, ONLY: COMPUTE_BATCHES
-    IMPLICIT NONE
-    INTEGER, INTENT(IN) :: NUM_BATCHES
+    REAL(KIND=RT), INTENT(OUT), DIMENSION(AX_DIM_1,AX_DIM_2) :: AX
     INTEGER, INTENT(IN) :: X_DIM_1
     INTEGER, INTENT(IN) :: X_DIM_2
-    REAL(KIND=RT), INTENT(IN), DIMENSION(X_DIM_1,X_DIM_2) :: X
-    INTEGER, INTENT(IN) :: AX_DIM_1
-    INTEGER, INTENT(IN) :: AX_DIM_2
-    REAL(KIND=RT), INTENT(IN), DIMENSION(AX_DIM_1,AX_DIM_2) :: AX
-    INTEGER, INTENT(IN) :: SIZES_DIM_1
-    INTEGER, INTENT(IN), DIMENSION(SIZES_DIM_1) :: SIZES
-    INTEGER, INTENT(IN) :: BATCHA_DIM_1
-    INTEGER, INTENT(IN) :: BATCHA_DIM_2
-    INTEGER, INTENT(OUT), DIMENSION(BATCHA_DIM_1,BATCHA_DIM_2) :: BATCHA
-    INTEGER, INTENT(IN) :: BATCHM_DIM_1
-    INTEGER, INTENT(IN) :: BATCHM_DIM_2
-    INTEGER, INTENT(OUT), DIMENSION(BATCHM_DIM_1,BATCHM_DIM_2) :: BATCHM
-    INTEGER, INTENT(INOUT) :: INFO
+    REAL(KIND=RT), INTENT(OUT), DIMENSION(X_DIM_1,X_DIM_2) :: X
   
-    CALL COMPUTE_BATCHES(NUM_BATCHES, X, AX, SIZES, BATCHA, BATCHM, INFO)
-  END SUBROUTINE C_COMPUTE_BATCHES
+    CALL EMBED(CONFIG, MODEL, AXI, XI, AX, X)
+  END SUBROUTINE C_EMBED
   
 
   
-  SUBROUTINE C_EVALUATE(CONFIG, MODEL_DIM_1, MODEL, Y_DIM_1, Y_DIM_2, Y, X_DIM_1, X_DIM_2, X, AX_DIM_1, AX_DIM_2, AX, SIZES_DIM_1, &
-&SIZES, M_STATES_DIM_1, M_STATES_DIM_2, M_STATES_DIM_3, M_STATES, A_STATES_DIM_1, A_STATES_DIM_2, A_STATES_DIM_3, A_STATES, AY_DIM_&
-&1, AY_DIM_2, AY, INFO, SHIFT_PRESENT, SHIFT, THREADS_PRESENT, THREADS) BIND(C)
+  SUBROUTINE C_EVALUATE(CONFIG, MODEL_DIM_1, MODEL, AX_DIM_1, AX_DIM_2, AX, AY_DIM_1, AY_DIM_2, AY, SIZES_DIM_1, SIZES, X_DIM_1, X_&
+&DIM_2, X, Y_DIM_1, Y_DIM_2, Y, A_STATES_DIM_1, A_STATES_DIM_2, A_STATES_DIM_3, A_STATES, M_STATES_DIM_1, M_STATES_DIM_2, M_STATES_&
+&DIM_3, M_STATES, INFO) BIND(C)
     USE APOS, ONLY: EVALUATE
     USE APOS, ONLY: MODEL_CONFIG
     IMPLICIT NONE
     TYPE(MODEL_CONFIG), INTENT(IN) :: CONFIG
     INTEGER, INTENT(IN) :: MODEL_DIM_1
     REAL(KIND=RT), INTENT(IN), DIMENSION(MODEL_DIM_1) :: MODEL
-    INTEGER, INTENT(IN) :: Y_DIM_1
-    INTEGER, INTENT(IN) :: Y_DIM_2
-    REAL(KIND=RT), INTENT(OUT), DIMENSION(Y_DIM_1,Y_DIM_2) :: Y
-    INTEGER, INTENT(IN) :: X_DIM_1
-    INTEGER, INTENT(IN) :: X_DIM_2
-    REAL(KIND=RT), INTENT(INOUT), DIMENSION(X_DIM_1,X_DIM_2) :: X
     INTEGER, INTENT(IN) :: AX_DIM_1
     INTEGER, INTENT(IN) :: AX_DIM_2
     REAL(KIND=RT), INTENT(INOUT), DIMENSION(AX_DIM_1,AX_DIM_2) :: AX
+    INTEGER, INTENT(IN) :: AY_DIM_1
+    INTEGER, INTENT(IN) :: AY_DIM_2
+    REAL(KIND=RT), INTENT(OUT), DIMENSION(AY_DIM_1,AY_DIM_2) :: AY
     INTEGER, INTENT(IN) :: SIZES_DIM_1
     INTEGER, INTENT(IN), DIMENSION(SIZES_DIM_1) :: SIZES
-    INTEGER, INTENT(IN) :: M_STATES_DIM_1
-    INTEGER, INTENT(IN) :: M_STATES_DIM_2
-    INTEGER, INTENT(IN) :: M_STATES_DIM_3
-    REAL(KIND=RT), INTENT(OUT), DIMENSION(M_STATES_DIM_1,M_STATES_DIM_2,M_STATES_DIM_3) :: M_STATES
+    INTEGER, INTENT(IN) :: X_DIM_1
+    INTEGER, INTENT(IN) :: X_DIM_2
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(X_DIM_1,X_DIM_2) :: X
+    INTEGER, INTENT(IN) :: Y_DIM_1
+    INTEGER, INTENT(IN) :: Y_DIM_2
+    REAL(KIND=RT), INTENT(OUT), DIMENSION(Y_DIM_1,Y_DIM_2) :: Y
     INTEGER, INTENT(IN) :: A_STATES_DIM_1
     INTEGER, INTENT(IN) :: A_STATES_DIM_2
     INTEGER, INTENT(IN) :: A_STATES_DIM_3
     REAL(KIND=RT), INTENT(OUT), DIMENSION(A_STATES_DIM_1,A_STATES_DIM_2,A_STATES_DIM_3) :: A_STATES
-    INTEGER, INTENT(IN) :: AY_DIM_1
-    INTEGER, INTENT(IN) :: AY_DIM_2
-    REAL(KIND=RT), INTENT(OUT), DIMENSION(AY_DIM_1,AY_DIM_2) :: AY
+    INTEGER, INTENT(IN) :: M_STATES_DIM_1
+    INTEGER, INTENT(IN) :: M_STATES_DIM_2
+    INTEGER, INTENT(IN) :: M_STATES_DIM_3
+    REAL(KIND=RT), INTENT(OUT), DIMENSION(M_STATES_DIM_1,M_STATES_DIM_2,M_STATES_DIM_3) :: M_STATES
     INTEGER, INTENT(INOUT) :: INFO
-    LOGICAL, INTENT(IN) :: SHIFT_PRESENT
-    LOGICAL, INTENT(IN) :: SHIFT
-    LOGICAL, INTENT(IN) :: THREADS_PRESENT
-    INTEGER, INTENT(IN) :: THREADS
-  
-    IF (SHIFT_PRESENT) THEN
-      IF (THREADS_PRESENT) THEN
-        CALL EVALUATE(CONFIG=CONFIG, MODEL=MODEL, Y=Y, X=X, AX=AX, SIZES=SIZES, M_STATES=M_STATES, A_STATES=A_STATES, AY=AY, INFO=I&
-&NFO, SHIFT=SHIFT, THREADS=THREADS)
-      ELSE
-        CALL EVALUATE(CONFIG=CONFIG, MODEL=MODEL, Y=Y, X=X, AX=AX, SIZES=SIZES, M_STATES=M_STATES, A_STATES=A_STATES, AY=AY, INFO=I&
-&NFO, SHIFT=SHIFT)
-      END IF
-    ELSE
-      IF (THREADS_PRESENT) THEN
-        CALL EVALUATE(CONFIG=CONFIG, MODEL=MODEL, Y=Y, X=X, AX=AX, SIZES=SIZES, M_STATES=M_STATES, A_STATES=A_STATES, AY=AY, INFO=I&
-&NFO, THREADS=THREADS)
-      ELSE
-        CALL EVALUATE(CONFIG=CONFIG, MODEL=MODEL, Y=Y, X=X, AX=AX, SIZES=SIZES, M_STATES=M_STATES, A_STATES=A_STATES, AY=AY, INFO=I&
-&NFO)
-      END IF
-    END IF
+  
+    CALL EVALUATE(CONFIG, MODEL, AX, AY, SIZES, X, Y, A_STATES, M_STATES, INFO)
   END SUBROUTINE C_EVALUATE
   
 
   
   SUBROUTINE C_BASIS_GRADIENT(CONFIG, MODEL_DIM_1, MODEL, Y_DIM_1, Y_DIM_2, Y, X_DIM_1, X_DIM_2, X, AX_DIM_1, AX_DIM_2, AX, SIZES_D&
 &IM_1, SIZES, M_STATES_DIM_1, M_STATES_DIM_2, M_STATES_DIM_3, M_STATES, A_STATES_DIM_1, A_STATES_DIM_2, A_STATES_DIM_3, A_STATES, A&
-&Y_DIM_1, AY_DIM_2, AY, GRAD_DIM_1, GRAD, SKIP_EMBEDDINGS_PRESENT, SKIP_EMBEDDINGS) BIND(C)
+&Y_DIM_1, AY_DIM_2, AY, GRAD_DIM_1, GRAD) BIND(C)
     USE APOS, ONLY: BASIS_GRADIENT
     USE APOS, ONLY: MODEL_CONFIG
     IMPLICIT NONE
     TYPE(MODEL_CONFIG), INTENT(IN) :: CONFIG
     INTEGER, INTENT(IN) :: MODEL_DIM_1
     REAL(KIND=RT), INTENT(IN), DIMENSION(MODEL_DIM_1) :: MODEL
     INTEGER, INTENT(IN) :: Y_DIM_1
@@ -5128,24 +5359,16 @@
     INTEGER, INTENT(IN) :: A_STATES_DIM_3
     REAL(KIND=RT), INTENT(INOUT), DIMENSION(A_STATES_DIM_1,A_STATES_DIM_2,A_STATES_DIM_3) :: A_STATES
     INTEGER, INTENT(IN) :: AY_DIM_1
     INTEGER, INTENT(IN) :: AY_DIM_2
     REAL(KIND=RT), INTENT(INOUT), DIMENSION(AY_DIM_1,AY_DIM_2) :: AY
     INTEGER, INTENT(IN) :: GRAD_DIM_1
     REAL(KIND=RT), INTENT(OUT), DIMENSION(GRAD_DIM_1) :: GRAD
-    LOGICAL, INTENT(IN) :: SKIP_EMBEDDINGS_PRESENT
-    LOGICAL, INTENT(IN) :: SKIP_EMBEDDINGS
   
-    IF (SKIP_EMBEDDINGS_PRESENT) THEN
-      CALL BASIS_GRADIENT(CONFIG=CONFIG, MODEL=MODEL, Y=Y, X=X, AX=AX, SIZES=SIZES, M_STATES=M_STATES, A_STATES=A_STATES, AY=AY, GR&
-&AD=GRAD, SKIP_EMBEDDINGS=SKIP_EMBEDDINGS)
-    ELSE
-      CALL BASIS_GRADIENT(CONFIG=CONFIG, MODEL=MODEL, Y=Y, X=X, AX=AX, SIZES=SIZES, M_STATES=M_STATES, A_STATES=A_STATES, AY=AY, GR&
-&AD=GRAD)
-    END IF
+    CALL BASIS_GRADIENT(CONFIG, MODEL, Y, X, AX, SIZES, M_STATES, A_STATES, AY, GRAD)
   END SUBROUTINE C_BASIS_GRADIENT
   
 
   
   SUBROUTINE C_EMBEDDING_GRADIENT(MDE, MNE, INT_INPUTS_DIM_1, INT_INPUTS_DIM_2, INT_INPUTS, GRAD_DIM_1, GRAD_DIM_2, GRAD, EMBEDDING&
 &_GRAD_DIM_1, EMBEDDING_GRAD_DIM_2, EMBEDDING_GRAD) BIND(C)
     USE APOS, ONLY: EMBEDDING_GRADIENT
@@ -5163,82 +5386,56 @@
     REAL(KIND=RT), INTENT(INOUT), DIMENSION(EMBEDDING_GRAD_DIM_1,EMBEDDING_GRAD_DIM_2) :: EMBEDDING_GRAD
   
     CALL EMBEDDING_GRADIENT(MDE, MNE, INT_INPUTS, GRAD, EMBEDDING_GRAD)
   END SUBROUTINE C_EMBEDDING_GRADIENT
   
 
   
-  SUBROUTINE C_SQUARED_ERROR_GRADIENT(TARGETS_DIM_1, TARGETS_DIM_2, TARGETS, OUTPUTS_DIM_1, OUTPUTS_DIM_2, OUTPUTS) BIND(C)
-    USE APOS, ONLY: SQUARED_ERROR_GRADIENT
-    IMPLICIT NONE
-    INTEGER, INTENT(IN) :: TARGETS_DIM_1
-    INTEGER, INTENT(IN) :: TARGETS_DIM_2
-    REAL(KIND=RT), INTENT(IN), DIMENSION(TARGETS_DIM_1,TARGETS_DIM_2) :: TARGETS
-    INTEGER, INTENT(IN) :: OUTPUTS_DIM_1
-    INTEGER, INTENT(IN) :: OUTPUTS_DIM_2
-    REAL(KIND=RT), INTENT(INOUT), DIMENSION(OUTPUTS_DIM_1,OUTPUTS_DIM_2) :: OUTPUTS
-  
-    CALL SQUARED_ERROR_GRADIENT(TARGETS, OUTPUTS)
-  END SUBROUTINE C_SQUARED_ERROR_GRADIENT
-  
-
-  
-  SUBROUTINE C_TRUE_VALUE_GRADIENT(TARGETS_DIM_1, TARGETS_DIM_2, TARGETS, OUTPUTS_DIM_1, OUTPUTS_DIM_2, OUTPUTS) BIND(C)
-    USE APOS, ONLY: TRUE_VALUE_GRADIENT
-    IMPLICIT NONE
-    INTEGER, INTENT(IN) :: TARGETS_DIM_1
-    INTEGER, INTENT(IN) :: TARGETS_DIM_2
-    REAL(KIND=RT), INTENT(IN), DIMENSION(TARGETS_DIM_1,TARGETS_DIM_2) :: TARGETS
-    INTEGER, INTENT(IN) :: OUTPUTS_DIM_1
-    INTEGER, INTENT(IN) :: OUTPUTS_DIM_2
-    REAL(KIND=RT), INTENT(INOUT), DIMENSION(OUTPUTS_DIM_1,OUTPUTS_DIM_2) :: OUTPUTS
-  
-    CALL TRUE_VALUE_GRADIENT(TARGETS, OUTPUTS)
-  END SUBROUTINE C_TRUE_VALUE_GRADIENT
-  
-
-  
-  SUBROUTINE C_MINIMIZE_MSE(CONFIG, MODEL_DIM_1, MODEL, Y_DIM_1, Y_DIM_2, Y, X_DIM_1, X_DIM_2, X, XI_DIM_1, XI_DIM_2, XI, AX_DIM_1,&
-& AX_DIM_2, AX, AXI_DIM_1, AXI_DIM_2, AXI, SIZES_DIM_1, SIZES, STEPS, SUM_SQUARED_ERROR, RECORD_PRESENT, RECORD_DIM_1, RECORD_DIM_2&
-&, RECORD, INFO) BIND(C)
+  SUBROUTINE C_MINIMIZE_MSE(CONFIG, MODEL_DIM_1, MODEL, RWORK_DIM_1, RWORK, IWORK_DIM_1, IWORK, AX_DIM_1, AX_DIM_2, AX, AXI_DIM_1, &
+&AXI_DIM_2, AXI, SIZES_DIM_1, SIZES, X_DIM_1, X_DIM_2, X, XI_DIM_1, XI_DIM_2, XI, Y_DIM_1, Y_DIM_2, Y, STEPS, RECORD_PRESENT, RECOR&
+&D_DIM_1, RECORD_DIM_2, RECORD, SUM_SQUARED_ERROR, INFO) BIND(C)
     USE APOS, ONLY: MINIMIZE_MSE
     USE APOS, ONLY: MODEL_CONFIG
     IMPLICIT NONE
-    TYPE(MODEL_CONFIG), INTENT(IN) :: CONFIG
+    TYPE(MODEL_CONFIG), INTENT(INOUT) :: CONFIG
     INTEGER, INTENT(IN) :: MODEL_DIM_1
     REAL(KIND=RT), INTENT(INOUT), DIMENSION(MODEL_DIM_1) :: MODEL
-    INTEGER, INTENT(IN) :: Y_DIM_1
-    INTEGER, INTENT(IN) :: Y_DIM_2
-    REAL(KIND=RT), INTENT(INOUT), DIMENSION(Y_DIM_1,Y_DIM_2) :: Y
-    INTEGER, INTENT(IN) :: X_DIM_1
-    INTEGER, INTENT(IN) :: X_DIM_2
-    REAL(KIND=RT), INTENT(INOUT), DIMENSION(X_DIM_1,X_DIM_2) :: X
-    INTEGER, INTENT(IN) :: XI_DIM_1
-    INTEGER, INTENT(IN) :: XI_DIM_2
-    INTEGER, INTENT(IN), DIMENSION(XI_DIM_1,XI_DIM_2) :: XI
+    INTEGER, INTENT(IN) :: RWORK_DIM_1
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(RWORK_DIM_1) :: RWORK
+    INTEGER, INTENT(IN) :: IWORK_DIM_1
+    INTEGER, INTENT(INOUT), DIMENSION(IWORK_DIM_1) :: IWORK
     INTEGER, INTENT(IN) :: AX_DIM_1
     INTEGER, INTENT(IN) :: AX_DIM_2
     REAL(KIND=RT), INTENT(INOUT), DIMENSION(AX_DIM_1,AX_DIM_2) :: AX
     INTEGER, INTENT(IN) :: AXI_DIM_1
     INTEGER, INTENT(IN) :: AXI_DIM_2
     INTEGER, INTENT(IN), DIMENSION(AXI_DIM_1,AXI_DIM_2) :: AXI
     INTEGER, INTENT(IN) :: SIZES_DIM_1
     INTEGER, INTENT(IN), DIMENSION(SIZES_DIM_1) :: SIZES
+    INTEGER, INTENT(IN) :: X_DIM_1
+    INTEGER, INTENT(IN) :: X_DIM_2
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(X_DIM_1,X_DIM_2) :: X
+    INTEGER, INTENT(IN) :: XI_DIM_1
+    INTEGER, INTENT(IN) :: XI_DIM_2
+    INTEGER, INTENT(IN), DIMENSION(XI_DIM_1,XI_DIM_2) :: XI
+    INTEGER, INTENT(IN) :: Y_DIM_1
+    INTEGER, INTENT(IN) :: Y_DIM_2
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(Y_DIM_1,Y_DIM_2) :: Y
     INTEGER, INTENT(IN) :: STEPS
-    REAL(KIND=RT), INTENT(OUT) :: SUM_SQUARED_ERROR
     LOGICAL, INTENT(IN) :: RECORD_PRESENT
     INTEGER, INTENT(IN) :: RECORD_DIM_1
     INTEGER, INTENT(IN) :: RECORD_DIM_2
     REAL(KIND=RT), INTENT(OUT), DIMENSION(RECORD_DIM_1,RECORD_DIM_2) :: RECORD
+    REAL(KIND=RT), INTENT(OUT) :: SUM_SQUARED_ERROR
     INTEGER, INTENT(OUT) :: INFO
   
     IF (RECORD_PRESENT) THEN
-      CALL MINIMIZE_MSE(CONFIG=CONFIG, MODEL=MODEL, Y=Y, X=X, XI=XI, AX=AX, AXI=AXI, SIZES=SIZES, STEPS=STEPS, SUM_SQUARED_ERROR=SU&
-&M_SQUARED_ERROR, INFO=INFO, RECORD=RECORD)
+      CALL MINIMIZE_MSE(CONFIG=CONFIG, MODEL=MODEL, RWORK=RWORK, IWORK=IWORK, AX=AX, AXI=AXI, SIZES=SIZES, X=X, XI=XI, Y=Y, STEPS=S&
+&TEPS, SUM_SQUARED_ERROR=SUM_SQUARED_ERROR, INFO=INFO, RECORD=RECORD)
     ELSE
-      CALL MINIMIZE_MSE(CONFIG=CONFIG, MODEL=MODEL, Y=Y, X=X, XI=XI, AX=AX, AXI=AXI, SIZES=SIZES, STEPS=STEPS, SUM_SQUARED_ERROR=SU&
-&M_SQUARED_ERROR, INFO=INFO)
+      CALL MINIMIZE_MSE(CONFIG=CONFIG, MODEL=MODEL, RWORK=RWORK, IWORK=IWORK, AX=AX, AXI=AXI, SIZES=SIZES, X=X, XI=XI, Y=Y, STEPS=S&
+&TEPS, SUM_SQUARED_ERROR=SUM_SQUARED_ERROR, INFO=INFO)
     END IF
   END SUBROUTINE C_MINIMIZE_MSE
   
 END MODULE C_APOS
```

### Comparing `tlux-0.0.8/tlux/approximate/apos/apos/apos_python_wrapper.py` & `tlux-0.0.9/tlux/approximate/apos/apos/apos_python_wrapper.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,42 +1,37 @@
 '''This Python code is an automatically generated wrapper
 for Fortran code made by 'fmodpy'. The original documentation
 for the Fortran source code follows.
 
 ! TODO:
 !
-! - Unify memory allocation so that threads don't have to allocate their
-!   own temporary space.
+! - Thoroughly test NORMALIZE (make sure data is correctly normalized in all use cases).
+!   Particularly, check that the initialization of the apositional output scale is working.
 !
-! - Enable a model that has no internal states (for linear regression).
+! - Reset convention to be order of processing (AX, AXI, AY, SIZES, X, XI, Y)
+! - Enable a model that has no internal states for linear regression (*NS=0).
+! - Enable a apositional without a following model (MDO=0) (no apositional shifting).
 !
-! - Enable a apositional without a following model.
+! - Update Python testing code to test all combinations of AX, AXI, AY, X, XI, and Y.
+! - Update Python testing code to attempt different edge-case model sizes
+!    (linear regression, no apositional, no model).
 !
-! - Center and fit inputs and outputs to spherical points (unit length).
+! - Make data normalization use the same work space as the fit procedure
+!   (since these are not needed at the same time).
+! - Pull normalization code out and have it be called separately from 'FIT'.
+!   (decide how to handle encoding the normalization into the model, function?)
+!   Goal is to achieve near-zero losses for doing a few steps at a time in
+!   Python (allowing for easier cancellation, progress updates, ...).
 !
-! - Change initialization of shift terms to be based on the assumption
-!   that input data has spherical shape. Internal shift terms use
-!   previous shift and weight matrices to estimate value ranges for
-!   each basis function, with largest functions getting most negative
-!   shift and smallest functions getting most positive shift.
-!
-! - Create 'condition_model' subroutine that takes values and gradients
-!   at all internal states, uses linear transformations to identify and
-!   remove redundant basis functions and initialize new basis functions
-!   that align most with the error function.
-!
-! - Get stats on the internal values within the network during training.
-!   - step size progression
-!   - shift values
-!   - vector magnitudes for each node
-!   - output weights magnitude for each node
-!   - internal node contributions to MSE
-!   - data distributions at internal nodes (% less and greater than 0)
+! - Use LAPACK to do linear regression, implement simple SVD + gradient descent method
+!   in MATRIX_OPERATIONS, compare speed of both methodologies.
+! - Implement and test Fortran intrinsic version of matrix multiplication.
+! - Implement and test Fortran intrinsic version of SSYRK (manually do loop).
 !
-
+! ---------------------------------------------------------------------------
 
 ! Module for matrix multiplication (absolutely crucial for APOS speed).
 '''
 
 import os
 import ctypes
 import platform
@@ -46,15 +41,15 @@
 #               CONFIGURATION
 # 
 _verbose = True
 _fort_compiler = "gfortran"
 _shared_object_name = "apos." + platform.machine() + ".so"
 _this_directory = os.path.dirname(os.path.abspath(__file__))
 _path_to_lib = os.path.join(_this_directory, _shared_object_name)
-_compile_options = ['-fPIC', '-shared', '-O3', '-lblas', '-fopenmp', '-fcheck=bounds', '-llapack']
+_compile_options = ['-fPIC', '-shared', '-O3', '-lblas', '-llapack', '-fopenmp', '-fcheck=bounds']
 _ordered_dependencies = ['apos.f90', 'apos_c_wrapper.f90']
 # 
 # --------------------------------------------------------------------
 #               AUTO-COMPILING
 #
 # Try to import the existing object. If that fails, recompile and then try.
 try:
@@ -194,138 +189,630 @@
     
         # Call C-accessible Fortran wrapper.
         clib.c_random_unit_vectors(ctypes.byref(column_vectors_dim_1), ctypes.byref(column_vectors_dim_2), ctypes.c_void_p(column_vectors.ctypes.data))
     
         # Return final results, 'INTENT(OUT)' arguments only.
         return column_vectors
 
+    
+    # ----------------------------------------------
+    # Wrapper for the Fortran subroutine ORTHOGONALIZE
+    
+    def orthogonalize(self, a, lengths=None, rank=None, order=None):
+        '''! Orthogonalize and normalize column vectors of A with pivoting.'''
+        
+        # Setting up "a"
+        if ((not issubclass(type(a), numpy.ndarray)) or
+            (not numpy.asarray(a).flags.f_contiguous) or
+            (not (a.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 'a' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            a = numpy.asarray(a, dtype=ctypes.c_float, order='F')
+        a_dim_1 = ctypes.c_int(a.shape[0])
+        a_dim_2 = ctypes.c_int(a.shape[1])
+        
+        # Setting up "lengths"
+        if (lengths is None):
+            lengths = numpy.zeros(shape=(a.shape[1]), dtype=ctypes.c_float, order='F')
+        elif ((not issubclass(type(lengths), numpy.ndarray)) or
+              (not numpy.asarray(lengths).flags.f_contiguous) or
+              (not (lengths.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 'lengths' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            lengths = numpy.asarray(lengths, dtype=ctypes.c_float, order='F')
+        lengths_dim_1 = ctypes.c_int(lengths.shape[0])
+        
+        # Setting up "rank"
+        rank_present = ctypes.c_bool(True)
+        if (rank is None):
+            rank_present = ctypes.c_bool(False)
+            rank = ctypes.c_int()
+        else:
+            rank = ctypes.c_int(rank)
+        
+        # Setting up "order"
+        order_present = ctypes.c_bool(True)
+        if (order is None):
+            order_present = ctypes.c_bool(False)
+            order = numpy.zeros(shape=(1), dtype=ctypes.c_int, order='F')
+        elif (type(order) == bool) and (order):
+            order = numpy.zeros(shape=(a.shape[1]), dtype=ctypes.c_int, order='F')
+        elif ((not issubclass(type(order), numpy.ndarray)) or
+              (not numpy.asarray(order).flags.f_contiguous) or
+              (not (order.dtype == numpy.dtype(ctypes.c_int)))):
+            import warnings
+            warnings.warn("The provided argument 'order' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
+            order = numpy.asarray(order, dtype=ctypes.c_int, order='F')
+        if (order_present):
+            order_dim_1 = ctypes.c_int(order.shape[0])
+        else:
+            order_dim_1 = ctypes.c_int()
+    
+        # Call C-accessible Fortran wrapper.
+        clib.c_orthogonalize(ctypes.byref(a_dim_1), ctypes.byref(a_dim_2), ctypes.c_void_p(a.ctypes.data), ctypes.byref(lengths_dim_1), ctypes.c_void_p(lengths.ctypes.data), ctypes.byref(rank_present), ctypes.byref(rank), ctypes.byref(order_present), ctypes.byref(order_dim_1), ctypes.c_void_p(order.ctypes.data))
+    
+        # Return final results, 'INTENT(OUT)' arguments only.
+        return a, lengths, (rank.value if rank_present else None), (order if order_present else None)
+
+    
+    # ----------------------------------------------
+    # Wrapper for the Fortran subroutine SVD
+    
+    def svd(self, a, s=None, vt=None, rank=None, steps=None, bias=None):
+        '''! Compute the singular values and right singular vectors for matrix A.'''
+        
+        # Setting up "a"
+        if ((not issubclass(type(a), numpy.ndarray)) or
+            (not numpy.asarray(a).flags.f_contiguous) or
+            (not (a.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 'a' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            a = numpy.asarray(a, dtype=ctypes.c_float, order='F')
+        a_dim_1 = ctypes.c_int(a.shape[0])
+        a_dim_2 = ctypes.c_int(a.shape[1])
+        
+        # Setting up "s"
+        if (s is None):
+            s = numpy.zeros(shape=(min(a.shape[0],a.shape[1])), dtype=ctypes.c_float, order='F')
+        elif ((not issubclass(type(s), numpy.ndarray)) or
+              (not numpy.asarray(s).flags.f_contiguous) or
+              (not (s.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 's' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            s = numpy.asarray(s, dtype=ctypes.c_float, order='F')
+        s_dim_1 = ctypes.c_int(s.shape[0])
+        
+        # Setting up "vt"
+        if (vt is None):
+            vt = numpy.zeros(shape=(min(a.shape[0],a.shape[1]), min(a.shape[0],a.shape[1])), dtype=ctypes.c_float, order='F')
+        elif ((not issubclass(type(vt), numpy.ndarray)) or
+              (not numpy.asarray(vt).flags.f_contiguous) or
+              (not (vt.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 'vt' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            vt = numpy.asarray(vt, dtype=ctypes.c_float, order='F')
+        vt_dim_1 = ctypes.c_int(vt.shape[0])
+        vt_dim_2 = ctypes.c_int(vt.shape[1])
+        
+        # Setting up "rank"
+        rank_present = ctypes.c_bool(True)
+        if (rank is None):
+            rank_present = ctypes.c_bool(False)
+            rank = ctypes.c_int()
+        else:
+            rank = ctypes.c_int(rank)
+        
+        # Setting up "steps"
+        steps_present = ctypes.c_bool(True)
+        if (steps is None):
+            steps_present = ctypes.c_bool(False)
+            steps = ctypes.c_int()
+        else:
+            steps = ctypes.c_int(steps)
+        if (type(steps) is not ctypes.c_int): steps = ctypes.c_int(steps)
+        
+        # Setting up "bias"
+        bias_present = ctypes.c_bool(True)
+        if (bias is None):
+            bias_present = ctypes.c_bool(False)
+            bias = ctypes.c_float()
+        else:
+            bias = ctypes.c_float(bias)
+        if (type(bias) is not ctypes.c_float): bias = ctypes.c_float(bias)
+    
+        # Call C-accessible Fortran wrapper.
+        clib.c_svd(ctypes.byref(a_dim_1), ctypes.byref(a_dim_2), ctypes.c_void_p(a.ctypes.data), ctypes.byref(s_dim_1), ctypes.c_void_p(s.ctypes.data), ctypes.byref(vt_dim_1), ctypes.byref(vt_dim_2), ctypes.c_void_p(vt.ctypes.data), ctypes.byref(rank_present), ctypes.byref(rank), ctypes.byref(steps_present), ctypes.byref(steps), ctypes.byref(bias_present), ctypes.byref(bias))
+    
+        # Return final results, 'INTENT(OUT)' arguments only.
+        return s, vt, (rank.value if rank_present else None)
+
+    
+    # ----------------------------------------------
+    # Wrapper for the Fortran subroutine RADIALIZE
+    
+    def radialize(self, x, shift, vecs, invert_result=None, steps=None):
+        '''! If there are at least as many data points as dimension, then
+! compute the principal components and rescale the data by
+! projecting onto those and rescaling so that each component has
+! identical singular values (this makes the data more "radially
+! symmetric").'''
+        
+        # Setting up "x"
+        if ((not issubclass(type(x), numpy.ndarray)) or
+            (not numpy.asarray(x).flags.f_contiguous) or
+            (not (x.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 'x' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            x = numpy.asarray(x, dtype=ctypes.c_float, order='F')
+        x_dim_1 = ctypes.c_int(x.shape[0])
+        x_dim_2 = ctypes.c_int(x.shape[1])
+        
+        # Setting up "shift"
+        if ((not issubclass(type(shift), numpy.ndarray)) or
+            (not numpy.asarray(shift).flags.f_contiguous) or
+            (not (shift.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 'shift' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            shift = numpy.asarray(shift, dtype=ctypes.c_float, order='F')
+        shift_dim_1 = ctypes.c_int(shift.shape[0])
+        
+        # Setting up "vecs"
+        if ((not issubclass(type(vecs), numpy.ndarray)) or
+            (not numpy.asarray(vecs).flags.f_contiguous) or
+            (not (vecs.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 'vecs' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            vecs = numpy.asarray(vecs, dtype=ctypes.c_float, order='F')
+        vecs_dim_1 = ctypes.c_int(vecs.shape[0])
+        vecs_dim_2 = ctypes.c_int(vecs.shape[1])
+        
+        # Setting up "invert_result"
+        invert_result_present = ctypes.c_bool(True)
+        if (invert_result is None):
+            invert_result_present = ctypes.c_bool(False)
+            invert_result = ctypes.c_int()
+        else:
+            invert_result = ctypes.c_int(invert_result)
+        if (type(invert_result) is not ctypes.c_int): invert_result = ctypes.c_int(invert_result)
+        
+        # Setting up "steps"
+        steps_present = ctypes.c_bool(True)
+        if (steps is None):
+            steps_present = ctypes.c_bool(False)
+            steps = ctypes.c_int()
+        else:
+            steps = ctypes.c_int(steps)
+        if (type(steps) is not ctypes.c_int): steps = ctypes.c_int(steps)
+    
+        # Call C-accessible Fortran wrapper.
+        clib.c_radialize(ctypes.byref(x_dim_1), ctypes.byref(x_dim_2), ctypes.c_void_p(x.ctypes.data), ctypes.byref(shift_dim_1), ctypes.c_void_p(shift.ctypes.data), ctypes.byref(vecs_dim_1), ctypes.byref(vecs_dim_2), ctypes.c_void_p(vecs.ctypes.data), ctypes.byref(invert_result_present), ctypes.byref(invert_result), ctypes.byref(steps_present), ctypes.byref(steps))
+    
+        # Return final results, 'INTENT(OUT)' arguments only.
+        return x, shift, vecs
+
 matrix_operations = matrix_operations()
 
 
+class sort_and_select:
+    '''! A module for fast sorting and selecting of data.'''
+
+    
+    # ----------------------------------------------
+    # Wrapper for the Fortran subroutine SWAP_INT
+    
+    def swap_int(self, v1, v2):
+        '''! Swap the values of two integers.'''
+        
+        # Setting up "v1"
+        if (type(v1) is not ctypes.c_int): v1 = ctypes.c_int(v1)
+        
+        # Setting up "v2"
+        if (type(v2) is not ctypes.c_int): v2 = ctypes.c_int(v2)
+    
+        # Call C-accessible Fortran wrapper.
+        clib.c_swap_int(ctypes.byref(v1), ctypes.byref(v2))
+    
+        # Return final results, 'INTENT(OUT)' arguments only.
+        return v1.value, v2.value
+
+    
+    # ----------------------------------------------
+    # Wrapper for the Fortran subroutine ARGSELECT
+    
+    def argselect(self, values, k, indices, divisor=None, max_size=None, recursing=None):
+        '''!                       FastSelect method
+!
+! Given VALUES list of numbers, rearrange the elements of INDICES
+! such that the element of VALUES at INDICES(K) has rank K (holds
+! its same location as if all of VALUES were sorted in INDICES).
+! All elements of VALUES at INDICES(:K-1) are less than or equal,
+! while all elements of VALUES at INDICES(K+1:) are greater or equal.
+!
+! This algorithm uses a recursive approach to exponentially shrink
+! the number of indices that have to be considered to find the
+! element of desired rank, while simultaneously pivoting values
+! that are less than the target rank left and larger right.
+!
+! Arguments:
+!
+!   VALUES   --  A 1D array of real numbers. Will not be modified.
+!   K        --  A positive integer for the rank index about which
+!                VALUES should be rearranged.
+! Optional:
+!
+!   DIVISOR  --  A positive integer >= 2 that represents the
+!                division factor used for large VALUES arrays.
+!   MAX_SIZE --  An integer >= DIVISOR that represents the largest
+!                sized VALUES for which the worst-case pivot value
+!                selection is tolerable. A worst-case pivot causes
+!                O( SIZE(VALUES)^2 ) runtime. This value should be
+!                determined heuristically based on compute hardware.
+! Output:
+!
+!   INDICES  --  A 1D array of original indices for elements of VALUES.
+!
+!   The elements of the array INDICES are rearranged such that the
+!   element at position VALUES(INDICES(K)) is in the same location
+!   it would be if all of VALUES were referenced in sorted order in
+!   INDICES. Also known as, VALUES(INDICES(K)) has rank K.
+!
+! Arguments'''
+        
+        # Setting up "values"
+        if ((not issubclass(type(values), numpy.ndarray)) or
+            (not numpy.asarray(values).flags.f_contiguous) or
+            (not (values.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 'values' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            values = numpy.asarray(values, dtype=ctypes.c_float, order='F')
+        values_dim_1 = ctypes.c_int(values.shape[0])
+        
+        # Setting up "k"
+        if (type(k) is not ctypes.c_int): k = ctypes.c_int(k)
+        
+        # Setting up "indices"
+        if ((not issubclass(type(indices), numpy.ndarray)) or
+            (not numpy.asarray(indices).flags.f_contiguous) or
+            (not (indices.dtype == numpy.dtype(ctypes.c_int)))):
+            import warnings
+            warnings.warn("The provided argument 'indices' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
+            indices = numpy.asarray(indices, dtype=ctypes.c_int, order='F')
+        indices_dim_1 = ctypes.c_int(indices.shape[0])
+        
+        # Setting up "divisor"
+        divisor_present = ctypes.c_bool(True)
+        if (divisor is None):
+            divisor_present = ctypes.c_bool(False)
+            divisor = ctypes.c_int()
+        else:
+            divisor = ctypes.c_int(divisor)
+        if (type(divisor) is not ctypes.c_int): divisor = ctypes.c_int(divisor)
+        
+        # Setting up "max_size"
+        max_size_present = ctypes.c_bool(True)
+        if (max_size is None):
+            max_size_present = ctypes.c_bool(False)
+            max_size = ctypes.c_int()
+        else:
+            max_size = ctypes.c_int(max_size)
+        if (type(max_size) is not ctypes.c_int): max_size = ctypes.c_int(max_size)
+        
+        # Setting up "recursing"
+        recursing_present = ctypes.c_bool(True)
+        if (recursing is None):
+            recursing_present = ctypes.c_bool(False)
+            recursing = ctypes.c_int()
+        else:
+            recursing = ctypes.c_int(recursing)
+        if (type(recursing) is not ctypes.c_int): recursing = ctypes.c_int(recursing)
+    
+        # Call C-accessible Fortran wrapper.
+        clib.c_argselect(ctypes.byref(values_dim_1), ctypes.c_void_p(values.ctypes.data), ctypes.byref(k), ctypes.byref(indices_dim_1), ctypes.c_void_p(indices.ctypes.data), ctypes.byref(divisor_present), ctypes.byref(divisor), ctypes.byref(max_size_present), ctypes.byref(max_size), ctypes.byref(recursing_present), ctypes.byref(recursing))
+    
+        # Return final results, 'INTENT(OUT)' arguments only.
+        return indices
+
+    
+    # ----------------------------------------------
+    # Wrapper for the Fortran subroutine ARGSORT
+    
+    def argsort(self, values, indices, min_size=None, init_inds=None):
+        '''!                         FastSort
+!
+! This routine uses a combination of QuickSort (with modestly
+! intelligent pivot selection) and Insertion Sort (for small arrays)
+! to achieve very fast average case sort times for both random and
+! partially sorted data. The pivot is selected for QuickSort as the
+! median of the first, middle, and last values in the array.
+!
+! Arguments:
+!
+!   VALUES   --  A 1D array of real numbers.
+!   INDICES  --  A 1D array of original indices for elements of VALUES.
+!
+! Optional:
+!
+!   MIN_SIZE --  An positive integer that represents the largest
+!                sized VALUES for which a partition about a pivot
+!                is used to reduce the size of a an unsorted array.
+!                Any size less than this will result in the use of
+!                INSERTION_ARGSORT instead of ARGPARTITION.
+!
+! Output:
+!
+!   The elements of the array INDICES contain ths sorted order of VALUES.'''
+        
+        # Setting up "values"
+        if ((not issubclass(type(values), numpy.ndarray)) or
+            (not numpy.asarray(values).flags.f_contiguous) or
+            (not (values.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 'values' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            values = numpy.asarray(values, dtype=ctypes.c_float, order='F')
+        values_dim_1 = ctypes.c_int(values.shape[0])
+        
+        # Setting up "indices"
+        if ((not issubclass(type(indices), numpy.ndarray)) or
+            (not numpy.asarray(indices).flags.f_contiguous) or
+            (not (indices.dtype == numpy.dtype(ctypes.c_int)))):
+            import warnings
+            warnings.warn("The provided argument 'indices' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
+            indices = numpy.asarray(indices, dtype=ctypes.c_int, order='F')
+        indices_dim_1 = ctypes.c_int(indices.shape[0])
+        
+        # Setting up "min_size"
+        min_size_present = ctypes.c_bool(True)
+        if (min_size is None):
+            min_size_present = ctypes.c_bool(False)
+            min_size = ctypes.c_int()
+        else:
+            min_size = ctypes.c_int(min_size)
+        if (type(min_size) is not ctypes.c_int): min_size = ctypes.c_int(min_size)
+        
+        # Setting up "init_inds"
+        init_inds_present = ctypes.c_bool(True)
+        if (init_inds is None):
+            init_inds_present = ctypes.c_bool(False)
+            init_inds = ctypes.c_int()
+        else:
+            init_inds = ctypes.c_int(init_inds)
+        if (type(init_inds) is not ctypes.c_int): init_inds = ctypes.c_int(init_inds)
+    
+        # Call C-accessible Fortran wrapper.
+        clib.c_argsort(ctypes.byref(values_dim_1), ctypes.c_void_p(values.ctypes.data), ctypes.byref(indices_dim_1), ctypes.c_void_p(indices.ctypes.data), ctypes.byref(min_size_present), ctypes.byref(min_size), ctypes.byref(init_inds_present), ctypes.byref(init_inds))
+    
+        # Return final results, 'INTENT(OUT)' arguments only.
+        return indices
+
+    
+    # ----------------------------------------------
+    # Wrapper for the Fortran subroutine INSERTION_ARGSORT
+    
+    def insertion_argsort(self, values, indices):
+        '''! Insertion sort (best for small lists).'''
+        
+        # Setting up "values"
+        if ((not issubclass(type(values), numpy.ndarray)) or
+            (not numpy.asarray(values).flags.f_contiguous) or
+            (not (values.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 'values' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            values = numpy.asarray(values, dtype=ctypes.c_float, order='F')
+        values_dim_1 = ctypes.c_int(values.shape[0])
+        
+        # Setting up "indices"
+        if ((not issubclass(type(indices), numpy.ndarray)) or
+            (not numpy.asarray(indices).flags.f_contiguous) or
+            (not (indices.dtype == numpy.dtype(ctypes.c_int)))):
+            import warnings
+            warnings.warn("The provided argument 'indices' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
+            indices = numpy.asarray(indices, dtype=ctypes.c_int, order='F')
+        indices_dim_1 = ctypes.c_int(indices.shape[0])
+    
+        # Call C-accessible Fortran wrapper.
+        clib.c_insertion_argsort(ctypes.byref(values_dim_1), ctypes.c_void_p(values.ctypes.data), ctypes.byref(indices_dim_1), ctypes.c_void_p(indices.ctypes.data))
+    
+        # Return final results, 'INTENT(OUT)' arguments only.
+        return indices
+
+    
+    # ----------------------------------------------
+    # Wrapper for the Fortran subroutine ARGPARTITION
+    
+    def argpartition(self, values, indices):
+        '''! This function efficiently partitions values based on the median
+! of the first, middle, and last elements of the VALUES array. This
+! function returns the index of the pivot.'''
+        
+        # Setting up "values"
+        if ((not issubclass(type(values), numpy.ndarray)) or
+            (not numpy.asarray(values).flags.f_contiguous) or
+            (not (values.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 'values' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            values = numpy.asarray(values, dtype=ctypes.c_float, order='F')
+        values_dim_1 = ctypes.c_int(values.shape[0])
+        
+        # Setting up "indices"
+        if ((not issubclass(type(indices), numpy.ndarray)) or
+            (not numpy.asarray(indices).flags.f_contiguous) or
+            (not (indices.dtype == numpy.dtype(ctypes.c_int)))):
+            import warnings
+            warnings.warn("The provided argument 'indices' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
+            indices = numpy.asarray(indices, dtype=ctypes.c_int, order='F')
+        indices_dim_1 = ctypes.c_int(indices.shape[0])
+        
+        # Setting up "left"
+        left = ctypes.c_int()
+    
+        # Call C-accessible Fortran wrapper.
+        clib.c_argpartition(ctypes.byref(values_dim_1), ctypes.c_void_p(values.ctypes.data), ctypes.byref(indices_dim_1), ctypes.c_void_p(indices.ctypes.data), ctypes.byref(left))
+    
+        # Return final results, 'INTENT(OUT)' arguments only.
+        return indices, left.value
+
+sort_and_select = sort_and_select()
+
+
 class apos:
     '''! An apositional (/aggregate) and positional piecewise linear regression model.'''
     
     # This defines a C structure that can be used to hold this defined type.
     class MODEL_CONFIG(ctypes.Structure):
         # (name, ctype) fields for this structure.
-        _fields_ = [("mdi", ctypes.c_int), ("mds", ctypes.c_int), ("mns", ctypes.c_int), ("mdo", ctypes.c_int), ("mne", ctypes.c_int), ("mde", ctypes.c_int), ("adi", ctypes.c_int), ("ads", ctypes.c_int), ("ans", ctypes.c_int), ("ado", ctypes.c_int), ("ane", ctypes.c_int), ("ade", ctypes.c_int), ("total_size", ctypes.c_int), ("num_vars", ctypes.c_int), ("msiv", ctypes.c_int), ("meiv", ctypes.c_int), ("msis", ctypes.c_int), ("meis", ctypes.c_int), ("mssv", ctypes.c_int), ("mesv", ctypes.c_int), ("msss", ctypes.c_int), ("mess", ctypes.c_int), ("msov", ctypes.c_int), ("meov", ctypes.c_int), ("msev", ctypes.c_int), ("meev", ctypes.c_int), ("asiv", ctypes.c_int), ("aeiv", ctypes.c_int), ("asis", ctypes.c_int), ("aeis", ctypes.c_int), ("assv", ctypes.c_int), ("aesv", ctypes.c_int), ("asss", ctypes.c_int), ("aess", ctypes.c_int), ("asov", ctypes.c_int), ("aeov", ctypes.c_int), ("asev", ctypes.c_int), ("aeev", ctypes.c_int), ("miss", ctypes.c_int), ("mise", ctypes.c_int), ("moss", ctypes.c_int), ("mose", ctypes.c_int), ("aiss", ctypes.c_int), ("aise", ctypes.c_int), ("discontinuity", ctypes.c_float), ("initial_shift_range", ctypes.c_float), ("initial_output_scale", ctypes.c_float), ("initial_step", ctypes.c_float), ("initial_step_mean_change", ctypes.c_float), ("initial_step_curv_change", ctypes.c_float), ("faster_rate", ctypes.c_float), ("slower_rate", ctypes.c_float), ("min_steps_to_stability", ctypes.c_int), ("num_threads", ctypes.c_int), ("keep_best", ctypes.c_bool), ("early_stop", ctypes.c_bool)]
+        _fields_ = [("adn", ctypes.c_int), ("adi", ctypes.c_int), ("ads", ctypes.c_int), ("ans", ctypes.c_int), ("ado", ctypes.c_int), ("ane", ctypes.c_int), ("ade", ctypes.c_int), ("mdn", ctypes.c_int), ("mdi", ctypes.c_int), ("mds", ctypes.c_int), ("mns", ctypes.c_int), ("mdo", ctypes.c_int), ("mne", ctypes.c_int), ("mde", ctypes.c_int), ("total_size", ctypes.c_int), ("num_vars", ctypes.c_int), ("asiv", ctypes.c_int), ("aeiv", ctypes.c_int), ("asis", ctypes.c_int), ("aeis", ctypes.c_int), ("assv", ctypes.c_int), ("aesv", ctypes.c_int), ("asss", ctypes.c_int), ("aess", ctypes.c_int), ("asov", ctypes.c_int), ("aeov", ctypes.c_int), ("asev", ctypes.c_int), ("aeev", ctypes.c_int), ("msiv", ctypes.c_int), ("meiv", ctypes.c_int), ("msis", ctypes.c_int), ("meis", ctypes.c_int), ("mssv", ctypes.c_int), ("mesv", ctypes.c_int), ("msss", ctypes.c_int), ("mess", ctypes.c_int), ("msov", ctypes.c_int), ("meov", ctypes.c_int), ("msev", ctypes.c_int), ("meev", ctypes.c_int), ("aiss", ctypes.c_int), ("aise", ctypes.c_int), ("aoss", ctypes.c_int), ("aose", ctypes.c_int), ("miss", ctypes.c_int), ("mise", ctypes.c_int), ("moss", ctypes.c_int), ("mose", ctypes.c_int), ("discontinuity", ctypes.c_float), ("initial_shift_range", ctypes.c_float), ("initial_output_scale", ctypes.c_float), ("step_factor", ctypes.c_float), ("step_mean_change", ctypes.c_float), ("step_curv_change", ctypes.c_float), ("faster_rate", ctypes.c_float), ("slower_rate", ctypes.c_float), ("min_update_ratio", ctypes.c_float), ("min_steps_to_stability", ctypes.c_int), ("num_threads", ctypes.c_int), ("print_delay_sec", ctypes.c_int), ("steps_taken", ctypes.c_int), ("logging_step_frequency", ctypes.c_int), ("num_to_update", ctypes.c_int), ("ax_normalized", ctypes.c_bool), ("axi_normalized", ctypes.c_bool), ("ay_normalized", ctypes.c_bool), ("x_normalized", ctypes.c_bool), ("xi_normalized", ctypes.c_bool), ("y_normalized", ctypes.c_bool), ("encode_normalization", ctypes.c_bool), ("apply_shift", ctypes.c_bool), ("keep_best", ctypes.c_bool), ("early_stop", ctypes.c_bool), ("rwork_size", ctypes.c_int), ("iwork_size", ctypes.c_int), ("na", ctypes.c_int), ("nm", ctypes.c_int), ("smg", ctypes.c_int), ("emg", ctypes.c_int), ("smgm", ctypes.c_int), ("emgm", ctypes.c_int), ("smgc", ctypes.c_int), ("emgc", ctypes.c_int), ("sbm", ctypes.c_int), ("ebm", ctypes.c_int), ("sfma", ctypes.c_int), ("efma", ctypes.c_int), ("saxs", ctypes.c_int), ("eaxs", ctypes.c_int), ("saxg", ctypes.c_int), ("eaxg", ctypes.c_int), ("saa", ctypes.c_int), ("eaa", ctypes.c_int), ("say", ctypes.c_int), ("eay", ctypes.c_int), ("sxt", ctypes.c_int), ("ext", ctypes.c_int), ("sayg", ctypes.c_int), ("eayg", ctypes.c_int), ("smxs", ctypes.c_int), ("emxs", ctypes.c_int), ("smxg", ctypes.c_int), ("emxg", ctypes.c_int), ("sma", ctypes.c_int), ("ema", ctypes.c_int), ("syg", ctypes.c_int), ("eyg", ctypes.c_int), ("saxr", ctypes.c_int), ("eaxr", ctypes.c_int), ("saxis", ctypes.c_int), ("eaxis", ctypes.c_int), ("saxir", ctypes.c_int), ("eaxir", ctypes.c_int), ("sayr", ctypes.c_int), ("eayr", ctypes.c_int), ("smxr", ctypes.c_int), ("emxr", ctypes.c_int), ("smxis", ctypes.c_int), ("emxis", ctypes.c_int), ("smxir", ctypes.c_int), ("emxir", ctypes.c_int), ("syr", ctypes.c_int), ("eyr", ctypes.c_int), ("sui", ctypes.c_int), ("eui", ctypes.c_int), ("sbas", ctypes.c_int), ("ebas", ctypes.c_int), ("sbae", ctypes.c_int), ("ebae", ctypes.c_int), ("sbms", ctypes.c_int), ("ebms", ctypes.c_int), ("sbme", ctypes.c_int), ("ebme", ctypes.c_int)]
         # Define an "__init__" that can take a class or keyword arguments as input.
         def __init__(self, value=0, **kwargs):
             # From whatever object (or dictionary) was given, assign internal values.
-            self.mdi = kwargs.get("mdi", getattr(value, "mdi", value))
-            self.mds = kwargs.get("mds", getattr(value, "mds", value))
-            self.mns = kwargs.get("mns", getattr(value, "mns", value))
-            self.mdo = kwargs.get("mdo", getattr(value, "mdo", value))
-            self.mne = kwargs.get("mne", getattr(value, "mne", value))
-            self.mde = kwargs.get("mde", getattr(value, "mde", value))
+            self.adn = kwargs.get("adn", getattr(value, "adn", value))
             self.adi = kwargs.get("adi", getattr(value, "adi", value))
             self.ads = kwargs.get("ads", getattr(value, "ads", value))
             self.ans = kwargs.get("ans", getattr(value, "ans", value))
             self.ado = kwargs.get("ado", getattr(value, "ado", value))
             self.ane = kwargs.get("ane", getattr(value, "ane", value))
             self.ade = kwargs.get("ade", getattr(value, "ade", value))
+            self.mdn = kwargs.get("mdn", getattr(value, "mdn", value))
+            self.mdi = kwargs.get("mdi", getattr(value, "mdi", value))
+            self.mds = kwargs.get("mds", getattr(value, "mds", value))
+            self.mns = kwargs.get("mns", getattr(value, "mns", value))
+            self.mdo = kwargs.get("mdo", getattr(value, "mdo", value))
+            self.mne = kwargs.get("mne", getattr(value, "mne", value))
+            self.mde = kwargs.get("mde", getattr(value, "mde", value))
             self.total_size = kwargs.get("total_size", getattr(value, "total_size", value))
             self.num_vars = kwargs.get("num_vars", getattr(value, "num_vars", value))
-            self.msiv = kwargs.get("msiv", getattr(value, "msiv", value))
-            self.meiv = kwargs.get("meiv", getattr(value, "meiv", value))
-            self.msis = kwargs.get("msis", getattr(value, "msis", value))
-            self.meis = kwargs.get("meis", getattr(value, "meis", value))
-            self.mssv = kwargs.get("mssv", getattr(value, "mssv", value))
-            self.mesv = kwargs.get("mesv", getattr(value, "mesv", value))
-            self.msss = kwargs.get("msss", getattr(value, "msss", value))
-            self.mess = kwargs.get("mess", getattr(value, "mess", value))
-            self.msov = kwargs.get("msov", getattr(value, "msov", value))
-            self.meov = kwargs.get("meov", getattr(value, "meov", value))
-            self.msev = kwargs.get("msev", getattr(value, "msev", value))
-            self.meev = kwargs.get("meev", getattr(value, "meev", value))
             self.asiv = kwargs.get("asiv", getattr(value, "asiv", value))
             self.aeiv = kwargs.get("aeiv", getattr(value, "aeiv", value))
             self.asis = kwargs.get("asis", getattr(value, "asis", value))
             self.aeis = kwargs.get("aeis", getattr(value, "aeis", value))
             self.assv = kwargs.get("assv", getattr(value, "assv", value))
             self.aesv = kwargs.get("aesv", getattr(value, "aesv", value))
             self.asss = kwargs.get("asss", getattr(value, "asss", value))
             self.aess = kwargs.get("aess", getattr(value, "aess", value))
             self.asov = kwargs.get("asov", getattr(value, "asov", value))
             self.aeov = kwargs.get("aeov", getattr(value, "aeov", value))
             self.asev = kwargs.get("asev", getattr(value, "asev", value))
             self.aeev = kwargs.get("aeev", getattr(value, "aeev", value))
+            self.msiv = kwargs.get("msiv", getattr(value, "msiv", value))
+            self.meiv = kwargs.get("meiv", getattr(value, "meiv", value))
+            self.msis = kwargs.get("msis", getattr(value, "msis", value))
+            self.meis = kwargs.get("meis", getattr(value, "meis", value))
+            self.mssv = kwargs.get("mssv", getattr(value, "mssv", value))
+            self.mesv = kwargs.get("mesv", getattr(value, "mesv", value))
+            self.msss = kwargs.get("msss", getattr(value, "msss", value))
+            self.mess = kwargs.get("mess", getattr(value, "mess", value))
+            self.msov = kwargs.get("msov", getattr(value, "msov", value))
+            self.meov = kwargs.get("meov", getattr(value, "meov", value))
+            self.msev = kwargs.get("msev", getattr(value, "msev", value))
+            self.meev = kwargs.get("meev", getattr(value, "meev", value))
+            self.aiss = kwargs.get("aiss", getattr(value, "aiss", value))
+            self.aise = kwargs.get("aise", getattr(value, "aise", value))
+            self.aoss = kwargs.get("aoss", getattr(value, "aoss", value))
+            self.aose = kwargs.get("aose", getattr(value, "aose", value))
             self.miss = kwargs.get("miss", getattr(value, "miss", value))
             self.mise = kwargs.get("mise", getattr(value, "mise", value))
             self.moss = kwargs.get("moss", getattr(value, "moss", value))
             self.mose = kwargs.get("mose", getattr(value, "mose", value))
-            self.aiss = kwargs.get("aiss", getattr(value, "aiss", value))
-            self.aise = kwargs.get("aise", getattr(value, "aise", value))
             self.discontinuity = kwargs.get("discontinuity", getattr(value, "discontinuity", value))
             self.initial_shift_range = kwargs.get("initial_shift_range", getattr(value, "initial_shift_range", value))
             self.initial_output_scale = kwargs.get("initial_output_scale", getattr(value, "initial_output_scale", value))
-            self.initial_step = kwargs.get("initial_step", getattr(value, "initial_step", value))
-            self.initial_step_mean_change = kwargs.get("initial_step_mean_change", getattr(value, "initial_step_mean_change", value))
-            self.initial_step_curv_change = kwargs.get("initial_step_curv_change", getattr(value, "initial_step_curv_change", value))
+            self.step_factor = kwargs.get("step_factor", getattr(value, "step_factor", value))
+            self.step_mean_change = kwargs.get("step_mean_change", getattr(value, "step_mean_change", value))
+            self.step_curv_change = kwargs.get("step_curv_change", getattr(value, "step_curv_change", value))
             self.faster_rate = kwargs.get("faster_rate", getattr(value, "faster_rate", value))
             self.slower_rate = kwargs.get("slower_rate", getattr(value, "slower_rate", value))
+            self.min_update_ratio = kwargs.get("min_update_ratio", getattr(value, "min_update_ratio", value))
             self.min_steps_to_stability = kwargs.get("min_steps_to_stability", getattr(value, "min_steps_to_stability", value))
             self.num_threads = kwargs.get("num_threads", getattr(value, "num_threads", value))
+            self.print_delay_sec = kwargs.get("print_delay_sec", getattr(value, "print_delay_sec", value))
+            self.steps_taken = kwargs.get("steps_taken", getattr(value, "steps_taken", value))
+            self.logging_step_frequency = kwargs.get("logging_step_frequency", getattr(value, "logging_step_frequency", value))
+            self.num_to_update = kwargs.get("num_to_update", getattr(value, "num_to_update", value))
+            self.ax_normalized = kwargs.get("ax_normalized", getattr(value, "ax_normalized", value))
+            self.axi_normalized = kwargs.get("axi_normalized", getattr(value, "axi_normalized", value))
+            self.ay_normalized = kwargs.get("ay_normalized", getattr(value, "ay_normalized", value))
+            self.x_normalized = kwargs.get("x_normalized", getattr(value, "x_normalized", value))
+            self.xi_normalized = kwargs.get("xi_normalized", getattr(value, "xi_normalized", value))
+            self.y_normalized = kwargs.get("y_normalized", getattr(value, "y_normalized", value))
+            self.encode_normalization = kwargs.get("encode_normalization", getattr(value, "encode_normalization", value))
+            self.apply_shift = kwargs.get("apply_shift", getattr(value, "apply_shift", value))
             self.keep_best = kwargs.get("keep_best", getattr(value, "keep_best", value))
             self.early_stop = kwargs.get("early_stop", getattr(value, "early_stop", value))
+            self.rwork_size = kwargs.get("rwork_size", getattr(value, "rwork_size", value))
+            self.iwork_size = kwargs.get("iwork_size", getattr(value, "iwork_size", value))
+            self.na = kwargs.get("na", getattr(value, "na", value))
+            self.nm = kwargs.get("nm", getattr(value, "nm", value))
+            self.smg = kwargs.get("smg", getattr(value, "smg", value))
+            self.emg = kwargs.get("emg", getattr(value, "emg", value))
+            self.smgm = kwargs.get("smgm", getattr(value, "smgm", value))
+            self.emgm = kwargs.get("emgm", getattr(value, "emgm", value))
+            self.smgc = kwargs.get("smgc", getattr(value, "smgc", value))
+            self.emgc = kwargs.get("emgc", getattr(value, "emgc", value))
+            self.sbm = kwargs.get("sbm", getattr(value, "sbm", value))
+            self.ebm = kwargs.get("ebm", getattr(value, "ebm", value))
+            self.sfma = kwargs.get("sfma", getattr(value, "sfma", value))
+            self.efma = kwargs.get("efma", getattr(value, "efma", value))
+            self.saxs = kwargs.get("saxs", getattr(value, "saxs", value))
+            self.eaxs = kwargs.get("eaxs", getattr(value, "eaxs", value))
+            self.saxg = kwargs.get("saxg", getattr(value, "saxg", value))
+            self.eaxg = kwargs.get("eaxg", getattr(value, "eaxg", value))
+            self.saa = kwargs.get("saa", getattr(value, "saa", value))
+            self.eaa = kwargs.get("eaa", getattr(value, "eaa", value))
+            self.say = kwargs.get("say", getattr(value, "say", value))
+            self.eay = kwargs.get("eay", getattr(value, "eay", value))
+            self.sxt = kwargs.get("sxt", getattr(value, "sxt", value))
+            self.ext = kwargs.get("ext", getattr(value, "ext", value))
+            self.sayg = kwargs.get("sayg", getattr(value, "sayg", value))
+            self.eayg = kwargs.get("eayg", getattr(value, "eayg", value))
+            self.smxs = kwargs.get("smxs", getattr(value, "smxs", value))
+            self.emxs = kwargs.get("emxs", getattr(value, "emxs", value))
+            self.smxg = kwargs.get("smxg", getattr(value, "smxg", value))
+            self.emxg = kwargs.get("emxg", getattr(value, "emxg", value))
+            self.sma = kwargs.get("sma", getattr(value, "sma", value))
+            self.ema = kwargs.get("ema", getattr(value, "ema", value))
+            self.syg = kwargs.get("syg", getattr(value, "syg", value))
+            self.eyg = kwargs.get("eyg", getattr(value, "eyg", value))
+            self.saxr = kwargs.get("saxr", getattr(value, "saxr", value))
+            self.eaxr = kwargs.get("eaxr", getattr(value, "eaxr", value))
+            self.saxis = kwargs.get("saxis", getattr(value, "saxis", value))
+            self.eaxis = kwargs.get("eaxis", getattr(value, "eaxis", value))
+            self.saxir = kwargs.get("saxir", getattr(value, "saxir", value))
+            self.eaxir = kwargs.get("eaxir", getattr(value, "eaxir", value))
+            self.sayr = kwargs.get("sayr", getattr(value, "sayr", value))
+            self.eayr = kwargs.get("eayr", getattr(value, "eayr", value))
+            self.smxr = kwargs.get("smxr", getattr(value, "smxr", value))
+            self.emxr = kwargs.get("emxr", getattr(value, "emxr", value))
+            self.smxis = kwargs.get("smxis", getattr(value, "smxis", value))
+            self.emxis = kwargs.get("emxis", getattr(value, "emxis", value))
+            self.smxir = kwargs.get("smxir", getattr(value, "smxir", value))
+            self.emxir = kwargs.get("emxir", getattr(value, "emxir", value))
+            self.syr = kwargs.get("syr", getattr(value, "syr", value))
+            self.eyr = kwargs.get("eyr", getattr(value, "eyr", value))
+            self.sui = kwargs.get("sui", getattr(value, "sui", value))
+            self.eui = kwargs.get("eui", getattr(value, "eui", value))
+            self.sbas = kwargs.get("sbas", getattr(value, "sbas", value))
+            self.ebas = kwargs.get("ebas", getattr(value, "ebas", value))
+            self.sbae = kwargs.get("sbae", getattr(value, "sbae", value))
+            self.ebae = kwargs.get("ebae", getattr(value, "ebae", value))
+            self.sbms = kwargs.get("sbms", getattr(value, "sbms", value))
+            self.ebms = kwargs.get("ebms", getattr(value, "ebms", value))
+            self.sbme = kwargs.get("sbme", getattr(value, "sbme", value))
+            self.ebme = kwargs.get("ebme", getattr(value, "ebme", value))
     
 
     
     # ----------------------------------------------
     # Wrapper for the Fortran subroutine NEW_MODEL_CONFIG
     
-    def new_model_config(self, mdi, mdo, adi, mds=None, mns=None, mne=None, mde=None, ado=None, ads=None, ans=None, ane=None, ade=None, num_threads=None):
+    def new_model_config(self, adn, mdn, mdo, ado=None, ads=None, ans=None, ane=None, ade=None, mds=None, mns=None, mne=None, mde=None, num_threads=None):
         '''! Generate a model configuration given state parameters for the model.
 ! Size related parameters.'''
         MODEL_CONFIG = apos.MODEL_CONFIG
         
-        # Setting up "mdi"
-        if (type(mdi) is not ctypes.c_int): mdi = ctypes.c_int(mdi)
-        
-        # Setting up "mdo"
-        if (type(mdo) is not ctypes.c_int): mdo = ctypes.c_int(mdo)
-        
-        # Setting up "mds"
-        mds_present = ctypes.c_bool(True)
-        if (mds is None):
-            mds_present = ctypes.c_bool(False)
-            mds = ctypes.c_int()
-        else:
-            mds = ctypes.c_int(mds)
-        if (type(mds) is not ctypes.c_int): mds = ctypes.c_int(mds)
-        
-        # Setting up "mns"
-        mns_present = ctypes.c_bool(True)
-        if (mns is None):
-            mns_present = ctypes.c_bool(False)
-            mns = ctypes.c_int()
-        else:
-            mns = ctypes.c_int(mns)
-        if (type(mns) is not ctypes.c_int): mns = ctypes.c_int(mns)
-        
-        # Setting up "mne"
-        mne_present = ctypes.c_bool(True)
-        if (mne is None):
-            mne_present = ctypes.c_bool(False)
-            mne = ctypes.c_int()
-        else:
-            mne = ctypes.c_int(mne)
-        if (type(mne) is not ctypes.c_int): mne = ctypes.c_int(mne)
-        
-        # Setting up "mde"
-        mde_present = ctypes.c_bool(True)
-        if (mde is None):
-            mde_present = ctypes.c_bool(False)
-            mde = ctypes.c_int()
-        else:
-            mde = ctypes.c_int(mde)
-        if (type(mde) is not ctypes.c_int): mde = ctypes.c_int(mde)
-        
-        # Setting up "adi"
-        if (type(adi) is not ctypes.c_int): adi = ctypes.c_int(adi)
+        # Setting up "adn"
+        if (type(adn) is not ctypes.c_int): adn = ctypes.c_int(adn)
         
         # Setting up "ado"
         ado_present = ctypes.c_bool(True)
         if (ado is None):
             ado_present = ctypes.c_bool(False)
             ado = ctypes.c_int()
         else:
@@ -364,28 +851,95 @@
         if (ade is None):
             ade_present = ctypes.c_bool(False)
             ade = ctypes.c_int()
         else:
             ade = ctypes.c_int(ade)
         if (type(ade) is not ctypes.c_int): ade = ctypes.c_int(ade)
         
+        # Setting up "mdn"
+        if (type(mdn) is not ctypes.c_int): mdn = ctypes.c_int(mdn)
+        
+        # Setting up "mdo"
+        if (type(mdo) is not ctypes.c_int): mdo = ctypes.c_int(mdo)
+        
+        # Setting up "mds"
+        mds_present = ctypes.c_bool(True)
+        if (mds is None):
+            mds_present = ctypes.c_bool(False)
+            mds = ctypes.c_int()
+        else:
+            mds = ctypes.c_int(mds)
+        if (type(mds) is not ctypes.c_int): mds = ctypes.c_int(mds)
+        
+        # Setting up "mns"
+        mns_present = ctypes.c_bool(True)
+        if (mns is None):
+            mns_present = ctypes.c_bool(False)
+            mns = ctypes.c_int()
+        else:
+            mns = ctypes.c_int(mns)
+        if (type(mns) is not ctypes.c_int): mns = ctypes.c_int(mns)
+        
+        # Setting up "mne"
+        mne_present = ctypes.c_bool(True)
+        if (mne is None):
+            mne_present = ctypes.c_bool(False)
+            mne = ctypes.c_int()
+        else:
+            mne = ctypes.c_int(mne)
+        if (type(mne) is not ctypes.c_int): mne = ctypes.c_int(mne)
+        
+        # Setting up "mde"
+        mde_present = ctypes.c_bool(True)
+        if (mde is None):
+            mde_present = ctypes.c_bool(False)
+            mde = ctypes.c_int()
+        else:
+            mde = ctypes.c_int(mde)
+        if (type(mde) is not ctypes.c_int): mde = ctypes.c_int(mde)
+        
         # Setting up "num_threads"
         num_threads_present = ctypes.c_bool(True)
         if (num_threads is None):
             num_threads_present = ctypes.c_bool(False)
             num_threads = ctypes.c_int()
         else:
             num_threads = ctypes.c_int(num_threads)
         if (type(num_threads) is not ctypes.c_int): num_threads = ctypes.c_int(num_threads)
         
         # Setting up "config"
         config = MODEL_CONFIG()
     
         # Call C-accessible Fortran wrapper.
-        clib.c_new_model_config(ctypes.byref(mdi), ctypes.byref(mdo), ctypes.byref(mds_present), ctypes.byref(mds), ctypes.byref(mns_present), ctypes.byref(mns), ctypes.byref(mne_present), ctypes.byref(mne), ctypes.byref(mde_present), ctypes.byref(mde), ctypes.byref(adi), ctypes.byref(ado_present), ctypes.byref(ado), ctypes.byref(ads_present), ctypes.byref(ads), ctypes.byref(ans_present), ctypes.byref(ans), ctypes.byref(ane_present), ctypes.byref(ane), ctypes.byref(ade_present), ctypes.byref(ade), ctypes.byref(num_threads_present), ctypes.byref(num_threads), ctypes.byref(config))
+        clib.c_new_model_config(ctypes.byref(adn), ctypes.byref(ado_present), ctypes.byref(ado), ctypes.byref(ads_present), ctypes.byref(ads), ctypes.byref(ans_present), ctypes.byref(ans), ctypes.byref(ane_present), ctypes.byref(ane), ctypes.byref(ade_present), ctypes.byref(ade), ctypes.byref(mdn), ctypes.byref(mdo), ctypes.byref(mds_present), ctypes.byref(mds), ctypes.byref(mns_present), ctypes.byref(mns), ctypes.byref(mne_present), ctypes.byref(mne), ctypes.byref(mde_present), ctypes.byref(mde), ctypes.byref(num_threads_present), ctypes.byref(num_threads), ctypes.byref(config))
+    
+        # Return final results, 'INTENT(OUT)' arguments only.
+        return config
+
+    
+    # ----------------------------------------------
+    # Wrapper for the Fortran subroutine NEW_FIT_CONFIG
+    
+    def new_fit_config(self, nm, na, config):
+        '''! Given a number of X points "NM", and a number of apositional X points
+! "NA", update the "RWORK_SIZE" and "IWORK_SIZE" attributes in "CONFIG"
+! as well as all related work indices for that size data.'''
+        MODEL_CONFIG = apos.MODEL_CONFIG
+        
+        # Setting up "nm"
+        if (type(nm) is not ctypes.c_int): nm = ctypes.c_int(nm)
+        
+        # Setting up "na"
+        if (type(na) is not ctypes.c_int): na = ctypes.c_int(na)
+        
+        # Setting up "config"
+        if (type(config) is not MODEL_CONFIG): config = MODEL_CONFIG(config)
+    
+        # Call C-accessible Fortran wrapper.
+        clib.c_new_fit_config(ctypes.byref(nm), ctypes.byref(na), ctypes.byref(config))
     
         # Return final results, 'INTENT(OUT)' arguments only.
         return config
 
     
     # ----------------------------------------------
     # Wrapper for the Fortran subroutine INIT_MODEL
@@ -421,15 +975,15 @@
         # Return final results, 'INTENT(OUT)' arguments only.
         return model
 
     
     # ----------------------------------------------
     # Wrapper for the Fortran subroutine CHECK_SHAPE
     
-    def check_shape(self, config, model, y, x, xi, ax, axi, sizes):
+    def check_shape(self, config, model, ax, axi, sizes, x, xi, y):
         '''! Returnn nonzero INFO if any shapes or values do not match expectations.'''
         MODEL_CONFIG = apos.MODEL_CONFIG
         
         # Setting up "config"
         if (type(config) is not MODEL_CONFIG): config = MODEL_CONFIG(config)
         
         # Setting up "model"
@@ -437,44 +991,14 @@
             (not numpy.asarray(model).flags.f_contiguous) or
             (not (model.dtype == numpy.dtype(ctypes.c_float)))):
             import warnings
             warnings.warn("The provided argument 'model' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
             model = numpy.asarray(model, dtype=ctypes.c_float, order='F')
         model_dim_1 = ctypes.c_int(model.shape[0])
         
-        # Setting up "y"
-        if ((not issubclass(type(y), numpy.ndarray)) or
-            (not numpy.asarray(y).flags.f_contiguous) or
-            (not (y.dtype == numpy.dtype(ctypes.c_float)))):
-            import warnings
-            warnings.warn("The provided argument 'y' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
-            y = numpy.asarray(y, dtype=ctypes.c_float, order='F')
-        y_dim_1 = ctypes.c_int(y.shape[0])
-        y_dim_2 = ctypes.c_int(y.shape[1])
-        
-        # Setting up "x"
-        if ((not issubclass(type(x), numpy.ndarray)) or
-            (not numpy.asarray(x).flags.f_contiguous) or
-            (not (x.dtype == numpy.dtype(ctypes.c_float)))):
-            import warnings
-            warnings.warn("The provided argument 'x' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
-            x = numpy.asarray(x, dtype=ctypes.c_float, order='F')
-        x_dim_1 = ctypes.c_int(x.shape[0])
-        x_dim_2 = ctypes.c_int(x.shape[1])
-        
-        # Setting up "xi"
-        if ((not issubclass(type(xi), numpy.ndarray)) or
-            (not numpy.asarray(xi).flags.f_contiguous) or
-            (not (xi.dtype == numpy.dtype(ctypes.c_int)))):
-            import warnings
-            warnings.warn("The provided argument 'xi' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
-            xi = numpy.asarray(xi, dtype=ctypes.c_int, order='F')
-        xi_dim_1 = ctypes.c_int(xi.shape[0])
-        xi_dim_2 = ctypes.c_int(xi.shape[1])
-        
         # Setting up "ax"
         if ((not issubclass(type(ax), numpy.ndarray)) or
             (not numpy.asarray(ax).flags.f_contiguous) or
             (not (ax.dtype == numpy.dtype(ctypes.c_float)))):
             import warnings
             warnings.warn("The provided argument 'ax' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
             ax = numpy.asarray(ax, dtype=ctypes.c_float, order='F')
@@ -496,44 +1020,14 @@
             (not numpy.asarray(sizes).flags.f_contiguous) or
             (not (sizes.dtype == numpy.dtype(ctypes.c_int)))):
             import warnings
             warnings.warn("The provided argument 'sizes' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
             sizes = numpy.asarray(sizes, dtype=ctypes.c_int, order='F')
         sizes_dim_1 = ctypes.c_int(sizes.shape[0])
         
-        # Setting up "info"
-        info = ctypes.c_int()
-    
-        # Call C-accessible Fortran wrapper.
-        clib.c_check_shape(ctypes.byref(config), ctypes.byref(model_dim_1), ctypes.c_void_p(model.ctypes.data), ctypes.byref(y_dim_1), ctypes.byref(y_dim_2), ctypes.c_void_p(y.ctypes.data), ctypes.byref(x_dim_1), ctypes.byref(x_dim_2), ctypes.c_void_p(x.ctypes.data), ctypes.byref(xi_dim_1), ctypes.byref(xi_dim_2), ctypes.c_void_p(xi.ctypes.data), ctypes.byref(ax_dim_1), ctypes.byref(ax_dim_2), ctypes.c_void_p(ax.ctypes.data), ctypes.byref(axi_dim_1), ctypes.byref(axi_dim_2), ctypes.c_void_p(axi.ctypes.data), ctypes.byref(sizes_dim_1), ctypes.c_void_p(sizes.ctypes.data), ctypes.byref(info))
-    
-        # Return final results, 'INTENT(OUT)' arguments only.
-        return info.value
-
-    
-    # ----------------------------------------------
-    # Wrapper for the Fortran subroutine EMBED
-    
-    def embed(self, config, model, x, xi, ax, axi, xxi, axxi):
-        '''! Given a model and mixed real and integer inputs, embed the inputs
-!  into their appropriate real-value-only formats.'''
-        MODEL_CONFIG = apos.MODEL_CONFIG
-        
-        # Setting up "config"
-        if (type(config) is not MODEL_CONFIG): config = MODEL_CONFIG(config)
-        
-        # Setting up "model"
-        if ((not issubclass(type(model), numpy.ndarray)) or
-            (not numpy.asarray(model).flags.f_contiguous) or
-            (not (model.dtype == numpy.dtype(ctypes.c_float)))):
-            import warnings
-            warnings.warn("The provided argument 'model' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
-            model = numpy.asarray(model, dtype=ctypes.c_float, order='F')
-        model_dim_1 = ctypes.c_int(model.shape[0])
-        
         # Setting up "x"
         if ((not issubclass(type(x), numpy.ndarray)) or
             (not numpy.asarray(x).flags.f_contiguous) or
             (not (x.dtype == numpy.dtype(ctypes.c_float)))):
             import warnings
             warnings.warn("The provided argument 'x' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
             x = numpy.asarray(x, dtype=ctypes.c_float, order='F')
@@ -546,253 +1040,277 @@
             (not (xi.dtype == numpy.dtype(ctypes.c_int)))):
             import warnings
             warnings.warn("The provided argument 'xi' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
             xi = numpy.asarray(xi, dtype=ctypes.c_int, order='F')
         xi_dim_1 = ctypes.c_int(xi.shape[0])
         xi_dim_2 = ctypes.c_int(xi.shape[1])
         
-        # Setting up "ax"
-        if ((not issubclass(type(ax), numpy.ndarray)) or
-            (not numpy.asarray(ax).flags.f_contiguous) or
-            (not (ax.dtype == numpy.dtype(ctypes.c_float)))):
-            import warnings
-            warnings.warn("The provided argument 'ax' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
-            ax = numpy.asarray(ax, dtype=ctypes.c_float, order='F')
-        ax_dim_1 = ctypes.c_int(ax.shape[0])
-        ax_dim_2 = ctypes.c_int(ax.shape[1])
-        
-        # Setting up "axi"
-        if ((not issubclass(type(axi), numpy.ndarray)) or
-            (not numpy.asarray(axi).flags.f_contiguous) or
-            (not (axi.dtype == numpy.dtype(ctypes.c_int)))):
-            import warnings
-            warnings.warn("The provided argument 'axi' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
-            axi = numpy.asarray(axi, dtype=ctypes.c_int, order='F')
-        axi_dim_1 = ctypes.c_int(axi.shape[0])
-        axi_dim_2 = ctypes.c_int(axi.shape[1])
-        
-        # Setting up "xxi"
-        if ((not issubclass(type(xxi), numpy.ndarray)) or
-            (not numpy.asarray(xxi).flags.f_contiguous) or
-            (not (xxi.dtype == numpy.dtype(ctypes.c_float)))):
+        # Setting up "y"
+        if ((not issubclass(type(y), numpy.ndarray)) or
+            (not numpy.asarray(y).flags.f_contiguous) or
+            (not (y.dtype == numpy.dtype(ctypes.c_float)))):
             import warnings
-            warnings.warn("The provided argument 'xxi' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
-            xxi = numpy.asarray(xxi, dtype=ctypes.c_float, order='F')
-        xxi_dim_1 = ctypes.c_int(xxi.shape[0])
-        xxi_dim_2 = ctypes.c_int(xxi.shape[1])
+            warnings.warn("The provided argument 'y' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            y = numpy.asarray(y, dtype=ctypes.c_float, order='F')
+        y_dim_1 = ctypes.c_int(y.shape[0])
+        y_dim_2 = ctypes.c_int(y.shape[1])
         
-        # Setting up "axxi"
-        if ((not issubclass(type(axxi), numpy.ndarray)) or
-            (not numpy.asarray(axxi).flags.f_contiguous) or
-            (not (axxi.dtype == numpy.dtype(ctypes.c_float)))):
-            import warnings
-            warnings.warn("The provided argument 'axxi' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
-            axxi = numpy.asarray(axxi, dtype=ctypes.c_float, order='F')
-        axxi_dim_1 = ctypes.c_int(axxi.shape[0])
-        axxi_dim_2 = ctypes.c_int(axxi.shape[1])
+        # Setting up "info"
+        info = ctypes.c_int()
     
         # Call C-accessible Fortran wrapper.
-        clib.c_embed(ctypes.byref(config), ctypes.byref(model_dim_1), ctypes.c_void_p(model.ctypes.data), ctypes.byref(x_dim_1), ctypes.byref(x_dim_2), ctypes.c_void_p(x.ctypes.data), ctypes.byref(xi_dim_1), ctypes.byref(xi_dim_2), ctypes.c_void_p(xi.ctypes.data), ctypes.byref(ax_dim_1), ctypes.byref(ax_dim_2), ctypes.c_void_p(ax.ctypes.data), ctypes.byref(axi_dim_1), ctypes.byref(axi_dim_2), ctypes.c_void_p(axi.ctypes.data), ctypes.byref(xxi_dim_1), ctypes.byref(xxi_dim_2), ctypes.c_void_p(xxi.ctypes.data), ctypes.byref(axxi_dim_1), ctypes.byref(axxi_dim_2), ctypes.c_void_p(axxi.ctypes.data))
+        clib.c_check_shape(ctypes.byref(config), ctypes.byref(model_dim_1), ctypes.c_void_p(model.ctypes.data), ctypes.byref(ax_dim_1), ctypes.byref(ax_dim_2), ctypes.c_void_p(ax.ctypes.data), ctypes.byref(axi_dim_1), ctypes.byref(axi_dim_2), ctypes.c_void_p(axi.ctypes.data), ctypes.byref(sizes_dim_1), ctypes.c_void_p(sizes.ctypes.data), ctypes.byref(x_dim_1), ctypes.byref(x_dim_2), ctypes.c_void_p(x.ctypes.data), ctypes.byref(xi_dim_1), ctypes.byref(xi_dim_2), ctypes.c_void_p(xi.ctypes.data), ctypes.byref(y_dim_1), ctypes.byref(y_dim_2), ctypes.c_void_p(y.ctypes.data), ctypes.byref(info))
     
         # Return final results, 'INTENT(OUT)' arguments only.
-        return xxi, axxi
+        return info.value
 
     
     # ----------------------------------------------
     # Wrapper for the Fortran subroutine COMPUTE_BATCHES
     
-    def compute_batches(self, num_batches, x, ax, sizes, batcha, batchm, info):
+    def compute_batches(self, num_batches, nm, na, sizes, batcha_starts, batcha_ends, batchm_starts, batchm_ends, info):
         '''! Given a number of batches, compute the batch start and ends for
 !  the apositional and positional inputs. Store in (2,_) arrays.'''
         MODEL_CONFIG = apos.MODEL_CONFIG
         
         # Setting up "num_batches"
         if (type(num_batches) is not ctypes.c_int): num_batches = ctypes.c_int(num_batches)
         
-        # Setting up "x"
-        if ((not issubclass(type(x), numpy.ndarray)) or
-            (not numpy.asarray(x).flags.f_contiguous) or
-            (not (x.dtype == numpy.dtype(ctypes.c_float)))):
-            import warnings
-            warnings.warn("The provided argument 'x' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
-            x = numpy.asarray(x, dtype=ctypes.c_float, order='F')
-        x_dim_1 = ctypes.c_int(x.shape[0])
-        x_dim_2 = ctypes.c_int(x.shape[1])
+        # Setting up "nm"
+        if (type(nm) is not ctypes.c_int): nm = ctypes.c_int(nm)
         
-        # Setting up "ax"
-        if ((not issubclass(type(ax), numpy.ndarray)) or
-            (not numpy.asarray(ax).flags.f_contiguous) or
-            (not (ax.dtype == numpy.dtype(ctypes.c_float)))):
-            import warnings
-            warnings.warn("The provided argument 'ax' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
-            ax = numpy.asarray(ax, dtype=ctypes.c_float, order='F')
-        ax_dim_1 = ctypes.c_int(ax.shape[0])
-        ax_dim_2 = ctypes.c_int(ax.shape[1])
+        # Setting up "na"
+        if (type(na) is not ctypes.c_int): na = ctypes.c_int(na)
         
         # Setting up "sizes"
         if ((not issubclass(type(sizes), numpy.ndarray)) or
             (not numpy.asarray(sizes).flags.f_contiguous) or
             (not (sizes.dtype == numpy.dtype(ctypes.c_int)))):
             import warnings
             warnings.warn("The provided argument 'sizes' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
             sizes = numpy.asarray(sizes, dtype=ctypes.c_int, order='F')
         sizes_dim_1 = ctypes.c_int(sizes.shape[0])
         
-        # Setting up "batcha"
-        if ((not issubclass(type(batcha), numpy.ndarray)) or
-            (not numpy.asarray(batcha).flags.f_contiguous) or
-            (not (batcha.dtype == numpy.dtype(ctypes.c_int)))):
-            import warnings
-            warnings.warn("The provided argument 'batcha' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
-            batcha = numpy.asarray(batcha, dtype=ctypes.c_int, order='F')
-        batcha_dim_1 = ctypes.c_int(batcha.shape[0])
-        batcha_dim_2 = ctypes.c_int(batcha.shape[1])
-        
-        # Setting up "batchm"
-        if ((not issubclass(type(batchm), numpy.ndarray)) or
-            (not numpy.asarray(batchm).flags.f_contiguous) or
-            (not (batchm.dtype == numpy.dtype(ctypes.c_int)))):
-            import warnings
-            warnings.warn("The provided argument 'batchm' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
-            batchm = numpy.asarray(batchm, dtype=ctypes.c_int, order='F')
-        batchm_dim_1 = ctypes.c_int(batchm.shape[0])
-        batchm_dim_2 = ctypes.c_int(batchm.shape[1])
+        # Setting up "batcha_starts"
+        if ((not issubclass(type(batcha_starts), numpy.ndarray)) or
+            (not numpy.asarray(batcha_starts).flags.f_contiguous) or
+            (not (batcha_starts.dtype == numpy.dtype(ctypes.c_int)))):
+            import warnings
+            warnings.warn("The provided argument 'batcha_starts' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
+            batcha_starts = numpy.asarray(batcha_starts, dtype=ctypes.c_int, order='F')
+        batcha_starts_dim_1 = ctypes.c_int(batcha_starts.shape[0])
+        
+        # Setting up "batcha_ends"
+        if ((not issubclass(type(batcha_ends), numpy.ndarray)) or
+            (not numpy.asarray(batcha_ends).flags.f_contiguous) or
+            (not (batcha_ends.dtype == numpy.dtype(ctypes.c_int)))):
+            import warnings
+            warnings.warn("The provided argument 'batcha_ends' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
+            batcha_ends = numpy.asarray(batcha_ends, dtype=ctypes.c_int, order='F')
+        batcha_ends_dim_1 = ctypes.c_int(batcha_ends.shape[0])
+        
+        # Setting up "batchm_starts"
+        if ((not issubclass(type(batchm_starts), numpy.ndarray)) or
+            (not numpy.asarray(batchm_starts).flags.f_contiguous) or
+            (not (batchm_starts.dtype == numpy.dtype(ctypes.c_int)))):
+            import warnings
+            warnings.warn("The provided argument 'batchm_starts' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
+            batchm_starts = numpy.asarray(batchm_starts, dtype=ctypes.c_int, order='F')
+        batchm_starts_dim_1 = ctypes.c_int(batchm_starts.shape[0])
+        
+        # Setting up "batchm_ends"
+        if ((not issubclass(type(batchm_ends), numpy.ndarray)) or
+            (not numpy.asarray(batchm_ends).flags.f_contiguous) or
+            (not (batchm_ends.dtype == numpy.dtype(ctypes.c_int)))):
+            import warnings
+            warnings.warn("The provided argument 'batchm_ends' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
+            batchm_ends = numpy.asarray(batchm_ends, dtype=ctypes.c_int, order='F')
+        batchm_ends_dim_1 = ctypes.c_int(batchm_ends.shape[0])
         
         # Setting up "info"
         if (type(info) is not ctypes.c_int): info = ctypes.c_int(info)
     
         # Call C-accessible Fortran wrapper.
-        clib.c_compute_batches(ctypes.byref(num_batches), ctypes.byref(x_dim_1), ctypes.byref(x_dim_2), ctypes.c_void_p(x.ctypes.data), ctypes.byref(ax_dim_1), ctypes.byref(ax_dim_2), ctypes.c_void_p(ax.ctypes.data), ctypes.byref(sizes_dim_1), ctypes.c_void_p(sizes.ctypes.data), ctypes.byref(batcha_dim_1), ctypes.byref(batcha_dim_2), ctypes.c_void_p(batcha.ctypes.data), ctypes.byref(batchm_dim_1), ctypes.byref(batchm_dim_2), ctypes.c_void_p(batchm.ctypes.data), ctypes.byref(info))
+        clib.c_compute_batches(ctypes.byref(num_batches), ctypes.byref(nm), ctypes.byref(na), ctypes.byref(sizes_dim_1), ctypes.c_void_p(sizes.ctypes.data), ctypes.byref(batcha_starts_dim_1), ctypes.c_void_p(batcha_starts.ctypes.data), ctypes.byref(batcha_ends_dim_1), ctypes.c_void_p(batcha_ends.ctypes.data), ctypes.byref(batchm_starts_dim_1), ctypes.c_void_p(batchm_starts.ctypes.data), ctypes.byref(batchm_ends_dim_1), ctypes.c_void_p(batchm_ends.ctypes.data), ctypes.byref(info))
     
         # Return final results, 'INTENT(OUT)' arguments only.
-        return batcha, batchm, info.value
+        return batcha_starts, batcha_ends, batchm_starts, batchm_ends, info.value
 
     
     # ----------------------------------------------
-    # Wrapper for the Fortran subroutine EVALUATE
+    # Wrapper for the Fortran subroutine EMBED
     
-    def evaluate(self, config, model, y, x, ax, sizes, m_states, a_states, ay, info, shift=None, threads=None):
-        '''! Evaluate the piecewise linear regression model, assume already-embedded inputs.'''
+    def embed(self, config, model, axi, xi, ax, x):
+        '''! Given a model and mixed real and integer inputs, embed the integer
+!  inputs into their appropriate real-value-only formats.'''
         MODEL_CONFIG = apos.MODEL_CONFIG
         
         # Setting up "config"
         if (type(config) is not MODEL_CONFIG): config = MODEL_CONFIG(config)
         
         # Setting up "model"
         if ((not issubclass(type(model), numpy.ndarray)) or
             (not numpy.asarray(model).flags.f_contiguous) or
             (not (model.dtype == numpy.dtype(ctypes.c_float)))):
             import warnings
             warnings.warn("The provided argument 'model' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
             model = numpy.asarray(model, dtype=ctypes.c_float, order='F')
         model_dim_1 = ctypes.c_int(model.shape[0])
         
-        # Setting up "y"
-        if ((not issubclass(type(y), numpy.ndarray)) or
-            (not numpy.asarray(y).flags.f_contiguous) or
-            (not (y.dtype == numpy.dtype(ctypes.c_float)))):
+        # Setting up "axi"
+        if ((not issubclass(type(axi), numpy.ndarray)) or
+            (not numpy.asarray(axi).flags.f_contiguous) or
+            (not (axi.dtype == numpy.dtype(ctypes.c_int)))):
             import warnings
-            warnings.warn("The provided argument 'y' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
-            y = numpy.asarray(y, dtype=ctypes.c_float, order='F')
-        y_dim_1 = ctypes.c_int(y.shape[0])
-        y_dim_2 = ctypes.c_int(y.shape[1])
+            warnings.warn("The provided argument 'axi' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
+            axi = numpy.asarray(axi, dtype=ctypes.c_int, order='F')
+        axi_dim_1 = ctypes.c_int(axi.shape[0])
+        axi_dim_2 = ctypes.c_int(axi.shape[1])
+        
+        # Setting up "xi"
+        if ((not issubclass(type(xi), numpy.ndarray)) or
+            (not numpy.asarray(xi).flags.f_contiguous) or
+            (not (xi.dtype == numpy.dtype(ctypes.c_int)))):
+            import warnings
+            warnings.warn("The provided argument 'xi' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
+            xi = numpy.asarray(xi, dtype=ctypes.c_int, order='F')
+        xi_dim_1 = ctypes.c_int(xi.shape[0])
+        xi_dim_2 = ctypes.c_int(xi.shape[1])
+        
+        # Setting up "ax"
+        if ((not issubclass(type(ax), numpy.ndarray)) or
+            (not numpy.asarray(ax).flags.f_contiguous) or
+            (not (ax.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 'ax' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            ax = numpy.asarray(ax, dtype=ctypes.c_float, order='F')
+        ax_dim_1 = ctypes.c_int(ax.shape[0])
+        ax_dim_2 = ctypes.c_int(ax.shape[1])
         
         # Setting up "x"
         if ((not issubclass(type(x), numpy.ndarray)) or
             (not numpy.asarray(x).flags.f_contiguous) or
             (not (x.dtype == numpy.dtype(ctypes.c_float)))):
             import warnings
             warnings.warn("The provided argument 'x' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
             x = numpy.asarray(x, dtype=ctypes.c_float, order='F')
         x_dim_1 = ctypes.c_int(x.shape[0])
         x_dim_2 = ctypes.c_int(x.shape[1])
+    
+        # Call C-accessible Fortran wrapper.
+        clib.c_embed(ctypes.byref(config), ctypes.byref(model_dim_1), ctypes.c_void_p(model.ctypes.data), ctypes.byref(axi_dim_1), ctypes.byref(axi_dim_2), ctypes.c_void_p(axi.ctypes.data), ctypes.byref(xi_dim_1), ctypes.byref(xi_dim_2), ctypes.c_void_p(xi.ctypes.data), ctypes.byref(ax_dim_1), ctypes.byref(ax_dim_2), ctypes.c_void_p(ax.ctypes.data), ctypes.byref(x_dim_1), ctypes.byref(x_dim_2), ctypes.c_void_p(x.ctypes.data))
+    
+        # Return final results, 'INTENT(OUT)' arguments only.
+        return ax, x
+
+    
+    # ----------------------------------------------
+    # Wrapper for the Fortran subroutine EVALUATE
+    
+    def evaluate(self, config, model, ax, ay, sizes, x, y, a_states, m_states, info):
+        '''! Evaluate the piecewise linear regression model, assume already-embedded inputs.'''
+        MODEL_CONFIG = apos.MODEL_CONFIG
+        
+        # Setting up "config"
+        if (type(config) is not MODEL_CONFIG): config = MODEL_CONFIG(config)
+        
+        # Setting up "model"
+        if ((not issubclass(type(model), numpy.ndarray)) or
+            (not numpy.asarray(model).flags.f_contiguous) or
+            (not (model.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 'model' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            model = numpy.asarray(model, dtype=ctypes.c_float, order='F')
+        model_dim_1 = ctypes.c_int(model.shape[0])
         
         # Setting up "ax"
         if ((not issubclass(type(ax), numpy.ndarray)) or
             (not numpy.asarray(ax).flags.f_contiguous) or
             (not (ax.dtype == numpy.dtype(ctypes.c_float)))):
             import warnings
             warnings.warn("The provided argument 'ax' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
             ax = numpy.asarray(ax, dtype=ctypes.c_float, order='F')
         ax_dim_1 = ctypes.c_int(ax.shape[0])
         ax_dim_2 = ctypes.c_int(ax.shape[1])
         
+        # Setting up "ay"
+        if ((not issubclass(type(ay), numpy.ndarray)) or
+            (not numpy.asarray(ay).flags.f_contiguous) or
+            (not (ay.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 'ay' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            ay = numpy.asarray(ay, dtype=ctypes.c_float, order='F')
+        ay_dim_1 = ctypes.c_int(ay.shape[0])
+        ay_dim_2 = ctypes.c_int(ay.shape[1])
+        
         # Setting up "sizes"
         if ((not issubclass(type(sizes), numpy.ndarray)) or
             (not numpy.asarray(sizes).flags.f_contiguous) or
             (not (sizes.dtype == numpy.dtype(ctypes.c_int)))):
             import warnings
             warnings.warn("The provided argument 'sizes' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
             sizes = numpy.asarray(sizes, dtype=ctypes.c_int, order='F')
         sizes_dim_1 = ctypes.c_int(sizes.shape[0])
         
-        # Setting up "m_states"
-        if ((not issubclass(type(m_states), numpy.ndarray)) or
-            (not numpy.asarray(m_states).flags.f_contiguous) or
-            (not (m_states.dtype == numpy.dtype(ctypes.c_float)))):
+        # Setting up "x"
+        if ((not issubclass(type(x), numpy.ndarray)) or
+            (not numpy.asarray(x).flags.f_contiguous) or
+            (not (x.dtype == numpy.dtype(ctypes.c_float)))):
             import warnings
-            warnings.warn("The provided argument 'm_states' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
-            m_states = numpy.asarray(m_states, dtype=ctypes.c_float, order='F')
-        m_states_dim_1 = ctypes.c_int(m_states.shape[0])
-        m_states_dim_2 = ctypes.c_int(m_states.shape[1])
-        m_states_dim_3 = ctypes.c_int(m_states.shape[2])
+            warnings.warn("The provided argument 'x' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            x = numpy.asarray(x, dtype=ctypes.c_float, order='F')
+        x_dim_1 = ctypes.c_int(x.shape[0])
+        x_dim_2 = ctypes.c_int(x.shape[1])
+        
+        # Setting up "y"
+        if ((not issubclass(type(y), numpy.ndarray)) or
+            (not numpy.asarray(y).flags.f_contiguous) or
+            (not (y.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 'y' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            y = numpy.asarray(y, dtype=ctypes.c_float, order='F')
+        y_dim_1 = ctypes.c_int(y.shape[0])
+        y_dim_2 = ctypes.c_int(y.shape[1])
         
         # Setting up "a_states"
         if ((not issubclass(type(a_states), numpy.ndarray)) or
             (not numpy.asarray(a_states).flags.f_contiguous) or
             (not (a_states.dtype == numpy.dtype(ctypes.c_float)))):
             import warnings
             warnings.warn("The provided argument 'a_states' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
             a_states = numpy.asarray(a_states, dtype=ctypes.c_float, order='F')
         a_states_dim_1 = ctypes.c_int(a_states.shape[0])
         a_states_dim_2 = ctypes.c_int(a_states.shape[1])
         a_states_dim_3 = ctypes.c_int(a_states.shape[2])
         
-        # Setting up "ay"
-        if ((not issubclass(type(ay), numpy.ndarray)) or
-            (not numpy.asarray(ay).flags.f_contiguous) or
-            (not (ay.dtype == numpy.dtype(ctypes.c_float)))):
+        # Setting up "m_states"
+        if ((not issubclass(type(m_states), numpy.ndarray)) or
+            (not numpy.asarray(m_states).flags.f_contiguous) or
+            (not (m_states.dtype == numpy.dtype(ctypes.c_float)))):
             import warnings
-            warnings.warn("The provided argument 'ay' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
-            ay = numpy.asarray(ay, dtype=ctypes.c_float, order='F')
-        ay_dim_1 = ctypes.c_int(ay.shape[0])
-        ay_dim_2 = ctypes.c_int(ay.shape[1])
+            warnings.warn("The provided argument 'm_states' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            m_states = numpy.asarray(m_states, dtype=ctypes.c_float, order='F')
+        m_states_dim_1 = ctypes.c_int(m_states.shape[0])
+        m_states_dim_2 = ctypes.c_int(m_states.shape[1])
+        m_states_dim_3 = ctypes.c_int(m_states.shape[2])
         
         # Setting up "info"
         if (type(info) is not ctypes.c_int): info = ctypes.c_int(info)
-        
-        # Setting up "shift"
-        shift_present = ctypes.c_bool(True)
-        if (shift is None):
-            shift_present = ctypes.c_bool(False)
-            shift = ctypes.c_bool()
-        else:
-            shift = ctypes.c_bool(shift)
-        if (type(shift) is not ctypes.c_bool): shift = ctypes.c_bool(shift)
-        
-        # Setting up "threads"
-        threads_present = ctypes.c_bool(True)
-        if (threads is None):
-            threads_present = ctypes.c_bool(False)
-            threads = ctypes.c_int()
-        else:
-            threads = ctypes.c_int(threads)
-        if (type(threads) is not ctypes.c_int): threads = ctypes.c_int(threads)
     
         # Call C-accessible Fortran wrapper.
-        clib.c_evaluate(ctypes.byref(config), ctypes.byref(model_dim_1), ctypes.c_void_p(model.ctypes.data), ctypes.byref(y_dim_1), ctypes.byref(y_dim_2), ctypes.c_void_p(y.ctypes.data), ctypes.byref(x_dim_1), ctypes.byref(x_dim_2), ctypes.c_void_p(x.ctypes.data), ctypes.byref(ax_dim_1), ctypes.byref(ax_dim_2), ctypes.c_void_p(ax.ctypes.data), ctypes.byref(sizes_dim_1), ctypes.c_void_p(sizes.ctypes.data), ctypes.byref(m_states_dim_1), ctypes.byref(m_states_dim_2), ctypes.byref(m_states_dim_3), ctypes.c_void_p(m_states.ctypes.data), ctypes.byref(a_states_dim_1), ctypes.byref(a_states_dim_2), ctypes.byref(a_states_dim_3), ctypes.c_void_p(a_states.ctypes.data), ctypes.byref(ay_dim_1), ctypes.byref(ay_dim_2), ctypes.c_void_p(ay.ctypes.data), ctypes.byref(info), ctypes.byref(shift_present), ctypes.byref(shift), ctypes.byref(threads_present), ctypes.byref(threads))
+        clib.c_evaluate(ctypes.byref(config), ctypes.byref(model_dim_1), ctypes.c_void_p(model.ctypes.data), ctypes.byref(ax_dim_1), ctypes.byref(ax_dim_2), ctypes.c_void_p(ax.ctypes.data), ctypes.byref(ay_dim_1), ctypes.byref(ay_dim_2), ctypes.c_void_p(ay.ctypes.data), ctypes.byref(sizes_dim_1), ctypes.c_void_p(sizes.ctypes.data), ctypes.byref(x_dim_1), ctypes.byref(x_dim_2), ctypes.c_void_p(x.ctypes.data), ctypes.byref(y_dim_1), ctypes.byref(y_dim_2), ctypes.c_void_p(y.ctypes.data), ctypes.byref(a_states_dim_1), ctypes.byref(a_states_dim_2), ctypes.byref(a_states_dim_3), ctypes.c_void_p(a_states.ctypes.data), ctypes.byref(m_states_dim_1), ctypes.byref(m_states_dim_2), ctypes.byref(m_states_dim_3), ctypes.c_void_p(m_states.ctypes.data), ctypes.byref(info))
     
         # Return final results, 'INTENT(OUT)' arguments only.
-        return y, x, ax, m_states, a_states, ay, info.value
+        return ax, ay, x, y, a_states, m_states, info.value
 
     
     # ----------------------------------------------
     # Wrapper for the Fortran subroutine BASIS_GRADIENT
     
-    def basis_gradient(self, config, model, y, x, ax, sizes, m_states, a_states, ay, grad, skip_embeddings=None):
+    def basis_gradient(self, config, model, y, x, ax, sizes, m_states, a_states, ay, grad):
         '''! Given the values at all internal states in the model and an output
 !  gradient, propogate the output gradient through the model and
 !  return the gradient of all basis functions.'''
         MODEL_CONFIG = apos.MODEL_CONFIG
         
         # Setting up "config"
         if (type(config) is not MODEL_CONFIG): config = MODEL_CONFIG(config)
@@ -881,26 +1399,17 @@
         if ((not issubclass(type(grad), numpy.ndarray)) or
             (not numpy.asarray(grad).flags.f_contiguous) or
             (not (grad.dtype == numpy.dtype(ctypes.c_float)))):
             import warnings
             warnings.warn("The provided argument 'grad' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
             grad = numpy.asarray(grad, dtype=ctypes.c_float, order='F')
         grad_dim_1 = ctypes.c_int(grad.shape[0])
-        
-        # Setting up "skip_embeddings"
-        skip_embeddings_present = ctypes.c_bool(True)
-        if (skip_embeddings is None):
-            skip_embeddings_present = ctypes.c_bool(False)
-            skip_embeddings = ctypes.c_bool()
-        else:
-            skip_embeddings = ctypes.c_bool(skip_embeddings)
-        if (type(skip_embeddings) is not ctypes.c_bool): skip_embeddings = ctypes.c_bool(skip_embeddings)
     
         # Call C-accessible Fortran wrapper.
-        clib.c_basis_gradient(ctypes.byref(config), ctypes.byref(model_dim_1), ctypes.c_void_p(model.ctypes.data), ctypes.byref(y_dim_1), ctypes.byref(y_dim_2), ctypes.c_void_p(y.ctypes.data), ctypes.byref(x_dim_1), ctypes.byref(x_dim_2), ctypes.c_void_p(x.ctypes.data), ctypes.byref(ax_dim_1), ctypes.byref(ax_dim_2), ctypes.c_void_p(ax.ctypes.data), ctypes.byref(sizes_dim_1), ctypes.c_void_p(sizes.ctypes.data), ctypes.byref(m_states_dim_1), ctypes.byref(m_states_dim_2), ctypes.byref(m_states_dim_3), ctypes.c_void_p(m_states.ctypes.data), ctypes.byref(a_states_dim_1), ctypes.byref(a_states_dim_2), ctypes.byref(a_states_dim_3), ctypes.c_void_p(a_states.ctypes.data), ctypes.byref(ay_dim_1), ctypes.byref(ay_dim_2), ctypes.c_void_p(ay.ctypes.data), ctypes.byref(grad_dim_1), ctypes.c_void_p(grad.ctypes.data), ctypes.byref(skip_embeddings_present), ctypes.byref(skip_embeddings))
+        clib.c_basis_gradient(ctypes.byref(config), ctypes.byref(model_dim_1), ctypes.c_void_p(model.ctypes.data), ctypes.byref(y_dim_1), ctypes.byref(y_dim_2), ctypes.c_void_p(y.ctypes.data), ctypes.byref(x_dim_1), ctypes.byref(x_dim_2), ctypes.c_void_p(x.ctypes.data), ctypes.byref(ax_dim_1), ctypes.byref(ax_dim_2), ctypes.c_void_p(ax.ctypes.data), ctypes.byref(sizes_dim_1), ctypes.c_void_p(sizes.ctypes.data), ctypes.byref(m_states_dim_1), ctypes.byref(m_states_dim_2), ctypes.byref(m_states_dim_3), ctypes.c_void_p(m_states.ctypes.data), ctypes.byref(a_states_dim_1), ctypes.byref(a_states_dim_2), ctypes.byref(a_states_dim_3), ctypes.c_void_p(a_states.ctypes.data), ctypes.byref(ay_dim_1), ctypes.byref(ay_dim_2), ctypes.c_void_p(ay.ctypes.data), ctypes.byref(grad_dim_1), ctypes.c_void_p(grad.ctypes.data))
     
         # Return final results, 'INTENT(OUT)' arguments only.
         return x, ax, m_states, a_states, ay, grad
 
     
     # ----------------------------------------------
     # Wrapper for the Fortran subroutine EMBEDDING_GRADIENT
@@ -950,88 +1459,17 @@
         clib.c_embedding_gradient(ctypes.byref(mde), ctypes.byref(mne), ctypes.byref(int_inputs_dim_1), ctypes.byref(int_inputs_dim_2), ctypes.c_void_p(int_inputs.ctypes.data), ctypes.byref(grad_dim_1), ctypes.byref(grad_dim_2), ctypes.c_void_p(grad.ctypes.data), ctypes.byref(embedding_grad_dim_1), ctypes.byref(embedding_grad_dim_2), ctypes.c_void_p(embedding_grad.ctypes.data))
     
         # Return final results, 'INTENT(OUT)' arguments only.
         return embedding_grad
 
     
     # ----------------------------------------------
-    # Wrapper for the Fortran subroutine SQUARED_ERROR_GRADIENT
-    
-    def squared_error_gradient(self, targets, outputs):
-        '''! Compute the sum of squared error, store the gradient in the OUTPUTS.
-!   TARGETS - row vectors containing target values
-!   OUTPUTS - column vectors containing model predictions'''
-        MODEL_CONFIG = apos.MODEL_CONFIG
-        
-        # Setting up "targets"
-        if ((not issubclass(type(targets), numpy.ndarray)) or
-            (not numpy.asarray(targets).flags.f_contiguous) or
-            (not (targets.dtype == numpy.dtype(ctypes.c_float)))):
-            import warnings
-            warnings.warn("The provided argument 'targets' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
-            targets = numpy.asarray(targets, dtype=ctypes.c_float, order='F')
-        targets_dim_1 = ctypes.c_int(targets.shape[0])
-        targets_dim_2 = ctypes.c_int(targets.shape[1])
-        
-        # Setting up "outputs"
-        if ((not issubclass(type(outputs), numpy.ndarray)) or
-            (not numpy.asarray(outputs).flags.f_contiguous) or
-            (not (outputs.dtype == numpy.dtype(ctypes.c_float)))):
-            import warnings
-            warnings.warn("The provided argument 'outputs' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
-            outputs = numpy.asarray(outputs, dtype=ctypes.c_float, order='F')
-        outputs_dim_1 = ctypes.c_int(outputs.shape[0])
-        outputs_dim_2 = ctypes.c_int(outputs.shape[1])
-    
-        # Call C-accessible Fortran wrapper.
-        clib.c_squared_error_gradient(ctypes.byref(targets_dim_1), ctypes.byref(targets_dim_2), ctypes.c_void_p(targets.ctypes.data), ctypes.byref(outputs_dim_1), ctypes.byref(outputs_dim_2), ctypes.c_void_p(outputs.ctypes.data))
-    
-        # Return final results, 'INTENT(OUT)' arguments only.
-        return outputs
-
-    
-    # ----------------------------------------------
-    # Wrapper for the Fortran subroutine TRUE_VALUE_GRADIENT
-    
-    def true_value_gradient(self, targets, outputs):
-        '''! Produce the true values as the gradient (which will show large
-!  magnitudes for parameters in the model that align with values).'''
-        MODEL_CONFIG = apos.MODEL_CONFIG
-        
-        # Setting up "targets"
-        if ((not issubclass(type(targets), numpy.ndarray)) or
-            (not numpy.asarray(targets).flags.f_contiguous) or
-            (not (targets.dtype == numpy.dtype(ctypes.c_float)))):
-            import warnings
-            warnings.warn("The provided argument 'targets' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
-            targets = numpy.asarray(targets, dtype=ctypes.c_float, order='F')
-        targets_dim_1 = ctypes.c_int(targets.shape[0])
-        targets_dim_2 = ctypes.c_int(targets.shape[1])
-        
-        # Setting up "outputs"
-        if ((not issubclass(type(outputs), numpy.ndarray)) or
-            (not numpy.asarray(outputs).flags.f_contiguous) or
-            (not (outputs.dtype == numpy.dtype(ctypes.c_float)))):
-            import warnings
-            warnings.warn("The provided argument 'outputs' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
-            outputs = numpy.asarray(outputs, dtype=ctypes.c_float, order='F')
-        outputs_dim_1 = ctypes.c_int(outputs.shape[0])
-        outputs_dim_2 = ctypes.c_int(outputs.shape[1])
-    
-        # Call C-accessible Fortran wrapper.
-        clib.c_true_value_gradient(ctypes.byref(targets_dim_1), ctypes.byref(targets_dim_2), ctypes.c_void_p(targets.ctypes.data), ctypes.byref(outputs_dim_1), ctypes.byref(outputs_dim_2), ctypes.c_void_p(outputs.ctypes.data))
-    
-        # Return final results, 'INTENT(OUT)' arguments only.
-        return outputs
-
-    
-    # ----------------------------------------------
     # Wrapper for the Fortran subroutine MINIMIZE_MSE
     
-    def minimize_mse(self, config, model, y, x, xi, ax, axi, sizes, steps, record=None):
+    def minimize_mse(self, config, model, rwork, iwork, ax, axi, sizes, x, xi, y, steps, record=None):
         '''! Fit input / output pairs by minimizing mean squared error.'''
         MODEL_CONFIG = apos.MODEL_CONFIG
         
         # Setting up "config"
         if (type(config) is not MODEL_CONFIG): config = MODEL_CONFIG(config)
         
         # Setting up "model"
@@ -1039,43 +1477,31 @@
             (not numpy.asarray(model).flags.f_contiguous) or
             (not (model.dtype == numpy.dtype(ctypes.c_float)))):
             import warnings
             warnings.warn("The provided argument 'model' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
             model = numpy.asarray(model, dtype=ctypes.c_float, order='F')
         model_dim_1 = ctypes.c_int(model.shape[0])
         
-        # Setting up "y"
-        if ((not issubclass(type(y), numpy.ndarray)) or
-            (not numpy.asarray(y).flags.f_contiguous) or
-            (not (y.dtype == numpy.dtype(ctypes.c_float)))):
-            import warnings
-            warnings.warn("The provided argument 'y' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
-            y = numpy.asarray(y, dtype=ctypes.c_float, order='F')
-        y_dim_1 = ctypes.c_int(y.shape[0])
-        y_dim_2 = ctypes.c_int(y.shape[1])
-        
-        # Setting up "x"
-        if ((not issubclass(type(x), numpy.ndarray)) or
-            (not numpy.asarray(x).flags.f_contiguous) or
-            (not (x.dtype == numpy.dtype(ctypes.c_float)))):
-            import warnings
-            warnings.warn("The provided argument 'x' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
-            x = numpy.asarray(x, dtype=ctypes.c_float, order='F')
-        x_dim_1 = ctypes.c_int(x.shape[0])
-        x_dim_2 = ctypes.c_int(x.shape[1])
-        
-        # Setting up "xi"
-        if ((not issubclass(type(xi), numpy.ndarray)) or
-            (not numpy.asarray(xi).flags.f_contiguous) or
-            (not (xi.dtype == numpy.dtype(ctypes.c_int)))):
-            import warnings
-            warnings.warn("The provided argument 'xi' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
-            xi = numpy.asarray(xi, dtype=ctypes.c_int, order='F')
-        xi_dim_1 = ctypes.c_int(xi.shape[0])
-        xi_dim_2 = ctypes.c_int(xi.shape[1])
+        # Setting up "rwork"
+        if ((not issubclass(type(rwork), numpy.ndarray)) or
+            (not numpy.asarray(rwork).flags.f_contiguous) or
+            (not (rwork.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 'rwork' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            rwork = numpy.asarray(rwork, dtype=ctypes.c_float, order='F')
+        rwork_dim_1 = ctypes.c_int(rwork.shape[0])
+        
+        # Setting up "iwork"
+        if ((not issubclass(type(iwork), numpy.ndarray)) or
+            (not numpy.asarray(iwork).flags.f_contiguous) or
+            (not (iwork.dtype == numpy.dtype(ctypes.c_int)))):
+            import warnings
+            warnings.warn("The provided argument 'iwork' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
+            iwork = numpy.asarray(iwork, dtype=ctypes.c_int, order='F')
+        iwork_dim_1 = ctypes.c_int(iwork.shape[0])
         
         # Setting up "ax"
         if ((not issubclass(type(ax), numpy.ndarray)) or
             (not numpy.asarray(ax).flags.f_contiguous) or
             (not (ax.dtype == numpy.dtype(ctypes.c_float)))):
             import warnings
             warnings.warn("The provided argument 'ax' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
@@ -1098,44 +1524,74 @@
             (not numpy.asarray(sizes).flags.f_contiguous) or
             (not (sizes.dtype == numpy.dtype(ctypes.c_int)))):
             import warnings
             warnings.warn("The provided argument 'sizes' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
             sizes = numpy.asarray(sizes, dtype=ctypes.c_int, order='F')
         sizes_dim_1 = ctypes.c_int(sizes.shape[0])
         
+        # Setting up "x"
+        if ((not issubclass(type(x), numpy.ndarray)) or
+            (not numpy.asarray(x).flags.f_contiguous) or
+            (not (x.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 'x' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            x = numpy.asarray(x, dtype=ctypes.c_float, order='F')
+        x_dim_1 = ctypes.c_int(x.shape[0])
+        x_dim_2 = ctypes.c_int(x.shape[1])
+        
+        # Setting up "xi"
+        if ((not issubclass(type(xi), numpy.ndarray)) or
+            (not numpy.asarray(xi).flags.f_contiguous) or
+            (not (xi.dtype == numpy.dtype(ctypes.c_int)))):
+            import warnings
+            warnings.warn("The provided argument 'xi' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
+            xi = numpy.asarray(xi, dtype=ctypes.c_int, order='F')
+        xi_dim_1 = ctypes.c_int(xi.shape[0])
+        xi_dim_2 = ctypes.c_int(xi.shape[1])
+        
+        # Setting up "y"
+        if ((not issubclass(type(y), numpy.ndarray)) or
+            (not numpy.asarray(y).flags.f_contiguous) or
+            (not (y.dtype == numpy.dtype(ctypes.c_float)))):
+            import warnings
+            warnings.warn("The provided argument 'y' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
+            y = numpy.asarray(y, dtype=ctypes.c_float, order='F')
+        y_dim_1 = ctypes.c_int(y.shape[0])
+        y_dim_2 = ctypes.c_int(y.shape[1])
+        
         # Setting up "steps"
         if (type(steps) is not ctypes.c_int): steps = ctypes.c_int(steps)
         
-        # Setting up "sum_squared_error"
-        sum_squared_error = ctypes.c_float()
-        
         # Setting up "record"
         record_present = ctypes.c_bool(True)
         if (record is None):
             record_present = ctypes.c_bool(False)
             record = numpy.zeros(shape=(1,1), dtype=ctypes.c_float, order='F')
         elif (type(record) == bool) and (record):
-            record = numpy.zeros(shape=(4, steps), dtype=ctypes.c_float, order='F')
+            record = numpy.zeros(shape=(6, steps), dtype=ctypes.c_float, order='F')
         elif ((not issubclass(type(record), numpy.ndarray)) or
               (not numpy.asarray(record).flags.f_contiguous) or
               (not (record.dtype == numpy.dtype(ctypes.c_float)))):
             import warnings
             warnings.warn("The provided argument 'record' was not an f_contiguous NumPy array of type 'ctypes.c_float' (or equivalent). Automatically converting (probably creating a full copy).")
             record = numpy.asarray(record, dtype=ctypes.c_float, order='F')
         if (record_present):
             record_dim_1 = ctypes.c_int(record.shape[0])
             record_dim_2 = ctypes.c_int(record.shape[1])
         else:
             record_dim_1 = ctypes.c_int()
             record_dim_2 = ctypes.c_int()
         
+        # Setting up "sum_squared_error"
+        sum_squared_error = ctypes.c_float()
+        
         # Setting up "info"
         info = ctypes.c_int()
     
         # Call C-accessible Fortran wrapper.
-        clib.c_minimize_mse(ctypes.byref(config), ctypes.byref(model_dim_1), ctypes.c_void_p(model.ctypes.data), ctypes.byref(y_dim_1), ctypes.byref(y_dim_2), ctypes.c_void_p(y.ctypes.data), ctypes.byref(x_dim_1), ctypes.byref(x_dim_2), ctypes.c_void_p(x.ctypes.data), ctypes.byref(xi_dim_1), ctypes.byref(xi_dim_2), ctypes.c_void_p(xi.ctypes.data), ctypes.byref(ax_dim_1), ctypes.byref(ax_dim_2), ctypes.c_void_p(ax.ctypes.data), ctypes.byref(axi_dim_1), ctypes.byref(axi_dim_2), ctypes.c_void_p(axi.ctypes.data), ctypes.byref(sizes_dim_1), ctypes.c_void_p(sizes.ctypes.data), ctypes.byref(steps), ctypes.byref(sum_squared_error), ctypes.byref(record_present), ctypes.byref(record_dim_1), ctypes.byref(record_dim_2), ctypes.c_void_p(record.ctypes.data), ctypes.byref(info))
+        clib.c_minimize_mse(ctypes.byref(config), ctypes.byref(model_dim_1), ctypes.c_void_p(model.ctypes.data), ctypes.byref(rwork_dim_1), ctypes.c_void_p(rwork.ctypes.data), ctypes.byref(iwork_dim_1), ctypes.c_void_p(iwork.ctypes.data), ctypes.byref(ax_dim_1), ctypes.byref(ax_dim_2), ctypes.c_void_p(ax.ctypes.data), ctypes.byref(axi_dim_1), ctypes.byref(axi_dim_2), ctypes.c_void_p(axi.ctypes.data), ctypes.byref(sizes_dim_1), ctypes.c_void_p(sizes.ctypes.data), ctypes.byref(x_dim_1), ctypes.byref(x_dim_2), ctypes.c_void_p(x.ctypes.data), ctypes.byref(xi_dim_1), ctypes.byref(xi_dim_2), ctypes.c_void_p(xi.ctypes.data), ctypes.byref(y_dim_1), ctypes.byref(y_dim_2), ctypes.c_void_p(y.ctypes.data), ctypes.byref(steps), ctypes.byref(record_present), ctypes.byref(record_dim_1), ctypes.byref(record_dim_2), ctypes.c_void_p(record.ctypes.data), ctypes.byref(sum_squared_error), ctypes.byref(info))
     
         # Return final results, 'INTENT(OUT)' arguments only.
-        return model, y, x, ax, sum_squared_error.value, (record if record_present else None), info.value
+        return config, model, rwork, iwork, ax, x, y, (record if record_present else None), sum_squared_error.value, info.value
 
 apos = apos()
```

### Comparing `tlux-0.0.8/tlux/approximate/apos/apos.f90` & `tlux-0.0.9/tlux/approximate/apos/apos.f90`

 * *Files 26% similar despite different names*

```diff
@@ -1,38 +1,33 @@
 ! TODO:
 ! 
-! - Unify memory allocation so that threads don't have to allocate their
-!   own temporary space.
+! - Thoroughly test NORMALIZE (make sure data is correctly normalized in all use cases).
+!   Particularly, check that the initialization of the apositional output scale is working.
 ! 
-! - Enable a model that has no internal states (for linear regression).
+! - Reset convention to be order of processing (AX, AXI, AY, SIZES, X, XI, Y)
+! - Enable a model that has no internal states for linear regression (*NS=0).
+! - Enable a apositional without a following model (MDO=0) (no apositional shifting).
+!
+! - Update Python testing code to test all combinations of AX, AXI, AY, X, XI, and Y.
+! - Update Python testing code to attempt different edge-case model sizes
+!    (linear regression, no apositional, no model).
 ! 
-! - Enable a apositional without a following model.
+! - Make data normalization use the same work space as the fit procedure
+!   (since these are not needed at the same time).
+! - Pull normalization code out and have it be called separately from 'FIT'.
+!   (decide how to handle encoding the normalization into the model, function?)
+!   Goal is to achieve near-zero losses for doing a few steps at a time in
+!   Python (allowing for easier cancellation, progress updates, ...).
 ! 
-! - Center and fit inputs and outputs to spherical points (unit length).
+! - Use LAPACK to do linear regression, implement simple SVD + gradient descent method
+!   in MATRIX_OPERATIONS, compare speed of both methodologies.
+! - Implement and test Fortran intrinsic version of matrix multiplication.
+! - Implement and test Fortran intrinsic version of SSYRK (manually do loop).
 ! 
-! - Change initialization of shift terms to be based on the assumption
-!   that input data has spherical shape. Internal shift terms use
-!   previous shift and weight matrices to estimate value ranges for
-!   each basis function, with largest functions getting most negative
-!   shift and smallest functions getting most positive shift.
-! 
-! - Create 'condition_model' subroutine that takes values and gradients
-!   at all internal states, uses linear transformations to identify and
-!   remove redundant basis functions and initialize new basis functions
-!   that align most with the error function.
-! 
-! - Get stats on the internal values within the network during training.
-!   - step size progression
-!   - shift values
-!   - vector magnitudes for each node
-!   - output weights magnitude for each node
-!   - internal node contributions to MSE
-!   - data distributions at internal nodes (% less and greater than 0)
-! 
-
+! ---------------------------------------------------------------------------
 
 ! Module for matrix multiplication (absolutely crucial for APOS speed).
 MODULE MATRIX_OPERATIONS
   USE ISO_FORTRAN_ENV, ONLY: RT => REAL32
   IMPLICIT NONE
 
 CONTAINS
@@ -67,32 +62,29 @@
     !    ELSE
     !       C(:,:) = C(:,:) + AB_MULT * MATMUL(TRANSPOSE(A(:,:)), TRANSPOSE(B(:,:)))
     !    END IF
     ! END IF
   END SUBROUTINE GEMM
 
   ! Orthogonalize and normalize column vectors of A in order.
-  SUBROUTINE ORTHONORMALIZE(A, RANK)
+  SUBROUTINE ORTHONORMALIZE(A)
     REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: A
-    INTEGER, INTENT(OUT), OPTIONAL :: RANK
     REAL(KIND=RT), DIMENSION(SIZE(A,2)) :: MULTIPLIERS
     REAL(KIND=RT) :: LEN
     INTEGER :: I, J
-    IF (PRESENT(RANK)) RANK = 0
     DO I = 1, SIZE(A,2)
        LEN = NORM2(A(:,I))
        IF (LEN .GT. 0.0_RT) THEN
           A(:,I) = A(:,I) / LEN
-          IF (PRESENT(RANK)) RANK = RANK + 1
-       END IF
-       IF ((LEN .GT. 0.0_RT) .AND. (I .LT. SIZE(A,2))) THEN
-          MULTIPLIERS(I+1:) = MATMUL(A(:,I), A(:,I+1:))
-          DO J = I+1, SIZE(A,2)
-             A(:,J) = A(:,J) - MULTIPLIERS(J) * A(:,I)
-          END DO
+          IF (I .LT. SIZE(A,2)) THEN
+             MULTIPLIERS(I+1:) = MATMUL(A(:,I), A(:,I+1:))
+             DO J = I+1, SIZE(A,2)
+                A(:,J) = A(:,J) - MULTIPLIERS(J) * A(:,I)
+             END DO
+          END IF
        END IF
     END DO
   END SUBROUTINE ORTHONORMALIZE
 
   ! Generate randomly distributed vectors on the N-sphere.
   SUBROUTINE RANDOM_UNIT_VECTORS(COLUMN_VECTORS)
     REAL(KIND=RT), INTENT(OUT), DIMENSION(:,:) :: COLUMN_VECTORS
@@ -115,186 +107,674 @@
     END IF
     ! Orthonormalize the first components of the column
     !  vectors to ensure those are well spaced.
     I = MIN(SIZE(COLUMN_VECTORS,1), SIZE(COLUMN_VECTORS,2))
     IF (I .GT. 1) CALL ORTHONORMALIZE(COLUMN_VECTORS(:,1:I))
   END SUBROUTINE RANDOM_UNIT_VECTORS
 
+  ! Orthogonalize and normalize column vectors of A with pivoting.
+  SUBROUTINE ORTHOGONALIZE(A, LENGTHS, RANK, ORDER)
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: A
+    REAL(KIND=RT), INTENT(OUT), DIMENSION(SIZE(A,2)) :: LENGTHS
+    INTEGER, INTENT(OUT), OPTIONAL :: RANK
+    INTEGER, INTENT(OUT), DIMENSION(SIZE(A,2)), OPTIONAL :: ORDER
+    REAL(KIND=RT) :: L, VEC(SIZE(A,1)) 
+    INTEGER :: I, J, K
+    IF (PRESENT(RANK)) RANK = 0
+    IF (PRESENT(ORDER)) THEN
+       FORALL (I=1:SIZE(A,2)) ORDER(I) = I
+    END IF
+    column_orthogonolization : DO I = 1, SIZE(A,2)
+       LENGTHS(I:) = SUM(A(:,I:)**2, 1)
+       ! Pivot the largest magnitude vector to the front.
+       J = I-1+MAXLOC(LENGTHS(I:),1)
+       IF (J .NE. I) THEN
+          IF (PRESENT(ORDER)) THEN
+             K = ORDER(I)
+             ORDER(I) = ORDER(J)
+             ORDER(J) = K
+          END IF
+          L = LENGTHS(I)
+          LENGTHS(I) = LENGTHS(J)
+          LENGTHS(J) = L
+          VEC(:) = A(:,I)
+          A(:,I) = A(:,J)
+          A(:,J) = VEC(:)
+       END IF
+       ! Subtract the first vector from all others.
+       IF (LENGTHS(I) .GT. EPSILON(1.0_RT)) THEN
+          LENGTHS(I) = SQRT(LENGTHS(I))
+          A(:,I) = A(:,I) / LENGTHS(I)
+          IF (I .LT. SIZE(A,2)) THEN
+             LENGTHS(I+1:) = MATMUL(A(:,I), A(:,I+1:))
+             DO J = I+1, SIZE(A,2)
+                A(:,J) = A(:,J) - LENGTHS(J) * A(:,I)
+             END DO
+          END IF
+          IF (PRESENT(RANK)) RANK = RANK + 1
+       ELSE
+          LENGTHS(I:) = 0.0_RT
+          EXIT column_orthogonolization
+       END IF
+    END DO column_orthogonolization
+  END SUBROUTINE ORTHOGONALIZE
+
+  ! Compute the singular values and right singular vectors for matrix A.
+  SUBROUTINE SVD(A, S, VT, RANK, STEPS, BIAS)
+    IMPLICIT NONE
+    REAL(KIND=RT), INTENT(IN), DIMENSION(:,:) :: A
+    REAL(KIND=RT), INTENT(OUT), DIMENSION(MIN(SIZE(A,1),SIZE(A,2))) :: S
+    REAL(KIND=RT), INTENT(OUT), DIMENSION(MIN(SIZE(A,1),SIZE(A,2)),MIN(SIZE(A,1),SIZE(A,2))) :: VT
+    INTEGER, INTENT(OUT), OPTIONAL :: RANK
+    INTEGER, INTENT(IN), OPTIONAL :: STEPS
+    REAL(KIND=RT), INTENT(IN), OPTIONAL :: BIAS
+    ! Local variables.
+    REAL(KIND=RT), DIMENSION(MIN(SIZE(A,1),SIZE(A,2)),MIN(SIZE(A,1),SIZE(A,2))) :: ATA, Q
+    INTEGER :: I, J, K, NUM_STEPS
+    REAL(KIND=RT) :: MULTIPLIER
+    EXTERNAL :: SSYRK
+    ! Set the number of steps.
+    IF (PRESENT(STEPS)) THEN
+       NUM_STEPS = STEPS
+    ELSE
+       NUM_STEPS = 1
+    END IF
+    ! Set "K" (the number of components).
+    K = MIN(SIZE(A,1),SIZE(A,2))
+    ! Find the multiplier on A.
+    MULTIPLIER = MAXVAL(ABS(A(:,:)))
+    IF (MULTIPLIER .EQ. 0.0_RT) THEN
+       S(:) = 0.0_RT
+       VT(:,:) = 0.0_RT
+       RETURN
+    END IF
+    IF (PRESENT(BIAS)) MULTIPLIER = MULTIPLIER / BIAS
+    MULTIPLIER = 1.0_RT / MULTIPLIER
+    ! Compute ATA.
+    IF (SIZE(A,1) .LE. SIZE(A,2)) THEN
+       ! ATA(:,:) = MATMUL(AT(:,:), TRANSPOSE(AT(:,:)))
+       CALL SSYRK('U', 'N', K, SIZE(A,2), MULTIPLIER**2, A(:,:), &
+            SIZE(A,1), 0.0_RT, ATA(:,:), K)
+    ELSE
+       ! ATA(:,:) = MATMUL(TRANSPOSE(A(:,:)), A(:,:))
+       CALL SSYRK('U', 'T', K, SIZE(A,1), MULTIPLIER**2, A(:,:), &
+            SIZE(A,1), 0.0_RT, ATA(:,:), K)
+    END IF
+    ! Copy the upper diagnoal portion into the lower diagonal portion.
+    DO I = 1, K
+       ATA(I+1:,I) = ATA(I,I+1:)
+    END DO
+    ! Compute initial right singular vectors.
+    VT(:,:) = ATA(:,:)
+    ! Orthogonalize and reorder by magnitudes.
+    CALL ORTHOGONALIZE(VT(:,:), S(:), RANK)
+    ! Do power iterations.
+    power_iteration : DO I = 1, NUM_STEPS
+       Q(:,:) = VT(:,:)
+       ! Q(:,:) = MATMUL(TRANSPOSE(ATA(:,:)), QTEMP(:,:))
+       CALL GEMM('N', 'N', K, K, K, 1.0_RT, &
+            ATA(:,:), K, Q(:,:), K, 0.0_RT, &
+            VT(:,:), K)
+       CALL ORTHOGONALIZE(VT(:,:), S(:), RANK)
+    END DO power_iteration
+    ! Compute the singular values.
+    WHERE (S(:) .NE. 0.0_RT)
+       S(:) = SQRT(S(:)) / MULTIPLIER
+    END WHERE
+  END SUBROUTINE SVD
+
+  ! If there are at least as many data points as dimension, then
+  ! compute the principal components and rescale the data by
+  ! projecting onto those and rescaling so that each component has
+  ! identical singular values (this makes the data more "radially
+  ! symmetric").
+  SUBROUTINE RADIALIZE(X, SHIFT, VECS, INVERT_RESULT, STEPS)
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: X
+    REAL(KIND=RT), INTENT(OUT), DIMENSION(:) :: SHIFT
+    REAL(KIND=RT), INTENT(OUT), DIMENSION(:,:) :: VECS
+    LOGICAL, INTENT(IN), OPTIONAL :: INVERT_RESULT
+    INTEGER, INTENT(IN), OPTIONAL :: STEPS
+    ! Local variables.
+    LOGICAL :: INVERSE
+    REAL(KIND=RT), DIMENSION(SIZE(VECS,1),SIZE(VECS,2)) :: TEMP_VECS
+    REAL(KIND=RT), DIMENSION(SIZE(X,1)) :: VALS
+    REAL(KIND=RT), DIMENSION(SIZE(X,1), SIZE(X,2)) :: X1
+    REAL(KIND=RT) :: RN
+    INTEGER :: I, D
+    ! Set the default value for "INVERSE".
+    IF (PRESENT(INVERT_RESULT)) THEN
+       INVERSE = INVERT_RESULT
+    ELSE
+       INVERSE = .FALSE.
+    END IF
+    ! Shift the data to be be centered about the origin.
+    D = SIZE(X,1)
+    RN = REAL(SIZE(X,2),RT)
+    SHIFT(:) = -SUM(X(:,:),2) / RN
+    DO I = 1, D
+       X(I,:) = X(I,:) + SHIFT(I)
+    END DO
+    ! Set the unused portion of the "VECS" matrix to the identity.
+    VECS(D+1:,D+1:) = 0.0_RT
+    DO I = D+1, SIZE(VECS,1)
+       VECS(I,I) = 1.0_RT
+    END DO
+    ! Find the directions along which the data is most elongated.
+    IF (PRESENT(STEPS)) THEN
+       CALL SVD(X, VALS, VECS(:D,:D), STEPS=STEPS)
+    ELSE
+       CALL SVD(X, VALS, VECS(:D,:D), STEPS=10)
+    END IF
+    ! Normalize the values to make the output componentwise unit mean squared magnitude.
+    VALS(:) = VALS(:) / SQRT(RN)
+    ! For all nonzero vectors, rescale them so that 
+    !  the average distance from zero is exactly 1.
+    DO I = 1, D
+       IF (VALS(I) .GT. 0.0_RT) THEN
+          VECS(:,I) = VECS(:,I) / VALS(I)
+       END IF
+    END DO
+    ! Apply the column vectors to the data to make it radially symmetric.
+    X1(:,:) = X(:,:)
+    CALL GEMM('T', 'N', D, SIZE(X,2), D, 1.0_RT, &
+         VECS(:D,:D), D, &
+         X1(:,:), D, &
+         0.0_RT, X(:,:), D)
+    ! Compute the inverse of the transformation if requested.
+    IF (INVERSE) THEN
+       VALS(:) = VALS(:)**2
+       DO I = 1, D
+          IF (VALS(I) .GT. 0.0_RT) THEN
+             VECS(:D,I) = VECS(:D,I) * VALS(I)
+          END IF
+       END DO
+       VECS(:D,:D) = TRANSPOSE(VECS(:D,:D))
+       SHIFT(:) = -SHIFT(:)
+    END IF
+  END SUBROUTINE RADIALIZE
+
 END MODULE MATRIX_OPERATIONS
 
+! ---------------------------------------------------------------------------
+
+! A module for fast sorting and selecting of data.
+MODULE SORT_AND_SELECT
+  USE ISO_FORTRAN_ENV, ONLY: RT => REAL32
+  IMPLICIT NONE
+
+CONTAINS
+
+  ! Swap the values of two integers.
+  SUBROUTINE SWAP_INT(V1, V2)
+    INTEGER, INTENT(INOUT) :: V1, V2
+    INTEGER :: TEMP
+    TEMP = V1
+    V1 = V2
+    V2 = TEMP
+  END SUBROUTINE SWAP_INT
+
+  !                       FastSelect method
+  ! 
+  ! Given VALUES list of numbers, rearrange the elements of INDICES
+  ! such that the element of VALUES at INDICES(K) has rank K (holds
+  ! its same location as if all of VALUES were sorted in INDICES).
+  ! All elements of VALUES at INDICES(:K-1) are less than or equal,
+  ! while all elements of VALUES at INDICES(K+1:) are greater or equal.
+  ! 
+  ! This algorithm uses a recursive approach to exponentially shrink
+  ! the number of indices that have to be considered to find the
+  ! element of desired rank, while simultaneously pivoting values
+  ! that are less than the target rank left and larger right.
+  ! 
+  ! Arguments:
+  ! 
+  !   VALUES   --  A 1D array of real numbers. Will not be modified.
+  !   K        --  A positive integer for the rank index about which
+  !                VALUES should be rearranged.
+  ! Optional:
+  ! 
+  !   DIVISOR  --  A positive integer >= 2 that represents the
+  !                division factor used for large VALUES arrays.
+  !   MAX_SIZE --  An integer >= DIVISOR that represents the largest
+  !                sized VALUES for which the worst-case pivot value
+  !                selection is tolerable. A worst-case pivot causes
+  !                O( SIZE(VALUES)^2 ) runtime. This value should be
+  !                determined heuristically based on compute hardware.
+  ! Output:
+  ! 
+  !   INDICES  --  A 1D array of original indices for elements of VALUES.
+  ! 
+  !   The elements of the array INDICES are rearranged such that the
+  !   element at position VALUES(INDICES(K)) is in the same location 
+  !   it would be if all of VALUES were referenced in sorted order in
+  !   INDICES. Also known as, VALUES(INDICES(K)) has rank K.
+  ! 
+  RECURSIVE SUBROUTINE ARGSELECT(VALUES, K, INDICES, DIVISOR, MAX_SIZE, RECURSING)
+    ! Arguments
+    REAL(KIND=RT), INTENT(IN), DIMENSION(:) :: VALUES
+    INTEGER, INTENT(IN) :: K
+    INTEGER, INTENT(INOUT), DIMENSION(:) :: INDICES
+    INTEGER, INTENT(IN), OPTIONAL :: DIVISOR, MAX_SIZE
+    LOGICAL, INTENT(IN), OPTIONAL :: RECURSING
+    ! Locals
+    INTEGER :: LEFT, RIGHT, L, R, MS, D, I
+    REAL(KIND=RT) :: P
+    ! Initialize the divisor (for making subsets).
+    IF (PRESENT(DIVISOR)) THEN ; D = DIVISOR
+    ELSE IF (SIZE(INDICES) .GE. 8388608) THEN ; D = 32 ! 2**5 ! 2**23
+    ELSE IF (SIZE(INDICES) .GE. 1048576) THEN ; D = 8  ! 2**3 ! 2**20
+    ELSE                                      ; D = 4  ! 2**2
+    END IF
+    ! Initialize the max size (before subsets are created).
+    IF (PRESENT(MAX_SIZE)) THEN ; MS = MAX_SIZE
+    ELSE                        ; MS = 1024 ! 2**10
+    END IF
+    ! When not recursing, set the INDICES to default values.
+    IF (.NOT. PRESENT(RECURSING)) THEN
+       FORALL(I=1:SIZE(INDICES)) INDICES(I) = I
+    END IF
+    ! Initialize LEFT and RIGHT to be the entire array.
+    LEFT = 1
+    RIGHT = SIZE(INDICES)
+    ! Loop until done finding the K-th element.
+    DO WHILE (LEFT .LT. RIGHT)
+       ! Use SELECT recursively to improve the quality of the
+       ! selected pivot value for large arrays.
+       IF (RIGHT - LEFT .GT. MS) THEN
+          ! Compute how many elements should be left and right of K
+          ! to maintain the same percentile in a subset.
+          L = K - K / D
+          R = L + (SIZE(INDICES) / D)
+          ! Perform fast select on an array a fraction of the size about K.
+          CALL ARGSELECT(VALUES(:), K - L + 1, INDICES(L:R), &
+               DIVISOR=D, MAX_SIZE=MS, RECURSING=.TRUE.)
+       END IF
+       ! Pick a partition element at position K.
+       P = VALUES(INDICES(K))
+       L = LEFT
+       R = RIGHT
+       ! Move the partition element to the front of the list.
+       CALL SWAP_INT(INDICES(LEFT), INDICES(K))
+       ! Pre-swap the left and right elements (temporarily putting a
+       ! larger element on the left) before starting the partition loop.
+       IF (VALUES(INDICES(RIGHT)) .GT. P) THEN
+          CALL SWAP_INT(INDICES(LEFT), INDICES(RIGHT))
+       END IF
+       ! Now partition the elements about the pivot value "P".
+       DO WHILE (L .LT. R)
+          CALL SWAP_INT(INDICES(L), INDICES(R))
+          L = L + 1
+          R = R - 1
+          DO WHILE (VALUES(INDICES(L)) .LT. P) ; L = L + 1 ; END DO
+          DO WHILE (VALUES(INDICES(R)) .GT. P) ; R = R - 1 ; END DO
+       END DO
+       ! Place the pivot element back into its appropriate place.
+       IF (VALUES(INDICES(LEFT)) .EQ. P) THEN
+          CALL SWAP_INT(INDICES(LEFT), INDICES(R))
+       ELSE
+          R = R + 1
+          CALL SWAP_INT(INDICES(R), INDICES(RIGHT))
+       END IF
+       ! adjust left and right towards the boundaries of the subset
+       ! containing the (k - left + 1)th smallest element
+       IF (R .LE. K) LEFT = R + 1
+       IF (K .LE. R) RIGHT = R - 1
+    END DO
+  END SUBROUTINE ARGSELECT
+  
+  !                         FastSort
+  ! 
+  ! This routine uses a combination of QuickSort (with modestly
+  ! intelligent pivot selection) and Insertion Sort (for small arrays)
+  ! to achieve very fast average case sort times for both random and
+  ! partially sorted data. The pivot is selected for QuickSort as the
+  ! median of the first, middle, and last values in the array.
+  ! 
+  ! Arguments:
+  ! 
+  !   VALUES   --  A 1D array of real numbers.
+  !   INDICES  --  A 1D array of original indices for elements of VALUES.
+  ! 
+  ! Optional:
+  ! 
+  !   MIN_SIZE --  An positive integer that represents the largest
+  !                sized VALUES for which a partition about a pivot
+  !                is used to reduce the size of a an unsorted array.
+  !                Any size less than this will result in the use of
+  !                INSERTION_ARGSORT instead of ARGPARTITION.
+  ! 
+  ! Output:
+  ! 
+  !   The elements of the array INDICES contain ths sorted order of VALUES.
+  ! 
+  RECURSIVE SUBROUTINE ARGSORT(VALUES, INDICES, MIN_SIZE, INIT_INDS)
+    REAL(KIND=RT), INTENT(IN),    DIMENSION(:) :: VALUES
+    INTEGER,       INTENT(INOUT), DIMENSION(:) :: INDICES
+    INTEGER,       INTENT(IN), OPTIONAL        :: MIN_SIZE
+    LOGICAL,       INTENT(IN), OPTIONAL        :: INIT_INDS
+    ! Local variables
+    LOGICAL :: INIT
+    INTEGER :: I, MS
+    IF (PRESENT(MIN_SIZE)) THEN ; MS = MIN_SIZE
+    ELSE                        ; MS = 2**6
+    END IF
+    IF (PRESENT(INIT_INDS)) THEN ; INIT = INIT_INDS
+    ELSE                         ; INIT = .TRUE.
+    END IF
+    ! Initialize all indices (for the first call).
+    IF (INIT) THEN
+       FORALL (I=1:SIZE(INDICES)) INDICES(I) = I
+    END IF
+    ! Base case, return.
+    IF (SIZE(INDICES) .LT. MS) THEN
+       CALL INSERTION_ARGSORT(VALUES, INDICES)
+    ! Call this function recursively after pivoting about the median.
+    ELSE
+       ! ---------------------------------------------------------------
+       ! If you are having slow runtime with the selection of pivot values 
+       ! provided by ARGPARTITION, then consider using ARGSELECT instead.
+       I = ARGPARTITION(VALUES, INDICES)
+       ! ---------------------------------------------------------------
+       ! I = SIZE(INDICES) / 2
+       ! CALL ARGSELECT(VALUES, INDICES, I)
+       ! ---------------------------------------------------------------
+       CALL ARGSORT(VALUES(:), INDICES(:I-1), MS, INIT_INDS=.FALSE.)
+       CALL ARGSORT(VALUES(:), INDICES(I+1:), MS, INIT_INDS=.FALSE.)
+    END IF
+  END SUBROUTINE ARGSORT
+
+  ! This function efficiently partitions values based on the median
+  ! of the first, middle, and last elements of the VALUES array. This
+  ! function returns the index of the pivot.
+  FUNCTION ARGPARTITION(VALUES, INDICES) RESULT(LEFT)
+    REAL(KIND=RT), INTENT(IN),    DIMENSION(:) :: VALUES
+    INTEGER,       INTENT(INOUT), DIMENSION(:) :: INDICES
+    INTEGER :: LEFT, MID, RIGHT
+    REAL(KIND=RT) :: PIVOT
+    ! Use the median of the first, middle, and last element as the
+    ! pivot. Place the pivot at the end of the array.
+    MID = (1 + SIZE(INDICES)) / 2
+    ! Swap the first and last elements (if the last is smaller).
+    IF (VALUES(INDICES(SIZE(INDICES))) < VALUES(INDICES(1))) THEN
+       CALL SWAP_INT(INDICES(1), INDICES(SIZE(INDICES)))
+    END IF
+    ! Swap the middle and first elements (if the middle is smaller).
+    IF (VALUES(INDICES(MID)) < VALUES(INDICES(SIZE(INDICES)))) THEN
+       CALL SWAP_INT(INDICES(MID), INDICES(SIZE(INDICES)))       
+       ! Swap the last and first elements (if the last is smaller).
+       IF (VALUES(INDICES(SIZE(INDICES))) < VALUES(INDICES(1))) THEN
+          CALL SWAP_INT(INDICES(1), INDICES(SIZE(INDICES)))
+       END IF
+    END IF
+    ! Set the pivot, LEFT index and RIGHT index (skip the smallest,
+    ! which is in location 1, and the pivot at the end).
+    PIVOT = VALUES(INDICES(SIZE(INDICES)))
+    LEFT  = 2
+    RIGHT = SIZE(INDICES) - 1
+    ! Partition all elements to the left and right side of the pivot
+    ! (left if they are smaller, right if they are bigger).
+    DO WHILE (LEFT < RIGHT)
+       ! Loop left until we find a value that is greater or equal to pivot.
+       DO WHILE (VALUES(INDICES(LEFT)) < PIVOT)
+          LEFT = LEFT + 1
+       END DO
+       ! Loop right until we find a value that is less or equal to pivot (or LEFT).
+       DO WHILE (RIGHT .NE. LEFT)
+          IF (VALUES(INDICES(RIGHT)) .LT. PIVOT) EXIT
+          RIGHT = RIGHT - 1
+       END DO
+       ! Now we know that [VALUES(RIGHT) < PIVOT < VALUES(LEFT)], so swap them.
+       CALL SWAP_INT(INDICES(LEFT), INDICES(RIGHT))
+    END DO
+    ! The last swap was done even though LEFT == RIGHT, we need to undo.
+    CALL SWAP_INT(INDICES(LEFT), INDICES(RIGHT))
+    ! Finally, we put the pivot back into its proper location.
+    CALL SWAP_INT(INDICES(LEFT), INDICES(SIZE(INDICES)))
+  END FUNCTION ARGPARTITION
+
+  ! Insertion sort (best for small lists).
+  SUBROUTINE INSERTION_ARGSORT(VALUES, INDICES)
+    REAL(KIND=RT), INTENT(IN),    DIMENSION(:) :: VALUES
+    INTEGER,       INTENT(INOUT), DIMENSION(:) :: INDICES
+    ! Local variables.
+    REAL(KIND=RT)   :: TEMP_VAL
+    INTEGER :: I, BEFORE, AFTER, TEMP_IND
+    ! Return for the base case.
+    IF (SIZE(INDICES) .LE. 1) RETURN
+    ! Put the smallest value at the front of the list.
+    I = MINLOC(VALUES(INDICES(:)),1)
+    CALL SWAP_INT(INDICES(1), INDICES(I))
+    ! Insertion sort the rest of the array.
+    DO I = 3, SIZE(INDICES)
+       TEMP_IND = INDICES(I)
+       TEMP_VAL = VALUES(TEMP_IND)
+       ! Search backwards in the list, 
+       BEFORE = I - 1
+       AFTER  = I
+       DO WHILE (TEMP_VAL .LT. VALUES(INDICES(BEFORE)))
+          INDICES(AFTER) = INDICES(BEFORE)
+          BEFORE = BEFORE - 1
+          AFTER  = AFTER - 1
+       END DO
+       ! Put the value into its place (where it is greater than the
+       ! element before it, but less than all values after it).
+       INDICES(AFTER) = TEMP_IND
+    END DO
+  END SUBROUTINE INSERTION_ARGSORT
+
+END MODULE SORT_AND_SELECT
+
+
+! ---------------------------------------------------------------------------
+
 
 ! An apositional (/aggregate) and positional piecewise linear regression model.
 MODULE APOS
-  USE ISO_FORTRAN_ENV, ONLY: RT => REAL32
-  USE MATRIX_OPERATIONS, ONLY: GEMM, ORTHONORMALIZE, RANDOM_UNIT_VECTORS
+  USE ISO_FORTRAN_ENV, ONLY: RT => REAL32, INT64, INT8
+  USE MATRIX_OPERATIONS, ONLY: GEMM, RANDOM_UNIT_VECTORS, ORTHOGONALIZE, RADIALIZE
+  USE SORT_AND_SELECT, ONLY: ARGSORT, ARGSELECT
+
   IMPLICIT NONE
 
   PRIVATE :: MODEL_GRADIENT
 
   ! Model configuration, internal sizes and fit parameters.
   TYPE, BIND(C) :: MODEL_CONFIG
-     ! (Positional) model configuration.
-     INTEGER :: MDI      ! model dimension of input
-     INTEGER :: MDS = 32 ! model dimension of state
-     INTEGER :: MNS = 8  ! model number of states
-     INTEGER :: MDO      ! model dimension of output
-     INTEGER :: MNE = 0  ! model number of embeddings
-     INTEGER :: MDE = 0  ! model dimension of embeddings
      ! Apositional model configuration.
+     INTEGER :: ADN      ! apositional dimension numeric (input)
      INTEGER :: ADI      ! apositional dimension of input
      INTEGER :: ADS = 32 ! apositional dimension of state
      INTEGER :: ANS = 8  ! apositional number of states
      INTEGER :: ADO = 32 ! apositional dimension of output
      INTEGER :: ANE = 0  ! apositional number of embeddings
      INTEGER :: ADE = 0  ! apositional dimension of embeddings
+     ! (Positional) model configuration.
+     INTEGER :: MDN      ! model dimension numeric (input)
+     INTEGER :: MDI      ! model dimension of input
+     INTEGER :: MDS = 32 ! model dimension of state
+     INTEGER :: MNS = 8  ! model number of states
+     INTEGER :: MDO      ! model dimension of output
+     INTEGER :: MNE = 0  ! model number of embeddings
+     INTEGER :: MDE = 0  ! model dimension of embeddings
      ! Summary numbers that are computed.
      INTEGER :: TOTAL_SIZE
      INTEGER :: NUM_VARS
      ! Index subsets of total size vector naming scheme:
      !   M___ -> model,   A___ -> apositional (/ aggregate) model
      !   _S__ -> start,   _E__ -> end
      !   __I_ -> input,   __S_ -> states, __O_ -> output, __E_ -> embedding
      !   ___V -> vectors, ___S -> shifts
-     INTEGER :: MSIV, MEIV, MSIS, MEIS ! model input
-     INTEGER :: MSSV, MESV, MSSS, MESS ! model states
-     INTEGER :: MSOV, MEOV             ! model output
-     INTEGER :: MSEV, MEEV             ! model embedding
      INTEGER :: ASIV, AEIV, ASIS, AEIS ! apositional input
      INTEGER :: ASSV, AESV, ASSS, AESS ! apositional states
      INTEGER :: ASOV, AEOV             ! apositional output
      INTEGER :: ASEV, AEEV             ! apositional embedding
+     INTEGER :: MSIV, MEIV, MSIS, MEIS ! model input
+     INTEGER :: MSSV, MESV, MSSS, MESS ! model states
+     INTEGER :: MSOV, MEOV             ! model output
+     INTEGER :: MSEV, MEEV             ! model embedding
      ! Index subsets for input and output shifts.
      ! M___ -> model,       A___ -> apositional (/ aggregate) model
      ! _IS_ -> input shift, _OS_ -> output shift
      ! ___S -> start,       ___E -> end
+     INTEGER :: AISS, AISE, AOSS, AOSE
      INTEGER :: MISS, MISE, MOSS, MOSE
-     INTEGER :: AISS, AISE
      ! Function parameter.
      REAL(KIND=RT) :: DISCONTINUITY = 0.0_RT
      ! Initialization related parameters.
      REAL(KIND=RT) :: INITIAL_SHIFT_RANGE = 1.0_RT
      REAL(KIND=RT) :: INITIAL_OUTPUT_SCALE = 0.1_RT
-     REAL(KIND=RT) :: INITIAL_STEP = 0.001_RT
-     REAL(KIND=RT) :: INITIAL_STEP_MEAN_CHANGE = 0.1_RT
-     REAL(KIND=RT) :: INITIAL_STEP_CURV_CHANGE = 0.01_RT
      ! Optimization related parameters.
+     REAL(KIND=RT) :: STEP_FACTOR = 0.001_RT
+     REAL(KIND=RT) :: STEP_MEAN_CHANGE = 0.1_RT
+     REAL(KIND=RT) :: STEP_CURV_CHANGE = 0.01_RT
      REAL(KIND=RT) :: FASTER_RATE = 1.01_RT
      REAL(KIND=RT) :: SLOWER_RATE = 0.99_RT
-     INTEGER       :: MIN_STEPS_TO_STABILITY = 1
-     INTEGER       :: NUM_THREADS = 1
-     LOGICAL       :: KEEP_BEST = .TRUE.
-     LOGICAL       :: EARLY_STOP = .TRUE.
+     REAL(KIND=RT) :: MIN_UPDATE_RATIO = 0.05_RT
+     INTEGER :: MIN_STEPS_TO_STABILITY = 1
+     INTEGER :: NUM_THREADS = 1
+     INTEGER :: PRINT_DELAY_SEC = 3
+     INTEGER :: STEPS_TAKEN = 0
+     INTEGER :: LOGGING_STEP_FREQUENCY = 10
+     INTEGER :: NUM_TO_UPDATE = HUGE(0)
+     LOGICAL(KIND=INT8) :: AX_NORMALIZED = .FALSE.
+     LOGICAL(KIND=INT8) :: AXI_NORMALIZED = .FALSE.
+     LOGICAL(KIND=INT8) :: AY_NORMALIZED = .FALSE.
+     LOGICAL(KIND=INT8) :: X_NORMALIZED = .FALSE.
+     LOGICAL(KIND=INT8) :: XI_NORMALIZED = .FALSE.
+     LOGICAL(KIND=INT8) :: Y_NORMALIZED = .FALSE.
+     LOGICAL(KIND=INT8) :: ENCODE_NORMALIZATION = .TRUE.
+     LOGICAL(KIND=INT8) :: APPLY_SHIFT = .TRUE.
+     LOGICAL(KIND=INT8) :: KEEP_BEST = .TRUE.
+     LOGICAL(KIND=INT8) :: EARLY_STOP = .TRUE.
+     ! Descriptions of the number of points that can be in one batch.
+     INTEGER :: RWORK_SIZE = 0
+     INTEGER :: IWORK_SIZE = 0
+     INTEGER :: NA = 0
+     INTEGER :: NM = 0
+     ! Optimization work space start and end indices.
+     INTEGER :: SMG, EMG ! MODEL_GRAD(NUM_VARS)
+     INTEGER :: SMGM, EMGM ! MODEL_GRAD_MEAN(NUM_VARS)
+     INTEGER :: SMGC, EMGC ! MODEL_GRAD_CURV(NUM_VARS)
+     INTEGER :: SBM, EBM ! BEST_MODEL(NUM_VARS)
+
+     INTEGER :: SFMA, EFMA ! FULL_MODEL_ALIGN(NUM_VARS,NUM_THREADS)
+     
+     INTEGER :: SAXS, EAXS ! A_STATES(NA,ADS,ANS+1)
+     INTEGER :: SAXG, EAXG ! A_GRADS(NA,ADS,ANS+1)
+     INTEGER :: SAA, EAA ! A_ALIGN(ADS,ANS)
+     INTEGER :: SAY, EAY ! AY(NA,ADO)
+
+     INTEGER :: SXT, EXT ! X_TEMP(CONFIG%MDE+CONFIG%ADO,NM,NUM_THREADS)
+
+     INTEGER :: SAYG, EAYG ! AY_GRAD(NA,ADO)
+     INTEGER :: SMXS, EMXS ! M_STATES(NM,MDS,MNS+1)
+     INTEGER :: SMXG, EMXG ! M_GRADS(NM,MDS,MNS+1)
+     INTEGER :: SMA, EMA ! M_ALIGN(MDS,MNS)
+     INTEGER :: SYG, EYG ! Y_GRADIENT(MDO,NM)
+     INTEGER :: SAXR, EAXR ! AX_RESCALE(ADN,ADN)
+     INTEGER :: SAXIS, EAXIS ! AXI_SHIFT(ADE)
+     INTEGER :: SAXIR, EAXIR ! AXI_RESCALE(ADE,ADE)
+     INTEGER :: SAYR, EAYR ! AY_RESCALE(ADO)
+     INTEGER :: SMXR, EMXR ! X_RESCALE(MDN,MDN)
+     INTEGER :: SMXIS, EMXIS ! XI_SHIFT(MDE)
+     INTEGER :: SMXIR, EMXIR ! XI_RESCALE(MDE,MDE)
+     INTEGER :: SYR, EYR ! Y_RESCALE(MDO,MDO)
+     ! Integer workspace (for optimization).
+     INTEGER :: SUI, EUI ! UPDATE_INDICES(NUM_VARS)
+     INTEGER :: SBAS, EBAS ! BATCHA_STARTS(NUM_THREADS)
+     INTEGER :: SBAE, EBAE ! BATCHA_ENDS(NUM_THREADS)
+     INTEGER :: SBMS, EBMS ! BATCHM_STARTS(NUM_THREADS)
+     INTEGER :: SBME, EBME ! BATCHM_ENDS(NUM_THREADS)
   END TYPE MODEL_CONFIG
 
   ! Function that is defined by OpenMP.
   INTERFACE
      FUNCTION OMP_GET_MAX_THREADS()
        INTEGER :: OMP_GET_MAX_THREADS
      END FUNCTION OMP_GET_MAX_THREADS
   END INTERFACE
 
 CONTAINS
 
   ! Generate a model configuration given state parameters for the model.
-  SUBROUTINE NEW_MODEL_CONFIG(MDI, MDO, MDS, MNS, MNE, MDE, &
-       ADI, ADO, ADS, ANS, ANE, ADE, NUM_THREADS, CONFIG)
+  SUBROUTINE NEW_MODEL_CONFIG(ADN, ADO, ADS, ANS, ANE, ADE, &
+       MDN, MDO, MDS, MNS, MNE, MDE, NUM_THREADS, CONFIG)
      ! Size related parameters.
-     INTEGER, INTENT(IN) :: MDI, ADI
+     INTEGER, INTENT(IN) :: ADN, MDN
      INTEGER, INTENT(IN) :: MDO
      INTEGER, OPTIONAL, INTENT(IN) :: ADO
-     INTEGER, OPTIONAL, INTENT(IN) :: MDS, ADS
-     INTEGER, OPTIONAL, INTENT(IN) :: MNS, ANS
-     INTEGER, OPTIONAL, INTENT(IN) :: MNE, ANE
-     INTEGER, OPTIONAL, INTENT(IN) :: MDE, ADE
+     INTEGER, OPTIONAL, INTENT(IN) :: ADS, MDS
+     INTEGER, OPTIONAL, INTENT(IN) :: ANS, MNS
+     INTEGER, OPTIONAL, INTENT(IN) :: ANE, MNE
+     INTEGER, OPTIONAL, INTENT(IN) :: ADE, MDE
      INTEGER, OPTIONAL, INTENT(IN) :: NUM_THREADS
      ! Output
      TYPE(MODEL_CONFIG), INTENT(OUT) :: CONFIG
      ! ---------------------------------------------------------------
-     ! MDS
-     IF (PRESENT(MDS)) CONFIG%MDS = MDS
-     ! MNS
-     IF (PRESENT(MNS)) CONFIG%MNS = MNS
-     ! MNE
-     IF (PRESENT(MNE)) CONFIG%MNE = MNE
-     ! MDE
-     IF (PRESENT(MDE)) THEN
-        CONFIG%MDE = MDE
-     ELSE IF (CONFIG%MNE .GT. 0) THEN
+     ! ANE
+     IF (PRESENT(ANE)) CONFIG%ANE = ANE
+     ! ADE
+     IF (PRESENT(ADE)) THEN
+        CONFIG%ADE = ADE
+     ELSE IF (CONFIG%ANE .GT. 0) THEN
         ! Compute a reasonable default dimension (tied to volume of space).
-        CONFIG%MDE = MAX(1, 1 + CEILING(LOG(REAL(CONFIG%MNE,RT)) / LOG(2.0_RT)))
-        IF (CONFIG%MNE .GT. 2) CONFIG%MDE = CONFIG%MDE + 1
+        CONFIG%ADE = MAX(1, 1 + CEILING(LOG(REAL(CONFIG%ANE,RT)) / LOG(2.0_RT)))
+        IF (CONFIG%ANE .GT. 2) CONFIG%ADE = CONFIG%ADE + 1
      END IF
-     ! ---------------------------------------------------------------
+     ! ADN, ADI
+     CONFIG%ADN = ADN
+     CONFIG%ADI = CONFIG%ADN + CONFIG%ADE
      ! ADO
      IF (PRESENT(ADO)) THEN
         CONFIG%ADO = ADO
-     ELSE IF (ADI .EQ. 0) THEN
+     ELSE IF (CONFIG%ADI .EQ. 0) THEN
         CONFIG%ADO = 0
      END IF
      ! ADS
      IF (PRESENT(ADS)) THEN
         CONFIG%ADS = ADS
-     ELSE IF (ADI .EQ. 0) THEN
+     ELSE IF (CONFIG%ADI .EQ. 0) THEN
         CONFIG%ADS = 0
      END IF
      ! ANS
      IF (PRESENT(ANS)) THEN
         CONFIG%ANS = ANS
-     ELSE IF (ADI .EQ. 0) THEN
+     ELSE IF (CONFIG%ADI .EQ. 0) THEN
         CONFIG%ANS = 0
      END IF
-     ! ANE
-     IF (PRESENT(ANE)) CONFIG%ANE = ANE
-     ! ADE
-     IF (PRESENT(ADE)) THEN
-        CONFIG%ADE = ADE
-     ELSE IF (CONFIG%ANE .GT. 0) THEN
+     ! ---------------------------------------------------------------
+     ! MDO
+     CONFIG%MDO = MDO
+     ! MDS
+     IF (PRESENT(MDS)) CONFIG%MDS = MDS
+     ! MNS
+     IF (PRESENT(MNS)) CONFIG%MNS = MNS
+     ! MNE
+     IF (PRESENT(MNE)) CONFIG%MNE = MNE
+     ! MDE
+     IF (PRESENT(MDE)) THEN
+        CONFIG%MDE = MDE
+     ELSE IF (CONFIG%MNE .GT. 0) THEN
         ! Compute a reasonable default dimension (tied to volume of space).
-        CONFIG%ADE = MAX(1, 1 + CEILING(LOG(REAL(CONFIG%ANE,RT)) / LOG(2.0_RT)))
-        IF (CONFIG%ANE .GT. 2) CONFIG%ADE = CONFIG%ADE + 1
+        CONFIG%MDE = MAX(1, 1 + CEILING(LOG(REAL(CONFIG%MNE,RT)) / LOG(2.0_RT)))
+        IF (CONFIG%MNE .GT. 2) CONFIG%MDE = CONFIG%MDE + 1
      END IF
+     ! MDN, MDI
+     CONFIG%MDN = MDN
+     CONFIG%MDI = CONFIG%MDN + CONFIG%MDE + CONFIG%ADO
      ! ---------------------------------------------------------------
      ! NUM_THREADS
      IF (PRESENT(NUM_THREADS)) THEN
         CONFIG%NUM_THREADS = NUM_THREADS
      ELSE
         CONFIG%NUM_THREADS = OMP_GET_MAX_THREADS()
      END IF
-     ! Declare all required configurations.
-     CONFIG%ADI = ADI + CONFIG%ADE
-     CONFIG%MDI = MDI + CONFIG%MDE + CONFIG%ADO
-     CONFIG%MDO = MDO
      ! Compute indices related to the parameter vector for this model.
      CONFIG%TOTAL_SIZE = 0
      ! ---------------------------------------------------------------
-     !   model input vecs
-     CONFIG%MSIV = 1 + CONFIG%TOTAL_SIZE
-     CONFIG%MEIV = CONFIG%MSIV-1  +  CONFIG%MDI * CONFIG%MDS
-     CONFIG%TOTAL_SIZE = CONFIG%MEIV
-     !   model input shift
-     CONFIG%MSIS = 1 + CONFIG%TOTAL_SIZE
-     CONFIG%MEIS = CONFIG%MSIS-1  +  CONFIG%MDS
-     CONFIG%TOTAL_SIZE = CONFIG%MEIS
-     !   model state vecs
-     CONFIG%MSSV = 1 + CONFIG%TOTAL_SIZE
-     CONFIG%MESV = CONFIG%MSSV-1  +  CONFIG%MDS * CONFIG%MDS * (CONFIG%MNS-1)
-     CONFIG%TOTAL_SIZE = CONFIG%MESV
-     !   model state shift
-     CONFIG%MSSS = 1 + CONFIG%TOTAL_SIZE
-     CONFIG%MESS = CONFIG%MSSS-1  +  CONFIG%MDS * (CONFIG%MNS-1)
-     CONFIG%TOTAL_SIZE = CONFIG%MESS
-     !   model output vecs
-     CONFIG%MSOV = 1 + CONFIG%TOTAL_SIZE
-     CONFIG%MEOV = CONFIG%MSOV-1  +  CONFIG%MDS * CONFIG%MDO
-     CONFIG%TOTAL_SIZE = CONFIG%MEOV
-     !   model embedding vecs
-     CONFIG%MSEV = 1 + CONFIG%TOTAL_SIZE
-     CONFIG%MEEV = CONFIG%MSEV-1  +  CONFIG%MDE * CONFIG%MNE
-     CONFIG%TOTAL_SIZE = CONFIG%MEEV
-     ! ---------------------------------------------------------------
      !   apositional input vecs
      CONFIG%ASIV = 1 + CONFIG%TOTAL_SIZE
      CONFIG%AEIV = CONFIG%ASIV-1  +  CONFIG%ADI * CONFIG%ADS
      CONFIG%TOTAL_SIZE = CONFIG%AEIV
      !   apositional input shift
      CONFIG%ASIS = 1 + CONFIG%TOTAL_SIZE
      CONFIG%AEIS = CONFIG%ASIS-1  +  CONFIG%ADS
@@ -312,31 +792,187 @@
      CONFIG%AEOV = CONFIG%ASOV-1  +  CONFIG%ADS * CONFIG%ADO
      CONFIG%TOTAL_SIZE = CONFIG%AEOV
      !   apositional embedding vecs
      CONFIG%ASEV = 1 + CONFIG%TOTAL_SIZE
      CONFIG%AEEV = CONFIG%ASEV-1  +  CONFIG%ADE * CONFIG%ANE
      CONFIG%TOTAL_SIZE = CONFIG%AEEV
      ! ---------------------------------------------------------------
+     !   model input vecs
+     CONFIG%MSIV = 1 + CONFIG%TOTAL_SIZE
+     CONFIG%MEIV = CONFIG%MSIV-1  +  CONFIG%MDI * CONFIG%MDS
+     CONFIG%TOTAL_SIZE = CONFIG%MEIV
+     !   model input shift
+     CONFIG%MSIS = 1 + CONFIG%TOTAL_SIZE
+     CONFIG%MEIS = CONFIG%MSIS-1  +  CONFIG%MDS
+     CONFIG%TOTAL_SIZE = CONFIG%MEIS
+     !   model state vecs
+     CONFIG%MSSV = 1 + CONFIG%TOTAL_SIZE
+     CONFIG%MESV = CONFIG%MSSV-1  +  CONFIG%MDS * CONFIG%MDS * (CONFIG%MNS-1)
+     CONFIG%TOTAL_SIZE = CONFIG%MESV
+     !   model state shift
+     CONFIG%MSSS = 1 + CONFIG%TOTAL_SIZE
+     CONFIG%MESS = CONFIG%MSSS-1  +  CONFIG%MDS * (CONFIG%MNS-1)
+     CONFIG%TOTAL_SIZE = CONFIG%MESS
+     !   model output vecs
+     CONFIG%MSOV = 1 + CONFIG%TOTAL_SIZE
+     CONFIG%MEOV = CONFIG%MSOV-1  +  CONFIG%MDS * CONFIG%MDO
+     CONFIG%TOTAL_SIZE = CONFIG%MEOV
+     !   model embedding vecs
+     CONFIG%MSEV = 1 + CONFIG%TOTAL_SIZE
+     CONFIG%MEEV = CONFIG%MSEV-1  +  CONFIG%MDE * CONFIG%MNE
+     CONFIG%TOTAL_SIZE = CONFIG%MEEV
+     ! ---------------------------------------------------------------
      !   number of variables
      CONFIG%NUM_VARS = CONFIG%TOTAL_SIZE
      ! ---------------------------------------------------------------
+     !   apositional input shift
+     CONFIG%AISS = 1 + CONFIG%TOTAL_SIZE
+     CONFIG%AISE = CONFIG%AISS-1 + CONFIG%ADN
+     CONFIG%TOTAL_SIZE = CONFIG%AISE
+     !   apositional output shift
+     CONFIG%AOSS = 1 + CONFIG%TOTAL_SIZE
+     CONFIG%AOSE = CONFIG%AOSS-1 + CONFIG%ADO
+     CONFIG%TOTAL_SIZE = CONFIG%AOSE
      !   model input shift
      CONFIG%MISS = 1 + CONFIG%TOTAL_SIZE
-     CONFIG%MISE = CONFIG%MISS-1 + CONFIG%MDI-CONFIG%ADO-CONFIG%MDE
+     CONFIG%MISE = CONFIG%MISS-1 + CONFIG%MDN
      CONFIG%TOTAL_SIZE = CONFIG%MISE
      !   model output shift
      CONFIG%MOSS = 1 + CONFIG%TOTAL_SIZE
      CONFIG%MOSE = CONFIG%MOSS-1 + CONFIG%MDO
      CONFIG%TOTAL_SIZE = CONFIG%MOSE
-     !   apositional input shift
-     CONFIG%AISS = 1 + CONFIG%TOTAL_SIZE
-     CONFIG%AISE = CONFIG%AISS-1 + CONFIG%ADI-CONFIG%ADE
-     CONFIG%TOTAL_SIZE = CONFIG%AISE
   END SUBROUTINE NEW_MODEL_CONFIG
 
+  ! Given a number of X points "NM", and a number of apositional X points
+  ! "NA", update the "RWORK_SIZE" and "IWORK_SIZE" attributes in "CONFIG"
+  ! as well as all related work indices for that size data.
+  SUBROUTINE NEW_FIT_CONFIG(NM, NA, CONFIG)
+    INTEGER, INTENT(IN) :: NM, NA
+    TYPE(MODEL_CONFIG), INTENT(INOUT) :: CONFIG
+    CONFIG%NM = NM
+    CONFIG%NA = NA
+    ! ------------------------------------------------------------
+    ! Set up the real valued work array.
+    CONFIG%RWORK_SIZE = 0
+    ! model gradient
+    CONFIG%SMG = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EMG = CONFIG%SMG-1 + CONFIG%NUM_VARS
+    CONFIG%RWORK_SIZE = CONFIG%EMG
+    ! model gradient mean
+    CONFIG%SMGM = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EMGM = CONFIG%SMGM-1 + CONFIG%NUM_VARS
+    CONFIG%RWORK_SIZE = CONFIG%EMGM
+    ! model gradient curvature
+    CONFIG%SMGC = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EMGC = CONFIG%SMGC-1 + CONFIG%NUM_VARS
+    CONFIG%RWORK_SIZE = CONFIG%EMGC
+    ! best model
+    CONFIG%SBM = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EBM = CONFIG%SBM-1 + CONFIG%NUM_VARS
+    CONFIG%RWORK_SIZE = CONFIG%EBM
+    ! apositional states
+    CONFIG%SAXS = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EAXS = CONFIG%SAXS-1 + CONFIG%NA * CONFIG%ADS * (CONFIG%ANS+1)
+    CONFIG%RWORK_SIZE = CONFIG%EAXS
+    ! apositional model gradients at states
+    CONFIG%SAXG = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EAXG = CONFIG%SAXG-1 + CONFIG%NA * CONFIG%ADS * (CONFIG%ANS+1)
+    CONFIG%RWORK_SIZE = CONFIG%EAXG
+    ! apositional model (internal state) alignment
+    CONFIG%SAA = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EAA = CONFIG%SAA-1 + CONFIG%ADS * CONFIG%ANS
+    CONFIG%RWORK_SIZE = CONFIG%EAA
+    ! AY
+    CONFIG%SAY = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EAY = CONFIG%SAY-1 + CONFIG%NA * CONFIG%ADO
+    CONFIG%RWORK_SIZE = CONFIG%EAY
+    ! AY gradient
+    CONFIG%SAYG = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EAYG = CONFIG%SAYG-1 + CONFIG%NA * CONFIG%ADO
+    CONFIG%RWORK_SIZE = CONFIG%EAYG
+    ! model states
+    CONFIG%SMXS = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EMXS = CONFIG%SMXS-1 + CONFIG%NM * CONFIG%MDS * (CONFIG%MNS+1)
+    CONFIG%RWORK_SIZE = CONFIG%EMXS
+    ! model gradients at states
+    CONFIG%SMXG = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EMXG = CONFIG%SMXG-1 + CONFIG%NM * CONFIG%MDS * (CONFIG%MNS+1)
+    CONFIG%RWORK_SIZE = CONFIG%EMXG
+    ! (positional) model (internal state) alignment
+    CONFIG%SMA = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EMA = CONFIG%SMA-1 + CONFIG%MDS * CONFIG%MNS
+    CONFIG%RWORK_SIZE = CONFIG%EMA
+    ! Y gradient
+    CONFIG%SYG = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EYG = CONFIG%SYG-1 + CONFIG%MDO * CONFIG%NM
+    CONFIG%RWORK_SIZE = CONFIG%EYG
+    ! AX rescale
+    CONFIG%SAXR = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EAXR = CONFIG%SAXR-1 + CONFIG%ADN * CONFIG%ADN
+    CONFIG%RWORK_SIZE = CONFIG%EAXR
+    ! AXI shift
+    CONFIG%SAXIS = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EAXIS = CONFIG%SAXIS-1 + CONFIG%ADE
+    CONFIG%RWORK_SIZE = CONFIG%EAXIS
+    ! AXI rescale
+    CONFIG%SAXIR = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EAXIR = CONFIG%SAXIR-1 + CONFIG%ADE * CONFIG%ADE
+    CONFIG%RWORK_SIZE = CONFIG%EAXIR
+    ! AY rescale
+    CONFIG%SAYR = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EAYR = CONFIG%SAYR-1 + CONFIG%ADO
+    CONFIG%RWORK_SIZE = CONFIG%EAYR
+    ! X rescale
+    CONFIG%SMXR = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EMXR = CONFIG%SMXR-1 + CONFIG%MDN * CONFIG%MDN
+    CONFIG%RWORK_SIZE = CONFIG%EMXR
+    ! XI shift
+    CONFIG%SMXIS = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EMXIS = CONFIG%SMXIS-1 + CONFIG%MDE
+    CONFIG%RWORK_SIZE = CONFIG%EMXIS
+    ! XI rescale
+    CONFIG%SMXIR = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EMXIR = CONFIG%SMXIR-1 + CONFIG%MDE * CONFIG%MDE
+    CONFIG%RWORK_SIZE = CONFIG%EMXIR
+    ! Y rescale
+    CONFIG%SYR = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EYR = CONFIG%SYR-1 + CONFIG%MDO * CONFIG%MDO
+    CONFIG%RWORK_SIZE = CONFIG%EYR
+    ! MODEL ALIGN
+    CONFIG%SFMA = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EFMA = CONFIG%SFMA-1 + CONFIG%NUM_VARS * CONFIG%NUM_THREADS
+    CONFIG%RWORK_SIZE = CONFIG%EFMA
+    ! X_TEMP
+    CONFIG%SXT = 1 + CONFIG%RWORK_SIZE
+    CONFIG%EXT = CONFIG%SXT-1 + (CONFIG%MDE + CONFIG%ADO) * CONFIG%NM * CONFIG%NUM_THREADS
+    CONFIG%RWORK_SIZE = CONFIG%EXT
+    ! ------------------------------------------------------------
+    ! Set up the integer valued work array.
+    CONFIG%IWORK_SIZE = 0
+    ! update indices of model 
+    CONFIG%SUI = 1 + CONFIG%IWORK_SIZE
+    CONFIG%EUI = CONFIG%SUI-1 + CONFIG%NUM_VARS
+    CONFIG%IWORK_SIZE = CONFIG%EUI
+    ! apositional batch starts
+    CONFIG%SBAS = 1 + CONFIG%IWORK_SIZE
+    CONFIG%EBAS = CONFIG%SBAS-1 + CONFIG%NUM_THREADS
+    CONFIG%IWORK_SIZE = CONFIG%EBAS
+    ! apositional batch ends
+    CONFIG%SBAE = 1 + CONFIG%IWORK_SIZE
+    CONFIG%EBAE = CONFIG%SBAE-1 + CONFIG%NUM_THREADS
+    CONFIG%IWORK_SIZE = CONFIG%EBAE
+    ! model batch starts
+    CONFIG%SBMS = 1 + CONFIG%IWORK_SIZE
+    CONFIG%EBMS = CONFIG%SBMS-1 + CONFIG%NUM_THREADS
+    CONFIG%IWORK_SIZE = CONFIG%EBMS
+    ! model batchm ends
+    CONFIG%SBME = 1 + CONFIG%IWORK_SIZE
+    CONFIG%EBME = CONFIG%SBME-1 + CONFIG%NUM_THREADS
+    CONFIG%IWORK_SIZE = CONFIG%EBME
+  END SUBROUTINE NEW_FIT_CONFIG
 
   ! Initialize the weights for a model, optionally provide a random seed.
   SUBROUTINE INIT_MODEL(CONFIG, MODEL, SEED)
     TYPE(MODEL_CONFIG), INTENT(IN) :: CONFIG
     REAL(KIND=RT), INTENT(INOUT), DIMENSION(:) :: MODEL
     INTEGER, INTENT(IN), OPTIONAL :: SEED
     !  Storage for seeding the random number generator (for repeatability).
@@ -382,252 +1018,241 @@
       INTEGER, INTENT(IN) :: MDI, MDS, MNS, MDO, MDE, MNE
       REAL(KIND=RT), DIMENSION(MDI, MDS) :: INPUT_VECS
       REAL(KIND=RT), DIMENSION(MDS) :: INPUT_SHIFT
       REAL(KIND=RT), DIMENSION(MDS, MDS, MNS-1) :: STATE_VECS
       REAL(KIND=RT), DIMENSION(MDS, MNS-1) :: STATE_SHIFT
       REAL(KIND=RT), DIMENSION(MDS, MDO) :: OUTPUT_VECS
       REAL(KIND=RT), DIMENSION(MDE, MNE) :: EMBEDDINGS
+      ! Local holder for "origin" at each layer.
+      REAL(KIND=RT), DIMENSION(MDS) :: ORIGIN
+      INTEGER,       DIMENSION(MDS) :: ORDER
+      INTEGER :: I, J
       ! Generate well spaced random unit-length vectors (no scaling biases)
       ! for all initial variables in the input, internal, output, and embedings.
       CALL RANDOM_UNIT_VECTORS(INPUT_VECS(:,:))
       DO I = 1, MNS-1
          CALL RANDOM_UNIT_VECTORS(STATE_VECS(:,:,I))
       END DO
       CALL RANDOM_UNIT_VECTORS(OUTPUT_VECS(:,:))
       CALL RANDOM_UNIT_VECTORS(EMBEDDINGS(:,:))
       ! Make the output vectors have very small magnitude initially.
       OUTPUT_VECS(:,:) = OUTPUT_VECS(:,:) * CONFIG%INITIAL_OUTPUT_SCALE
       ! Generate random shifts for inputs and internal layers, zero
       !  shift for the output layer (first two will be rescaled).
       DO I = 1, MDS
-         INPUT_SHIFT(I) = 2.0_RT * CONFIG%INITIAL_SHIFT_RANGE * &    ! 2 * shift *
-              (REAL(I-1,RT) / MAX(1.0_RT, REAL(MDS-1, RT))) & ! range [0, 1]
-              - CONFIG%INITIAL_SHIFT_RANGE                           ! - shift
-         STATE_SHIFT(I,:) = INPUT_SHIFT(I) ! range [-shift, shift]
+         INPUT_SHIFT(I) = 2.0_RT * CONFIG%INITIAL_SHIFT_RANGE * & ! 2 * shift *
+              (REAL(I-1,RT) / MAX(1.0_RT, REAL(MDS-1, RT))) &     ! range [0, 1]
+              - CONFIG%INITIAL_SHIFT_RANGE                        ! - shift
+      END DO
+      ! Set the state shifts based on translation of the origin, always try
+      !  to apply translations to bring the origin back closer to center
+      !  (to prevent terrible conditioning of models with many layers).
+      ORIGIN(:) = INPUT_SHIFT(:)
+      DO J = 1, MNS-1
+         ORIGIN(:) = MATMUL(ORIGIN(:), STATE_VECS(:,:,J))
+         ! Argsort the values of origin, adding the most to the smallest values.
+         CALL ARGSORT(ORIGIN(:), ORDER(:))
+         DO I = 1, MDS
+            STATE_SHIFT(ORDER(MDS-I+1),J) = INPUT_SHIFT(I) ! range [-shift, shift]
+         END DO
+         ORIGIN(:) = ORIGIN(:) + STATE_SHIFT(:,J)
       END DO
     END SUBROUTINE UNPACKED_INIT_MODEL
   END SUBROUTINE INIT_MODEL
 
 
   ! Returnn nonzero INFO if any shapes or values do not match expectations.
-  SUBROUTINE CHECK_SHAPE(CONFIG, MODEL, Y, X, XI, AX, AXI, SIZES, INFO)
+  SUBROUTINE CHECK_SHAPE(CONFIG, MODEL, AX, AXI, SIZES, X, XI, Y, INFO)
     TYPE(MODEL_CONFIG), INTENT(IN) :: CONFIG
     REAL(KIND=RT), INTENT(IN), DIMENSION(:) :: MODEL
-    REAL(KIND=RT), INTENT(IN), DIMENSION(:,:) :: Y
-    REAL(KIND=RT), INTENT(IN), DIMENSION(:,:) :: X
-    INTEGER,       INTENT(IN), DIMENSION(:,:) :: XI
     REAL(KIND=RT), INTENT(IN), DIMENSION(:,:) :: AX
     INTEGER,       INTENT(IN), DIMENSION(:,:) :: AXI
     INTEGER,       INTENT(IN), DIMENSION(:) :: SIZES
+    REAL(KIND=RT), INTENT(IN), DIMENSION(:,:) :: X
+    INTEGER,       INTENT(IN), DIMENSION(:,:) :: XI
+    REAL(KIND=RT), INTENT(IN), DIMENSION(:,:) :: Y
     INTEGER,       INTENT(OUT) :: INFO
     INFO = 0
     ! Compute whether the shape matches the CONFIG.
     IF (SIZE(MODEL) .NE. CONFIG%TOTAL_SIZE) THEN
        INFO = 1 ! Model size does not match model configuration.
     ELSE IF (SIZE(X,2) .NE. SIZE(Y,2)) THEN
        INFO = 2 ! Input arrays do not match in size.
-    ELSE IF (SIZE(X,1) + CONFIG%MDE + CONFIG%ADO .NE. CONFIG%MDI) THEN
+    ELSE IF (SIZE(X,1) .NE. CONFIG%MDI) THEN
        INFO = 3 ! X input dimension is bad.
     ELSE IF (SIZE(Y,1) .NE. CONFIG%MDO) THEN
        INFO = 4 ! Output dimension is bad.
     ELSE IF ((CONFIG%MNE .GT. 0) .AND. (SIZE(XI,2) .NE. SIZE(X,2))) THEN
-       INFO = 5 ! Input integer X size does not match.
+       INFO = 5 ! Input integer XI size does not match X.
     ELSE IF ((MINVAL(XI) .LT. 0) .OR. (MAXVAL(XI) .GT. CONFIG%MNE)) THEN
        INFO = 6 ! Input integer X index out of range.
-    ELSE IF ((CONFIG%ADI .GT. 0) .AND. (SIZE(X,2) .NE. SIZE(SIZES))) THEN
-       INFO = 7 ! X and SIZES do not match.
+    ELSE IF ((CONFIG%ADI .GT. 0) .AND. (SIZE(SIZES) .NE. SIZE(Y,2))) THEN
+       INFO = 7 ! SIZES has wrong size.
     ELSE IF (SIZE(AX,2) .NE. SUM(SIZES)) THEN
        INFO = 8 ! AX and SUM(SIZES) do not match.
-    ELSE IF (SIZE(AX,1) + CONFIG%ADE .NE. CONFIG%ADI) THEN
+    ELSE IF (SIZE(AX,1) .NE. CONFIG%ADI) THEN
        INFO = 9 ! AX input dimension is bad.
     ELSE IF (SIZE(AXI,2) .NE. SIZE(AX,2)) THEN
-       INFO = 10 ! Input integer AX size does not match.
+       INFO = 10 ! Input integer AXI size does not match AX.
     ELSE IF ((MINVAL(AXI) .LT. 0) .OR. (MAXVAL(AXI) .GT. CONFIG%ANE)) THEN
        INFO = 11 ! Input integer AX index out of range.
     END IF
   END SUBROUTINE CHECK_SHAPE
 
  
-  ! Given a model and mixed real and integer inputs, embed the inputs
-  !  into their appropriate real-value-only formats.
-  SUBROUTINE EMBED(CONFIG, MODEL, X, XI, AX, AXI, XXI, AXXI)
-    TYPE(MODEL_CONFIG), INTENT(IN) :: CONFIG
-    REAL(KIND=RT), INTENT(IN),  DIMENSION(:) :: MODEL
-    REAL(KIND=RT), INTENT(IN),  DIMENSION(:,:) :: X
-    INTEGER,       INTENT(IN),  DIMENSION(:,:) :: XI
-    REAL(KIND=RT), INTENT(IN),  DIMENSION(:,:) :: AX
-    INTEGER,       INTENT(IN),  DIMENSION(:,:) :: AXI
-    REAL(KIND=RT), INTENT(OUT), DIMENSION(:,:) :: XXI  ! MDI, SIZE(X,2)
-    REAL(KIND=RT), INTENT(OUT), DIMENSION(:,:) :: AXXI ! ADI, SIZE(AX,2)
-    ! Add the real inputs to the front of each vector before apositional outputs.
-    XXI(1:SIZE(X,1),:) = X(:,:)
-    ! If there is XInteger input, unpack it into end of XXI.
-    CALL UNPACK_EMBEDDINGS(CONFIG%MDE, CONFIG%MNE, &
-         MODEL(CONFIG%MSEV:CONFIG%MEEV), &
-         XI(:,:), XXI(SIZE(X,1)+1:SIZE(X,1)+CONFIG%MDE,:))
-    ! Add the real inputs to the front of each vector.
-    AXXI(1:SIZE(AX,1),:) = AX(:,:)
-    ! If there is AXInteger input, unpack it into XXI.
-    CALL UNPACK_EMBEDDINGS(CONFIG%ADE, CONFIG%ANE, &
-         MODEL(CONFIG%ASEV:CONFIG%AEEV), &
-         AXI(:,:), AXXI(SIZE(AX,1)+1:,:))
-  CONTAINS
-    ! Given integer inputs and embedding vectors, put embeddings in
-    !  place of integer inputs inside of a real matrix.
-    SUBROUTINE UNPACK_EMBEDDINGS(MDE, MNE, EMBEDDINGS, INT_INPUTS, EMBEDDED)
-      INTEGER, INTENT(IN) :: MDE, MNE
-      REAL(KIND=RT), INTENT(IN), DIMENSION(MDE, MNE) :: EMBEDDINGS
-      INTEGER, INTENT(IN), DIMENSION(:,:) :: INT_INPUTS
-      REAL(KIND=RT), INTENT(OUT), DIMENSION(:,:) :: EMBEDDED
-      INTEGER :: N, D, E
-      REAL(KIND=RT) :: RD
-      RD = REAL(SIZE(INT_INPUTS,1),RT)
-      ! Add together appropriate embedding vectors based on integer inputs.
-      EMBEDDED(:,:) = 0.0_RT
-      DO N = 1, SIZE(INT_INPUTS,2)
-         DO D = 1, SIZE(INT_INPUTS,1)
-            E = INT_INPUTS(D,N)
-            IF (E .GT. 0) THEN
-               EMBEDDED(:,N) = EMBEDDED(:,N) + EMBEDDINGS(:,E)
-            END IF
-         END DO
-         EMBEDDED(:,N) = EMBEDDED(:,N) / RD
-      END DO
-    END SUBROUTINE UNPACK_EMBEDDINGS
-  END SUBROUTINE EMBED
-
-
   ! Given a number of batches, compute the batch start and ends for
   !  the apositional and positional inputs. Store in (2,_) arrays.
-  SUBROUTINE COMPUTE_BATCHES(NUM_BATCHES, X, AX, SIZES, BATCHA, BATCHM, INFO)
-    INTEGER,       INTENT(IN) :: NUM_BATCHES
-    REAL(KIND=RT), INTENT(IN),  DIMENSION(:,:) :: X
-    REAL(KIND=RT), INTENT(IN),  DIMENSION(:,:) :: AX
+  SUBROUTINE COMPUTE_BATCHES(NUM_BATCHES, NM, NA, SIZES, &
+       BATCHA_STARTS, BATCHA_ENDS, BATCHM_STARTS, BATCHM_ENDS, INFO)
+    INTEGER,       INTENT(IN) :: NUM_BATCHES, NM, NA
     INTEGER,       INTENT(IN),  DIMENSION(:)   :: SIZES
-    INTEGER,       INTENT(OUT), DIMENSION(:,:) :: BATCHA, BATCHM
+    INTEGER,       INTENT(OUT), DIMENSION(:) :: BATCHA_STARTS, BATCHA_ENDS
+    INTEGER,       INTENT(OUT), DIMENSION(:) :: BATCHM_STARTS, BATCHM_ENDS
     INTEGER,       INTENT(INOUT) :: INFO
     ! Local variables.
-    INTEGER :: BATCH, BE, BN, BS, I, MN, AN
-    ! Compute sizes of inputs.
-    IF ((SIZE(SIZES) .GT. 0) .OR. (SIZE(AX,2) .GT. 0)) THEN
-       MN = SIZE(SIZES)
-    ELSE
-       MN = SIZE(X,2)
-    END IF
-    AN = SUM(SIZES(:))
+    INTEGER :: BATCH, BE, BN, BS, I
     ! Check for errors.
-    IF (SIZE(X,2) .NE. MN) THEN
-       PRINT *, 'ERROR (COMPUTE_BATCHES): Sizes of X and SIZES do not match.', SIZE(X,2), SIZE(SIZES)
+    IF (NUM_BATCHES .GT. NM) THEN
+       PRINT *, 'ERROR (COMPUTE_BATCHES): Requested number of batches is too large.', NUM_BATCHES, NM, NA
        INFO = -1
-    ELSE IF (SIZE(AX,2) .NE. AN) THEN
-       PRINT *, 'ERROR (COMPUTE_BATCHES): Size of AX and sum of SIZES do not match.', SIZE(AX,2), AN
+       RETURN
+    ELSE IF (NUM_BATCHES .NE. SIZE(BATCHA_STARTS)) THEN
+       PRINT *, 'ERROR (COMPUTE_BATCHES): Number of batches does not match BATCHA.', NUM_BATCHES, SIZE(BATCHA_STARTS)
        INFO = -2
-    ELSE IF (NUM_BATCHES .GT. MN) THEN
-       PRINT *, 'ERROR (COMPUTE_BATCHES): Requested number of batches is too large.', NUM_BATCHES, MN, AN
+       RETURN
+    ELSE IF (NUM_BATCHES .NE. SIZE(BATCHM_STARTS)) THEN
+       PRINT *, 'ERROR (COMPUTE_BATCHES): Number of batches does not match BATCHM.', NUM_BATCHES, SIZE(BATCHM_STARTS)
        INFO = -3
-    ELSE IF (NUM_BATCHES .NE. SIZE(BATCHA,2)) THEN
-       PRINT *, 'ERROR (COMPUTE_BATCHES): Number of batches does not match BATCHA.', NUM_BATCHES, SIZE(BATCHA,2)
+       RETURN
+    ELSE IF (NUM_BATCHES .LT. 1) THEN
+       PRINT *, 'ERROR (COMPUTE_BATCHES): Number of batches is negative.', NUM_BATCHES
        INFO = -4
-    ELSE IF (NUM_BATCHES .NE. SIZE(BATCHM,2)) THEN
-       PRINT *, 'ERROR (COMPUTE_BATCHES): Number of batches does not match BATCHM.', NUM_BATCHES, SIZE(BATCHM,2)
-       INFO = -5
+       RETURN
     END IF
-    IF (INFO .NE. 0) RETURN
     ! Construct batches for data sets with apositional inputs.
-    IF (AN .GT. 0) THEN
+    IF (NA .GT. 0) THEN
        IF (NUM_BATCHES .EQ. 1) THEN
-          BATCHA(1,1) = 1
-          BATCHA(2,1) = AN
-          BATCHM(1,1) = 1
-          BATCHM(2,1) = MN
+          BATCHA_STARTS(1) = 1
+          BATCHA_ENDS(1) = NA
+          BATCHM_STARTS(1) = 1
+          BATCHM_ENDS(1) = NM
        ELSE
-          BN = (AN + NUM_BATCHES - 1) / NUM_BATCHES ! = CEIL(AN / NUM_BATCHES)
+          BN = (NA + NUM_BATCHES - 1) / NUM_BATCHES ! = CEIL(NA / NUM_BATCHES)
           ! Compute how many X points are associated with each Y.
           BS = 1
           BE = SIZES(1)
           BATCH = 1
-          BATCHM(1,BATCH) = 1
-          DO I = 2, MN
+          BATCHM_STARTS(BATCH) = 1
+          DO I = 2, NM
              ! If a fair share of the points have been aggregated, OR
              !   there are only as many sets left as there are batches.
-             IF ((BE-BS .GT. BN) .OR. (1+MN-I .LE. (NUM_BATCHES-BATCH))) THEN
-                BATCHM(2,BATCH) = I-1
-                BATCHA(1,BATCH) = BS
-                BATCHA(2,BATCH) = BE
+             IF ((BE-BS .GT. BN) .OR. (1+NM-I .LE. (NUM_BATCHES-BATCH))) THEN
+                BATCHM_ENDS(BATCH) = I-1
+                BATCHA_STARTS(BATCH) = BS
+                BATCHA_ENDS(BATCH) = BE
                 BATCH = BATCH+1
-                BATCHM(1,BATCH) = I
+                BATCHM_STARTS(BATCH) = I
                 BS = BE+1
                 BE = BS - 1
              END IF
              BE = BE + SIZES(I)
           END DO
-          BATCHM(2,BATCH) = MN
-          BATCHA(1,BATCH) = BS
-          BATCHA(2,BATCH) = BE
+          BATCHM_ENDS(BATCH) = NM
+          BATCHA_STARTS(BATCH) = BS
+          BATCHA_ENDS(BATCH) = BE
        END IF
     ! Construct batches for data sets that only have positional inputs.
     ELSE
-       BN = (MN + NUM_BATCHES - 1) / NUM_BATCHES ! = CEIL(MN / NUM_BATCHES)
+       BN = (NM + NUM_BATCHES - 1) / NUM_BATCHES ! = CEIL(NM / NUM_BATCHES)
        DO BATCH = 1, NUM_BATCHES
-          BATCHM(1,BATCH) = BN*(BATCH-1) + 1
-          BATCHM(2,BATCH) = MIN(MN, BN*BATCH)
+          BATCHM_STARTS(BATCH) = BN*(BATCH-1) + 1
+          BATCHM_ENDS(BATCH) = MIN(NM, BN*BATCH)
        END DO
-       BATCHA(1,:) = 0
-       BATCHA(2,:) = -1
+       BATCHA_STARTS(:) = 0
+       BATCHA_ENDS(:) = -1
     END IF
   END SUBROUTINE COMPUTE_BATCHES
 
 
+  ! Given a model and mixed real and integer inputs, embed the integer
+  !  inputs into their appropriate real-value-only formats.
+  SUBROUTINE EMBED(CONFIG, MODEL, AXI, XI, AX, X)
+    TYPE(MODEL_CONFIG), INTENT(IN) :: CONFIG
+    REAL(KIND=RT), INTENT(IN),  DIMENSION(:) :: MODEL
+    INTEGER,       INTENT(IN),  DIMENSION(:,:) :: AXI
+    INTEGER,       INTENT(IN),  DIMENSION(:,:) :: XI
+    REAL(KIND=RT), INTENT(OUT), DIMENSION(:,:) :: AX ! ADI, SIZE(AX,2)
+    REAL(KIND=RT), INTENT(OUT), DIMENSION(:,:) :: X  ! MDI, SIZE(X,2)
+    ! If there is AXInteger input, unpack it into X.
+    CALL UNPACK_EMBEDDINGS(CONFIG%ADE, CONFIG%ANE, &
+         MODEL(CONFIG%ASEV:CONFIG%AEEV), &
+         AXI(:,:), AX(CONFIG%ADI-CONFIG%ADE+1:,:))
+    ! If there is XInteger input, unpack it into end of X.
+    CALL UNPACK_EMBEDDINGS(CONFIG%MDE, CONFIG%MNE, &
+         MODEL(CONFIG%MSEV:CONFIG%MEEV), &
+         XI(:,:), X(CONFIG%MDI-CONFIG%MDE-CONFIG%ADO+1:CONFIG%MDI-CONFIG%ADO,:))
+  CONTAINS
+    ! Given integer inputs and embedding vectors, put embeddings in
+    !  place of integer inputs inside of a real matrix.
+    SUBROUTINE UNPACK_EMBEDDINGS(MDE, MNE, EMBEDDINGS, INT_INPUTS, EMBEDDED)
+      INTEGER, INTENT(IN) :: MDE, MNE
+      REAL(KIND=RT), INTENT(IN), DIMENSION(MDE, MNE) :: EMBEDDINGS
+      INTEGER, INTENT(IN), DIMENSION(:,:) :: INT_INPUTS
+      REAL(KIND=RT), INTENT(OUT), DIMENSION(:,:) :: EMBEDDED
+      INTEGER :: N, D, E
+      REAL(KIND=RT) :: RD
+      RD = REAL(SIZE(INT_INPUTS,1),RT)
+      ! Add together appropriate embedding vectors based on integer inputs.
+      EMBEDDED(:,:) = 0.0_RT
+      DO N = 1, SIZE(INT_INPUTS,2)
+         DO D = 1, SIZE(INT_INPUTS,1)
+            E = INT_INPUTS(D,N)
+            IF (E .GT. 0) THEN
+               EMBEDDED(:,N) = EMBEDDED(:,N) + EMBEDDINGS(:,E)
+            END IF
+         END DO
+         EMBEDDED(:,N) = EMBEDDED(:,N) / RD
+      END DO
+    END SUBROUTINE UNPACK_EMBEDDINGS
+  END SUBROUTINE EMBED
+
+
   ! Evaluate the piecewise linear regression model, assume already-embedded inputs.
-  SUBROUTINE EVALUATE(CONFIG, MODEL, Y, X, AX, SIZES, M_STATES, &
-       A_STATES, AY, INFO, SHIFT, THREADS)
+  SUBROUTINE EVALUATE(CONFIG, MODEL, AX, AY, SIZES, X, Y, A_STATES, M_STATES, INFO)
     TYPE(MODEL_CONFIG), INTENT(IN) :: CONFIG
     REAL(KIND=RT), INTENT(IN),  DIMENSION(:) :: MODEL
-    REAL(KIND=RT), INTENT(OUT),   DIMENSION(:,:) :: Y
-    REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: X
     REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: AX
+    REAL(KIND=RT), INTENT(OUT),   DIMENSION(:,:) :: AY
     INTEGER,       INTENT(IN),    DIMENSION(:)   :: SIZES
-    REAL(KIND=RT), INTENT(OUT),   DIMENSION(:,:,:) :: M_STATES ! SIZE(X, 2), MDS, (MNS|2)
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: X
+    REAL(KIND=RT), INTENT(OUT),   DIMENSION(:,:) :: Y
     REAL(KIND=RT), INTENT(OUT),   DIMENSION(:,:,:) :: A_STATES ! SIZE(AX,2), ADS, (ANS|2)
-    REAL(KIND=RT), INTENT(OUT),   DIMENSION(:,:) :: AY ! SIZE(AX,2), ADO
+    REAL(KIND=RT), INTENT(OUT),   DIMENSION(:,:,:) :: M_STATES ! SIZE(X, 2), MDS, (MNS|2)
     INTEGER, INTENT(INOUT) :: INFO
-    LOGICAL, INTENT(IN), OPTIONAL :: SHIFT
-    INTEGER, INTENT(IN), OPTIONAL :: THREADS
     ! Internal values.
-    LOGICAL :: APPLY_SHIFT
     INTEGER :: I, BATCH, NB, BN, BS, BE, BT, GS, GE, NT
-    INTEGER, DIMENSION(:,:), ALLOCATABLE :: BATCHA, BATCHM
-    ! Set default for shifting data.
-    IF (PRESENT(SHIFT)) THEN
-       APPLY_SHIFT = SHIFT
-    ELSE
-       APPLY_SHIFT = .TRUE.
-    END IF
-    ! Set default for the number of threads.
-    IF (PRESENT(THREADS)) THEN
-       NT = THREADS
-    ELSE
-       NT = CONFIG%NUM_THREADS
-    END IF
+    INTEGER, DIMENSION(:), ALLOCATABLE :: BATCHA_STARTS, BATCHA_ENDS, BATCHM_STARTS, BATCHM_ENDS
     ! Set up batching for parallelization.
-    NB = MIN(SIZE(Y,2), NT)
-    ALLOCATE(BATCHA(2,NB), BATCHM(2,NB))
+    NB = MIN(SIZE(Y,2), CONFIG%NUM_THREADS)
+    NT = MIN(CONFIG%NUM_THREADS, NB)
     ! Compute the batch start and end indices.
-    CALL COMPUTE_BATCHES(NB, X, AX, SIZES, BATCHA, BATCHM, INFO)
+    ALLOCATE(BATCHA_STARTS(NB), BATCHA_ENDS(NB), BATCHM_STARTS(NB), BATCHM_ENDS(NB))
+    CALL COMPUTE_BATCHES(NB, SIZE(X,2), SIZE(AX,2), SIZES, &
+         BATCHA_STARTS, BATCHA_ENDS, BATCHM_STARTS, BATCHM_ENDS, INFO)
     IF (INFO .NE. 0) RETURN
-    !$OMP PARALLEL DO NUM_THREADS(NT) PRIVATE(I, BS, BE, BT) IF(NB > 1)
+    !$OMP PARALLEL DO NUM_THREADS(NT) PRIVATE(I, BS, BE, BT, GS, GE) IF(NB > 1)
     batch_evaluation : DO BATCH = 1, NB
        ! If there is an apositional model, apply it.
        IF (CONFIG%ADI .GT. 0) THEN
-          BS = BATCHA(1,BATCH)
-          BE = BATCHA(2,BATCH)
+          BS = BATCHA_STARTS(BATCH)
+          BE = BATCHA_ENDS(BATCH)
           BT = BE-BS+1
           IF (BT .EQ. 0) CYCLE batch_evaluation
           ! Apply shift terms to apositional inputs.
-          IF (APPLY_SHIFT) THEN
+          IF (CONFIG%APPLY_SHIFT) THEN
              GE = CONFIG%ADI-CONFIG%ADE
              IF (GE .GT. 0) THEN
                 DO I = BS, BE
                    AX(:GE,I) = AX(:GE,I) + MODEL(CONFIG%AISS:CONFIG%AISE)
                 END DO
              END IF
           END IF
@@ -637,57 +1262,76 @@
                MODEL(CONFIG%ASIV:CONFIG%AEIV), &
                MODEL(CONFIG%ASIS:CONFIG%AEIS), &
                MODEL(CONFIG%ASSV:CONFIG%AESV), &
                MODEL(CONFIG%ASSS:CONFIG%AESS), &
                MODEL(CONFIG%ASOV:CONFIG%AEOV), &
                AX(:,BS:BE), AY(BS:BE,:), A_STATES(BS:BE,:,:), YTRANS=.TRUE.)
           ! Aggregate the outputs from the apositional model.
-          BT = SIZE(X,1)-CONFIG%ADO+1 ! <- reuse this variable name
+          BT = CONFIG%MDN+CONFIG%MDE+1 ! <- reuse to be "start of apositional output"
           GS = BS
-          DO I = BATCHM(1,BATCH), BATCHM(2,BATCH)
+          ! Always apply shift terms to apositional model outputs.
+          DO I = 1, CONFIG%ADO
+             AY(BS:BE,I) = AY(BS:BE,I) + MODEL(CONFIG%AOSS + I-1)
+          END DO
+          ! Take the mean of all outputs from the apositional model.
+          DO I = BATCHM_STARTS(BATCH), BATCHM_ENDS(BATCH)
              GE = GS + SIZES(I) - 1
              X(BT:,I) = SUM(AY(GS:GE,:), 1) / REAL(SIZES(I),RT) 
              GS = GE + 1
           END DO
-          BS = BATCHM(1,BATCH)
-          BE = BATCHM(2,BATCH)
+          ! Unapply shift terms to apositional inputs.
+          IF (CONFIG%APPLY_SHIFT) THEN
+             GE = CONFIG%ADI-CONFIG%ADE
+             IF (GE .GT. 0) THEN
+                DO I = BS, BE
+                   AX(:GE,I) = AX(:GE,I) - MODEL(CONFIG%AISS:CONFIG%AISE)
+                END DO
+             END IF
+          END IF
+          ! Update "BS", "BE", and "BT" to coincide with the model.
+          BS = BATCHM_STARTS(BATCH)
+          BE = BATCHM_ENDS(BATCH)
           BT = BE-BS+1
        ELSE
-          BS = BATCHM(1,BATCH)
-          BE = BATCHM(2,BATCH)
+          BS = BATCHM_STARTS(BATCH)
+          BE = BATCHM_ENDS(BATCH)
           BT = BE-BS+1
           IF (BT .EQ. 0) CYCLE batch_evaluation
        END IF
-       ! Apply shift terms to model inputs.
-       IF (APPLY_SHIFT) THEN
-          GE = CONFIG%MDI-CONFIG%MDE-CONFIG%ADO
-          IF (GE .GT. 0) THEN
+       ! Regular model forward pass.
+       IF (CONFIG%MDI .GT. 0) THEN
+          ! Apply shift terms to model inputs.
+          IF ((CONFIG%APPLY_SHIFT) .AND. (CONFIG%MDN .GT. 0)) THEN
              DO I = BS, BE
-                X(:GE,I) = X(:GE,I) + MODEL(CONFIG%MISS:CONFIG%MISE)
+                X(:CONFIG%MDN,I) = X(:CONFIG%MDN,I) + MODEL(CONFIG%MISS:CONFIG%MISE)
+             END DO
+          END IF
+          ! Run the positional model.
+          CALL UNPACKED_EVALUATE(BT, &
+               CONFIG%MDI, CONFIG%MDS, CONFIG%MNS, CONFIG%MDO, &
+               MODEL(CONFIG%MSIV:CONFIG%MEIV), &
+               MODEL(CONFIG%MSIS:CONFIG%MEIS), &
+               MODEL(CONFIG%MSSV:CONFIG%MESV), &
+               MODEL(CONFIG%MSSS:CONFIG%MESS), &
+               MODEL(CONFIG%MSOV:CONFIG%MEOV), &
+               X(:,BS:BE), Y(:,BS:BE), M_STATES(BS:BE,:,:), YTRANS=.FALSE.)
+          ! Apply shift terms to model outputs.
+          IF (CONFIG%APPLY_SHIFT) THEN
+             DO I = BS, BE
+                Y(:,I) = Y(:,I) + MODEL(CONFIG%MOSS:CONFIG%MOSE)
+             END DO
+             ! Unapply the X shifts.
+             DO I = BS, BE
+                X(:CONFIG%MDN,I) = X(:CONFIG%MDN,I) - MODEL(CONFIG%MISS:CONFIG%MISE)
              END DO
           END IF
-       END IF
-       ! Run the positional model.
-       CALL UNPACKED_EVALUATE(BT, &
-            CONFIG%MDI, CONFIG%MDS, CONFIG%MNS, CONFIG%MDO, &
-            MODEL(CONFIG%MSIV:CONFIG%MEIV), &
-            MODEL(CONFIG%MSIS:CONFIG%MEIS), &
-            MODEL(CONFIG%MSSV:CONFIG%MESV), &
-            MODEL(CONFIG%MSSS:CONFIG%MESS), &
-            MODEL(CONFIG%MSOV:CONFIG%MEOV), &
-            X(:,BS:BE), Y(:,BS:BE), M_STATES(BS:BE,:,:))
-       ! Apply shift terms to model outputs.
-       IF (APPLY_SHIFT) THEN
-          DO I = BS, BE
-             Y(:,I) = Y(:,I) + MODEL(CONFIG%MOSS:CONFIG%MOSE)
-          END DO
        END IF
     END DO batch_evaluation
     !$OMP END PARALLEL DO
-    DEALLOCATE(BATCHA, BATCHM)
+    DEALLOCATE(BATCHA_STARTS, BATCHA_ENDS, BATCHM_STARTS, BATCHM_ENDS)
 
   CONTAINS
 
     SUBROUTINE UNPACKED_EVALUATE(N, MDI, MDS, MNS, MDO, INPUT_VECS, &
          INPUT_SHIFT, STATE_VECS, STATE_SHIFT, OUTPUT_VECS, X, Y, &
          STATES, YTRANS)
       INTEGER, INTENT(IN) :: N, MDI, MDS, MNS, MDO
@@ -695,61 +1339,52 @@
       REAL(KIND=RT), INTENT(IN),  DIMENSION(MDS) :: INPUT_SHIFT
       REAL(KIND=RT), INTENT(IN),  DIMENSION(MDS, MDS, MNS-1) :: STATE_VECS
       REAL(KIND=RT), INTENT(IN),  DIMENSION(MDS, MNS-1) :: STATE_SHIFT
       REAL(KIND=RT), INTENT(IN),  DIMENSION(MDS, MDO) :: OUTPUT_VECS
       REAL(KIND=RT), INTENT(IN),  DIMENSION(:,:) :: X
       REAL(KIND=RT), INTENT(OUT), DIMENSION(:,:) :: Y
       REAL(KIND=RT), INTENT(OUT), DIMENSION(:,:,:) :: STATES
-      LOGICAL, INTENT(IN), OPTIONAL :: YTRANS
+      LOGICAL, INTENT(IN) :: YTRANS
       ! Local variables to evaluating a single batch.
       INTEGER :: D, L, S1, S2, S3
-      LOGICAL :: REUSE_STATES, YT
-      IF (PRESENT(YTRANS)) THEN
-         YT = YTRANS
-      ELSE
-         YT = .FALSE.
-      END IF
+      LOGICAL :: REUSE_STATES
       REUSE_STATES = (SIZE(STATES,3) .LT. MNS)
       ! Compute the input transformation.
       CALL GEMM('T', 'N', N, MDS, MDI, 1.0_RT, &
            X(:,:), SIZE(X,1), &
            INPUT_VECS(:,:), SIZE(INPUT_VECS,1), &
            0.0_RT, STATES(:,:,1), N)
       ! Apply the rectification.
       DO D = 1, MDS
          STATES(:,D,1) = MAX(STATES(:,D,1) + INPUT_SHIFT(D), CONFIG%DISCONTINUITY)
       END DO
       ! Compute the next set of internal values with a rectified activation.
       DO L = 1, MNS-1
          ! Determine the storage locations of values based on number of states.
-         IF (REUSE_STATES) THEN
-            S1 = 1 ; S2 = 2   ; S3 = 1
-         ELSE
-            S1 = L ; S2 = L+1 ; S3 = L+1
+         IF (REUSE_STATES) THEN ; S1 = 1 ; S2 = 2   ; S3 = 1
+         ELSE                   ; S1 = L ; S2 = L+1 ; S3 = L+1
          END IF
          ! Compute all vectors.
          CALL GEMM('N', 'N', N, MDS, MDS, 1.0_RT, &
               STATES(:,:,S1), N, &
               STATE_VECS(:,:,L), SIZE(STATE_VECS,1), &
               0.0_RT, STATES(:,:,S2), N)
          ! Compute all piecewise linear functions and apply the rectification.
          DO D = 1, MDS
             STATES(:,D,S3) = MAX(STATES(:,D,S2) + STATE_SHIFT(D,L), CONFIG%DISCONTINUITY)
          END DO
       END DO
       ! Set the location of the "previous state output".
-      IF (REUSE_STATES) THEN
-         S3 = 1
-      ELSE
-         S3 = MNS
+      IF (REUSE_STATES) THEN ; S3 = 1
+      ELSE                   ; S3 = MNS
       END IF
       ! Return the final output (default to assuming Y is contiguous
       !   by component unless PRESENT(YTRANS) and YTRANS = .TRUE.
       !   then assume it is contiguous by individual sample).
-      IF (YT) THEN
+      IF (YTRANS) THEN
          CALL GEMM('N', 'N', N, MDO, MDS, 1.0_RT, &
               STATES(:,:,S3), N, &
               OUTPUT_VECS(:,:), SIZE(OUTPUT_VECS,1), &
               0.0_RT, Y(:,:), SIZE(Y,1))
       ELSE
          CALL GEMM('T', 'T', MDO, N, MDS, 1.0_RT, &
               OUTPUT_VECS(:,:), SIZE(OUTPUT_VECS,1), &
@@ -762,43 +1397,43 @@
 
   ! Given the values at all internal states in the model and an output
   !  gradient, propogate the output gradient through the model and
   !  return the gradient of all basis functions.
   SUBROUTINE BASIS_GRADIENT(CONFIG, MODEL, Y, X, AX, SIZES, &
        M_STATES, A_STATES, AY, GRAD)
     TYPE(MODEL_CONFIG), INTENT(IN) :: CONFIG
-    REAL(KIND=RT), INTENT(IN),  DIMENSION(:) :: MODEL
-    REAL(KIND=RT), INTENT(IN), DIMENSION(:,:) :: Y
-    REAL(KIND=RT), INTENT(INOUT),  DIMENSION(:,:) :: X
-    REAL(KIND=RT), INTENT(INOUT),  DIMENSION(:,:) :: AX
-    INTEGER,       INTENT(IN),  DIMENSION(:)   :: SIZES
+    REAL(KIND=RT), INTENT(IN),    DIMENSION(:) :: MODEL
+    REAL(KIND=RT), INTENT(IN),    DIMENSION(:,:) :: Y
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: X
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: AX
+    INTEGER,       INTENT(IN),    DIMENSION(:) :: SIZES
     REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:,:) :: M_STATES ! SIZE(X, 2), MDS, MNS+1
     REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:,:) :: A_STATES ! SIZE(AX,2), ADS, ANS+1
     REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: AY ! SIZE(AX,2), ADO
-    REAL(KIND=RT), INTENT(OUT), DIMENSION(:) :: GRAD ! model gradient
+    REAL(KIND=RT), INTENT(OUT),   DIMENSION(:) :: GRAD
     ! Set the dimension of the X gradient that should be calculated.
     INTEGER :: I, J, GS, GE, XDG
+    XDG = CONFIG%MDE
     IF (CONFIG%ADI .GT. 0) THEN
-       XDG = CONFIG%ADO + CONFIG%MDE
-    ELSE
-       XDG = CONFIG%MDE
+       XDG = XDG + CONFIG%ADO
     END IF
     ! Do the backward gradient calculation assuming "Y" contains output gradient.
     CALL UNPACKED_BASIS_GRADIENT( Y(:,:), M_STATES(:,:,:), X(:,:), &
          CONFIG%MDI, CONFIG%MDS, CONFIG%MNS, CONFIG%MDO, XDG, &
          MODEL(CONFIG%MSIV:CONFIG%MEIV), &
          MODEL(CONFIG%MSIS:CONFIG%MEIS), &
          MODEL(CONFIG%MSSV:CONFIG%MESV), &
          MODEL(CONFIG%MSSS:CONFIG%MESS), &
          MODEL(CONFIG%MSOV:CONFIG%MEOV), &
          GRAD(CONFIG%MSIV:CONFIG%MEIV), &
          GRAD(CONFIG%MSIS:CONFIG%MEIS), &
          GRAD(CONFIG%MSSV:CONFIG%MESV), &
          GRAD(CONFIG%MSSS:CONFIG%MESS), &
-         GRAD(CONFIG%MSOV:CONFIG%MEOV))
+         GRAD(CONFIG%MSOV:CONFIG%MEOV), &
+         YTRANS=.FALSE.) ! Y is in COLUMN vector format.
     ! Propogate the gradient form X into the aggregate outputs.
     IF (CONFIG%ADI .GT. 0) THEN
        XDG = SIZE(X,1) - CONFIG%ADO + 1
        GS = 1
        DO I = 1, SIZE(SIZES)
           GE = GS + SIZES(I) - 1
           DO J = GS, GE
@@ -814,15 +1449,16 @@
             MODEL(CONFIG%ASSV:CONFIG%AESV), &
             MODEL(CONFIG%ASSS:CONFIG%AESS), &
             MODEL(CONFIG%ASOV:CONFIG%AEOV), &
             GRAD(CONFIG%ASIV:CONFIG%AEIV), &
             GRAD(CONFIG%ASIS:CONFIG%AEIS), &
             GRAD(CONFIG%ASSV:CONFIG%AESV), &
             GRAD(CONFIG%ASSS:CONFIG%AESS), &
-            GRAD(CONFIG%ASOV:CONFIG%AEOV), YTRANS=.TRUE.)
+            GRAD(CONFIG%ASOV:CONFIG%AEOV), &
+            YTRANS=.TRUE.) ! AY is in ROW vector format.
     END IF
 
   CONTAINS
     ! Compute the model gradient.
     SUBROUTINE UNPACKED_BASIS_GRADIENT( Y, STATES, X, &
          MDI, MDS, MNS, MDO, MDE, &
          INPUT_VECS, INPUT_SHIFT, &
@@ -842,33 +1478,27 @@
       REAL(KIND=RT), INTENT(IN), DIMENSION(MDS,MDO) :: OUTPUT_VECS
       ! Model variable gradients.
       REAL(KIND=RT), INTENT(INOUT), DIMENSION(MDI,MDS) :: INPUT_VECS_GRADIENT
       REAL(KIND=RT), INTENT(INOUT), DIMENSION(MDS) :: INPUT_SHIFT_GRADIENT
       REAL(KIND=RT), INTENT(INOUT), DIMENSION(MDS,MDS,MNS-1) :: STATE_VECS_GRADIENT
       REAL(KIND=RT), INTENT(INOUT), DIMENSION(MDS,MNS-1) :: STATE_SHIFT_GRADIENT
       REAL(KIND=RT), INTENT(INOUT), DIMENSION(MDS,MDO) :: OUTPUT_VECS_GRADIENT
-      LOGICAL, INTENT(IN), OPTIONAL :: YTRANS
+      LOGICAL, INTENT(IN) :: YTRANS
       ! D   - dimension index
       ! L   - layer index
       ! LP1 - layer index "plus 1" -> "P1"
       INTEGER :: D, L, LP1
       CHARACTER :: YT
       ! Number of points.
       REAL(KIND=RT) :: N, NORM
       ! Get the number of points.
       N = REAL(SIZE(X,2), RT)
       ! Set default for assuming Y is transposed (row vectors).
-      IF (PRESENT(YTRANS)) THEN
-         IF (YTRANS) THEN
-            YT = 'N'
-         ELSE
-            YT = 'T'
-         END IF
-      ELSE
-         YT = 'T'
+      IF (YTRANS) THEN ; YT = 'N'
+      ELSE             ; YT = 'T'
       END IF
       ! Compute the gradient of variables with respect to the "output gradient"
       CALL GEMM('T', YT, MDS, MDO, SIZE(X,2), 1.0_RT / N, &
            STATES(:,:,MNS), SIZE(STATES,1), &
            Y(:,:), SIZE(Y,1), &
            1.0_RT, OUTPUT_VECS_GRADIENT(:,:), SIZE(OUTPUT_VECS_GRADIENT,1))
       ! Propogate the gradient back to the last internal vector space.
@@ -959,363 +1589,671 @@
        END IF
     END DO
   END SUBROUTINE EMBEDDING_GRADIENT
 
 
   ! Compute the gradient of the sum of squared error of this regression
   ! model with respect to its variables given input and output pairs.
-  SUBROUTINE MODEL_GRADIENT(CONFIG, MODEL, Y, X, XI, AX, AXI, SIZES, &
-       SUM_SQUARED_GRADIENT, MODEL_GRAD, ERROR_GRADIENT, INFO, SHIFT, THREADS)
+  SUBROUTINE MODEL_GRADIENT(CONFIG, MODEL, AX, AXI, AY, SIZES, X, XI, Y, &
+       SUM_SQUARED_GRADIENT, MODEL_GRAD, A_ALIGN, M_ALIGN, MODEL_ALIGN, &
+       X_TEMP, AY_GRAD, Y_GRADIENT, A_STATES, A_GRADS, M_STATES, M_GRADS, &
+       INFO)
     TYPE(MODEL_CONFIG), INTENT(IN) :: CONFIG
     REAL(KIND=RT), INTENT(IN), DIMENSION(:) :: MODEL
-    REAL(KIND=RT), INTENT(IN), DIMENSION(:,:) :: Y
-    REAL(KIND=RT), INTENT(IN), DIMENSION(:,:) :: X
-    INTEGER,       INTENT(IN), DIMENSION(:,:) :: XI
-    REAL(KIND=RT), INTENT(IN), DIMENSION(:,:) :: AX
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: AX
     INTEGER,       INTENT(IN), DIMENSION(:,:) :: AXI
-    INTEGER,       INTENT(IN), DIMENSION(:)   :: SIZES
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: AY
+    INTEGER,       INTENT(IN), DIMENSION(:) :: SIZES
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: X
+    INTEGER,       INTENT(IN), DIMENSION(:,:) :: XI
+    REAL(KIND=RT), INTENT(IN), DIMENSION(:,:) :: Y
     ! Sum (over all data) squared error (summed over dimensions).
     REAL(KIND=RT), INTENT(INOUT) :: SUM_SQUARED_GRADIENT
     ! Gradient of the model parameters.
     REAL(KIND=RT), INTENT(OUT), DIMENSION(:) :: MODEL_GRAD
-    ! Interface to subroutine that computes the error gradient given outputs and targets.
-    INTERFACE
-       SUBROUTINE ERROR_GRADIENT(TARGETS, OUTPUTS)
-         USE ISO_FORTRAN_ENV, ONLY: RT => REAL32
-         REAL(KIND=RT), INTENT(IN),    DIMENSION(:,:) :: TARGETS
-         REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: OUTPUTS
-       END SUBROUTINE ERROR_GRADIENT
-    END INTERFACE
+    REAL(KIND=RT), INTENT(OUT), DIMENSION(:,:) :: A_ALIGN, M_ALIGN
+    ! Work space.
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(SIZE(MODEL_GRAD)) :: MODEL_ALIGN
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(CONFIG%MDE+CONFIG%ADO, SIZE(X,2)) :: X_TEMP
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(SIZE(AX,2),CONFIG%ADO) :: AY_GRAD
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(CONFIG%MDO,SIZE(Y,2)) :: Y_GRADIENT
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(SIZE(X,2),CONFIG%MDS,CONFIG%MNS+1) :: M_STATES, M_GRADS
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(SIZE(AX,2),CONFIG%ADS,CONFIG%ANS+1) :: A_STATES, A_GRADS
+    ! Output and optional inputs.
     INTEGER, INTENT(INOUT) :: INFO
-    LOGICAL, INTENT(IN), OPTIONAL :: SHIFT
-    INTEGER, INTENT(IN), OPTIONAL :: THREADS
-    ! Local allocations for computing gradient.
-    REAL(KIND=RT), DIMENSION(CONFIG%MDI,SIZE(X,2)) :: XXI
-    REAL(KIND=RT), DIMENSION(CONFIG%ADI,SIZE(AX,2)) :: AXXI
-    REAL(KIND=RT), DIMENSION(CONFIG%MDO,SIZE(Y,2)) :: Y_GRADIENT
-    REAL(KIND=RT), DIMENSION(SIZE(X,2),CONFIG%MDS,CONFIG%MNS+1) :: M_STATES
-    REAL(KIND=RT), DIMENSION(SIZE(AX,2),CONFIG%ADS,CONFIG%ANS+1) :: A_STATES
-    REAL(KIND=RT), DIMENSION(SIZE(AX,2),CONFIG%ADO) :: AY
+    INTEGER :: L, D
     ! Embed all integer inputs into real matrix inputs.
-    CALL EMBED(CONFIG, MODEL, X, XI, AX, AXI, XXI, AXXI)
+    CALL EMBED(CONFIG, MODEL, AXI, XI, AX, X)
     ! Evaluate the model, storing internal states (for gradient calculation).
-    CALL EVALUATE(CONFIG, MODEL, Y_GRADIENT, XXI, AXXI, SIZES, &
-         M_STATES, A_STATES, AY, INFO, SHIFT=SHIFT, THREADS=THREADS)
+    CALL EVALUATE(CONFIG, MODEL, AX, AY, SIZES, X, Y_GRADIENT, A_STATES, M_STATES, INFO)
+    ! --------------------------------------------------------------------------
+    ! Measure model alignmnt with function.
+    X_TEMP(:,:) = X(CONFIG%MDI-SIZE(X_TEMP,1)+1:,:)
+    A_GRADS(:,:,:) = A_STATES(:,:,:)
+    AY_GRAD(:,:) = AY(:,:)
+    M_GRADS(:,:,:) = M_STATES(:,:,:)
+    CALL BASIS_GRADIENT(CONFIG, MODEL, Y, X, AX, &
+         SIZES, M_GRADS, A_GRADS, AY_GRAD, MODEL_ALIGN)
+    ! Compute the "alignment" by summing the gradient over output vectors.
+    CALL UNPACKED_COMPUTE_ALIGNMENT( &
+         CONFIG%MDS, CONFIG%MNS, CONFIG%MDO, &
+         MODEL_ALIGN(CONFIG%MSSV:CONFIG%MESV), &
+         MODEL_ALIGN(CONFIG%MSOV:CONFIG%MEOV), &
+         M_ALIGN(:,:))
+    CALL UNPACKED_COMPUTE_ALIGNMENT( &
+         CONFIG%ADS, CONFIG%ANS, CONFIG%ADO, &
+         MODEL_ALIGN(CONFIG%ASSV:CONFIG%AESV), &
+         MODEL_ALIGN(CONFIG%ASOV:CONFIG%AEOV), &
+         A_ALIGN(:,:))
+    ! Reset X values (embedding values and apositional outputs).
+    X(CONFIG%MDI-SIZE(X_TEMP,1)+1:,:) = X_TEMP(:,:)
+    ! --------------------------------------------------------------------------
     ! Compute the gradient of the model outputs, overwriting "Y_GRADIENT"
-    CALL ERROR_GRADIENT(Y, Y_GRADIENT)
+    Y_GRADIENT(:,:) = Y_GRADIENT(:,:) - Y(:,:) ! squared error gradient
     SUM_SQUARED_GRADIENT = SUM_SQUARED_GRADIENT + SUM(Y_GRADIENT(:,:)**2)
+    ! Copy the state values into holders for the gradients.
+    A_GRADS(:,:,:) = A_STATES(:,:,:)
+    AY_GRAD(:,:) = AY(:,:)
+    M_GRADS(:,:,:) = M_STATES(:,:,:)
     ! Compute the gradient with respect to the model basis functions.
-    CALL BASIS_GRADIENT(CONFIG, MODEL, Y_GRADIENT, XXI, AXXI, &
-         SIZES, M_STATES, A_STATES, AY, MODEL_GRAD)
+    CALL BASIS_GRADIENT(CONFIG, MODEL, Y_GRADIENT, X, AX, &
+         SIZES, M_GRADS, A_GRADS, AY_GRAD, MODEL_GRAD)
     ! Convert the computed input gradients into average gradients for each embedding.
-    IF (SIZE(XI,1) .GT. 0) THEN
+    IF (CONFIG%MDE .GT. 0) THEN
        CALL EMBEDDING_GRADIENT(CONFIG%MDE, CONFIG%MNE, &
-            XI, XXI(CONFIG%ADO+SIZE(X,1)+1:,:), &
+            XI, X(CONFIG%MDI-CONFIG%ADO-CONFIG%MDE+1:CONFIG%MDI-CONFIG%ADO,:), &
             MODEL_GRAD(CONFIG%MSEV:CONFIG%MEEV))
     END IF
     ! Convert the computed input gradients into average gradients for each embedding.
-    IF (SIZE(AXI,1) .GT. 0) THEN
+    IF (CONFIG%ADE .GT. 0) THEN
        CALL EMBEDDING_GRADIENT(CONFIG%ADE, CONFIG%ANE, &
-            AXI, AXXI(SIZE(AX,1)+1:,:), &
+            AXI, AX(CONFIG%ADI-CONFIG%ADE+1:CONFIG%ADI,:), &
             MODEL_GRAD(CONFIG%ASEV:CONFIG%AEEV))
     END IF
-  END SUBROUTINE MODEL_GRADIENT
 
+  CONTAINS
+    ! Sum the output alignments for each internal state.
+    SUBROUTINE UNPACKED_COMPUTE_ALIGNMENT(MDS, MNS, MDO, &
+         STATE_VECS, OUTPUT_VECS, ALIGNMENT)
+      INTEGER, INTENT(IN) :: MDS, MNS, MDO
+      REAL(KIND=RT), INTENT(IN), DIMENSION(MDS,MDS,MNS-1) :: STATE_VECS
+      REAL(KIND=RT), INTENT(IN), DIMENSION(MDS,MDO) :: OUTPUT_VECS
+      REAL(KIND=RT), INTENT(OUT), DIMENSION(MDS,MNS) :: ALIGNMENT
+      INTEGER :: L
+      IF (MNS .GT. 0) THEN
+         DO L = 1, MNS-1
+            ALIGNMENT(:,L) = ALIGNMENT(:,L) + SUM(STATE_VECS(:,:,L), 2)
+         END DO
+         ALIGNMENT(:,MNS) = ALIGNMENT(:,MNS) + SUM(OUTPUT_VECS(:,:), 2)
+      END IF
+    END SUBROUTINE UNPACKED_COMPUTE_ALIGNMENT
 
-  ! Compute the sum of squared error, store the gradient in the OUTPUTS.
-  !   TARGETS - row vectors containing target values
-  !   OUTPUTS - column vectors containing model predictions
-  SUBROUTINE SQUARED_ERROR_GRADIENT(TARGETS, OUTPUTS)
-    REAL(KIND=RT), INTENT(IN),    DIMENSION(:,:) :: TARGETS
-    REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: OUTPUTS
-    INTEGER :: D
-    OUTPUTS(:,:) = OUTPUTS(:,:) - TARGETS(:,:)
-  END SUBROUTINE SQUARED_ERROR_GRADIENT
-
-
-  ! Produce the true values as the gradient (which will show large
-  !  magnitudes for parameters in the model that align with values).
-  SUBROUTINE TRUE_VALUE_GRADIENT(TARGETS, OUTPUTS)
-    REAL(KIND=RT), INTENT(IN),    DIMENSION(:,:) :: TARGETS
-    REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: OUTPUTS
-    INTEGER :: D
-    OUTPUTS(:,:) = TARGETS(:,:)
-  END SUBROUTINE TRUE_VALUE_GRADIENT
+  END SUBROUTINE MODEL_GRADIENT
 
 
   ! Fit input / output pairs by minimizing mean squared error.
-  SUBROUTINE MINIMIZE_MSE(CONFIG, MODEL, Y, X, XI, AX, AXI, SIZES, &
-       STEPS, SUM_SQUARED_ERROR, RECORD, INFO)
-    TYPE(MODEL_CONFIG), INTENT(IN) :: CONFIG
+  SUBROUTINE MINIMIZE_MSE(CONFIG, MODEL, RWORK, IWORK, &
+       AX, AXI, SIZES, X, XI, Y, &
+       STEPS, RECORD, SUM_SQUARED_ERROR, INFO)
+    TYPE(MODEL_CONFIG), INTENT(INOUT) :: CONFIG
     REAL(KIND=RT), INTENT(INOUT), DIMENSION(:) :: MODEL
-    REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: Y
-    REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: X
-    INTEGER,       INTENT(IN), DIMENSION(:,:) :: XI
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(:) :: RWORK
+    INTEGER,       INTENT(INOUT), DIMENSION(:) :: IWORK
     REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: AX
-    INTEGER,       INTENT(IN), DIMENSION(:,:) :: AXI
-    INTEGER,       INTENT(IN), DIMENSION(:) :: SIZES
+    INTEGER,       INTENT(IN),    DIMENSION(:,:) :: AXI
+    INTEGER,       INTENT(IN),    DIMENSION(:) :: SIZES
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: X
+    INTEGER,       INTENT(IN),    DIMENSION(:,:) :: XI
+    REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: Y
     INTEGER,       INTENT(IN) :: STEPS
+    REAL(KIND=RT), INTENT(OUT), DIMENSION(6,STEPS), OPTIONAL :: RECORD
     REAL(KIND=RT), INTENT(OUT) :: SUM_SQUARED_ERROR
-    REAL(KIND=RT), INTENT(OUT), DIMENSION(4,STEPS), OPTIONAL :: RECORD
     INTEGER,       INTENT(OUT) :: INFO
-    !  Local variables.
-    !    gradient step arrays, 4 copies of model + (num threads - 1)
-    REAL(KIND=RT), DIMENSION(CONFIG%NUM_VARS) :: &
-         MODEL_GRAD, MODEL_GRAD_MEAN, MODEL_GRAD_CURV, BEST_MODEL
-    REAL(KIND=RT), DIMENSION(CONFIG%MDI-CONFIG%MDE-CONFIG%ADO) :: X_SCALE
-    REAL(KIND=RT), DIMENSION(CONFIG%ADI-CONFIG%ADE) :: AX_SCALE
-    REAL(KIND=RT), DIMENSION(CONFIG%MDO) :: Y_SCALE
-    !    batch start and end indices for parallelization
-    INTEGER, DIMENSION(2,CONFIG%NUM_THREADS) :: BATCHA, BATCHM
+    ! Local variables.
+    !    measured gradient contribution of all input points
+    REAL(KIND=RT), DIMENSION(SIZE(AX,2)) :: AX_CONTRIB
+    REAL(KIND=RT), DIMENSION(SIZE(X,2)) :: X_CONTRIB
+    !    count of how many steps have been taken since last usage
+    INTEGER, DIMENSION(SIZE(AX,2)) :: AX_UNUSED_STEPS
+    INTEGER, DIMENSION(SIZE(X,2)) :: X_UNUSED_STEPS
+    !    indices (used for sorting and selecting points for gradient computation)
+    INTEGER, DIMENSION(SIZE(AX,2)) :: AX_INDICES
+    INTEGER, DIMENSION(SIZE(X,2)) :: X_INDICES
     !    "backspace" character array for printing to the same line repeatedly
     CHARACTER(LEN=*), PARAMETER :: RESET_LINE = REPEAT(CHAR(8),25)
-    !    singletons
-    LOGICAL :: REVERT_TO_BEST, DID_PRINT
-    INTEGER :: BN, I, NB, NS, NY, BATCH, SS, SE
-    INTEGER :: UPDATE_INDICES(CONFIG%NUM_VARS), NUM_TO_UPDATE
-    REAL(KIND=RT) :: RNY, BATCHES, PREV_MSE, MSE, BEST_MSE
-    REAL(KIND=RT) :: STEP_FACTOR, STEP_MEAN_CHANGE, STEP_MEAN_REMAIN, &
-         STEP_CURV_CHANGE, STEP_CURV_REMAIN
-    REAL :: LAST_PRINT_TIME, CURRENT_TIME, WAIT_TIME
-    ! Check for a valid data shape given the model.
-    INFO = 0
-    CALL CHECK_SHAPE(CONFIG, MODEL, Y, X, XI, AX, AXI, SIZES, INFO)
-    IF (INFO .NE. 0) RETURN
-    ! Number of points.
-    NY = SIZE(Y,2)
-    RNY = REAL(NY, RT)
-    ! Set the step factor.
-    STEP_FACTOR = CONFIG%INITIAL_STEP
-    ! Set the initial "number of steps taken since best" counter.
-    NS = 0
-    ! Set the batch N (BN) and num batches (NB).
-    NB = MIN(CONFIG%NUM_THREADS, NY)
-    BN = (NY + NB - 1) / NB
-    CALL COMPUTE_BATCHES(NB, X, AX, SIZES, BATCHA, BATCHM, INFO)
-    IF (INFO .NE. 0) THEN
-       Y(:,:) = 0.0_RT
-       RETURN
-    END IF
-    ! Only "revert" to the best model seen if some steps are taken.
-    REVERT_TO_BEST = CONFIG%KEEP_BEST .AND. (STEPS .GT. 0)
-    ! Store the start time of this routine (to make sure updates can
-    !    be shown to the user at a reasonable frequency).
-    CALL CPU_TIME(LAST_PRINT_TIME)
-    DID_PRINT = .FALSE.
-    WAIT_TIME = 2.0 * NB ! 2 seconds (times number of threads)
-    ! Set the initial number of variables to update at the whole model.
-    NUM_TO_UPDATE = CONFIG%NUM_VARS
-    ! Initial rates of change of mean and variance values.
-    STEP_MEAN_CHANGE = CONFIG%INITIAL_STEP_MEAN_CHANGE
-    STEP_MEAN_REMAIN = 1.0_RT - STEP_MEAN_CHANGE
-    STEP_CURV_CHANGE = CONFIG%INITIAL_STEP_CURV_CHANGE
-    STEP_CURV_REMAIN = 1.0_RT - STEP_CURV_CHANGE
-    ! Initial mean squared error is "max representable value".
-    PREV_MSE = HUGE(PREV_MSE)
-    BEST_MSE = HUGE(BEST_MSE)
-    ! Set the average step sizes.
-    MODEL_GRAD_MEAN(:) = 0.0_RT
-    ! Set the estiamted curvature in steps.
-    MODEL_GRAD_CURV(:) = 0.0_RT
-    ! Set the default size start and end indices for when it is absent.
-    IF (SIZE(SIZES) .EQ. 0) THEN
-       SS = 1
-       SE = -1
-    END IF
-    ! Set shift terms to center all inputs and outputs.
-    MODEL(CONFIG%MISS:CONFIG%MISE) = -SUM(X(:,:),2) / RNY
-    MODEL(CONFIG%AISS:CONFIG%AISE) = -SUM(AX(:,:),2) / RNY
-    MODEL(CONFIG%MOSS:CONFIG%MOSE) =  SUM(Y(:,:),2) / RNY
-    IF (SIZE(X,1) .GT. 0) THEN
-       DO I = 1, SIZE(X,2)
-          X(:,I) = X(:,I) + MODEL(CONFIG%MISS:CONFIG%MISE)
-       END DO
-    END IF
-    IF (SIZE(AX,1) .GT. 0) THEN
-       DO I = 1, SIZE(AX,2)
-          AX(:,I) = AX(:,I) + MODEL(CONFIG%AISS:CONFIG%AISE)
-       END DO
-    END IF
-    DO I = 1, SIZE(Y,2)
-       Y(:,I) = Y(:,I) - MODEL(CONFIG%MOSS:CONFIG%MOSE)
-    END DO
-    ! Make inputs and outputs componentwise unit deviation.
-    !   X
-    X_SCALE(:)  = NORM2(X(:,:),2) / SQRT(RNY)
-    WHERE ( X_SCALE(:) .LT. EPSILON(1.0_RT))  X_SCALE(:) = 1.0_RT
-    IF (SIZE(X,1) .GT. 0) THEN
-       DO I = 1, SIZE(X,2)
-          X(:,I) = X(:,I) / X_SCALE(:)
-       END DO
-    END IF
-    !   AX
-    AX_SCALE(:) = NORM2(AX(:,:),2)
-    IF (SIZE(AX,2) .GT. 0) AX_SCALE(:) = AX_SCALE(:) / SQRT(REAL(SIZE(AX,2),RT))
-    WHERE (AX_SCALE(:) .LT. EPSILON(1.0_RT)) AX_SCALE(:) = 1.0_RT
-    IF (SIZE(AX,1) .GT. 0) THEN
-       DO I = 1, SIZE(AX,2)
-          AX(:,I) = AX(:,I) / AX_SCALE(:)
-       END DO
-    END IF
-    !   Y
-    Y_SCALE(:)  = NORM2(Y(:,:),2) / SQRT(RNY)
-    WHERE ( Y_SCALE(:) .LT. EPSILON(1.0_RT))  Y_SCALE(:) = 1.0_RT
-    DO I = 1, SIZE(Y,2)
-       Y(:,I) = Y(:,I) / Y_SCALE(:)
-    END DO
-    ! Iterate, taking steps with the average gradient over all data.
-    fit_loop : DO I = 1, STEPS
-       ! Compute the average gradient over all points.
-       SUM_SQUARED_ERROR = 0.0_RT
-       ! Set gradients to zero initially.
-       MODEL_GRAD(:) = 0.0_RT
-       !$OMP PARALLEL DO NUM_THREADS(NB) PRIVATE(BATCH) FIRSTPRIVATE(SS, SE) &
-       !$OMP& REDUCTION(+: SUM_SQUARED_ERROR, MODEL_GRAD)
-       DO BATCH = 1, NB
-          ! Set the size start and end.
-          IF (CONFIG%ADI .GT. 0) THEN
-             SS = BATCHM(1,BATCH)
-             SE = BATCHM(2,BATCH)
-          END IF
-          ! Sum the gradient over all data batches.
-          CALL MODEL_GRADIENT(CONFIG, MODEL(:), &
-               Y(:,BATCHM(1,BATCH):BATCHM(2,BATCH)), &
-               X(:,BATCHM(1,BATCH):BATCHM(2,BATCH)), &
-               XI(:,BATCHM(1,BATCH):BATCHM(2,BATCH)), &
-               AX(:,BATCHA(1,BATCH):BATCHA(2,BATCH)), &
-               AXI(:,BATCHA(1,BATCH):BATCHA(2,BATCH)), &
-               SIZES(SS:SE), SUM_SQUARED_ERROR, MODEL_GRAD(:), &
-               SQUARED_ERROR_GRADIENT, INFO, SHIFT=.FALSE., THREADS=1)
-       END DO
-       !$OMP END PARALLEL DO
-       IF (INFO .NE. 0) RETURN
-       ! Convert the sum of squared errors into the mean squared error.
-       MSE = SUM_SQUARED_ERROR / REAL(SIZE(Y),RT) ! RNY * SIZE(Y,1)
-       ! Update the step factor based on model improvement.
-       IF (MSE .LE. PREV_MSE) THEN
-          STEP_FACTOR = STEP_FACTOR * CONFIG%FASTER_RATE
-          STEP_MEAN_CHANGE = STEP_MEAN_CHANGE * CONFIG%SLOWER_RATE
-          STEP_MEAN_REMAIN = 1.0_RT - STEP_MEAN_CHANGE
-          STEP_CURV_CHANGE = STEP_CURV_CHANGE * CONFIG%SLOWER_RATE
-          STEP_CURV_REMAIN = 1.0_RT - STEP_CURV_CHANGE
-          NUM_TO_UPDATE = MIN(CONFIG%NUM_VARS, &
-               NUM_TO_UPDATE + (CONFIG%NUM_VARS - NUM_TO_UPDATE) / 2)
-       ELSE
-          STEP_FACTOR = STEP_FACTOR * CONFIG%SLOWER_RATE
-          STEP_MEAN_CHANGE = STEP_MEAN_CHANGE * CONFIG%FASTER_RATE
-          STEP_MEAN_REMAIN = 1.0_RT - STEP_MEAN_CHANGE
-          STEP_CURV_CHANGE = STEP_CURV_CHANGE * CONFIG%FASTER_RATE
-          STEP_CURV_REMAIN = 1.0_RT - STEP_CURV_CHANGE
-          NUM_TO_UPDATE = MAX(1, NUM_TO_UPDATE / 2)
-       END IF
-       ! Store the previous error for tracking the best-so-far.
-       PREV_MSE = MSE
+    !    temporary holders for overwritten CONFIG attributes
+    LOGICAL :: APPLY_SHIFT
+    INTEGER :: NUM_THREADS
+    !    miscellaneous (hard to concisely categorize)
+    LOGICAL :: DID_PRINT
+    INTEGER :: STEP, BATCH, NB, NS, SS, SE, MIN_TO_UPDATE, D, VS, VE
+    INTEGER :: TOTAL_RANK, TOTAL_EVAL_RANK, TOTAL_GRAD_RANK
+    INTEGER(KIND=INT64) :: CURRENT_TIME, CLOCK_RATE, CLOCK_MAX, LAST_PRINT_TIME, WAIT_TIME
+    REAL(KIND=RT) :: MSE, PREV_MSE, BEST_MSE
+    REAL(KIND=RT) :: STEP_MEAN_REMAIN, STEP_CURV_REMAIN
+
+    ! Unpack all of the work storage into the expected shapes.
+    CALL UNPACKED_MINIZE_MSE(&
+         RWORK(CONFIG%SMG : CONFIG%EMG), & ! MODEL_GRAD(NUM_VARS)
+         RWORK(CONFIG%SMGM : CONFIG%EMGM), & ! MODEL_GRAD_MEAN(NUM_VARS)
+         RWORK(CONFIG%SMGC : CONFIG%EMGC), & ! MODEL_GRAD_CURV(NUM_VARS)
+         RWORK(CONFIG%SBM : CONFIG%EBM), & ! BEST_MODEL(NUM_VARS)
+         RWORK(CONFIG%SMA : CONFIG%EMA), & ! M_ALIGN(MDS,MNS)
+         RWORK(CONFIG%SAA : CONFIG%EAA), & ! A_ALIGN(ADS,ANS)
+         RWORK(CONFIG%SYG : CONFIG%EYG), & ! Y_GRADIENT(MDO,NM)
+         RWORK(CONFIG%SMXS : CONFIG%EMXS), & ! M_STATES(NM,MDS,MNS+1)
+         RWORK(CONFIG%SMXG : CONFIG%EMXG), & ! M_GRADS(NM,MDS,MNS+1)
+         RWORK(CONFIG%SAXS : CONFIG%EAXS), & ! A_STATES(NA,ADS,ANS+1)
+         RWORK(CONFIG%SAXG : CONFIG%EAXG), & ! A_GRADS(NA,ADS,ANS+1)
+         RWORK(CONFIG%SAY : CONFIG%EAY), & ! AY(NA,ADO)
+         RWORK(CONFIG%SAYG : CONFIG%EAYG), & ! AY_GRAD(NA,ADO)
+         RWORK(CONFIG%SMXR : CONFIG%EMXR), & ! X_RESCALE(MDN,MDN)
+         RWORK(CONFIG%SMXIS : CONFIG%EMXIS), & ! XI_SHIFT(MDE)
+         RWORK(CONFIG%SMXIR : CONFIG%EMXIR), & ! XI_RESCALE(MDE,MDE)
+         RWORK(CONFIG%SAXR : CONFIG%EAXR), & ! AX_RESCALE(ADN,ADN)
+         RWORK(CONFIG%SAXIS : CONFIG%EAXIS), & ! AXI_SHIFT(ADE)
+         RWORK(CONFIG%SAXIR : CONFIG%EAXIR), & ! AXI_RESCALE(ADE,ADE)
+         RWORK(CONFIG%SAYR : CONFIG%EAYR), & ! AY_RESCALE(ADO)
+         RWORK(CONFIG%SYR : CONFIG%EYR), & ! Y_RESCALE(MDO,MDO)
+         RWORK(CONFIG%SFMA : CONFIG%EFMA), & ! MODEL_ALIGN(NUM_VARS,NUM_THREADS)
+         RWORK(CONFIG%SXT : CONFIG%EXT), & ! X_TEMP(MDE+ADO,NM,NUM_THREADS)
+         MODEL(CONFIG%ASIV : CONFIG%AEIV), & ! APOSITIONAL_INPUT_VECS
+         MODEL(CONFIG%MSIV : CONFIG%MEIV), & ! MODEL_INPUT_VECS
+         MODEL(CONFIG%ASOV : CONFIG%AEOV), & ! APOSITIONAL_OUTPUT_VECS
+         MODEL(CONFIG%MSOV : CONFIG%MEOV), & ! APOSITIONAL_OUTPUT_VECS
+         IWORK(CONFIG%SUI : CONFIG%EUI), & ! UPDATE_INDICES(NUM_VARS)
+         IWORK(CONFIG%SBAS : CONFIG%EBAS), & ! BATCHA_STARTS(NUM_THREADS)
+         IWORK(CONFIG%SBAE : CONFIG%EBAE), & ! BATCHA_ENDS(NUM_THREADS)
+         IWORK(CONFIG%SBMS : CONFIG%EBMS), & ! BATCHM_STARTS(NUM_THREADS)
+         IWORK(CONFIG%SBME : CONFIG%EBME)) ! BATCHM_ENDS(NUM_THREADS)
 
-       ! Record that a step was taken.
-       NS = NS + 1
-       ! Update the saved "best" model based on error.
-       IF (MSE .LT. BEST_MSE) THEN
-          NS = 0
-          BEST_MSE = MSE
-          IF (REVERT_TO_BEST) THEN
-             BEST_MODEL(:) = MODEL(1:CONFIG%NUM_VARS)
-          END IF
-       ! Early stop if we don't expect to see a better solution
-       !  by the time the fit operation is complete.
-       ELSE IF (CONFIG%EARLY_STOP .AND. (NS .GT. STEPS - I)) THEN
-          EXIT fit_loop
-       END IF
+  CONTAINS
 
-       ! Convert the summed gradients to average gradients.
-       MODEL_GRAD(:) = MODEL_GRAD(:) / REAL(NB,RT)
-       MODEL_GRAD_MEAN(:) = STEP_MEAN_REMAIN * MODEL_GRAD_MEAN(:) &
-            + STEP_MEAN_CHANGE * MODEL_GRAD(:)
-       MODEL_GRAD_CURV(:) = STEP_CURV_REMAIN * MODEL_GRAD_CURV(:) &
-            + STEP_CURV_CHANGE * (MODEL_GRAD_MEAN(:) - MODEL_GRAD(:))**2
-       MODEL_GRAD_CURV(:) = MAX(MODEL_GRAD_CURV(:), EPSILON(STEP_FACTOR))
-       ! Set the step as the mean direction (over the past few steps).
-       MODEL_GRAD(:) = MODEL_GRAD_MEAN(:)
-       ! Start scaling by step magnitude by curvature once enough data is collected.
-       IF (I .GE. CONFIG%MIN_STEPS_TO_STABILITY) THEN
-          MODEL_GRAD(:) = MODEL_GRAD(:) / SQRT(MODEL_GRAD_CURV(:))
-       END IF
-       ! Update as many parameters as it seems safe to update (and still converge).
-       IF (NUM_TO_UPDATE .LT. CONFIG%NUM_VARS) THEN
-          ! Identify the subset of components that will be updapted this step.
-          CALL ARGSELECT(-ABS(MODEL_GRAD(:)), NUM_TO_UPDATE, UPDATE_INDICES(:))
-          ! Take the gradient steps (based on the computed "step" above).
-          MODEL(UPDATE_INDICES(1:NUM_TO_UPDATE)) = MODEL(UPDATE_INDICES(1:NUM_TO_UPDATE)) &
-               - MODEL_GRAD(UPDATE_INDICES(1:NUM_TO_UPDATE)) * STEP_FACTOR
-       ELSE
-          ! Take the gradient steps (based on the computed "step" above).
-          MODEL(1:CONFIG%NUM_VARS) = MODEL(1:CONFIG%NUM_VARS) - MODEL_GRAD(:) * STEP_FACTOR
-       END IF
+    ! Unpack the work arrays into the proper shapes.
+    SUBROUTINE UNPACKED_MINIZE_MSE(&
+         MODEL_GRAD, MODEL_GRAD_MEAN, MODEL_GRAD_CURV, BEST_MODEL, &
+         M_ALIGN, A_ALIGN, Y_GRADIENT, M_STATES, M_GRADS, A_STATES, A_GRADS, &
+         AY, AY_GRAD, X_RESCALE, XI_SHIFT, XI_RESCALE, &
+         AX_RESCALE, AXI_SHIFT, AXI_RESCALE, AY_RESCALE, &
+         Y_RESCALE, MODEL_ALIGN, X_TEMP, &
+         A_IN_VECS, M_IN_VECS, A_OUT_VECS, M_OUT_VECS, &
+         UPDATE_INDICES, BATCHA_STARTS, BATCHA_ENDS, BATCHM_STARTS, BATCHM_ENDS)
+      ! Definition of unpacked work storage.
+      REAL(KIND=RT), DIMENSION(CONFIG%NUM_VARS) :: &
+           MODEL_GRAD, MODEL_GRAD_MEAN, MODEL_GRAD_CURV, BEST_MODEL
+      REAL(KIND=RT), DIMENSION(CONFIG%NA, CONFIG%ADS, CONFIG%ANS+1) :: A_STATES, A_GRADS
+      REAL(KIND=RT), DIMENSION(CONFIG%NM, CONFIG%MDS, CONFIG%MNS+1) :: M_STATES, M_GRADS
+      REAL(KIND=RT), DIMENSION(CONFIG%ADS, CONFIG%ANS) :: A_ALIGN
+      REAL(KIND=RT), DIMENSION(CONFIG%NA, CONFIG%ADO) :: AY, AY_GRAD
+      REAL(KIND=RT), DIMENSION(CONFIG%MDS, CONFIG%MNS) :: M_ALIGN
+      REAL(KIND=RT), DIMENSION(CONFIG%MDO, CONFIG%NM) :: Y_GRADIENT
+      REAL(KIND=RT), DIMENSION(CONFIG%ADN, CONFIG%ADN) :: AX_RESCALE
+      REAL(KIND=RT), DIMENSION(CONFIG%ADE) :: AXI_SHIFT
+      REAL(KIND=RT), DIMENSION(CONFIG%ADE, CONFIG%ADE) :: AXI_RESCALE
+      REAL(KIND=RT), DIMENSION(CONFIG%ADO) :: AY_RESCALE
+      REAL(KIND=RT), DIMENSION(CONFIG%MDN, CONFIG%MDN) :: X_RESCALE
+      REAL(KIND=RT), DIMENSION(CONFIG%MDE) :: XI_SHIFT
+      REAL(KIND=RT), DIMENSION(CONFIG%MDE, CONFIG%MDE) :: XI_RESCALE
+      REAL(KIND=RT), DIMENSION(CONFIG%MDO, CONFIG%MDO) :: Y_RESCALE
+      REAL(KIND=RT), DIMENSION(CONFIG%NUM_VARS, CONFIG%NUM_THREADS) :: MODEL_ALIGN
+      REAL(KIND=RT), DIMENSION(CONFIG%MDE+CONFIG%ADO, CONFIG%NM, CONFIG%NUM_THREADS) :: X_TEMP
+      REAL(KIND=RT), DIMENSION(CONFIG%ADI, CONFIG%ADS) :: A_IN_VECS
+      REAL(KIND=RT), DIMENSION(CONFIG%MDI, CONFIG%MDS) :: M_IN_VECS
+      REAL(KIND=RT), DIMENSION(CONFIG%ADS, CONFIG%ADO) :: A_OUT_VECS
+      REAL(KIND=RT), DIMENSION(CONFIG%MDS, CONFIG%MDO) :: M_OUT_VECS
+      INTEGER, DIMENSION(CONFIG%NUM_VARS) :: UPDATE_INDICES
+      INTEGER, DIMENSION(CONFIG%NUM_THREADS) :: &
+           BATCHA_STARTS, BATCHA_ENDS, BATCHM_STARTS, BATCHM_ENDS
+      ! Check for a valid data shape given the model.
+      INFO = 0
+      ! Check the shape of all inputs (to make sure they match this model).
+      CALL CHECK_SHAPE(CONFIG, MODEL, AX, AXI, SIZES, X, XI, Y, INFO)
+      ! Do shape checks on the work space provided.
+      IF (SIZE(RWORK) .LT. CONFIG%RWORK_SIZE) THEN
+         INFO = 12
+      ELSE IF (SIZE(IWORK) .LT. CONFIG%IWORK_SIZE) THEN
+         INFO = 13
+      ELSE IF ((CONFIG%ADI .GT. 0) .AND. (CONFIG%NA .LT. 1)) THEN
+         INFO = 14
+      ELSE IF ((CONFIG%MDI .GT. 0) .AND. (CONFIG%NM .LT. 1)) THEN
+         INFO = 15
+      END IF
+      IF (INFO .NE. 0) RETURN
+      ! 
+      ! ----------------------------------------------------------------
+      !                 Initialization and preparation
+      ! 
+      ! Set the "total rank", the number of internal state components.
+      TOTAL_RANK = CONFIG%MDS*CONFIG%MNS + CONFIG%ADS*CONFIG%ANS
+      ! Compute the minimum number of model parameters to update.
+      MIN_TO_UPDATE = MAX(1,INT(CONFIG%MIN_UPDATE_RATIO * REAL(CONFIG%NUM_VARS,RT)))
+      ! Set the initial "number of steps taken since best" counter.
+      NS = 0
+      ! Set the num batches (NB).
+      NB = MIN(CONFIG%NUM_THREADS, SIZE(Y,2))
+      CALL COMPUTE_BATCHES(NB, SIZE(X,2), SIZE(AX,2), SIZES, &
+           BATCHA_STARTS, BATCHA_ENDS, BATCHM_STARTS, BATCHM_ENDS, INFO)
+      IF (INFO .NE. 0) THEN
+         Y(:,:) = 0.0_RT
+         RETURN
+      END IF
+      ! Store the start time of this routine (to make sure updates can
+      !  be shown to the user at a reasonable frequency).
+      CALL SYSTEM_CLOCK(LAST_PRINT_TIME, CLOCK_RATE, CLOCK_MAX)
+      WAIT_TIME = CLOCK_RATE * CONFIG%PRINT_DELAY_SEC
+      DID_PRINT = .FALSE.
+      ! Initial rates of change of mean and variance values.
+      STEP_MEAN_REMAIN = 1.0_RT - CONFIG%STEP_MEAN_CHANGE
+      STEP_CURV_REMAIN = 1.0_RT - CONFIG%STEP_CURV_CHANGE
+      ! Initial mean squared error is "max representable value".
+      PREV_MSE = HUGE(PREV_MSE)
+      BEST_MSE = HUGE(BEST_MSE)
+      ! Set the default size start and end indices for when it is absent.
+      IF (SIZE(SIZES) .EQ. 0) THEN
+         SS = 1
+         SE = -1
+      END IF
+      ! Disable the application of SHIFT (since data is / will be normalized).
+      APPLY_SHIFT = CONFIG%APPLY_SHIFT
+      CONFIG%APPLY_SHIFT = .FALSE.
+      ! Normalize the data.
+      CALL NORMALIZE_DATA(CONFIG, MODEL, AX, AXI, AY, SIZES, X, XI, Y, &
+           AX_RESCALE, AXI_SHIFT, AXI_RESCALE, AY_RESCALE, X_RESCALE, &
+           XI_SHIFT, XI_RESCALE, Y_RESCALE, A_STATES, &
+           MODEL(CONFIG%MSEV:CONFIG%MEEV), &
+           MODEL(CONFIG%ASEV:CONFIG%AEEV), &
+           MODEL(CONFIG%ASOV:CONFIG%AEOV))
+      ! Set the number of threads to 1 to prevent nested parallelization.
+      NUM_THREADS = CONFIG%NUM_THREADS
+      CONFIG%NUM_THREADS = 1
+      ! 
+      ! ----------------------------------------------------------------
+      !                    Minimizing mean squared error
+      ! 
+      ! Iterate, taking steps with the average gradient over all data.
+      fit_loop : DO STEP = 1, STEPS
+         ! 
+         ! - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
+         !                       Compute model gradient 
+         ! 
+         ! Compute the average gradient over all points.
+         SUM_SQUARED_ERROR = 0.0_RT
+         ! Set gradients to zero initially.
+         MODEL_GRAD(:) = 0.0_RT
+         M_ALIGN(:,:) = 0.0_RT
+         A_ALIGN(:,:) = 0.0_RT
+         !$OMP PARALLEL DO NUM_THREADS(NB) PRIVATE(BATCH) FIRSTPRIVATE(SS, SE) &
+         !$OMP& REDUCTION(+: SUM_SQUARED_ERROR, MODEL_GRAD, M_ALIGN, A_ALIGN)
+         DO BATCH = 1, NB
+            ! Set the size start and end.
+            IF (CONFIG%ADI .GT. 0) THEN
+               SS = BATCHM_STARTS(BATCH)
+               SE = BATCHM_ENDS(BATCH)
+            END IF
+            ! Sum the gradient over all data batches.
+            CALL MODEL_GRADIENT(CONFIG, MODEL(:), &
+                 AX(:,BATCHA_STARTS(BATCH):BATCHA_ENDS(BATCH)), &
+                 AXI(:,BATCHA_STARTS(BATCH):BATCHA_ENDS(BATCH)), &
+                 AY(BATCHA_STARTS(BATCH):BATCHA_ENDS(BATCH),:), &
+                 SIZES(SS:SE), &
+                 X(:,BATCHM_STARTS(BATCH):BATCHM_ENDS(BATCH)), &
+                 XI(:,BATCHM_STARTS(BATCH):BATCHM_ENDS(BATCH)), &
+                 Y(:,BATCHM_STARTS(BATCH):BATCHM_ENDS(BATCH)), &
+                 SUM_SQUARED_ERROR, MODEL_GRAD(:), &
+                 A_ALIGN(:,:), M_ALIGN(:,:), &
+                 MODEL_ALIGN(:,BATCH), &
+                 X_TEMP(:,:,BATCH), &
+                 AY_GRAD(BATCHA_STARTS(BATCH):BATCHA_ENDS(BATCH),:), &
+                 Y_GRADIENT(:,BATCHM_STARTS(BATCH):BATCHM_ENDS(BATCH)), &
+                 A_STATES(BATCHA_STARTS(BATCH):BATCHA_ENDS(BATCH),:,:), &
+                 A_GRADS(BATCHA_STARTS(BATCH):BATCHA_ENDS(BATCH),:,:), &
+                 M_STATES(BATCHM_STARTS(BATCH):BATCHM_ENDS(BATCH),:,:), &
+                 M_GRADS(BATCHM_STARTS(BATCH):BATCHM_ENDS(BATCH),:,:), &
+                 INFO)
+         END DO
+         !$OMP END PARALLEL DO
+         IF (INFO .NE. 0) RETURN
+         ! 
+         ! - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
+         !           Update the step factors, early stop if appropaite.
+         ! 
+         ! Convert the sum of squared errors into the mean squared error.
+         MSE = SUM_SQUARED_ERROR / REAL(SIZE(Y),RT) ! RNY * SIZE(Y,1)
+         ! Adjust exponential sliding windows based on change in error.
+         IF (MSE .LE. PREV_MSE) THEN
+            CONFIG%STEP_FACTOR = CONFIG%STEP_FACTOR * CONFIG%FASTER_RATE
+            CONFIG%STEP_MEAN_CHANGE = CONFIG%STEP_MEAN_CHANGE * CONFIG%SLOWER_RATE
+            STEP_MEAN_REMAIN = 1.0_RT - CONFIG%STEP_MEAN_CHANGE
+            CONFIG%STEP_CURV_CHANGE = CONFIG%STEP_CURV_CHANGE * CONFIG%SLOWER_RATE
+            STEP_CURV_REMAIN = 1.0_RT - CONFIG%STEP_CURV_CHANGE
+            CONFIG%NUM_TO_UPDATE = CONFIG%NUM_TO_UPDATE + INT(0.05_RT * REAL(CONFIG%NUM_VARS,RT))
+         ELSE
+            CONFIG%STEP_FACTOR = CONFIG%STEP_FACTOR * CONFIG%SLOWER_RATE
+            CONFIG%STEP_MEAN_CHANGE = CONFIG%STEP_MEAN_CHANGE * CONFIG%FASTER_RATE
+            STEP_MEAN_REMAIN = 1.0_RT - CONFIG%STEP_MEAN_CHANGE
+            CONFIG%STEP_CURV_CHANGE = CONFIG%STEP_CURV_CHANGE * CONFIG%FASTER_RATE
+            STEP_CURV_REMAIN = 1.0_RT - CONFIG%STEP_CURV_CHANGE
+            CONFIG%NUM_TO_UPDATE = CONFIG%NUM_TO_UPDATE - INT(0.05_RT * REAL(CONFIG%NUM_VARS,RT))
+         END IF
+         ! Project the number of variables to update into allowable bounds.
+         CONFIG%NUM_TO_UPDATE = MIN(CONFIG%NUM_VARS, MAX(MIN_TO_UPDATE, CONFIG%NUM_TO_UPDATE))
+         ! Store the previous error for tracking the best-so-far.
+         PREV_MSE = MSE
+         ! Record that a step was taken.
+         NS = NS + 1
+         ! Update the saved "best" model based on error.
+         IF (MSE .LT. BEST_MSE) THEN
+            NS = 0
+            BEST_MSE = MSE
+            IF (CONFIG%KEEP_BEST) THEN
+               BEST_MODEL(:) = MODEL(1:CONFIG%NUM_VARS)
+            END IF
+            ! Early stop if we don't expect to see a better solution
+            !  by the time the fit operation is complete.
+         ELSE IF (CONFIG%EARLY_STOP .AND. (NS .GT. STEPS - STEP)) THEN
+            EXIT fit_loop
+         END IF
 
-       ! Record the 2-norm of the step that was taken (the GRAD variables were updated).
-       IF (PRESENT(RECORD)) THEN
-          ! Store the mean squared error at this iteration.
-          RECORD(1,I) = MSE
-          ! Store the current multiplier on the step.
-          RECORD(2,I) = STEP_FACTOR
-          ! Store the norm of the step that was taken.
-          RECORD(3,I) = SQRT(MAX(EPSILON(0.0_RT), SUM(MODEL_GRAD(:)**2)))
-          ! Store the percentage of parameters updated in this step.
-          RECORD(4,I) = REAL(NUM_TO_UPDATE,RT) / REAL(CONFIG%NUM_VARS)
-       END IF
+         ! - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
+         !              Modify the model parameters (take step).
+         ! 
+         ! Convert the summed gradients to average gradients.
+         MODEL_GRAD(:) = MODEL_GRAD(:) / REAL(NB,RT)
+         MODEL_GRAD_MEAN(:) = STEP_MEAN_REMAIN * MODEL_GRAD_MEAN(:) &
+              + CONFIG%STEP_MEAN_CHANGE * MODEL_GRAD(:)
+         MODEL_GRAD_CURV(:) = STEP_CURV_REMAIN * MODEL_GRAD_CURV(:) &
+              + CONFIG%STEP_CURV_CHANGE * (MODEL_GRAD_MEAN(:) - MODEL_GRAD(:))**2
+         MODEL_GRAD_CURV(:) = MAX(MODEL_GRAD_CURV(:), EPSILON(CONFIG%STEP_FACTOR))
+         ! Set the step as the mean direction (over the past few steps).
+         MODEL_GRAD(:) = MODEL_GRAD_MEAN(:)
+         ! Start scaling by step magnitude by curvature once enough data is collected.
+         IF (STEP .GE. CONFIG%MIN_STEPS_TO_STABILITY) THEN
+            MODEL_GRAD(:) = MODEL_GRAD(:) / SQRT(MODEL_GRAD_CURV(:))
+         END IF
+         ! Update as many parameters as it seems safe to update (and still converge).
+         IF (CONFIG%NUM_TO_UPDATE .LT. CONFIG%NUM_VARS) THEN
+            ! Identify the subset of components that will be updapted this step.
+            CALL ARGSELECT(-ABS(MODEL_GRAD(:)), &
+                 CONFIG%NUM_TO_UPDATE, UPDATE_INDICES(:))
+            ! Take the gradient steps (based on the computed "step" above).
+            MODEL(UPDATE_INDICES(1:CONFIG%NUM_TO_UPDATE)) = &
+                 MODEL(UPDATE_INDICES(1:CONFIG%NUM_TO_UPDATE)) &
+                 - MODEL_GRAD(UPDATE_INDICES(1:CONFIG%NUM_TO_UPDATE)) &
+                 * CONFIG%STEP_FACTOR
+         ELSE
+            ! Take the gradient steps (based on the computed "step" above).
+            MODEL(1:CONFIG%NUM_VARS) = MODEL(1:CONFIG%NUM_VARS) &
+                 - MODEL_GRAD(:) * CONFIG%STEP_FACTOR
+         END IF
+         CONFIG%STEPS_TAKEN = CONFIG%STEPS_TAKEN + 1
+         ! - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
+         ! Rescale internal vectors to have a maximum 2-norm of 1.
+         ! Center the outputs of the apositional model about the origin.
+         ! (for I = 1, rescale last layer of apositional model to unit variance)
+         CALL CONDITION_MODEL(CONFIG, CONFIG%STEPS_TAKEN, &
+              M_STATES(:,:,:), A_STATES(:,:,:), M_GRADS(:,:,:), A_GRADS(:,:,:), &
+              AY(:,:))
+         ! - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
+         ! Record various statistics that are currently of interest (for research).
+         IF (PRESENT(RECORD)) THEN
+            ! Store the mean squared error at this iteration.
+            RECORD(1,STEP) = MSE
+            ! Store the current multiplier on the step.
+            RECORD(2,STEP) = CONFIG%STEP_FACTOR
+            ! Store the norm of the step that was taken (intermittently).
+            IF (MOD(CONFIG%STEPS_TAKEN-1,CONFIG%LOGGING_STEP_FREQUENCY) .EQ. 0) THEN
+               RECORD(3,STEP) = SQRT(MAX(EPSILON(0.0_RT), SUM(MODEL_GRAD(:)**2))) / SQRT(REAL(CONFIG%NUM_VARS,RT))
+            ELSE
+               RECORD(3,STEP) = RECORD(3,STEP-1)
+            END IF
+            ! Store the percentage of parameters updated in this step.
+            RECORD(4,STEP) = REAL(CONFIG%NUM_TO_UPDATE,RT) / REAL(CONFIG%NUM_VARS)
+            ! Store the evaluative utilization rate (total data rank over full rank)
+            RECORD(5,STEP) = REAL(TOTAL_EVAL_RANK,RT) / REAL(TOTAL_RANK,RT)
+            ! Store the gradient utilization rate (total gradient rank over full rank)
+            RECORD(6,STEP) = REAL(TOTAL_GRAD_RANK,RT) / REAL(CONFIG%MDS*CONFIG%MNS + CONFIG%ADS*CONFIG%ANS,RT)
+         END IF
+         ! - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
+         ! Write an update about step and convergence to the command line.
+         CALL SYSTEM_CLOCK(CURRENT_TIME, CLOCK_RATE, CLOCK_MAX)
+         IF (CURRENT_TIME - LAST_PRINT_TIME .GT. WAIT_TIME) THEN
+            IF (DID_PRINT) WRITE (*,'(A)',ADVANCE='NO') RESET_LINE
+            WRITE (*,'(I6,"  (",F6.3,") [",F6.3,"]")', ADVANCE='NO') STEP, MSE, BEST_MSE
+            LAST_PRINT_TIME = CURRENT_TIME
+            DID_PRINT = .TRUE.
+         END IF
+      END DO fit_loop
+      ! 
+      ! ----------------------------------------------------------------
+      !                 Finalization, prepare for return.
+      ! 
+      ! Restore the best model seen so far (if enough steps were taken).
+      IF (CONFIG%KEEP_BEST .AND. (STEPS .GT. 0)) THEN
+         MSE                      = BEST_MSE
+         MODEL(1:CONFIG%NUM_VARS) = BEST_MODEL(:)
+      END IF
+      ! 
+      ! Apply the data normalizing scaling factors to the weight
+      !  matrices to embed normalization into the model.
+      IF (CONFIG%ENCODE_NORMALIZATION) THEN
+         IF (CONFIG%ADN .GT. 0) &
+              CALL SCALE_BASIS(A_IN_VECS(:CONFIG%ADN,:), AX_RESCALE(:,:))
+         IF (CONFIG%MDN .GT. 0) &
+              CALL SCALE_BASIS(M_IN_VECS(:CONFIG%MDN,:), X_RESCALE(:,:))
+         CALL SCALE_BASIS(M_OUT_VECS(:,:), Y_RESCALE(:,:))
+      END IF
+      ! 
+      ! Erase the printed message if one was produced.
+      IF (DID_PRINT) WRITE (*,'(A)',ADVANCE='NO') RESET_LINE
+      ! 
+      ! Reset configuration settings that were modified.
+      CONFIG%APPLY_SHIFT = APPLY_SHIFT
+      CONFIG%NUM_THREADS = NUM_THREADS
+    END SUBROUTINE UNPACKED_MINIZE_MSE
 
-       ! TODO: Replace with a more general "condition_model" routine that takes
-       !       the values and gradients for a model, then updates and replaces
-       !       bad basis functions, as well as normalizing them all.
-       !       Must orthogonalize outputs of basis functions when ranking,
-       !       ensure that highly redundant functions are removed in favor
-       !       of single (more information-unique) basis functions.
-       !       Use the expected decrease in loss (gradient * step) to
-       !       determine when a replacement can be made.
-       ! 
-       ! Maintain a constant max-norm across the magnitue of input and internal vectors.
-       CALL UNIT_MAX_NORM(CONFIG%MDI, CONFIG%MDS, CONFIG%MNS, &
-            MODEL(CONFIG%MSIV:CONFIG%MEIV), &
-            MODEL(CONFIG%MSSV:CONFIG%MESV))
-       IF (CONFIG%ADI .GT. 0) THEN
-          CALL UNIT_MAX_NORM(CONFIG%ADI, CONFIG%ADS, CONFIG%ANS, &
-               MODEL(CONFIG%ASIV:CONFIG%AEIV), &
-               MODEL(CONFIG%ASSV:CONFIG%AESV))
-       END IF
 
-       ! Write an update about step and convergence to the command line.
-       CALL CPU_TIME(CURRENT_TIME)
-       IF (CURRENT_TIME - LAST_PRINT_TIME .GT. WAIT_TIME) THEN
-          IF (DID_PRINT) WRITE (*,'(A)',ADVANCE='NO') RESET_LINE
-          WRITE (*,'(I6,"  (",F6.3,") [",F6.3,"]")', ADVANCE='NO') I, MSE, BEST_MSE
-          LAST_PRINT_TIME = CURRENT_TIME
-          DID_PRINT = .TRUE.
-       END IF
+    ! Make inputs and outputs radially symmetric (to make initialization
+    !  more well spaced and lower the curvature of the error gradient).
+    ! 
+    SUBROUTINE NORMALIZE_DATA(CONFIG, MODEL, AX, AXI, AY, SIZES, X, XI, Y, &
+         AX_RESCALE, AXI_SHIFT, AXI_RESCALE, AY_RESCALE, X_RESCALE, &
+         XI_SHIFT, XI_RESCALE, Y_RESCALE, &
+         A_STATES, A_EMB_VECS, M_EMB_VECS, A_OUT_VECS)
+      TYPE(MODEL_CONFIG), INTENT(INOUT) :: CONFIG
+      REAL(KIND=RT), INTENT(INOUT), DIMENSION(:) :: MODEL
+      REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: AX
+      INTEGER,       INTENT(IN),    DIMENSION(:,:) :: AXI
+      REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: AY
+      INTEGER,       INTENT(IN),    DIMENSION(:) :: SIZES
+      REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: X
+      INTEGER,       INTENT(IN),    DIMENSION(:,:) :: XI
+      REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: Y
+      REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: AX_RESCALE
+      REAL(KIND=RT), INTENT(INOUT), DIMENSION(:) :: AXI_SHIFT
+      REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: AXI_RESCALE
+      REAL(KIND=RT), INTENT(INOUT), DIMENSION(:) :: AY_RESCALE
+      REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: X_RESCALE
+      REAL(KIND=RT), INTENT(INOUT), DIMENSION(:) :: XI_SHIFT
+      REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: XI_RESCALE
+      REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: Y_RESCALE
+      REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:,:) :: A_STATES
+      REAL(KIND=RT), INTENT(INOUT), DIMENSION(CONFIG%ADE,CONFIG%ADE) :: A_EMB_VECS
+      REAL(KIND=RT), INTENT(INOUT), DIMENSION(CONFIG%MDE,CONFIG%MNE) :: M_EMB_VECS
+      REAL(KIND=RT), INTENT(INOUT), DIMENSION(CONFIG%ADS,CONFIG%ADO) :: A_OUT_VECS
+      INTEGER :: D
+      ! Encode embeddings if the are provided.
+      IF ((CONFIG%MDE + CONFIG%ADE .GT. 0) .AND. (&
+           (.NOT. CONFIG%XI_NORMALIZED) .OR. (.NOT. CONFIG%AXI_NORMALIZED))) THEN
+         CALL EMBED(CONFIG, MODEL, AXI, XI, AX, X)
+      END IF
+      ! 
+      !$OMP PARALLEL NUM_THREADS(5)
+      !$OMP SECTIONS PRIVATE(D)
+      !$OMP SECTION
+      IF ((.NOT. CONFIG%X_NORMALIZED) .AND. (CONFIG%MDN .GT. 0)) THEN
+         CALL RADIALIZE(X(:CONFIG%MDN,:), MODEL(CONFIG%MISS:CONFIG%MISE), X_RESCALE(:,:))
+         CONFIG%X_NORMALIZED = .TRUE.
+      ELSE IF (CONFIG%MDN .GT. 0) THEN
+         MODEL(CONFIG%MISS:CONFIG%MISE) = 0.0_RT
+         X_RESCALE(:,:) = 0.0_RT
+         FORALL (D=1:CONFIG%MDN) X_RESCALE(D,D) = 1.0_RT
+      END IF
+      !$OMP SECTION
+      IF ((.NOT. CONFIG%XI_NORMALIZED) .AND. (CONFIG%MDE .GT. 0)) THEN
+         CALL RADIALIZE(X(CONFIG%MDN+1:CONFIG%MDN+CONFIG%MDE,:), &
+              XI_SHIFT(:), XI_RESCALE(:,:))
+         ! Apply the shift to the source embeddings.
+         DO D = 1, CONFIG%MDE
+            M_EMB_VECS(D,:) = M_EMB_VECS(D,:) + XI_SHIFT(D)
+         END DO
+         ! Apply the transformation to the source embeddings.
+         M_EMB_VECS(:,:) = MATMUL(TRANSPOSE(XI_RESCALE(:,:)), M_EMB_VECS(:,:))
+         CONFIG%XI_NORMALIZED = .TRUE.
+      END IF
+      !$OMP SECTION
+      IF ((.NOT. CONFIG%AX_NORMALIZED) .AND. (CONFIG%ADN .GT. 0)) THEN
+         CALL RADIALIZE(AX(:CONFIG%ADN,:), &
+              MODEL(CONFIG%AISS:CONFIG%AISE), AX_RESCALE(:,:))
+         CONFIG%AX_NORMALIZED = .TRUE.
+      ELSE IF (CONFIG%ADN .GT. 0) THEN
+         MODEL(CONFIG%AISS:CONFIG%AISE) = 0.0_RT
+         AX_RESCALE(:,:) = 0.0_RT
+         FORALL (D=1:CONFIG%ADN) AX_RESCALE(D,D) = 1.0_RT
+      END IF
+      !$OMP SECTION
+      IF ((.NOT. CONFIG%AXI_NORMALIZED) .AND. (CONFIG%ADE .GT. 0)) THEN
+         CALL RADIALIZE(AX(CONFIG%ADN+1:CONFIG%ADN+CONFIG%ADE,:), &
+              XI_SHIFT(:), XI_RESCALE(:,:))
+         ! Apply the shift to the source embeddings.
+         DO D = 1, CONFIG%ADE
+            A_EMB_VECS(D,:) = A_EMB_VECS(D,:) + XI_SHIFT(D)
+         END DO
+         ! Apply the transformation to the source embeddings.
+         A_EMB_VECS(:,:) = MATMUL(TRANSPOSE(XI_RESCALE(:,:)), A_EMB_VECS(:,:))
+         CONFIG%AXI_NORMALIZED = .TRUE.
+      END IF
+      !$OMP SECTION
+      IF (.NOT. CONFIG%Y_NORMALIZED) THEN
+         CALL RADIALIZE(Y(:,:), MODEL(CONFIG%MOSS:CONFIG%MOSE), &
+              Y_RESCALE(:,:), INVERT_RESULT=.TRUE.)
+         CONFIG%Y_NORMALIZED = .TRUE.
+      ELSE
+         MODEL(CONFIG%MOSS:CONFIG%MOSE) = 0.0_RT
+         Y_RESCALE(:,:) = 0.0_RT
+         FORALL (D=1:CONFIG%MDO) Y_RESCALE(D,D) = 1.0_RT
+      END IF
+      !$OMP END SECTIONS
+      !$OMP END PARALLEL
+      ! 
+      ! Normalize AY outside the parallel region (AX must be normalized).
+      IF ((.NOT. CONFIG%AY_NORMALIZED) .AND. (CONFIG%ADO .GT. 0)) THEN
+         ! Disable "model" evaluation for this forward pass.
+         !   (Reuse "A_STATES" for the "M_STATES" argument, since it will be unused.)
+         D = CONFIG%MDI ; CONFIG%MDI = 0
+         CALL EVALUATE(CONFIG, MODEL, AX, AY, SIZES, X, Y, A_STATES, A_STATES, INFO)
+         CONFIG%MDI = D
+         ! Compute AY shift as the mean, apply it.
+         MODEL(CONFIG%AOSS:CONFIG%AOSE) = -SUM(AY(:,:),1) / REAL(SIZE(AY,1),RT)
+         DO D = 1, CONFIG%ADO
+            AY(:,D) = AY(:,D) + MODEL(CONFIG%AOSS + D-1)
+         END DO
+         ! Compute the AY scale as the standard deviation.
+         AY(1,:) = SUM(AY(:,:)**2,1)
+         WHERE (AY(1,:) .GT. 0.0_RT)
+            AY(1,:) = SQRT(AY(1,:))
+         ELSEWHERE
+            AY(1,:) = 1.0_RT
+         END WHERE
+         ! Apply the factor to the output vectors.
+         DO D = 1, CONFIG%ADO
+            A_OUT_VECS(:,D) = A_OUT_VECS(:,D) / AY(1,D)
+         END DO
+         CONFIG%AY_NORMALIZED = .TRUE.
+      END IF
+    END SUBROUTINE NORMALIZE_DATA
 
-    END DO fit_loop
 
-    ! Restore the best model seen so far (if enough steps were taken).
-    IF (REVERT_TO_BEST) THEN
-       MSE                      = BEST_MSE
-       MODEL(1:CONFIG%NUM_VARS) = BEST_MODEL(:)
-    END IF
-
-    ! Apply the data normalizing scaling factors to the weight matrices.
-    IF (SIZE(X,1) .GT. 0) &
-         CALL SCALE_BASIS(CONFIG%MDI, CONFIG%MDS, &
-         MODEL(CONFIG%MSIV:CONFIG%MEIV), 1.0_RT / X_SCALE(:))
-    IF (SIZE(AX,1) .GT. 0) &
-         CALL SCALE_BASIS(CONFIG%ADI, CONFIG%ADS, &
-         MODEL(CONFIG%ASIV:CONFIG%AEIV), 1.0_RT / AX_SCALE(:))
-    CALL SCALE_BASIS(CONFIG%MDS, CONFIG%MDO, &
-         MODEL(CONFIG%MSOV:CONFIG%MEOV), Y_SCALE(:), TRANS=.TRUE.)
+    ! Performing conditioning related operations on this model 
+    !  (ensure that mean squared error is effectively reduced).
+    SUBROUTINE CONDITION_MODEL(CONFIG, FIT_STEP, M_STATES, A_STATES, M_GRADS, A_GRADS, AY)
+      TYPE(MODEL_CONFIG), INTENT(IN) :: CONFIG
+      INTEGER, INTENT(IN) :: FIT_STEP
+      REAL(KIND=RT), DIMENSION(:,:,:) :: M_STATES, A_STATES, M_GRADS, A_GRADS
+      REAL(KIND=RT), DIMENSION(:,:) :: AY 
+      ! Local variables.
+      INTEGER :: I, VS, VE, J, R
+      REAL(KIND=RT) :: M_LENGTHS(SIZE(M_STATES,2)), A_LENGTHS(SIZE(A_STATES,2))
+      REAL(KIND=RT) :: M_STATE_TEMP(SIZE(M_STATES,1), SIZE(M_STATES,2))
+      REAL(KIND=RT) :: A_STATE_TEMP(SIZE(A_STATES,1), SIZE(A_STATES,2))
+      INTEGER :: M_ORDER(CONFIG%MDS), A_ORDER(CONFIG%ADS)
+      ! Maintain a constant max-norm across the magnitue of input and internal vectors.
+      CALL UNIT_MAX_NORM(CONFIG%MDI, CONFIG%MDS, CONFIG%MNS, &
+           MODEL(CONFIG%MSIV:CONFIG%MEIV), &
+           MODEL(CONFIG%MSSV:CONFIG%MESV))
+      IF (CONFIG%ADI .GT. 0) THEN
+         CALL UNIT_MAX_NORM(CONFIG%ADI, CONFIG%ADS, CONFIG%ANS, &
+              MODEL(CONFIG%ASIV:CONFIG%AEIV), &
+              MODEL(CONFIG%ASSV:CONFIG%AESV))
+      END IF
 
-    ! Erase the printed message if one was produced.
-    IF (DID_PRINT) WRITE (*,'(A)',ADVANCE='NO') RESET_LINE
+      ! Update the apositional model output shift to 
+      !  produce componentwise mean-zero values (prevent divergence).
+      IF (CONFIG%ADO .GT. 0) THEN
+         MODEL(CONFIG%AOSS:CONFIG%AOSE) = -SUM(AY(:,:),1) / REAL(SIZE(AY,1),RT)
+      END IF
+
+      ! -------------------------------------------------------------
+      ! TODO:
+      !  - Using the computed rank of values and gradients, delete the
+      !    least aligned basis functions and initialize with a combination
+      !    of aligning previous layer values with gradients (first nonzero
+      !    gradient components, then remaining nonzero input components).
+      ! 
+      ! - When measuring alignment of two vectors come up with way to
+      !   quickly find the "most aligned" shift term (the shift that
+      !   maximizes the dot product of the vectors assuming rectification).
+      ! 
+      IF (MOD(FIT_STEP-1,CONFIG%LOGGING_STEP_FREQUENCY) .EQ. 0) THEN
+         TOTAL_EVAL_RANK = 0
+         TOTAL_GRAD_RANK = 0
+         ! Check the rank of all internal apositional states.
+         J = CONFIG%ANS+1
+         !$OMP PARALLEL DO PRIVATE(A_ORDER,A_STATE_TEMP,A_LENGTHS,R) &
+         !$OMP& REDUCTION(+: TOTAL_EVAL_RANK, TOTAL_GRAD_RANK)
+         DO I = 1, CONFIG%ANS-1
+            ! Compute model state rank.
+            A_STATE_TEMP(:,:) = A_STATES(:,:,I)
+            CALL ORTHOGONALIZE(A_STATE_TEMP(:,:), A_LENGTHS(:), R)
+            TOTAL_EVAL_RANK = TOTAL_EVAL_RANK + R
+            ! Compute grad state rank.
+            A_STATE_TEMP(:,:) = A_GRADS(:,:,I)
+            CALL ORTHOGONALIZE(A_STATE_TEMP(:,:), A_LENGTHS(:), R)
+            TOTAL_GRAD_RANK = TOTAL_GRAD_RANK + R
+         END DO
+         !$OMP END PARALLEL DO
+         ! 
+         ! Check the rank of all internal model states.
+         J = CONFIG%MNS+1
+         !$OMP PARALLEL DO PRIVATE(M_ORDER,M_STATE_TEMP,M_LENGTHS,R) &
+         !$OMP& REDUCTION(+: TOTAL_EVAL_RANK, TOTAL_GRAD_RANK)
+         DO I = 1, CONFIG%MNS-1
+            ! Compute model state rank.
+            M_STATE_TEMP(:,:) = M_STATES(:,:,I)
+            CALL ORTHOGONALIZE(M_STATE_TEMP(:,:), M_LENGTHS(:), R, M_ORDER(:))
+            TOTAL_EVAL_RANK = TOTAL_EVAL_RANK + R
+            ! Compute grad state rank.
+            M_STATE_TEMP(:,:) = M_GRADS(:,:,I)
+            CALL ORTHOGONALIZE(M_STATE_TEMP(:,:), M_LENGTHS(:), R, M_ORDER(:))
+            TOTAL_GRAD_RANK = TOTAL_GRAD_RANK + R
+         END DO
+         !$OMP END PARALLEL DO
+      END IF
+
+    END SUBROUTINE CONDITION_MODEL
 
-  CONTAINS
 
     ! Set the input vectors and the state vectors to 
     SUBROUTINE UNIT_MAX_NORM(MDI, MDS, MNS, INPUT_VECS, STATE_VECS)
       INTEGER, INTENT(IN) :: MDI, MDS, MNS
       REAL(KIND=RT), INTENT(INOUT), DIMENSION(MDI,MDS)       :: INPUT_VECS
       REAL(KIND=RT), INTENT(INOUT), DIMENSION(MDS,MDS,MNS-1) :: STATE_VECS
       REAL(KIND=RT) :: SCALAR
@@ -1326,157 +2264,40 @@
       DO L = 1, SIZE(STATE_VECS,3)
          SCALAR = SQRT(MAXVAL(SUM(STATE_VECS(:,:,L)**2, 1)))
          STATE_VECS(:,:,L) = STATE_VECS(:,:,L) / SCALAR
       END DO
       !$OMP END PARALLEL DO
     END SUBROUTINE UNIT_MAX_NORM
 
+
     ! Scale a set of basis functions by "weights".
-    SUBROUTINE SCALE_BASIS(M, N, MATRIX, WEIGHTS, TRANS)
-      INTEGER, INTENT(IN) :: M, N
-      REAL(KIND=RT), INTENT(INOUT), DIMENSION(M,N) :: MATRIX
-      REAL(KIND=RT), INTENT(IN), DIMENSION(:) :: WEIGHTS
-      LOGICAL, INTENT(IN), OPTIONAL :: TRANS
-      LOGICAL :: T
-      INTEGER :: I
-      IF (PRESENT(TRANS)) THEN ; T = TRANS
-      ELSE                     ; T = .FALSE.
-      END IF
-      IF (T) THEN
-         DO I = 1, SIZE(WEIGHTS)
-            MATRIX(:,I) = MATRIX(:,I) * WEIGHTS(I)
-         END DO
-      ELSE
-         DO I = 1, SIZE(WEIGHTS)
-            MATRIX(I,:) = MATRIX(I,:) * WEIGHTS(I)
-         END DO
+    SUBROUTINE SCALE_BASIS(MATRIX, TRANSFORMATION)
+      REAL(KIND=RT), INTENT(INOUT), DIMENSION(:,:) :: MATRIX
+      REAL(KIND=RT), INTENT(IN), DIMENSION(:,:) :: TRANSFORMATION
+      ! Local variables.
+      REAL(KIND=RT), DIMENSION(SIZE(MATRIX,1),SIZE(MATRIX,2)) :: MATRIX_TEMP
+      INTEGER :: I, M, N
+      M = SIZE(MATRIX,1)
+      N = SIZE(MATRIX,2)
+      ! Create a copy of the matrix.
+      MATRIX_TEMP(:,:) = MATRIX(:,:)
+      IF (SIZE(TRANSFORMATION,1) .EQ. M) THEN
+         ! Multiply the transformation on the left.
+         CALL GEMM('N', 'N', M, N, M, 1.0_RT, &
+              TRANSFORMATION(:,:), M, &
+              MATRIX_TEMP(:,:), M, &
+              0.0_RT, MATRIX(:,:), M)
+      ELSE IF (SIZE(TRANSFORMATION,1) .EQ. N) THEN
+         ! Multiply the transformation on the right.
+         CALL GEMM('N', 'N', M, N, N, 1.0_RT, &
+              MATRIX_TEMP(:,:), M, &
+              TRANSFORMATION(:,:), N, &
+              0.0_RT, MATRIX(:,:), M)
       END IF
     END SUBROUTINE SCALE_BASIS
 
-    
-    ! ------------------------------------------------------------------
-    !                       FastSelect method
-    ! 
-    ! Given VALUES list of numbers, rearrange the elements of INDICES
-    ! such that the element of VALUES at INDICES(K) has rank K (holds
-    ! its same location as if all of VALUES were sorted in INDICES).
-    ! All elements of VALUES at INDICES(:K-1) are less than or equal,
-    ! while all elements of VALUES at INDICES(K+1:) are greater or equal.
-    ! 
-    ! This algorithm uses a recursive approach to exponentially shrink
-    ! the number of indices that have to be considered to find the
-    ! element of desired rank, while simultaneously pivoting values
-    ! that are less than the target rank left and larger right.
-    ! 
-    ! Arguments:
-    ! 
-    !   VALUES   --  A 1D array of real numbers. Will not be modified.
-    !   K        --  A positive integer for the rank index about which
-    !                VALUES should be rearranged.
-    ! Optional:
-    ! 
-    !   DIVISOR  --  A positive integer >= 2 that represents the
-    !                division factor used for large VALUES arrays.
-    !   MAX_SIZE --  An integer >= DIVISOR that represents the largest
-    !                sized VALUES for which the worst-case pivot value
-    !                selection is tolerable. A worst-case pivot causes
-    !                O( SIZE(VALUES)^2 ) runtime. This value should be
-    !                determined heuristically based on compute hardware.
-    ! Output:
-    ! 
-    !   INDICES  --  A 1D array of original indices for elements of VALUES.
-    ! 
-    !   The elements of the array INDICES are rearranged such that the
-    !   element at position VALUES(INDICES(K)) is in the same location 
-    !   it would be if all of VALUES were referenced in sorted order in
-    !   INDICES. Also known as, VALUES(INDICES(K)) has rank K.
-    ! 
-    RECURSIVE SUBROUTINE ARGSELECT(VALUES, K, INDICES, DIVISOR, MAX_SIZE, RECURSING)
-      USE ISO_FORTRAN_ENV, ONLY: RT => REAL32
-      IMPLICIT NONE
-      ! Arguments
-      REAL(KIND=RT), INTENT(IN), DIMENSION(:) :: VALUES
-      INTEGER, INTENT(IN) :: K
-      INTEGER, INTENT(INOUT), DIMENSION(:) :: INDICES
-      INTEGER, INTENT(IN), OPTIONAL :: DIVISOR, MAX_SIZE
-      LOGICAL, INTENT(IN), OPTIONAL :: RECURSING
-      ! Locals
-      INTEGER :: LEFT, RIGHT, L, R, MS, D, I
-      REAL(KIND=RT) :: P
-      ! Initialize the divisor (for making subsets).
-      IF (PRESENT(DIVISOR)) THEN ; D = DIVISOR
-      ELSE IF (SIZE(INDICES) .GE. 8388608) THEN ; D = 32 ! 2**5 ! 2**23
-      ELSE IF (SIZE(INDICES) .GE. 1048576) THEN ; D = 8  ! 2**3 ! 2**20
-      ELSE                                      ; D = 4  ! 2**2
-      END IF
-      ! Initialize the max size (before subsets are created).
-      IF (PRESENT(MAX_SIZE)) THEN ; MS = MAX_SIZE
-      ELSE                        ; MS = 1024 ! 2**10
-      END IF
-      ! When not recursing, set the INDICES to default values.
-      IF (.NOT. PRESENT(RECURSING)) THEN
-         FORALL(I=1:SIZE(INDICES)) INDICES(I) = I
-      END IF
-      ! Initialize LEFT and RIGHT to be the entire array.
-      LEFT = 1
-      RIGHT = SIZE(INDICES)
-      ! Loop until done finding the K-th element.
-      DO WHILE (LEFT .LT. RIGHT)
-         ! Use SELECT recursively to improve the quality of the
-         ! selected pivot value for large arrays.
-         IF (RIGHT - LEFT .GT. MS) THEN
-            ! Compute how many elements should be left and right of K
-            ! to maintain the same percentile in a subset.
-            L = K - K / D
-            R = L + (SIZE(INDICES) / D)
-            ! Perform fast select on an array a fraction of the size about K.
-            CALL ARGSELECT(VALUES(:), K - L + 1, INDICES(L:R), &
-                 DIVISOR=D, MAX_SIZE=MS, RECURSING=.TRUE.)
-         END IF
-         ! Pick a partition element at position K.
-         P = VALUES(INDICES(K))
-         L = LEFT
-         R = RIGHT
-         ! Move the partition element to the front of the list.
-         CALL SWAP_INT(INDICES(LEFT), INDICES(K))
-         ! Pre-swap the left and right elements (temporarily putting a
-         ! larger element on the left) before starting the partition loop.
-         IF (VALUES(INDICES(RIGHT)) .GT. P) THEN
-            CALL SWAP_INT(INDICES(LEFT), INDICES(RIGHT))
-         END IF
-         ! Now partition the elements about the pivot value "P".
-         DO WHILE (L .LT. R)
-            CALL SWAP_INT(INDICES(L), INDICES(R))
-            L = L + 1
-            R = R - 1
-            DO WHILE (VALUES(INDICES(L)) .LT. P) ; L = L + 1 ; END DO
-            DO WHILE (VALUES(INDICES(R)) .GT. P) ; R = R - 1 ; END DO
-         END DO
-         ! Place the pivot element back into its appropriate place.
-         IF (VALUES(INDICES(LEFT)) .EQ. P) THEN
-            CALL SWAP_INT(INDICES(LEFT), INDICES(R))
-         ELSE
-            R = R + 1
-            CALL SWAP_INT(INDICES(R), INDICES(RIGHT))
-         END IF
-         ! adjust left and right towards the boundaries of the subset
-         ! containing the (k - left + 1)th smallest element
-         IF (R .LE. K) LEFT = R + 1
-         IF (K .LE. R) RIGHT = R - 1
-      END DO
-    END SUBROUTINE ARGSELECT
-
-    SUBROUTINE SWAP_INT(V1, V2)
-      IMPLICIT NONE
-      INTEGER, INTENT(INOUT) :: V1, V2
-      INTEGER :: TEMP
-      TEMP = V1
-      V1 = V2
-      V2 = TEMP
-    END SUBROUTINE SWAP_INT
-
 
   END SUBROUTINE MINIMIZE_MSE
 
 
 END MODULE APOS
```

### Comparing `tlux-0.0.8/tlux/approximate/apos/test/argselect.f90` & `tlux-0.0.9/tlux/approximate/apos/test/argselect.f90`

 * *Files identical despite different names*

### Comparing `tlux-0.0.8/tlux/approximate/base.py` & `tlux-0.0.9/tlux/approximate/base.py`

 * *Files identical despite different names*

### Comparing `tlux-0.0.8/tlux/approximate/delaunay/__init__.py` & `tlux-0.0.9/tlux/approximate/delaunay/__init__.py`

 * *Files identical despite different names*

### Comparing `tlux-0.0.8/tlux/approximate/delaunay/blas.f` & `tlux-0.0.9/tlux/approximate/delaunay/blas.f`

 * *Files identical despite different names*

### Comparing `tlux-0.0.8/tlux/approximate/delaunay/delfort.py` & `tlux-0.0.9/tlux/approximate/delaunay/delfort.py`

 * *Files identical despite different names*

### Comparing `tlux-0.0.8/tlux/approximate/delaunay/delsparse/__init__.py` & `tlux-0.0.9/tlux/approximate/delaunay/delsparse/__init__.py`

 * *Files identical despite different names*

### Comparing `tlux-0.0.8/tlux/approximate/delaunay/delsparse/delsparse.f90` & `tlux-0.0.9/tlux/approximate/delaunay/delsparse/delsparse.f90`

 * *Files identical despite different names*

### Comparing `tlux-0.0.8/tlux/approximate/delaunay/delsparse/delsparse.x86_64.so` & `tlux-0.0.9/tlux/approximate/delaunay/delsparse/delsparse.x86_64.so`

 * *Files identical despite different names*

### Comparing `tlux-0.0.8/tlux/approximate/delaunay/delsparse/delsparse_c_wrapper.f90` & `tlux-0.0.9/tlux/approximate/delaunay/delsparse/delsparse_c_wrapper.f90`

 * *Files identical despite different names*

### Comparing `tlux-0.0.8/tlux/approximate/delaunay/delsparse/delsparse_python_wrapper.py` & `tlux-0.0.9/tlux/approximate/delaunay/delsparse/delsparse_python_wrapper.py`

 * *Files identical despite different names*

### Comparing `tlux-0.0.8/tlux/approximate/delaunay/delsparse/slatec.f` & `tlux-0.0.9/tlux/approximate/delaunay/delsparse/slatec.f`

 * *Files identical despite different names*

### Comparing `tlux-0.0.8/tlux/approximate/delaunay/delsparse.f90` & `tlux-0.0.9/tlux/approximate/delaunay/delsparse.f90`

 * *Files identical despite different names*

### Comparing `tlux-0.0.8/tlux/approximate/delaunay/lapack.f` & `tlux-0.0.9/tlux/approximate/delaunay/lapack.f`

 * *Files identical despite different names*

### Comparing `tlux-0.0.8/tlux/approximate/delaunay/qhull.py` & `tlux-0.0.9/tlux/approximate/delaunay/qhull.py`

 * *Files identical despite different names*

### Comparing `tlux-0.0.8/tlux/approximate/delaunay/slatec.f` & `tlux-0.0.9/tlux/approximate/delaunay/slatec.f`

 * *Files identical despite different names*

### Comparing `tlux-0.0.8/tlux/approximate/nearest_neighbor.py` & `tlux-0.0.9/tlux/approximate/nearest_neighbor.py`

 * *Files identical despite different names*

### Comparing `tlux-0.0.8/tlux/math/__init__.py` & `tlux-0.0.9/tlux/math/__init__.py`

 * *Files identical despite different names*

### Comparing `tlux-0.0.8/tlux/math/fmath.f90` & `tlux-0.0.9/tlux/math/fmath.f90`

 * *Files identical despite different names*

### Comparing `tlux-0.0.8/tlux/math/fraction.py` & `tlux-0.0.9/tlux/math/fraction.py`

 * *Files identical despite different names*

### Comparing `tlux-0.0.8/tlux/math/fsort.f90` & `tlux-0.0.9/tlux/math/fsort.f90`

 * *Files identical despite different names*

### Comparing `tlux-0.0.8/tlux/math/polynomial.py` & `tlux-0.0.9/tlux/math/polynomial.py`

 * *Files identical despite different names*

### Comparing `tlux-0.0.8/tlux/plot.py` & `tlux-0.0.9/tlux/plot.py`

 * *Files identical despite different names*

### Comparing `tlux-0.0.8/tlux/random.py` & `tlux-0.0.9/tlux/random.py`

 * *Files identical despite different names*

### Comparing `tlux-0.0.8/tlux/readme.md` & `tlux-0.0.9/tlux/readme.md`

 * *Files identical despite different names*

### Comparing `tlux-0.0.8/tlux.egg-info/PKG-INFO` & `tlux-0.0.9/tlux.egg-info/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,16 +1,16 @@
 Metadata-Version: 1.2
 Name: tlux
-Version: 0.0.8
+Version: 0.0.9
 Summary: A package.
 Home-page: https://github.com/tchlux/tlux
 Author: Thomas C.H. Lux
 Author-email: thomas.ch.lux@gmail.com
 License: MIT
-Download-URL: https://github.com/tchlux/tlux/archive/0.0.8.tar.gz
+Download-URL: https://github.com/tchlux/tlux/archive/0.0.9.tar.gz
 Description: UNKNOWN
 Keywords: python,python3
 Platform: UNKNOWN
 Classifier: Development Status :: 3 - Alpha
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
```

### Comparing `tlux-0.0.8/tlux.egg-info/SOURCES.txt` & `tlux-0.0.9/tlux.egg-info/SOURCES.txt`

 * *Files 15% similar despite different names*

```diff
@@ -1,8 +1,7 @@
-LICENSE.txt
 MANIFEST.in
 setup.cfg
 setup.py
 tlux/__init__.py
 tlux/__main__.py
 tlux/plot.py
 tlux/random.py
@@ -23,41 +22,44 @@
 tlux/about/version.txt
 tlux/about/version_history.md
 tlux/approximate/base.py
 tlux/approximate/nearest_neighbor.py
 tlux/approximate/apos/.gitignore
 tlux/approximate/apos/__init__.py
 tlux/approximate/apos/apos.f90
+tlux/approximate/apos/apos.mod
+tlux/approximate/apos/matrix_operations.mod
+tlux/approximate/apos/sort_and_select.mod
 tlux/approximate/apos/apos/__init__.py
+tlux/approximate/apos/apos/apos.arm64.so
 tlux/approximate/apos/apos/apos.f90
 tlux/approximate/apos/apos/apos.mod
-tlux/approximate/apos/apos/apos.x86_64.so
 tlux/approximate/apos/apos/apos_c_wrapper.f90
 tlux/approximate/apos/apos/apos_python_wrapper.py
 tlux/approximate/apos/apos/c_apos.mod
 tlux/approximate/apos/apos/c_matrix_operations.mod
+tlux/approximate/apos/apos/c_sort_and_select.mod
 tlux/approximate/apos/apos/matrix_operations.mod
+tlux/approximate/apos/apos/sort_and_select.mod
 tlux/approximate/apos/test/argselect.f90
 tlux/approximate/apos/test/test_argselect.py
+tlux/approximate/apos/test/test_argsort.f90
+tlux/approximate/apos/test/test_clock.f90
 tlux/approximate/delaunay/__init__.py
 tlux/approximate/delaunay/blas.f
 tlux/approximate/delaunay/delfort.py
 tlux/approximate/delaunay/delsparse.f90
 tlux/approximate/delaunay/lapack.f
 tlux/approximate/delaunay/qhull.py
 tlux/approximate/delaunay/slatec.f
 tlux/approximate/delaunay/delsparse/__init__.py
-tlux/approximate/delaunay/delsparse/c_delsparse_mod.mod
-tlux/approximate/delaunay/delsparse/c_real_precision.mod
 tlux/approximate/delaunay/delsparse/delsparse.f90
 tlux/approximate/delaunay/delsparse/delsparse.x86_64.so
 tlux/approximate/delaunay/delsparse/delsparse_c_wrapper.f90
-tlux/approximate/delaunay/delsparse/delsparse_mod.mod
 tlux/approximate/delaunay/delsparse/delsparse_python_wrapper.py
-tlux/approximate/delaunay/delsparse/real_precision.mod
 tlux/approximate/delaunay/delsparse/slatec.f
+tlux/math/.gitignore
 tlux/math/__init__.py
-tlux/math/fast_sort.mod
 tlux/math/fmath.f90
 tlux/math/fraction.py
 tlux/math/fsort.f90
 tlux/math/polynomial.py
```

