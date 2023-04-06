# Comparing `tmp/maptasker-1.3.1.tar.gz` & `tmp/maptasker-1.3.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "maptasker-1.3.1.tar", max compression
+gzip compressed data, was "maptasker-1.3.2.tar", max compression
```

## Comparing `maptasker-1.3.1.tar` & `maptasker-1.3.2.tar`

### file list

```diff
@@ -1,93 +1,94 @@
--rw-r--r--   0        0        0    35149 2023-02-10 17:49:08.224000 maptasker-1.3.1/LICENSE.txt
--rw-r--r--   0        0        0      296 2023-03-16 14:54:53.454155 maptasker-1.3.1/README_PyPl.md
--rw-r--r--   0        0        0     8196 2023-02-27 17:44:14.167143 maptasker-1.3.1/maptasker/.DS_Store
--rw-r--r--   0        0        0        0 2023-02-15 21:09:13.241439 maptasker-1.3.1/maptasker/__init__.py
--rw-r--r--   0        0        0      169 2023-03-11 17:11:25.837533 maptasker-1.3.1/maptasker/main.py
--rw-r--r--   0        0        0     6148 2023-02-27 16:37:40.904578 maptasker-1.3.1/maptasker/src/.DS_Store
--rw-r--r--   0        0        0        0 2023-02-17 17:51:56.564000 maptasker-1.3.1/maptasker/src/__init__.py
--rw-r--r--   0        0        0      212 2023-02-17 18:06:10.482000 maptasker-1.3.1/maptasker/src/__pycache__/__init__.cpython-310.pyc
--rw-r--r--   0        0        0     2285 2023-02-19 16:04:38.544193 maptasker-1.3.1/maptasker/src/__pycache__/actargs.cpython-310.pyc
--rw-r--r--   0        0        0     6600 2023-03-16 16:18:24.140995 maptasker-1.3.1/maptasker/src/__pycache__/action.cpython-310.pyc
--rw-r--r--   0        0        0   107715 2023-03-17 16:54:28.972890 maptasker-1.3.1/maptasker/src/__pycache__/actionc.cpython-310.pyc
--rw-r--r--   0        0        0     2586 2023-02-19 16:04:38.545163 maptasker-1.3.1/maptasker/src/__pycache__/actiond.cpython-310.pyc
--rw-r--r--   0        0        0     3552 2023-03-07 17:19:40.246352 maptasker-1.3.1/maptasker/src/__pycache__/actione.cpython-310.pyc
--rw-r--r--   0        0        0     2985 2023-02-19 16:04:38.539584 maptasker-1.3.1/maptasker/src/__pycache__/actionr.cpython-310.pyc
--rw-r--r--   0        0        0    14483 2023-03-10 18:30:57.731352 maptasker-1.3.1/maptasker/src/__pycache__/actiont.cpython-310.pyc
--rw-r--r--   0        0        0     1005 2023-03-03 20:16:45.890308 maptasker-1.3.1/maptasker/src/__pycache__/argsdict.cpython-310.pyc
--rw-r--r--   0        0        0     2041 2023-03-17 16:35:42.237037 maptasker-1.3.1/maptasker/src/__pycache__/caveats.cpython-310.pyc
--rw-r--r--   0        0        0     4400 2023-03-17 16:47:32.443814 maptasker-1.3.1/maptasker/src/__pycache__/colors.cpython-310.pyc
--rw-r--r--   0        0        0     1736 2023-03-16 14:47:52.664286 maptasker-1.3.1/maptasker/src/__pycache__/colrmode.cpython-310.pyc
--rw-r--r--   0        0        0     3848 2023-03-15 17:29:03.169022 maptasker-1.3.1/maptasker/src/__pycache__/condition.cpython-310.pyc
--rw-r--r--   0        0        0     1181 2023-03-16 15:14:47.510794 maptasker-1.3.1/maptasker/src/__pycache__/config.cpython-310.pyc
--rw-r--r--   0        0        0      952 2023-03-16 19:18:47.408265 maptasker-1.3.1/maptasker/src/__pycache__/debug.cpython-310.pyc
--rw-r--r--   0        0        0      351 2023-02-17 18:06:19.024776 maptasker-1.3.1/maptasker/src/__pycache__/depricated.cpython-310.pyc
--rw-r--r--   0        0        0     1430 2023-03-19 16:13:40.231551 maptasker-1.3.1/maptasker/src/__pycache__/getids.cpython-310.pyc
--rw-r--r--   0        0        0      969 2023-02-19 16:07:46.522758 maptasker-1.3.1/maptasker/src/__pycache__/getputarg.cpython-310.pyc
--rw-r--r--   0        0        0      754 2023-03-05 16:12:20.556282 maptasker-1.3.1/maptasker/src/__pycache__/initparg.cpython-310.pyc
--rw-r--r--   0        0        0     1223 2023-02-26 19:09:05.853521 maptasker-1.3.1/maptasker/src/__pycache__/kidapp.cpython-310.pyc
--rw-r--r--   0        0        0     6628 2023-03-16 19:15:58.455139 maptasker-1.3.1/maptasker/src/__pycache__/mapit.cpython-310.pyc
--rw-r--r--   0        0        0     3244 2023-03-16 19:15:58.476241 maptasker-1.3.1/maptasker/src/__pycache__/outputl.cpython-310.pyc
--rw-r--r--   0        0        0     4396 2023-03-06 15:38:34.820840 maptasker-1.3.1/maptasker/src/__pycache__/parsearg.cpython-310.pyc
--rw-r--r--   0        0        0     3770 2023-03-11 16:32:14.025148 maptasker-1.3.1/maptasker/src/__pycache__/prefers.cpython-310.pyc
--rw-r--r--   0        0        0      773 2023-02-26 20:27:39.482769 maptasker-1.3.1/maptasker/src/__pycache__/priority.cpython-310.pyc
--rw-r--r--   0        0        0     2067 2023-03-17 18:33:34.110297 maptasker-1.3.1/maptasker/src/__pycache__/proclist.cpython-310.pyc
--rw-r--r--   0        0        0     4590 2023-03-10 17:25:41.968956 maptasker-1.3.1/maptasker/src/__pycache__/profiles.cpython-310.pyc
--rw-r--r--   0        0        0      674 2023-03-03 18:37:39.993310 maptasker-1.3.1/maptasker/src/__pycache__/progargs.cpython-310.pyc
--rw-r--r--   0        0        0     4047 2023-03-16 15:27:46.759471 maptasker-1.3.1/maptasker/src/__pycache__/proginit.cpython-310.pyc
--rw-r--r--   0        0        0     7147 2023-03-17 19:28:02.320600 maptasker-1.3.1/maptasker/src/__pycache__/projects.cpython-310.pyc
--rw-r--r--   0        0        0     4273 2023-03-16 15:26:18.990027 maptasker-1.3.1/maptasker/src/__pycache__/runcli.cpython-310.pyc
--rw-r--r--   0        0        0     1601 2023-03-15 16:37:38.752585 maptasker-1.3.1/maptasker/src/__pycache__/rungui.cpython-310.pyc
--rw-r--r--   0        0        0     4169 2023-03-17 19:28:02.322665 maptasker-1.3.1/maptasker/src/__pycache__/scenes.cpython-310.pyc
--rw-r--r--   0        0        0     8098 2023-03-10 18:19:55.766918 maptasker-1.3.1/maptasker/src/__pycache__/servicec.cpython-310.pyc
--rw-r--r--   0        0        0     1329 2023-02-19 16:04:51.192560 maptasker-1.3.1/maptasker/src/__pycache__/share.cpython-310.pyc
--rw-r--r--   0        0        0      998 2023-02-19 16:04:38.542930 maptasker-1.3.1/maptasker/src/__pycache__/shellsort.cpython-310.pyc
--rw-r--r--   0        0        0     2365 2023-03-16 15:25:35.027123 maptasker-1.3.1/maptasker/src/__pycache__/sysconst.cpython-310.pyc
--rw-r--r--   0        0        0     2314 2023-03-14 17:05:20.258885 maptasker-1.3.1/maptasker/src/__pycache__/taskactn.cpython-310.pyc
--rw-r--r--   0        0        0     1331 2023-03-07 19:12:33.226952 maptasker-1.3.1/maptasker/src/__pycache__/taskerd.cpython-310.pyc
--rw-r--r--   0        0        0     6435 2023-03-16 14:26:19.653483 maptasker-1.3.1/maptasker/src/__pycache__/tasks.cpython-310.pyc
--rw-r--r--   0        0        0     3409 2023-03-19 16:23:23.360396 maptasker-1.3.1/maptasker/src/__pycache__/taskuniq.cpython-310.pyc
--rw-r--r--   0        0        0    13296 2023-03-15 17:59:53.530349 maptasker-1.3.1/maptasker/src/__pycache__/userintr.cpython-310.pyc
--rw-r--r--   0        0        0     1061 2023-02-22 16:51:10.059765 maptasker-1.3.1/maptasker/src/__pycache__/xmldata.cpython-310.pyc
--rw-r--r--   0        0        0     5612 2023-02-19 16:04:35.207746 maptasker-1.3.1/maptasker/src/actargs.py
--rw-r--r--   0        0        0    18462 2023-03-16 16:17:22.879063 maptasker-1.3.1/maptasker/src/action.py
--rw-r--r--   0        0        0   150799 2023-03-17 16:54:15.733175 maptasker-1.3.1/maptasker/src/actionc.py
--rw-r--r--   0        0        0     6713 2023-02-19 16:04:35.200924 maptasker-1.3.1/maptasker/src/actiond.py
--rw-r--r--   0        0        0     8850 2023-03-07 17:15:47.572361 maptasker-1.3.1/maptasker/src/actione.py
--rw-r--r--   0        0        0     7296 2023-02-19 16:04:35.202596 maptasker-1.3.1/maptasker/src/actionr.py
--rw-r--r--   0        0        0    17381 2023-03-10 18:26:19.758702 maptasker-1.3.1/maptasker/src/actiont.py
--rw-r--r--   0        0        0     3691 2023-03-17 16:35:42.136409 maptasker-1.3.1/maptasker/src/caveats.py
--rw-r--r--   0        0        0     8220 2023-03-17 16:37:08.589958 maptasker-1.3.1/maptasker/src/colors.py
--rw-r--r--   0        0        0     3285 2023-03-16 14:47:52.599612 maptasker-1.3.1/maptasker/src/colrmode.py
--rw-r--r--   0        0        0     9131 2023-03-15 16:55:20.022098 maptasker-1.3.1/maptasker/src/condition.py
--rw-r--r--   0        0        0     3742 2023-03-16 14:51:09.689577 maptasker-1.3.1/maptasker/src/config.py
--rw-r--r--   0        0        0     1945 2023-03-16 19:15:58.553655 maptasker-1.3.1/maptasker/src/debug.py
--rw-r--r--   0        0        0      342 2023-02-13 17:01:44.647422 maptasker-1.3.1/maptasker/src/depricated.py
--rw-r--r--   0        0        0     2576 2023-03-19 16:13:40.130882 maptasker-1.3.1/maptasker/src/getids.py
--rw-r--r--   0        0        0     2142 2023-02-19 16:07:46.460066 maptasker-1.3.1/maptasker/src/getputarg.py
--rw-r--r--   0        0        0     2366 2023-03-03 20:27:21.947370 maptasker-1.3.1/maptasker/src/initparg.py
--rw-r--r--   0        0        0     2397 2023-02-26 19:09:05.787572 maptasker-1.3.1/maptasker/src/kidapp.py
--rw-r--r--   0        0        0    17604 2023-03-16 19:15:58.381387 maptasker-1.3.1/maptasker/src/mapit.py
--rw-r--r--   0        0        0     7996 2023-03-16 19:15:58.384281 maptasker-1.3.1/maptasker/src/outputl.py
--rw-r--r--   0        0        0     8092 2023-03-06 15:38:34.755304 maptasker-1.3.1/maptasker/src/parsearg.py
--rw-r--r--   0        0        0     7224 2023-03-10 20:29:05.303454 maptasker-1.3.1/maptasker/src/prefers.py
--rw-r--r--   0        0        0     1649 2023-02-26 20:27:39.402221 maptasker-1.3.1/maptasker/src/priority.py
--rw-r--r--   0        0        0     4386 2023-03-17 18:33:26.636338 maptasker-1.3.1/maptasker/src/proclist.py
--rw-r--r--   0        0        0    10183 2023-03-10 17:21:57.366140 maptasker-1.3.1/maptasker/src/profiles.py
--rw-r--r--   0        0        0     1934 2023-03-03 18:37:39.903763 maptasker-1.3.1/maptasker/src/progargs.py
--rw-r--r--   0        0        0     7589 2023-03-16 15:27:46.669356 maptasker-1.3.1/maptasker/src/proginit.py
--rw-r--r--   0        0        0    14410 2023-03-17 19:28:02.220502 maptasker-1.3.1/maptasker/src/projects.py
--rw-r--r--   0        0        0     8999 2023-03-16 15:26:18.900702 maptasker-1.3.1/maptasker/src/runcli.py
--rw-r--r--   0        0        0     4154 2023-03-15 16:34:27.955367 maptasker-1.3.1/maptasker/src/rungui.py
--rw-r--r--   0        0        0     7556 2023-03-17 19:27:59.392583 maptasker-1.3.1/maptasker/src/scenes.py
--rw-r--r--   0        0        0    14219 2023-03-10 18:11:52.028611 maptasker-1.3.1/maptasker/src/servicec.py
--rw-r--r--   0        0        0     3290 2023-02-19 16:04:15.973939 maptasker-1.3.1/maptasker/src/share.py
--rw-r--r--   0        0        0     3354 2023-02-19 16:04:15.995487 maptasker-1.3.1/maptasker/src/shellsort.py
--rw-r--r--   0        0        0     4071 2023-03-16 15:25:34.944136 maptasker-1.3.1/maptasker/src/sysconst.py
--rw-r--r--   0        0        0     4921 2023-03-14 17:04:09.778356 maptasker-1.3.1/maptasker/src/taskactn.py
--rw-r--r--   0        0        0     3107 2023-03-07 19:12:33.157596 maptasker-1.3.1/maptasker/src/taskerd.py
--rw-r--r--   0        0        0    13873 2023-03-16 14:26:19.473341 maptasker-1.3.1/maptasker/src/tasks.py
--rw-r--r--   0        0        0     9244 2023-03-19 16:23:16.584702 maptasker-1.3.1/maptasker/src/taskuniq.py
--rw-r--r--   0        0        0    28690 2023-03-15 17:54:20.329915 maptasker-1.3.1/maptasker/src/userintr.py
--rw-r--r--   0        0        0     2426 2023-02-22 16:50:59.285536 maptasker-1.3.1/maptasker/src/xmldata.py
--rw-r--r--   0        0        0     1158 2023-03-16 15:00:45.380267 maptasker-1.3.1/pyproject.toml
--rw-r--r--   0        0        0     1296 1970-01-01 00:00:00.000000 maptasker-1.3.1/PKG-INFO
+-rw-r--r--   0        0        0    35149 2023-02-10 17:49:08.224000 maptasker-1.3.2/LICENSE.txt
+-rw-r--r--   0        0        0      296 2023-03-16 14:54:53.454155 maptasker-1.3.2/README_PyPl.md
+-rw-r--r--   0        0        0     8196 2023-02-27 17:44:14.167143 maptasker-1.3.2/maptasker/.DS_Store
+-rw-r--r--   0        0        0        0 2023-02-15 21:09:13.241439 maptasker-1.3.2/maptasker/__init__.py
+-rw-r--r--   0        0        0      169 2023-03-11 17:11:25.837533 maptasker-1.3.2/maptasker/main.py
+-rw-r--r--   0        0        0     6148 2023-02-27 16:37:40.000000 maptasker-1.3.2/maptasker/src/.DS_Store
+-rw-r--r--   0        0        0     1159 2023-03-23 17:42:41.413000 maptasker-1.3.2/maptasker/src/MainItem.py
+-rw-r--r--   0        0        0        0 2023-03-23 17:42:41.454000 maptasker-1.3.2/maptasker/src/__init__.py
+-rw-r--r--   0        0        0      212 2023-03-23 17:49:08.090530 maptasker-1.3.2/maptasker/src/__pycache__/__init__.cpython-310.pyc
+-rw-r--r--   0        0        0     3112 2023-03-23 17:49:08.129098 maptasker-1.3.2/maptasker/src/__pycache__/actargs.cpython-310.pyc
+-rw-r--r--   0        0        0     5777 2023-04-04 15:04:43.335513 maptasker-1.3.2/maptasker/src/__pycache__/action.cpython-310.pyc
+-rw-r--r--   0        0        0   107715 2023-03-23 17:49:08.156251 maptasker-1.3.2/maptasker/src/__pycache__/actionc.cpython-310.pyc
+-rw-r--r--   0        0        0     2586 2023-03-23 17:49:08.130230 maptasker-1.3.2/maptasker/src/__pycache__/actiond.cpython-310.pyc
+-rw-r--r--   0        0        0     4092 2023-04-04 17:31:32.000823 maptasker-1.3.2/maptasker/src/__pycache__/actione.cpython-310.pyc
+-rw-r--r--   0        0        0     3113 2023-03-31 16:38:58.765668 maptasker-1.3.2/maptasker/src/__pycache__/actionr.cpython-310.pyc
+-rw-r--r--   0        0        0    14483 2023-03-23 17:49:08.400678 maptasker-1.3.2/maptasker/src/__pycache__/actiont.cpython-310.pyc
+-rw-r--r--   0        0        0     1005 2023-03-23 17:42:41.454000 maptasker-1.3.2/maptasker/src/__pycache__/argsdict.cpython-310.pyc
+-rw-r--r--   0        0        0     1847 2023-04-04 15:34:28.525854 maptasker-1.3.2/maptasker/src/__pycache__/caveats.cpython-310.pyc
+-rw-r--r--   0        0        0     4400 2023-03-23 17:49:08.182225 maptasker-1.3.2/maptasker/src/__pycache__/colors.cpython-310.pyc
+-rw-r--r--   0        0        0     1726 2023-03-31 16:03:07.520328 maptasker-1.3.2/maptasker/src/__pycache__/colrmode.cpython-310.pyc
+-rw-r--r--   0        0        0     3848 2023-03-23 17:49:08.203819 maptasker-1.3.2/maptasker/src/__pycache__/condition.cpython-310.pyc
+-rw-r--r--   0        0        0      314 2023-03-23 17:49:08.122336 maptasker-1.3.2/maptasker/src/__pycache__/config.cpython-310.pyc
+-rw-r--r--   0        0        0     1123 2023-03-27 15:29:00.454256 maptasker-1.3.2/maptasker/src/__pycache__/debug.cpython-310.pyc
+-rw-r--r--   0        0        0      351 2023-03-23 17:49:08.397467 maptasker-1.3.2/maptasker/src/__pycache__/depricated.cpython-310.pyc
+-rw-r--r--   0        0        0     1379 2023-04-04 17:24:36.764246 maptasker-1.3.2/maptasker/src/__pycache__/getids.cpython-310.pyc
+-rw-r--r--   0        0        0      969 2023-03-23 17:49:08.182943 maptasker-1.3.2/maptasker/src/__pycache__/getputarg.cpython-310.pyc
+-rw-r--r--   0        0        0      754 2023-03-23 17:49:08.190511 maptasker-1.3.2/maptasker/src/__pycache__/initparg.cpython-310.pyc
+-rw-r--r--   0        0        0     1223 2023-03-23 17:49:08.206563 maptasker-1.3.2/maptasker/src/__pycache__/kidapp.cpython-310.pyc
+-rw-r--r--   0        0        0     5188 2023-04-04 17:33:48.583248 maptasker-1.3.2/maptasker/src/__pycache__/mapit.cpython-310.pyc
+-rw-r--r--   0        0        0     3748 2023-04-04 14:44:36.346643 maptasker-1.3.2/maptasker/src/__pycache__/outputl.cpython-310.pyc
+-rw-r--r--   0        0        0     4396 2023-03-23 17:49:08.186264 maptasker-1.3.2/maptasker/src/__pycache__/parsearg.cpython-310.pyc
+-rw-r--r--   0        0        0     3864 2023-03-30 18:39:13.650737 maptasker-1.3.2/maptasker/src/__pycache__/prefers.cpython-310.pyc
+-rw-r--r--   0        0        0      773 2023-03-23 17:49:08.204379 maptasker-1.3.2/maptasker/src/__pycache__/priority.cpython-310.pyc
+-rw-r--r--   0        0        0     2083 2023-04-03 19:11:00.966898 maptasker-1.3.2/maptasker/src/__pycache__/proclist.cpython-310.pyc
+-rw-r--r--   0        0        0     4581 2023-04-04 17:24:36.763063 maptasker-1.3.2/maptasker/src/__pycache__/profiles.cpython-310.pyc
+-rw-r--r--   0        0        0      678 2023-03-23 17:49:08.179364 maptasker-1.3.2/maptasker/src/__pycache__/progargs.cpython-310.pyc
+-rw-r--r--   0        0        0     6079 2023-03-30 17:50:55.588405 maptasker-1.3.2/maptasker/src/__pycache__/proginit.cpython-310.pyc
+-rw-r--r--   0        0        0     7395 2023-04-04 17:27:48.326254 maptasker-1.3.2/maptasker/src/__pycache__/projects.cpython-310.pyc
+-rw-r--r--   0        0        0     4273 2023-03-23 17:49:08.181004 maptasker-1.3.2/maptasker/src/__pycache__/runcli.cpython-310.pyc
+-rw-r--r--   0        0        0     1601 2023-03-23 17:49:08.189915 maptasker-1.3.2/maptasker/src/__pycache__/rungui.cpython-310.pyc
+-rw-r--r--   0        0        0     4247 2023-04-04 14:48:58.901070 maptasker-1.3.2/maptasker/src/__pycache__/scenes.cpython-310.pyc
+-rw-r--r--   0        0        0     8098 2023-03-23 17:49:08.215471 maptasker-1.3.2/maptasker/src/__pycache__/servicec.cpython-310.pyc
+-rw-r--r--   0        0        0     2046 2023-04-04 14:24:20.204824 maptasker-1.3.2/maptasker/src/__pycache__/share.cpython-310.pyc
+-rw-r--r--   0        0        0      998 2023-03-23 17:49:08.120911 maptasker-1.3.2/maptasker/src/__pycache__/shellsort.cpython-310.pyc
+-rw-r--r--   0        0        0     2376 2023-04-04 17:43:19.909562 maptasker-1.3.2/maptasker/src/__pycache__/sysconst.cpython-310.pyc
+-rw-r--r--   0        0        0     2374 2023-04-03 19:11:00.967760 maptasker-1.3.2/maptasker/src/__pycache__/taskactn.cpython-310.pyc
+-rw-r--r--   0        0        0     1331 2023-03-23 17:49:08.199590 maptasker-1.3.2/maptasker/src/__pycache__/taskerd.cpython-310.pyc
+-rw-r--r--   0        0        0     7944 2023-04-04 16:03:53.668918 maptasker-1.3.2/maptasker/src/__pycache__/tasks.cpython-310.pyc
+-rw-r--r--   0        0        0     3427 2023-04-04 17:52:29.735433 maptasker-1.3.2/maptasker/src/__pycache__/taskuniq.cpython-310.pyc
+-rw-r--r--   0        0        0    13296 2023-04-04 17:53:27.430394 maptasker-1.3.2/maptasker/src/__pycache__/userintr.cpython-310.pyc
+-rw-r--r--   0        0        0     2504 2023-04-04 14:19:09.456115 maptasker-1.3.2/maptasker/src/__pycache__/xmldata.cpython-310.pyc
+-rw-r--r--   0        0        0     6328 2023-03-23 17:42:41.454000 maptasker-1.3.2/maptasker/src/actargs.py
+-rw-r--r--   0        0        0    14801 2023-04-04 15:04:43.263794 maptasker-1.3.2/maptasker/src/action.py
+-rw-r--r--   0        0        0   150799 2023-03-23 17:42:41.454000 maptasker-1.3.2/maptasker/src/actionc.py
+-rw-r--r--   0        0        0     6713 2023-03-23 17:42:41.454000 maptasker-1.3.2/maptasker/src/actiond.py
+-rw-r--r--   0        0        0     9670 2023-04-04 17:31:26.510616 maptasker-1.3.2/maptasker/src/actione.py
+-rw-r--r--   0        0        0     7541 2023-03-31 16:38:58.724693 maptasker-1.3.2/maptasker/src/actionr.py
+-rw-r--r--   0        0        0    17381 2023-03-23 17:42:41.413000 maptasker-1.3.2/maptasker/src/actiont.py
+-rw-r--r--   0        0        0     3401 2023-04-04 15:26:45.790042 maptasker-1.3.2/maptasker/src/caveats.py
+-rw-r--r--   0        0        0     8220 2023-03-23 17:42:41.450000 maptasker-1.3.2/maptasker/src/colors.py
+-rw-r--r--   0        0        0     3285 2023-03-31 16:03:07.377591 maptasker-1.3.2/maptasker/src/colrmode.py
+-rw-r--r--   0        0        0     9131 2023-03-23 17:42:41.454000 maptasker-1.3.2/maptasker/src/condition.py
+-rw-r--r--   0        0        0     2318 2023-03-23 17:42:41.454000 maptasker-1.3.2/maptasker/src/config.py
+-rw-r--r--   0        0        0     2440 2023-03-27 15:29:00.384399 maptasker-1.3.2/maptasker/src/debug.py
+-rw-r--r--   0        0        0      342 2023-03-23 17:42:41.413000 maptasker-1.3.2/maptasker/src/depricated.py
+-rw-r--r--   0        0        0     2463 2023-04-04 17:24:36.654348 maptasker-1.3.2/maptasker/src/getids.py
+-rw-r--r--   0        0        0     2142 2023-03-23 17:42:41.413000 maptasker-1.3.2/maptasker/src/getputarg.py
+-rw-r--r--   0        0        0     2366 2023-03-23 17:42:41.413000 maptasker-1.3.2/maptasker/src/initparg.py
+-rw-r--r--   0        0        0     2397 2023-03-23 17:42:41.454000 maptasker-1.3.2/maptasker/src/kidapp.py
+-rw-r--r--   0        0        0    15342 2023-04-04 17:33:48.564468 maptasker-1.3.2/maptasker/src/mapit.py
+-rw-r--r--   0        0        0     9854 2023-04-04 14:42:44.210128 maptasker-1.3.2/maptasker/src/outputl.py
+-rw-r--r--   0        0        0     8092 2023-03-23 17:42:41.413000 maptasker-1.3.2/maptasker/src/parsearg.py
+-rw-r--r--   0        0        0     7310 2023-03-30 18:39:13.574286 maptasker-1.3.2/maptasker/src/prefers.py
+-rw-r--r--   0        0        0     1649 2023-03-23 17:42:41.413000 maptasker-1.3.2/maptasker/src/priority.py
+-rw-r--r--   0        0        0     4688 2023-04-03 19:11:00.841847 maptasker-1.3.2/maptasker/src/proclist.py
+-rw-r--r--   0        0        0    10484 2023-04-04 17:24:36.651496 maptasker-1.3.2/maptasker/src/profiles.py
+-rw-r--r--   0        0        0     1947 2023-03-23 17:42:41.454000 maptasker-1.3.2/maptasker/src/progargs.py
+-rw-r--r--   0        0        0    10459 2023-03-30 17:50:55.543478 maptasker-1.3.2/maptasker/src/proginit.py
+-rw-r--r--   0        0        0    15015 2023-04-04 17:27:48.225904 maptasker-1.3.2/maptasker/src/projects.py
+-rw-r--r--   0        0        0     8999 2023-03-23 17:42:41.454000 maptasker-1.3.2/maptasker/src/runcli.py
+-rw-r--r--   0        0        0     4154 2023-03-23 17:42:41.454000 maptasker-1.3.2/maptasker/src/rungui.py
+-rw-r--r--   0        0        0     7762 2023-04-04 14:44:36.436998 maptasker-1.3.2/maptasker/src/scenes.py
+-rw-r--r--   0        0        0    14219 2023-03-23 17:42:41.454000 maptasker-1.3.2/maptasker/src/servicec.py
+-rw-r--r--   0        0        0     4300 2023-04-04 14:24:15.779355 maptasker-1.3.2/maptasker/src/share.py
+-rw-r--r--   0        0        0     3354 2023-03-23 17:42:41.454000 maptasker-1.3.2/maptasker/src/shellsort.py
+-rw-r--r--   0        0        0     4082 2023-04-04 17:43:19.871730 maptasker-1.3.2/maptasker/src/sysconst.py
+-rw-r--r--   0        0        0     5247 2023-04-03 19:11:00.837179 maptasker-1.3.2/maptasker/src/taskactn.py
+-rw-r--r--   0        0        0     3107 2023-03-23 17:42:41.413000 maptasker-1.3.2/maptasker/src/taskerd.py
+-rw-r--r--   0        0        0    15228 2023-04-04 15:44:52.485008 maptasker-1.3.2/maptasker/src/tasks.py
+-rw-r--r--   0        0        0     9526 2023-04-04 17:52:29.653958 maptasker-1.3.2/maptasker/src/taskuniq.py
+-rw-r--r--   0        0        0    28690 2023-03-23 17:42:41.454000 maptasker-1.3.2/maptasker/src/userintr.py
+-rw-r--r--   0        0        0     6623 2023-04-04 13:54:26.475440 maptasker-1.3.2/maptasker/src/xmldata.py
+-rw-r--r--   0        0        0     1157 2023-03-19 17:43:40.831675 maptasker-1.3.2/pyproject.toml
+-rw-r--r--   0        0        0     1296 1970-01-01 00:00:00.000000 maptasker-1.3.2/PKG-INFO
```

### Comparing `maptasker-1.3.1/LICENSE.txt` & `maptasker-1.3.2/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `maptasker-1.3.1/maptasker/.DS_Store` & `maptasker-1.3.2/maptasker/.DS_Store`

 * *Files identical despite different names*

### Comparing `maptasker-1.3.1/maptasker/src/.DS_Store` & `maptasker-1.3.2/maptasker/src/.DS_Store`

 * *Files identical despite different names*

### Comparing `maptasker-1.3.1/maptasker/src/__pycache__/action.cpython-310.pyc` & `maptasker-1.3.2/maptasker/src/__pycache__/action.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Thu Mar 16 16:17:22 2023 UTC, .py size: 18462 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 15% similar despite different names*

```diff
@@ -1,413 +1,362 @@
-00000000: 6f0d 0d0a 0000 0000 1241 1364 1e48 0000  o........A.d.H..
+00000000: 6f0d 0d0a 0000 0000 8b3c 2c64 d139 0000  o........<,d.9..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
-00000020: 0003 0000 0040 0000 0073 a200 0000 6400  .....@...s....d.
-00000030: 6401 6c00 6d01 0200 0100 6d02 5a03 0100  d.l.m.....m.Z...
-00000040: 6400 6402 6c04 6d05 5a05 0100 6400 6401  d.d.l.m.Z...d.d.
-00000050: 6c06 5a06 6400 6401 6c07 5a07 6506 a008  l.Z.d.d.l.Z.e...
-00000060: 6403 a101 5a09 6404 6405 8400 5a0a 6406  d...Z.d.d...Z.d.
-00000070: 6407 8400 5a0b 6408 6409 8400 5a0c 640a  d...Z.d.d...Z.d.
-00000080: 640b 8400 5a0d 640c 640d 8400 5a0e 640e  d...Z.d.d...Z.d.
-00000090: 640f 8400 5a0f 6410 6411 8400 5a10 6412  d...Z.d.d...Z.d.
-000000a0: 6511 6602 6413 6414 8404 5a12 6415 6416  e.f.d.d...Z.d.d.
-000000b0: 8400 5a13 6417 6418 8400 5a14 6419 641a  ..Z.d.d...Z.d.d.
-000000c0: 8400 5a15 641b 641c 8400 5a16 6401 5300  ..Z.d.d...Z.d.S.
-000000d0: 291d e900 0000 004e 2901 da06 6c6f 6767  )......N)...logg
-000000e0: 6572 7a05 3c2e 2a3f 3e63 0200 0000 0000  erz.<.*?>c......
-000000f0: 0000 0000 0000 0800 0000 0600 0000 4300  ..............C.
-00000100: 0000 739e 0000 0067 0067 0067 0003 0302  ..s....g.g.g....
-00000110: 037d 027d 037d 0464 017d 057c 0044 005d  .}.}.}.d.}.|.D.]
-00000120: 187d 067c 066a 007c 0176 0072 1471 0c7c  .}.|.j.|.v.r.q.|
-00000130: 066a 01a0 0264 02a1 017d 077c 0764 0075  .j...d...}.|.d.u
-00000140: 0072 1f71 0c7c 04a0 037c 06a1 0101 0071  .r.q.|...|.....q
-00000150: 0c7c 0472 4a74 047c 0464 0364 0483 0301  .|.rJt.|.d.d....
-00000160: 007c 0444 005d 117d 067c 03a0 037c 066a  .|.D.].}.|...|.j
-00000170: 00a1 0101 007c 02a0 037c 066a 01a0 0264  .....|...|.j...d
-00000180: 02a1 01a1 0101 0071 2f64 0564 0684 0074  .......q/d.d...t
-00000190: 057c 0283 0144 0083 017d 057c 027c 037c  .|...D...}.|.|.|
-000001a0: 0566 0353 0029 074e 7201 0000 00da 0273  .f.S.).Nr......s
-000001b0: 7254 4663 0100 0000 0000 0000 0000 0000  rTFc............
-000001c0: 0300 0000 0400 0000 5300 0000 7318 0000  ........S...s...
-000001d0: 0067 007c 005d 085c 027d 017d 0274 007c  .g.|.].\.}.}.t.|
-000001e0: 0183 0191 0271 0253 00a9 0029 01da 0373  .....q.S...)...s
-000001f0: 7472 2903 da02 2e30 5a03 696e 64da 0178  tr)....0Z.ind..x
-00000200: 7204 0000 0072 0400 0000 fa75 2f55 7365  r....r.....u/Use
-00000210: 7273 2f6d 696b 7275 6269 6e2f 4c69 6272  rs/mikrubin/Libr
-00000220: 6172 792f 436c 6f75 6453 746f 7261 6765  ary/CloudStorage
-00000230: 2f47 6f6f 676c 6544 7269 7665 2d6d 696b  /GoogleDrive-mik
-00000240: 7275 6269 6e40 676d 6169 6c2e 636f 6d2f  rubin@gmail.com/
-00000250: 4d79 2044 7269 7665 2f50 7974 686f 6e2f  My Drive/Python/
-00000260: 6d61 7074 6173 6b65 722f 6d61 7074 6173  maptasker/maptas
-00000270: 6b65 722f 7372 632f 6163 7469 6f6e 2e70  ker/src/action.p
-00000280: 79da 0a3c 6c69 7374 636f 6d70 3e33 0000  y..<listcomp>3..
-00000290: 0073 0600 0000 0600 0c01 06ff 7a1c 6765  .s..........z.ge
-000002a0: 745f 6172 6773 2e3c 6c6f 6361 6c73 3e2e  t_args.<locals>.
-000002b0: 3c6c 6973 7463 6f6d 703e 2906 da03 7461  <listcomp>)...ta
-000002c0: 67da 0661 7474 7269 62da 0367 6574 da06  g..attrib..get..
-000002d0: 6170 7065 6e64 da0a 7368 656c 6c5f 736f  append..shell_so
-000002e0: 7274 da09 656e 756d 6572 6174 6529 08da  rt..enumerate)..
-000002f0: 0661 6374 696f 6e5a 0b69 676e 6f72 655f  .actionZ.ignore_
-00000300: 6c69 7374 da08 6172 675f 6c69 7374 5a09  list..arg_listZ.
-00000310: 7479 7065 5f6c 6973 745a 0b6d 6173 7465  type_listZ.maste
-00000320: 725f 6c69 7374 5a08 6172 675f 6e75 6d73  r_listZ.arg_nums
-00000330: da05 6368 696c 645a 0a61 6374 696f 6e5f  ..childZ.action_
-00000340: 6172 6772 0400 0000 7204 0000 0072 0800  argr....r....r..
-00000350: 0000 da08 6765 745f 6172 6773 2100 0000  ....get_args!...
-00000360: 7324 0000 0010 0104 0108 010a 0102 010c  s$..............
-00000370: 0108 0102 010c 0204 020c 0208 010c 0114  ................
-00000380: 0106 0106 0106 ff0a 0472 1300 0000 6303  .........r....c.
-00000390: 0000 0000 0000 0000 0000 0003 0000 0002  ................
-000003a0: 0000 0043 0000 0073 1000 0000 7c00 6401  ...C...s....|.d.
-000003b0: 6b02 7206 7c01 5300 7c02 5300 2902 4eda  k.r.|.S.|.S.).N.
-000003c0: 0130 7204 0000 0029 035a 0974 6865 5f76  .0r....).Z.the_v
-000003d0: 616c 7565 5a0e 6966 5f7a 6572 6f5f 7374  alueZ.if_zero_st
-000003e0: 7269 6e67 5a12 6966 5f6e 6f74 5f7a 6572  ringZ.if_not_zer
-000003f0: 6f5f 7374 7269 6e67 7204 0000 0072 0400  o_stringr....r..
-00000400: 0000 7208 0000 00da 0c69 665f 7a65 726f  ..r......if_zero
-00000410: 5f65 6c73 653d 0000 0073 0200 0000 1001  _else=...s......
-00000420: 7215 0000 0063 0100 0000 0000 0000 0000  r....c..........
-00000430: 0000 0600 0000 0d00 0000 4300 0000 7372  ..........C...sr
-00000440: 0000 0064 0164 0264 0364 0464 0564 0664  ...d.d.d.d.d.d.d
-00000450: 0764 0864 0164 0964 0a64 0b64 0c9c 0c7d  .d.d.d.d.d.d...}
-00000460: 017c 00a0 0064 0da1 016a 017d 027c 00a0  .|...d...j.}.|..
-00000470: 0064 0ea1 016a 017d 037c 017c 0319 007d  .d...j.}.|.|...}
-00000480: 0464 0f7c 0476 0172 327c 00a0 0064 10a1  .d.|.v.r2|...d..
-00000490: 016a 0164 0075 0172 327c 00a0 0064 10a1  .j.d.u.r2|...d..
-000004a0: 016a 017d 056e 0264 117d 057c 027c 047c  .j.}.n.d.}.|.|.|
-000004b0: 0566 0353 0029 124e 7a03 203d 207a 0520  .f.S.).Nz. = z. 
-000004c0: 4e45 5120 7a03 207e 207a 0420 217e 207a  NEQ z. ~ z. !~ z
-000004d0: 0520 217e 5220 7a04 207e 5220 7a03 203c  . !~R z. ~R z. <
-000004e0: 207a 0320 3e20 7a04 2021 3d20 7a07 2069   z. > z. != z. i
-000004f0: 7320 7365 747a 0820 6e6f 7420 7365 7429  s setz. not set)
-00000500: 0c72 1400 0000 da01 31da 0132 da01 33da  .r......1..2..3.
-00000510: 0134 da01 35da 0136 da01 37da 0138 da01  .4..5..6..7..8..
-00000520: 39da 0231 32da 0231 335a 036c 6873 da02  9..12..13Z.lhs..
-00000530: 6f70 da03 7365 745a 0372 6873 da00 2902  op..setZ.rhs..).
-00000540: da04 6669 6e64 da04 7465 7874 2906 7212  ..find..text).r.
-00000550: 0000 005a 0e74 6865 5f6f 7065 7261 7469  ...Z.the_operati
-00000560: 6f6e 735a 0c66 6972 7374 5f73 7472 696e  onsZ.first_strin
-00000570: 675a 096f 7065 7261 7469 6f6e 5a0d 7468  gZ.operationZ.th
-00000580: 655f 6f70 6572 6174 696f 6e5a 0d73 6563  e_operationZ.sec
-00000590: 6f6e 645f 7374 7269 6e67 7204 0000 0072  ond_stringr....r
-000005a0: 0400 0000 7208 0000 00da 1265 7661 6c75  ....r......evalu
-000005b0: 6174 655f 636f 6e64 6974 696f 6e44 0000  ate_conditionD..
-000005c0: 0073 2800 0000 0202 0201 0201 0201 0201  .s(.............
-000005d0: 0201 0201 0201 0201 0201 0201 0201 06f4  ................
-000005e0: 0c0f 0c01 0801 1802 0e02 0402 0a02 7226  ..............r&
-000005f0: 0000 0063 0100 0000 0000 0000 0000 0000  ...c............
-00000600: 0300 0000 0500 0000 4300 0000 7374 0000  ........C...st..
-00000610: 0074 007c 0083 0164 0118 007d 017c 0164  .t.|...d...}.|.d
-00000620: 026b 0472 3874 017c 0083 0144 005d 297d  .k.r8t.|...D.])}
-00000630: 027c 0264 036b 0272 197c 0164 0118 007d  .|.d.k.r.|.d...}
-00000640: 0171 0e7c 0274 007c 0283 0164 0418 0064  .q.|.t.|...d...d
-00000650: 0085 0219 0064 056b 0272 357c 0264 0074  .....d.k.r5|.d.t
-00000660: 007c 0283 0164 0418 0085 0219 007c 007c  .|...d.......|.|
-00000670: 013c 007c 0002 0001 0053 0001 007c 0053  .<.|.....S...|.S
-00000680: 007c 0053 0029 064e e901 0000 0072 0100  .|.S.).N.....r..
-00000690: 0000 7223 0000 00e9 0200 0000 fa02 2c20  ..r#.........., 
-000006a0: 2902 da03 6c65 6eda 0872 6576 6572 7365  )...len..reverse
-000006b0: 6429 03da 0d6d 6174 6368 5f72 6573 756c  d)...match_resul
-000006c0: 7473 5a10 6c61 7374 5f76 616c 6964 5f65  tsZ.last_valid_e
-000006d0: 6e74 7279 da04 6974 656d 7204 0000 0072  ntry..itemr....r
-000006e0: 0400 0000 7208 0000 00da 1364 726f 705f  ....r......drop_
-000006f0: 7472 6169 6c69 6e67 5f63 6f6d 6d61 6400  trailing_commad.
-00000700: 0000 7314 0000 000c 0108 010c 0108 010a  ..s.............
-00000710: 0118 0118 0108 0102 0208 0172 2e00 0000  ...........r....
-00000720: 6300 0000 0000 0000 0000 0000 0003 0000  c...............
-00000730: 0006 0000 0047 0000 0073 6c00 0000 6700  .....G...sl...g.
-00000740: 7d01 7c00 4400 5d2f 7d02 7c02 6401 1900  }.|.D.]/}.|.d...
-00000750: 721c 7c02 6402 1900 6403 6b03 721c 7c01  r.|.d...d.k.r.|.
-00000760: a000 7c02 6404 1900 7c02 6402 1900 1700  ..|.d...|.d.....
-00000770: a101 0100 7104 7c02 6401 1900 7326 7c02  ....q.|.d...s&|.
-00000780: 6402 1900 6405 6b03 722c 7c01 a000 6403  d...d.k.r,|...d.
-00000790: a101 0100 7104 7c01 a000 7c02 6404 1900  ....q.|...|.d...
-000007a0: a101 0100 7104 7c01 5300 2906 4e72 0100  ....q.|.S.).Nr..
-000007b0: 0000 7227 0000 0072 2300 0000 7228 0000  ..r'...r#...r(..
-000007c0: 0072 1600 0000 2901 720d 0000 0029 03da  .r....).r....)..
-000007d0: 0461 7267 73da 0772 6573 756c 7473 722d  .args..resultsr-
-000007e0: 0000 0072 0400 0000 7204 0000 0072 0800  ...r....r....r..
-000007f0: 0000 da17 6576 616c 7561 7465 5f61 6374  ....evaluate_act
-00000800: 696f 6e5f 7365 7474 696e 677a 0000 0073  ion_settingz...s
-00000810: 1000 0000 0401 0802 1401 1801 1401 0c01  ................
-00000820: 1002 0401 7231 0000 0063 0500 0000 0000  ....r1...c......
-00000830: 0000 0000 0000 0f00 0000 0400 0000 4300  ..............C.
-00000840: 0000 73a6 0100 0064 0164 026c 006d 017d  ..s....d.d.l.m.}
-00000850: 0501 007c 007c 0119 007d 067c 0664 0119  ...|.|...}.|.d..
-00000860: 007d 0764 017d 0864 037d 097c 0972 d17c  .}.d.}.d.}.|.r.|
-00000870: 0864 0417 0074 027c 0683 0116 007d 087c  .d...t.|.....}.|
-00000880: 067c 0819 007d 0a7c 0aa0 03a1 0072 4a7c  .|...}.|.....rJ|
-00000890: 0864 0417 0074 027c 0683 0116 007d 087c  .d...t.|.....}.|
-000008a0: 067c 0819 007d 0b7c 0a7c 026b 0272 407c  .|...}.|.|.k.r@|
-000008b0: 03a0 047c 077c 0b17 0064 0517 00a1 0101  ...|.|...d......
-000008c0: 0009 0064 0053 007c 0874 027c 0683 016b  ...d.S.|.t.|...k
-000008d0: 0472 4909 0064 0053 006e 857c 0a64 0676  .rI..d.S.n.|.d.v
-000008e0: 0072 707c 0864 0417 0074 027c 0683 0116  .rp|.d...t.|....
-000008f0: 007d 087c 067c 0819 007d 0b74 0564 077c  .}.|.|...}.t.d.|
-00000900: 027c 0b67 0383 017d 0c7c 0c64 0119 009b  .|.g...}.|.d....
-00000910: 0064 059d 027d 0c7c 03a0 047c 0ca1 0101  .d...}.|...|....
-00000920: 0009 0064 0053 007c 0a64 086b 0272 bc7c  ...d.S.|.d.k.r.|
-00000930: 0864 0417 0074 027c 0683 0116 007d 087c  .d...t.|.....}.|
-00000940: 067c 0819 007c 0576 0072 a17c 057c 067c  .|...|.v.r.|.|.|
-00000950: 0819 0019 0074 067c 0283 0119 0067 017d  .....t.|.....g.}
-00000960: 0c7c 067c 0864 0918 0019 007c 0c64 0119  .|.|.d.....|.d..
-00000970: 0017 0064 0517 007d 0c7c 03a0 047c 0ca1  ...d...}.|...|..
-00000980: 0101 0009 0064 0053 0064 0a7c 067c 0819  .....d.S.d.|.|..
-00000990: 009b 0064 0b7c 009b 009d 047d 0d74 07a0  ...d.|.....}.t..
-000009a0: 087c 0da1 0101 0074 097c 0d83 0101 0074  .|.....t.|.....t
-000009b0: 0aa0 0b64 04a1 0101 0009 0064 0053 0064  ...d.......d.S.d
-000009c0: 0c7c 0a9b 0064 0d7c 049b 009d 047c 0066  .|...d.|.....|.f
-000009d0: 027d 0e74 07a0 087c 0ea1 0101 0074 0b64  .}.t...|.....t.d
-000009e0: 0e83 0101 007c 0973 1464 0053 0029 0f4e  .....|.s.d.S.).N
-000009f0: 7201 0000 0029 01da 0d6c 6f6f 6b75 705f  r....)...lookup_
-00000a00: 7661 6c75 6573 5472 2700 0000 7229 0000  valuesTr'...r)..
-00000a10: 0029 02da 0165 da02 6966 46da 016c 7228  .)...e..ifF..lr(
-00000a20: 0000 007a 0f50 726f 6772 616d 2065 7272  ...z.Program err
-00000a30: 6f72 3a20 7a2b 2069 7320 6e6f 7420 696e  or: z+ is not in
-00000a40: 2061 6374 696f 6e74 2028 6c6f 6f6b 7570   actiont (lookup
-00000a50: 2074 6162 6c65 2920 666f 7220 6e61 6d65   table) for name
-00000a60: 3a7a 3367 6574 5f78 6d6c 5f69 6e74 5f61  :z3get_xml_int_a
-00000a70: 7267 756d 656e 745f 746f 5f76 616c 7565  rgument_to_value
-00000a80: 2066 6169 6c65 642d 2074 6869 735f 656c   failed- this_el
-00000a90: 656d 656e 743a fa01 20e9 0800 0000 290c  ement:.. .....).
-00000aa0: 5a15 6d61 7074 6173 6b65 722e 7372 632e  Z.maptasker.src.
-00000ab0: 6163 7469 6f6e 7472 3200 0000 722a 0000  actiontr2...r*..
-00000ac0: 00da 0769 7364 6967 6974 720d 0000 0072  ...isdigitr....r
-00000ad0: 3100 0000 da03 696e 7472 0200 0000 da05  1.....intr......
-00000ae0: 6465 6275 67da 0570 7269 6e74 da03 7379  debug..print..sy
-00000af0: 73da 0465 7869 7429 0fda 056e 616d 6573  s..exit)...names
-00000b00: da0c 6172 675f 6c6f 6361 7469 6f6e da0d  ..arg_location..
-00000b10: 7468 655f 696e 745f 7661 6c75 6572 2c00  the_int_valuer,.
-00000b20: 0000 da09 6172 6775 6d65 6e74 7372 3200  ....argumentsr2.
-00000b30: 0000 5a08 7468 655f 6c69 7374 5a09 7468  ..Z.the_listZ.th
-00000b40: 655f 7469 746c 65da 0369 6478 da07 7275  e_title..idx..ru
-00000b50: 6e6e 696e 675a 0c74 6869 735f 656c 656d  nningZ.this_elem
-00000b60: 656e 745a 0c6e 6578 745f 656c 656d 656e  entZ.next_elemen
-00000b70: 745a 0f65 7661 6c75 6174 6564 5f76 616c  tZ.evaluated_val
-00000b80: 7565 da09 6572 726f 725f 6d73 67da 036d  ue..error_msg..m
-00000b90: 7367 7204 0000 0072 0400 0000 7208 0000  sgr....r....r...
-00000ba0: 00da 1070 726f 6365 7373 5f78 6d6c 5f6c  ...process_xml_l
-00000bb0: 6973 748f 0000 0073 7200 0000 0c02 0802  ist....sr.......
-00000bc0: 0801 0401 0401 0403 1001 0801 0801 1002  ................
-00000bd0: 0801 0801 1201 0201 0427 0cdb 0201 0424  .........'.....$
-00000be0: 02db 0802 1001 0801 0201 0801 04ff 0e03  ................
-00000bf0: 0a01 0201 041b 08e6 1001 0c02 1601 1801  ................
-00000c00: 0a01 0209 040b 0cef 0201 04ff 02ff 0a04  ................
-00000c10: 0801 0a01 0201 040b 02f9 0201 04ff 0201  ................
-00000c20: 04ff 0203 04fb 0a07 0801 04d1 0430 7246  .............0rF
-00000c30: 0000 0063 0300 0000 0000 0000 0000 0000  ...c............
-00000c40: 0900 0000 0800 0000 4300 0000 73ca 0000  ........C...s...
-00000c50: 0067 007d 037c 0044 005d 5c7d 047c 046a  .g.}.|.D.]\}.|.j
-00000c60: 0064 016b 0272 607c 046a 01a0 0264 02a1  .d.k.r`|.j...d..
-00000c70: 017d 057c 0144 005d 4c7d 067c 067c 056b  .}.|.D.]L}.|.|.k
-00000c80: 0272 5f7c 01a0 037c 06a1 017d 0764 037d  .r_|...|...}.d.}
-00000c90: 087c 046a 01a0 0264 04a1 0164 0075 0172  .|.j...d...d.u.r
-00000ca0: 2f7c 046a 01a0 0264 04a1 017d 086e 0d7c  /|.j...d...}.n.|
-00000cb0: 04a0 0464 05a1 0164 0075 0172 3c7c 04a0  ...d...d.u.r<|..
-00000cc0: 0464 05a1 016a 057d 087c 0872 5a74 067c  .d...j.}.|.rZt.|
-00000cd0: 027c 0719 0083 0174 0775 0072 4f74 087c  .|.....t.u.rOt.|
-00000ce0: 027c 077c 087c 037c 0183 0501 006e 097c  .|.|.|.|.....n.|
-00000cf0: 03a0 097c 027c 0719 007c 0817 00a1 0101  ...|.|...|......
-00000d00: 0001 006e 067c 03a0 0964 03a1 0101 0071  ...n.|...d.....q
-00000d10: 1371 0474 0a7c 0383 0153 0029 064e da03  .q.t.|...S.).N..
-00000d20: 496e 7472 0300 0000 7223 0000 00da 0376  Intr....r#.....v
-00000d30: 616c da03 7661 7229 0b72 0a00 0000 720b  al..var).r....r.
-00000d40: 0000 0072 0c00 0000 da05 696e 6465 7872  ...r......indexr
-00000d50: 2400 0000 7225 0000 00da 0474 7970 65da  $...r%.....type.
-00000d60: 046c 6973 7472 4600 0000 720d 0000 0072  .listrF...r....r
-00000d70: 2e00 0000 2909 7210 0000 0072 4100 0000  ....).r....rA...
-00000d80: 723e 0000 0072 2c00 0000 7212 0000 00da  r>...r,...r.....
-00000d90: 0774 6865 5f61 7267 da03 6172 6772 3f00  .the_arg..argr?.
-00000da0: 0000 7240 0000 0072 0400 0000 7204 0000  ..r@...r....r...
-00000db0: 0072 0800 0000 da1d 6765 745f 786d 6c5f  .r......get_xml_
-00000dc0: 696e 745f 6172 6775 6d65 6e74 5f74 6f5f  int_argument_to_
-00000dd0: 7661 6c75 65d8 0000 0073 4000 0000 0401  value....s@.....
-00000de0: 0802 0a01 0c01 0801 0801 0a01 0401 1001  ................
-00000df0: 0601 0201 06ff 0e03 0c01 0401 1002 0201  ................
-00000e00: 0201 0201 0201 0201 0201 06fb 0408 0a01  ................
-00000e10: 04ff 0403 0402 0201 04ff 0480 0804 724f  ..............rO
-00000e20: 0000 00da 0672 6574 7572 6e63 0300 0000  .....returnc....
-00000e30: 0000 0000 0000 0000 0800 0000 0600 0000  ................
-00000e40: 4300 0000 737a 0000 0067 007d 037c 0044  C...sz...g.}.|.D
-00000e50: 005d 347d 047c 046a 0064 016b 0272 387c  .]4}.|.j.d.k.r8|
-00000e60: 046a 01a0 0264 02a1 017d 057c 0144 005d  .j...d...}.|.D.]
-00000e70: 247d 067c 067c 056b 0272 377c 01a0 037c  $}.|.|.k.r7|...|
-00000e80: 06a1 017d 077c 046a 0464 0075 0172 307c  ...}.|.j.d.u.r0|
-00000e90: 03a0 057c 027c 0719 007c 046a 0417 0064  ...|.|...|.j...d
-00000ea0: 0317 00a1 0101 006e 057c 03a0 0564 04a1  .......n.|...d..
-00000eb0: 0101 0001 006e 0171 1371 0474 067c 0383  .....n.q.q.t.|..
-00000ec0: 0153 0029 054e da03 5374 7272 0300 0000  .S.).N..Strr....
-00000ed0: 7229 0000 0072 2300 0000 2907 720a 0000  r)...r#...).r...
-00000ee0: 0072 0b00 0000 720c 0000 0072 4a00 0000  .r....r....rJ...
-00000ef0: 7225 0000 0072 0d00 0000 722e 0000 0029  r%...r....r....)
-00000f00: 0872 1000 0000 7241 0000 0072 3e00 0000  .r....rA...r>...
-00000f10: 722c 0000 0072 1200 0000 724d 0000 0072  r,...r....rM...r
-00000f20: 4e00 0000 723f 0000 0072 0400 0000 7204  N...r?...r....r.
-00000f30: 0000 0072 0800 0000 da1d 6765 745f 786d  ...r......get_xm
-00000f40: 6c5f 7374 725f 6172 6775 6d65 6e74 5f74  l_str_argument_t
-00000f50: 6f5f 7661 6c75 6504 0100 0073 1c00 0000  o_value....s....
-00000f60: 0401 0801 0a01 0c01 0801 0801 0a01 0a01  ................
-00000f70: 1a01 0a02 0401 02fa 0280 0807 7252 0000  ............rR..
-00000f80: 0063 0200 0000 0000 0000 0000 0000 0f00  .c..............
-00000f90: 0000 0b00 0000 4300 0000 7336 0100 0064  ......C...s6...d
-00000fa0: 017c 0164 0219 0017 0064 0317 007d 0264  .|.d.....d...}.d
-00000fb0: 047d 0364 047d 047c 00a0 0064 05a1 016a  .}.d.}.|...d...j
-00000fc0: 017d 057c 00a0 0064 06a1 0164 0075 0172  .}.|...d...d.u.r
-00000fd0: 287c 00a0 0064 06a1 016a 017d 067c 0664  (|...d...j.}.|.d
-00000fe0: 0776 0172 2874 027c 067c 0183 027d 037c  .v.r(t.|.|...}.|
-00000ff0: 00a0 0064 08a1 0164 0075 0172 317c 026e  ...d...d.u.r1|.n
-00001000: 0164 047d 077c 00a0 0064 09a1 0164 0075  .d.}.|...d...d.u
-00001010: 0172 9564 0a7d 0864 047d 0967 007d 0a7c  .r.d.}.d.}.g.}.|
-00001020: 00a0 0064 09a1 0144 005d 457d 0b64 0b7c  ...d...D.]E}.d.|
-00001030: 0b6a 0376 0072 537c 0aa0 047c 0b6a 01a1  .j.v.rS|...|.j..
-00001040: 0101 0071 457c 0b6a 0364 0c6b 0272 8a7c  ...qE|.j.d.k.r.|
-00001050: 0564 0d6b 0372 8a74 057c 0b83 015c 037d  .d.k.r.t.|...\.}
-00001060: 0c7d 0d7d 0e7c 0864 0a6b 0372 727c 0a7c  .}.}.|.d.k.rr|.|
-00001070: 0864 0e18 0019 00a0 06a1 009b 0064 0f9d  .d...........d..
-00001080: 027d 097c 049b 0064 017c 0164 1019 009b  .}.|...d.|.d....
-00001090: 0064 117c 099b 0064 127c 0c9b 007c 0d9b  .d.|...d.|...|..
-000010a0: 007c 0e9b 0064 139d 0a7d 047c 0864 0e37  .|...d...}.|.d.7
-000010b0: 007d 0871 457c 0564 146b 0272 957c 04a0  .}.qE|.d.k.r.|..
-000010c0: 0764 1564 16a1 027d 047c 047c 0717 007c  .d.d...}.|.|...|
-000010d0: 0317 0053 0029 174e fa16 203c 7370 616e  ...S.).N.. <span
-000010e0: 2073 7479 6c65 203d 2022 636f 6c6f 723a   style = "color:
-000010f0: da15 6469 7361 626c 6564 5f61 6374 696f  ..disabled_actio
-00001100: 6e5f 636f 6c6f 727a 1222 3c2f 7370 616e  n_colorz."</span
-00001110: 3e5b 4449 5341 424c 4544 5d72 2300 0000  >[DISABLED]r#...
-00001120: da04 636f 6465 da05 6c61 6265 6c29 0272  ..code..label).r
-00001130: 2300 0000 da01 0a5a 026f 6eda 0d43 6f6e  #......Z.on..Con
-00001140: 6469 7469 6f6e 4c69 7374 7201 0000 00da  ditionListr.....
-00001150: 0462 6f6f 6cda 0943 6f6e 6469 7469 6f6e  .bool..Condition
-00001160: da02 3337 7227 0000 0072 3600 0000 da16  ..37r'...r6.....
-00001170: 6163 7469 6f6e 5f63 6f6e 6469 7469 6f6e  action_condition
-00001180: 5f63 6f6c 6f72 7a0a 223c 2f73 7061 6e3e  _colorz."</span>
-00001190: 2028 7a0f 636f 6e64 6974 696f 6e3a 2020   (z.condition:  
-000011a0: 4966 20fa 0129 da02 3335 7a0e 636f 6e64  If ..)..35z.cond
-000011b0: 6974 696f 6e3a 2020 4966 7a0e 3c65 6d3e  ition:  Ifz.<em>
-000011c0: 554e 5449 4c3c 2f65 6d3e 2908 7224 0000  UNTIL</em>).r$..
-000011d0: 0072 2500 0000 da0b 636c 6561 6e5f 6c61  .r%.....clean_la
-000011e0: 6265 6c72 0a00 0000 720d 0000 0072 2600  belr....r....r&.
-000011f0: 0000 da05 7570 7065 72da 0772 6570 6c61  ....upper..repla
-00001200: 6365 290f 7212 0000 00da 0863 6f6c 6f72  ce).r......color
-00001210: 6d61 705a 1464 6973 6162 6c65 645f 6163  mapZ.disabled_ac
-00001220: 7469 6f6e 5f68 746d 6c5a 0a74 6173 6b5f  tion_htmlZ.task_
-00001230: 6c61 6265 6c5a 0f74 6173 6b5f 636f 6e64  labelZ.task_cond
-00001240: 6974 696f 6e73 5a0f 7468 655f 6163 7469  itionsZ.the_acti
-00001250: 6f6e 5f63 6f64 65da 036c 626c 5a0f 6163  on_code..lblZ.ac
-00001260: 7469 6f6e 5f64 6973 6162 6c65 645a 0f63  tion_disabledZ.c
-00001270: 6f6e 6469 7469 6f6e 5f63 6f75 6e74 5a11  ondition_countZ.
-00001280: 626f 6f6c 6561 6e5f 746f 5f69 6e6a 6563  boolean_to_injec
-00001290: 745a 0862 6f6f 6c65 616e 73da 0863 6869  tZ.booleans..chi
-000012a0: 6c64 7265 6e5a 0773 7472 696e 6731 da08  ldrenZ.string1..
-000012b0: 6f70 6572 6174 6f72 5a07 7374 7269 6e67  operatorZ.string
-000012c0: 3272 0400 0000 7204 0000 0072 0800 0000  2r....r....r....
-000012d0: da1c 6765 745f 6c61 6265 6c5f 6469 7361  ..get_label_disa
-000012e0: 626c 6564 5f63 6f6e 6469 7469 6f6e 1701  bled_condition..
-000012f0: 0000 7358 0000 0002 0206 0102 ff02 0202  ..sX............
-00001300: fe02 ff04 0604 010c 010e 010c 0108 030a  ................
-00001310: 0116 020e 0104 0104 0104 010e 010a 010e  ................
-00001320: 0112 010e 0108 0116 0106 0206 0104 ff02  ................
-00001330: 0204 fe02 0202 fe02 0202 fe02 0206 fe02  ................
-00001340: ff08 0502 8008 0104 0104 0104 ff0c 0472  ...............r
-00001350: 6600 0000 6302 0000 0000 0000 0000 0000  f...c...........
-00001360: 0004 0000 0004 0000 0043 0000 0073 7c00  .........C...s|.
-00001370: 0000 7c00 a000 6401 6402 a102 7d00 7c00  ..|...d.d...}.|.
-00001380: a000 6403 6402 a102 7d00 7c00 a000 6404  ..d.d...}.|...d.
-00001390: 6402 a102 7d00 7c00 a000 6405 6403 a102  d...}.|...d.d...
-000013a0: 7d00 7c00 a001 6406 a101 7d02 7c02 6407  }.|...d...}.|.d.
-000013b0: 6b04 7234 7c00 a001 6408 a101 7d03 7c02  k.r4|...d...}.|.
-000013c0: 7c03 6b04 7234 7c00 9b00 6409 7c01 640a  |.k.r4|...d.|.d.
-000013d0: 1900 9b00 640b 9d04 7d00 640c 7c01 640a  ....d...}.d.|.d.
-000013e0: 1900 9b00 640d 7c00 9b00 9d04 5300 290e  ....d.|.....S.).
-000013f0: 4e72 5700 0000 7223 0000 00fa 073c 2f66  NrW...r#.....</f
-00001400: 6f6e 743e 7a06 3c2f 6269 673e 7a0e 3c2f  ont>z.</big>z.</
-00001410: 666f 6e74 3e3c 2f66 6f6e 743e fa05 3c66  font></font>..<f
-00001420: 6f6e 7472 0100 0000 7a05 2f66 6f6e 747a  ontr....z./fontz
-00001430: 0d3c 666f 6e74 2022 636f 6c6f 723a da12  .<font "color:..
-00001440: 6163 7469 6f6e 5f6c 6162 656c 5f63 6f6c  action_label_col
-00001450: 6f72 7a08 223c 2f66 6f6e 743e 7253 0000  orz."</font>rS..
-00001460: 007a 1722 3c2f 7370 616e 3e2e 2e2e 7769  .z."</span>...wi
-00001470: 7468 206c 6162 656c 3a20 2902 7261 0000  th label: ).ra..
-00001480: 00da 0563 6f75 6e74 2904 7263 0000 0072  ...count).rc...r
-00001490: 6200 0000 5a0a 666f 6e74 5f63 6f75 6e74  b...Z.font_count
-000014a0: 5a0e 656e 645f 666f 6e74 5f63 6f75 6e74  Z.end_font_count
-000014b0: 7204 0000 0072 0400 0000 7208 0000 0072  r....r....r....r
-000014c0: 5f00 0000 4501 0000 731a 0000 000c 020c  _...E...s.......
-000014d0: 010c 010c 010a 0108 020a 0208 0114 010c  ................
-000014e0: 0302 0104 ff02 ff72 5f00 0000 6304 0000  .......r_...c...
-000014f0: 0000 0000 0000 0000 0006 0000 0004 0000  ................
-00001500: 0043 0000 0073 b200 0000 7c01 722f 7400  .C...s....|.r/t.
-00001510: 7c00 7c02 8302 7d04 6401 7c04 7600 7214  |.|...}.d.|.v.r.
-00001520: 6402 7c04 7601 7214 7c04 9b00 6402 9d02  d.|.v.r.|...d...
-00001530: 7d04 6403 7c04 7600 7221 6404 7c04 7601  }.d.|.v.r!d.|.v.
-00001540: 7221 7c04 9b00 6402 9d02 7d04 6405 7c04  r!|...d...}.d.|.
-00001550: 7600 722e 6406 7c04 7601 722e 7c04 9b00  v.r.d.|.v.r.|...
-00001560: 6406 9d02 7d04 6e02 6407 7d04 7c03 6408  d...}.n.d.}.|.d.
-00001570: 1900 7244 7c01 7244 7c04 9b00 6409 9d02  ..rD|.rD|...d...
-00001580: 7c00 a001 640a a101 6a02 1700 640b 1700  |...d...j...d...
-00001590: 7d04 7c00 a001 640c a101 7d05 7c05 6400  }.|...d...}.|.d.
-000015a0: 7501 7257 7c05 6a02 640d 6b02 7257 640e  u.rW|.j.d.k.rWd.
-000015b0: 7c04 9b00 9d02 7d04 7c04 5300 290f 4e72  |.....}.|.S.).Nr
-000015c0: 6800 0000 7267 0000 007a 0826 6c74 3b66  h...rg...z.&lt;f
-000015d0: 6f6e 747a 0d26 6c74 3b2f 666f 6e74 2667  ontz.&lt;/font&g
-000015e0: 743b 7a03 3c62 3e7a 043c 2f62 3e72 2300  t;z.<b>z.</b>r#.
-000015f0: 0000 723a 0000 007a 2f3c 7370 616e 2073  ..r:...z/<span s
-00001600: 7479 6c65 3d22 636f 6c6f 723a 5265 6422  tyle="color:Red"
-00001610: 3c2f 7370 616e 3e26 6e62 7370 3b26 6e62  </span>&nbsp;&nb
-00001620: 7370 3b63 6f64 653a 7255 0000 00fa 012d  sp;code:rU.....-
-00001630: da02 7365 da05 6661 6c73 657a 1c20 5b43  ..se..falsez. [C
-00001640: 6f6e 7469 6e75 6520 5461 736b 2041 6674  ontinue Task Aft
-00001650: 6572 2045 7272 6f72 5d29 0372 6600 0000  er Error]).rf...
-00001660: 7224 0000 0072 2500 0000 2906 da0b 636f  r$...r%...)...co
-00001670: 6465 5f61 6374 696f 6eda 0b61 6374 696f  de_action..actio
-00001680: 6e5f 7479 7065 7262 0000 00da 0c70 726f  n_typerb.....pro
-00001690: 6772 616d 5f61 7267 73da 0b65 7874 7261  gram_args..extra
-000016a0: 5f73 7475 6666 7212 0000 0072 0400 0000  _stuffr....r....
-000016b0: 7204 0000 0072 0800 0000 da0f 6765 745f  r....r......get_
-000016c0: 6578 7472 615f 7374 7566 665e 0100 0073  extra_stuff^...s
-000016d0: 3600 0000 0202 02ff 0203 0401 04ff 1004  6...............
-000016e0: 0a02 1002 0a02 1002 0a02 0280 0402 0602  ................
-000016f0: 02ff 0201 02ff 0804 0a01 02ff 0202 02fe  ................
-00001700: 02ff 0a07 1201 0a01 0401 7272 0000 0063  ..........rr...c
-00001710: 0400 0000 0000 0000 0000 0000 0900 0000  ................
-00001720: 0500 0000 4300 0000 73ba 0000 0074 007c  ....C...s....t.|
-00001730: 007c 017c 027c 0383 047d 0464 015c 037d  .|.|.|...}.d.\.}
-00001740: 057d 067d 077c 00a0 0164 02a1 017d 087c  .}.}.|...d...}.|
-00001750: 0864 0075 0172 577c 086a 0264 026b 0272  .d.u.rW|.j.d.k.r
-00001760: 577c 08a0 0164 03a1 0164 0075 0072 2764  W|...d...d.u.r'd
-00001770: 0464 0464 047c 0466 0453 007c 08a0 0164  .d.d.|.f.S.|...d
-00001780: 03a1 016a 0364 0075 0172 3764 057c 08a0  ...j.d.u.r7d.|..
-00001790: 0164 03a1 016a 0317 007d 057c 08a0 0164  .d...j...}.|...d
-000017a0: 06a1 016a 0364 0075 0172 4764 077c 08a0  ...j.d.u.rGd.|..
-000017b0: 0164 06a1 016a 0317 007d 067c 08a0 0164  .d...j...}.|...d
-000017c0: 08a1 016a 0364 0075 0172 5764 097c 08a0  ...j.d.u.rWd.|..
-000017d0: 0164 08a1 016a 0317 007d 077c 057c 067c  .d...j...}.|.|.|
-000017e0: 077c 0466 0453 0029 0a4e 2903 7223 0000  .|.f.S.).N).r#..
-000017f0: 0072 2300 0000 7223 0000 00da 0341 7070  .r#...r#.....App
-00001800: 5a08 6170 7043 6c61 7373 7223 0000 007a  Z.appClassr#...z
-00001810: 0643 6c61 7373 3a5a 0661 7070 506b 677a  .Class:Z.appPkgz
-00001820: 0a2c 2050 6163 6b61 6765 3a72 5600 0000  ., Package:rV...
-00001830: 7a06 2c20 4170 703a 2904 7272 0000 0072  z., App:).rr...r
-00001840: 2400 0000 720a 0000 0072 2500 0000 2909  $...r....r%...).
-00001850: da0a 636f 6465 5f63 6869 6c64 726f 0000  ..code_childro..
-00001860: 0072 6200 0000 7270 0000 0072 7100 0000  .rb...rp...rq...
-00001870: 5a09 6170 705f 636c 6173 735a 0761 7070  Z.app_classZ.app
-00001880: 5f70 6b67 5a03 6170 7072 1200 0000 7204  _pkgZ.appr....r.
-00001890: 0000 0072 0400 0000 7208 0000 00da 0f67  ...r....r......g
-000018a0: 6574 5f61 7070 5f64 6574 6169 6c73 8601  et_app_details..
-000018b0: 0000 731a 0000 000e 010a 010a 0112 010e  ..s.............
-000018c0: 010c 0110 0110 0110 0110 0110 0110 010c  ................
-000018d0: 0172 7500 0000 2917 5a17 6d61 7074 6173  .ru...).Z.maptas
-000018e0: 6b65 722e 7372 632e 7368 656c 6c73 6f72  ker.src.shellsor
-000018f0: 74da 0373 7263 5a09 7368 656c 6c73 6f72  t..srcZ.shellsor
-00001900: 7472 0e00 0000 da16 6d61 7074 6173 6b65  tr......maptaske
-00001910: 722e 7372 632e 7379 7363 6f6e 7374 7202  r.src.sysconstr.
-00001920: 0000 00da 0272 6572 3c00 0000 da07 636f  .....rer<.....co
-00001930: 6d70 696c 65da 0770 6174 7465 726e 7213  mpile..patternr.
-00001940: 0000 0072 1500 0000 7226 0000 0072 2e00  ...r....r&...r..
-00001950: 0000 7231 0000 0072 4600 0000 724f 0000  ..r1...rF...rO..
-00001960: 0072 4c00 0000 7252 0000 0072 6600 0000  .rL...rR...rf...
-00001970: 725f 0000 0072 7200 0000 7275 0000 0072  r_...rr...ru...r
-00001980: 0400 0000 7204 0000 0072 0400 0000 7208  ....r....r....r.
-00001990: 0000 00da 083c 6d6f 6475 6c65 3e01 0000  .....<module>...
-000019a0: 0073 2200 0000 120d 0c01 0801 0801 0a02  .s".............
-000019b0: 080e 081c 0807 0820 0816 0815 0849 0e2c  ....... .....I.,
-000019c0: 0813 082e 0819 0c28                      .......(
+00000020: 0002 0000 0040 0000 0073 8000 0000 6400  .....@...s....d.
+00000030: 6401 6c00 5a00 6400 6402 6c01 6d02 5a02  d.l.Z.d.d.l.m.Z.
+00000040: 0100 6400 6403 6c03 6d04 5a04 0100 6400  ..d.d.l.m.Z...d.
+00000050: 6404 6c03 6d05 5a05 0100 6405 6406 8400  d.l.m.Z...d.d...
+00000060: 5a06 6407 6408 8400 5a07 6409 640a 8400  Z.d.d...Z.d.d...
+00000070: 5a08 640b 640c 8400 5a09 640d 640e 8400  Z.d.d...Z.d.d...
+00000080: 5a0a 640f 6410 8400 5a0b 6411 6412 8400  Z.d.d...Z.d.d...
+00000090: 5a0c 6413 6414 8400 5a0d 6415 6416 8400  Z.d.d...Z.d.d...
+000000a0: 5a0e 6417 6418 8400 5a0f 6401 5300 2919  Z.d.d...Z.d.S.).
+000000b0: e900 0000 004e 2901 da0a 7368 656c 6c5f  .....N)...shell_
+000000c0: 736f 7274 2901 da06 6c6f 6767 6572 2901  sort)...logger).
+000000d0: da0b 464f 4e54 5f54 4f5f 5553 4563 0200  ..FONT_TO_USEc..
+000000e0: 0000 0000 0000 0000 0000 0800 0000 0600  ................
+000000f0: 0000 4300 0000 739e 0000 0067 0067 0067  ..C...s....g.g.g
+00000100: 0003 0302 037d 027d 037d 0464 017d 057c  .....}.}.}.d.}.|
+00000110: 0044 005d 187d 067c 066a 007c 0176 0072  .D.].}.|.j.|.v.r
+00000120: 1471 0c7c 066a 01a0 0264 02a1 017d 077c  .q.|.j...d...}.|
+00000130: 0764 0075 0072 1f71 0c7c 04a0 037c 06a1  .d.u.r.q.|...|..
+00000140: 0101 0071 0c7c 0472 4a74 047c 0464 0364  ...q.|.rJt.|.d.d
+00000150: 0483 0301 007c 0444 005d 117d 067c 03a0  .....|.D.].}.|..
+00000160: 037c 066a 00a1 0101 007c 02a0 037c 066a  .|.j.....|...|.j
+00000170: 01a0 0264 02a1 01a1 0101 0071 2f64 0564  ...d.......q/d.d
+00000180: 0684 0074 057c 0283 0144 0083 017d 057c  ...t.|...D...}.|
+00000190: 027c 037c 0566 0353 0029 074e 7201 0000  .|.|.f.S.).Nr...
+000001a0: 00da 0273 7254 4663 0100 0000 0000 0000  ...srTFc........
+000001b0: 0000 0000 0300 0000 0400 0000 5300 0000  ............S...
+000001c0: 7318 0000 0067 007c 005d 085c 027d 017d  s....g.|.].\.}.}
+000001d0: 0274 007c 0183 0191 0271 0253 00a9 0029  .t.|.....q.S...)
+000001e0: 01da 0373 7472 2903 da02 2e30 5a03 696e  ...str)....0Z.in
+000001f0: 64da 0178 7206 0000 0072 0600 0000 fa75  d..xr....r.....u
+00000200: 2f55 7365 7273 2f6d 696b 7275 6269 6e2f  /Users/mikrubin/
+00000210: 4c69 6272 6172 792f 436c 6f75 6453 746f  Library/CloudSto
+00000220: 7261 6765 2f47 6f6f 676c 6544 7269 7665  rage/GoogleDrive
+00000230: 2d6d 696b 7275 6269 6e40 676d 6169 6c2e  -mikrubin@gmail.
+00000240: 636f 6d2f 4d79 2044 7269 7665 2f50 7974  com/My Drive/Pyt
+00000250: 686f 6e2f 6d61 7074 6173 6b65 722f 6d61  hon/maptasker/ma
+00000260: 7074 6173 6b65 722f 7372 632f 6163 7469  ptasker/src/acti
+00000270: 6f6e 2e70 79da 0a3c 6c69 7374 636f 6d70  on.py..<listcomp
+00000280: 3e32 0000 0073 0600 0000 0600 0c01 06ff  >2...s..........
+00000290: 7a1c 6765 745f 6172 6773 2e3c 6c6f 6361  z.get_args.<loca
+000002a0: 6c73 3e2e 3c6c 6973 7463 6f6d 703e 2906  ls>.<listcomp>).
+000002b0: da03 7461 67da 0661 7474 7269 62da 0367  ..tag..attrib..g
+000002c0: 6574 da06 6170 7065 6e64 7202 0000 00da  et..appendr.....
+000002d0: 0965 6e75 6d65 7261 7465 2908 da06 6163  .enumerate)...ac
+000002e0: 7469 6f6e 5a0b 6967 6e6f 7265 5f6c 6973  tionZ.ignore_lis
+000002f0: 74da 0861 7267 5f6c 6973 745a 0974 7970  t..arg_listZ.typ
+00000300: 655f 6c69 7374 5a0b 6d61 7374 6572 5f6c  e_listZ.master_l
+00000310: 6973 745a 0861 7267 5f6e 756d 73da 0563  istZ.arg_nums..c
+00000320: 6869 6c64 5a0a 6163 7469 6f6e 5f61 7267  hildZ.action_arg
+00000330: 7206 0000 0072 0600 0000 720a 0000 00da  r....r....r.....
+00000340: 0867 6574 5f61 7267 7320 0000 0073 2400  .get_args ...s$.
+00000350: 0000 1001 0401 0801 0a01 0201 0c01 0801  ................
+00000360: 0201 0c02 0402 0c02 0801 0c01 1401 0601  ................
+00000370: 0601 06ff 0a04 7214 0000 0063 0300 0000  ......r....c....
+00000380: 0000 0000 0000 0000 0300 0000 0200 0000  ................
+00000390: 4300 0000 7310 0000 007c 0064 016b 0272  C...s....|.d.k.r
+000003a0: 067c 0153 007c 0253 0029 024e da01 3072  .|.S.|.S.).N..0r
+000003b0: 0600 0000 2903 5a09 7468 655f 7661 6c75  ....).Z.the_valu
+000003c0: 655a 0e69 665f 7a65 726f 5f73 7472 696e  eZ.if_zero_strin
+000003d0: 675a 1269 665f 6e6f 745f 7a65 726f 5f73  gZ.if_not_zero_s
+000003e0: 7472 696e 6772 0600 0000 7206 0000 0072  tringr....r....r
+000003f0: 0a00 0000 da0c 6966 5f7a 6572 6f5f 656c  ......if_zero_el
+00000400: 7365 3c00 0000 7302 0000 0010 0172 1600  se<...s......r..
+00000410: 0000 6301 0000 0000 0000 0000 0000 0006  ..c.............
+00000420: 0000 000d 0000 0043 0000 0073 7200 0000  .......C...sr...
+00000430: 6401 6402 6403 6404 6405 6406 6407 6408  d.d.d.d.d.d.d.d.
+00000440: 6401 6409 640a 640b 640c 9c0c 7d01 7c00  d.d.d.d.d...}.|.
+00000450: a000 640d a101 6a01 7d02 7c00 a000 640e  ..d...j.}.|...d.
+00000460: a101 6a01 7d03 7c01 7c03 1900 7d04 640f  ..j.}.|.|...}.d.
+00000470: 7c04 7601 7232 7c00 a000 6410 a101 6a01  |.v.r2|...d...j.
+00000480: 6400 7501 7232 7c00 a000 6410 a101 6a01  d.u.r2|...d...j.
+00000490: 7d05 6e02 6411 7d05 7c02 7c04 7c05 6603  }.n.d.}.|.|.|.f.
+000004a0: 5300 2912 4e7a 0320 3d20 7a05 204e 4551  S.).Nz. = z. NEQ
+000004b0: 207a 0320 7e20 7a04 2021 7e20 7a05 2021   z. ~ z. !~ z. !
+000004c0: 7e52 207a 0420 7e52 207a 0320 3c20 7a03  ~R z. ~R z. < z.
+000004d0: 203e 207a 0420 213d 207a 0720 6973 2073   > z. != z. is s
+000004e0: 6574 7a08 206e 6f74 2073 6574 290c 7215  etz. not set).r.
+000004f0: 0000 00da 0131 da01 32da 0133 da01 34da  .....1..2..3..4.
+00000500: 0135 da01 36da 0137 da01 38da 0139 5a02  .5..6..7..8..9Z.
+00000510: 3132 5a02 3133 5a03 6c68 73da 026f 70da  12Z.13Z.lhs..op.
+00000520: 0373 6574 5a03 7268 73da 0029 02da 0466  .setZ.rhs..)...f
+00000530: 696e 64da 0474 6578 7429 0672 1300 0000  ind..text).r....
+00000540: 5a0e 7468 655f 6f70 6572 6174 696f 6e73  Z.the_operations
+00000550: 5a0c 6669 7273 745f 7374 7269 6e67 5a09  Z.first_stringZ.
+00000560: 6f70 6572 6174 696f 6e5a 0d74 6865 5f6f  operationZ.the_o
+00000570: 7065 7261 7469 6f6e 5a0d 7365 636f 6e64  perationZ.second
+00000580: 5f73 7472 696e 6772 0600 0000 7206 0000  _stringr....r...
+00000590: 0072 0a00 0000 da12 6576 616c 7561 7465  .r......evaluate
+000005a0: 5f63 6f6e 6469 7469 6f6e 4300 0000 7328  _conditionC...s(
+000005b0: 0000 0002 0202 0102 0102 0102 0102 0102  ................
+000005c0: 0102 0102 0102 0102 0102 0106 f40c 0f0c  ................
+000005d0: 0108 0118 020e 0204 020a 0272 2500 0000  ...........r%...
+000005e0: 6301 0000 0000 0000 0000 0000 0003 0000  c...............
+000005f0: 0005 0000 0043 0000 0073 7400 0000 7400  .....C...st...t.
+00000600: 7c00 8301 6401 1800 7d01 7c01 6402 6b04  |...d...}.|.d.k.
+00000610: 7238 7401 7c00 8301 4400 5d29 7d02 7c02  r8t.|...D.])}.|.
+00000620: 6403 6b02 7219 7c01 6401 1800 7d01 710e  d.k.r.|.d...}.q.
+00000630: 7c02 7400 7c02 8301 6404 1800 6400 8502  |.t.|...d...d...
+00000640: 1900 6405 6b02 7235 7c02 6400 7400 7c02  ..d.k.r5|.d.t.|.
+00000650: 8301 6404 1800 8502 1900 7c00 7c01 3c00  ..d.......|.|.<.
+00000660: 7c00 0200 0100 5300 0100 7c00 5300 7c00  |.....S...|.S.|.
+00000670: 5300 2906 4ee9 0100 0000 7201 0000 0072  S.).N.....r....r
+00000680: 2200 0000 e902 0000 00fa 022c 2029 02da  ".........., )..
+00000690: 036c 656e da08 7265 7665 7273 6564 2903  .len..reversed).
+000006a0: da0d 6d61 7463 685f 7265 7375 6c74 735a  ..match_resultsZ
+000006b0: 106c 6173 745f 7661 6c69 645f 656e 7472  .last_valid_entr
+000006c0: 79da 0469 7465 6d72 0600 0000 7206 0000  y..itemr....r...
+000006d0: 0072 0a00 0000 da13 6472 6f70 5f74 7261  .r......drop_tra
+000006e0: 696c 696e 675f 636f 6d6d 6163 0000 0073  iling_commac...s
+000006f0: 1400 0000 0c01 0801 0c01 0801 0a01 1801  ................
+00000700: 1801 0801 0202 0801 722d 0000 0063 0000  ........r-...c..
+00000710: 0000 0000 0000 0000 0000 0300 0000 0600  ................
+00000720: 0000 4700 0000 736c 0000 0067 007d 017c  ..G...sl...g.}.|
+00000730: 0044 005d 2f7d 027c 0264 0119 0072 1c7c  .D.]/}.|.d...r.|
+00000740: 0264 0219 0064 036b 0372 1c7c 01a0 007c  .d...d.k.r.|...|
+00000750: 0264 0419 007c 0264 0219 0017 00a1 0101  .d...|.d........
+00000760: 0071 047c 0264 0119 0073 267c 0264 0219  .q.|.d...s&|.d..
+00000770: 0064 056b 0372 2c7c 01a0 0064 03a1 0101  .d.k.r,|...d....
+00000780: 0071 047c 01a0 007c 0264 0419 00a1 0101  .q.|...|.d......
+00000790: 0071 047c 0153 0029 064e 7201 0000 0072  .q.|.S.).Nr....r
+000007a0: 2600 0000 7222 0000 0072 2700 0000 7217  &...r"...r'...r.
+000007b0: 0000 0029 0172 0f00 0000 2903 da04 6172  ...).r....)...ar
+000007c0: 6773 da07 7265 7375 6c74 7372 2c00 0000  gs..resultsr,...
+000007d0: 7206 0000 0072 0600 0000 720a 0000 00da  r....r....r.....
+000007e0: 1765 7661 6c75 6174 655f 6163 7469 6f6e  .evaluate_action
+000007f0: 5f73 6574 7469 6e67 7900 0000 7310 0000  _settingy...s...
+00000800: 0004 0108 0214 0118 0114 010c 0110 0204  ................
+00000810: 0172 3000 0000 6305 0000 0000 0000 0000  .r0...c.........
+00000820: 0000 000f 0000 0004 0000 0043 0000 0073  ...........C...s
+00000830: a601 0000 6401 6402 6c00 6d01 7d05 0100  ....d.d.l.m.}...
+00000840: 7c00 7c01 1900 7d06 7c06 6401 1900 7d07  |.|...}.|.d...}.
+00000850: 6401 7d08 6403 7d09 7c09 72d1 7c08 6404  d.}.d.}.|.r.|.d.
+00000860: 1700 7402 7c06 8301 1600 7d08 7c06 7c08  ..t.|.....}.|.|.
+00000870: 1900 7d0a 7c0a a003 a100 724a 7c08 6404  ..}.|.....rJ|.d.
+00000880: 1700 7402 7c06 8301 1600 7d08 7c06 7c08  ..t.|.....}.|.|.
+00000890: 1900 7d0b 7c0a 7c02 6b02 7240 7c03 a004  ..}.|.|.k.r@|...
+000008a0: 7c07 7c0b 1700 6405 1700 a101 0100 0900  |.|...d.........
+000008b0: 6400 5300 7c08 7402 7c06 8301 6b04 7249  d.S.|.t.|...k.rI
+000008c0: 0900 6400 5300 6e85 7c0a 6406 7600 7270  ..d.S.n.|.d.v.rp
+000008d0: 7c08 6404 1700 7402 7c06 8301 1600 7d08  |.d...t.|.....}.
+000008e0: 7c06 7c08 1900 7d0b 7405 6407 7c02 7c0b  |.|...}.t.d.|.|.
+000008f0: 6703 8301 7d0c 7c0c 6401 1900 9b00 6405  g...}.|.d.....d.
+00000900: 9d02 7d0c 7c03 a004 7c0c a101 0100 0900  ..}.|...|.......
+00000910: 6400 5300 7c0a 6408 6b02 72bc 7c08 6404  d.S.|.d.k.r.|.d.
+00000920: 1700 7402 7c06 8301 1600 7d08 7c06 7c08  ..t.|.....}.|.|.
+00000930: 1900 7c05 7600 72a1 7c05 7c06 7c08 1900  ..|.v.r.|.|.|...
+00000940: 1900 7406 7c02 8301 1900 6701 7d0c 7c06  ..t.|.....g.}.|.
+00000950: 7c08 6409 1800 1900 7c0c 6401 1900 1700  |.d.....|.d.....
+00000960: 6405 1700 7d0c 7c03 a004 7c0c a101 0100  d...}.|...|.....
+00000970: 0900 6400 5300 640a 7c06 7c08 1900 9b00  ..d.S.d.|.|.....
+00000980: 640b 7c00 9b00 9d04 7d0d 7407 a008 7c0d  d.|.....}.t...|.
+00000990: a101 0100 7409 7c0d 8301 0100 740a a00b  ....t.|.....t...
+000009a0: 6404 a101 0100 0900 6400 5300 640c 7c0a  d.......d.S.d.|.
+000009b0: 9b00 640d 7c04 9b00 9d04 7c00 6602 7d0e  ..d.|.....|.f.}.
+000009c0: 7407 a008 7c0e a101 0100 740b 640e 8301  t...|.....t.d...
+000009d0: 0100 7c09 7314 6400 5300 290f 4e72 0100  ..|.s.d.S.).Nr..
+000009e0: 0000 2901 da0d 6c6f 6f6b 7570 5f76 616c  ..)...lookup_val
+000009f0: 7565 7354 7226 0000 0072 2800 0000 2902  uesTr&...r(...).
+00000a00: da01 65da 0269 6646 da01 6c72 2700 0000  ..e..ifF..lr'...
+00000a10: 7a0f 5072 6f67 7261 6d20 6572 726f 723a  z.Program error:
+00000a20: 207a 2b20 6973 206e 6f74 2069 6e20 6163   z+ is not in ac
+00000a30: 7469 6f6e 7420 286c 6f6f 6b75 7020 7461  tiont (lookup ta
+00000a40: 626c 6529 2066 6f72 206e 616d 653a 7a33  ble) for name:z3
+00000a50: 6765 745f 786d 6c5f 696e 745f 6172 6775  get_xml_int_argu
+00000a60: 6d65 6e74 5f74 6f5f 7661 6c75 6520 6661  ment_to_value fa
+00000a70: 696c 6564 2d20 7468 6973 5f65 6c65 6d65  iled- this_eleme
+00000a80: 6e74 3afa 0120 e908 0000 0029 0c5a 156d  nt:.. .....).Z.m
+00000a90: 6170 7461 736b 6572 2e73 7263 2e61 6374  aptasker.src.act
+00000aa0: 696f 6e74 7231 0000 0072 2900 0000 da07  iontr1...r).....
+00000ab0: 6973 6469 6769 7472 0f00 0000 7230 0000  isdigitr....r0..
+00000ac0: 00da 0369 6e74 7203 0000 00da 0564 6562  ...intr......deb
+00000ad0: 7567 da05 7072 696e 74da 0373 7973 da04  ug..print..sys..
+00000ae0: 6578 6974 290f da05 6e61 6d65 735a 0c61  exit)...namesZ.a
+00000af0: 7267 5f6c 6f63 6174 696f 6e5a 0d74 6865  rg_locationZ.the
+00000b00: 5f69 6e74 5f76 616c 7565 722b 0000 00da  _int_valuer+....
+00000b10: 0961 7267 756d 656e 7473 7231 0000 005a  .argumentsr1...Z
+00000b20: 0874 6865 5f6c 6973 745a 0974 6865 5f74  .the_listZ.the_t
+00000b30: 6974 6c65 da03 6964 78da 0772 756e 6e69  itle..idx..runni
+00000b40: 6e67 5a0c 7468 6973 5f65 6c65 6d65 6e74  ngZ.this_element
+00000b50: 5a0c 6e65 7874 5f65 6c65 6d65 6e74 5a0f  Z.next_elementZ.
+00000b60: 6576 616c 7561 7465 645f 7661 6c75 65da  evaluated_value.
+00000b70: 0965 7272 6f72 5f6d 7367 da03 6d73 6772  .error_msg..msgr
+00000b80: 0600 0000 7206 0000 0072 0a00 0000 da10  ....r....r......
+00000b90: 7072 6f63 6573 735f 786d 6c5f 6c69 7374  process_xml_list
+00000ba0: 8e00 0000 7372 0000 000c 0208 0208 0104  ....sr..........
+00000bb0: 0104 0104 0310 0108 0108 0110 0208 0108  ................
+00000bc0: 0112 0102 0104 270c db02 0104 2402 db08  ......'.....$...
+00000bd0: 0210 0108 0102 0108 0104 ff0e 030a 0102  ................
+00000be0: 0104 1b08 e610 010c 0216 0118 010a 0102  ................
+00000bf0: 0904 0b0c ef02 0104 ff02 ff0a 0408 010a  ................
+00000c00: 0102 0104 0b02 f902 0104 ff02 0104 ff02  ................
+00000c10: 0304 fb0a 0708 0104 d104 3072 4300 0000  ..........0rC...
+00000c20: 6302 0000 0000 0000 0000 0000 000f 0000  c...............
+00000c30: 000b 0000 0043 0000 0073 3a01 0000 6401  .....C...s:...d.
+00000c40: 7c01 6402 1900 1700 7400 1700 6403 1700  |.d.....t...d...
+00000c50: 7d02 6404 7d03 6404 7d04 7c00 a001 6405  }.d.}.d.}.|...d.
+00000c60: a101 6a02 7d05 7c00 a001 6406 a101 6400  ..j.}.|...d...d.
+00000c70: 7501 722a 7c00 a001 6406 a101 6a02 7d06  u.r*|...d...j.}.
+00000c80: 7c06 6407 7601 722a 7403 7c06 7c01 8302  |.d.v.r*t.|.|...
+00000c90: 7d03 7c00 a001 6408 a101 6400 7501 7233  }.|...d...d.u.r3
+00000ca0: 7c02 6e01 6404 7d07 7c00 a001 6409 a101  |.n.d.}.|...d...
+00000cb0: 6400 7501 7297 640a 7d08 6404 7d09 6700  d.u.r.d.}.d.}.g.
+00000cc0: 7d0a 7c00 a001 6409 a101 4400 5d45 7d0b  }.|...d...D.]E}.
+00000cd0: 640b 7c0b 6a04 7600 7255 7c0a a005 7c0b  d.|.j.v.rU|...|.
+00000ce0: 6a02 a101 0100 7147 7c0b 6a04 640c 6b02  j.....qG|.j.d.k.
+00000cf0: 728c 7c05 640d 6b03 728c 7406 7c0b 8301  r.|.d.k.r.t.|...
+00000d00: 5c03 7d0c 7d0d 7d0e 7c08 640a 6b03 7274  \.}.}.}.|.d.k.rt
+00000d10: 7c0a 7c08 640e 1800 1900 a007 a100 9b00  |.|.d...........
+00000d20: 640f 9d02 7d09 7c04 9b00 6410 7c01 6411  d...}.|...d.|.d.
+00000d30: 1900 9b00 6412 7c09 9b00 6413 7c0c 9b00  ....d.|...d.|...
+00000d40: 7c0d 9b00 7c0e 9b00 6414 9d0a 7d04 7c08  |...|...d...}.|.
+00000d50: 640e 3700 7d08 7147 7c05 6415 6b02 7297  d.7.}.qG|.d.k.r.
+00000d60: 7c04 a008 6416 6417 a102 7d04 7c04 7c07  |...d.d...}.|.|.
+00000d70: 1700 7c03 1700 5300 2918 4e7a 1b20 3c2f  ..|...S.).Nz. </
+00000d80: 7370 616e 3e3c 7370 616e 2073 7479 6c65  span><span style
+00000d90: 3d22 636f 6c6f 723a 5a15 6469 7361 626c  ="color:Z.disabl
+00000da0: 6564 5f61 6374 696f 6e5f 636f 6c6f 727a  ed_action_colorz
+00000db0: 123e 5b44 4953 4142 4c45 445d 3c2f 7370  .>[DISABLED]</sp
+00000dc0: 616e 3e72 2200 0000 da04 636f 6465 da05  an>r".....code..
+00000dd0: 6c61 6265 6c29 0272 2200 0000 da01 0a5a  label).r"......Z
+00000de0: 026f 6eda 0d43 6f6e 6469 7469 6f6e 4c69  .on..ConditionLi
+00000df0: 7374 7201 0000 00da 0462 6f6f 6cda 0943  str......bool..C
+00000e00: 6f6e 6469 7469 6f6e 5a02 3337 7226 0000  onditionZ.37r&..
+00000e10: 0072 3500 0000 7a15 203c 7370 616e 2073  .r5...z. <span s
+00000e20: 7479 6c65 3d20 2263 6f6c 6f72 3a5a 1661  tyle= "color:Z.a
+00000e30: 6374 696f 6e5f 636f 6e64 6974 696f 6e5f  ction_condition_
+00000e40: 636f 6c6f 727a 0b22 3e3c 2f73 7061 6e3e  colorz."></span>
+00000e50: 2028 7a0f 636f 6e64 6974 696f 6e3a 2020   (z.condition:  
+00000e60: 4966 20fa 0129 5a02 3335 7a0e 636f 6e64  If ..)Z.35z.cond
+00000e70: 6974 696f 6e3a 2020 4966 7a0e 3c65 6d3e  ition:  Ifz.<em>
+00000e80: 554e 5449 4c3c 2f65 6d3e 2909 7204 0000  UNTIL</em>).r...
+00000e90: 0072 2300 0000 7224 0000 00da 0b63 6c65  .r#...r$.....cle
+00000ea0: 616e 5f6c 6162 656c 720c 0000 0072 0f00  an_labelr....r..
+00000eb0: 0000 7225 0000 00da 0575 7070 6572 da07  ..r%.....upper..
+00000ec0: 7265 706c 6163 6529 0f72 1300 0000 da08  replace).r......
+00000ed0: 636f 6c6f 726d 6170 5a14 6469 7361 626c  colormapZ.disabl
+00000ee0: 6564 5f61 6374 696f 6e5f 6874 6d6c 5a0a  ed_action_htmlZ.
+00000ef0: 7461 736b 5f6c 6162 656c 5a0f 7461 736b  task_labelZ.task
+00000f00: 5f63 6f6e 6469 7469 6f6e 735a 0f74 6865  _conditionsZ.the
+00000f10: 5f61 6374 696f 6e5f 636f 6465 da03 6c62  _action_code..lb
+00000f20: 6c5a 0f61 6374 696f 6e5f 6469 7361 626c  lZ.action_disabl
+00000f30: 6564 5a0f 636f 6e64 6974 696f 6e5f 636f  edZ.condition_co
+00000f40: 756e 745a 1162 6f6f 6c65 616e 5f74 6f5f  untZ.boolean_to_
+00000f50: 696e 6a65 6374 5a08 626f 6f6c 6561 6e73  injectZ.booleans
+00000f60: da08 6368 696c 6472 656e 5a07 7374 7269  ..childrenZ.stri
+00000f70: 6e67 31da 086f 7065 7261 746f 725a 0773  ng1..operatorZ.s
+00000f80: 7472 696e 6732 7206 0000 0072 0600 0000  tring2r....r....
+00000f90: 720a 0000 00da 1c67 6574 5f6c 6162 656c  r......get_label
+00000fa0: 5f64 6973 6162 6c65 645f 636f 6e64 6974  _disabled_condit
+00000fb0: 696f 6ece 0000 0073 5c00 0000 0202 0601  ion....s\.......
+00000fc0: 02ff 0202 02fe 0203 02fd 02ff 0407 0401  ................
+00000fd0: 0c01 0e01 0c01 0803 0a01 1602 0e01 0401  ................
+00000fe0: 0401 0401 0e01 0a01 0e01 1201 0e01 0801  ................
+00000ff0: 1601 0602 0601 04ff 0202 04fe 0202 02fe  ................
+00001000: 0202 02fe 0202 06fe 02ff 0805 0280 0801  ................
+00001010: 0401 0401 04ff 0c04 7252 0000 0063 0200  ........rR...c..
+00001020: 0000 0000 0000 0000 0000 0400 0000 0500  ................
+00001030: 0000 4300 0000 737e 0000 007c 00a0 0064  ..C...s~...|...d
+00001040: 0164 02a1 027d 007c 00a0 0064 0364 02a1  .d...}.|...d.d..
+00001050: 027d 007c 00a0 0064 0464 02a1 027d 007c  .}.|...d.d...}.|
+00001060: 00a0 0064 0564 03a1 027d 007c 00a0 0164  ...d.d...}.|...d
+00001070: 06a1 017d 027c 0264 076b 0472 347c 00a0  ...}.|.d.k.r4|..
+00001080: 0164 08a1 017d 037c 027c 036b 0472 347c  .d...}.|.|.k.r4|
+00001090: 009b 0064 097c 0164 0a19 009b 0064 0b9d  ...d.|.d.....d..
+000010a0: 047d 0064 0c7c 0164 0a19 009b 0064 0d7c  .}.d.|.d.....d.|
+000010b0: 009b 0064 0e9d 0553 0029 0f4e 7246 0000  ...d...S.).NrF..
+000010c0: 0072 2200 0000 fa07 3c2f 666f 6e74 3e7a  .r".....</font>z
+000010d0: 063c 2f62 6967 3e7a 0e3c 2f66 6f6e 743e  .</big>z.</font>
+000010e0: 3c2f 666f 6e74 3efa 053c 666f 6e74 7201  </font>..<fontr.
+000010f0: 0000 007a 052f 666f 6e74 7a13 3c73 7061  ...z./fontz.<spa
+00001100: 6e20 7374 796c 653d 2263 6f6c 6f72 3ada  n style="color:.
+00001110: 1261 6374 696f 6e5f 6c61 6265 6c5f 636f  .action_label_co
+00001120: 6c6f 72fa 0122 7a14 203c 7370 616e 2073  lor.."z. <span s
+00001130: 7479 6c65 3d22 636f 6c6f 723a 7a11 223e  tyle="color:z.">
+00001140: 2e2e 2e77 6974 6820 6c61 6265 6c3a 207a  ...with label: z
+00001150: 0b3c 2f73 7061 6e3e 3c2f 623e 2902 724d  .</span></b>).rM
+00001160: 0000 00da 0563 6f75 6e74 2904 724f 0000  .....count).rO..
+00001170: 0072 4e00 0000 5a0a 666f 6e74 5f63 6f75  .rN...Z.font_cou
+00001180: 6e74 5a0e 656e 645f 666f 6e74 5f63 6f75  ntZ.end_font_cou
+00001190: 6e74 7206 0000 0072 0600 0000 720a 0000  ntr....r....r...
+000011a0: 0072 4b00 0000 fd00 0000 731a 0000 000c  .rK.......s.....
+000011b0: 020c 010c 010c 010a 0108 020a 0208 0114  ................
+000011c0: 010c 0302 0106 ff02 ff72 4b00 0000 6304  .........rK...c.
+000011d0: 0000 0000 0000 0000 0000 0006 0000 0004  ................
+000011e0: 0000 0043 0000 0073 bc00 0000 7c01 722f  ...C...s....|.r/
+000011f0: 7400 7c00 7c02 8302 7d04 6401 7c04 7600  t.|.|...}.d.|.v.
+00001200: 7214 6402 7c04 7601 7214 7c04 9b00 6402  r.d.|.v.r.|...d.
+00001210: 9d02 7d04 6403 7c04 7600 7221 6404 7c04  ..}.d.|.v.r!d.|.
+00001220: 7601 7221 7c04 9b00 6402 9d02 7d04 6405  v.r!|...d...}.d.
+00001230: 7c04 7600 722e 6406 7c04 7601 722e 7c04  |.v.r.d.|.v.r.|.
+00001240: 9b00 6406 9d02 7d04 6e02 6407 7d04 7c03  ..d...}.n.d.}.|.
+00001250: 6408 1900 7249 7c01 7249 7c04 9b00 6409  d...rI|.rI|...d.
+00001260: 7c03 640a 1900 9b00 640b 9d04 7c00 a001  |.d.....d...|...
+00001270: 640c a101 6a02 1700 640d 1700 7d04 7c00  d...j...d...}.|.
+00001280: a001 640e a101 7d05 7c05 6400 7501 725c  ..d...}.|.d.u.r\
+00001290: 7c05 6a02 640f 6b02 725c 6410 7c04 9b00  |.j.d.k.r\d.|...
+000012a0: 9d02 7d04 7c04 5300 2911 4e72 5400 0000  ..}.|.S.).NrT...
+000012b0: 7253 0000 007a 0826 6c74 3b66 6f6e 747a  rS...z.&lt;fontz
+000012c0: 0d26 6c74 3b2f 666f 6e74 2667 743b 7a03  .&lt;/font&gt;z.
+000012d0: 3c62 3e7a 043c 2f62 3e72 2200 0000 7239  <b>z.</b>r"...r9
+000012e0: 0000 007a 1d3c 2f73 7061 6e3e 3c73 7061  ...z.</span><spa
+000012f0: 6e20 7374 796c 653d 2263 6f6c 6f72 3a52  n style="color:R
+00001300: 6564 da0b 666f 6e74 5f74 6f5f 7573 657a  ed..font_to_usez
+00001310: 123e 266e 6273 703b 266e 6273 703b 636f  .>&nbsp;&nbsp;co
+00001320: 6465 3a72 4400 0000 fa01 2d5a 0273 655a  de:rD.....-Z.seZ
+00001330: 0566 616c 7365 7a1c 205b 436f 6e74 696e  .falsez. [Contin
+00001340: 7565 2054 6173 6b20 4166 7465 7220 4572  ue Task After Er
+00001350: 726f 725d 2903 7252 0000 0072 2300 0000  ror]).rR...r#...
+00001360: 7224 0000 0029 06da 0b63 6f64 655f 6163  r$...)...code_ac
+00001370: 7469 6f6e da0b 6163 7469 6f6e 5f74 7970  tion..action_typ
+00001380: 6572 4e00 0000 da0c 7072 6f67 7261 6d5f  erN.....program_
+00001390: 6172 6773 da0b 6578 7472 615f 7374 7566  args..extra_stuf
+000013a0: 6672 1300 0000 7206 0000 0072 0600 0000  fr....r....r....
+000013b0: 720a 0000 00da 0f67 6574 5f65 7874 7261  r......get_extra
+000013c0: 5f73 7475 6666 1601 0000 733a 0000 0002  _stuff....s:....
+000013d0: 0202 ff02 0304 0104 ff10 040a 0210 020a  ................
+000013e0: 0210 020a 0202 8004 0206 0202 ff02 0102  ................
+000013f0: ff06 0406 0106 ff0a 0202 fe02 0302 fd02  ................
+00001400: ff0a 0812 010a 0104 0172 5e00 0000 6304  .........r^...c.
+00001410: 0000 0000 0000 0000 0000 0009 0000 0005  ................
+00001420: 0000 0043 0000 0073 ba00 0000 7400 7c00  ...C...s....t.|.
+00001430: 7c01 7c02 7c03 8304 7d04 6401 5c03 7d05  |.|.|...}.d.\.}.
+00001440: 7d06 7d07 7c00 a001 6402 a101 7d08 7c08  }.}.|...d...}.|.
+00001450: 6400 7501 7257 7c08 6a02 6402 6b02 7257  d.u.rW|.j.d.k.rW
+00001460: 7c08 a001 6403 a101 6400 7500 7227 6404  |...d...d.u.r'd.
+00001470: 6404 6404 7c04 6604 5300 7c08 a001 6403  d.d.|.f.S.|...d.
+00001480: a101 6a03 6400 7501 7237 6405 7c08 a001  ..j.d.u.r7d.|...
+00001490: 6403 a101 6a03 1700 7d05 7c08 a001 6406  d...j...}.|...d.
+000014a0: a101 6a03 6400 7501 7247 6407 7c08 a001  ..j.d.u.rGd.|...
+000014b0: 6406 a101 6a03 1700 7d06 7c08 a001 6408  d...j...}.|...d.
+000014c0: a101 6a03 6400 7501 7257 6409 7c08 a001  ..j.d.u.rWd.|...
+000014d0: 6408 a101 6a03 1700 7d07 7c05 7c06 7c07  d...j...}.|.|.|.
+000014e0: 7c04 6604 5300 290a 4e29 0372 2200 0000  |.f.S.).N).r"...
+000014f0: 7222 0000 0072 2200 0000 da03 4170 705a  r"...r".....AppZ
+00001500: 0861 7070 436c 6173 7372 2200 0000 7a06  .appClassr"...z.
+00001510: 436c 6173 733a 5a06 6170 7050 6b67 7a0a  Class:Z.appPkgz.
+00001520: 2c20 5061 636b 6167 653a 7245 0000 007a  , Package:rE...z
+00001530: 062c 2041 7070 3a29 0472 5e00 0000 7223  ., App:).r^...r#
+00001540: 0000 0072 0c00 0000 7224 0000 0029 09da  ...r....r$...)..
+00001550: 0a63 6f64 655f 6368 696c 6472 5b00 0000  .code_childr[...
+00001560: 724e 0000 0072 5c00 0000 725d 0000 005a  rN...r\...r]...Z
+00001570: 0961 7070 5f63 6c61 7373 5a07 6170 705f  .app_classZ.app_
+00001580: 706b 675a 0361 7070 7213 0000 0072 0600  pkgZ.appr....r..
+00001590: 0000 7206 0000 0072 0a00 0000 da0f 6765  ..r....r......ge
+000015a0: 745f 6170 705f 6465 7461 696c 733f 0100  t_app_details?..
+000015b0: 0073 1a00 0000 0e01 0a01 0a01 1201 0e01  .s..............
+000015c0: 0c01 1001 1001 1001 1001 1001 1001 0c01  ................
+000015d0: 7261 0000 0029 1072 3b00 0000 5a17 6d61  ra...).r;...Z.ma
+000015e0: 7074 6173 6b65 722e 7372 632e 7368 656c  ptasker.src.shel
+000015f0: 6c73 6f72 7472 0200 0000 da16 6d61 7074  lsortr......mapt
+00001600: 6173 6b65 722e 7372 632e 7379 7363 6f6e  asker.src.syscon
+00001610: 7374 7203 0000 0072 0400 0000 7214 0000  str....r....r...
+00001620: 0072 1600 0000 7225 0000 0072 2d00 0000  .r....r%...r-...
+00001630: 7230 0000 0072 4300 0000 7252 0000 0072  r0...rC...rR...r
+00001640: 4b00 0000 725e 0000 0072 6100 0000 7206  K...r^...ra...r.
+00001650: 0000 0072 0600 0000 7206 0000 0072 0a00  ...r....r....r..
+00001660: 0000 da08 3c6d 6f64 756c 653e 0100 0000  ....<module>....
+00001670: 731c 0000 0008 0d0c 020c 010c 0108 0e08  s...............
+00001680: 1c08 0708 2008 1608 1508 4008 2f08 190c  .... .....@./...
+00001690: 29                                       )
```

### Comparing `maptasker-1.3.1/maptasker/src/__pycache__/actionc.cpython-310.pyc` & `maptasker-1.3.2/maptasker/src/__pycache__/actionc.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 17 16:54:15 2023 UTC, .py size: 150799 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 379b 1464 0f4d 0200  o.......7..d.M..
+00000000: 6f0d 0d0a 0000 0000 918f 1c64 0f4d 0200  o..........d.M..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0018 0000 0040 0000 0073 e459 0000 6900  .....@...s.Y..i.
 00000030: 6400 6401 6402 6701 6403 6701 6404 6402  d.d.d.g.d.g.d.d.
 00000040: 6701 6700 6405 a201 6701 6406 9c06 9301  g.g.d...g.d.....
 00000050: 6407 6401 6700 6700 6408 6700 6700 6406  d.d.g.g.d.g.g.d.
 00000060: 9c06 9301 6409 6401 6700 6700 6408 6700  ....d.d.g.g.d.g.
 00000070: 6700 6406 9c06 9301 640a 6401 6700 6700  g.d.....d.d.g.g.
@@ -1567,15 +1567,15 @@
 000061e0: 0f00 0000 720f 0000 007a 1050 726f 7869  ....r....z.Proxi
 000061f0: 6d69 7479 2053 656e 736f 725a 0431 3235  mity SensorZ.125
 00006200: 747a 0d43 6f6d 706f 7365 2045 6d61 696c  tz.Compose Email
 00006210: 2903 fa0d 5265 6369 7069 656e 7428 7329  )...Recipient(s)
 00006220: 3a7a 0a2c 2053 7562 6a65 6374 3afa 0a2c  :z., Subject:..,
 00006230: 204d 6573 7361 6765 3a5a 0431 3236 7429   Message:Z.126t)
 00006240: 0672 0f00 0000 7203 0000 0072 0300 0000  .r....r....r....
-00006250: 7203 0000 0072 0f00 0000 7210 0000 00da  r....r....r.....
+00006250: 7203 0000 0072 0f00 0000 7210 0000 005a  r....r....r....Z
 00006260: 0652 6574 7572 6e7a 0656 616c 7565 3a29  .Returnz.Value:)
 00006270: 0372 1200 0000 7213 0000 007a 062c 2053  .r....r....z., S
 00006280: 746f 7029 0372 1200 0000 7213 0000 007a  top).r....r....z
 00006290: 1c2c 204c 6f63 616c 2056 6172 6961 626c  ., Local Variabl
 000062a0: 6520 5061 7373 7468 726f 7567 6829 0372  e Passthrough).r
 000062b0: 1200 0000 7213 0000 007a 182c 2052 6570  ....r....z., Rep
 000062c0: 6c61 6365 204f 6e20 5061 7373 7468 726f  lace On Passthro
@@ -1597,16 +1597,16 @@
 000063c0: 0c72 0f00 0000 7203 0000 0072 0f00 0000  .r....r....r....
 000063d0: 720f 0000 0072 0f00 0000 7203 0000 0072  r....r....r....r
 000063e0: 0300 0000 720f 0000 0072 0300 0000 7203  ....r....r....r.
 000063f0: 0000 0072 0300 0000 7210 0000 007a 0c50  ...r....r....z.P
 00006400: 6572 666f 726d 2054 6173 6b29 0b72 0200  erform Task).r..
 00006410: 0000 720d 0000 0072 0e00 0000 7215 0000  ..r....r....r...
 00006420: 0072 1600 0000 721d 0000 0072 2700 0000  .r....r....r'...
-00006430: 7228 0000 0072 2e00 0000 722f 0000 0072  r(...r....r/...r
-00006440: 3000 0000 fa05 4e61 6d65 3a7a 0b2c 2050  0.....Name:z., P
+00006430: 7228 0000 0072 2d00 0000 722e 0000 0072  r(...r-...r....r
+00006440: 2f00 0000 fa05 4e61 6d65 3a7a 0b2c 2050  /.....Name:z., P
 00006450: 7269 6f72 6974 793a 7a0e 2c20 5061 7261  riority:z., Para
 00006460: 6d65 7465 7220 313a 7a0e 2c20 5061 7261  meter 1:z., Para
 00006470: 6d65 7465 7220 323a 7a18 2c20 5265 7475  meter 2:z., Retu
 00006480: 726e 2056 616c 7565 2056 6172 6961 626c  rn Value Variabl
 00006490: 653a 2903 7212 0000 0072 1300 0000 7a17  e:).r....r....z.
 000064a0: 2c20 5265 7365 7420 5265 7475 726e 2056  , Reset Return V
 000064b0: 6172 6961 626c 6529 0372 1200 0000 7213  ariable).r....r.
@@ -1638,15 +1638,15 @@
 00006650: 5a04 3133 3665 7a0c 4361 7264 2052 656d  Z.136ez.Card Rem
 00006660: 6f76 6564 5a04 3133 3673 7a0d 5650 4e20  ovedZ.136sz.VPN 
 00006670: 436f 6e6e 6563 7465 645a 0431 3336 747a  ConnectedZ.136tz
 00006680: 0d53 6f75 6e64 2045 6666 6563 7473 2903  .Sound Effects).
 00006690: 721b 0000 0072 0400 0000 7229 0000 005a  r....r....r)...Z
 000066a0: 0431 3337 7429 0372 0300 0000 720f 0000  .137t).r....r...
 000066b0: 0072 1000 0000 da04 5374 6f70 2903 7212  .r......Stop).r.
-000066c0: 0000 0072 1300 0000 7236 0000 00fa 072c  ...r....r6.....,
+000066c0: 0000 0072 1300 0000 7235 0000 00fa 072c  ...r....r5.....,
 000066d0: 2054 6173 6b3a 5a04 3133 3874 da03 496d   Task:Z.138t..Im
 000066e0: 677a 0f53 6574 2054 6173 6b65 7220 4963  gz.Set Tasker Ic
 000066f0: 6f6e fa05 4963 6f6e 3a5a 0431 3339 747a  on..Icon:Z.139tz
 00006700: 1044 6973 6162 6c65 2028 5461 736b 6572  .Disable (Tasker
 00006710: 295a 0a31 3430 3631 3837 3736 747a 0e41  )Z.140618776tz.A
 00006720: 7574 6f57 6561 7220 546f 6173 745a 0431  utoWear ToastZ.1
 00006730: 3430 73e9 0200 0000 7a0d 4261 7474 6572  40s.....z.Batter
@@ -1690,15 +1690,15 @@
 00006990: 745a 0431 3438 747a 0b53 686f 7720 5275  tZ.148tz.Show Ru
 000069a0: 6e6c 6f67 5a04 3134 3973 7a08 5065 6e20  nlogZ.149sz.Pen 
 000069b0: 4d65 6e75 5a03 3134 737a 0f50 6f77 6572  MenuZ.14sz.Power
 000069c0: 2053 6176 6520 4d6f 6465 5a0b 3135 3038   Save ModeZ.1508
 000069d0: 3932 3933 3537 747a 0f41 7574 6f54 6f6f  929357tz.AutoToo
 000069e0: 6c73 2041 7272 6179 da04 3135 3073 7a0d  ls Array..150sz.
 000069f0: 5553 4220 436f 6e6e 6563 7465 6429 0372  USB Connected).r
-00006a00: 2400 0000 7204 0000 0072 3f00 0000 5a04  $...r....r?...Z.
+00006a00: 2400 0000 7204 0000 0072 3e00 0000 5a04  $...r....r>...Z.
 00006a10: 3135 3074 5a08 4b65 7967 7561 7264 5a0b  150tZ.KeyguardZ.
 00006a20: 3135 3230 3235 3734 3134 657a 1a41 7574  1520257414ez.Aut
 00006a30: 6f4e 6f74 6966 6963 6174 696f 6e20 496e  oNotification In
 00006a40: 7465 7263 6570 745a 0431 3532 747a 0f53  terceptZ.152tz.S
 00006a50: 6574 2057 6964 6765 7420 4963 6f6e 7a07  et Widget Iconz.
 00006a60: 2c20 4963 6f6e 3a5a 0431 3533 7429 0372  , Icon:Z.153t).r
 00006a70: 0300 0000 7203 0000 0072 0f00 0000 7a0b  ....r....r....z.
@@ -1746,22 +1746,22 @@
 00006d10: 3a7a 062c 204d 4143 3a7a 042c 2049 5029  :z., MAC:z., IP)
 00006d20: 037a 0741 6374 6976 653a 7204 0000 0072  .z.Active:r....r
 00006d30: 1f00 0000 5a04 3136 3173 7a10 4574 6865  ....Z.161sz.Ethe
 00006d40: 726e 6574 2043 6f6e 6e65 6374 5a04 3136  rnet ConnectZ.16
 00006d50: 3174 2904 720f 0000 0072 0f00 0000 720f  1t).r....r....r.
 00006d60: 0000 0072 0f00 0000 7a13 5365 7475 7020  ...r....z.Setup 
 00006d70: 4170 7020 5368 6f72 7463 7574 7329 0472  App Shortcuts).r
-00006d80: 3b00 0000 7237 0000 0072 3700 0000 7237  ;...r7...r7...r7
+00006d80: 3a00 0000 7236 0000 0072 3600 0000 7236  :...r6...r6...r6
 00006d90: 0000 005a 0b31 3632 3037 3733 3038 3674  ...Z.1620773086t
 00006da0: 7a12 5368 6172 7054 6f6f 6c73 2041 2054  z.SharpTools A T
 00006db0: 6869 6e67 5a04 3136 3274 e90d 0000 0029  hingZ.162t.....)
 00006dc0: 0d72 0200 0000 720d 0000 0072 0e00 0000  .r....r....r....
 00006dd0: 7215 0000 0072 1600 0000 721d 0000 0072  r....r....r....r
-00006de0: 2700 0000 7228 0000 0072 2e00 0000 722f  '...r(...r....r/
-00006df0: 0000 0072 3000 0000 7231 0000 00da 0231  ...r0...r1.....1
+00006de0: 2700 0000 7228 0000 0072 2d00 0000 722e  '...r(...r-...r.
+00006df0: 0000 0072 2f00 0000 7230 0000 00da 0231  ...r/...r0.....1
 00006e00: 3229 0d72 0300 0000 720f 0000 0072 0300  2).r....r....r..
 00006e10: 0000 7203 0000 0072 0f00 0000 720f 0000  ..r....r....r...
 00006e20: 0072 0f00 0000 720f 0000 0072 0f00 0000  .r....r....r....
 00006e30: 720f 0000 0072 0f00 0000 720f 0000 0072  r....r....r....r
 00006e40: 0f00 0000 7a18 5365 7475 7020 5175 6963  ....z.Setup Quic
 00006e50: 6b20 5365 7474 696e 6720 5469 6c65 2903  k Setting Tile).
 00006e60: 7211 0000 0072 0400 0000 5a03 3136 3229  r....r....Z.162)
@@ -1813,15 +1813,15 @@
 00007140: 037a 0753 7472 6561 6d3a 7204 0000 00da  .z.Stream:r.....
 00007150: 0331 3731 5a04 3137 3274 2905 720f 0000  .171Z.172t).r...
 00007160: 0072 0300 0000 7203 0000 0072 0300 0000  .r....r....r....
 00007170: 7203 0000 005a 054d 6f72 7365 7a0c 2c20  r....Z.Morsez., 
 00007180: 4672 6571 7565 6e63 793a 7a08 2c20 5370  Frequency:z., Sp
 00007190: 6565 643a 7a0c 2c20 416d 706c 6974 7564  eed:z., Amplitud
 000071a0: 653a 2903 7a09 2c20 5374 7265 616d 3a72  e:).z., Stream:r
-000071b0: 0400 0000 7247 0000 005a 0b31 3733 3236  ....rG...Z.17326
+000071b0: 0400 0000 7246 0000 005a 0b31 3733 3236  ....rF...Z.17326
 000071c0: 3335 3932 3474 7a10 4175 746f 496e 7075  35924tz.AutoInpu
 000071d0: 7420 4163 7469 6f6e 5a04 3137 3374 da03  t ActionZ.173t..
 000071e0: 4170 707a 0e4e 6574 776f 726b 2041 6363  Appz.Network Acc
 000071f0: 6573 7329 0372 2100 0000 7204 0000 005a  ess).r!...r....Z
 00007200: 0331 3733 5a04 3137 3573 5a08 4472 6561  .173Z.175sZ.Drea
 00007210: 6d69 6e67 5a04 3137 3574 7a0a 506f 7765  mingZ.175tz.Powe
 00007220: 7220 4d6f 6465 2903 7221 0000 0072 0400  r Mode).r!...r..
@@ -1864,18 +1864,18 @@
 00007470: 6f74 7a12 2c20 5265 6164 2053 6574 7469  otz., Read Setti
 00007480: 6e67 2054 6f3a 5a04 3138 3774 2903 720f  ng To:Z.187t).r.
 00007490: 0000 0072 0300 0000 7203 0000 007a 0a53  ...r....r....z.S
 000074a0: 6176 6520 496d 6167 657a 102c 2049 6d61  ave Imagez., Ima
 000074b0: 6765 2051 7561 6c69 7479 3a29 0372 1200  ge Quality:).r..
 000074c0: 0000 7213 0000 007a 1a2c 2044 656c 6574  ..r....z., Delet
 000074d0: 6520 4672 6f6d 204d 656d 6f72 7920 4166  e From Memory Af
-000074e0: 7465 725a 0431 3838 7329 0372 3800 0000  terZ.188s).r8...
+000074e0: 7465 725a 0431 3838 7329 0372 3700 0000  terZ.188s).r7...
 000074f0: 7203 0000 0072 0300 0000 7a09 4461 726b  r....r....z.Dark
 00007500: 204d 6f64 655a 0431 3838 747a 0a4c 6f61   ModeZ.188tz.Loa
-00007510: 6420 496d 6167 6572 4100 0000 7a16 2c20  d ImagerA...z., 
+00007510: 6420 496d 6167 6572 4000 0000 7a16 2c20  d Imager@...z., 
 00007520: 4d61 7820 5769 6474 6820 6f72 2048 6569  Max Width or Hei
 00007530: 6768 743a 2903 7212 0000 0072 1300 0000  ght:).r....r....
 00007540: 7a1a 2c20 5265 7370 6563 7420 4558 4946  z., Respect EXIF
 00007550: 204f 7269 656e 7461 7469 6f6e 5a09 3138   OrientationZ.18
 00007560: 3932 3734 3434 657a 1041 7574 6f41 7070  927444ez.AutoApp
 00007570: 7320 436f 6d6d 616e 645a 0431 3839 7429  s CommandZ.189t)
 00007580: 0472 0300 0000 7203 0000 0072 0300 0000  .r....r....r....
@@ -1893,36 +1893,36 @@
 00007640: 005a 0331 3930 5a0b 3139 3130 3338 3331  .Z.190Z.19103831
 00007650: 3438 747a 0f41 7574 6f54 6f6f 6c73 2052  48tz.AutoTools R
 00007660: 6567 6578 5a0b 3139 3132 3532 3237 3634  egexZ.1912522764
 00007670: 747a 0f41 7574 6f54 6f6f 6c73 2054 6f61  tz.AutoTools Toa
 00007680: 7374 5a0a 3139 3139 3731 3530 3774 7a11  stZ.191971507tz.
 00007690: 4175 746f 5765 6172 2041 4442 2057 6966  AutoWear ADB Wif
 000076a0: 695a 0431 3931 747a 0c52 6f74 6174 6520  iZ.191tz.Rotate 
-000076b0: 496d 6167 6529 0372 4d00 0000 7204 0000  Image).rM...r...
+000076b0: 496d 6167 6529 0372 4c00 0000 7204 0000  Image).rL...r...
 000076c0: 005a 0331 3931 2903 7a0a 2c20 4465 6772  .Z.191).z., Degr
 000076d0: 6565 733a 7204 0000 005a 0431 3931 615a  ees:r....Z.191aZ
 000076e0: 0431 3932 735a 0853 6c65 6570 696e 675a  .192sZ.SleepingZ
 000076f0: 0431 3932 7429 0372 0300 0000 720f 0000  .192t).r....r...
 00007700: 0072 0300 0000 7a0d 506c 6179 2052 696e  .r....z.Play Rin
-00007710: 6774 6f6e 6529 0372 4d00 0000 7204 0000  gtone).rM...r...
+00007710: 6774 6f6e 6529 0372 4c00 0000 7204 0000  gtone).rL...r...
 00007720: 005a 0331 3932 7a08 2c20 536f 756e 643a  .Z.192z., Sound:
 00007730: 5a04 3139 3374 7a0c 5265 7369 7a65 2049  Z.193tz.Resize I
 00007740: 6d61 6765 7a06 5769 6474 683a 7a09 2c20  magez.Width:z., 
 00007750: 4865 6967 6874 3a5a 0431 3934 747a 0a54  Height:Z.194tz.T
 00007760: 6573 7420 5363 656e 6529 03fa 072c 2054  est Scene)..., T
 00007770: 6573 743a 7204 0000 005a 0331 3934 7a12  est:r....Z.194z.
 00007780: 2c20 5374 6f72 6520 5265 7375 6c74 2049  , Store Result I
 00007790: 6e3a 5a0b 3139 3537 3637 3033 3532 747a  n:Z.1957670352tz
 000077a0: 0c41 7574 6f57 6561 7220 4170 705a 0b31  .AutoWear AppZ.1
 000077b0: 3935 3736 3831 3030 3065 7a11 4175 746f  957681000ez.Auto
 000077c0: 496e 7075 7420 4765 7374 7572 655a 0431  Input GestureZ.1
 000077d0: 3935 737a 0a4e 4643 2053 7461 7475 735a  95sz.NFC StatusZ
 000077e0: 0431 3935 7429 0472 0f00 0000 720f 0000  .195t).r....r...
 000077f0: 0072 0300 0000 720f 0000 007a 0c54 6573  .r....r....z.Tes
-00007800: 7420 456c 656d 656e 7429 0372 4e00 0000  t Element).rN...
+00007800: 7420 456c 656d 656e 7429 0372 4d00 0000  t Element).rM...
 00007810: 7204 0000 005a 0331 3935 5a04 3139 3774  r....Z.195Z.197t
 00007820: 7a12 4465 7665 6c6f 7065 7220 5365 7474  z.Developer Sett
 00007830: 696e 6773 5a04 3139 3874 7a14 4465 7669  ingsZ.198tz.Devi
 00007840: 6365 2049 6e66 6f20 5365 7474 696e 6773  ce Info Settings
 00007850: 5a04 3139 3974 7a14 4164 6420 4163 636f  Z.199tz.Add Acco
 00007860: 756e 7420 5365 7474 696e 6773 5a0a 3139  unt SettingsZ.19
 00007870: 3935 3538 3832 3674 7a12 546f 7563 6854  9558826tz.TouchT
@@ -1931,17 +1931,17 @@
 000078a0: 6e20 436c 6963 6bfa 124f 776e 6572 2041  n Click..Owner A
 000078b0: 7070 6c69 6361 7469 6f6e 3afa 082c 2054  pplication:.., T
 000078c0: 6974 6c65 3a5a 0532 3030 3365 5a05 3230  itle:Z.2003eZ.20
 000078d0: 3035 657a 0b53 4d53 2053 7563 6365 7373  05ez.SMS Success
 000078e0: 5a04 3230 3074 7a0c 416c 6c20 5365 7474  Z.200tz.All Sett
 000078f0: 696e 6773 5a05 3230 3130 657a 0b53 4d53  ingsZ.2010ez.SMS
 00007900: 2046 6169 6c75 7265 5a04 3230 3165 2904   FailureZ.201e).
-00007910: 7248 0000 0072 0f00 0000 720f 0000 0072  rH...r....r....r
+00007910: 7247 0000 0072 0f00 0000 720f 0000 0072  rG...r....r....r
 00007920: 0f00 0000 7a12 4173 7369 7374 616e 6365  ....z.Assistance
-00007930: 2052 6571 7565 7374 724c 0000 007a 062c   RequestrL...z.,
+00007930: 2052 6571 7565 7374 724b 0000 007a 062c   RequestrK...z.,
 00007940: 2055 524c 3a7a 082c 2054 6578 7473 3a7a   URL:z., Texts:z
 00007950: 092c 2045 7874 7261 733a 7205 0000 005a  ., Extras:r....Z
 00007960: 0432 3031 747a 1641 6972 706c 616e 6520  .201tz.Airplane 
 00007970: 4d6f 6465 2053 6574 7469 6e67 735a 0b32  Mode SettingsZ.2
 00007980: 3031 3031 3836 3631 3374 7a1e 4175 746f  010186613tz.Auto
 00007990: 5368 6565 7473 2044 656c 6574 6520 4365  Sheets Delete Ce
 000079a0: 6c6c 2043 6f6e 7465 6e74 5a04 3230 3274  ll ContentZ.202t
@@ -1959,38 +1959,38 @@
 00007a60: 7569 636b 2053 6574 7469 6e67 2043 6c69  uick Setting Cli
 00007a70: 636b 6564 5a04 3230 3565 7a0c 4261 7474  ckedZ.205ez.Batt
 00007a80: 6572 7920 4675 6c6c 5a04 3230 3665 7a13  ery FullZ.206ez.
 00007a90: 4261 7474 6572 7920 4f76 6572 6865 6174  Battery Overheat
 00007aa0: 696e 675a 0432 3036 747a 1157 6972 656c  ingZ.206tz.Wirel
 00007ab0: 6573 7320 5365 7474 696e 6773 5a05 3230  ess SettingsZ.20
 00007ac0: 3735 6529 0372 0300 0000 720f 0000 0072  75e).r....r....r
-00007ad0: 0f00 0000 2903 7240 0000 0072 0400 0000  ....).r@...r....
-00007ae0: 724a 0000 005a 0532 3037 3665 7a07 4e46  rJ...Z.2076ez.NF
+00007ad0: 0f00 0000 2903 723f 0000 0072 0400 0000  ....).r?...r....
+00007ae0: 7249 0000 005a 0532 3037 3665 7a07 4e46  rI...Z.2076ez.NF
 00007af0: 4320 5461 67fa 0349 443a 7a0a 2c20 436f  C Tag..ID:z., Co
 00007b00: 6e74 656e 743a 5a05 3230 3737 6572 1700  ntent:Z.2077er..
 00007b10: 0000 7a14 5365 636f 6e64 6172 7920 4170  ..z.Secondary Ap
 00007b20: 7020 4f70 656e 6564 5a05 3230 3738 657a  p OpenedZ.2078ez
 00007b30: 0b41 7070 2043 6861 6e67 6564 7a08 5061  .App Changedz.Pa
 00007b40: 636b 6167 653a da05 3230 3739 657a 1156  ckage:..2079ez.V
 00007b50: 6f6c 756d 6520 4c6f 6e67 2050 7265 7373  olume Long Press
-00007b60: 2903 7240 0000 0072 0400 0000 7252 0000  ).r@...r....rR..
+00007b60: 2903 723f 0000 0072 0400 0000 7251 0000  ).r?...r....rQ..
 00007b70: 007a 122c 2041 6464 6974 696f 6e61 6c20  .z., Additional 
 00007b80: 5469 6d65 3a5a 0532 3038 3065 2904 7217  Time:Z.2080e).r.
 00007b90: 0000 0072 0f00 0000 720f 0000 0072 1000  ...r....r....r..
 00007ba0: 0000 7a0c 4254 2043 6f6e 6e65 6374 6564  ..z.BT Connected
 00007bb0: 720e 0000 00da 0532 3038 3165 2906 7217  r......2081e).r.
 00007bc0: 0000 0072 0f00 0000 720f 0000 0072 0f00  ...r....r....r..
 00007bd0: 0000 720f 0000 0072 0300 0000 7a13 4d75  ..r....r....z.Mu
 00007be0: 7369 6320 5472 6163 6b20 4368 616e 6765  sic Track Change
 00007bf0: 6429 0572 0d00 0000 720e 0000 0072 1500  d).r....r....r..
 00007c00: 0000 7216 0000 0072 1d00 0000 7a06 5472  ..r....r....z.Tr
 00007c10: 6163 6b3a 7a08 2c20 416c 6275 6d3a 7a08  ack:z., Album:z.
 00007c20: 2c20 4172 7469 7374 7a0a 2c20 5061 636b  , Artistz., Pack
 00007c30: 6167 653a 2903 fa07 2c20 5479 7065 3a72  age:)..., Type:r
-00007c40: 0400 0000 7253 0000 005a 0532 3038 3365  ....rS...Z.2083e
+00007c40: 0400 0000 7252 0000 005a 0532 3038 3365  ....rR...Z.2083e
 00007c50: 7a12 5369 676e 6966 6963 616e 7420 4d6f  z.Significant Mo
 00007c60: 7469 6f6e 5a05 3230 3834 657a 0d41 6c61  tionZ.2084ez.Ala
 00007c70: 726d 2043 6861 6e67 6564 5a05 3230 3835  rm ChangedZ.2085
 00007c80: 657a 0c4c 6f67 6361 7420 456e 7472 7929  ez.Logcat Entry)
 00007c90: 0372 0d00 0000 720e 0000 0072 1500 0000  .r....r....r....
 00007ca0: 7a0a 436f 6d70 6f6e 656e 743a 7a09 2c20  z.Component:z., 
 00007cb0: 4669 6c74 6572 3a29 0372 1200 0000 7213  Filter:).r....r.
@@ -2001,15 +2001,15 @@
 00007d00: 696e 6773 5a05 3230 3931 655a 0532 3039  ingsZ.2091eZ.209
 00007d10: 3265 7a10 506f 7765 7220 4d65 6e75 2053  2ez.Power Menu S
 00007d20: 686f 776e 5a05 3230 3933 657a 1041 7373  hownZ.2093ez.Ass
 00007d30: 6973 7461 6e74 2041 6374 696f 6e5a 0532  istant ActionZ.2
 00007d40: 3039 3465 7a0d 4361 6c6c 2053 6372 6565  094ez.Call Scree
 00007d50: 6e65 645a 0532 3039 3565 5a04 5469 636b  nedZ.2095eZ.Tick
 00007d60: 7a0e 496e 7465 7276 616c 2028 6d73 293a  z.Interval (ms):
-00007d70: 5a05 3230 3936 655a 0332 3074 2905 7248  Z.2096eZ.20t).rH
+00007d70: 5a05 3230 3936 655a 0332 3074 2905 7247  Z.2096eZ.20t).rG
 00007d80: 0000 0072 0f00 0000 7203 0000 0072 0300  ...r....r....r..
 00007d90: 0000 7210 0000 007a 0a4c 6175 6e63 6820  ..r....z.Launch 
 00007da0: 4170 707a 072c 2044 6174 613a 2903 7212  Appz., Data:).r.
 00007db0: 0000 0072 1300 0000 7a18 4578 636c 7564  ...r....z.Exclud
 00007dc0: 6520 4672 6f6d 2052 6563 656e 7420 4170  e From Recent Ap
 00007dd0: 7073 2903 7212 0000 0072 1300 0000 7a15  ps).r....r....z.
 00007de0: 416c 7761 7973 2053 7461 7274 204e 6577  Always Start New
@@ -2108,21 +2108,21 @@
 000083b0: 6c75 6574 6f6f 7468 5a04 3239 3574 7a0c  luetoothZ.295tz.
 000083c0: 426c 7565 746f 6f74 6820 4944 5a04 3239  Bluetooth IDZ.29
 000083d0: 3674 7a0f 426c 7565 746f 6f74 6820 566f  6tz.Bluetooth Vo
 000083e0: 6963 655a 0232 657a 0d50 686f 6e65 204f  iceZ.2ez.Phone O
 000083f0: 6666 686f 6f6b 5a02 3273 5a05 3330 3030  ffhookZ.2sZ.3000
 00008400: 655a 0747 6573 7475 7265 da05 3330 3031  eZ.Gesture..3001
 00008410: 655a 0553 6861 6b65 2903 7a05 4178 6973  eZ.Shake).z.Axis
-00008420: 3a72 0400 0000 7257 0000 0029 037a 0c53  :r....rW...).z.S
+00008420: 3a72 0400 0000 7256 0000 0029 037a 0c53  :r....rV...).z.S
 00008430: 656e 7369 7469 7669 7479 3a72 0400 0000  ensitivity:r....
 00008440: 5a06 3330 3031 6561 2903 7a09 4475 7261  Z.3001ea).z.Dura
 00008450: 7469 6f6e 3a72 0400 0000 5a06 3330 3031  tion:r....Z.3001
 00008460: 6562 5a04 3330 3065 7a08 4461 7465 2053  ebZ.300ez.Date S
 00008470: 6574 5a04 3330 3074 5a06 416e 6368 6f72  etZ.300tZ.Anchor
-00008480: da05 4c61 6265 6c5a 0433 3031 747a 084d  ..LabelZ.301tz.M
+00008480: 5a05 4c61 6265 6c5a 0433 3031 747a 084d  Z.LabelZ.301tz.M
 00008490: 6963 204d 7574 655a 0433 3032 657a 0d54  ic MuteZ.302ez.T
 000084a0: 696d 652f 4461 7465 2053 6574 5a04 3330  ime/Date SetZ.30
 000084b0: 3365 7a0c 5469 6d65 7220 4368 616e 6765  3ez.Timer Change
 000084c0: 5a04 3330 3374 7a0c 416c 6172 6d20 566f  Z.303tz.Alarm Vo
 000084d0: 6c75 6d65 7a06 4c65 7665 6c3a 2903 7212  lumez.Level:).r.
 000084e0: 0000 0072 1300 0000 7a09 2c20 4469 7370  ...r....z., Disp
 000084f0: 6c61 7929 0372 1200 0000 7213 0000 007a  lay).r....r....z
@@ -2149,18 +2149,18 @@
 00008640: 566f 6c75 6d65 5a04 3330 3874 7a0d 5379  VolumeZ.308tz.Sy
 00008650: 7374 656d 2056 6f6c 756d 655a 0433 3039  stem VolumeZ.309
 00008660: 657a 0b53 7465 7073 2054 616b 656e 5a04  ez.Steps TakenZ.
 00008670: 3330 3974 7a0b 4454 4d46 2056 6f6c 756d  309tz.DTMF Volum
 00008680: 65da 0333 3073 2906 7203 0000 0072 0300  e..30s).r....r..
 00008690: 0000 7203 0000 0072 0300 0000 7203 0000  ..r....r....r...
 000086a0: 0072 1000 0000 7a0f 4865 6164 7365 7420  .r....z.Headset 
-000086b0: 506c 7567 6765 6429 0372 4000 0000 7204  Plugged).r@...r.
-000086c0: 0000 0072 5900 0000 5a03 3330 745a 0457  ...rY...Z.30tZ.W
+000086b0: 506c 7567 6765 6429 0372 3f00 0000 7204  Plugged).r?...r.
+000086c0: 0000 0072 5700 0000 5a03 3330 745a 0457  ...rW...Z.30tZ.W
 000086d0: 6169 7429 05fa 034d 533a fa0a 2c20 5365  ait)...MS:.., Se
-000086e0: 636f 6e64 733a 7246 0000 00fa 082c 2048  conds:rF....., H
+000086e0: 636f 6e64 733a 7245 0000 00fa 082c 2048  conds:rE....., H
 000086f0: 6f75 7273 3afa 072c 2044 6179 733a 5a04  ours:.., Days:Z.
 00008700: 3331 3074 7a0c 5669 6272 6174 6520 4d6f  310tz.Vibrate Mo
 00008710: 6465 2903 7221 0000 0072 0400 0000 5a03  de).r!...r....Z.
 00008720: 3331 305a 0433 3131 747a 0f42 5420 566f  310Z.311tz.BT Vo
 00008730: 6963 6520 566f 6c75 6d65 5a04 3331 3274  ice VolumeZ.312t
 00008740: 2908 7203 0000 0072 0300 0000 7203 0000  ).r....r....r...
 00008750: 0072 0300 0000 720f 0000 0072 0f00 0000  .r....r....r....
@@ -2170,21 +2170,21 @@
 00008790: 7429 0372 0300 0000 7203 0000 0072 1000  t).r....r....r..
 000087a0: 0000 7a0a 536f 756e 6420 4d6f 6465 2903  ..z.Sound Mode).
 000087b0: 7221 0000 0072 0400 0000 5a03 3331 3329  r!...r....Z.313)
 000087c0: 0372 1200 0000 7213 0000 007a 0c2c 2049  .r....r....z., I
 000087d0: 676e 6f72 6520 444e 445a 0433 3134 74e9  gnore DNDZ.314t.
 000087e0: 0a00 0000 290a 7202 0000 0072 0d00 0000  ....).r....r....
 000087f0: 720e 0000 0072 1500 0000 7216 0000 0072  r....r....r....r
-00008800: 1d00 0000 7227 0000 0072 2800 0000 722e  ....r'...r(...r.
-00008810: 0000 0072 2f00 0000 290a 7203 0000 0072  ...r/...).r....r
+00008800: 1d00 0000 7227 0000 0072 2800 0000 722d  ....r'...r(...r-
+00008810: 0000 0072 2e00 0000 290a 7203 0000 0072  ...r....).r....r
 00008820: 0f00 0000 720f 0000 0072 0f00 0000 720f  ....r....r....r.
 00008830: 0000 0072 0300 0000 720f 0000 0072 0300  ...r....r....r..
 00008840: 0000 7203 0000 0072 0300 0000 7a15 4175  ..r....r....z.Au
 00008850: 7468 656e 7469 6361 7469 6f6e 2044 6961  thentication Dia
-00008860: 6c6f 6729 0372 4000 0000 7204 0000 005a  log).r@...r....Z
+00008860: 6c6f 6729 0372 3f00 0000 7204 0000 005a  log).r?...r....Z
 00008870: 0333 3134 7a0e 2c20 4465 7363 7269 7074  .314z., Descript
 00008880: 696f 6e3a 7a15 2c20 4361 6e63 656c 2042  ion:z., Cancel B
 00008890: 7574 746f 6e20 5465 7874 3a7a 152c 204e  utton Text:z., N
 000088a0: 756d 6265 7220 6f66 2041 7474 656d 7074  umber of Attempt
 000088b0: 733a 7a13 2c20 5265 6164 2052 6573 756c  s:z., Read Resul
 000088c0: 7420 496e 746f 3a7a 142c 2054 696d 656f  t Into:z., Timeo
 000088d0: 7574 2028 5365 636f 6e64 7329 3a29 0372  ut (Seconds):).r
@@ -2206,30 +2206,30 @@
 000089d0: 747a 0f41 736b 2050 6572 6d69 7373 696f  tz.Ask Permissio
 000089e0: 6e73 7a15 5265 7175 6972 6564 2050 6572  nsz.Required Per
 000089f0: 6d69 7373 696f 6e73 3a7a 182c 2050 726f  missions:z., Pro
 00008a00: 6d70 7420 4966 204e 6f74 2047 7261 6e74  mpt If Not Grant
 00008a10: 6564 3a5a 0433 3230 7429 0572 0f00 0000  ed:Z.320t).r....
 00008a20: 7203 0000 0072 0f00 0000 720f 0000 0072  r....r....r....r
 00008a30: 0f00 0000 5a04 5069 6e67 2905 7a07 2c20  ....Z.Ping).z., 
-00008a40: 486f 7374 3a72 3500 0000 7a1a 2c20 4176  Host:r5...z., Av
+00008a40: 486f 7374 3a72 3400 0000 7a1a 2c20 4176  Host:r4...z., Av
 00008a50: 6572 6167 6520 5265 7375 6c74 2056 6172  erage Result Var
 00008a60: 6961 626c 653a 7a16 2c20 4d69 6e20 5265  iable:z., Min Re
 00008a70: 7375 6c74 2056 6172 6961 626c 653a 7a16  sult Variable:z.
 00008a80: 2c20 4d61 7820 5265 7375 6c74 2056 6172  , Max Result Var
 00008a90: 6961 626c 653a 5a04 3332 3174 e909 0000  iable:Z.321t....
 00008aa0: 0029 0972 0200 0000 720d 0000 0072 0e00  .).r....r....r..
 00008ab0: 0000 7215 0000 0072 1600 0000 721d 0000  ..r....r....r...
-00008ac0: 0072 2700 0000 7228 0000 0072 2e00 0000  .r'...r(...r....
+00008ac0: 0072 2700 0000 7228 0000 0072 2d00 0000  .r'...r(...r-...
 00008ad0: 2909 7217 0000 0072 0f00 0000 720f 0000  ).r....r....r...
 00008ae0: 0072 0f00 0000 720f 0000 0072 0f00 0000  .r....r....r....
 00008af0: 7203 0000 0072 0300 0000 720f 0000 007a  r....r....r....z
 00008b00: 0947 4420 5570 6c6f 6164 2908 720d 0000  .GD Upload).r...
 00008b10: 0072 0e00 0000 7215 0000 0072 1600 0000  .r....r....r....
 00008b20: 721d 0000 0072 2700 0000 7228 0000 0072  r....r'...r(...r
-00008b30: 2e00 0000 7a15 476f 6f67 6c65 2044 7269  ....z.Google Dri
+00008b30: 2d00 0000 7a15 476f 6f67 6c65 2044 7269  -...z.Google Dri
 00008b40: 7665 2f41 6363 6f75 6e74 3a7a 0c2c 2044  ve/Account:z., D
 00008b50: 6174 612f 4669 6c65 3a7a 132c 2052 656d  ata/File:z., Rem
 00008b60: 6f74 6520 4669 6c65 204e 616d 653a 7a10  ote File Name:z.
 00008b70: 2c20 5265 6d6f 7465 2046 6f6c 6465 723a  , Remote Folder:
 00008b80: 7a16 2c20 436f 6e74 656e 7420 4465 7363  z., Content Desc
 00008b90: 7269 7074 696f 6e3a 2903 7212 0000 0072  ription:).r....r
 00008ba0: 1300 0000 7a15 2c20 4f76 6572 7772 6974  ....z., Overwrit
@@ -2240,37 +2240,37 @@
 00008bf0: 3274 7a0b 4461 7461 2042 6163 6b75 707a  2tz.Data Backupz
 00008c00: 172c 2047 6f6f 676c 6520 4472 6976 6520  ., Google Drive 
 00008c10: 4163 636f 756e 743a 2903 7212 0000 0072  Account:).r....r
 00008c20: 1300 0000 7a19 2c20 496e 636c 7564 6520  ....z., Include 
 00008c30: 5573 6572 2056 6172 732f 5072 6566 735a  User Vars/PrefsZ
 00008c40: 0433 3233 747a 0f41 6972 706c 616e 6520  .323tz.Airplane 
 00008c50: 5261 6469 6f73 2903 7212 0000 0072 1300  Radios).r....r..
-00008c60: 0000 7256 0000 0029 0372 1200 0000 7213  ..rV...).r....r.
+00008c60: 0000 7255 0000 0029 0372 1200 0000 7213  ..rU...).r....r.
 00008c70: 0000 007a 062c 2043 656c 6c29 0372 1200  ...z., Cell).r..
 00008c80: 0000 7213 0000 007a 052c 204e 4643 2903  ..r....z., NFC).
 00008c90: 7212 0000 0072 1300 0000 7a06 2c20 5769  r....r....z., Wi
 00008ca0: 6669 2903 7212 0000 0072 1300 0000 7a07  fi).r....r....z.
 00008cb0: 2c20 5769 6d61 785a 0433 3234 7429 0672  , WimaxZ.324t).r
 00008cc0: 1700 0000 720f 0000 0072 0300 0000 7203  ....r....r....r.
 00008cd0: 0000 0072 0f00 0000 720f 0000 007a 0747  ...r....r....z.G
 00008ce0: 4420 4c69 7374 2904 720d 0000 0072 0e00  D List).r....r..
 00008cf0: 0000 7215 0000 0072 1d00 0000 7a15 476f  ..r....r....z.Go
 00008d00: 6f67 6c65 2044 7269 7665 2041 6363 6f75  ogle Drive Accou
-00008d10: 6e74 3a29 0372 5400 0000 7204 0000 005a  nt:).rT...r....Z
+00008d10: 6e74 3a29 0372 5300 0000 7204 0000 005a  nt:).rS...r....Z
 00008d20: 0333 3234 2903 7a13 2c20 4669 6c65 7320  .324).z., Files 
 00008d30: 6f72 2046 6f6c 6465 7273 3a72 0400 0000  or Folders:r....
 00008d40: 5a04 3332 3461 7a08 2c20 5175 6572 793a  Z.324az., Query:
 00008d50: 5a04 3332 3574 2908 7217 0000 0072 0f00  Z.325t).r....r..
 00008d60: 0000 7203 0000 0072 0300 0000 720f 0000  ..r....r....r...
 00008d70: 0072 0f00 0000 720f 0000 0072 0f00 0000  .r....r....r....
 00008d80: 7a08 4744 2054 7261 7368 2906 720d 0000  z.GD Trash).r...
 00008d90: 0072 0e00 0000 7215 0000 0072 1600 0000  .r....r....r....
 00008da0: 721d 0000 0072 2700 0000 2903 7a0e 2c20  r....r'...).z., 
 00008db0: 5472 6173 6820 5661 6c75 653a 7204 0000  Trash Value:r...
-00008dc0: 005a 0333 3235 2903 7254 0000 0072 0400  .Z.325).rT...r..
+00008dc0: 005a 0333 3235 2903 7253 0000 0072 0400  .Z.325).rS...r..
 00008dd0: 0000 5a04 3332 3561 7a0a 2c20 4669 6c65  ..Z.325az., File
 00008de0: 2049 443a 7a07 2c20 5061 7468 3a5a 0433   ID:z., Path:Z.3
 00008df0: 3236 7429 0772 1700 0000 720f 0000 0072  26t).r....r....r
 00008e00: 0300 0000 720f 0000 0072 0f00 0000 720f  ....r....r....r.
 00008e10: 0000 0072 0f00 0000 7a0b 4744 2044 6f77  ...r....z.GD Dow
 00008e20: 6e6c 6f61 647a 0d2c 204c 6f63 616c 2050  nloadz., Local P
 00008e30: 6174 683a 5a04 3332 3774 2903 7217 0000  ath:Z.327t).r...
@@ -2293,16 +2293,16 @@
 00008f40: 6164 2054 7970 653a 5a04 3333 3174 5a04  ad Type:Z.331tZ.
 00008f50: 3333 3274 5a03 4750 535a 0433 3333 745a  332tZ.GPSZ.333tZ
 00008f60: 0433 3334 7429 0972 0f00 0000 720f 0000  .334t).r....r...
 00008f70: 0072 0300 0000 7203 0000 0072 0300 0000  .r....r....r....
 00008f80: 7203 0000 0072 0f00 0000 720f 0000 0072  r....r....r....r
 00008f90: 0300 0000 7a0b 5361 7920 5761 7665 4e65  ....z.Say WaveNe
 00008fa0: 747a 0a54 6573 742f 5353 4d4c 3a7a 082c  tz.Test/SSML:z.,
-00008fb0: 2056 6f69 6365 3a29 0372 5400 0000 7204   Voice:).rT...r.
-00008fc0: 0000 0072 4700 0000 7a08 2c20 5069 7463  ...rG...z., Pitc
+00008fb0: 2056 6f69 6365 3a29 0372 5300 0000 7204   Voice:).rS...r.
+00008fc0: 0000 0072 4600 0000 7a08 2c20 5069 7463  ...rF...z., Pitc
 00008fd0: 683a 2903 7212 0000 0072 1300 0000 7a1b  h:).r....r....z.
 00008fe0: 2c20 436f 6e74 696e 7565 2054 6173 6b20  , Continue Task 
 00008ff0: 496d 6d65 6469 6174 656c 797a 072c 2046  Immediatelyz., F
 00009000: 696c 653a 7a13 2c20 4f76 6572 7269 6465  ile:z., Override
 00009010: 2041 5049 204b 6579 3a29 0372 1200 0000   API Key:).r....
 00009020: 7213 0000 007a 152c 2052 6573 7065 6374  r....z., Respect
 00009030: 2041 7564 696f 2046 6f63 7573 5a04 3333   Audio FocusZ.33
@@ -2319,26 +2319,26 @@
 000090e0: 7469 6f6e 2053 6574 7469 6e67 737a 0b2c  tion Settingsz.,
 000090f0: 2043 6174 6567 6f72 793a 5a04 3333 3874   Category:Z.338t
 00009100: 7a1a 4e6f 7469 6669 6361 7469 6f6e 2043  z.Notification C
 00009110: 6174 6567 6f72 7920 496e 666f 7a09 4361  ategory Infoz.Ca
 00009120: 7465 676f 7279 3a5a 0433 3339 74e9 0e00  tegory:Z.339t...
 00009130: 0000 290e 7202 0000 0072 0d00 0000 720e  ..).r....r....r.
 00009140: 0000 0072 1500 0000 7216 0000 0072 1d00  ...r....r....r..
-00009150: 0000 7227 0000 0072 2800 0000 722e 0000  ..r'...r(...r...
-00009160: 0072 2f00 0000 7230 0000 0072 3100 0000  .r/...r0...r1...
-00009170: 7245 0000 00da 0231 3329 0e72 1700 0000  rE.....13).r....
+00009150: 0000 7227 0000 0072 2800 0000 722d 0000  ..r'...r(...r-..
+00009160: 0072 2e00 0000 722f 0000 0072 3000 0000  .r....r/...r0...
+00009170: 7244 0000 00da 0231 3329 0e72 1700 0000  rD.....13).r....
 00009180: 7203 0000 0072 0f00 0000 720f 0000 0072  r....r....r....r
 00009190: 0f00 0000 720f 0000 0072 0f00 0000 720f  ....r....r....r.
 000091a0: 0000 0072 0300 0000 7203 0000 0072 0300  ...r....r....r..
 000091b0: 0000 7203 0000 0072 0300 0000 7210 0000  ..r....r....r...
 000091c0: 007a 0c48 5454 5020 5265 7175 6573 7429  .z.HTTP Request)
 000091d0: 0c72 0d00 0000 720e 0000 0072 1500 0000  .r....r....r....
 000091e0: 7216 0000 0072 1d00 0000 7227 0000 0072  r....r....r'...r
-000091f0: 2800 0000 722e 0000 0072 2f00 0000 7230  (...r....r/...r0
-00009200: 0000 0072 3100 0000 7245 0000 0029 03fa  ...r1...rE...)..
+000091f0: 2800 0000 722d 0000 0072 2e00 0000 722f  (...r-...r....r/
+00009200: 0000 0072 3000 0000 7244 0000 0029 03fa  ...r0...rD...)..
 00009210: 074d 6574 686f 643a 7204 0000 005a 0333  .Method:r....Z.3
 00009220: 3339 7a0a 2c20 4865 6164 6572 733a 7a13  39z., Headers:z.
 00009230: 2c20 5175 6572 7920 5061 7261 6d65 7465  , Query Paramete
 00009240: 7273 3a7a 072c 2042 6f64 793a 7a0f 2c20  rs:z., Body:z., 
 00009250: 4669 6c65 2054 6f20 5365 6e64 3a7a 252c  File To Send:z%,
 00009260: 2046 696c 652f 4469 7265 6374 6f72 7920   File/Directory 
 00009270: 546f 2053 6176 6520 5769 7468 204f 7574  To Save With Out
@@ -2348,53 +2348,53 @@
 000092b0: 7213 0000 007a 202c 2041 7574 6f6d 6174  r....z , Automat
 000092c0: 6963 616c 6c79 2046 6f6c 6c6f 7720 5265  ically Follow Re
 000092d0: 6469 7265 6374 7329 0372 1200 0000 7213  directs).r....r.
 000092e0: 0000 007a 0d2c 2055 7365 2043 6f6f 6b69  ...z., Use Cooki
 000092f0: 6573 5a04 3334 3074 2904 7217 0000 0072  esZ.340t).r....r
 00009300: 0300 0000 720f 0000 0072 0300 0000 7a14  ....r....r....z.
 00009310: 426c 7565 746f 6f74 6820 436f 6e6e 6563  Bluetooth Connec
-00009320: 7469 6f6e 2903 7234 0000 0072 0400 0000  tion).r4...r....
+00009320: 7469 6f6e 2903 7233 0000 0072 0400 0000  tion).r3...r....
 00009330: 5a03 3334 307a 092c 2044 6576 6963 653a  Z.340z., Device:
 00009340: 5a04 3334 3174 7a08 5465 7374 204e 6574  Z.341tz.Test Net
-00009350: 2903 7240 0000 0072 0400 0000 5a03 3334  ).r@...r....Z.34
+00009350: 2903 723f 0000 0072 0400 0000 5a03 3334  ).r?...r....Z.34
 00009360: 315a 0433 3432 7429 0672 0300 0000 720f  1Z.342t).r....r.
 00009370: 0000 0072 0f00 0000 7203 0000 0072 0300  ...r....r....r..
 00009380: 0000 7210 0000 007a 0954 6573 7420 4669  ..r....z.Test Fi
-00009390: 6c65 2903 7240 0000 0072 0400 0000 5a03  le).r@...r....Z.
+00009390: 6c65 2903 723f 0000 0072 0400 0000 5a03  le).r?...r....Z.
 000093a0: 3334 325a 0433 3433 747a 0a54 6573 7420  342Z.343tz.Test 
-000093b0: 4d65 6469 6129 0372 4000 0000 7204 0000  Media).r@...r...
+000093b0: 4d65 6469 6129 0372 3f00 0000 7204 0000  Media).r?...r...
 000093c0: 005a 0333 3433 5a0a 3334 3436 3336 3434  .Z.343Z.34463644
 000093d0: 3674 7a1f 4175 746f 566f 6963 6520 5472  6tz.AutoVoice Tr
 000093e0: 6967 6765 7220 416c 6578 6120 526f 7574  igger Alexa Rout
 000093f0: 696e 655a 0433 3434 747a 0854 6573 7420  ineZ.344tz.Test 
-00009400: 4170 7029 0372 4000 0000 7204 0000 005a  App).r@...r....Z
+00009400: 4170 7029 0372 3f00 0000 7204 0000 005a  App).r?...r....Z
 00009410: 0333 3434 5a04 3334 3574 7a0d 5465 7374  .344Z.345tz.Test
-00009420: 2056 6172 6961 626c 6529 0372 4000 0000   Variable).r@...
+00009420: 2056 6172 6961 626c 6529 0372 3f00 0000   Variable).r?...
 00009430: 7204 0000 005a 0333 3435 7a13 2c20 5374  r....Z.345z., St
 00009440: 6f72 6520 5265 7375 6c74 7320 496e 3a5a  ore Results In:Z
 00009450: 0433 3436 747a 0a54 6573 7420 5068 6f6e  .346tz.Test Phon
-00009460: 6529 0372 4000 0000 7204 0000 005a 0333  e).r@...r....Z.3
+00009460: 6529 0372 3f00 0000 7204 0000 005a 0333  e).r?...r....Z.3
 00009470: 3436 5a04 3334 3774 2904 7203 0000 0072  46Z.347t).r....r
 00009480: 0f00 0000 720f 0000 0072 1000 0000 7a0b  ....r....r....z.
-00009490: 5465 7374 2054 6173 6b65 7229 0372 4000  Test Tasker).r@.
+00009490: 5465 7374 2054 6173 6b65 7229 0372 3f00  Test Tasker).r?.
 000094a0: 0000 7204 0000 005a 0333 3437 5a09 3334  ..r....Z.347Z.34
 000094b0: 3832 3930 3837 655a 0433 3438 747a 0c54  829087eZ.348tz.T
-000094c0: 6573 7420 4469 7370 6c61 7929 0372 4000  est Display).r@.
+000094c0: 6573 7420 4469 7370 6c61 7929 0372 3f00  est Display).r?.
 000094d0: 0000 7204 0000 005a 0333 3438 5a04 3334  ..r....Z.348Z.34
 000094e0: 3974 7a0b 5465 7374 2053 7973 7465 6d29  9tz.Test System)
-000094f0: 0372 4000 0000 7204 0000 005a 0333 3439  .r@...r....Z.349
+000094f0: 0372 3f00 0000 7204 0000 005a 0333 3439  .r?...r....Z.349
 00009500: 5a04 3335 3174 e90b 0000 0029 0b72 1700  Z.351t.....).r..
 00009510: 0000 7203 0000 0072 0f00 0000 720f 0000  ..r....r....r...
 00009520: 0072 0f00 0000 720f 0000 0072 0f00 0000  .r....r....r....
 00009530: 7203 0000 0072 0300 0000 720f 0000 0072  r....r....r....r
 00009540: 0f00 0000 7a09 4854 5450 2041 7574 6829  ....z.HTTP Auth)
 00009550: 0a72 0d00 0000 720e 0000 0072 1500 0000  .r....r....r....
 00009560: 7216 0000 0072 1d00 0000 7227 0000 0072  r....r....r'...r
-00009570: 2800 0000 722e 0000 0072 2f00 0000 7230  (...r....r/...r0
-00009580: 0000 0029 0372 6200 0000 7204 0000 005a  ...).rb...r....Z
+00009570: 2800 0000 722d 0000 0072 2e00 0000 722f  (...r-...r....r/
+00009580: 0000 0029 0372 6000 0000 7204 0000 005a  ...).r`...r....Z
 00009590: 0333 3531 7a0c 2c20 436c 6965 6e74 2049  .351z., Client I
 000095a0: 443a 7a10 2c20 436c 6965 6e74 2053 6563  D:z., Client Sec
 000095b0: 7265 743a 7a17 2c20 456e 6470 6f69 6e74  ret:z., Endpoint
 000095c0: 2054 6f20 4765 7420 436f 6465 3a7a 202c   To Get Code:z ,
 000095d0: 2045 6e64 706f 696e 7420 546f 2047 6574   Endpoint To Get
 000095e0: 2052 6566 7265 7368 2054 6f6b 656e 3a7a   Refresh Token:z
 000095f0: 092c 2053 636f 7065 733a 2903 7212 0000  ., Scopes:).r...
@@ -2405,27 +2405,27 @@
 00009640: 0472 0f00 0000 720f 0000 0072 0f00 0000  .r....r....r....
 00009650: 7210 0000 007a 0941 7272 6179 2053 6574  r....z.Array Set
 00009660: 2903 fa0f 5661 7269 6162 6c65 2041 7272  )...Variable Arr
 00009670: 6179 3afa 092c 2056 616c 7565 733a fa0b  ay:.., Values:..
 00009680: 2c20 5370 6c69 7474 6572 3a5a 0433 3535  , Splitter:Z.355
 00009690: 7429 0572 0f00 0000 7203 0000 0072 0f00  t).r....r....r..
 000096a0: 0000 7203 0000 0072 1000 0000 7a0a 4172  ..r....r....z.Ar
-000096b0: 7261 7920 5075 7368 7264 0000 00fa 0b2c  ray Pushrd.....,
+000096b0: 7261 7920 5075 7368 7262 0000 00fa 0b2c  ray Pushrb.....,
 000096c0: 2050 6f73 6974 696f 6e3a 2903 7212 0000   Position:).r...
 000096d0: 0072 1300 0000 7a0d 2c20 4669 6c6c 2053  .r....z., Fill S
 000096e0: 7061 6365 735a 0433 3536 7429 0472 0f00  pacesZ.356t).r..
 000096f0: 0000 7203 0000 0072 0f00 0000 7210 0000  ..r....r....r...
-00009700: 007a 0941 7272 6179 2050 6f70 2903 7264  .z.Array Pop).rd
-00009710: 0000 0072 6700 0000 fa09 2c20 546f 2056  ...rg....., To V
+00009700: 007a 0941 7272 6179 2050 6f70 2903 7262  .z.Array Pop).rb
+00009710: 0000 0072 6500 0000 fa09 2c20 546f 2056  ...re....., To V
 00009720: 6172 3a5a 0433 3537 747a 0b41 7272 6179  ar:Z.357tz.Array
 00009730: 2043 6c65 6172 5a04 3335 3874 7a0e 426c   ClearZ.358tz.Bl
-00009740: 7565 746f 6f74 6820 496e 666f 2903 7240  uetooth Info).r@
+00009740: 7565 746f 6f74 6820 496e 666f 2903 723f  uetooth Info).r?
 00009750: 0000 0072 0400 0000 5a03 3335 385a 0333  ...r....Z.358Z.3
-00009760: 3574 7a0a 5761 6974 2055 6e74 696c 725a  5tz.Wait UntilrZ
-00009770: 0000 0072 5b00 0000 725c 0000 0072 5d00  ...r[...r\...r].
+00009760: 3574 7a0a 5761 6974 2055 6e74 696c 7258  5tz.Wait UntilrX
+00009770: 0000 0072 5900 0000 725a 0000 0072 5b00  ...rY...rZ...r[.
 00009780: 0000 5a04 3336 3074 2908 7217 0000 0072  ..Z.360t).r....r
 00009790: 0f00 0000 720f 0000 0072 0f00 0000 7203  ....r....r....r.
 000097a0: 0000 0072 0f00 0000 7203 0000 0072 0300  ...r....r....r..
 000097b0: 0000 7a0c 496e 7075 7420 4469 616c 6f67  ..z.Input Dialog
 000097c0: 2907 720d 0000 0072 0e00 0000 7215 0000  ).r....r....r...
 000097d0: 0072 1600 0000 721d 0000 0072 2700 0000  .r....r....r'...
 000097e0: 7228 0000 00fa 0654 6974 6c65 3afa 072c  r(.....Title:..,
@@ -2449,16 +2449,16 @@
 00009900: 0946 756e 6374 696f 6e3a 5a04 3336 3674  .Function:Z.366t
 00009910: 290a 7217 0000 0072 0300 0000 720f 0000  ).r....r....r...
 00009920: 0072 0f00 0000 720f 0000 0072 0f00 0000  .r....r....r....
 00009930: 7203 0000 0072 0300 0000 720f 0000 0072  r....r....r....r
 00009940: 0300 0000 7a0f 4765 7420 4c6f 6361 7469  ....z.Get Locati
 00009950: 6f6e 2056 3229 0972 0d00 0000 720e 0000  on V2).r....r...
 00009960: 0072 1500 0000 7216 0000 0072 1d00 0000  .r....r....r....
-00009970: 7227 0000 0072 2800 0000 722e 0000 0072  r'...r(...r....r
-00009980: 2f00 0000 7a12 5469 6d65 6f75 7420 2853  /...z.Timeout (S
+00009970: 7227 0000 0072 2800 0000 722d 0000 0072  r'...r(...r-...r
+00009980: 2e00 0000 7a12 5469 6d65 6f75 7420 2853  ....z.Timeout (S
 00009990: 6563 6f6e 6473 293a 7a1c 2c20 4d69 6e69  econds):z., Mini
 000099a0: 6d75 6d20 4163 6375 7261 6379 2028 6d65  mum Accuracy (me
 000099b0: 7465 7273 293a 7a18 2c20 5370 6565 6420  ters):z., Speed 
 000099c0: 286d 6574 6572 732f 7365 636f 6e64 293a  (meters/second):
 000099d0: 7a14 2c20 416c 7469 7475 6465 2028 6d65  z., Altitude (me
 000099e0: 7465 7273 293a 7a10 2c20 4e65 6172 204c  ters):z., Near L
 000099f0: 6f63 6174 696f 6e3a 2903 7212 0000 0072  ocation:).r....r
@@ -2476,27 +2476,27 @@
 00009ab0: 0000 0072 0300 0000 7a0d 5069 636b 204c  ...r....z.Pick L
 00009ac0: 6f63 6174 696f 6e29 0372 1200 0000 7213  ocation).r....r.
 00009ad0: 0000 007a 0f2c 2053 656c 6563 7420 5261  ...z., Select Ra
 00009ae0: 6469 7573 7a13 2c20 496e 6974 6961 6c20  diusz., Initial 
 00009af0: 4c6f 6361 7469 6f6e 3a29 03fa 062c 2053  Location:)..., S
 00009b00: 6574 3a72 0400 0000 5a03 3336 385a 0433  et:r....Z.368Z.3
 00009b10: 3639 747a 0d41 7272 6179 2050 726f 6365  69tz.Array Proce
-00009b20: 7373 2903 7254 0000 0072 0400 0000 5a03  ss).rT...r....Z.
+00009b20: 7373 2903 7253 0000 0072 0400 0000 5a03  ss).rS...r....Z.
 00009b30: 3336 395a 0433 3730 745a 0853 686f 7274  369Z.370tZ.Short
 00009b40: 6375 747a 0953 686f 7274 6375 743a 5a04  cutz.Shortcut:Z.
 00009b50: 3337 3174 5a06 4173 7472 6964 5a04 3337  371tZ.AstridZ.37
 00009b60: 3274 7a0b 5365 6e73 6f72 2049 6e66 6f72  2tz.Sensor Infor
-00009b70: 4000 0000 5a04 3337 3374 7a0b 5465 7374  @...Z.373tz.Test
+00009b70: 3f00 0000 5a04 3337 3374 7a0b 5465 7374  ?...Z.373tz.Test
 00009b80: 2053 656e 736f 7229 0372 1200 0000 7213   Sensor).r....r.
 00009b90: 0000 007a 152c 2043 6f6e 7665 7274 204f  ...z., Convert O
 00009ba0: 7269 656e 7461 7469 6f6e 5a04 3337 3474  rientationZ.374t
 00009bb0: 2908 7217 0000 0072 0300 0000 720f 0000  ).r....r....r...
 00009bc0: 0072 0300 0000 720f 0000 0072 0f00 0000  .r....r....r....
 00009bd0: 720f 0000 0072 0f00 0000 7a0e 5363 7265  r....r....z.Scre
-00009be0: 656e 2043 6170 7475 7265 2903 7240 0000  en Capture).r@..
+00009be0: 656e 2043 6170 7475 7265 2903 723f 0000  en Capture).r?..
 00009bf0: 0072 0400 0000 5a03 3337 347a 0e2c 204f  .r....Z.374z., O
 00009c00: 7574 7075 7420 4669 6c65 3a7a 102c 2056  utput File:z., V
 00009c10: 6964 656f 2045 6e63 6f64 6572 3a7a 0d2c  ideo Encoder:z.,
 00009c20: 2052 6573 6f6c 7574 696f 6e3a 7a10 2c20   Resolution:z., 
 00009c30: 5669 6465 6f20 4269 7472 6174 653a 5a04  Video Bitrate:Z.
 00009c40: 3337 3574 7a08 4144 4220 5769 6669 5a04  375tz.ADB WifiZ.
 00009c50: 3337 3674 7a0a 5368 6172 6520 4669 6c65  376tz.Share File
@@ -2511,63 +2511,63 @@
 00009ce0: 742f 496d 6167 6520 4469 616c 6f67 7a0b  t/Image Dialogz.
 00009cf0: 2c20 4275 7474 6f6e 2031 3a7a 0b2c 2042  , Button 1:z., B
 00009d00: 7574 746f 6e20 323a 7a0b 2c20 4275 7474  utton 2:z., Butt
 00009d10: 6f6e 2033 3afa 082c 2049 6d61 6765 3a5a  on 3:.., Image:Z
 00009d20: 0433 3738 74e9 0f00 0000 290f 7202 0000  .378t.....).r...
 00009d30: 0072 0d00 0000 720e 0000 0072 1500 0000  .r....r....r....
 00009d40: 7216 0000 0072 1d00 0000 7227 0000 0072  r....r....r'...r
-00009d50: 2800 0000 722e 0000 0072 2f00 0000 7230  (...r....r/...r0
-00009d60: 0000 0072 3100 0000 7245 0000 0072 6100  ...r1...rE...ra.
+00009d50: 2800 0000 722d 0000 0072 2e00 0000 722f  (...r-...r....r/
+00009d60: 0000 0072 3000 0000 7244 0000 0072 5f00  ...r0...rD...r_.
 00009d70: 0000 da02 3134 290f 7217 0000 0072 0300  ....14).r....r..
 00009d80: 0000 720f 0000 0072 0f00 0000 720f 0000  ..r....r....r...
 00009d90: 0072 0f00 0000 720f 0000 0072 0f00 0000  .r....r....r....
 00009da0: 720f 0000 0072 0300 0000 7203 0000 0072  r....r....r....r
 00009db0: 0300 0000 7203 0000 0072 0f00 0000 7210  ....r....r....r.
 00009dc0: 0000 007a 0b4c 6973 7420 4469 616c 6f67  ...z.List Dialog
 00009dd0: 290c 720d 0000 0072 0e00 0000 7215 0000  ).r....r....r...
 00009de0: 0072 1600 0000 7227 0000 0072 2800 0000  .r....r'...r(...
-00009df0: 722e 0000 0072 2f00 0000 7230 0000 0072  r....r/...r0...r
-00009e00: 3100 0000 7245 0000 0072 6100 0000 2903  1...rE...ra...).
+00009df0: 722d 0000 0072 2e00 0000 722f 0000 0072  r-...r....r/...r
+00009e00: 3000 0000 7244 0000 0072 5f00 0000 2903  0...rD...r_...).
 00009e10: 7221 0000 0072 0400 0000 5a03 3337 387a  r!...r....Z.378z
 00009e20: 082c 2049 7465 6d73 3a7a 162c 2046 6972  ., Items:z., Fir
 00009e30: 7374 2056 6973 6962 6c65 2049 6e64 6578  st Visible Index
 00009e40: 3a29 0372 1200 0000 7213 0000 007a 0d2c  :).r....r....z.,
 00009e50: 2048 6964 6520 4669 6c74 6572 5a03 3337   Hide FilterZ.37
-00009e60: 735a 0333 3774 da02 4966 5a04 3338 3174  sZ.37t..IfZ.381t
+00009e60: 735a 0333 3774 5a02 4966 5a04 3338 3174  sZ.37tZ.IfZ.381t
 00009e70: 2905 7217 0000 0072 0f00 0000 720f 0000  ).r....r....r...
 00009e80: 0072 0f00 0000 7203 0000 007a 0f43 6f6e  .r....r....z.Con
 00009e90: 7461 6374 2056 6961 2041 7070 fa08 436f  tact Via App..Co
 00009ea0: 6e74 6163 743a 7a06 2c20 4170 703a 5a04  ntact:z., App:Z.
 00009eb0: 3338 3374 7a0e 5365 7474 696e 6773 2050  383tz.Settings P
-00009ec0: 616e 656c 2903 7272 0000 0072 0400 0000  anel).rr...r....
+00009ec0: 616e 656c 2903 726f 0000 0072 0400 0000  anel).ro...r....
 00009ed0: 5a03 3338 335a 0433 3834 7429 0f72 1700  Z.383Z.384t).r..
 00009ee0: 0000 720f 0000 0072 0300 0000 7203 0000  ..r....r....r...
 00009ef0: 0072 0f00 0000 720f 0000 0072 0f00 0000  .r....r....r....
 00009f00: 720f 0000 0072 0f00 0000 720f 0000 0072  r....r....r....r
 00009f10: 0f00 0000 720f 0000 0072 0f00 0000 720f  ....r....r....r.
 00009f20: 0000 0072 0300 0000 7a22 4465 7669 6365  ...r....z"Device
 00009f30: 2043 6f6e 7472 6f6c 2028 506f 7765 7220   Control (Power 
 00009f40: 4d65 6e75 2041 6374 696f 6e29 290e 720d  Menu Action)).r.
 00009f50: 0000 0072 0e00 0000 7215 0000 0072 1600  ...r....r....r..
 00009f60: 0000 721d 0000 0072 2700 0000 7228 0000  ..r....r'...r(..
-00009f70: 0072 2e00 0000 722f 0000 0072 3000 0000  .r....r/...r0...
-00009f80: 7231 0000 0072 4500 0000 7261 0000 0072  r1...rE...ra...r
-00009f90: 7000 0000 2903 723c 0000 0072 0400 0000  p...).r<...r....
-00009fa0: 5a03 3338 3429 0372 5400 0000 7204 0000  Z.384).rT...r...
+00009f70: 0072 2d00 0000 722e 0000 0072 2f00 0000  .r-...r....r/...
+00009f80: 7230 0000 0072 4400 0000 725f 0000 0072  r0...rD...r_...r
+00009f90: 6e00 0000 2903 723b 0000 0072 0400 0000  n...).r;...r....
+00009fa0: 5a03 3338 3429 0372 5300 0000 7204 0000  Z.384).rS...r...
 00009fb0: 005a 0433 3834 6172 1e00 0000 7a0c 2c20  .Z.384ar....z., 
 00009fc0: 5261 6e67 6520 4d69 6e3a 7a0c 2c20 5261  Range Min:z., Ra
 00009fd0: 6e67 6520 4d61 783a 7a10 2c20 5261 6e67  nge Max:z., Rang
 00009fe0: 6520 4375 7272 656e 743a 7a0b 5261 6e67  e Current:z.Rang
 00009ff0: 6520 5374 6570 3a7a 0f2c 2052 616e 6765  e Step:z., Range
 0000a000: 2046 6f72 6d61 743a 5a04 3338 3574 5a07   Format:Z.385tZ.
 0000a010: 436f 6d6d 616e 645a 0433 3836 7429 0672  CommandZ.386t).r
 0000a020: 1700 0000 7203 0000 0072 0300 0000 7203  ....r....r....r.
 0000a030: 0000 0072 0300 0000 7203 0000 007a 0e43  ...r....r....z.C
 0000a040: 616c 6c20 5363 7265 656e 696e 6729 0372  all Screening).r
-0000a050: 5100 0000 7204 0000 005a 0333 3836 2903  Q...r....Z.386).
+0000a050: 5000 0000 7204 0000 005a 0333 3836 2903  P...r....Z.386).
 0000a060: 7212 0000 0072 1300 0000 7a0f 2c20 536b  r....r....z., Sk
 0000a070: 6970 2043 616c 6c20 4c6f 6729 0372 1200  ip Call Log).r..
 0000a080: 0000 7213 0000 007a 132c 2053 6b69 7020  ..r....z., Skip 
 0000a090: 4e6f 7469 6669 6361 7469 6f6e 5a04 3338  NotificationZ.38
 0000a0a0: 3774 7a14 4163 6365 7373 6962 696c 6974  7tz.Accessibilit
 0000a0b0: 7920 566f 6c75 6d65 5a0a 3338 3835 3433  y VolumeZ.388543
 0000a0c0: 3737 3474 7a24 4175 746f 5368 6565 7473  774tz$AutoSheets
@@ -2576,55 +2576,55 @@
 0000a0f0: 290a 7217 0000 0072 0f00 0000 720f 0000  ).r....r....r...
 0000a100: 0072 0f00 0000 720f 0000 0072 0300 0000  .r....r....r....
 0000a110: 7203 0000 0072 0300 0000 7203 0000 0072  r....r....r....r
 0000a120: 1000 0000 7a16 4d75 6c74 6970 6c65 2056  ....z.Multiple V
 0000a130: 6172 6961 626c 6573 2053 6574 7a06 4e61  ariables Setz.Na
 0000a140: 6d65 733a 7a19 2c20 5661 7269 6162 6c65  mes:z., Variable
 0000a150: 204e 616d 6520 5370 6c69 7474 6572 3a72   Name Splitter:r
-0000a160: 6500 0000 7a12 2c20 5661 6c75 6573 2053  e...z., Values S
+0000a160: 6300 0000 7a12 2c20 5661 6c75 6573 2053  c...z., Values S
 0000a170: 706c 6974 7465 723a 2903 7212 0000 0072  plitter:).r....r
 0000a180: 1300 0000 7a0a 2c20 446f 204d 6174 6873  ....z., Do Maths
 0000a190: 2903 7212 0000 0072 1300 0000 7a0f 2c20  ).r....r....z., 
 0000a1a0: 4b65 6570 2045 7869 7374 696e 675a 0333  Keep ExistingZ.3
 0000a1b0: 3874 7a06 456e 6420 4966 5a04 3339 3074  8tz.End IfZ.390t
 0000a1c0: 2906 7217 0000 0072 0f00 0000 720f 0000  ).r....r....r...
 0000a1d0: 0072 0f00 0000 720f 0000 0072 1000 0000  .r....r....r....
 0000a1e0: 7a11 5069 636b 2049 6e70 7574 2044 6961  z.Pick Input Dia
-0000a1f0: 6c6f 6729 0472 4000 0000 7250 0000 007a  log).r@...rP...z
-0000a200: 092c 2c2c 2054 6578 743a 726b 0000 005a  .,,, Text:rk...Z
+0000a1f0: 6c6f 6729 0472 3f00 0000 724f 0000 007a  log).r?...rO...z
+0000a200: 092c 2c2c 2054 6578 743a 7269 0000 005a  .,,, Text:ri...Z
 0000a210: 0433 3931 7429 0c72 1700 0000 7203 0000  .391t).r....r...
 0000a220: 0072 0f00 0000 720f 0000 0072 0300 0000  .r....r....r....
 0000a230: 720f 0000 0072 0f00 0000 7203 0000 0072  r....r....r....r
 0000a240: 0300 0000 7203 0000 0072 0300 0000 7210  ....r....r....r.
 0000a250: 0000 007a 0f50 726f 6772 6573 7320 4469  ...z.Progress Di
-0000a260: 616c 6f67 2903 7234 0000 0072 0400 0000  alog).r4...r....
-0000a270: 5a03 3339 3129 0372 5400 0000 7204 0000  Z.391).rT...r...
+0000a260: 616c 6f67 2903 7233 0000 0072 0400 0000  alog).r3...r....
+0000a270: 5a03 3339 3129 0372 5300 0000 7204 0000  Z.391).rS...r...
 0000a280: 005a 0433 3931 617a 132c 2041 6e69 6d61  .Z.391az., Anima
 0000a290: 7469 6f6e 2049 6d61 6765 733a 7a11 2c20  tion Images:z., 
 0000a2a0: 416e 696d 6174 696f 6e20 5469 6e74 3a7a  Animation Tint:z
 0000a2b0: 112c 2046 7261 6d65 2044 7572 6174 696f  ., Frame Duratio
 0000a2c0: 6e3a 7a0b 2c20 5072 6f67 7265 7373 3afa  n:z., Progress:.
 0000a2d0: 062c 204d 6178 3a5a 0433 3932 747a 1653  ., Max:Z.392tz.S
 0000a2e0: 6574 2056 6172 6961 626c 6520 5374 7275  et Variable Stru
 0000a2f0: 6374 7572 657a 112c 2053 7472 7563 7475  cturez., Structu
 0000a300: 7265 2054 7970 653a 5a04 3339 3374 7a0b  re Type:Z.393tz.
-0000a310: 4172 7261 7920 4d65 7267 6529 0372 5000  Array Merge).rP.
+0000a310: 4172 7261 7920 4d65 7267 6529 0372 4f00  Array Merge).rO.
 0000a320: 0000 7204 0000 005a 0333 3933 7a09 2c20  ..r....Z.393z., 
 0000a330: 4a6f 696e 6572 3afa 092c 2046 6f72 6d61  Joiner:.., Forma
 0000a340: 743a 7a09 2c20 4f75 7470 7574 3a7a 0e2c  t:z., Output:z.,
 0000a350: 204a 6f69 6e20 4f75 7470 7574 3a5a 0433   Join Output:Z.3
 0000a360: 3934 7429 0d72 1700 0000 7203 0000 0072  94t).r....r....r
 0000a370: 0f00 0000 720f 0000 0072 0f00 0000 720f  ....r....r....r.
 0000a380: 0000 0072 0f00 0000 720f 0000 0072 0300  ...r....r....r..
 0000a390: 0000 7203 0000 0072 0300 0000 720f 0000  ..r....r....r...
 0000a3a0: 0072 1000 0000 7a15 5061 7273 652f 466f  .r....z.Parse/Fo
 0000a3b0: 726d 6174 2044 6174 6554 696d 6529 0a72  rmat DateTime).r
 0000a3c0: 0d00 0000 720e 0000 0072 1500 0000 7216  ....r....r....r.
-0000a3d0: 0000 0072 1d00 0000 7228 0000 0072 2e00  ...r....r(...r..
-0000a3e0: 0000 722f 0000 0072 3000 0000 7231 0000  ..r/...r0...r1..
+0000a3d0: 0000 0072 1d00 0000 7228 0000 0072 2d00  ...r....r(...r-.
+0000a3e0: 0000 722e 0000 0072 2f00 0000 7230 0000  ..r....r/...r0..
 0000a3f0: 0029 037a 0b49 6e70 7574 2054 7970 653a  .).z.Input Type:
 0000a400: 7204 0000 005a 0333 3934 7a08 2c20 496e  r....Z.394z., In
 0000a410: 7075 743a 7a0f 2c20 496e 7075 7420 466f  put:z., Input Fo
 0000a420: 726d 6174 3a7a 122c 2049 6e70 7574 2053  rmat:z., Input S
 0000a430: 6570 6172 6174 6f72 3a7a 102c 204f 7574  eparator:z., Out
 0000a440: 7075 7420 466f 726d 6174 3a7a 182c 2046  put Format:z., F
 0000a450: 6f72 6d61 7474 6564 2056 616c 7565 204e  ormatted Value N
@@ -2632,43 +2632,43 @@
 0000a470: 7420 4f66 6673 6574 2054 7970 653a 7204  t Offset Type:r.
 0000a480: 0000 005a 0433 3934 617a 102c 204f 7574  ...Z.394az., Out
 0000a490: 7075 7420 4f66 6673 6574 3a5a 0433 3935  put Offset:Z.395
 0000a4a0: 747a 094a 4420 5374 6174 7573 5a04 3339  tz.JD StatusZ.39
 0000a4b0: 3674 2905 7217 0000 0072 0300 0000 720f  6t).r....r....r.
 0000a4c0: 0000 0072 0f00 0000 720f 0000 007a 1253  ...r....r....z.S
 0000a4d0: 696d 706c 6520 4d61 7463 682f 5265 6765  imple Match/Rege
-0000a4e0: 7829 0372 4000 0000 7204 0000 005a 0333  x).r@...r....Z.3
+0000a4e0: 7829 0372 3f00 0000 7204 0000 005a 0333  x).r?...r....Z.3
 0000a4f0: 3936 7a16 2c20 4d61 7463 6820 5061 7474  96z., Match Patt
 0000a500: 6572 6e2f 5265 6765 783a 5a04 3339 3774  ern/Regex:Z.397t
 0000a510: 7a17 4765 7420 4d61 7465 7269 616c 2059  z.Get Material Y
 0000a520: 6f75 2043 6f6c 6f72 7329 0372 1200 0000  ou Colors).r....
 0000a530: 7213 0000 007a 0f4f 7574 7075 7420 4861  r....z.Output Ha
 0000a540: 7368 7461 6773 5a04 3339 3874 7a0f 436f  shtagsZ.398tz.Co
 0000a550: 6e6e 6563 7420 546f 2057 6946 695a 0433  nnect To WiFiZ.3
 0000a560: 3939 7429 0a72 1700 0000 720f 0000 0072  99t).r....r....r
 0000a570: 0f00 0000 720f 0000 0072 0f00 0000 720f  ....r....r....r.
 0000a580: 0000 0072 0300 0000 7203 0000 0072 0300  ...r....r....r..
 0000a590: 0000 720f 0000 007a 0c56 6172 6961 626c  ..r....z.Variabl
 0000a5a0: 6520 4d61 7029 0872 0d00 0000 720e 0000  e Map).r....r...
 0000a5b0: 0072 1500 0000 7216 0000 0072 1d00 0000  .r....r....r....
-0000a5c0: 7228 0000 0072 2e00 0000 722f 0000 007a  r(...r....r/...z
+0000a5c0: 7228 0000 0072 2d00 0000 722e 0000 007a  r(...r-...r....z
 0000a5d0: 0649 6e70 7574 3a7a 102c 2049 6e70 7574  .Input:z., Input
 0000a5e0: 204d 696e 696d 756d 3a7a 102c 2049 6e70   Minimum:z., Inp
 0000a5f0: 7574 204d 6178 696d 756d 3a7a 112c 204f  ut Maximum:z., O
 0000a600: 7574 7075 7420 4d69 6e69 6d75 6d3a 7a11  utput Minimum:z.
 0000a610: 2c20 4f75 7470 7574 204d 6178 696d 756d  , Output Maximum
 0000a620: 3a29 0372 1200 0000 7213 0000 007a 082c  :).r....r....z.,
 0000a630: 2049 6e76 6572 7429 0372 1200 0000 7213   Invert).r....r.
 0000a640: 0000 007a 102c 2052 6573 7472 6963 7420  ...z., Restrict 
 0000a650: 5261 6e67 657a 162c 204d 6178 2052 6f75  Rangez., Max Rou
 0000a660: 6e64 696e 6720 4469 6769 7473 3a7a 172c  nding Digits:z.,
 0000a670: 204f 7574 7075 7420 5661 7269 6162 6c65   Output Variable
 0000a680: 204e 616d 653a 5a03 3339 7429 0472 0f00   Name:Z.39t).r..
 0000a690: 0000 720f 0000 0072 0300 0000 7210 0000  ..r....r....r...
-0000a6a0: 00da 0346 6f72 5a02 3373 5a04 3430 3074  ...ForZ.3sZ.400t
+0000a6a0: 005a 0346 6f72 5a02 3373 5a04 3430 3074  .Z.ForZ.3sZ.400t
 0000a6b0: 5a04 4d6f 7665 5a04 3430 3274 7a0d 4765  Z.MoveZ.402tz.Ge
 0000a6c0: 7420 436c 6970 626f 6172 645a 0434 3034  t ClipboardZ.404
 0000a6d0: 747a 0943 6f70 7920 4669 6c65 5a04 3430  tz.Copy FileZ.40
 0000a6e0: 3574 7a08 436f 7079 2044 6972 5a04 3430  5tz.Copy DirZ.40
 0000a6f0: 3674 2905 720f 0000 0072 0300 0000 7203  6t).r....r....r.
 0000a700: 0000 0072 0300 0000 7210 0000 007a 0b44  ...r....r....z.D
 0000a710: 656c 6574 6520 4669 6c65 5a04 3430 3774  elete FileZ.407t
@@ -2684,15 +2684,15 @@
 0000a7b0: 0072 0300 0000 7203 0000 007a 1044 656c  .r....r....z.Del
 0000a7c0: 6574 6520 4469 7265 6374 6f72 797a 0a44  ete Directoryz.D
 0000a7d0: 6972 6563 746f 7279 3a29 0372 1200 0000  irectory:).r....
 0000a7e0: 7213 0000 007a 092c 2052 6563 7572 7365  r....z., Recurse
 0000a7f0: 5a04 3430 3974 7a10 4372 6561 7465 2044  Z.409tz.Create D
 0000a800: 6972 6563 746f 7279 2903 7212 0000 0072  irectory).r....r
 0000a810: 1300 0000 7a0c 2c20 4372 6561 7465 2041  ....z., Create A
-0000a820: 6c6c 5a03 3430 73da 0443 616c 6c5a 0334  llZ.40s..CallZ.4
+0000a820: 6c6c 5a03 3430 735a 0443 616c 6c5a 0334  llZ.40sZ.CallZ.4
 0000a830: 3074 7a07 456e 6420 466f 725a 0434 3130  0tz.End ForZ.410
 0000a840: 747a 0a57 7269 7465 2046 696c 6529 0372  tz.Write File).r
 0000a850: 1200 0000 7213 0000 007a 082c 2041 7070  ....r....z., App
 0000a860: 656e 6429 0372 1200 0000 7213 0000 007a  end).r....r....z
 0000a870: 0e2c 2041 6464 204e 6577 204c 696e 655a  ., Add New LineZ
 0000a880: 0434 3131 657a 0b44 6576 6963 6520 426f  .411ez.Device Bo
 0000a890: 6f74 5a04 3431 3274 2907 720f 0000 0072  otZ.412t).r....r
@@ -2703,24 +2703,24 @@
 0000a8e0: 162c 2049 6e63 6c75 6465 2048 6964 6465  ., Include Hidde
 0000a8f0: 6e20 4669 6c65 7329 037a 112c 2053 6f72  n Files).z., Sor
 0000a900: 7420 5365 6c65 6374 696f 6e3a 7204 0000  t Selection:r...
 0000a910: 005a 0334 3132 7a11 2c20 5661 7269 6162  .Z.412z., Variab
 0000a920: 6c65 2041 7272 6179 3a5a 0434 3133 747a  le Array:Z.413tz
 0000a930: 1052 6571 7565 7374 2041 6464 2054 696c  .Request Add Til
 0000a940: 6529 037a 0c54 696c 6520 546f 2041 6464  e).z.Tile To Add
-0000a950: 3a72 6900 0000 7239 0000 005a 0434 3133  :ri...r9...Z.413
+0000a950: 3a72 6700 0000 7238 0000 005a 0434 3133  :rg...r8...Z.413
 0000a960: 657a 0f44 6576 6963 6520 5368 7574 646f  ez.Device Shutdo
 0000a970: 776e 5a04 3431 3574 7a09 5265 6164 204c  wnZ.415tz.Read L
 0000a980: 696e 655a 0934 3136 3238 3334 3065 7a13  ineZ.41628340ez.
 0000a990: 4175 746f 566f 6963 6520 496e 7465 7263  AutoVoice Interc
 0000a9a0: 6570 745a 0434 3136 747a 0e52 6561 6420  eptZ.416tz.Read 
-0000a9b0: 5061 7261 6772 6170 6829 0372 4900 0000  Paragraph).rI...
-0000a9c0: 7a07 2c20 5061 7261 3a72 6800 0000 5a04  z., Para:rh...Z.
+0000a9b0: 5061 7261 6772 6170 6829 0372 4800 0000  Paragraph).rH...
+0000a9c0: 7a07 2c20 5061 7261 3a72 6600 0000 5a04  z., Para:rf...Z.
 0000a9d0: 3431 3774 7a09 5265 6164 2046 696c 6572  417tz.Read Filer
-0000a9e0: 6800 0000 5a03 3431 7429 0572 0f00 0000  h...Z.41t).r....
+0000a9e0: 6600 0000 5a03 3431 7429 0572 0f00 0000  f...Z.41t).r....
 0000a9f0: 720f 0000 0072 0300 0000 720f 0000 0072  r....r....r....r
 0000aa00: 0300 0000 7a08 5365 6e64 2053 4d53 2904  ....z.Send SMS).
 0000aa10: 7202 0000 0072 0d00 0000 7215 0000 0072  r....r....r....r
 0000aa20: 1600 0000 722b 0000 007a 0b2c 2053 494d  ....r+...z., SIM
 0000aa30: 2043 6172 643a 2903 7212 0000 0072 1300   Card:).r....r..
 0000aa40: 0000 7a11 2c20 5761 6974 2046 6f72 2052  ..z., Wait For R
 0000aa50: 6573 756c 745a 0434 3230 7429 0472 0f00  esultZ.420t).r..
@@ -2736,15 +2736,15 @@
 0000aaf0: 6520 5a69 705a 0434 3234 657a 0d53 6372  e ZipZ.424ez.Scr
 0000ab00: 6565 626c 202f 2054 5343 5a04 3432 3474  eebl / TSCZ.424t
 0000ab10: 7a10 4765 7420 4261 7474 6572 7920 496e  z.Get Battery In
 0000ab20: 666f 5a04 3432 3565 7a11 4b39 2045 6d61  foZ.425ez.K9 Ema
 0000ab30: 696c 2052 6563 6569 7665 645a 0434 3235  il ReceivedZ.425
 0000ab40: 745a 0457 6966 695a 0434 3236 657a 0d57  tZ.WifiZ.426ez.W
 0000ab50: 6964 6765 7420 4c6f 636b 6572 5a04 3432  idget LockerZ.42
-0000ab60: 3674 7a08 5769 6669 204e 6574 2903 7234  6tz.Wifi Net).r4
+0000ab60: 3674 7a08 5769 6669 204e 6574 2903 7233  6tz.Wifi Net).r3
 0000ab70: 0000 0072 0400 0000 5a03 3432 3629 0372  ...r....Z.426).r
 0000ab80: 1200 0000 7213 0000 007a 072c 2046 6f72  ....r....z., For
 0000ab90: 6365 2903 7212 0000 0072 1300 0000 7a10  ce).r....r....z.
 0000aba0: 2c20 5265 706f 7274 2046 6169 6c75 7265  , Report Failure
 0000abb0: 5a04 3432 3765 5a09 4f70 656e 5761 7463  Z.427eZ.OpenWatc
 0000abc0: 685a 0434 3237 747a 0a57 6966 6920 536c  hZ.427tz.Wifi Sl
 0000abd0: 6565 7029 037a 0750 6f6c 6963 793a 7204  eep).z.Policy:r.
@@ -2761,23 +2761,23 @@
 0000ac80: 0072 0300 0000 7210 0000 007a 0e52 6573  .r....r....z.Res
 0000ac90: 7461 7274 2054 6173 6b65 7229 0372 1200  tart Tasker).r..
 0000aca0: 0000 7213 0000 007a 0e2c 204f 6e6c 7920  ..r....z., Only 
 0000acb0: 4d6f 6e69 746f 725a 0434 3331 7429 0572  MonitorZ.431t).r
 0000acc0: 1700 0000 7203 0000 0072 0f00 0000 720f  ....r....r....r.
 0000acd0: 0000 0072 1000 0000 7a16 4163 6365 7373  ...r....z.Access
 0000ace0: 6962 696c 6974 7920 5365 7276 6963 6573  ibility Services
-0000acf0: 2903 7234 0000 0072 0400 0000 5a03 3433  ).r4...r....Z.43
+0000acf0: 2903 7233 0000 0072 0400 0000 5a03 3433  ).r3...r....Z.43
 0000ad00: 317a 0a2c 2053 6572 7669 6365 735a 0434  1z., ServicesZ.4
 0000ad10: 3333 747a 0b4d 6f62 696c 6520 4461 7461  33tz.Mobile Data
 0000ad20: 5a04 3433 3974 5a05 5769 4d61 785a 0334  Z.439tZ.WiMaxZ.4
 0000ad30: 3374 7a0c 456c 7365 2f45 6c73 6520 4966  3tz.Else/Else If
 0000ad40: 5a04 3434 3074 7a0c 5365 7420 5469 6d65  Z.440tz.Set Time
 0000ad50: 7a6f 6e65 5a04 3434 3274 5a08 536c 6565  zoneZ.442tZ.Slee
 0000ad60: 7042 6f74 5a04 3434 3374 2904 7203 0000  pBotZ.443t).r...
-0000ad70: 0072 0300 0000 7248 0000 0072 0300 0000  .r....rH...r....
+0000ad70: 0072 0300 0000 7247 0000 0072 0300 0000  .r....rG...r....
 0000ad80: 7a0d 4d65 6469 6120 436f 6e74 726f 6c29  z.Media Control)
 0000ad90: 03fa 0443 6d64 3a72 0400 0000 5a03 3434  ...Cmd:r....Z.44
 0000ada0: 3329 0372 1200 0000 7213 0000 007a 172c  3).r....r....z.,
 0000adb0: 2053 696d 756c 6174 6520 4d65 6469 6120   Simulate Media 
 0000adc0: 4275 7474 6f6e 7a13 2c20 5061 636b 6167  Buttonz., Packag
 0000add0: 652f 4170 7020 4e61 6d65 3a29 0372 1200  e/App Name:).r..
 0000ade0: 0000 7213 0000 007a 1f2c 2055 7365 204e  ..r....z., Use N
@@ -2786,16 +2786,16 @@
 0000ae10: 506f 6d6f 6472 6f69 646f 5a04 3434 3474  PomodroidoZ.444t
 0000ae20: 5a08 5465 736c 614c 4544 5a04 3434 3565  Z.TeslaLEDZ.445e
 0000ae30: 5a0a 5261 6461 7264 726f 6964 5a04 3434  Z.RadardroidZ.44
 0000ae40: 3574 2906 720f 0000 0072 0300 0000 7203  5t).r....r....r.
 0000ae50: 0000 0072 0300 0000 7203 0000 0072 1000  ...r....r....r..
 0000ae60: 0000 7a0a 4d75 7369 6320 506c 6179 7a08  ..z.Music Playz.
 0000ae70: 2c20 5374 6172 743a 2903 7212 0000 0072  , Start:).r....r
-0000ae80: 1300 0000 7a06 2c20 4c6f 6f70 2903 7277  ....z., Loop).rw
-0000ae90: 0000 0072 0400 0000 7247 0000 005a 0434  ...r....rG...Z.4
+0000ae80: 1300 0000 7a06 2c20 4c6f 6f70 2903 7272  ....z., Loop).rr
+0000ae90: 0000 0072 0400 0000 7246 0000 005a 0434  ...r....rF...Z.4
 0000aea0: 3436 657a 0c47 656e 746c 6520 416c 6172  46ez.Gentle Alar
 0000aeb0: 6d5a 0434 3437 657a 0d52 6564 6469 7420  mZ.447ez.Reddit 
 0000aec0: 4e6f 7469 6679 5a04 3434 3774 2906 720f  NotifyZ.447t).r.
 0000aed0: 0000 0072 0300 0000 7203 0000 0072 0300  ...r....r....r..
 0000aee0: 0000 7203 0000 0072 0300 0000 7a0e 4d75  ..r....r....z.Mu
 0000aef0: 7369 6320 506c 6179 2044 6972 2903 7212  sic Play Dir).r.
 0000af00: 0000 0072 1300 0000 7a09 2c20 5375 6264  ...r....z., Subd
@@ -2816,110 +2816,110 @@
 0000aff0: 7a0a 4d75 7369 6320 536b 6970 7a05 4a75  z.Music Skipz.Ju
 0000b000: 6d70 3a5a 0434 3533 657a 0f50 6163 6b61  mp:Z.453ez.Packa
 0000b010: 6765 2055 7064 6174 6564 5a04 3435 3374  ge UpdatedZ.453t
 0000b020: 7a0a 4d75 7369 6320 4261 636b 5a04 3435  z.Music BackZ.45
 0000b030: 3574 7a0c 5265 636f 7264 2041 7564 696f  5tz.Record Audio
 0000b040: 2903 7a09 2c20 536f 7572 6365 3a72 0400  ).z., Source:r..
 0000b050: 0000 5a03 3435 357a 0a2c 204d 6178 5369  ..Z.455z., MaxSi
-0000b060: 7a65 3a29 0372 7400 0000 7204 0000 005a  ze:).rt...r....Z
+0000b060: 7a65 3a29 0372 7100 0000 7204 0000 005a  ze:).rq...r....Z
 0000b070: 0434 3535 615a 0434 3536 747a 064a 4420  .455aZ.456tz.JD 
 0000b080: 4150 4e5a 0434 3537 747a 1044 6566 6175  APNZ.457tz.Defau
 0000b090: 6c74 2052 696e 6774 6f6e 655a 0434 3538  lt RingtoneZ.458
 0000b0a0: 745a 0c57 6964 6765 744c 6f63 6b65 725a  tZ.WidgetLockerZ
 0000b0b0: 0434 3539 747a 0a53 6361 6e20 4d65 6469  .459tz.Scan Medi
 0000b0c0: 615a 0434 3630 657a 1157 616c 6c70 6170  aZ.460ez.Wallpap
 0000b0d0: 6572 2043 6861 6e67 6564 5a04 3436 3165  er ChangedZ.461e
-0000b0e0: 2908 7248 0000 0072 0f00 0000 720f 0000  ).rH...r....r...
+0000b0e0: 2908 7247 0000 0072 0f00 0000 720f 0000  ).rG...r....r...
 0000b0f0: 0072 0f00 0000 720f 0000 0072 0f00 0000  .r....r....r....
 0000b100: 720f 0000 0072 0300 0000 5a0c 4e6f 7469  r....r....Z.Noti
 0000b110: 6669 6361 7469 6f6e fa0a 2c20 5375 6274  fication.., Subt
 0000b120: 6578 743a fa0b 2c20 4d65 7373 6167 6573  ext:.., Messages
 0000b130: 3afa 0d2c 204f 7468 6572 2054 6578 743a  :.., Other Text:
 0000b140: fa06 2c20 4361 743a 2903 7212 0000 0072  .., Cat:).r....r
 0000b150: 1300 0000 7a0a 2c20 4e65 7720 4f6e 6c79  ....z., New Only
 0000b160: 5a04 3436 3174 5a04 3436 3265 7a15 4275  Z.461tZ.462ez.Bu
 0000b170: 7474 6f6e 2057 6964 6765 7420 436c 6963  tton Widget Clic
 0000b180: 6b65 645a 0434 3633 657a 0a4e 6577 2057  kedZ.463ez.New W
-0000b190: 696e 646f 775a 0434 3634 6529 0672 4800  indowZ.464e).rH.
+0000b190: 696e 646f 775a 0434 3634 6529 0672 4700  indowZ.464e).rG.
 0000b1a0: 0000 720f 0000 0072 0f00 0000 720f 0000  ..r....r....r...
 0000b1b0: 0072 0f00 0000 720f 0000 007a 144e 6f74  .r....r....z.Not
 0000b1c0: 6966 6963 6174 696f 6e20 5265 6d6f 7661  ification Remova
-0000b1d0: 6c29 0672 4f00 0000 7250 0000 0072 6a00  l).rO...rP...rj.
-0000b1e0: 0000 7278 0000 0072 7900 0000 727a 0000  ..rx...ry...rz..
+0000b1d0: 6c29 0672 4e00 0000 724f 0000 0072 6800  l).rN...rO...rh.
+0000b1e0: 0000 7273 0000 0072 7400 0000 7275 0000  ..rs...rt...ru..
 0000b1f0: 005a 0334 3674 7a0c 4372 6561 7465 2053  .Z.46tz.Create S
 0000b200: 6365 6e65 5a04 3437 3574 5a04 475a 6970  ceneZ.475tZ.GZip
 0000b210: 2903 7212 0000 0072 1300 0000 7a0d 2c20  ).r....r....z., 
 0000b220: 4465 6c65 7465 204f 7269 675a 0434 3736  Delete OrigZ.476
 0000b230: 745a 0647 556e 7a69 705a 0334 3774 290c  tZ.GUnzipZ.47t).
 0000b240: 720f 0000 0072 0300 0000 7203 0000 0072  r....r....r....r
 0000b250: 0300 0000 7203 0000 0072 0300 0000 7203  ....r....r....r.
 0000b260: 0000 0072 0300 0000 7203 0000 0072 0300  ...r....r....r..
 0000b270: 0000 7203 0000 0072 1000 0000 7a0a 4469  ..r....r....z.Di
 0000b280: 7370 6c61 7920 4173 2907 7202 0000 0072  splay As).r....r
-0000b290: 0d00 0000 7227 0000 0072 2800 0000 722e  ....r'...r(...r.
-0000b2a0: 0000 0072 2f00 0000 7255 0000 0029 037a  ...r/...rU...).z
+0000b290: 0d00 0000 7227 0000 0072 2800 0000 722d  ....r'...r(...r-
+0000b2a0: 0000 0072 2e00 0000 7254 0000 0029 037a  ...r....rT...).z
 0000b2b0: 0b44 6973 706c 6179 2041 733a 7204 0000  .Display As:r...
 0000b2c0: 005a 0234 3729 0372 1200 0000 7213 0000  .Z.47).r....r...
 0000b2d0: 007a 1053 686f 7720 4578 6974 2042 7574  .z.Show Exit But
 0000b2e0: 746f 6e29 0372 1200 0000 7213 0000 007a  ton).r....r....z
 0000b2f0: 1943 6f6e 7469 6e75 6520 5461 736b 2049  .Continue Task I
 0000b300: 6d6d 6564 6961 7465 6c79 2903 7212 0000  mmediately).r...
 0000b310: 0072 1300 0000 7a18 416c 6c6f 7720 4f75  .r....z.Allow Ou
 0000b320: 7473 6964 6520 426f 756e 6461 7269 6573  tside Boundaries
 0000b330: 2903 7212 0000 0072 1300 0000 7a12 426c  ).r....r....z.Bl
 0000b340: 6f63 6b69 6e67 204f 7665 726c 6179 202b  ocking Overlay +
 0000b350: 5a03 3438 747a 0a48 6964 6520 5363 656e  Z.48tz.Hide Scen
 0000b360: 6529 037a 0a41 6e69 6d61 7469 6f6e 3a72  e).z.Animation:r
 0000b370: 0400 0000 5a02 3438 5a04 3439 3074 7a13  ....Z.48Z.490tz.
 0000b380: 4d65 6469 6120 4275 7474 6f6e 2045 7665  Media Button Eve
-0000b390: 6e74 7329 0372 4900 0000 7204 0000 005a  nts).rI...r....Z
+0000b390: 6e74 7329 0372 4800 0000 7204 0000 005a  nts).rH...r....Z
 0000b3a0: 0334 3930 2903 7212 0000 0072 1300 0000  .490).r....r....
 0000b3b0: 7a0d 2c20 5573 6520 4e65 7720 4150 495a  z., Use New APIZ
 0000b3c0: 0334 3974 7a0d 4465 7374 726f 7920 5363  .49tz.Destroy Sc
 0000b3d0: 656e 655a 0234 657a 0a50 686f 6e65 2049  eneZ.4ez.Phone I
 0000b3e0: 646c 655a 0a35 3032 3130 3231 3433 747a  dleZ.502102143tz
 0000b3f0: 1a41 7574 6f53 6865 6574 7320 4765 7420  .AutoSheets Get 
 0000b400: 5370 7265 6164 7368 6565 745a 0a35 3032  SpreadsheetZ.502
 0000b410: 3830 3736 3838 747a 1741 7574 6f41 7070  807688tz.AutoApp
 0000b420: 7348 7562 2053 656e 6443 6f6d 6d61 6e64  sHub SendCommand
 0000b430: 5a03 3530 737a 0c4b 6579 626f 6172 6420  Z.50sz.Keyboard 
 0000b440: 4f75 745a 0335 3074 7a0d 456c 656d 656e  OutZ.50tz.Elemen
-0000b450: 7420 5661 6c75 6529 0372 3d00 0000 723e  t Value).r=...r>
-0000b460: 0000 0072 3300 0000 5a04 3531 3174 5a05  ...r3...Z.511tZ.
-0000b470: 546f 7263 6829 0372 4900 0000 7204 0000  Torch).rI...r...
+0000b450: 7420 5661 6c75 6529 0372 3c00 0000 723d  t Value).r<...r=
+0000b460: 0000 0072 3200 0000 5a04 3531 3174 5a05  ...r2...Z.511tZ.
+0000b470: 546f 7263 6829 0372 4800 0000 7204 0000  Torch).rH...r...
 0000b480: 0072 2900 0000 5a04 3531 3274 7a0a 5374  .r)...Z.512tz.St
-0000b490: 6174 7573 2042 6172 2903 7249 0000 0072  atus Bar).rI...r
+0000b490: 6174 7573 2042 6172 2903 7248 0000 0072  atus Bar).rH...r
 0000b4a0: 0400 0000 5a03 3531 325a 0435 3133 747a  ....Z.512Z.513tz
 0000b4b0: 1443 6c6f 7365 2053 7973 7465 6d20 4469  .Close System Di
 0000b4c0: 616c 6f67 735a 0335 3174 2906 720f 0000  alogsZ.51t).r...
 0000b4d0: 0072 0f00 0000 7203 0000 0072 0f00 0000  .r....r....r....
 0000b4e0: 720f 0000 0072 1000 0000 7a0c 456c 656d  r....r....z.Elem
-0000b4f0: 656e 7420 5465 7874 2903 7267 0000 0072  ent Text).rg...r
+0000b4f0: 656e 7420 5465 7874 2903 7265 0000 0072  ent Text).re...r
 0000b500: 0400 0000 5a02 3531 7a0c 2c20 5365 6c65  ....Z.51z., Sele
 0000b510: 6374 696f 6e3a 5a04 3532 3374 290d 720f  ction:Z.523t).r.
-0000b520: 0000 0072 0f00 0000 7238 0000 0072 0300  ...r....r8...r..
+0000b520: 0000 0072 0f00 0000 7237 0000 0072 0300  ...r....r7...r..
 0000b530: 0000 7203 0000 0072 0300 0000 7203 0000  ..r....r....r...
 0000b540: 0072 0300 0000 7203 0000 0072 0f00 0000  .r....r....r....
 0000b550: 720f 0000 0072 0f00 0000 7210 0000 005a  r....r....r....Z
 0000b560: 064e 6f74 6966 7929 0372 1200 0000 7213  .Notify).r....r.
 0000b570: 0000 007a 0b2c 2050 6572 6d61 6e65 6e74  ...z., Permanent
 0000b580: 2903 7212 0000 0072 1300 0000 7a0e 2c20  ).r....r....z., 
 0000b590: 5265 7065 6174 2041 6c65 7274 2903 7a0c  Repeat Alert).z.
 0000b5a0: 2c20 4c45 4420 436f 6c6f 723a 7204 0000  , LED Color:r...
 0000b5b0: 005a 0335 3233 7a0b 2c20 4c45 4420 5261  .Z.523z., LED Ra
 0000b5c0: 7465 3a7a 0d2c 2053 6f75 6e64 2046 696c  te:z., Sound Fil
 0000b5d0: 653a 7a14 2c20 5669 6272 6174 696f 6e20  e:z., Vibration 
 0000b5e0: 5061 7474 6572 6e3a 7a08 4163 7469 6f6e  Pattern:z.Action
 0000b5f0: 733a 5a04 3532 3574 2908 720f 0000 0072  s:Z.525t).r....r
-0000b600: 0f00 0000 7238 0000 0072 0300 0000 7203  ....r8...r....r.
+0000b600: 0f00 0000 7237 0000 0072 0300 0000 7203  ....r7...r....r.
 0000b610: 0000 0072 0300 0000 7203 0000 0072 0300  ...r....r....r..
 0000b620: 0000 7a0a 4e6f 7469 6679 204c 4544 7a07  ..z.Notify LEDz.
 0000b630: 3a54 6974 6c65 3a7a 072c 2052 6174 653a  :Title:z., Rate:
 0000b640: 5a04 3533 3674 2907 720f 0000 0072 0f00  Z.536t).r....r..
-0000b650: 0000 7238 0000 0072 0300 0000 720f 0000  ..r8...r....r...
+0000b650: 0000 7237 0000 0072 0300 0000 720f 0000  ..r7...r....r...
 0000b660: 0072 0300 0000 7203 0000 007a 0e4e 6f74  .r....r....z.Not
 0000b670: 6966 7920 5669 6272 6174 6529 0672 0200  ify Vibrate).r..
 0000b680: 0000 720d 0000 0072 0e00 0000 7216 0000  ..r....r....r...
 0000b690: 0072 1d00 0000 7227 0000 007a 0a2c 2050  .r....r'...z., P
 0000b6a0: 6174 7465 726e 3a5a 0435 3338 747a 124e  attern:Z.538tz.N
 0000b6b0: 6f74 6966 6963 6174 696f 6e20 536f 756e  otification Soun
 0000b6c0: 6429 0572 0200 0000 720d 0000 0072 0e00  d).r....r....r..
@@ -2928,33 +2928,33 @@
 0000b6f0: 6f6e 7472 6f6c 2903 fa07 2c20 4d6f 6465  ontrol)..., Mode
 0000b700: 3a72 0400 0000 5a02 3533 5a04 3534 3374  :r....Z.53Z.543t
 0000b710: 7a12 5374 6172 7420 5379 7374 656d 2054  z.Start System T
 0000b720: 696d 6572 7a08 5365 636f 6e64 733a 2903  imerz.Seconds:).
 0000b730: 7212 0000 0072 1300 0000 7a09 2c20 5368  r....r....z., Sh
 0000b740: 6f77 2055 495a 0435 3434 747a 1454 696d  ow UIZ.544tz.Tim
 0000b750: 6572 2057 6964 6765 7420 436f 6e74 726f  er Widget Contro
-0000b760: 6c29 0372 5400 0000 7204 0000 005a 0335  l).rT...r....Z.5
+0000b760: 6c29 0372 5300 0000 7204 0000 005a 0335  l).rS...r....Z.5
 0000b770: 3434 5a04 3534 3574 7a12 5661 7269 6162  44Z.545tz.Variab
-0000b780: 6c65 2052 616e 646f 6d69 7a65 2903 7232  le Randomize).r2
-0000b790: 0000 007a 062c 204d 696e 3a72 7300 0000  ...z., Min:rs...
+0000b780: 6c65 2052 616e 646f 6d69 7a65 2903 7231  le Randomize).r1
+0000b790: 0000 007a 062c 204d 696e 3a72 7000 0000  ...z., Min:rp...
 0000b7a0: 5a04 3534 3674 7a10 5469 6d65 7220 5769  Z.546tz.Timer Wi
-0000b7b0: 6467 6574 2053 6574 2905 7232 0000 0072  dget Set).r2...r
-0000b7c0: 5b00 0000 7246 0000 0072 5c00 0000 725d  [...rF...r\...r]
+0000b7b0: 6467 6574 2053 6574 2905 7231 0000 0072  dget Set).r1...r
+0000b7c0: 5900 0000 7245 0000 0072 5a00 0000 725b  Y...rE...rZ...r[
 0000b7d0: 0000 005a 0435 3437 6529 0872 0f00 0000  ...Z.547e).r....
 0000b7e0: 720f 0000 0072 0300 0000 7203 0000 0072  r....r....r....r
 0000b7f0: 0300 0000 7203 0000 0072 0300 0000 7210  ....r....r....r.
 0000b800: 0000 00da 0875 6e6d 6170 7065 645a 0435  .....unmappedZ.5
 0000b810: 3437 7429 0372 1200 0000 7213 0000 007a  47t).r....r....z
 0000b820: 152c 2052 6563 7572 7369 7665 2056 6172  ., Recursive Var
 0000b830: 6961 626c 6573 5a04 3534 3874 e910 0000  iablesZ.548t....
 0000b840: 0029 1072 0200 0000 720d 0000 0072 0e00  .).r....r....r..
 0000b850: 0000 7215 0000 0072 1600 0000 721d 0000  ..r....r....r...
-0000b860: 0072 2700 0000 7228 0000 0072 2e00 0000  .r'...r(...r....
-0000b870: 722f 0000 0072 3000 0000 7231 0000 0072  r/...r0...r1...r
-0000b880: 4500 0000 7261 0000 0072 7000 0000 da02  E...ra...rp.....
+0000b860: 0072 2700 0000 7228 0000 0072 2d00 0000  .r'...r(...r-...
+0000b870: 722e 0000 0072 2f00 0000 7230 0000 0072  r....r/...r0...r
+0000b880: 4400 0000 725f 0000 0072 6e00 0000 5a02  D...r_...rn...Z.
 0000b890: 3135 2910 720f 0000 0072 0300 0000 7203  15).r....r....r.
 0000b8a0: 0000 0072 0f00 0000 720f 0000 0072 0f00  ...r....r....r..
 0000b8b0: 0000 720f 0000 0072 0f00 0000 720f 0000  ..r....r....r...
 0000b8c0: 0072 0300 0000 720f 0000 0072 0300 0000  .r....r....r....
 0000b8d0: 7203 0000 0072 0f00 0000 7203 0000 0072  r....r....r....r
 0000b8e0: 1000 0000 5a05 466c 6173 6829 0372 1200  ....Z.Flash).r..
 0000b8f0: 0000 7213 0000 007a 062c 204c 6f6e 6729  ..r....z., Long)
@@ -2970,45 +2970,45 @@
 0000b990: 675a 0435 3439 747a 0e56 6172 6961 626c  gZ.549tz.Variabl
 0000b9a0: 6520 436c 6561 7229 0372 1200 0000 7213  e Clear).r....r.
 0000b9b0: 0000 007a 122c 2050 6174 7465 726e 204d  ...z., Pattern M
 0000b9c0: 6174 6368 696e 6729 0372 1200 0000 7213  atching).r....r.
 0000b9d0: 0000 007a 152c 2043 6c65 6172 2041 6c6c  ...z., Clear All
 0000b9e0: 2056 6172 6961 626c 6573 5a03 3534 747a   VariablesZ.54tz
 0000b9f0: 1245 6c65 6d65 6e74 2054 6578 7420 436f  .Element Text Co
-0000ba00: 6c6f 7229 0372 3d00 0000 723e 0000 00fa  lor).r=...r>....
+0000ba00: 6c6f 7229 0372 3c00 0000 723d 0000 00fa  lor).r<...r=....
 0000ba10: 0820 436f 6c6f 7572 3a5a 0435 3530 7429  . Colour:Z.550t)
 0000ba20: 0672 0f00 0000 720f 0000 0072 0f00 0000  .r....r....r....
 0000ba30: 720f 0000 0072 0300 0000 7203 0000 005a  r....r....r....Z
 0000ba40: 0550 6f70 7570 2903 7212 0000 0072 1300  .Popup).r....r..
 0000ba50: 0000 7a14 2c20 5368 6f77 204f 7665 7220  ..z., Show Over 
-0000ba60: 4b65 7967 7561 7264 5a04 3535 3174 da04  KeyguardZ.551t..
+0000ba60: 4b65 7967 7561 7264 5a04 3535 3174 5a04  KeyguardZ.551tZ.
 0000ba70: 4d65 6e75 5a04 3535 3274 2909 720f 0000  MenuZ.552t).r...
 0000ba80: 0072 0300 0000 720f 0000 0072 0f00 0000  .r....r....r....
 0000ba90: 720f 0000 0072 0f00 0000 720f 0000 0072  r....r....r....r
 0000baa0: 0300 0000 7203 0000 007a 1250 6f70 7570  ....r....z.Popup
 0000bab0: 2054 6173 6b20 4275 7474 6f6e 7329 0372   Task Buttons).r
-0000bac0: 7c00 0000 7204 0000 005a 0335 3532 5a04  |...r....Z.552Z.
+0000bac0: 7700 0000 7204 0000 005a 0335 3532 5a04  w...r....Z.552Z.
 0000bad0: 3535 3374 7a0b 534d 5320 4261 636b 7570  553tz.SMS Backup
 0000bae0: 2b5a 0435 3535 745a 0942 6579 6f6e 6450  +Z.555tZ.BeyondP
 0000baf0: 6f64 5a04 3535 3674 5a08 4772 617a 6552  odZ.556tZ.GrazeR
 0000bb00: 5353 5a0a 3535 3736 3439 3435 3874 7a0d  SSZ.557649458tz.
 0000bb10: 4175 746f 5765 6172 2054 696d 655a 0435  AutoWear TimeZ.5
 0000bb20: 3538 747a 1041 6e64 726f 6964 204e 6f74  58tz.Android Not
 0000bb30: 6966 6965 725a 0435 3539 7429 0972 0f00  ifierZ.559t).r..
 0000bb40: 0000 720f 0000 0072 0300 0000 7203 0000  ..r....r....r...
 0000bb50: 0072 0300 0000 7203 0000 0072 0300 0000  .r....r....r....
 0000bb60: 7203 0000 0072 1000 0000 5a03 5361 797a  r....r....Z.Sayz
 0000bb70: 0f2c 2045 6e67 696e 6520 566f 6963 653a  ., Engine Voice:
 0000bb80: 2903 7a08 2c20 5374 7265 616d 7204 0000  ).z., Streamr...
-0000bb90: 0072 4700 0000 2903 7212 0000 0072 1300  .rG...).r....r..
+0000bb90: 0072 4600 0000 2903 7212 0000 0072 1300  .rF...).r....r..
 0000bba0: 0000 7a09 2c20 4e65 7477 6f72 6b5a 0335  ..z., NetworkZ.5
 0000bbb0: 3574 2905 720f 0000 0072 0f00 0000 720f  5t).r....r....r.
 0000bbc0: 0000 0072 0f00 0000 7210 0000 007a 1245  ...r....r....z.E
 0000bbd0: 6c65 6d65 6e74 2042 6163 6b20 436f 6c6f  lement Back Colo
-0000bbe0: 7229 0472 3d00 0000 723e 0000 0072 8000  r).r=...r>...r..
+0000bbe0: 7229 0472 3c00 0000 723d 0000 0072 7a00  r).r<...r=...rz.
 0000bbf0: 0000 7a0c 2045 6e64 2043 6f6c 6f75 723a  ..z. End Colour:
 0000bc00: 5a0a 3536 3332 3133 3431 3474 7a16 4175  Z.563213414tz.Au
 0000bc10: 746f 4e6f 7469 6669 6361 7469 6f6e 2054  toNotification T
 0000bc20: 6162 6c65 5a0a 3536 3533 3835 3036 3874  ableZ.565385068t
 0000bc30: 7a16 4175 746f 4e6f 7469 6669 6361 7469  z.AutoNotificati
 0000bc40: 6f6e 2051 7565 7279 5a04 3536 3674 2907  on QueryZ.566t).
 0000bc50: 7203 0000 0072 0300 0000 720f 0000 0072  r....r....r....r
@@ -3028,40 +3028,40 @@
 0000bd30: 2041 7661 696c 6162 6c65 2903 7212 0000   Available).r...
 0000bd40: 0072 1300 0000 7a09 2c20 416c 6c20 4461  .r....z., All Da
 0000bd50: 795a 0435 3638 747a 1244 6169 6c79 526f  yZ.568tz.DailyRo
 0000bd60: 6164 7320 566f 7961 6765 725a 0835 3638  ads VoyagerZ.568
 0000bd70: 3335 3033 657a 1341 7574 6f49 6e70 7574  3503ez.AutoInput
 0000bd80: 2055 4920 4163 7469 6f6e 5a03 3536 747a   UI ActionZ.56tz
 0000bd90: 0e45 6c65 6d65 6e74 2042 6f72 6465 7229  .Element Border)
-0000bda0: 0472 3d00 0000 723e 0000 00fa 082c 2057  .r=...r>....., W
+0000bda0: 0472 3c00 0000 723d 0000 00fa 082c 2057  .r<...r=....., W
 0000bdb0: 6964 7468 3a7a 092c 2043 6f6c 6f75 723a  idth:z., Colour:
 0000bdc0: 5a03 3537 7429 0672 0f00 0000 720f 0000  Z.57t).r....r...
 0000bdd0: 0072 0300 0000 7203 0000 0072 0300 0000  .r....r....r....
 0000bde0: 7203 0000 007a 0c45 6c65 6d65 6e74 2053  r....z.Element S
 0000bdf0: 697a 6529 037a 0e2c 204f 7269 656e 7461  ize).z., Orienta
 0000be00: 7469 6f6e 3a72 0400 0000 5a02 3537 7a04  tion:r....Z.57z.
 0000be10: 2c20 583a 7a04 2c20 593a 7a16 2c20 416e  , X:z., Y:z., An
 0000be20: 696d 6174 696f 6e20 5469 6d65 2028 4d53  imation Time (MS
 0000be30: 293a 5a0a 3537 3032 3337 3332 3774 7a17  ):Z.570237327tz.
 0000be40: 4175 746f 5368 6565 7473 2046 6f72 6d61  AutoSheets Forma
 0000be50: 7420 4365 6c6c 735a 0a35 3830 3935 3337  t CellsZ.5809537
 0000be60: 3939 655a 0941 7574 6f53 6861 7265 5a03  99eZ.AutoShareZ.
-0000be70: 3538 7472 8200 0000 5a04 3539 3074 7a0e  58tr....Z.590tz.
-0000be80: 5661 7269 6162 6c65 2053 706c 6974 7266  Variable Splitrf
+0000be70: 3538 7472 7b00 0000 5a04 3539 3074 7a0e  58tr{...Z.590tz.
+0000be80: 5661 7269 6162 6c65 2053 706c 6974 7264  Variable Splitrd
 0000be90: 0000 0029 0372 1200 0000 7213 0000 007a  ...).r....r....z
 0000bea0: 0d2c 2044 656c 6574 6520 4261 7365 2903  ., Delete Base).
 0000beb0: 7212 0000 0072 1300 0000 7a07 2c20 5265  r....r....z., Re
 0000bec0: 6765 785a 0435 3932 747a 0d56 6172 6961  gexZ.592tz.Varia
 0000bed0: 626c 6520 4a6f 696e 2903 7212 0000 0072  ble Join).r....r
 0000bee0: 1300 0000 7a0e 2c20 4465 6c65 7465 2050  ....z., Delete P
 0000bef0: 6172 7473 5a04 3539 3574 2908 720f 0000  artsZ.595t).r...
 0000bf00: 0072 0f00 0000 7203 0000 0072 0f00 0000  .r....r....r....
 0000bf10: 720f 0000 0072 0f00 0000 7203 0000 0072  r....r....r....r
 0000bf20: 0300 0000 7a0e 5661 7269 6162 6c65 2051  ....z.Variable Q
-0000bf30: 7565 7279 2903 726c 0000 0072 0400 0000  uery).rl...r....
+0000bf30: 7565 7279 2903 726a 0000 0072 0400 0000  uery).rj...r....
 0000bf40: 5a03 3539 357a 0a2c 2044 6566 6175 6c74  Z.595z., Default
 0000bf50: 3a5a 0435 3936 7429 0472 0f00 0000 7203  :Z.596t).r....r.
 0000bf60: 0000 0072 0f00 0000 7203 0000 007a 1056  ...r....r....z.V
 0000bf70: 6172 6961 626c 6520 436f 6e76 6572 7429  ariable Convert)
 0000bf80: 03fa 0b2c 2046 756e 6374 696f 6e3a 7204  ..., Function:r.
 0000bf90: 0000 005a 0335 3936 5a04 3539 3774 2905  ...Z.596Z.597t).
 0000bfa0: 720f 0000 0072 0300 0000 7203 0000 0072  r....r....r....r
@@ -3083,110 +3083,110 @@
 0000c0a0: 6368 204f 6e6c 797a 182c 2053 686f 7720  ch Onlyz., Show 
 0000c0b0: 4d61 7463 6865 7320 496e 2041 7272 6179  Matches In Array
 0000c0c0: 3a29 0372 1200 0000 7213 0000 007a 112c  :).r....r....z.,
 0000c0d0: 2052 6570 6c61 6365 204d 6174 6368 6573   Replace Matches
 0000c0e0: 5a04 3539 3965 2905 720f 0000 0072 0300  Z.599e).r....r..
 0000c0f0: 0000 7203 0000 0072 0f00 0000 720f 0000  ..r....r....r...
 0000c100: 007a 0f49 6e74 656e 7420 5265 6365 6976  .z.Intent Receiv
-0000c110: 6564 2903 727b 0000 0072 0400 0000 da03  ed).r{...r......
+0000c110: 6564 2903 7276 0000 0072 0400 0000 da03  ed).rv...r......
 0000c120: 3837 377a 092c 2053 6368 656d 613a 2903  877z., Schema:).
 0000c130: 7212 0000 0072 1300 0000 7a0c 2c20 5374  r....r....z., St
 0000c140: 6f70 2045 7665 6e74 5a04 3539 3974 7a09  op EventZ.599tz.
 0000c150: 4475 6520 546f 6461 795a 0335 3974 5a06  Due TodayZ.59tZ.
 0000c160: 5265 626f 6f74 5a02 3573 7a0e 4361 6c65  RebootZ.5sz.Cale
 0000c170: 6e64 6172 2045 6e74 7279 5a03 3630 7429  ndar EntryZ.60t)
 0000c180: 0972 0f00 0000 720f 0000 0072 0f00 0000  .r....r....r....
 0000c190: 720f 0000 0072 0f00 0000 7203 0000 0072  r....r....r....r
-0000c1a0: 0300 0000 720f 0000 0072 3800 0000 7a15  ....r....r8...z.
+0000c1a0: 0300 0000 720f 0000 0072 3700 0000 7a15  ....r....r7...z.
 0000c1b0: 456c 656d 656e 7420 4164 6420 4765 6f4d  Element Add GeoM
-0000c1c0: 6172 6b65 7229 0672 3d00 0000 723e 0000  arker).r=...r>..
+0000c1c0: 6172 6b65 7229 0672 3c00 0000 723d 0000  arker).r<...r=..
 0000c1d0: 007a 0b2c 204c 6174 2c4c 6f6e 673a 7222  .z., Lat,Long:r"
 0000c1e0: 0000 007a 172c 2053 706f 7420 5261 6469  ...z., Spot Radi
 0000c1f0: 7573 2028 4d65 7465 7273 293a 7a0d 2c20  us (Meters):z., 
 0000c200: 5370 6f74 2043 6f6c 6f72 3a5a 0436 3132  Spot Color:Z.612
 0000c210: 747a 1545 6c65 6d65 6e74 2056 6964 656f  tz.Element Video
-0000c220: 2043 6f6e 7472 6f6c 2903 727c 0000 0072   Control).r|...r
+0000c220: 2043 6f6e 7472 6f6c 2903 7277 0000 0072   Control).rw...r
 0000c230: 0400 0000 5a03 3631 327a 0f2c 204d 696c  ....Z.612z., Mil
 0000c240: 6c69 5365 636f 6e64 733a 5a03 3631 745a  liSeconds:Z.61tZ
 0000c250: 0756 6962 7261 7465 7a05 5469 6d65 3a5a  .Vibratez.Time:Z
 0000c260: 0336 3274 7a0f 5669 6272 6174 6520 5061  .62tz.Vibrate Pa
 0000c270: 7474 6572 6e7a 0850 6174 7465 726e 3a5a  tternz.Pattern:Z
 0000c280: 0336 3374 7a18 456c 656d 656e 7420 4465  .63tz.Element De
 0000c290: 6c65 7465 2047 656f 4d61 726b 6572 2904  lete GeoMarker).
-0000c2a0: 723d 0000 0072 3e00 0000 7a0a 204c 6174  r=...r>...z. Lat
+0000c2a0: 723c 0000 0072 3d00 0000 7a0a 204c 6174  r<...r=...z. Lat
 0000c2b0: 2c4c 6f6e 673a 7a07 204c 6162 656c 3a5a  ,Long:z. Label:Z
 0000c2c0: 0436 3433 745a 0a4f 6666 6963 6554 616c  .643tZ.OfficeTal
 0000c2d0: 6b5a 0336 3474 7a13 456c 656d 656e 7420  kZ.64tz.Element 
-0000c2e0: 4d61 7020 436f 6e74 726f 6c29 0372 7c00  Map Control).r|.
+0000c2e0: 4d61 7020 436f 6e74 726f 6c29 0372 7700  Map Control).rw.
 0000c2f0: 0000 7204 0000 005a 0236 345a 0436 3537  ..r....Z.64Z.657
 0000c300: 747a 1152 6563 6f72 6420 4175 6469 6f20  tz.Record Audio 
 0000c310: 5374 6f70 5a03 3635 7429 0672 0f00 0000  StopZ.65t).r....
 0000c320: 720f 0000 0072 0300 0000 7203 0000 0072  r....r....r....r
 0000c330: 0300 0000 7210 0000 007a 1245 6c65 6d65  ....r....z.Eleme
 0000c340: 6e74 2056 6973 6962 696c 6974 797a 102c  nt Visibilityz.,
 0000c350: 2045 6c65 6d65 6e74 204d 6174 6368 3a29   Element Match:)
-0000c360: 0372 6d00 0000 7204 0000 005a 0236 357a  .rm...r....Z.65z
+0000c360: 0372 6b00 0000 7204 0000 005a 0236 357a  .rk...r....Z.65z
 0000c370: 1441 6e69 6d61 7469 6f6e 2054 696d 6520  .Animation Time 
 0000c380: 284d 5329 3a5a 0a36 3538 3532 3733 3732  (MS):Z.658527372
 0000c390: 747a 1341 7574 6f54 6f6f 6c73 2048 544d  tz.AutoTools HTM
 0000c3a0: 4c20 5265 6164 5a04 3636 3474 290a 720f  L ReadZ.664t).r.
 0000c3b0: 0000 0072 0f00 0000 720f 0000 0072 0f00  ...r....r....r..
 0000c3c0: 0000 720f 0000 0072 0f00 0000 720f 0000  ..r....r....r...
 0000c3d0: 0072 0f00 0000 720f 0000 0072 0f00 0000  .r....r....r....
 0000c3e0: 7a0d 4a61 7661 2046 756e 6374 696f 6e7a  z.Java Functionz
 0000c3f0: 1043 6c61 7373 206f 7220 4f62 6a65 6374  .Class or Object
-0000c400: 3a72 8300 0000 5a04 3636 3574 7a0b 4a61  :r....Z.665tz.Ja
+0000c400: 3a72 7c00 0000 5a04 3636 3574 7a0b 4a61  :r|...Z.665tz.Ja
 0000c410: 7661 204f 626a 6563 7429 0372 2100 0000  va Object).r!...
 0000c420: 7204 0000 005a 0336 3635 5a04 3636 3774  r....Z.665Z.667t
 0000c430: 7a09 5351 4c20 5175 6572 795a 0336 3674  z.SQL QueryZ.66t
-0000c440: 2904 720f 0000 0072 0f00 0000 7238 0000  ).r....r....r8..
+0000c440: 2904 720f 0000 0072 0f00 0000 7237 0000  ).r....r....r7..
 0000c450: 0072 1000 0000 7a0d 456c 656d 656e 7420  .r....z.Element 
-0000c460: 496d 6167 6529 0372 3d00 0000 723e 0000  Image).r=...r>..
-0000c470: 0072 6e00 0000 5a03 3637 747a 0d45 6c65  .rn...Z.67tz.Ele
-0000c480: 6d65 6e74 2044 6570 7468 2903 723d 0000  ment Depth).r=..
-0000c490: 0072 3e00 0000 7a0c 2c20 5365 7420 4465  .r>...z., Set De
+0000c460: 496d 6167 6529 0372 3c00 0000 723d 0000  Image).r<...r=..
+0000c470: 0072 6c00 0000 5a03 3637 747a 0d45 6c65  .rl...Z.67tz.Ele
+0000c480: 6d65 6e74 2044 6570 7468 2903 723c 0000  ment Depth).r<..
+0000c490: 0072 3d00 0000 7a0c 2c20 5365 7420 4465  .r=...z., Set De
 0000c4a0: 7074 683a 5a03 3638 747a 0d45 6c65 6d65  pth:Z.68tz.Eleme
 0000c4b0: 6e74 2046 6f63 7573 2903 7212 0000 0072  nt Focus).r....r
 0000c4c0: 1300 0000 7a05 2c20 5365 745a 0436 3937  ....z., SetZ.697
 0000c4d0: 747a 0753 6875 7420 5570 5a04 3639 3974  tz.Shut UpZ.699t
 0000c4e0: 2907 720f 0000 0072 0f00 0000 720f 0000  ).r....r....r...
 0000c4f0: 0072 0300 0000 7203 0000 0072 0300 0000  .r....r....r....
 0000c500: 7203 0000 007a 0b53 6179 2054 6f20 4669  r....z.Say To Fi
 0000c510: 6c65 7a0f 2c20 456e 6769 6e65 2f56 6f69  lez., Engine/Voi
 0000c520: 6365 3a5a 0336 3974 7a0e 456c 656d 656e  ce:Z.69tz.Elemen
-0000c530: 7420 4372 6561 7465 2903 726d 0000 0072  t Create).rm...r
+0000c530: 7420 4372 6561 7465 2903 726b 0000 0072  t Create).rk...r
 0000c540: 0400 0000 5a02 3639 2903 7212 0000 0072  ....Z.69).r....r
 0000c550: 1300 0000 7a09 2c20 5669 7369 626c 655a  ....z., VisibleZ
 0000c560: 0236 657a 0d50 686f 6e65 2052 696e 6769  .6ez.Phone Ringi
 0000c570: 6e67 5a02 3673 5a04 3730 3174 5a04 4470  ngZ.6sZ.701tZ.Dp
 0000c580: 6164 5a04 3730 3274 da04 5479 7065 5a0a  adZ.702t..TypeZ.
 0000c590: 3730 3339 3533 3130 3374 7a13 4b4c 5750  703953103tz.KLWP
 0000c5a0: 204c 6976 6520 5761 6c6c 7061 7065 725a   Live WallpaperZ
-0000c5b0: 0437 3033 74da 0642 7574 746f 6e5a 0337  .703t..ButtonZ.7
+0000c5b0: 0437 3033 745a 0642 7574 746f 6e5a 0337  .703tZ.ButtonZ.7
 0000c5c0: 3174 7a11 456c 656d 656e 7420 5465 7874  1tz.Element Text
-0000c5d0: 2053 697a 6529 0372 3d00 0000 723e 0000   Size).r=...r>..
+0000c5d0: 2053 697a 6529 0372 3c00 0000 723d 0000   Size).r<...r=..
 0000c5e0: 00fa 0c2c 2054 6578 7420 5369 7a65 3a5a  ..., Text Size:Z
 0000c5f0: 0437 3231 747a 0f5a 6f6f 6d20 5669 7369  .721tz.Zoom Visi
 0000c600: 6269 6c69 7479 fa08 456c 656d 656e 743a  bility..Element:
 0000c610: 5a04 3733 3174 7a09 5461 6b65 2043 616c  Z.731tz.Take Cal
 0000c620: 6c5a 0437 3332 745a 0552 6164 696f 5a04  lZ.732tZ.RadioZ.
 0000c630: 3733 3374 7a08 456e 6420 4361 6c6c 5a04  733tz.End CallZ.
 0000c640: 3733 3474 7a0e 5369 6c65 6e63 6520 5269  734tz.Silence Ri
 0000c650: 6e67 6572 5a04 3733 3574 7a11 4d6f 6269  ngerZ.735tz.Mobi
 0000c660: 6c65 2044 6174 6120 3247 2f33 475a 0337  le Data 2G/3GZ.7
 0000c670: 3374 7a0f 456c 656d 656e 7420 4465 7374  3tz.Element Dest
 0000c680: 726f 795a 0437 3430 747a 095a 6f6f 6d20  royZ.740tz.Zoom 
 0000c690: 5465 7874 5a04 3734 3174 7a0e 5a6f 6f6d  TextZ.741tz.Zoom
-0000c6a0: 2054 6578 7420 5369 7a65 7287 0000 005a   Text Sizer....Z
+0000c6a0: 2054 6578 7420 5369 7a65 727f 0000 005a   Text Sizer....Z
 0000c6b0: 0437 3432 747a 0f5a 6f6f 6d20 5465 7874  .742tz.Zoom Text
 0000c6c0: 2043 6f6c 6f72 5a04 3736 3074 7a0a 5a6f   ColorZ.760tz.Zo
-0000c6d0: 6f6d 2041 6c70 6861 726d 0000 005a 0437  om Alpharm...Z.7
+0000c6d0: 6f6d 2041 6c70 6861 726b 0000 005a 0437  om Alphark...Z.7
 0000c6e0: 3631 747a 0a5a 6f6f 6d20 496d 6167 655a  61tz.Zoom ImageZ
 0000c6f0: 0437 3632 747a 0a5a 6f6f 6d20 436f 6c6f  .762tz.Zoom Colo
-0000c700: 7229 0372 8800 0000 7a08 2c20 436f 6c6f  r).r....z., Colo
+0000c700: 7229 0372 8000 0000 7a08 2c20 436f 6c6f  r).r....z., Colo
 0000c710: 723a 7a0c 2c20 456e 6420 436f 6c6f 723a  r:z., End Color:
 0000c720: 5a0a 3737 3433 3531 3930 3674 7a0b 4a6f  Z.774351906tz.Jo
 0000c730: 696e 2041 6374 696f 6e5a 0437 3735 747a  in ActionZ.775tz
 0000c740: 0c57 7269 7465 2042 696e 6172 795a 0437  .Write BinaryZ.7
 0000c750: 3736 747a 0b52 6561 6420 4269 6e61 7279  76tz.Read Binary
 0000c760: 5a0a 3737 3836 3832 3236 3774 7a12 4175  Z.778682267tz.Au
 0000c770: 746f 496e 7075 7420 4765 7374 7572 6573  toInput Gestures
@@ -3195,15 +3195,15 @@
 0000c7a0: 745a 0437 3933 747a 0a5a 6f6f 6d20 5374  tZ.793tz.Zoom St
 0000c7b0: 6174 657a 082c 2053 7461 7465 3a5a 0437  atez., State:Z.7
 0000c7c0: 3934 747a 0d5a 6f6f 6d20 506f 7369 7469  94tz.Zoom Positi
 0000c7d0: 6f6e 5a04 3739 3574 7a09 5a6f 6f6d 2053  onZ.795tz.Zoom S
 0000c7e0: 697a 65da 0237 6529 0572 0300 0000 720f  ize..7e).r....r.
 0000c7f0: 0000 0072 0f00 0000 720f 0000 0072 0f00  ...r....r....r..
 0000c800: 0000 7a0d 5265 6365 6976 6564 2054 6578  ..z.Received Tex
-0000c810: 7429 0372 4000 0000 7204 0000 0072 8900  t).r@...r....r..
+0000c810: 7429 0372 3f00 0000 7204 0000 0072 8100  t).r?...r....r..
 0000c820: 0000 7a09 2c20 5365 6e64 6572 3a7a 0b2c  ..z., Sender:z.,
 0000c830: 204d 4d53 2042 6f64 793a 5a02 3773 7a09   MMS Body:Z.7sz.
 0000c840: 4365 6c6c 204e 6561 725a 0438 3034 747a  Cell NearZ.804tz
 0000c850: 1349 6e70 7574 204d 6574 686f 6420 5365  .Input Method Se
 0000c860: 6c65 6374 5a04 3830 3674 7a07 5475 726e  lectZ.806tz.Turn
 0000c870: 204f 6e7a 0b42 6c6f 636b 2054 696d 653a   Onz.Block Time:
 0000c880: 5a04 3830 3874 7a0f 4175 746f 2042 7269  Z.808tz.Auto Bri
@@ -3215,46 +3215,46 @@
 0000c8e0: 0372 1200 0000 7213 0000 007a 162c 2049  .r....r....z., I
 0000c8f0: 676e 6f72 6520 4375 7272 656e 7420 4c65  gnore Current Le
 0000c900: 7665 6c5a 0a38 3131 3037 3931 3033 747a  velZ.811079103tz
 0000c910: 1741 7574 6f49 6e70 7574 2047 6c6f 6261  .AutoInput Globa
 0000c920: 6c20 4163 7469 6f6e 5a04 3831 3274 7a0f  l ActionZ.812tz.
 0000c930: 4469 7370 6c61 7920 5469 6d65 6f75 7429  Display Timeout)
 0000c940: 037a 0553 6563 733a 7a07 2c20 4d69 6e73  .z.Secs:z., Mins
-0000c950: 3a72 5c00 0000 5a04 3831 3574 7a09 4c69  :r\...Z.815tz.Li
-0000c960: 7374 2041 7070 7329 0372 4000 0000 7204  st Apps).r@...r.
+0000c950: 3a72 5a00 0000 5a04 3831 3574 7a09 4c69  :rZ...Z.815tz.Li
+0000c960: 7374 2041 7070 7329 0372 3f00 0000 7204  st Apps).r?...r.
 0000c970: 0000 005a 0338 3135 5a04 3832 3074 7a07  ...Z.815Z.820tz.
 0000c980: 5374 6179 204f 6e29 0372 2100 0000 7204  Stay On).r!...r.
 0000c990: 0000 005a 0338 3230 5a04 3832 3274 7a12  ...Z.820Z.822tz.
 0000c9a0: 4469 7370 6c61 7920 4175 746f 726f 7461  Display Autorota
 0000c9b0: 7465 5a0a 3836 3436 3932 3735 3274 5a04  teZ.864692752tZ.
 0000c9c0: 3837 3774 290b 720f 0000 0072 0300 0000  877t).r....r....
 0000c9d0: 720f 0000 0072 0f00 0000 720f 0000 0072  r....r....r....r
 0000c9e0: 0f00 0000 720f 0000 0072 0f00 0000 720f  ....r....r....r.
 0000c9f0: 0000 0072 0300 0000 7210 0000 007a 0b53  ...r....r....z.S
-0000ca00: 656e 6420 496e 7465 6e74 2903 727c 0000  end Intent).r|..
-0000ca10: 0072 0400 0000 7284 0000 007a 082c 2045  .r....r....z., E
+0000ca00: 656e 6420 496e 7465 6e74 2903 7277 0000  end Intent).rw..
+0000ca10: 0072 0400 0000 727d 0000 007a 082c 2045  .r....r}...z., E
 0000ca20: 7874 7261 3a7a 082c 2043 6c61 7373 3a29  xtra:z., Class:)
 0000ca30: 037a 092c 2054 6172 6765 743a 7204 0000  .z., Target:r...
 0000ca40: 005a 0438 3737 615a 0438 3838 747a 0c56  .Z.877aZ.888tz.V
-0000ca50: 6172 6961 626c 6520 4164 6429 0372 3200  ariable Add).r2.
-0000ca60: 0000 7233 0000 007a 0e2c 2057 7261 7020  ..r3...z., Wrap 
+0000ca50: 6172 6961 626c 6520 4164 6429 0372 3100  ariable Add).r1.
+0000ca60: 0000 7232 0000 007a 0e2c 2057 7261 7020  ..r2...z., Wrap 
 0000ca70: 4172 6f75 6e64 3a5a 0438 3930 747a 1156  Around:Z.890tz.V
 0000ca80: 6172 6961 626c 6520 5375 6274 7261 6374  ariable Subtract
 0000ca90: 5a02 3865 7a11 5265 6365 6976 6564 2044  Z.8ez.Received D
 0000caa0: 6174 6120 534d 535a 0439 3030 747a 0c42  ata SMSZ.900tz.B
 0000cab0: 726f 7773 6520 4669 6c65 735a 0439 3031  rowse FilesZ.901
 0000cac0: 747a 0d53 746f 7020 4c6f 6361 7469 6f6e  tz.Stop Location
 0000cad0: 2903 721b 0000 0072 0400 0000 5a03 3930  ).r....r....Z.90
 0000cae0: 315a 0439 3032 747a 0c47 6574 204c 6f63  1Z.902tz.Get Loc
 0000caf0: 6174 696f 6e29 0372 1200 0000 7213 0000  ation).r....r...
 0000cb00: 007a 0f2c 204b 6565 7020 5472 6163 6b69  .z., Keep Tracki
 0000cb10: 6e67 5a04 3930 3374 2907 720f 0000 0072  ngZ.903t).r....r
 0000cb20: 0300 0000 720f 0000 0072 0300 0000 7203  ....r....r....r.
 0000cb30: 0000 0072 0300 0000 7217 0000 007a 0947  ...r....r....z.G
-0000cb40: 6574 2056 6f69 6365 2903 727c 0000 0072  et Voice).r|...r
+0000cb40: 6574 2056 6f69 6365 2903 7277 0000 0072  et Voice).rw...r
 0000cb50: 0400 0000 5a03 3930 337a 0b2c 204c 616e  ....Z.903z., Lan
 0000cb60: 6775 6167 653a 7a12 2c20 4d61 7869 6d75  guage:z., Maximu
 0000cb70: 6d20 5265 7375 6c74 733a 2903 7212 0000  m Results:).r...
 0000cb80: 0072 1300 0000 7a0d 2c20 4869 6465 2044  .r....z., Hide D
 0000cb90: 6961 6c6f 675a 0439 3034 747a 0d56 6f69  ialogZ.904tz.Voi
 0000cba0: 6365 2043 6f6d 6d61 6e64 5a04 3930 3574  ce CommandZ.905t
 0000cbb0: 7a0d 4c6f 6361 7469 6f6e 204d 6f64 6529  z.Location Mode)
@@ -3301,15 +3301,15 @@
 0000ce40: 645a 0439 3838 747a 0843 6172 204d 6f64  dZ.988tz.Car Mod
 0000ce50: 6529 0372 1200 0000 7213 0000 007a 092c  e).r....r....z.,
 0000ce60: 2047 6f20 486f 6d65 5a04 3938 3974 7a0a   Go HomeZ.989tz.
 0000ce70: 4e69 6768 7420 4d6f 6465 5a04 3939 3974  Night ModeZ.999t
 0000ce80: 7a09 5365 7420 4c69 6768 745a 0339 3974  z.Set LightZ.99t
 0000ce90: 7a0b 4361 6c6c 2052 6576 6572 744e 2901  z.Call RevertN).
 0000cea0: da0c 6163 7469 6f6e 5f63 6f64 6573 a900  ..action_codes..
-0000ceb0: 728b 0000 0072 8b00 0000 fa76 2f55 7365  r....r.....v/Use
+0000ceb0: 7283 0000 0072 8300 0000 fa76 2f55 7365  r....r.....v/Use
 0000cec0: 7273 2f6d 696b 7275 6269 6e2f 4c69 6272  rs/mikrubin/Libr
 0000ced0: 6172 792f 436c 6f75 6453 746f 7261 6765  ary/CloudStorage
 0000cee0: 2f47 6f6f 676c 6544 7269 7665 2d6d 696b  /GoogleDrive-mik
 0000cef0: 7275 6269 6e40 676d 6169 6c2e 636f 6d2f  rubin@gmail.com/
 0000cf00: 4d79 2044 7269 7665 2f50 7974 686f 6e2f  My Drive/Python/
 0000cf10: 6d61 7074 6173 6b65 722f 6d61 7074 6173  maptasker/maptas
 0000cf20: 6b65 722f 7372 632f 6163 7469 6f6e 632e  ker/src/actionc.
```

### Comparing `maptasker-1.3.1/maptasker/src/__pycache__/actiond.cpython-310.pyc` & `maptasker-1.3.2/maptasker/src/__pycache__/actiond.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Sun Feb 19 16:04:35 2023 UTC, .py size: 6713 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 9348 f263 391a 0000  o........H.c9...
+00000000: 6f0d 0d0a 0000 0000 918f 1c64 391a 0000  o..........d9...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 000a 0000 0040 0000 0073 2001 0000 6400  .....@...s ...d.
 00000030: 6401 6c00 5a01 6400 6402 6c02 6d03 5a03  d.l.Z.d.d.l.m.Z.
 00000040: 0100 6400 6401 6c04 6d05 0200 0100 6d06  ..d.d.l.m.....m.
 00000050: 5a07 0100 6400 6403 6c08 6d09 5a09 0100  Z...d.d.l.m.Z...
 00000060: 6400 6404 6c0a 6d0b 5a0b 0100 6700 6405  d.d.l.m.Z...g.d.
 00000070: a201 5a0c 6406 6501 6a0d 6a0e 6602 6407  ..Z.d.e.j.j.f.d.
```

### Comparing `maptasker-1.3.1/maptasker/src/__pycache__/actione.cpython-310.pyc` & `maptasker-1.3.2/maptasker/src/__pycache__/actione.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Tue Mar  7 17:15:47 2023 UTC, .py size: 8850 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 20% similar despite different names*

```diff
@@ -1,222 +1,256 @@
-00000000: 6f0d 0d0a 0000 0000 4371 0764 9222 0000  o.......Cq.d."..
+00000000: 6f0d 0d0a 0000 0000 ee5e 2c64 c625 0000  o........^,d.%..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
-00000020: 000e 0000 0040 0000 0073 b600 0000 6400  .....@...s....d.
+00000020: 000e 0000 0040 0000 0073 c200 0000 6400  .....@...s....d.
 00000030: 6401 6c00 5a00 6400 6401 6c01 5a01 6400  d.l.Z.d.d.l.Z.d.
 00000040: 6401 6c02 5a03 6400 6401 6c04 6d05 0200  d.l.Z.d.d.l.m...
 00000050: 0100 6d06 5a07 0100 6400 6402 6c08 6d09  ..m.Z...d.d.l.m.
 00000060: 5a09 0100 6400 6403 6c0a 6d0b 5a0b 0100  Z...d.d.l.m.Z...
 00000070: 6400 6404 6c0c 6d0d 5a0d 0100 6400 6405  d.d.l.m.Z...d.d.
-00000080: 6c0e 6d0f 5a0f 0100 6501 a010 6406 a101  l.m.Z...e...d...
-00000090: 5a11 6407 6408 8400 5a12 6409 640a 8400  Z.d.d...Z.d.d...
-000000a0: 5a13 640b 640c 8400 5a14 640d 6503 6a15  Z.d.d...Z.d.e.j.
-000000b0: 6a16 640e 6503 6a15 6a16 640f 6517 6410  j.d.e.j.j.d.e.d.
-000000c0: 6518 6411 6519 6412 6518 6413 6519 660e  e.d.e.d.e.d.e.f.
-000000d0: 6414 6415 8404 5a1a 6416 6417 8400 5a1b  d.d...Z.d.d...Z.
-000000e0: 6401 5300 2918 e900 0000 004e 2901 da0e  d.S.)......N)...
-000000f0: 434f 4e54 494e 5545 5f4c 494d 4954 2901  CONTINUE_LIMIT).
-00000100: da0f 6765 745f 6578 7472 615f 7374 7566  ..get_extra_stuf
-00000110: 6629 01da 0c61 6374 696f 6e5f 636f 6465  f)...action_code
-00000120: 7329 01da 066c 6f67 6765 727a 062c 5b2c  s)...loggerz.,[,
-00000130: 205d 2b63 0100 0000 0000 0000 0000 0000   ]+c............
-00000140: 0100 0000 0400 0000 4300 0000 7394 0000  ........C...s...
-00000150: 007c 00a0 0064 0164 02a1 027d 007c 00a0  .|...d.d...}.|..
-00000160: 0064 0364 04a1 027d 0074 01a0 0264 057c  .d.d...}.t...d.|
-00000170: 00a1 027d 007c 00a0 0064 0664 07a1 027d  ...}.|...d.d...}
-00000180: 007c 00a0 0064 0864 09a1 027d 007c 00a0  .|...d.d...}.|..
-00000190: 0064 0a64 04a1 027d 007c 00a0 0064 0b64  .d.d...}.|...d.d
-000001a0: 04a1 027d 007c 00a0 0064 0c64 04a1 027d  ...}.|...d.d...}
-000001b0: 007c 00a0 0064 0d64 04a1 027d 007c 00a0  .|...d.d...}.|..
-000001c0: 0064 0e64 04a1 027d 007c 00a0 0064 0f64  .d.d...}.|...d.d
-000001d0: 04a1 027d 007c 00a0 0064 1064 11a1 027d  ...}.|...d.d...}
-000001e0: 007c 0053 0029 124e 7a09 2c20 203c 666f  .|.S.).Nz.,  <fo
-000001f0: 6e74 3e7a 063c 666f 6e74 3e7a 032c 2028  nt>z.<font>z., (
-00000200: da00 7a02 2c20 7a07 2c20 3c73 7061 6e7a  ..z., z., <spanz
-00000210: 053c 7370 616e 7a08 2c20 203c 7370 616e  .<spanz.,  <span
-00000220: 7a07 2020 3c73 7061 6e7a 072c 2063 6f64  z.  <spanz., cod
-00000230: 653a 7a05 3c62 6967 3e7a 073c 736d 616c  e:z.<big>z.<smal
-00000240: 6c3e 7a04 3c74 743e 7a03 3c69 3e7a 033c  l>z.<tt>z.<i>z.<
-00000250: 753e 7a07 2c20 3c66 6f6e 747a 053c 666f  u>z., <fontz.<fo
-00000260: 6e74 2903 da07 7265 706c 6163 65da 0770  nt)...replace..p
-00000270: 6174 7465 726e da03 7375 6229 01da 0772  attern..sub)...r
-00000280: 6573 756c 7473 a900 720b 0000 00fa 762f  esults..r.....v/
-00000290: 5573 6572 732f 6d69 6b72 7562 696e 2f4c  Users/mikrubin/L
-000002a0: 6962 7261 7279 2f43 6c6f 7564 5374 6f72  ibrary/CloudStor
-000002b0: 6167 652f 476f 6f67 6c65 4472 6976 652d  age/GoogleDrive-
-000002c0: 6d69 6b72 7562 696e 4067 6d61 696c 2e63  mikrubin@gmail.c
-000002d0: 6f6d 2f4d 7920 4472 6976 652f 5079 7468  om/My Drive/Pyth
-000002e0: 6f6e 2f6d 6170 7461 736b 6572 2f6d 6170  on/maptasker/map
-000002f0: 7461 736b 6572 2f73 7263 2f61 6374 696f  tasker/src/actio
-00000300: 6e65 2e70 79da 1263 6c65 616e 7570 5f74  ne.py..cleanup_t
-00000310: 6865 5f72 6573 756c 741e 0000 0073 1e00  he_result....s..
-00000320: 0000 0403 0401 04ff 0c03 0c01 0c01 0c01  ................
-00000330: 0c01 0c01 0c01 0c01 0c01 0c01 0c01 0401  ................
-00000340: 720d 0000 0063 0000 0000 0000 0000 0000  r....c..........
-00000350: 0000 0500 0000 0500 0000 4300 0000 739c  ..........C...s.
-00000360: 0000 0064 017d 0074 0044 005d 3f7d 0174  ...d.}.t.D.]?}.t
-00000370: 007c 0119 007d 027c 0264 0219 007d 037c  .|...}.|.d...}.|
-00000380: 0364 036b 0472 2a64 047c 0276 0172 2a64  .d.k.r*d.|.v.r*d
-00000390: 057c 019b 0064 067c 039b 009d 047d 0474  .|...d.|.....}.t
-000003a0: 017c 0483 0101 0074 02a0 037c 049b 00a1  .|.....t...|....
-000003b0: 0101 0064 077d 0064 087c 0276 0172 4364  ...d.}.d.|.v.rCd
-000003c0: 057c 019b 0064 099d 037d 0474 017c 0483  .|...d...}.t.|..
-000003d0: 0101 0074 02a0 037c 04a1 0101 0064 0a7c  ...t...|.....d.|
-000003e0: 0264 083c 0064 077d 0071 047c 0072 4c74  .d.<.d.}.q.|.rLt
-000003f0: 0464 0b83 0101 0064 0053 0064 0053 0029  .d.....d.S.d.S.)
-00000400: 0c4e 46da 076e 756d 6172 6773 7201 0000  .NF..numargsr...
-00000410: 00da 0772 6571 6172 6773 7a11 4572 726f  ...reqargsz.Erro
-00000420: 723a 2064 6963 745f 636f 6465 207a 1b20  r: dict_code z. 
-00000430: 6d69 7373 696e 6720 7265 7161 7267 7321  missing reqargs!
-00000440: 2020 6e75 6d61 7267 733a 54da 0764 6973    numargs:T..dis
-00000450: 706c 6179 7a13 206d 6973 7369 6e67 2022  playz. missing "
-00000460: 6469 7370 6c61 7922 215a 0875 6e6d 6170  display"!Z.unmap
-00000470: 7065 64e9 6300 0000 2905 7204 0000 00da  ped.c...).r.....
-00000480: 0570 7269 6e74 7205 0000 00da 0564 6562  .printr......deb
-00000490: 7567 da04 6578 6974 2905 da04 666c 6167  ug..exit)...flag
-000004a0: da04 6974 656d da05 656e 7472 7972 0e00  ..item..entryr..
-000004b0: 0000 da09 6572 726f 725f 6d73 6772 0b00  ....error_msgr..
-000004c0: 0000 720b 0000 0072 0c00 0000 da14 6c6f  ..r....r......lo
-000004d0: 6f6b 5f66 6f72 5f6d 6973 7369 6e67 5f72  ok_for_missing_r
-000004e0: 6571 3500 0000 7326 0000 0004 0108 0108  eq5...s&........
-000004f0: 0108 0110 0110 0108 010c 0104 0108 010c  ................
-00000500: 0108 010a 0108 0104 0102 8004 010c 0104  ................
-00000510: ff72 1900 0000 6301 0000 0000 0000 0000  .r....c.........
-00000520: 0000 0003 0000 0003 0000 0043 0000 0073  ...........C...s
-00000530: 4400 0000 6401 6402 6c00 6d01 7d01 0100  D...d.d.l.m.}...
-00000540: 7c00 6400 6403 8502 1900 7d02 7c02 7c01  |.d.d.....}.|.|.
-00000550: 7600 7220 7c00 7402 7600 7220 6404 7402  v.r |.t.v.r d.t.
-00000560: 7c00 1900 6404 1900 6405 1700 6901 7402  |...d...d...i.t.
-00000570: 7c00 3c00 6400 5300 2906 4e72 0100 0000  |.<.d.S.).Nr....
-00000580: 2901 da0a 6465 7072 6963 6174 6564 e9ff  )...depricated..
-00000590: ffff ff72 1000 0000 7a1a 3c65 6d3e 2028  ...r....z.<em> (
-000005a0: 4973 2044 6570 7265 6361 7465 6429 3c2f  Is Deprecated)</
-000005b0: 656d 3e20 2903 5a18 6d61 7074 6173 6b65  em> ).Z.maptaske
-000005c0: 722e 7372 632e 6465 7072 6963 6174 6564  r.src.depricated
-000005d0: 721a 0000 0072 0400 0000 2903 da09 6469  r....r....)...di
-000005e0: 6374 5f63 6f64 6572 1a00 0000 da06 6c6f  ct_coder......lo
-000005f0: 6f6b 7570 720b 0000 0072 0b00 0000 720c  okupr....r....r.
-00000600: 0000 00da 1563 6865 636b 5f66 6f72 5f64  .....check_for_d
-00000610: 6570 7265 6361 7469 6f6e 4c00 0000 730c  eprecationL...s.
-00000620: 0000 000c 010c 0210 0110 0208 ff04 0372  ...............r
-00000630: 1e00 0000 da0a 636f 6465 5f63 6869 6c64  ......code_child
-00000640: da0b 636f 6465 5f61 6374 696f 6eda 0b61  ..code_action..a
-00000650: 6374 696f 6e5f 7479 7065 da08 636f 6c6f  ction_type..colo
-00000660: 726d 6170 da09 636f 6465 5f74 7970 65da  rmap..code_type.
-00000670: 0c70 726f 6772 616d 5f61 7267 73da 0672  .program_args..r
-00000680: 6574 7572 6e63 0600 0000 0000 0000 0000  eturnc..........
-00000690: 0000 0c00 0000 0a00 0000 4300 0000 735c  ..........C...s\
-000006a0: 0100 0074 00a0 0164 017c 006a 029b 007c  ...t...d.|.j...|
-000006b0: 049b 009d 03a1 0101 007c 006a 027c 0417  .........|.j.|..
-000006c0: 007d 0674 037c 0683 0101 007c 0674 0476  .}.t.|.....|.t.v
-000006d0: 0173 1e64 0274 047c 0619 0076 0172 3564  .s.d.t.|...v.r5d
-000006e0: 037c 069b 0064 0474 057c 017c 027c 037c  .|...d.t.|.|.|.|
-000006f0: 0583 049b 009d 047d 0774 00a0 0164 057c  .......}.t...d.|
-00000700: 069b 0064 069d 03a1 0101 006e 7364 077c  ...d.......nsd.|
-00000710: 0364 0819 0017 0064 0917 0074 047c 0619  .d.....d...t.|..
-00000720: 0064 0219 0017 007d 0764 0a74 047c 0619  .d.....}.d.t.|..
-00000730: 0076 0072 5074 047c 0619 0064 0a19 007d  .v.rPt.|...d...}
-00000740: 086e 0264 0b7d 087c 0864 0b6b 0372 7064  .n.d.}.|.d.k.rpd
-00000750: 0c74 047c 0619 0076 0072 7074 06a0 077c  .t.|...v.rpt...|
-00000760: 0674 047c 017c 027c 0374 047c 0619 0064  .t.|.|.|.t.|...d
-00000770: 0c19 0074 047c 0619 0064 0d19 007c 05a1  ...t.|...d...|..
-00000780: 087d 0764 0e74 047c 0619 0076 0072 a874  .}.d.t.|...v.r.t
-00000790: 047c 0619 0064 0e19 0064 0b19 007d 097c  .|...d...d...}.|
-000007a0: 0674 08a0 0974 047c 0919 00a1 0169 017d  .t...t.|.....i.}
-000007b0: 0a74 047c 0619 0064 0219 007d 0b74 08a0  .t.|...d...}.t..
-000007c0: 097c 0ba1 017c 0a64 023c 0074 06a0 077c  .|...|.d.<.t...|
-000007d0: 067c 0a7c 017c 027c 037c 0a7c 0619 0064  .|.|.|.|.|.|...d
-000007e0: 0c19 007c 0a7c 0619 0064 0d19 007c 05a1  ...|.|...d...|..
-000007f0: 087d 0774 0a7c 0783 017d 077c 0753 0029  .}.t.|...}.|.S.)
-00000800: 0f4e 7a08 6765 7463 6f64 653a 7210 0000  .Nz.getcode:r...
-00000810: 007a 0543 6f64 6520 7a0f 206e 6f74 2079  .z.Code z. not y
-00000820: 6574 206d 6170 7065 647a 1475 6e6d 6170  et mappedz.unmap
-00000830: 7065 6420 7461 736b 2063 6f64 653a 20fa  ped task code: .
-00000840: 0120 7a13 3c73 7061 6e20 7374 796c 653d  . z.<span style=
-00000850: 2263 6f6c 6f72 3ada 1161 6374 696f 6e5f  "color:..action_
-00000860: 6e61 6d65 5f63 6f6c 6f72 7a08 223c 2f73  name_colorz."</s
-00000870: 7061 6e3e 720e 0000 0072 0100 0000 720f  pan>r....r....r.
-00000880: 0000 005a 0865 7661 6c61 7267 735a 0872  ...Z.evalargsZ.r
-00000890: 6564 6972 6563 7429 0b72 0500 0000 7213  edirect).r....r.
-000008a0: 0000 00da 0474 6578 7472 1e00 0000 7204  .....textr....r.
-000008b0: 0000 0072 0300 0000 da0e 6163 7469 6f6e  ...r......action
-000008c0: 5f72 6573 756c 7473 5a12 6765 745f 6163  _resultsZ.get_ac
-000008d0: 7469 6f6e 5f72 6573 756c 7473 da04 636f  tion_results..co
-000008e0: 7079 da08 6465 6570 636f 7079 720d 0000  py..deepcopyr...
-000008f0: 0029 0c72 1f00 0000 7220 0000 0072 2100  .).r....r ...r!.
-00000900: 0000 7222 0000 0072 2300 0000 7224 0000  ..r"...r#...r$..
-00000910: 0072 1c00 0000 5a0a 7468 655f 7265 7375  .r....Z.the_resu
-00000920: 6c74 720e 0000 005a 0872 6566 6572 7261  ltr....Z.referra
-00000930: 6c5a 1174 656d 705f 6c6f 6f6b 7570 5f63  lZ.temp_lookup_c
-00000940: 6f64 6573 5a0c 6469 7370 6c61 795f 6e61  odesZ.display_na
-00000950: 6d65 720b 0000 0072 0b00 0000 720c 0000  mer....r....r...
-00000960: 00da 0f67 6574 5f61 6374 696f 6e5f 636f  ...get_action_co
-00000970: 6465 5a00 0000 7362 0000 0016 080a 0108  deZ...sb........
-00000980: 0214 021a 0214 0102 0406 0102 ff02 0202  ................
-00000990: fe0a 0302 fd02 ff0c 060e 0104 0214 0104  ................
-000009a0: 0102 0102 0102 0102 0102 010a 010a 0102  ................
-000009b0: 0104 f80c 0c0a 0102 0104 ff12 0306 0102  ................
-000009c0: 0104 ff0e 0304 0202 0102 0102 0102 0102  ................
-000009d0: 010a 010a 0102 0104 f808 0b04 0172 2c00  .............r,.
-000009e0: 0000 6305 0000 0000 0000 0000 0000 000a  ..c.............
-000009f0: 0000 0006 0000 0043 0000 0073 e400 0000  .......C...s....
-00000a00: 7c03 7d05 7c05 6401 6b03 720c 7c04 7c01  |.}.|.d.k.r.|.|.
-00000a10: 1700 7d01 6401 7d05 7c05 6401 6b00 7214  ..}.d.}.|.d.k.r.
-00000a20: 7c04 7c01 1700 7d01 7c01 6402 6b03 7266  |.|...}.|.d.k.rf
-00000a30: 7c01 a000 6403 a101 7d06 7401 7c01 8301  |...d...}.t.|...
-00000a40: 7d07 7c06 6404 6b02 7230 7c07 6405 6b04  }.|.d.k.r0|.d.k.
-00000a50: 7230 7c00 a002 7c01 a101 0100 6400 5300  r0|...|.....d.S.
-00000a60: 7c01 a003 6403 a101 7d08 6401 7d05 7c08  |...d...}.d.}.|.
-00000a70: 4400 5d2a 7d09 7c05 6401 6b02 7245 7c00  D.]*}.|.d.k.rE|.
-00000a80: a002 7c09 a101 0100 6e08 7c00 a002 6406  ..|.....n.|...d.
-00000a90: 7c09 9b00 9d02 a101 0100 7c05 6407 3700  |.........|.d.7.
-00000aa0: 7d05 7c05 7404 6b02 7263 7c00 a002 6408  }.|.t.k.rc|...d.
-00000ab0: 7405 7404 8301 9b00 6409 9d03 a101 0100  t.t.....d.......
-00000ac0: 0100 6400 5300 7139 6400 5300 7c00 a002  ..d.S.q9d.S.|...
-00000ad0: 640a 7c02 6a06 9b00 640b 9d03 a101 0100  d.|.j...d.......
-00000ae0: 6400 5300 290c 4e72 0100 0000 7206 0000  d.S.).Nr....r...
-00000af0: 00da 010a 721b 0000 00e9 5000 0000 7a03  ....r.....P...z.
-00000b00: 2e2e 2ee9 0100 0000 7a27 3c66 6f6e 7420  ........z'<font 
-00000b10: 636f 6c6f 723a 7265 643e 202e 2e2e 2063  color:red> ... c
-00000b20: 6f6e 7469 6e75 6520 6c69 6d69 7420 6f66  ontinue limit of
-00000b30: 207a 3520 7265 6163 6865 642e 2020 5365   z5 reached.  Se
-00000b40: 6520 2243 4f4e 5449 4e55 455f 4c49 4d49  e "CONTINUE_LIMI
-00000b50: 5420 3d22 2069 6e20 636f 6465 2066 6f72  T =" in code for
-00000b60: 2064 6574 6169 6c73 7a07 4163 7469 6f6e   detailsz.Action
-00000b70: 207a 103a 206e 6f74 2079 6574 206d 6170   z.: not yet map
-00000b80: 7065 6429 07da 0466 696e 64da 036c 656e  ped)...find..len
-00000b90: da06 6170 7065 6e64 da05 7370 6c69 7472  ..append..splitr
-00000ba0: 0200 0000 da03 7374 7272 2800 0000 290a  ......strr(...).
-00000bb0: 5a05 616c 6973 745a 0574 636f 6465 5a0c  Z.alistZ.tcodeZ.
-00000bc0: 636f 6465 5f65 6c65 6d65 6e74 da06 696e  code_element..in
-00000bd0: 6465 6e74 5a0a 696e 6465 6e74 5f61 6d74  dentZ.indent_amt
-00000be0: da05 636f 756e 74da 076e 6577 6c69 6e65  ..count..newline
-00000bf0: 5a09 7463 6f64 655f 6c65 6e5a 0e61 7272  Z.tcode_lenZ.arr
-00000c00: 6179 5f6f 665f 6c69 6e65 7372 1600 0000  ay_of_linesr....
-00000c10: 720b 0000 0072 0b00 0000 720c 0000 00da  r....r....r.....
-00000c20: 0c62 7569 6c64 5f61 6374 696f 6ea0 0000  .build_action...
-00000c30: 0073 3a00 0000 0402 0801 0801 0401 0801  .s:.............
-00000c40: 0801 0803 0a01 0801 1003 0a01 0413 0aef  ................
-00000c50: 0401 0801 0801 0c01 1002 0801 0802 0402  ................
-00000c60: 0e01 04ff 0203 0403 02f8 0408 14ff 0401  ................
-00000c70: 7238 0000 0029 1c72 2a00 0000 da02 7265  r8...).r*.....re
-00000c80: da15 786d 6c2e 6574 7265 652e 456c 656d  ..xml.etree.Elem
-00000c90: 656e 7454 7265 65da 0378 6d6c 5a15 6d61  entTree..xmlZ.ma
-00000ca0: 7074 6173 6b65 722e 7372 632e 6163 7469  ptasker.src.acti
-00000cb0: 6f6e 72da 0373 7263 5a07 6163 7469 6f6e  onr..srcZ.action
-00000cc0: 7272 2900 0000 da14 6d61 7074 6173 6b65  rr).....maptaske
-00000cd0: 722e 7372 632e 636f 6e66 6967 7202 0000  r.src.configr...
-00000ce0: 005a 146d 6170 7461 736b 6572 2e73 7263  .Z.maptasker.src
-00000cf0: 2e61 6374 696f 6e72 0300 0000 5a15 6d61  .actionr....Z.ma
-00000d00: 7074 6173 6b65 722e 7372 632e 6163 7469  ptasker.src.acti
-00000d10: 6f6e 6372 0400 0000 da16 6d61 7074 6173  oncr......maptas
-00000d20: 6b65 722e 7372 632e 7379 7363 6f6e 7374  ker.src.sysconst
-00000d30: 7205 0000 00da 0763 6f6d 7069 6c65 7208  r......compiler.
-00000d40: 0000 0072 0d00 0000 7219 0000 0072 1e00  ...r....r....r..
-00000d50: 0000 da05 6574 7265 65da 0b45 6c65 6d65  ....etree..Eleme
-00000d60: 6e74 5472 6565 da04 626f 6f6c da04 6469  ntTree..bool..di
-00000d70: 6374 7234 0000 0072 2c00 0000 7238 0000  ctr4...r,...r8..
-00000d80: 0072 0b00 0000 720b 0000 0072 0b00 0000  .r....r....r....
-00000d90: 720c 0000 00da 083c 6d6f 6475 6c65 3e01  r......<module>.
-00000da0: 0000 0073 3800 0000 080c 0801 0801 1202  ...s8...........
-00000db0: 0c01 0c01 0c01 0c01 0a02 0807 0817 0817  ................
-00000dc0: 020e 0601 02ff 0602 02fe 0203 02fd 0204  ................
-00000dd0: 02fc 0205 02fb 0206 02fa 0207 0af9 0c46  ...............F
+00000080: 6c0e 6d0f 5a0f 0100 6400 6406 6c0e 6d10  l.m.Z...d.d.l.m.
+00000090: 5a10 0100 6501 a011 6407 a101 5a12 6408  Z...e...d...Z.d.
+000000a0: 6409 8400 5a13 640a 640b 8400 5a14 640c  d...Z.d.d...Z.d.
+000000b0: 640d 8400 5a15 640e 6503 6a16 6a17 640f  d...Z.d.e.j.j.d.
+000000c0: 6503 6a16 6a17 6410 6518 6411 6519 6412  e.j.j.d.e.d.e.d.
+000000d0: 651a 6413 6519 6414 651a 660e 6415 6416  e.d.e.d.e.f.d.d.
+000000e0: 8404 5a1b 6417 6418 8400 5a1c 6401 5300  ..Z.d.d...Z.d.S.
+000000f0: 2919 e900 0000 004e 2901 da0e 434f 4e54  )......N)...CONT
+00000100: 494e 5545 5f4c 494d 4954 2901 da0f 6765  INUE_LIMIT)...ge
+00000110: 745f 6578 7472 615f 7374 7566 6629 01da  t_extra_stuff)..
+00000120: 0c61 6374 696f 6e5f 636f 6465 7329 01da  .action_codes)..
+00000130: 066c 6f67 6765 7229 01da 0b46 4f4e 545f  .logger)...FONT_
+00000140: 544f 5f55 5345 7a06 2c5b 2c20 5d2b 6301  TO_USEz.,[, ]+c.
+00000150: 0000 0000 0000 0000 0000 0001 0000 0004  ................
+00000160: 0000 0043 0000 0073 9400 0000 7c00 a000  ...C...s....|...
+00000170: 6401 6402 a102 7d00 7c00 a000 6403 6404  d.d...}.|...d.d.
+00000180: a102 7d00 7401 a002 6405 7c00 a102 7d00  ..}.t...d.|...}.
+00000190: 7c00 a000 6406 6407 a102 7d00 7c00 a000  |...d.d...}.|...
+000001a0: 6408 6409 a102 7d00 7c00 a000 640a 6404  d.d...}.|...d.d.
+000001b0: a102 7d00 7c00 a000 640b 6404 a102 7d00  ..}.|...d.d...}.
+000001c0: 7c00 a000 640c 6404 a102 7d00 7c00 a000  |...d.d...}.|...
+000001d0: 640d 6404 a102 7d00 7c00 a000 640e 6404  d.d...}.|...d.d.
+000001e0: a102 7d00 7c00 a000 640f 6404 a102 7d00  ..}.|...d.d...}.
+000001f0: 7c00 a000 6410 6411 a102 7d00 7c00 5300  |...d.d...}.|.S.
+00000200: 2912 4e7a 092c 2020 3c66 6f6e 743e 7a06  ).Nz.,  <font>z.
+00000210: 3c66 6f6e 743e 7a03 2c20 28da 007a 022c  <font>z., (..z.,
+00000220: 207a 072c 203c 7370 616e 7a05 3c73 7061   z., <spanz.<spa
+00000230: 6e7a 082c 2020 3c73 7061 6e7a 0720 203c  nz.,  <spanz.  <
+00000240: 7370 616e 7a07 2c20 636f 6465 3a7a 053c  spanz., code:z.<
+00000250: 6269 673e 7a07 3c73 6d61 6c6c 3e7a 043c  big>z.<small>z.<
+00000260: 7474 3e7a 033c 693e 7a03 3c75 3e7a 072c  tt>z.<i>z.<u>z.,
+00000270: 203c 666f 6e74 7a05 3c66 6f6e 7429 03da   <fontz.<font)..
+00000280: 0772 6570 6c61 6365 da07 7061 7474 6572  .replace..patter
+00000290: 6eda 0373 7562 2901 da07 7265 7375 6c74  n..sub)...result
+000002a0: 73a9 0072 0c00 0000 fa76 2f55 7365 7273  s..r.....v/Users
+000002b0: 2f6d 696b 7275 6269 6e2f 4c69 6272 6172  /mikrubin/Librar
+000002c0: 792f 436c 6f75 6453 746f 7261 6765 2f47  y/CloudStorage/G
+000002d0: 6f6f 676c 6544 7269 7665 2d6d 696b 7275  oogleDrive-mikru
+000002e0: 6269 6e40 676d 6169 6c2e 636f 6d2f 4d79  bin@gmail.com/My
+000002f0: 2044 7269 7665 2f50 7974 686f 6e2f 6d61   Drive/Python/ma
+00000300: 7074 6173 6b65 722f 6d61 7074 6173 6b65  ptasker/maptaske
+00000310: 722f 7372 632f 6163 7469 6f6e 652e 7079  r/src/actione.py
+00000320: da12 636c 6561 6e75 705f 7468 655f 7265  ..cleanup_the_re
+00000330: 7375 6c74 1f00 0000 731e 0000 0004 0304  sult....s.......
+00000340: 0104 ff0c 030c 010c 010c 010c 010c 010c  ................
+00000350: 010c 010c 010c 010c 0104 0172 0e00 0000  ...........r....
+00000360: 6300 0000 0000 0000 0000 0000 0005 0000  c...............
+00000370: 0005 0000 0043 0000 0073 9c00 0000 6401  .....C...s....d.
+00000380: 7d00 7400 4400 5d3f 7d01 7400 7c01 1900  }.t.D.]?}.t.|...
+00000390: 7d02 7c02 6402 1900 7d03 7c03 6403 6b04  }.|.d...}.|.d.k.
+000003a0: 722a 6404 7c02 7601 722a 6405 7c01 9b00  r*d.|.v.r*d.|...
+000003b0: 6406 7c03 9b00 9d04 7d04 7401 7c04 8301  d.|.....}.t.|...
+000003c0: 0100 7402 a003 7c04 9b00 a101 0100 6407  ..t...|.......d.
+000003d0: 7d00 6408 7c02 7601 7243 6405 7c01 9b00  }.d.|.v.rCd.|...
+000003e0: 6409 9d03 7d04 7401 7c04 8301 0100 7402  d...}.t.|.....t.
+000003f0: a003 7c04 a101 0100 640a 7c02 6408 3c00  ..|.....d.|.d.<.
+00000400: 6407 7d00 7104 7c00 724c 7404 640b 8301  d.}.q.|.rLt.d...
+00000410: 0100 6400 5300 6400 5300 290c 4e46 da07  ..d.S.d.S.).NF..
+00000420: 6e75 6d61 7267 7372 0100 0000 da07 7265  numargsr......re
+00000430: 7161 7267 737a 1145 7272 6f72 3a20 6469  qargsz.Error: di
+00000440: 6374 5f63 6f64 6520 7a1b 206d 6973 7369  ct_code z. missi
+00000450: 6e67 2072 6571 6172 6773 2120 206e 756d  ng reqargs!  num
+00000460: 6172 6773 3a54 da07 6469 7370 6c61 797a  args:T..displayz
+00000470: 1320 6d69 7373 696e 6720 2264 6973 706c  . missing "displ
+00000480: 6179 2221 5a08 756e 6d61 7070 6564 e963  ay"!Z.unmapped.c
+00000490: 0000 0029 0572 0400 0000 da05 7072 696e  ...).r......prin
+000004a0: 7472 0500 0000 da05 6465 6275 67da 0465  tr......debug..e
+000004b0: 7869 7429 05da 0466 6c61 67da 0469 7465  xit)...flag..ite
+000004c0: 6dda 0565 6e74 7279 720f 0000 00da 0965  m..entryr......e
+000004d0: 7272 6f72 5f6d 7367 720c 0000 0072 0c00  rror_msgr....r..
+000004e0: 0000 720d 0000 00da 146c 6f6f 6b5f 666f  ..r......look_fo
+000004f0: 725f 6d69 7373 696e 675f 7265 7136 0000  r_missing_req6..
+00000500: 0073 2600 0000 0401 0801 0801 0801 1001  .s&.............
+00000510: 1001 0801 0c01 0401 0801 0c01 0801 0a01  ................
+00000520: 0801 0401 0280 0401 0c01 04ff 721a 0000  ............r...
+00000530: 0063 0100 0000 0000 0000 0000 0000 0300  .c..............
+00000540: 0000 0300 0000 4300 0000 7344 0000 0064  ......C...sD...d
+00000550: 0164 026c 006d 017d 0101 007c 0064 0064  .d.l.m.}...|.d.d
+00000560: 0385 0219 007d 027c 027c 0176 0072 207c  .....}.|.|.v.r |
+00000570: 0074 0276 0072 2064 0474 027c 0019 0064  .t.v.r d.t.|...d
+00000580: 0419 0064 0517 0069 0174 027c 003c 0064  ...d...i.t.|.<.d
+00000590: 0053 0029 064e 7201 0000 0029 01da 0a64  .S.).Nr....)...d
+000005a0: 6570 7269 6361 7465 64e9 ffff ffff 7211  epricated.....r.
+000005b0: 0000 007a 1a3c 656d 3e20 2849 7320 4465  ...z.<em> (Is De
+000005c0: 7072 6563 6174 6564 293c 2f65 6d3e 2029  precated)</em> )
+000005d0: 035a 186d 6170 7461 736b 6572 2e73 7263  .Z.maptasker.src
+000005e0: 2e64 6570 7269 6361 7465 6472 1b00 0000  .depricatedr....
+000005f0: 7204 0000 0029 03da 0964 6963 745f 636f  r....)...dict_co
+00000600: 6465 721b 0000 00da 066c 6f6f 6b75 7072  der......lookupr
+00000610: 0c00 0000 720c 0000 0072 0d00 0000 da15  ....r....r......
+00000620: 6368 6563 6b5f 666f 725f 6465 7072 6563  check_for_deprec
+00000630: 6174 696f 6e4d 0000 0073 0c00 0000 0c01  ationM...s......
+00000640: 0c02 1001 1002 08ff 0403 721f 0000 00da  ..........r.....
+00000650: 0a63 6f64 655f 6368 696c 64da 0b63 6f64  .code_child..cod
+00000660: 655f 6163 7469 6f6e da0b 6163 7469 6f6e  e_action..action
+00000670: 5f74 7970 65da 0863 6f6c 6f72 6d61 70da  _type..colormap.
+00000680: 0963 6f64 655f 7479 7065 da0c 7072 6f67  .code_type..prog
+00000690: 7261 6d5f 6172 6773 da06 7265 7475 726e  ram_args..return
+000006a0: 6306 0000 0000 0000 0000 0000 000c 0000  c...............
+000006b0: 000a 0000 0043 0000 0073 6801 0000 7400  .....C...sh...t.
+000006c0: a001 6401 7c00 6a02 9b00 7c04 9b00 9d03  ..d.|.j...|.....
+000006d0: a101 0100 7c00 6a02 7c04 1700 7d06 7403  ....|.j.|...}.t.
+000006e0: 7c06 8301 0100 7c06 7404 7601 731e 6402  |.....|.t.v.s.d.
+000006f0: 7404 7c06 1900 7601 7235 6403 7c06 9b00  t.|...v.r5d.|...
+00000700: 6404 7405 7c01 7c02 7c03 7c05 8304 9b00  d.t.|.|.|.|.....
+00000710: 9d04 7d07 7400 a001 6405 7c06 9b00 6406  ..}.t...d.|...d.
+00000720: 9d03 a101 0100 6e79 6407 7c03 6408 1900  ......nyd.|.d...
+00000730: 1700 7c05 6409 1900 1700 640a 1700 7404  ..|.d.....d...t.
+00000740: 7c06 1900 6402 1900 1700 640b 1700 7d07  |...d.....d...}.
+00000750: 640c 7404 7c06 1900 7600 7256 7404 7c06  d.t.|...v.rVt.|.
+00000760: 1900 640c 1900 7d08 6e02 640d 7d08 7c08  ..d...}.n.d.}.|.
+00000770: 640d 6b03 7276 640e 7404 7c06 1900 7600  d.k.rvd.t.|...v.
+00000780: 7276 7406 a007 7c06 7404 7c01 7c02 7c03  rvt...|.t.|.|.|.
+00000790: 7404 7c06 1900 640e 1900 7404 7c06 1900  t.|...d...t.|...
+000007a0: 640f 1900 7c05 a108 7d07 6410 7404 7c06  d...|...}.d.t.|.
+000007b0: 1900 7600 72ae 7404 7c06 1900 6410 1900  ..v.r.t.|...d...
+000007c0: 640d 1900 7d09 7c06 7408 a009 7404 7c09  d...}.|.t...t.|.
+000007d0: 1900 a101 6901 7d0a 7404 7c06 1900 6402  ....i.}.t.|...d.
+000007e0: 1900 7d0b 7408 a009 7c0b a101 7c0a 6402  ..}.t...|...|.d.
+000007f0: 3c00 7406 a007 7c06 7c0a 7c01 7c02 7c03  <.t...|.|.|.|.|.
+00000800: 7c0a 7c06 1900 640e 1900 7c0a 7c06 1900  |.|...d...|.|...
+00000810: 640f 1900 7c05 a108 7d07 740a 7c07 8301  d...|...}.t.|...
+00000820: 7d07 7c07 5300 2911 6195 0100 000a 2020  }.|.S.).a.....  
+00000830: 2020 4769 7665 6e20 616e 2061 6374 696f    Given an actio
+00000840: 6e20 636f 6465 2c20 6576 616c 7561 7465  n code, evaluate
+00000850: 2069 7420 666f 7220 6469 7370 6c61 790a   it for display.
+00000860: 2020 2020 2020 2020 3a70 6172 616d 2063          :param c
+00000870: 6f64 655f 6368 696c 643a 2078 6d6c 2065  ode_child: xml e
+00000880: 6c65 6d65 6e74 206f 6620 7468 6520 3c63  lement of the <c
+00000890: 6f64 653e 0a20 2020 2020 2020 203a 7061  ode>.        :pa
+000008a0: 7261 6d20 636f 6465 5f61 6374 696f 6e3a  ram code_action:
+000008b0: 2076 616c 7565 206f 6620 3c63 6f64 653e   value of <code>
+000008c0: 2028 652e 672e 2022 3534 3922 290a 2020   (e.g. "549").  
+000008d0: 2020 2020 2020 3a70 6172 616d 2061 6374        :param act
+000008e0: 696f 6e5f 7479 7065 3a0a 2020 2020 2020  ion_type:.      
+000008f0: 2020 3a70 6172 616d 2063 6f6c 6f72 6d61    :param colorma
+00000900: 703a 2063 6f6c 6f72 7320 746f 2075 7365  p: colors to use
+00000910: 2069 6e20 6f75 7470 7574 0a20 2020 2020   in output.     
+00000920: 2020 203a 7061 7261 6d20 636f 6465 5f74     :param code_t
+00000930: 7970 653a 2027 6527 3d65 7665 6e74 2c20  ype: 'e'=event, 
+00000940: 2773 273d 7374 6174 652c 2027 7427 3d74  's'=state, 't'=t
+00000950: 6173 6b0a 2020 2020 2020 2020 3a70 6172  ask.        :par
+00000960: 616d 2070 726f 6772 616d 5f61 7267 733a  am program_args:
+00000970: 2072 756e 7469 6d65 2061 7267 756d 656e   runtime argumen
+00000980: 7473 0a20 2020 2020 2020 203a 7265 7475  ts.        :retu
+00000990: 726e 3a20 666f 726d 6174 7465 6420 6f75  rn: formatted ou
+000009a0: 7470 7574 206c 696e 6520 7769 7468 2061  tput line with a
+000009b0: 6374 696f 6e20 6465 7461 696c 730a 2020  ction details.  
+000009c0: 2020 7a08 6765 7463 6f64 653a 7211 0000    z.getcode:r...
+000009d0: 007a 0543 6f64 6520 7a0f 206e 6f74 2079  .z.Code z. not y
+000009e0: 6574 206d 6170 7065 647a 1475 6e6d 6170  et mappedz.unmap
+000009f0: 7065 6420 7461 736b 2063 6f64 653a 20fa  ped task code: .
+00000a00: 0120 7a13 3c73 7061 6e20 7374 796c 653d  . z.<span style=
+00000a10: 2263 6f6c 6f72 3a5a 1161 6374 696f 6e5f  "color:Z.action_
+00000a20: 6e61 6d65 5f63 6f6c 6f72 da0b 666f 6e74  name_color..font
+00000a30: 5f74 6f5f 7573 65fa 013e 7a07 3c2f 7370  _to_use..>z.</sp
+00000a40: 616e 3e72 0f00 0000 7201 0000 0072 1000  an>r....r....r..
+00000a50: 0000 5a08 6576 616c 6172 6773 5a08 7265  ..Z.evalargsZ.re
+00000a60: 6469 7265 6374 290b 7205 0000 0072 1400  direct).r....r..
+00000a70: 0000 da04 7465 7874 721f 0000 0072 0400  ....textr....r..
+00000a80: 0000 7203 0000 00da 0e61 6374 696f 6e5f  ..r......action_
+00000a90: 7265 7375 6c74 735a 1267 6574 5f61 6374  resultsZ.get_act
+00000aa0: 696f 6e5f 7265 7375 6c74 73da 0463 6f70  ion_results..cop
+00000ab0: 79da 0864 6565 7063 6f70 7972 0e00 0000  y..deepcopyr....
+00000ac0: 290c 7220 0000 0072 2100 0000 7222 0000  ).r ...r!...r"..
+00000ad0: 0072 2300 0000 7224 0000 0072 2500 0000  .r#...r$...r%...
+00000ae0: 721d 0000 005a 0a74 6865 5f72 6573 756c  r....Z.the_resul
+00000af0: 7472 0f00 0000 5a08 7265 6665 7272 616c  tr....Z.referral
+00000b00: 5a11 7465 6d70 5f6c 6f6f 6b75 705f 636f  Z.temp_lookup_co
+00000b10: 6465 735a 0c64 6973 706c 6179 5f6e 616d  desZ.display_nam
+00000b20: 6572 0c00 0000 720c 0000 0072 0d00 0000  er....r....r....
+00000b30: da0f 6765 745f 6163 7469 6f6e 5f63 6f64  ..get_action_cod
+00000b40: 655b 0000 0073 7000 0000 1612 0a01 0802  e[...sp.........
+00000b50: 1402 0802 0c01 04ff 02ff 1404 0205 0601  ................
+00000b60: 02ff 0602 02fe 0203 02fd 0a04 02fc 0205  ................
+00000b70: 02fb 02ff 0c08 0e01 0402 1402 0401 0201  ................
+00000b80: 0201 0201 0201 0201 0a01 0a01 0201 04f8  ................
+00000b90: 0c0c 0a01 0201 04ff 1203 0601 0201 04ff  ................
+00000ba0: 0e03 0402 0201 0201 0201 0201 0201 0a01  ................
+00000bb0: 0a01 0201 04f8 080b 0401 722e 0000 0063  ..........r....c
+00000bc0: 0500 0000 0000 0000 0000 0000 0a00 0000  ................
+00000bd0: 0600 0000 4300 0000 73fa 0000 007c 037d  ....C...s....|.}
+00000be0: 057c 0564 016b 0372 177c 01a0 0074 019b  .|.d.k.r.|...t..
+00000bf0: 0064 029d 0274 019b 0064 027c 049b 009d  .d...t...d.|....
+00000c00: 0364 03a1 037d 0164 017d 057c 0564 016b  .d...}.d.}.|.d.k
+00000c10: 0072 1f7c 047c 0117 007d 017c 0164 046b  .r.|.|...}.|.d.k
+00000c20: 0372 717c 01a0 0264 05a1 017d 0674 037c  .rq|...d...}.t.|
+00000c30: 0183 017d 077c 0664 066b 0272 3b7c 0764  ...}.|.d.k.r;|.d
+00000c40: 076b 0472 3b7c 00a0 047c 01a1 0101 0064  .k.r;|...|.....d
+00000c50: 0053 007c 01a0 0564 05a1 017d 0864 017d  .S.|...d...}.d.}
+00000c60: 057c 0844 005d 2a7d 097c 0564 016b 0272  .|.D.]*}.|.d.k.r
+00000c70: 507c 00a0 047c 09a1 0101 006e 087c 00a0  P|...|.....n.|..
+00000c80: 0464 087c 099b 009d 02a1 0101 007c 0564  .d.|.........|.d
+00000c90: 0337 007d 057c 0574 066b 0272 6e7c 00a0  .7.}.|.t.k.rn|..
+00000ca0: 0464 0974 0774 0683 019b 0064 0a9d 03a1  .d.t.t.....d....
+00000cb0: 0101 0001 0064 0053 0071 4464 0053 007c  .....d.S.qDd.S.|
+00000cc0: 00a0 0464 0b7c 026a 089b 0064 0c9d 03a1  ...d.|.j...d....
+00000cd0: 0101 0064 0053 0029 0d4e 7201 0000 0072  ...d.S.).Nr....r
+00000ce0: 2900 0000 e901 0000 0072 0700 0000 da01  )........r......
+00000cf0: 0a72 1c00 0000 e950 0000 007a 032e 2e2e  .r.....P...z....
+00000d00: 7a2f 3c73 7061 6e20 7374 796c 653d 2263  z/<span style="c
+00000d10: 6f6c 6f72 3a72 6564 223e 202e 2e2e 2063  olor:red"> ... c
+00000d20: 6f6e 7469 6e75 6520 6c69 6d69 7420 6f66  ontinue limit of
+00000d30: 207a 3c20 7265 6163 6865 642e 2020 5365   z< reached.  Se
+00000d40: 6520 2243 4f4e 5449 4e55 455f 4c49 4d49  e "CONTINUE_LIMI
+00000d50: 5420 3d22 2069 6e20 636f 6465 2066 6f72  T =" in code for
+00000d60: 2064 6574 6169 6c73 3c2f 7370 616e 3e7a   details</span>z
+00000d70: 0741 6374 696f 6e20 7a10 3a20 6e6f 7420  .Action z.: not 
+00000d80: 7965 7420 6d61 7070 6564 2909 7208 0000  yet mapped).r...
+00000d90: 0072 0600 0000 da04 6669 6e64 da03 6c65  .r......find..le
+00000da0: 6eda 0661 7070 656e 64da 0573 706c 6974  n..append..split
+00000db0: 7202 0000 00da 0373 7472 722a 0000 0029  r......strr*...)
+00000dc0: 0a5a 0561 6c69 7374 5a05 7463 6f64 655a  .Z.alistZ.tcodeZ
+00000dd0: 0c63 6f64 655f 656c 656d 656e 74da 0669  .code_element..i
+00000de0: 6e64 656e 745a 0a69 6e64 656e 745f 616d  ndentZ.indent_am
+00000df0: 74da 0563 6f75 6e74 da07 6e65 776c 696e  t..count..newlin
+00000e00: 655a 0974 636f 6465 5f6c 656e 5a0e 6172  eZ.tcode_lenZ.ar
+00000e10: 7261 795f 6f66 5f6c 696e 6573 7217 0000  ray_of_linesr...
+00000e20: 0072 0c00 0000 720c 0000 0072 0d00 0000  .r....r....r....
+00000e30: da0c 6275 696c 645f 6163 7469 6f6e b100  ..build_action..
+00000e40: 0000 733e 0000 0004 0208 011e 0104 0208  ..s>............
+00000e50: 0108 0108 030a 0108 0110 030a 0104 150a  ................
+00000e60: ed04 0108 0108 010c 0110 0208 0108 0204  ................
+00000e70: 0202 0106 0106 ff04 ff02 0504 0302 f604  ................
+00000e80: 0a14 ff04 0172 3a00 0000 291d 722c 0000  .....r:...).r,..
+00000e90: 00da 0272 65da 1578 6d6c 2e65 7472 6565  ...re..xml.etree
+00000ea0: 2e45 6c65 6d65 6e74 5472 6565 da03 786d  .ElementTree..xm
+00000eb0: 6c5a 156d 6170 7461 736b 6572 2e73 7263  lZ.maptasker.src
+00000ec0: 2e61 6374 696f 6e72 da03 7372 635a 0761  .actionr..srcZ.a
+00000ed0: 6374 696f 6e72 722b 0000 005a 146d 6170  ctionrr+...Z.map
+00000ee0: 7461 736b 6572 2e73 7263 2e63 6f6e 6669  tasker.src.confi
+00000ef0: 6772 0200 0000 5a14 6d61 7074 6173 6b65  gr....Z.maptaske
+00000f00: 722e 7372 632e 6163 7469 6f6e 7203 0000  r.src.actionr...
+00000f10: 005a 156d 6170 7461 736b 6572 2e73 7263  .Z.maptasker.src
+00000f20: 2e61 6374 696f 6e63 7204 0000 00da 166d  .actioncr......m
+00000f30: 6170 7461 736b 6572 2e73 7263 2e73 7973  aptasker.src.sys
+00000f40: 636f 6e73 7472 0500 0000 7206 0000 00da  constr....r.....
+00000f50: 0763 6f6d 7069 6c65 7209 0000 0072 0e00  .compiler....r..
+00000f60: 0000 721a 0000 0072 1f00 0000 da05 6574  ..r....r......et
+00000f70: 7265 65da 0b45 6c65 6d65 6e74 5472 6565  ree..ElementTree
+00000f80: da04 626f 6f6c da04 6469 6374 7236 0000  ..bool..dictr6..
+00000f90: 0072 2e00 0000 723a 0000 0072 0c00 0000  .r....r:...r....
+00000fa0: 720c 0000 0072 0c00 0000 720d 0000 00da  r....r....r.....
+00000fb0: 083c 6d6f 6475 6c65 3e01 0000 0073 3a00  .<module>....s:.
+00000fc0: 0000 080c 0801 0801 1202 0c01 0c01 0c01  ................
+00000fd0: 0c01 0c01 0a02 0807 0817 0817 020e 0601  ................
+00000fe0: 02ff 0602 02fe 0203 02fd 0204 02fc 0205  ................
+00000ff0: 02fb 0206 02fa 0207 0af9 0c56            ...........V
```

### Comparing `maptasker-1.3.1/maptasker/src/__pycache__/actionr.cpython-310.pyc` & `maptasker-1.3.2/maptasker/src/__pycache__/actionr.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Sun Feb 19 16:04:35 2023 UTC, .py size: 7296 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 15% similar despite different names*

```diff
@@ -1,187 +1,195 @@
-00000000: 6f0d 0d0a 0000 0000 9348 f263 801c 0000  o........H.c....
+00000000: 6f0d 0d0a 0000 0000 a20c 2764 751d 0000  o.........'du...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
-00000020: 0014 0000 0040 0000 0073 e800 0000 6400  .....@...s....d.
+00000020: 0014 0000 0040 0000 0073 0001 0000 6400  .....@...s....d.
 00000030: 6401 6c00 5a00 6400 6401 6c01 5a02 6400  d.l.Z.d.d.l.Z.d.
 00000040: 6402 6c03 6d04 5a04 0100 6400 6401 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 0200 0100 6d07 5a08 0100 6400 6403  m.....m.Z...d.d.
 00000060: 6c09 6d0a 5a0a 0100 6400 6404 6c0b 6d0c  l.m.Z...d.d.l.m.
 00000070: 5a0c 0100 6400 6405 6c0d 6d0e 5a0e 0100  Z...d.d.l.m.Z...
-00000080: 6406 650f 6407 6510 6604 6408 6409 8404  d.e.d.e.f.d.d...
-00000090: 5a11 640a 6502 6a12 6a13 640b 6514 640c  Z.d.e.j.j.d.e.d.
-000000a0: 6502 6a12 6a13 640d 6515 640e 650f 640f  e.j.j.d.e.d.e.d.
-000000b0: 650f 6410 650f 6411 6514 6406 650f 6407  e.d.e.d.e.d.e.d.
-000000c0: 6516 6614 6412 6413 8404 5a17 640a 6510  e.f.d.d...Z.d.e.
-000000d0: 6410 6502 6a12 6a13 640c 6502 6a12 6a13  d.e.j.j.d.e.j.j.
-000000e0: 640d 6515 640e 6502 6a12 6a13 640b 6514  d.e.d.e.j.j.d.e.
-000000f0: 6510 1900 6411 6514 6510 1900 640f 6502  e...d.e.e...d.e.
-00000100: 6a12 6a13 6407 6510 6612 6414 6415 8404  j.j.d.e.f.d.d...
-00000110: 5a18 6401 5300 2916 e900 0000 004e 2901  Z.d.S.)......N).
-00000120: da0b 6465 6661 756c 7464 6963 7429 01da  ..defaultdict)..
-00000130: 0b61 6374 696f 6e5f 6172 6773 2901 da0c  .action_args)...
-00000140: 6163 7469 6f6e 5f63 6f64 6573 2901 da06  action_codes)...
-00000150: 6c6f 6767 6572 da11 6576 616c 7561 7465  logger..evaluate
-00000160: 645f 7265 7375 6c74 73da 0672 6574 7572  d_results..retur
-00000170: 6e63 0100 0000 0000 0000 0000 0000 0400  nc..............
-00000180: 0000 0500 0000 4300 0000 7356 0100 0064  ......C...sV...d
-00000190: 017d 017c 0064 0219 0044 005d a27d 0264  .}.|.d...D.].}.d
-000001a0: 017d 037c 0204 0064 036b 0272 2201 007c  .}.|...d.k.r"..|
-000001b0: 0064 0419 0072 217c 0064 0419 0064 0519  .d...r!|.d...d..
-000001c0: 007d 037c 0064 0419 00a0 0064 05a1 0101  .}.|.d.....d....
-000001d0: 006e 7f04 0064 066b 0272 3901 007c 0064  .n...d.k.r9..|.d
-000001e0: 0719 0072 387c 0064 0719 0064 0519 007d  ...r8|.d...d...}
-000001f0: 037c 0064 0719 00a0 0064 05a1 0101 006e  .|.d.....d.....n
-00000200: 6804 0064 086b 0272 5001 007c 0064 0919  h..d.k.rP..|.d..
-00000210: 0072 4f7c 0064 0919 0064 0519 007d 037c  .rO|.d...d...}.|
-00000220: 0064 0919 00a0 0064 05a1 0101 006e 5104  .d.....d.....nQ.
-00000230: 0064 0a6b 0272 6701 007c 0064 0b19 0072  .d.k.rg..|.d...r
-00000240: 667c 0064 0b19 0064 0519 007d 037c 0064  f|.d...d...}.|.d
-00000250: 0b19 00a0 0064 05a1 0101 006e 3a04 0064  .....d.....n:..d
-00000260: 0c6b 0272 7e01 007c 0064 0d19 0072 7d7c  .k.r~..|.d...r}|
-00000270: 0064 0d19 0064 0519 007d 037c 0064 0d19  .d...d...}.|.d..
-00000280: 00a0 0064 05a1 0101 006e 2364 0e6b 0272  ...d.....n#d.k.r
-00000290: 937c 0064 0f19 0072 927c 0064 0f19 0064  .|.d...r.|.d...d
-000002a0: 0519 007d 037c 0064 0f19 00a0 0064 05a1  ...}.|.d.....d..
-000002b0: 0101 006e 0e09 0074 01a0 0264 107c 029b  ...n...t...d.|..
-000002c0: 009d 02a1 0101 0074 03a0 0464 11a1 0101  .......t...d....
-000002d0: 007c 019b 0064 127c 039b 009d 037d 0171  .|...d.|.....}.q
-000002e0: 067c 0153 0029 134e da00 5a11 706f 7369  .|.S.).N..Z.posi
-000002f0: 7469 6f6e 5f61 7267 5f74 7970 655a 0353  tion_arg_typeZ.S
-00000300: 7472 da0a 7265 7375 6c74 5f73 7472 7201  tr..result_strr.
-00000310: 0000 005a 0349 6e74 da0a 7265 7375 6c74  ...Z.Int..result
-00000320: 5f69 6e74 5a03 4170 705a 0a72 6573 756c  _intZ.AppZ.resul
-00000330: 745f 6170 705a 0d43 6f6e 6469 7469 6f6e  t_appZ.Condition
-00000340: 4c69 7374 5a0a 7265 7375 6c74 5f63 6f6e  ListZ.result_con
-00000350: 5a03 496d 675a 0a72 6573 756c 745f 696d  Z.ImgZ.result_im
-00000360: 675a 0642 756e 646c 655a 0a72 6573 756c  gZ.BundleZ.resul
-00000370: 745f 6275 6e7a 3646 756e 6374 696f 6e20  t_bunz6Function 
-00000380: 6765 745f 7265 7375 6c74 735f 696e 5f61  get_results_in_a
-00000390: 7267 5f6f 7264 6572 3a20 6e6f 206d 6174  rg_order: no mat
-000003a0: 6368 2066 6f72 2022 6172 6722 3ae9 0800  ch for "arg":...
-000003b0: 0000 fa01 2029 05da 0370 6f70 7205 0000  .... )...popr...
-000003c0: 00da 0564 6562 7567 da03 7379 73da 0465  ...debug..sys..e
-000003d0: 7869 7429 0472 0600 0000 5a0d 7265 7475  xit).r....Z.retu
-000003e0: 726e 5f72 6573 756c 74da 0361 7267 5a08  rn_result..argZ.
-000003f0: 7468 655f 6974 656d a900 7212 0000 00fa  the_item..r.....
-00000400: 762f 5573 6572 732f 6d69 6b72 7562 696e  v/Users/mikrubin
-00000410: 2f4c 6962 7261 7279 2f43 6c6f 7564 5374  /Library/CloudSt
-00000420: 6f72 6167 652f 476f 6f67 6c65 4472 6976  orage/GoogleDriv
-00000430: 652d 6d69 6b72 7562 696e 4067 6d61 696c  e-mikrubin@gmail
-00000440: 2e63 6f6d 2f4d 7920 4472 6976 652f 5079  .com/My Drive/Py
-00000450: 7468 6f6e 2f6d 6170 7461 736b 6572 2f6d  thon/maptasker/m
-00000460: 6170 7461 736b 6572 2f73 7263 2f61 6374  aptasker/src/act
-00000470: 696f 6e72 2e70 79da 1867 6574 5f72 6573  ionr.py..get_res
-00000480: 756c 7473 5f69 6e5f 6172 675f 6f72 6465  ults_in_arg_orde
-00000490: 721a 0000 0073 5600 0000 0401 0c01 0401  r....sV.........
-000004a0: 0201 0a01 0801 0c01 0801 0201 04ff 0280  ................
-000004b0: 0a03 0801 0c01 0e01 0280 0a01 0801 0c01  ................
-000004c0: 0e01 0280 0a01 0801 0c01 0e01 0280 0a01  ................
-000004d0: 0801 0c01 0e01 0280 0601 0801 0c01 0e01  ................
-000004e0: 0280 0201 0401 0801 04ff 0a03 1001 0401  ................
-000004f0: 7214 0000 00da 0964 6963 745f 636f 6465  r......dict_code
-00000500: da08 6172 675f 6c69 7374 da0b 636f 6465  ..arg_list..code
-00000510: 5f61 6374 696f 6eda 0b61 6374 696f 6e5f  _action..action_
-00000520: 7479 7065 da08 636f 6c6f 726d 6170 da0c  type..colormap..
-00000530: 7072 6f67 7261 6d5f 6172 6773 da11 6c6f  program_args..lo
-00000540: 6f6b 7570 5f63 6f64 655f 656e 7472 79da  okup_code_entry.
-00000550: 0d65 7661 6c75 6174 655f 6c69 7374 6309  .evaluate_listc.
-00000560: 0000 0000 0000 0000 0000 0009 0000 000a  ................
-00000570: 0000 0043 0000 0073 6800 0000 7400 7c01  ...C...sh...t.|.
-00000580: 7c00 7c06 7c07 7c02 7c03 7c04 7c05 7c08  |.|.|.|.|.|.|.|.
-00000590: 8309 7d08 7c08 6401 1900 7232 7c08 6402  ..}.|.d...r2|.d.
-000005a0: 1900 7221 7401 a002 7c02 7c08 6402 1900  ..r!t...|.|.d...
-000005b0: 7c08 6403 1900 a103 7c08 6404 3c00 7c08  |.d.....|.d.<.|.
-000005c0: 6405 1900 7232 7401 a003 7c02 7c08 6405  d...r2t...|.|.d.
-000005d0: 1900 7c08 6406 1900 a103 7c08 6407 3c00  ..|.d.....|.d.<.
-000005e0: 7c08 5300 2908 4e5a 0c67 6574 5f78 6d6c  |.S.).NZ.get_xml
-000005f0: 5f66 6c61 675a 0773 7472 6172 6773 5a07  _flagZ.strargsZ.
-00000600: 7374 7265 7661 6c72 0900 0000 5a07 696e  strevalr....Z.in
-00000610: 7461 7267 735a 0769 6e74 6576 616c 720a  targsZ.intevalr.
-00000620: 0000 0029 0472 0300 0000 da0a 6765 745f  ...).r......get_
-00000630: 6163 7469 6f6e 5a1d 6765 745f 786d 6c5f  actionZ.get_xml_
-00000640: 7374 725f 6172 6775 6d65 6e74 5f74 6f5f  str_argument_to_
-00000650: 7661 6c75 655a 1d67 6574 5f78 6d6c 5f69  valueZ.get_xml_i
-00000660: 6e74 5f61 7267 756d 656e 745f 746f 5f76  nt_argument_to_v
-00000670: 616c 7565 2909 7215 0000 0072 1600 0000  alue).r....r....
-00000680: 7217 0000 0072 1800 0000 7219 0000 0072  r....r....r....r
-00000690: 1a00 0000 721b 0000 0072 1c00 0000 7206  ....r....r....r.
-000006a0: 0000 0072 1200 0000 7212 0000 0072 1300  ...r....r....r..
-000006b0: 0000 da14 6576 616c 7561 7465 5f61 6374  ....evaluate_act
-000006c0: 696f 6e5f 6172 6773 4600 0000 732a 0000  ion_argsF...s*..
-000006d0: 0002 0c02 0102 0102 0102 0102 0102 0102  ................
-000006e0: 0102 0102 0104 f708 0c08 0104 010e 0108  ................
-000006f0: ff08 0304 010e 0108 ff04 0472 1e00 0000  ...........r....
-00000700: 6308 0000 0000 0000 0000 0000 000e 0000  c...............
-00000710: 000a 0000 0043 0000 0073 ce00 0000 7400  .....C...s....t.
-00000720: 6401 6402 8400 8301 7d08 6403 7d09 6404  d.d.....}.d.}.d.
-00000730: 7d0a 6405 7d0b 6406 7c00 7600 7314 6407  }.d.}.d.|.v.s.d.
-00000740: 7c00 7600 7219 6404 7d0c 6404 7d0d 6e10  |.v.r.d.}.d.}.n.
-00000750: 6408 7c04 6409 1900 1700 640a 1700 7d0c  d.|.d.....d...}.
-00000760: 6408 7c04 640b 1900 1700 640a 1700 7d0d  d.|.d.....d...}.
-00000770: 7c05 7c01 7c00 1900 640c 3c00 7c06 7c01  |.|.|...d.<.|.|.
-00000780: 7c00 1900 640d 3c00 7c05 7249 7c07 640e  |...d.<.|.rI|.d.
-00000790: 1900 640f 6b03 7249 7401 7c00 7c05 7c02  ..d.k.rIt.|.|.|.
-000007a0: 7c03 7c04 7c07 7c01 7c06 7c08 8309 7d08  |.|.|.|.|.|...}.
-000007b0: 7c08 6410 1900 7251 7402 7c08 8301 7d0a  |.d...rQt.|...}.
-000007c0: 7c0c 7403 7c00 1900 6411 1900 1700 7c0d  |.t.|...d.....|.
-000007d0: 1700 7c09 1700 7c0a 1700 7404 a005 7c02  ..|...|...t...|.
-000007e0: 7c03 7c04 7c07 a104 1700 5300 2912 4e63  |.|.|.....S.).Nc
-000007f0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
-00000800: 0100 0000 5300 0000 7304 0000 0067 0053  ....S...s....g.S
-00000810: 0029 014e 7212 0000 0072 1200 0000 7212  .).Nr....r....r.
-00000820: 0000 0072 1200 0000 7213 0000 00da 083c  ...r....r......<
-00000830: 6c61 6d62 6461 3e7a 0000 0073 0200 0000  lambda>z...s....
-00000840: 0400 7a24 6765 745f 6163 7469 6f6e 5f72  ..z$get_action_r
-00000850: 6573 756c 7473 2e3c 6c6f 6361 6c73 3e2e  esults.<locals>.
-00000860: 3c6c 616d 6264 613e 7a0c 266e 6273 703b  <lambda>z.&nbsp;
-00000870: 266e 6273 703b 7208 0000 0046 da01 73da  &nbsp;r....F..s.
-00000880: 0165 7a13 3c73 7061 6e20 7374 796c 653d  .ez.<span style=
-00000890: 2263 6f6c 6f72 3ada 1161 6374 696f 6e5f  "color:..action_
-000008a0: 6e61 6d65 5f63 6f6c 6f72 7a08 223c 2f73  name_colorz."</s
-000008b0: 7061 6e3e da0c 6163 7469 6f6e 5f63 6f6c  pan>..action_col
-000008c0: 6f72 da07 7265 7161 7267 73da 0865 7661  or..reqargs..eva
-000008d0: 6c61 7267 735a 1464 6973 706c 6179 5f64  largsZ.display_d
-000008e0: 6574 6169 6c5f 6c65 7665 6ce9 0200 0000  etail_level.....
-000008f0: da13 7265 7475 726e 696e 675f 736f 6d65  ..returning_some
-00000900: 7468 696e 67da 0764 6973 706c 6179 2906  thing..display).
-00000910: 7202 0000 0072 1e00 0000 7214 0000 0072  r....r....r....r
-00000920: 0400 0000 721d 0000 00da 0f67 6574 5f65  ....r......get_e
-00000930: 7874 7261 5f73 7475 6666 290e 7215 0000  xtra_stuff).r...
-00000940: 0072 1b00 0000 7217 0000 0072 1800 0000  .r....r....r....
-00000950: 7219 0000 0072 1600 0000 721c 0000 0072  r....r....r....r
-00000960: 1a00 0000 7206 0000 005a 0a74 776f 5f62  ....r....Z.two_b
-00000970: 6c61 6e6b 73da 0672 6573 756c 7472 2700  lanks..resultr'.
-00000980: 0000 5a12 6469 7370 6c61 795f 6e61 6d65  ..Z.display_name
-00000990: 5f63 6f6c 6f72 5a14 6469 7370 6c61 795f  _colorZ.display_
-000009a0: 6465 7461 696c 5f63 6f6c 6f72 7212 0000  detail_colorr...
-000009b0: 0072 1200 0000 7213 0000 00da 1267 6574  .r....r......get
-000009c0: 5f61 6374 696f 6e5f 7265 7375 6c74 736f  _action_resultso
-000009d0: 0000 0073 5200 0000 020a 0601 04ff 0403  ...sR...........
-000009e0: 0401 0401 1001 0401 0601 0e03 02ff 0e04  ................
-000009f0: 02ff 0c06 0c01 1002 0202 0201 0201 0201  ................
-00000a00: 0201 0201 0201 0201 0201 0201 04f7 080e  ................
-00000a10: 0801 0202 0a01 02ff 0202 02fe 0203 02fd  ................
-00000a20: 0204 02fc 0e05 02fb 02ff 722b 0000 0029  ..........r+...)
-00000a30: 1972 0f00 0000 da15 786d 6c2e 6574 7265  .r......xml.etre
-00000a40: 652e 456c 656d 656e 7454 7265 65da 0378  e.ElementTree..x
-00000a50: 6d6c da0b 636f 6c6c 6563 7469 6f6e 7372  ml..collectionsr
-00000a60: 0200 0000 da14 6d61 7074 6173 6b65 722e  ......maptasker.
-00000a70: 7372 632e 6163 7469 6f6e da03 7372 63da  src.action..src.
-00000a80: 0661 6374 696f 6e72 1d00 0000 5a15 6d61  .actionr....Z.ma
-00000a90: 7074 6173 6b65 722e 7372 632e 6163 7461  ptasker.src.acta
-00000aa0: 7267 7372 0300 0000 da15 6d61 7074 6173  rgsr......maptas
-00000ab0: 6b65 722e 7372 632e 6163 7469 6f6e 6372  ker.src.actioncr
-00000ac0: 0400 0000 da16 6d61 7074 6173 6b65 722e  ......maptasker.
-00000ad0: 7372 632e 7379 7363 6f6e 7374 7205 0000  src.sysconstr...
-00000ae0: 00da 0464 6963 74da 0373 7472 7214 0000  ...dict..strr...
-00000af0: 00da 0565 7472 6565 da0b 456c 656d 656e  ...etree..Elemen
-00000b00: 7454 7265 65da 046c 6973 74da 0462 6f6f  tTree..list..boo
-00000b10: 6cda 0574 7570 6c65 721e 0000 0072 2b00  l..tupler....r+.
-00000b20: 0000 7212 0000 0072 1200 0000 7212 0000  ..r....r....r...
-00000b30: 0072 1300 0000 da08 3c6d 6f64 756c 653e  .r......<module>
-00000b40: 0100 0000 7360 0000 0008 0c08 010c 0112  ....s`..........
-00000b50: 020c 010c 010c 0112 0602 2c06 0102 ff02  ..........,.....
-00000b60: 0202 fe06 0302 fd02 0402 fc02 0502 fb02  ................
-00000b70: 0602 fa02 0702 f902 0802 f802 0902 f702  ................
-00000b80: 0a0a f602 2902 0102 ff06 0202 fe06 0302  ....)...........
-00000b90: fd02 0402 fc06 0502 fb06 0602 fa06 0702  ................
-00000ba0: f906 0802 f802 090e f7                   .........
+00000080: 6400 6406 6c0f 6d10 5a10 0100 6400 6407  d.d.l.m.Z...d.d.
+00000090: 6c0f 6d11 5a11 0100 6408 6512 6409 6513  l.m.Z...d.e.d.e.
+000000a0: 6604 640a 640b 8404 5a14 640c 6502 6a15  f.d.d...Z.d.e.j.
+000000b0: 6a16 640d 6517 640e 6502 6a15 6a16 640f  j.d.e.d.e.j.j.d.
+000000c0: 6518 6410 6512 6411 6512 6412 6512 6413  e.d.e.d.e.d.e.d.
+000000d0: 6517 6408 6512 6409 6519 6614 6414 6415  e.d.e.d.e.f.d.d.
+000000e0: 8404 5a1a 640c 6513 6412 6502 6a15 6a16  ..Z.d.e.d.e.j.j.
+000000f0: 640e 6502 6a15 6a16 640f 6518 6410 6502  d.e.j.j.d.e.d.e.
+00000100: 6a15 6a16 640d 6517 6513 1900 6413 6517  j.j.d.e.e...d.e.
+00000110: 6513 1900 6411 6502 6a15 6a16 6409 6513  e...d.e.j.j.d.e.
+00000120: 6612 6416 6417 8404 5a1b 6401 5300 2918  f.d.d...Z.d.S.).
+00000130: e900 0000 004e 2901 da0b 6465 6661 756c  .....N)...defaul
+00000140: 7464 6963 7429 01da 0b61 6374 696f 6e5f  tdict)...action_
+00000150: 6172 6773 2901 da0c 6163 7469 6f6e 5f63  args)...action_c
+00000160: 6f64 6573 2901 da06 6c6f 6767 6572 2901  odes)...logger).
+00000170: da1d 6765 745f 786d 6c5f 696e 745f 6172  ..get_xml_int_ar
+00000180: 6775 6d65 6e74 5f74 6f5f 7661 6c75 6529  gument_to_value)
+00000190: 01da 1d67 6574 5f78 6d6c 5f73 7472 5f61  ...get_xml_str_a
+000001a0: 7267 756d 656e 745f 746f 5f76 616c 7565  rgument_to_value
+000001b0: da11 6576 616c 7561 7465 645f 7265 7375  ..evaluated_resu
+000001c0: 6c74 73da 0672 6574 7572 6e63 0100 0000  lts..returnc....
+000001d0: 0000 0000 0000 0000 0400 0000 0500 0000  ................
+000001e0: 4300 0000 7356 0100 0064 017d 017c 0064  C...sV...d.}.|.d
+000001f0: 0219 0044 005d a27d 0264 017d 037c 0204  ...D.].}.d.}.|..
+00000200: 0064 036b 0272 2201 007c 0064 0419 0072  .d.k.r"..|.d...r
+00000210: 217c 0064 0419 0064 0519 007d 037c 0064  !|.d...d...}.|.d
+00000220: 0419 00a0 0064 05a1 0101 006e 7f04 0064  .....d.....n...d
+00000230: 066b 0272 3901 007c 0064 0719 0072 387c  .k.r9..|.d...r8|
+00000240: 0064 0719 0064 0519 007d 037c 0064 0719  .d...d...}.|.d..
+00000250: 00a0 0064 05a1 0101 006e 6804 0064 086b  ...d.....nh..d.k
+00000260: 0272 5001 007c 0064 0919 0072 4f7c 0064  .rP..|.d...rO|.d
+00000270: 0919 0064 0519 007d 037c 0064 0919 00a0  ...d...}.|.d....
+00000280: 0064 05a1 0101 006e 5104 0064 0a6b 0272  .d.....nQ..d.k.r
+00000290: 6701 007c 0064 0b19 0072 667c 0064 0b19  g..|.d...rf|.d..
+000002a0: 0064 0519 007d 037c 0064 0b19 00a0 0064  .d...}.|.d.....d
+000002b0: 05a1 0101 006e 3a04 0064 0c6b 0272 7e01  .....n:..d.k.r~.
+000002c0: 007c 0064 0d19 0072 7d7c 0064 0d19 0064  .|.d...r}|.d...d
+000002d0: 0519 007d 037c 0064 0d19 00a0 0064 05a1  ...}.|.d.....d..
+000002e0: 0101 006e 2364 0e6b 0272 937c 0064 0f19  ...n#d.k.r.|.d..
+000002f0: 0072 927c 0064 0f19 0064 0519 007d 037c  .r.|.d...d...}.|
+00000300: 0064 0f19 00a0 0064 05a1 0101 006e 0e09  .d.....d.....n..
+00000310: 0074 01a0 0264 107c 029b 009d 02a1 0101  .t...d.|........
+00000320: 0074 03a0 0464 11a1 0101 007c 019b 0064  .t...d.....|...d
+00000330: 127c 039b 009d 037d 0171 067c 0153 0029  .|.....}.q.|.S.)
+00000340: 134e da00 5a11 706f 7369 7469 6f6e 5f61  .N..Z.position_a
+00000350: 7267 5f74 7970 655a 0353 7472 da0a 7265  rg_typeZ.Str..re
+00000360: 7375 6c74 5f73 7472 7201 0000 005a 0349  sult_strr....Z.I
+00000370: 6e74 da0a 7265 7375 6c74 5f69 6e74 5a03  nt..result_intZ.
+00000380: 4170 705a 0a72 6573 756c 745f 6170 705a  AppZ.result_appZ
+00000390: 0d43 6f6e 6469 7469 6f6e 4c69 7374 5a0a  .ConditionListZ.
+000003a0: 7265 7375 6c74 5f63 6f6e 5a03 496d 675a  result_conZ.ImgZ
+000003b0: 0a72 6573 756c 745f 696d 675a 0642 756e  .result_imgZ.Bun
+000003c0: 646c 655a 0a72 6573 756c 745f 6275 6e7a  dleZ.result_bunz
+000003d0: 3646 756e 6374 696f 6e20 6765 745f 7265  6Function get_re
+000003e0: 7375 6c74 735f 696e 5f61 7267 5f6f 7264  sults_in_arg_ord
+000003f0: 6572 3a20 6e6f 206d 6174 6368 2066 6f72  er: no match for
+00000400: 2022 6172 6722 3ae9 0800 0000 fa01 2029   "arg":....... )
+00000410: 05da 0370 6f70 7205 0000 00da 0564 6562  ...popr......deb
+00000420: 7567 da03 7379 73da 0465 7869 7429 0472  ug..sys..exit).r
+00000430: 0800 0000 5a0d 7265 7475 726e 5f72 6573  ....Z.return_res
+00000440: 756c 74da 0361 7267 5a08 7468 655f 6974  ult..argZ.the_it
+00000450: 656d a900 7214 0000 00fa 762f 5573 6572  em..r.....v/User
+00000460: 732f 6d69 6b72 7562 696e 2f4c 6962 7261  s/mikrubin/Libra
+00000470: 7279 2f43 6c6f 7564 5374 6f72 6167 652f  ry/CloudStorage/
+00000480: 476f 6f67 6c65 4472 6976 652d 6d69 6b72  GoogleDrive-mikr
+00000490: 7562 696e 4067 6d61 696c 2e63 6f6d 2f4d  ubin@gmail.com/M
+000004a0: 7920 4472 6976 652f 5079 7468 6f6e 2f6d  y Drive/Python/m
+000004b0: 6170 7461 736b 6572 2f6d 6170 7461 736b  aptasker/maptask
+000004c0: 6572 2f73 7263 2f61 6374 696f 6e72 2e70  er/src/actionr.p
+000004d0: 79da 1867 6574 5f72 6573 756c 7473 5f69  y..get_results_i
+000004e0: 6e5f 6172 675f 6f72 6465 721c 0000 0073  n_arg_order....s
+000004f0: 5600 0000 0401 0c01 0401 0201 0a01 0801  V...............
+00000500: 0c01 0801 0201 04ff 0280 0a03 0801 0c01  ................
+00000510: 0e01 0280 0a01 0801 0c01 0e01 0280 0a01  ................
+00000520: 0801 0c01 0e01 0280 0a01 0801 0c01 0e01  ................
+00000530: 0280 0601 0801 0c01 0e01 0280 0201 0401  ................
+00000540: 0801 04ff 0a03 1001 0401 7216 0000 00da  ..........r.....
+00000550: 0964 6963 745f 636f 6465 da08 6172 675f  .dict_code..arg_
+00000560: 6c69 7374 da0b 636f 6465 5f61 6374 696f  list..code_actio
+00000570: 6eda 0b61 6374 696f 6e5f 7479 7065 da08  n..action_type..
+00000580: 636f 6c6f 726d 6170 da0c 7072 6f67 7261  colormap..progra
+00000590: 6d5f 6172 6773 da11 6c6f 6f6b 7570 5f63  m_args..lookup_c
+000005a0: 6f64 655f 656e 7472 79da 0d65 7661 6c75  ode_entry..evalu
+000005b0: 6174 655f 6c69 7374 6309 0000 0000 0000  ate_listc.......
+000005c0: 0000 0000 0009 0000 000a 0000 0043 0000  .............C..
+000005d0: 0073 6400 0000 7400 7c01 7c00 7c06 7c07  .sd...t.|.|.|.|.
+000005e0: 7c02 7c03 7c04 7c05 7c08 8309 7d08 7c08  |.|.|.|.|...}.|.
+000005f0: 6401 1900 7230 7c08 6402 1900 7220 7401  d...r0|.d...r t.
+00000600: 7c02 7c08 6402 1900 7c08 6403 1900 8303  |.|.d...|.d.....
+00000610: 7c08 6404 3c00 7c08 6405 1900 7230 7402  |.d.<.|.d...r0t.
+00000620: 7c02 7c08 6405 1900 7c08 6406 1900 8303  |.|.d...|.d.....
+00000630: 7c08 6407 3c00 7c08 5300 2908 4e5a 0c67  |.d.<.|.S.).NZ.g
+00000640: 6574 5f78 6d6c 5f66 6c61 675a 0773 7472  et_xml_flagZ.str
+00000650: 6172 6773 5a07 7374 7265 7661 6c72 0b00  argsZ.strevalr..
+00000660: 0000 5a07 696e 7461 7267 735a 0769 6e74  ..Z.intargsZ.int
+00000670: 6576 616c 720c 0000 0029 0372 0300 0000  evalr....).r....
+00000680: 7207 0000 0072 0600 0000 2909 7217 0000  r....r....).r...
+00000690: 0072 1800 0000 7219 0000 0072 1a00 0000  .r....r....r....
+000006a0: 721b 0000 0072 1c00 0000 721d 0000 0072  r....r....r....r
+000006b0: 1e00 0000 7208 0000 0072 1400 0000 7214  ....r....r....r.
+000006c0: 0000 0072 1500 0000 da14 6576 616c 7561  ...r......evalua
+000006d0: 7465 5f61 6374 696f 6e5f 6172 6773 4800  te_action_argsH.
+000006e0: 0000 732a 0000 0002 0c02 0102 0102 0102  ..s*............
+000006f0: 0102 0102 0102 0102 0102 0104 f708 0c08  ................
+00000700: 0102 010e 0108 ff08 0302 010e 0108 ff04  ................
+00000710: 0472 1f00 0000 6308 0000 0000 0000 0000  .r....c.........
+00000720: 0000 000d 0000 000a 0000 0043 0000 0073  ...........C...s
+00000730: da00 0000 7400 6401 6402 8400 8301 7d08  ....t.d.d.....}.
+00000740: 6403 7d09 6404 7d0a 6405 7c00 7600 7312  d.}.d.}.d.|.v.s.
+00000750: 6406 7c00 7600 7217 6404 7d0b 6404 7d0c  d.|.v.r.d.}.d.}.
+00000760: 6e18 6407 7c04 6408 1900 1700 7c07 6409  n.d.|.d.....|.d.
+00000770: 1900 1700 640a 1700 7d0b 640b 7c04 640c  ....d...}.d.|.d.
+00000780: 1900 1700 7c07 6409 1900 1700 640a 1700  ....|.d.....d...
+00000790: 7d0c 7c05 7c01 7c00 1900 640d 3c00 7c06  }.|.|.|...d.<.|.
+000007a0: 7c01 7c00 1900 640e 3c00 7c05 724f 7c07  |.|...d.<.|.rO|.
+000007b0: 640f 1900 6410 6b03 724f 7401 7c00 7c05  d...d.k.rOt.|.|.
+000007c0: 7c02 7c03 7c04 7c07 7c01 7c06 7c08 8309  |.|.|.|.|.|.|...
+000007d0: 7d08 7c08 6411 1900 7257 7402 7c08 8301  }.|.d...rWt.|...
+000007e0: 7d0a 7c0b 7403 7c00 1900 6412 1900 1700  }.|.t.|...d.....
+000007f0: 7c0c 1700 7c09 1700 7c0a 1700 7404 a005  |...|...|...t...
+00000800: 7c02 7c03 7c04 7c07 a104 1700 5300 2913  |.|.|.|.....S.).
+00000810: 4e63 0000 0000 0000 0000 0000 0000 0000  Nc..............
+00000820: 0000 0100 0000 5300 0000 7304 0000 0067  ......S...s....g
+00000830: 0053 0029 014e 7214 0000 0072 1400 0000  .S.).Nr....r....
+00000840: 7214 0000 0072 1400 0000 7215 0000 00da  r....r....r.....
+00000850: 083c 6c61 6d62 6461 3e7c 0000 0073 0200  .<lambda>|...s..
+00000860: 0000 0400 7a24 6765 745f 6163 7469 6f6e  ....z$get_action
+00000870: 5f72 6573 756c 7473 2e3c 6c6f 6361 6c73  _results.<locals
+00000880: 3e2e 3c6c 616d 6264 613e 7a0c 266e 6273  >.<lambda>z.&nbs
+00000890: 703b 266e 6273 703b 720a 0000 00da 0173  p;&nbsp;r......s
+000008a0: da01 657a 133c 7370 616e 2073 7479 6c65  ..ez.<span style
+000008b0: 3d22 636f 6c6f 723a da11 6163 7469 6f6e  ="color:..action
+000008c0: 5f6e 616d 655f 636f 6c6f 72da 0b66 6f6e  _name_color..fon
+000008d0: 745f 746f 5f75 7365 fa01 3e7a 1a3c 2f73  t_to_use..>z.</s
+000008e0: 7061 6e3e 3c73 7061 6e20 7374 796c 653d  pan><span style=
+000008f0: 2263 6f6c 6f72 3ada 0c61 6374 696f 6e5f  "color:..action_
+00000900: 636f 6c6f 72da 0772 6571 6172 6773 da08  color..reqargs..
+00000910: 6576 616c 6172 6773 5a14 6469 7370 6c61  evalargsZ.displa
+00000920: 795f 6465 7461 696c 5f6c 6576 656c e902  y_detail_level..
+00000930: 0000 005a 1372 6574 7572 6e69 6e67 5f73  ...Z.returning_s
+00000940: 6f6d 6574 6869 6e67 da07 6469 7370 6c61  omething..displa
+00000950: 7929 0672 0200 0000 721f 0000 0072 1600  y).r....r....r..
+00000960: 0000 7204 0000 00da 0a67 6574 5f61 6374  ..r......get_act
+00000970: 696f 6eda 0f67 6574 5f65 7874 7261 5f73  ion..get_extra_s
+00000980: 7475 6666 290d 7217 0000 0072 1d00 0000  tuff).r....r....
+00000990: 7219 0000 0072 1a00 0000 721b 0000 0072  r....r....r....r
+000009a0: 1800 0000 721e 0000 0072 1c00 0000 7208  ....r....r....r.
+000009b0: 0000 005a 0a74 776f 5f62 6c61 6e6b 73da  ...Z.two_blanks.
+000009c0: 0672 6573 756c 745a 1264 6973 706c 6179  .resultZ.display
+000009d0: 5f6e 616d 655f 636f 6c6f 725a 1464 6973  _name_colorZ.dis
+000009e0: 706c 6179 5f64 6574 6169 6c5f 636f 6c6f  play_detail_colo
+000009f0: 7272 1400 0000 7214 0000 0072 1500 0000  rr....r....r....
+00000a00: da12 6765 745f 6163 7469 6f6e 5f72 6573  ..get_action_res
+00000a10: 756c 7473 7100 0000 7368 0000 0002 0a06  ultsq...sh......
+00000a20: 0104 ff04 0304 0110 0104 0106 0102 0306  ................
+00000a30: 0102 ff06 0202 fe02 0302 fd02 ff02 0706  ................
+00000a40: 0102 ff06 0202 fe02 0302 fd02 ff0c 090c  ................
+00000a50: 0110 0202 0202 0102 0102 0102 0102 0102  ................
+00000a60: 0102 0102 0102 0104 f708 0e08 0102 020a  ................
+00000a70: 0102 ff02 0202 fe02 0302 fd02 0402 fc0e  ................
+00000a80: 0502 fb02 ff72 2e00 0000 291c 7211 0000  .....r....).r...
+00000a90: 00da 1578 6d6c 2e65 7472 6565 2e45 6c65  ...xml.etree.Ele
+00000aa0: 6d65 6e74 5472 6565 da03 786d 6cda 0b63  mentTree..xml..c
+00000ab0: 6f6c 6c65 6374 696f 6e73 7202 0000 00da  ollectionsr.....
+00000ac0: 146d 6170 7461 736b 6572 2e73 7263 2e61  .maptasker.src.a
+00000ad0: 6374 696f 6eda 0373 7263 da06 6163 7469  ction..src..acti
+00000ae0: 6f6e 722b 0000 005a 156d 6170 7461 736b  onr+...Z.maptask
+00000af0: 6572 2e73 7263 2e61 6374 6172 6773 7203  er.src.actargsr.
+00000b00: 0000 00da 156d 6170 7461 736b 6572 2e73  .....maptasker.s
+00000b10: 7263 2e61 6374 696f 6e63 7204 0000 00da  rc.actioncr.....
+00000b20: 166d 6170 7461 736b 6572 2e73 7263 2e73  .maptasker.src.s
+00000b30: 7973 636f 6e73 7472 0500 0000 5a15 6d61  ysconstr....Z.ma
+00000b40: 7074 6173 6b65 722e 7372 632e 786d 6c64  ptasker.src.xmld
+00000b50: 6174 6172 0600 0000 7207 0000 00da 0464  atar....r......d
+00000b60: 6963 74da 0373 7472 7216 0000 00da 0565  ict..strr......e
+00000b70: 7472 6565 da0b 456c 656d 656e 7454 7265  tree..ElementTre
+00000b80: 65da 046c 6973 74da 0462 6f6f 6cda 0574  e..list..bool..t
+00000b90: 7570 6c65 721f 0000 0072 2e00 0000 7214  upler....r....r.
+00000ba0: 0000 0072 1400 0000 7214 0000 0072 1500  ...r....r....r..
+00000bb0: 0000 da08 3c6d 6f64 756c 653e 0100 0000  ....<module>....
+00000bc0: 7364 0000 0008 0c08 010c 0112 020c 010c  sd..............
+00000bd0: 010c 010c 010c 0112 0602 2c06 0102 ff02  ..........,.....
+00000be0: 0202 fe06 0302 fd02 0402 fc02 0502 fb02  ................
+00000bf0: 0602 fa02 0702 f902 0802 f802 0902 f702  ................
+00000c00: 0a0a f602 2902 0102 ff06 0202 fe06 0302  ....)...........
+00000c10: fd02 0402 fc06 0502 fb06 0602 fa06 0702  ................
+00000c20: f906 0802 f802 090e f7                   .........
```

### Comparing `maptasker-1.3.1/maptasker/src/__pycache__/actiont.cpython-310.pyc` & `maptasker-1.3.2/maptasker/src/__pycache__/actiont.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 10 18:26:19 2023 UTC, .py size: 17381 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 4b76 0b64 e543 0000  o.......Kv.d.C..
+00000000: 6f0d 0d0a 0000 0000 918f 1c64 e543 0000  o..........d.C..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0013 0000 0040 0000 0073 8e0d 0000 6900  .....@...s....i.
 00000030: 6400 6401 6402 6403 6404 6405 6406 9c05  d.d.d.d.d.d.d...
 00000040: 9301 6407 6408 6409 640a 640b 9c03 9301  ..d.d.d.d.d.....
 00000050: 640c 6408 640d 640e 640f 6410 6406 9c05  d.d.d.d.d.d.d...
 00000060: 9301 6411 6408 6412 6413 640b 9c03 9301  ..d.d.d.d.d.....
 00000070: 6414 6415 6416 6408 640b 9c03 9301 6417  d.d.d.d.d.....d.
@@ -241,15 +241,15 @@
 00000f00: 2042 6172 7a13 4163 7469 7669 7479 2c20   Barz.Activity, 
 00000f10: 4e6f 2053 7461 7475 737a 2341 6374 6976  No Statusz#Activ
 00000f20: 6974 792c 204e 6f20 4261 722c 204e 6f20  ity, No Bar, No 
 00000f30: 5374 6174 7573 2c20 4e6f 204e 6176 290a  Status, No Nav).
 00000f40: 7204 0000 0072 0500 0000 7206 0000 0072  r....r....r....r
 00000f50: 0700 0000 7208 0000 00e9 0500 0000 e906  ....r...........
 00000f60: 0000 00e9 0700 0000 e908 0000 00e9 0900  ................
-00000f70: 0000 da02 3438 5a06 5379 7374 656d da04  ....48Z.System..
+00000f70: 0000 da02 3438 da06 5379 7374 656d da04  ....48..System..
 00000f80: 4e6f 6e65 5a04 4661 6465 7a0b 426f 7474  NoneZ.Fadez.Bott
 00000f90: 6f6d 2046 6164 655a 044c 6566 745a 0552  om FadeZ.LeftZ.R
 00000fa0: 6967 6874 5a03 546f 705a 0642 6f74 746f  ightZ.TopZ.Botto
 00000fb0: 6d7a 094c 6566 7420 526f 6c6c 7a0a 5269  mz.Left Rollz.Ri
 00000fc0: 6768 7420 526f 6c6c da05 5363 616c 6529  ght Roll..Scale)
 00000fd0: 0b72 0400 0000 7205 0000 0072 0600 0000  .r....r....r....
 00000fe0: 7207 0000 0072 0800 0000 7210 0000 0072  r....r....r....r
@@ -262,15 +262,15 @@
 00001050: 746f 7279 7206 0000 005a 0446 696e 6472  toryr....Z.Findr
 00001060: 0700 0000 7a09 4669 6e64 204e 6578 7472  ....z.Find Nextr
 00001070: 0800 0000 7a07 476f 2042 6163 6b72 1000  ....z.Go Backr..
 00001080: 0000 7a0a 476f 2046 6f72 7761 7264 7211  ..z.Go Forwardr.
 00001090: 0000 007a 084c 6f61 6420 5552 4c72 1200  ...z.Load URLr..
 000010a0: 0000 7a0b 5061 6765 2042 7574 746f 6e72  ..z.Page Buttonr
 000010b0: 1300 0000 7a09 5061 6765 2044 6f77 6e72  ....z.Page Downr
-000010c0: 1400 0000 7a08 5061 6765 2054 6f70 7218  ....z.Page Topr.
+000010c0: 1400 0000 7a08 5061 6765 2054 6f70 7219  ....z.Page Topr.
 000010d0: 0000 007a 0750 6167 6520 5570 e90b 0000  ...z.Page Up....
 000010e0: 005a 0652 656c 6f61 64e9 0c00 0000 7a12  .Z.Reload.....z.
 000010f0: 5368 6f77 205a 6f6f 6d20 436f 6e74 726f  Show Zoom Contro
 00001100: 6c73 e90d 0000 007a 0c53 746f 7020 4c6f  ls.....z.Stop Lo
 00001110: 6164 696e 67e9 0e00 0000 7a07 5a6f 6f6d  ading.....z.Zoom
 00001120: 2049 6ee9 0f00 0000 7a08 5a6f 6f6d 204f   In.....z.Zoom O
 00001130: 7574 da02 3537 5a03 416c 6cda 0850 6f72  ut..57Z.All..Por
@@ -353,17 +353,17 @@
 00001600: 6961 626c 6520 416c 6172 6d73 7a07 5275  iable Alarmsz.Ru
 00001610: 6e20 4c6f 677a 1344 6562 7567 2054 6f20  n Logz.Debug To 
 00001620: 5379 7374 656d 204c 6f67 7a19 4465 6275  System Logz.Debu
 00001630: 6720 546f 2049 6e74 6572 6e61 6c20 5374  g To Internal St
 00001640: 6f72 6167 657a 094c 6f63 6b20 436f 6465  oragez.Lock Code
 00001650: 7a10 4170 7020 4368 6563 6b20 4d65 7468  z.App Check Meth
 00001660: 6f64 7a14 5573 6520 4d6f 7469 6f6e 2044  odz.Use Motion D
-00001670: 6574 6563 7469 6f6e 290c 7225 0000 0072  etection).r%...r
-00001680: 2600 0000 7227 0000 0072 2800 0000 7229  &...r'...r(...r)
-00001690: 0000 0072 2a00 0000 e917 0000 00e9 1800  ...r*...........
+00001670: 6574 6563 7469 6f6e 290c 7226 0000 0072  etection).r&...r
+00001680: 2700 0000 7228 0000 0072 2900 0000 722a  '...r(...r)...r*
+00001690: 0000 0072 2b00 0000 e917 0000 00e9 1800  ...r+...........
 000016a0: 0000 e919 0000 00e9 1a00 0000 e91b 0000  ................
 000016b0: 00e9 1c00 0000 da03 3133 357a 0d41 6374  ........135z.Act
 000016c0: 696f 6e20 4e75 6d62 6572 7a0c 4163 7469  ion Numberz.Acti
 000016d0: 6f6e 204c 6162 656c 7a0b 546f 7020 6f66  on Labelz.Top of
 000016e0: 204c 6f6f 707a 0b45 6e64 206f 6620 4c6f   Loopz.End of Lo
 000016f0: 6f70 7a09 456e 6420 6f66 2049 66da 0331  opz.End of If..1
 00001700: 3437 5a02 5549 5a07 4d6f 6e69 746f 72da  47Z.UIZ.Monitor.
@@ -381,16 +381,16 @@
 000017c0: 7373 2053 746f 7261 6765 7a16 5769 7265  ss Storagez.Wire
 000017d0: 6c65 7373 204d 6973 6365 6c6c 616e 656f  less Miscellaneo
 000017e0: 7573 7a0d 5065 7220 496e 7465 7266 6163  usz.Per Interfac
 000017f0: 655a 0850 6879 7369 6361 6c5a 0750 7269  eZ.PhysicalZ.Pri
 00001800: 6e74 6572 7a0e 4469 6769 7461 6c20 4361  nterz.Digital Ca
 00001810: 6d65 7261 7a0f 5665 6e64 6f72 2053 7065  meraz.Vendor Spe
 00001820: 6369 6669 637a 1357 6972 656c 6573 7320  cificz.Wireless 
-00001830: 436f 6e74 726f 6c6c 6572 2902 7225 0000  Controller).r%..
-00001840: 0072 2600 0000 da03 3135 33da 0454 6173  .r&.....153..Tas
+00001830: 436f 6e74 726f 6c6c 6572 2902 7226 0000  Controller).r&..
+00001840: 0072 2700 0000 da03 3135 33da 0454 6173  .r'.....153..Tas
 00001850: 6b5a 0d43 6f6e 6669 6775 7261 7469 6f6e  kZ.Configuration
 00001860: da04 3135 3361 5a06 536f 7572 6365 da03  ..153aZ.Source..
 00001870: 3135 365a 0654 6173 6b65 72da 0431 3536  156Z.Tasker..156
 00001880: 615a 0745 6e67 6c69 7368 5a06 4765 726d  aZ.EnglishZ.Germ
 00001890: 616e da03 3136 30da 0359 6573 da02 4e6f  an..160..Yes..No
 000018a0: da03 3136 325a 0331 7374 5a03 326e 645a  ..162Z.1stZ.2ndZ
 000018b0: 0333 7264 da04 3136 3261 5a06 4163 7469  .3rd..162aZ.Acti
@@ -470,16 +470,16 @@
 00001d50: 6f6e 6e65 6374 6564 7a0e 4254 2044 6576  onnectedz.BT Dev
 00001d60: 6963 6520 4e61 6d65 7a14 4254 2044 6576  ice Namez.BT Dev
 00001d70: 6963 6520 436c 6173 7320 4e61 6d65 7a09  ice Class Namez.
 00001d80: 4175 746f 2053 796e 637a 0f57 6966 6920  Auto Syncz.Wifi 
 00001d90: 4950 2041 6464 7265 7373 290c 7204 0000  IP Address).r...
 00001da0: 0072 0500 0000 7206 0000 0072 0700 0000  .r....r....r....
 00001db0: 7208 0000 0072 1000 0000 7211 0000 0072  r....r....r....r
-00001dc0: 1200 0000 7213 0000 0072 1400 0000 7218  ....r....r....r.
-00001dd0: 0000 0072 1b00 0000 da03 3334 327a 0a50  ...r......342z.P
+00001dc0: 1200 0000 7213 0000 0072 1400 0000 7219  ....r....r....r.
+00001dd0: 0000 0072 1c00 0000 da03 3334 327a 0a50  ...r......342z.P
 00001de0: 6172 656e 7420 4469 725a 094d 6f70 6469  arent DirZ.Mopdi
 00001df0: 6669 6564 da04 4e61 6d65 5a04 5369 7a65  fied..NameZ.Size
 00001e00: da04 5479 7065 5a06 4578 6973 7473 5a03  ..TypeZ.ExistsZ.
 00001e10: 4d44 357a 0742 6173 6520 3634 da03 3334  MD5z.Base 64..34
 00001e20: 337a 154d 7573 6963 2046 696c 6520 4172  3z.Music File Ar
 00001e30: 7469 7374 2054 6167 7a17 4d75 7369 6320  tist Tagz.Music 
 00001e40: 4669 6c65 2044 7572 6174 696f 6e20 5461  File Duration Ta
@@ -563,16 +563,16 @@
 00002320: 6972 7374 7a15 536f 7274 204e 756d 6572  irstz.Sort Numer
 00002330: 6963 2c20 496e 7465 6765 727a 0c53 6f72  ic, Integerz.Sor
 00002340: 7420 4e75 6d65 7269 637a 0e46 6c6f 6174  t Numericz.Float
 00002350: 696e 672d 506f 696e 745a 0653 7175 6173  ing-PointZ.Squas
 00002360: 6829 0f72 0400 0000 7205 0000 0072 0600  h).r....r....r..
 00002370: 0000 7207 0000 0072 0800 0000 7210 0000  ..r....r....r...
 00002380: 0072 1100 0000 7212 0000 0072 1300 0000  .r....r....r....
-00002390: 7214 0000 0072 1800 0000 721b 0000 0072  r....r....r....r
-000023a0: 1c00 0000 721d 0000 0072 1e00 0000 da03  ....r....r......
+00002390: 7214 0000 0072 1900 0000 721c 0000 0072  r....r....r....r
+000023a0: 1d00 0000 721e 0000 0072 1f00 0000 da03  ....r....r......
 000023b0: 3337 34da 0453 746f 70da 0333 3738 7a12  374..Stop..378z.
 000023c0: 5365 6c65 6374 2053 696e 676c 6520 4974  Select Single It
 000023d0: 656d 7a10 4d75 6c74 6970 6c65 2043 686f  emz.Multiple Cho
 000023e0: 6963 6573 da03 3338 335a 0c43 6f6e 6e65  ices..383Z.Conne
 000023f0: 6374 6976 6974 79da 034e 4643 5a06 566f  ctivity..NFCZ.Vo
 00002400: 6c75 6d65 5a04 5769 4669 7a0c 4d65 6469  lumeZ.WiFiz.Medi
 00002410: 6120 4f75 7470 7574 da03 3338 347a 0841  a Output..384z.A
@@ -680,18 +680,18 @@
 00002a70: 4261 7365 3635 2045 6e63 6f64 657a 0d42  Base65 Encodez.B
 00002a80: 6173 6536 3520 4465 636f 6465 7a0d 546f  ase65 Decodez.To
 00002a90: 204d 4435 2044 6967 6573 747a 0e54 6f20   MD5 Digestz.To 
 00002aa0: 5348 4131 2044 6967 6573 747a 0d54 6f20  SHA1 Digestz.To 
 00002ab0: 4c6f 7765 7220 4361 7365 7a0d 546f 2055  Lower Casez.To U
 00002ac0: 7070 6572 2043 6173 657a 1254 6f20 5570  pper Casez.To Up
 00002ad0: 7065 7263 6173 6520 4669 7273 7429 0e72  percase First).r
-00002ae0: 2500 0000 7226 0000 0072 2700 0000 7228  %...r&...r'...r(
-00002af0: 0000 0072 2900 0000 722a 0000 0072 3a00  ...r)...r*...r:.
-00002b00: 0000 723b 0000 0072 3c00 0000 723d 0000  ..r;...r<...r=..
-00002b10: 0072 3e00 0000 723f 0000 00e9 1d00 0000  .r>...r?........
+00002ae0: 2600 0000 7227 0000 0072 2800 0000 7229  &...r'...r(...r)
+00002af0: 0000 0072 2a00 0000 722b 0000 0072 3b00  ...r*...r+...r;.
+00002b00: 0000 723c 0000 0072 3d00 0000 723e 0000  ..r<...r=...r>..
+00002b10: 0072 3f00 0000 7240 0000 00e9 1d00 0000  .r?...r@........
 00002b20: e91e 0000 00da 0336 3132 5a04 476f 746f  .......612Z.Goto
 00002b30: 5a04 4c6f 6164 5a04 506c 6179 5a04 4261  Z.LoadZ.PlayZ.Ba
 00002b40: 636b 5a07 466f 7277 6172 64da 0336 3635  ckZ.Forward..665
 00002b50: da03 3831 355a 0750 6163 6b61 6765 da03  ..815Z.Package..
 00002b60: 4170 705a 0852 6563 6569 7665 725a 0853  AppZ.ReceiverZ.S
 00002b70: 6572 7669 6365 735a 0850 726f 7669 6465  ervicesZ.Provide
 00002b80: 72da 0338 3230 7a0d 5769 7468 2041 4320  r..820z.With AC 
@@ -709,16 +709,16 @@
 00002c40: 7220 446f 636b 7a09 4465 736b 2044 6f63  r Dockz.Desk Doc
 00002c50: 6b5a 0448 6f6d 65da 0449 6e66 6f5a 0a50  kZ.Home..InfoZ.P
 00002c60: 7265 6665 7265 6e63 657a 0c53 656c 6563  referencez.Selec
 00002c70: 7465 6420 416c 745a 0354 6162 5a09 4361  ted AltZ.TabZ.Ca
 00002c80: 7264 626f 6172 6429 0e72 0400 0000 7205  rdboard).r....r.
 00002c90: 0000 0072 0600 0000 7207 0000 0072 0800  ...r....r....r..
 00002ca0: 0000 7210 0000 0072 1100 0000 7212 0000  ..r....r....r...
-00002cb0: 0072 1300 0000 7214 0000 0072 1800 0000  .r....r....r....
-00002cc0: 721b 0000 0072 1c00 0000 721d 0000 00da  r....r....r.....
+00002cb0: 0072 1300 0000 7214 0000 0072 1900 0000  .r....r....r....
+00002cc0: 721c 0000 0072 1d00 0000 721e 0000 00da  r....r....r.....
 00002cd0: 0438 3737 617a 1242 726f 6164 6361 7374  .877az.Broadcast
 00002ce0: 2052 6563 6569 7665 725a 0753 6572 7669   ReceiverZ.Servi
 00002cf0: 6365 da03 3930 31da 0347 5053 5a03 4e65  ce..901..GPSZ.Ne
 00002d00: 74da 0339 3033 7a09 4672 6565 2046 6f72  t..903z.Free For
 00002d10: 6d7a 0a57 6562 2053 6561 7263 68da 0339  mz.Web Search..9
 00002d20: 3035 7a0b 4465 7669 6365 204f 6e6c 797a  05z.Device Onlyz
 00002d30: 0e42 6174 7465 7279 2053 6176 696e 677a  .Battery Savingz
@@ -750,15 +750,15 @@
 00002ed0: 686f 7274 5a05 5368 6f72 745a 044c 6f6e  hortZ.ShortZ.Lon
 00002ee0: 677a 0956 6572 7920 4c6f 6e67 2909 da03  gz.Very Long)...
 00002ef0: 3930 36da 0339 3039 da03 3931 30da 0532  906..909..910..2
 00002f00: 3037 3965 da05 3230 3831 65da 0533 3030  079e..2081e..300
 00002f10: 3165 da06 3330 3031 6561 da06 3330 3031  1e..3001ea..3001
 00002f20: 6562 da0a 7377 6974 6368 5f73 6574 4e29  eb..switch_setN)
 00002f30: 01da 0d6c 6f6f 6b75 705f 7661 6c75 6573  ...lookup_values
-00002f40: a900 72c8 0000 0072 c800 0000 fa76 2f55  ..r....r.....v/U
+00002f40: a900 72c9 0000 0072 c900 0000 fa76 2f55  ..r....r.....v/U
 00002f50: 7365 7273 2f6d 696b 7275 6269 6e2f 4c69  sers/mikrubin/Li
 00002f60: 6272 6172 792f 436c 6f75 6453 746f 7261  brary/CloudStora
 00002f70: 6765 2f47 6f6f 676c 6544 7269 7665 2d6d  ge/GoogleDrive-m
 00002f80: 696b 7275 6269 6e40 676d 6169 6c2e 636f  ikrubin@gmail.co
 00002f90: 6d2f 4d79 2044 7269 7665 2f50 7974 686f  m/My Drive/Pytho
 00002fa0: 6e2f 6d61 7074 6173 6b65 722f 6d61 7074  n/maptasker/mapt
 00002fb0: 6173 6b65 722f 7372 632f 6163 7469 6f6e  asker/src/action
```

### Comparing `maptasker-1.3.1/maptasker/src/__pycache__/argsdict.cpython-310.pyc` & `maptasker-1.3.2/maptasker/src/__pycache__/argsdict.cpython-310.pyc`

 * *Files identical despite different names*

### Comparing `maptasker-1.3.1/maptasker/src/__pycache__/caveats.cpython-310.pyc` & `maptasker-1.3.2/maptasker/src/__pycache__/caveats.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 17 16:35:42 2023 UTC, .py size: 3691 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 15% similar despite different names*

```diff
@@ -1,128 +1,116 @@
-00000000: 6f0d 0d0a 0000 0000 de96 1464 6b0e 0000  o..........dk...
+00000000: 6f0d 0d0a 0000 0000 b541 2c64 490d 0000  o........A,dI...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
-00000020: 0008 0000 0040 0000 0073 4000 0000 6400  .....@...s@...d.
+00000020: 0008 0000 0040 0000 0073 3400 0000 6400  .....@...s4...d.
 00000030: 6401 6c00 6d01 0200 0100 6d02 5a03 0100  d.l.m.....m.Z...
-00000040: 6400 6402 6c04 6d05 5a05 0100 6403 6506  d.d.l.m.Z...d.e.
-00000050: 6507 1900 6404 6508 6405 6508 6406 6401  e...d.e.d.e.d.d.
-00000060: 6608 6407 6408 8404 5a09 6401 5300 2909  f.d.d...Z.d.S.).
-00000070: e900 0000 004e 2901 da17 7472 6169 6c69  .....N)...traili
-00000080: 6e67 5f63 6f6d 6d65 6e74 735f 636f 6c6f  ng_comments_colo
-00000090: 72da 0b6f 7574 7075 745f 6c69 7374 da0c  r..output_list..
-000000a0: 7072 6f67 7261 6d5f 6172 6773 da08 636f  program_args..co
-000000b0: 6c6f 726d 6170 da06 7265 7475 726e 6303  lormap..returnc.
-000000c0: 0000 0000 0000 0000 0000 000a 0000 0007  ................
-000000d0: 0000 0043 0000 0073 e000 0000 6401 7c02  ...C...s....d.|.
-000000e0: 6402 1900 9b00 6403 9d03 7c01 6404 1900  d.....d...|.d...
-000000f0: 1700 6405 1700 7d03 6406 7d04 6407 7d05  ..d...}.d.}.d.}.
-00000100: 6408 7d06 6409 7d07 7400 a001 7c02 7c01  d.}.d.}.t...|.|.
-00000110: 7c00 640a 640b a105 0100 7400 a001 7c02  |.d.d.....t...|.
-00000120: 7c01 7c00 640c 7c03 a105 0100 7c01 640d  |.|.d.|.....|.d.
-00000130: 1900 640a 6b04 7239 640e 7d08 7400 a001  ..d.k.r9d.}.t...
-00000140: 7c02 7c01 7c00 640c 7c08 a105 0100 7400  |.|.|.d.|.....t.
-00000150: a001 7c02 7c01 7c00 640c 7c04 a105 0100  ..|.|.|.d.|.....
-00000160: 7400 a001 7c02 7c01 7c00 640c 7c05 a105  t...|.|.|.d.|...
-00000170: 0100 7c01 640d 1900 640a 6b02 725c 640f  ..|.d...d.k.r\d.
-00000180: 7d09 7400 a001 7c02 7c01 7c00 640c 7c09  }.t...|.|.|.d.|.
-00000190: a105 0100 7400 a001 7c02 7c01 7c00 640c  ....t...|.|.|.d.
-000001a0: 7c06 a105 0100 7400 a001 7c02 7c01 7c00  |.....t...|.|.|.
-000001b0: 640c 7c07 a105 0100 6410 5300 2911 6130  d.|.....d.S.).a0
-000001c0: 0100 006f 7574 7075 7420 7468 6520 7072  ...output the pr
-000001d0: 6f67 7261 6d20 6361 7665 6174 730a 2020  ogram caveats.  
-000001e0: 2020 4f75 7470 7574 2074 6865 2070 726f    Output the pro
-000001f0: 6772 616d 2063 6176 6561 7473 2061 7420  gram caveats at 
-00000200: 7468 6520 7665 7279 2065 6e64 0a20 2020  the very end.   
-00000210: 2020 2020 2050 6172 616d 6574 6572 733a       Parameters:
-00000220: 206c 6973 7420 696e 746f 2077 6869 6368   list into which
-00000230: 2061 6c6c 206f 7574 7075 7420 6861 7320   all output has 
-00000240: 6265 656e 2061 6464 6564 2c20 7468 6520  been added, the 
-00000250: 7072 6f67 7261 6d20 7275 6e74 696d 6520  program runtime 
-00000260: 6172 6775 6d65 6e74 732c 0a20 2020 2020  arguments,.     
-00000270: 2020 2020 2020 2020 2020 2020 2020 2074                 t
-00000280: 6865 2064 6963 7469 6f6e 6172 7920 6f66  he dictionary of
-00000290: 2063 6f6c 6f72 7320 746f 2075 7365 0a0a   colors to use..
-000002a0: 2020 2020 2020 2020 5265 7475 726e 733a          Returns:
-000002b0: 2074 6865 2063 6f75 6e74 206f 6620 7468   the count of th
-000002c0: 6520 6e75 6d62 6572 206f 6620 7469 6d65  e number of time
-000002d0: 7320 7468 6520 7072 6f67 7261 6d20 6861  s the program ha
-000002e0: 7320 6265 656e 2063 616c 6c65 640a 0a20  s been called.. 
-000002f0: 2020 207a 133c 7370 616e 2073 7479 6c65     z.<span style
-00000300: 3d22 636f 6c6f 723a 7202 0000 007a 0222  ="color:r....z."
-00000310: 3eda 0b66 6f6e 745f 746f 5f75 7365 7a10  >..font_to_usez.
-00000320: 3c2f 666f 6e74 3e43 4156 4541 5453 3a0a  </font>CAVEATS:.
-00000330: 7a7c 2d20 5468 6973 2068 6173 206f 6e6c  z|- This has onl
-00000340: 7920 6265 656e 2074 6573 7465 6420 6f6e  y been tested on
-00000350: 206d 7920 6f77 6e20 6261 636b 7570 2e78   my own backup.x
-00000360: 6d6c 2066 696c 652e 2020 466f 7220 7072  ml file.  For pr
-00000370: 6f62 6c65 6d73 2c20 7265 706f 7274 2074  oblems, report t
-00000380: 6865 6d20 6f6e 2068 7474 7073 3a2f 2f67  hem on https://g
-00000390: 6974 6875 622e 636f 6d2f 6d63 7469 6e6b  ithub.com/mctink
-000003a0: 6572 2f4d 6170 2d54 6173 6b65 722e 7a5e  er/Map-Tasker.z^
-000003b0: 2d20 5461 736b 7320 7468 6174 2061 7265  - Tasks that are
-000003c0: 2069 6465 6e74 6966 6965 6420 6173 2022   identified as "
-000003d0: 556e 6e61 6d65 642f 416e 6f6e 796d 6f75  Unnamed/Anonymou
-000003e0: 7322 2068 6176 6520 6e6f 206e 616d 6520  s" have no name 
-000003f0: 616e 6420 6172 6520 636f 6e73 6964 6572  and are consider
-00000400: 6564 2041 6e6f 6e79 6d6f 7573 2e0a 7a7e  ed Anonymous..z~
-00000410: 2d20 5461 736b 206c 6162 656c 7320 7468  - Task labels th
-00000420: 6174 2068 6176 6520 656d 6265 6464 6564  at have embedded
-00000430: 2048 544d 4c20 2865 2e67 2e20 636f 6c6f   HTML (e.g. colo
-00000440: 723d 2e2e 2e3e 2229 2077 696c 6c20 7265  r=...>") will re
-00000450: 7375 6c74 2069 6e20 7468 6520 7265 6d61  sult in the rema
-00000460: 696e 696e 6720 6c61 6265 6c20 6469 7370  ining label disp
-00000470: 6c61 7965 6420 696e 2074 6861 7420 7361  layed in that sa
-00000480: 6d65 2063 6f6c 6f72 2f66 6f6e 742e 7a75  me color/font.zu
-00000490: 2d20 5769 7468 2074 6865 206d 6f72 6520  - With the more 
-000004a0: 7265 6365 6e74 2076 6572 7369 6f6e 7320  recent versions 
-000004b0: 6f66 2054 6173 6b65 722c 2064 6973 6162  of Tasker, disab
-000004c0: 6c65 6420 5072 6f66 696c 6573 2061 7265  led Profiles are
-000004d0: 206e 6f74 2065 6173 696c 7920 6465 7465   not easily dete
-000004e0: 6374 6564 2061 6e64 2067 6f20 756e 7265  cted and go unre
-000004f0: 636f 676e 697a 6564 2061 7320 6469 7361  cognized as disa
-00000500: 626c 6564 2e72 0100 0000 7a04 3c68 723e  bled.r....z.<hr>
-00000510: e904 0000 00da 1464 6973 706c 6179 5f64  .......display_d
-00000520: 6574 6169 6c5f 6c65 7665 6c7a 6d2d 204d  etail_levelzm- M
-00000530: 6f73 7420 6275 7420 6e6f 7420 616c 6c20  ost but not all 
-00000540: 5461 736b 2061 6374 696f 6e73 2068 6176  Task actions hav
-00000550: 6520 6265 656e 206d 6170 7065 6420 616e  e been mapped an
-00000560: 6420 7769 6c6c 2064 6973 706c 6179 2061  d will display a
-00000570: 7320 7375 6368 2e20 204c 696b 6577 6973  s such.  Likewis
-00000580: 6520 666f 7220 5072 6f66 696c 6520 636f  e for Profile co
-00000590: 6e64 6974 696f 6e73 2e0a 7a87 2d20 466f  nditions..z.- Fo
-000005a0: 7220 6f70 7469 6f6e 202d 6430 2c20 5461  r option -d0, Ta
-000005b0: 736b 7320 7468 6174 2061 7265 2069 6465  sks that are ide
-000005c0: 6e74 6966 6965 6420 6173 2022 556e 6e61  ntified as "Unna
-000005d0: 6d65 642f 416e 6f6e 796d 6f75 7322 2077  med/Anonymous" w
-000005e0: 696c 6c20 6861 7665 2074 6865 6972 2066  ill have their f
-000005f0: 6972 7374 2054 6173 6b20 6f6e 6c79 206c  irst Task only l
-00000600: 6973 7465 642e 2e2e 2e0a 2020 6a75 7374  isted.....  just
-00000610: 206c 696b 6520 5461 736b 6572 2064 6f65   like Tasker doe
-00000620: 732e 0a4e 2902 da0c 6275 696c 645f 6f75  s..N)...build_ou
-00000630: 7470 7574 da09 6d79 5f6f 7574 7075 7429  tput..my_output)
-00000640: 0a72 0300 0000 7204 0000 0072 0500 0000  .r....r....r....
-00000650: 5a07 6361 7665 6174 315a 0763 6176 6561  Z.caveat1Z.cavea
-00000660: 7433 5a07 6361 7665 6174 345a 0763 6176  t3Z.caveat4Z.cav
-00000670: 6561 7436 5a07 6361 7665 6174 375a 0763  eat6Z.caveat7Z.c
-00000680: 6176 6561 7432 5a07 6361 7665 6174 35a9  aveat2Z.caveat5.
-00000690: 0072 0c00 0000 fa76 2f55 7365 7273 2f6d  .r.....v/Users/m
-000006a0: 696b 7275 6269 6e2f 4c69 6272 6172 792f  ikrubin/Library/
-000006b0: 436c 6f75 6453 746f 7261 6765 2f47 6f6f  CloudStorage/Goo
-000006c0: 676c 6544 7269 7665 2d6d 696b 7275 6269  gleDrive-mikrubi
-000006d0: 6e40 676d 6169 6c2e 636f 6d2f 4d79 2044  n@gmail.com/My D
-000006e0: 7269 7665 2f50 7974 686f 6e2f 6d61 7074  rive/Python/mapt
-000006f0: 6173 6b65 722f 6d61 7074 6173 6b65 722f  asker/maptasker/
-00000700: 7372 632f 6361 7665 6174 732e 7079 da0f  src/caveats.py..
-00000710: 6469 7370 6c61 795f 6361 7665 6174 7312  display_caveats.
-00000720: 0000 0073 4200 0000 0e0a 0601 02ff 0202  ...sB...........
-00000730: 02fe 02ff 0206 02ff 0205 02ff 0205 02ff  ................
-00000740: 0205 02ff 1204 1201 0c01 0202 02ff 0404  ................
-00000750: 0a01 04ff 1203 1201 0c02 0203 02ff 0404  ................
-00000760: 0a01 04ff 1203 1201 0401 720e 0000 0029  ..........r....)
-00000770: 0ada 156d 6170 7461 736b 6572 2e73 7263  ...maptasker.src
-00000780: 2e6f 7574 7075 746c da03 7372 63da 076f  .outputl..src..o
-00000790: 7574 7075 746c 720a 0000 00da 146d 6170  utputlr......map
-000007a0: 7461 736b 6572 2e73 7263 2e63 6f6e 6669  tasker.src.confi
-000007b0: 6772 0200 0000 da04 6c69 7374 da03 7374  gr......list..st
-000007c0: 72da 0464 6963 7472 0e00 0000 720c 0000  r..dictr....r...
-000007d0: 0072 0c00 0000 720c 0000 0072 0d00 0000  .r....r....r....
-000007e0: da08 3c6d 6f64 756c 653e 0100 0000 7306  ..<module>....s.
-000007f0: 0000 0012 0d0c 0122 03                   .......".
+00000040: 6402 6504 6505 1900 6403 6506 6404 6506  d.e.e...d.e.d.e.
+00000050: 6405 6401 6608 6406 6407 8404 5a07 6401  d.d.f.d.d...Z.d.
+00000060: 5300 2908 e900 0000 004e da0b 6f75 7470  S.)......N..outp
+00000070: 7574 5f6c 6973 74da 0c70 726f 6772 616d  ut_list..program
+00000080: 5f61 7267 73da 0863 6f6c 6f72 6d61 70da  _args..colormap.
+00000090: 0672 6574 7572 6e63 0300 0000 0000 0000  .returnc........
+000000a0: 0000 0000 0900 0000 0700 0000 4300 0000  ............C...
+000000b0: 73c8 0000 0064 017c 0264 0219 009b 009d  s....d.|.d......
+000000c0: 027c 0164 0319 0017 0064 0417 007d 0364  .|.d.....d...}.d
+000000d0: 057d 0464 067d 0564 077d 0674 00a0 017c  .}.d.}.d.}.t...|
+000000e0: 027c 017c 0064 0864 09a1 0501 0074 00a0  .|.|.d.d.....t..
+000000f0: 017c 027c 017c 0064 0a7c 03a1 0501 007c  .|.|.|.d.|.....|
+00000100: 0164 0b19 0064 086b 0472 3664 0c7d 0774  .d...d.k.r6d.}.t
+00000110: 00a0 017c 027c 017c 0064 0a7c 07a1 0501  ...|.|.|.d.|....
+00000120: 0074 00a0 017c 027c 017c 0064 0a7c 04a1  .t...|.|.|.d.|..
+00000130: 0501 0074 00a0 017c 027c 017c 0064 0a7c  ...t...|.|.|.d.|
+00000140: 05a1 0501 007c 0164 0b19 0064 086b 0272  .....|.d...d.k.r
+00000150: 5964 0d7d 0874 00a0 017c 027c 017c 0064  Yd.}.t...|.|.|.d
+00000160: 0a7c 08a1 0501 0074 00a0 017c 027c 017c  .|.....t...|.|.|
+00000170: 0064 0a7c 06a1 0501 0064 0e53 0029 0f61  .d.|.....d.S.).a
+00000180: 3001 0000 6f75 7470 7574 2074 6865 2070  0...output the p
+00000190: 726f 6772 616d 2063 6176 6561 7473 0a20  rogram caveats. 
+000001a0: 2020 204f 7574 7075 7420 7468 6520 7072     Output the pr
+000001b0: 6f67 7261 6d20 6361 7665 6174 7320 6174  ogram caveats at
+000001c0: 2074 6865 2076 6572 7920 656e 640a 2020   the very end.  
+000001d0: 2020 2020 2020 5061 7261 6d65 7465 7273        Parameters
+000001e0: 3a20 6c69 7374 2069 6e74 6f20 7768 6963  : list into whic
+000001f0: 6820 616c 6c20 6f75 7470 7574 2068 6173  h all output has
+00000200: 2062 6565 6e20 6164 6465 642c 2074 6865   been added, the
+00000210: 2070 726f 6772 616d 2072 756e 7469 6d65   program runtime
+00000220: 2061 7267 756d 656e 7473 2c0a 2020 2020   arguments,.    
+00000230: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00000240: 7468 6520 6469 6374 696f 6e61 7279 206f  the dictionary o
+00000250: 6620 636f 6c6f 7273 2074 6f20 7573 650a  f colors to use.
+00000260: 0a20 2020 2020 2020 2052 6574 7572 6e73  .        Returns
+00000270: 3a20 7468 6520 636f 756e 7420 6f66 2074  : the count of t
+00000280: 6865 206e 756d 6265 7220 6f66 2074 696d  he number of tim
+00000290: 6573 2074 6865 2070 726f 6772 616d 2068  es the program h
+000002a0: 6173 2062 6565 6e20 6361 6c6c 6564 0a0a  as been called..
+000002b0: 2020 2020 7a13 3c73 7061 6e20 7374 796c      z.<span styl
+000002c0: 653d 2263 6f6c 6f72 3ada 1774 7261 696c  e="color:..trail
+000002d0: 696e 675f 636f 6d6d 656e 7473 5f63 6f6c  ing_comments_col
+000002e0: 6f72 da0b 666f 6e74 5f74 6f5f 7573 657a  or..font_to_usez
+000002f0: 0a3e 4341 5645 4154 533a 0a7a 7c2d 2054  .>CAVEATS:.z|- T
+00000300: 6869 7320 6861 7320 6f6e 6c79 2062 6565  his has only bee
+00000310: 6e20 7465 7374 6564 206f 6e20 6d79 206f  n tested on my o
+00000320: 776e 2062 6163 6b75 702e 786d 6c20 6669  wn backup.xml fi
+00000330: 6c65 2e20 2046 6f72 2070 726f 626c 656d  le.  For problem
+00000340: 732c 2072 6570 6f72 7420 7468 656d 206f  s, report them o
+00000350: 6e20 6874 7470 733a 2f2f 6769 7468 7562  n https://github
+00000360: 2e63 6f6d 2f6d 6374 696e 6b65 722f 4d61  .com/mctinker/Ma
+00000370: 702d 5461 736b 6572 2e7a 5e2d 2054 6173  p-Tasker.z^- Tas
+00000380: 6b73 2074 6861 7420 6172 6520 6964 656e  ks that are iden
+00000390: 7469 6669 6564 2061 7320 2255 6e6e 616d  tified as "Unnam
+000003a0: 6564 2f41 6e6f 6e79 6d6f 7573 2220 6861  ed/Anonymous" ha
+000003b0: 7665 206e 6f20 6e61 6d65 2061 6e64 2061  ve no name and a
+000003c0: 7265 2063 6f6e 7369 6465 7265 6420 416e  re considered An
+000003d0: 6f6e 796d 6f75 732e 0a7a 802d 2054 6173  onymous..z.- Tas
+000003e0: 6b65 7220 6669 656c 6473 2074 6861 7420  ker fields that 
+000003f0: 6861 7665 2065 6d62 6564 6465 6420 4854  have embedded HT
+00000400: 4d4c 2028 652e 672e 2063 6f6c 6f72 3d2e  ML (e.g. color=.
+00000410: 2e2e 3e22 2920 7769 6c6c 2072 6573 756c  ..>") will resul
+00000420: 7420 696e 2074 6865 2072 656d 6169 6e69  t in the remaini
+00000430: 6e67 206c 6162 656c 2064 6973 706c 6179  ng label display
+00000440: 6564 2069 6e20 7468 6174 2073 616d 6520  ed in that same 
+00000450: 636f 6c6f 722f 666f 6e74 2e72 0100 0000  color/font.r....
+00000460: 7a04 3c68 723e e904 0000 00da 1464 6973  z.<hr>.......dis
+00000470: 706c 6179 5f64 6574 6169 6c5f 6c65 7665  play_detail_leve
+00000480: 6c7a 812d 204d 6f73 7420 6275 7420 6e6f  lz.- Most but no
+00000490: 7420 616c 6c20 5461 736b 2061 6374 696f  t all Task actio
+000004a0: 6e73 2068 6176 6520 6265 656e 206d 6170  ns have been map
+000004b0: 7065 6420 616e 6420 7769 6c6c 2064 6973  ped and will dis
+000004c0: 706c 6179 2061 7320 7375 6368 2e20 204c  play as such.  L
+000004d0: 696b 6577 6973 6520 666f 7220 5072 6f66  ikewise for Prof
+000004e0: 696c 6520 636f 6e64 6974 696f 6e73 2061  ile conditions a
+000004f0: 6e64 2050 6c75 672d 696e 732e 0a3c 2f73  nd Plug-ins..</s
+00000500: 7061 6e3e 7a87 2d20 466f 7220 6f70 7469  pan>z.- For opti
+00000510: 6f6e 202d 6430 2c20 5461 736b 7320 7468  on -d0, Tasks th
+00000520: 6174 2061 7265 2069 6465 6e74 6966 6965  at are identifie
+00000530: 6420 6173 2022 556e 6e61 6d65 642f 416e  d as "Unnamed/An
+00000540: 6f6e 796d 6f75 7322 2077 696c 6c20 6861  onymous" will ha
+00000550: 7665 2074 6865 6972 2066 6972 7374 2054  ve their first T
+00000560: 6173 6b20 6f6e 6c79 206c 6973 7465 642e  ask only listed.
+00000570: 2e2e 2e0a 2020 6a75 7374 206c 696b 6520  ....  just like 
+00000580: 5461 736b 6572 2064 6f65 732e 0a4e 2902  Tasker does..N).
+00000590: da0c 6275 696c 645f 6f75 7470 7574 da09  ..build_output..
+000005a0: 6d79 5f6f 7574 7075 7429 0972 0200 0000  my_output).r....
+000005b0: 7203 0000 0072 0400 0000 5a07 6361 7665  r....r....Z.cave
+000005c0: 6174 315a 0763 6176 6561 7433 5a07 6361  at1Z.caveat3Z.ca
+000005d0: 7665 6174 345a 0763 6176 6561 7436 5a07  veat4Z.caveat6Z.
+000005e0: 6361 7665 6174 325a 0763 6176 6561 7435  caveat2Z.caveat5
+000005f0: a900 720c 0000 00fa 762f 5573 6572 732f  ..r.....v/Users/
+00000600: 6d69 6b72 7562 696e 2f4c 6962 7261 7279  mikrubin/Library
+00000610: 2f43 6c6f 7564 5374 6f72 6167 652f 476f  /CloudStorage/Go
+00000620: 6f67 6c65 4472 6976 652d 6d69 6b72 7562  ogleDrive-mikrub
+00000630: 696e 4067 6d61 696c 2e63 6f6d 2f4d 7920  in@gmail.com/My 
+00000640: 4472 6976 652f 5079 7468 6f6e 2f6d 6170  Drive/Python/map
+00000650: 7461 736b 6572 2f6d 6170 7461 736b 6572  tasker/maptasker
+00000660: 2f73 7263 2f63 6176 6561 7473 2e70 79da  /src/caveats.py.
+00000670: 0f64 6973 706c 6179 5f63 6176 6561 7473  .display_caveats
+00000680: 1100 0000 733c 0000 000c 0a06 0102 ff02  ....s<..........
+00000690: 0202 fe02 ff02 0602 ff02 0502 ff02 0502  ................
+000006a0: ff12 0412 010c 0102 0202 ff04 040a 0104  ................
+000006b0: ff12 0312 010c 0202 0302 ff04 040a 0104  ................
+000006c0: ff12 0304 0172 0e00 0000 2908 da15 6d61  .....r....)...ma
+000006d0: 7074 6173 6b65 722e 7372 632e 6f75 7470  ptasker.src.outp
+000006e0: 7574 6cda 0373 7263 da07 6f75 7470 7574  utl..src..output
+000006f0: 6c72 0a00 0000 da04 6c69 7374 da03 7374  lr......list..st
+00000700: 72da 0464 6963 7472 0e00 0000 720c 0000  r..dictr....r...
+00000710: 0072 0c00 0000 720c 0000 0072 0d00 0000  .r....r....r....
+00000720: da08 3c6d 6f64 756c 653e 0100 0000 7304  ..<module>....s.
+00000730: 0000 0012 0d22 03                        .....".
```

### Comparing `maptasker-1.3.1/maptasker/src/__pycache__/colors.cpython-310.pyc` & `maptasker-1.3.2/maptasker/src/__pycache__/colors.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 17 16:37:08 2023 UTC, .py size: 8220 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 4% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 3497 1464 1c20 0000  o.......4..d. ..
+00000000: 6f0d 0d0a 0000 0000 918f 1c64 1c20 0000  o..........d. ..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0008 0000 0040 0000 0073 5600 0000 6400  .....@...sV...d.
 00000030: 6401 6c00 5a00 6400 6402 6c01 6d02 5a02  d.l.Z.d.d.l.m.Z.
 00000040: 0100 6400 6403 6c01 6d03 5a03 0100 6404  ..d.d.l.m.Z...d.
 00000050: 6405 8400 5a04 6406 6407 8400 5a05 6408  d...Z.d.d...Z.d.
 00000060: 6409 8400 5a06 640a 6507 640b 6507 640c  d...Z.d.e.d.e.d.
 00000070: 6508 640d 6401 6608 640e 640f 8404 5a09  e.d.d.f.d.d...Z.
@@ -53,93 +53,93 @@
 00000340: 0074 0364 167c 0783 0201 0074 0364 177c  .t.d.|.....t.d.|
 00000350: 0883 0201 0074 0364 187c 0983 0201 0074  .....t.d.|.....t
 00000360: 0364 197c 0a83 0201 0074 0364 1a7c 0b83  .d.|.....t.d.|..
 00000370: 0201 0074 0464 1b83 0101 0064 0053 0029  ...t.d.....d.S.)
 00000380: 1c4e 2909 5a09 496e 6469 616e 5265 645a  .N).Z.IndianRedZ
 00000390: 0a4c 6967 6874 436f 7261 6c5a 0653 616c  .LightCoralZ.Sal
 000003a0: 6d6f 6e5a 0a44 6172 6b53 616c 6d6f 6eda  monZ.DarkSalmon.
-000003b0: 0b4c 6967 6874 5361 6c6d 6f6e da07 4372  .LightSalmon..Cr
-000003c0: 696d 736f 6eda 0352 6564 5a09 4669 7265  imson..RedZ.Fire
+000003b0: 0b4c 6967 6874 5361 6c6d 6f6e 5a07 4372  .LightSalmonZ.Cr
+000003c0: 696d 736f 6e5a 0352 6564 5a09 4669 7265  imsonZ.RedZ.Fire
 000003d0: 4272 6963 6b5a 0744 6172 6b52 6564 2906  BrickZ.DarkRed).
-000003e0: 5a04 5069 6e6b da09 4c69 6768 7450 696e  Z.Pink..LightPin
+000003e0: 5a04 5069 6e6b 5a09 4c69 6768 7450 696e  Z.PinkZ.LightPin
 000003f0: 6b5a 0748 6f74 5069 6e6b 5a08 4465 6570  kZ.HotPinkZ.Deep
 00000400: 5069 6e6b 5a0f 4d65 6469 756d 5669 6f6c  PinkZ.MediumViol
 00000410: 6574 5265 645a 0d50 616c 6556 696f 6c65  etRedZ.PaleViole
 00000420: 7452 6564 2906 720e 0000 005a 0543 6f72  tRed).r....Z.Cor
 00000430: 616c 5a06 546f 6d61 746f 5a09 4f72 616e  alZ.TomatoZ.Oran
-00000440: 6765 5265 64da 0a44 6172 6b4f 7261 6e67  geRed..DarkOrang
+00000440: 6765 5265 645a 0a44 6172 6b4f 7261 6e67  geRedZ.DarkOrang
 00000450: 655a 064f 7261 6e67 6529 0b5a 0447 6f6c  eZ.Orange).Z.Gol
-00000460: 64da 0659 656c 6c6f 775a 0b4c 6967 6874  d..YellowZ.Light
+00000460: 645a 0659 656c 6c6f 775a 0b4c 6967 6874  dZ.YellowZ.Light
 00000470: 5965 6c6c 6f77 5a0c 4c65 6d6f 6e43 6869  YellowZ.LemonChi
 00000480: 6666 6f6e 5a14 4c69 6768 7447 6f6c 6465  ffonZ.LightGolde
-00000490: 6e72 6f64 5965 6c6c 6f77 da0a 5061 7061  nrodYellow..Papa
+00000490: 6e72 6f64 5965 6c6c 6f77 5a0a 5061 7061  nrodYellowZ.Papa
 000004a0: 7961 5768 6970 5a08 4d6f 6363 6173 696e  yaWhipZ.Moccasin
-000004b0: da09 5065 6163 6850 7566 66da 0d50 616c  ..PeachPuff..Pal
+000004b0: 5a09 5065 6163 6850 7566 665a 0d50 616c  Z.PeachPuffZ.Pal
 000004c0: 6547 6f6c 6465 6e72 6f64 5a05 4b68 616b  eGoldenrodZ.Khak
 000004d0: 695a 0944 6172 6b4b 6861 6b69 2913 5a08  iZ.DarkKhaki).Z.
 000004e0: 4c61 7665 6e64 6572 5a07 5468 6973 746c  LavenderZ.Thistl
 000004f0: 655a 0450 6c75 6d5a 0656 696f 6c65 745a  eZ.PlumZ.VioletZ
 00000500: 064f 7263 6869 645a 0746 7563 6873 6961  .OrchidZ.Fuchsia
-00000510: da07 4d61 6765 6e74 615a 0c4d 6564 6975  ..MagentaZ.Mediu
+00000510: 5a07 4d61 6765 6e74 615a 0c4d 6564 6975  Z.MagentaZ.Mediu
 00000520: 6d4f 7263 6869 645a 0c4d 6564 6975 6d50  mOrchidZ.MediumP
 00000530: 7572 706c 655a 0d52 6562 6563 6361 5075  urpleZ.RebeccaPu
 00000540: 7270 6c65 5a0a 426c 7565 5669 6f6c 6574  rpleZ.BlueViolet
 00000550: 5a0a 4461 726b 5669 6f6c 6574 5a0a 4461  Z.DarkVioletZ.Da
 00000560: 726b 4f72 6368 6964 5a0b 4461 726b 4d61  rkOrchidZ.DarkMa
 00000570: 6765 6e74 615a 0650 7572 706c 655a 0649  gentaZ.PurpleZ.I
 00000580: 6e64 6967 6f5a 0953 6c61 7465 426c 7565  ndigoZ.SlateBlue
 00000590: 5a0d 4461 726b 536c 6174 6542 6c75 65da  Z.DarkSlateBlue.
 000005a0: 0f4d 6564 6975 6d53 6c61 7465 426c 7565  .MediumSlateBlue
-000005b0: 2917 5a0b 4772 6565 6e59 656c 6c6f 77da  ).Z.GreenYellow.
+000005b0: 2917 5a0b 4772 6565 6e59 656c 6c6f 775a  ).Z.GreenYellowZ
 000005c0: 0a43 6861 7274 7265 7573 655a 094c 6177  .ChartreuseZ.Law
-000005d0: 6e47 7265 656e da04 4c69 6d65 5a09 4c69  nGreen..LimeZ.Li
+000005d0: 6e47 7265 656e 5a04 4c69 6d65 5a09 4c69  nGreenZ.LimeZ.Li
 000005e0: 6d65 4772 6565 6e5a 0950 616c 6547 7265  meGreenZ.PaleGre
 000005f0: 656e 5a0a 4c69 6768 7447 7265 656e 5a11  enZ.LightGreenZ.
 00000600: 4d65 6469 756d 5370 7269 6e67 4772 6565  MediumSpringGree
 00000610: 6e5a 0b53 7072 696e 6747 7265 656e 5a0e  nZ.SpringGreenZ.
 00000620: 4d65 6469 756d 5365 6147 7265 656e 5a08  MediumSeaGreenZ.
 00000630: 5365 6147 7265 656e 5a0b 466f 7265 7374  SeaGreenZ.Forest
 00000640: 4772 6565 6e5a 0547 7265 656e 5a09 4461  GreenZ.GreenZ.Da
 00000650: 726b 4772 6565 6e5a 0b59 656c 6c6f 7747  rkGreenZ.YellowG
 00000660: 7265 656e 5a09 4f6c 6976 6544 7261 625a  reenZ.OliveDrabZ
 00000670: 054f 6c69 7665 5a0e 4461 726b 4f6c 6976  .OliveZ.DarkOliv
 00000680: 6547 7265 656e 5a10 4d65 6469 756d 4171  eGreenZ.MediumAq
 00000690: 7561 6d61 7269 6e65 5a0c 4461 726b 5365  uamarineZ.DarkSe
 000006a0: 6147 7265 656e 5a0d 4c69 6768 7453 6561  aGreenZ.LightSea
 000006b0: 4772 6565 6e5a 0844 6172 6b43 7961 6e5a  GreenZ.DarkCyanZ
-000006c0: 0454 6561 6c29 19da 0441 7175 615a 0443  .Teal)...AquaZ.C
+000006c0: 0454 6561 6c29 195a 0441 7175 615a 0443  .Teal).Z.AquaZ.C
 000006d0: 7961 6e5a 094c 6967 6874 4379 616e 5a0d  yanZ.LightCyanZ.
 000006e0: 5061 6c65 5475 7271 756f 6973 655a 0a41  PaleTurquoiseZ.A
-000006f0: 7175 616d 6172 696e 65da 0954 7572 7175  quamarine..Turqu
+000006f0: 7175 616d 6172 696e 655a 0954 7572 7175  quamarineZ.Turqu
 00000700: 6f69 7365 5a0f 4d65 6469 756d 5475 7271  oiseZ.MediumTurq
 00000710: 756f 6973 655a 0d44 6172 6b54 7572 7175  uoiseZ.DarkTurqu
 00000720: 6f69 7365 5a09 4361 6465 7442 6c75 655a  oiseZ.CadetBlueZ
 00000730: 0953 7465 656c 426c 7565 5a0e 4c69 6768  .SteelBlueZ.Ligh
 00000740: 7453 7465 656c 426c 7565 5a0a 506f 7764  tSteelBlueZ.Powd
 00000750: 6572 426c 7565 5a09 4c69 6768 7442 6c75  erBlueZ.LightBlu
 00000760: 655a 0753 6b79 426c 7565 5a0c 4c69 6768  eZ.SkyBlueZ.Ligh
 00000770: 7453 6b79 426c 7565 5a0b 4465 6570 536b  tSkyBlueZ.DeepSk
 00000780: 7942 6c75 655a 0a44 6f64 6765 7242 6c75  yBlueZ.DodgerBlu
 00000790: 655a 0e43 6f72 6e66 6c6f 7765 7242 6c75  eZ.CornflowerBlu
-000007a0: 6572 1800 0000 5a09 526f 7961 6c42 6c75  er....Z.RoyalBlu
+000007a0: 6572 0f00 0000 5a09 526f 7961 6c42 6c75  er....Z.RoyalBlu
 000007b0: 655a 0442 6c75 655a 0a4d 6564 6975 6d42  eZ.BlueZ.MediumB
-000007c0: 6c75 65da 0844 6172 6b42 6c75 655a 044e  lue..DarkBlueZ.N
+000007c0: 6c75 655a 0844 6172 6b42 6c75 655a 044e  lueZ.DarkBlueZ.N
 000007d0: 6176 795a 0c4d 6964 6e69 6768 7442 6c75  avyZ.MidnightBlu
 000007e0: 6529 115a 0843 6f72 6e73 696c 6b5a 0e42  e).Z.CornsilkZ.B
 000007f0: 6c61 6e63 6865 6441 6c6d 6f6e 645a 0642  lanchedAlmondZ.B
 00000800: 6973 7175 655a 0b4e 6176 616a 6f57 6869  isqueZ.NavajoWhi
 00000810: 7465 5a05 5768 6561 745a 0942 7572 6c79  teZ.WheatZ.Burly
 00000820: 576f 6f64 5a03 5461 6e5a 0952 6f73 7942  WoodZ.TanZ.RosyB
 00000830: 726f 776e 5a0a 5361 6e64 7942 726f 776e  rownZ.SandyBrown
 00000840: 5a09 476f 6c64 656e 726f 645a 0d44 6172  Z.GoldenrodZ.Dar
 00000850: 6b47 6f6c 6465 6e72 6f64 5a04 5065 7275  kGoldenrodZ.Peru
 00000860: 5a09 4368 6f63 6f6c 6174 655a 0b53 6164  Z.ChocolateZ.Sad
 00000870: 646c 6542 726f 776e 5a06 5369 656e 6e61  dleBrownZ.Sienna
 00000880: 5a05 4272 6f77 6e5a 064d 6172 6f6f 6e29  Z.BrownZ.Maroon)
-00000890: 11da 0557 6869 7465 5a04 536e 6f77 5a08  ...WhiteZ.SnowZ.
+00000890: 115a 0557 6869 7465 5a04 536e 6f77 5a08  .Z.WhiteZ.SnowZ.
 000008a0: 486f 6e65 7944 6577 5a09 4d69 6e74 4372  HoneyDewZ.MintCr
 000008b0: 6561 6d5a 0541 7a75 7265 5a09 416c 6963  eamZ.AzureZ.Alic
 000008c0: 6542 6c75 655a 0a47 686f 7374 5768 6974  eBlueZ.GhostWhit
 000008d0: 655a 0a57 6869 7465 536d 6f6b 655a 0853  eZ.WhiteSmokeZ.S
 000008e0: 6561 5368 656c 6c5a 0542 6569 6765 5a07  eaShellZ.BeigeZ.
 000008f0: 4f6c 644c 6163 655a 0b46 6c6f 7261 6c57  OldLaceZ.FloralW
 00000900: 6869 7465 5a05 4976 6f72 795a 0c41 6e74  hiteZ.IvoryZ.Ant
@@ -199,15 +199,15 @@
 00000c60: 7465 5f63 6f6c 6f72 2700 0000 7364 0000  te_color'...sd..
 00000c70: 0008 0108 0b08 0808 0808 0d08 1508 1908  ................
 00000c80: 1b08 1308 1306 0c02 0302 0102 ff02 0202  ................
 00000c90: fe02 0302 fd02 0402 fc02 0502 fb02 0602  ................
 00000ca0: fa02 0702 f902 0802 f802 0902 f702 0a02  ................
 00000cb0: f602 ff08 0e0e 0112 0204 0108 020a 010a  ................
 00000cc0: 010a 010a 010a 010a 010a 010a 010a 010a  ................
-00000cd0: 010a 010c 0172 2800 0000 6302 0000 0000  .....r(...c.....
+00000cd0: 010a 010c 0172 1900 0000 6302 0000 0000  .....r....c.....
 00000ce0: 0000 0000 0000 0006 0000 0005 0000 0043  ...............C
 00000cf0: 0000 0073 a800 0000 7c00 6401 6400 8502  ...s....|.d.d...
 00000d00: 1900 a000 6402 a101 7d02 7c02 6403 1900  ....d...}.|.d...
 00000d10: 7d03 7401 7c02 8301 6401 6b00 721c 7402  }.t.|...d.k.r.t.
 00000d20: 7c00 9b00 6404 9d02 6405 6406 8303 0100  |...d...d.d.....
 00000d30: 7c03 7403 7601 7229 7402 7c03 9b00 6407  |.t.v.r)t.|...d.
 00000d40: 9d02 6405 6406 8303 0100 7c02 6408 1900  ..d.d.....|.d...
@@ -227,27 +227,27 @@
 00000e20: 6c70 2028 2d68 2921 7205 0000 007a 0f20  lp (-h)!r....z. 
 00000e30: 6465 7369 7265 645f 636f 6c6f 723a 7a19  desired_color:z.
 00000e40: 496e 7661 6c69 6420 636f 6c6f 7220 7370  Invalid color sp
 00000e50: 6563 6966 6965 643a 207a 0720 666f 7220  ecified: z. for 
 00000e60: 2763 7a02 2721 7a0c 2065 7869 7420 636f  'cz.'!z. exit co
 00000e70: 6465 2037 2907 da05 7370 6c69 7472 0600  de 7)...splitr..
 00000e80: 0000 da0c 6861 6e64 6c65 5f65 7272 6f72  ....handle_error
-00000e90: 7202 0000 0072 0300 0000 7225 0000 0072  r....r....r%...r
-00000ea0: 2800 0000 2906 da07 7468 655f 6172 67da  (...)...the_arg.
+00000e90: 7202 0000 0072 0300 0000 7216 0000 0072  r....r....r....r
+00000ea0: 1900 0000 2906 da07 7468 655f 6172 67da  ....)...the_arg.
 00000eb0: 0863 6f6c 6f72 6d61 705a 1074 6865 5f63  .colormapZ.the_c
 00000ec0: 6f6c 6f72 5f6f 7074 696f 6e5a 0a63 6f6c  olor_optionZ.col
 00000ed0: 6f72 5f74 7970 655a 0d64 6573 6972 6564  or_typeZ.desired
 00000ee0: 5f63 6f6c 6f72 da09 6572 726f 725f 6d73  _color..error_ms
 00000ef0: 6772 0b00 0000 720b 0000 0072 0c00 0000  gr....r....r....
 00000f00: da15 6765 745f 616e 645f 7365 745f 7468  ..get_and_set_th
 00000f10: 655f 636f 6c6f 72f3 0000 0073 2a00 0000  e_color....s*...
 00000f20: 1201 0801 0c01 0201 0c01 04ff 0803 0201  ................
 00000f30: 0801 0201 0201 04fd 0805 1001 0801 0c02  ................
-00000f40: 0406 14fd 02ff 0c03 0401 7231 0000 0072  ..........r1...r
-00000f50: 3000 0000 da04 6172 6731 da04 6172 6732  0.....arg1..arg2
+00000f40: 0406 14fd 02ff 0c03 0401 7222 0000 0072  ..........r"...r
+00000f50: 2100 0000 da04 6172 6731 da04 6172 6732  !.....arg1..arg2
 00000f60: da06 7265 7475 726e 6303 0000 0000 0000  ..returnc.......
 00000f70: 0000 0000 0003 0000 0004 0000 0043 0000  .............C..
 00000f80: 0073 2600 0000 7400 a001 7c00 9b00 7c01  .s&...t...|...|.
 00000f90: 9b00 9d02 a101 0100 7402 7c00 8301 0100  ........t.|.....
 00000fa0: 7403 7c02 8301 0100 6401 5300 2902 7ab2  t.|.....d.S.).z.
 00000fb0: 0a20 2020 204c 6f67 2061 6e64 2070 7269  .    Log and pri
 00000fc0: 6e74 2065 7272 6f72 206d 6573 7361 6765  nt error message
@@ -256,20 +256,20 @@
 00000ff0: 6572 726f 725f 6d73 673a 206d 6573 7361  error_msg: messa
 00001000: 6765 2074 6f20 6f75 7470 7574 0a20 2020  ge to output.   
 00001010: 2020 2020 203a 7061 7261 6d20 6172 6731       :param arg1
 00001020: 3a20 6578 6974 2063 6f64 6520 7465 7874  : exit code text
 00001030: 0a20 2020 2020 2020 203a 7061 7261 6d20  .        :param 
 00001040: 6172 6732 3a20 6578 6974 2063 6f64 6520  arg2: exit code 
 00001050: 6e75 6d62 6572 2061 7320 696e 740a 2020  number as int.  
-00001060: 2020 4e29 0472 0300 0000 7225 0000 0072    N).r....r%...r
-00001070: 0700 0000 7227 0000 0029 0372 3000 0000  ....r'...).r0...
-00001080: 7232 0000 0072 3300 0000 720b 0000 0072  r2...r3...r....r
-00001090: 0b00 0000 720c 0000 0072 2d00 0000 0d01  ....r....r-.....
-000010a0: 0000 7306 0000 0012 0708 010c 0172 2d00  ..s..........r-.
-000010b0: 0000 290a 7220 0000 00da 166d 6170 7461  ..).r .....mapta
+00001060: 2020 4e29 0472 0300 0000 7216 0000 0072    N).r....r....r
+00001070: 0700 0000 7218 0000 0029 0372 2100 0000  ....r....).r!...
+00001080: 7223 0000 0072 2400 0000 720b 0000 0072  r#...r$...r....r
+00001090: 0b00 0000 720c 0000 0072 1e00 0000 0d01  ....r....r......
+000010a0: 0000 7306 0000 0012 0708 010c 0172 1e00  ..s..........r..
+000010b0: 0000 290a 7211 0000 00da 166d 6170 7461  ..).r......mapta
 000010c0: 736b 6572 2e73 7263 2e73 7973 636f 6e73  sker.src.syscons
 000010d0: 7472 0200 0000 7203 0000 0072 0d00 0000  tr....r....r....
-000010e0: 7228 0000 0072 3100 0000 da03 7374 72da  r(...r1.....str.
-000010f0: 0369 6e74 722d 0000 0072 0b00 0000 720b  .intr-...r....r.
+000010e0: 7219 0000 0072 2200 0000 da03 7374 72da  r....r".....str.
+000010f0: 0369 6e74 721e 0000 0072 0b00 0000 720b  .intr....r....r.
 00001100: 0000 0072 0b00 0000 720c 0000 00da 083c  ...r....r......<
 00001110: 6d6f 6475 6c65 3e01 0000 0073 1000 0000  module>....s....
 00001120: 080d 0c01 0c01 0806 0811 007f 084d 1e1a  .............M..
```

### Comparing `maptasker-1.3.1/maptasker/src/__pycache__/colrmode.cpython-310.pyc` & `maptasker-1.3.2/maptasker/src/__pycache__/colrmode.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Thu Mar 16 14:47:52 2023 UTC, .py size: 3285 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 6% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 182c 1364 d50c 0000  o........,.d....
+00000000: 6f0d 0d0a 0000 0000 3b04 2764 d50c 0000  o.......;.'d....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 2200 0000 6400  .....@...s"...d.
 00000030: 6401 6c00 5a00 6402 6501 6403 6502 6404  d.l.Z.d.e.d.e.d.
 00000040: 6502 6606 6405 6406 8404 5a03 6401 5300  e.f.d.d...Z.d.S.
 00000050: 2907 e900 0000 004e da0f 6170 7065 6172  )......N..appear
 00000060: 616e 6365 5f6d 6f64 65da 0863 6f6c 6f72  ance_mode..color
 00000070: 6d61 70da 0672 6574 7572 6e63 0200 0000  map..returnc....
@@ -18,92 +18,91 @@
 00000110: 1c64 1d93 0164 1e64 1f93 0164 2064 2193  .d...d.d...d d!.
 00000120: 0164 2264 2393 0164 2464 2169 01a5 017d  .d"d#..d$d!i...}
 00000130: 017c 0153 0069 0064 0464 2593 0164 0664  .|.S.i.d.d%..d.d
 00000140: 1f93 0164 0864 2693 0164 0a64 2793 0164  ...d.d&..d.d'..d
 00000150: 0c64 2893 0164 0e64 2993 0164 0f64 2a93  .d(..d.d)..d.d*.
 00000160: 0164 1164 2593 0164 1464 2b93 0164 1264  .d.d%..d.d+..d.d
 00000170: 2c93 0164 1664 2d93 0164 1864 2e93 0164  ,..d.d-..d.d...d
-00000180: 1a64 2f93 0164 1c64 2b93 0164 1e64 3093  .d/..d.d+..d.d0.
-00000190: 0164 2064 3193 0164 2264 3293 0164 2464  .d d1..d"d2..d$d
-000001a0: 3369 01a5 017d 017c 0153 0029 347a db0a  3i...}.|.S.)4z..
+00000180: 1a64 2f93 0164 1c64 2b93 0164 1e64 1d93  .d/..d.d+..d.d..
+00000190: 0164 2064 3093 0164 2264 3193 0164 2464  .d d0..d"d1..d$d
+000001a0: 3269 01a5 017d 017c 0153 0029 337a db0a  2i...}.|.S.)3z..
 000001b0: 2020 2020 4769 7665 6e20 7468 6520 636f      Given the co
 000001c0: 6c6f 7220 6d6f 6465 2074 6f20 7573 6520  lor mode to use 
 000001d0: 2844 6172 6b20 6f72 204c 6967 6874 292c  (Dark or Light),
 000001e0: 2073 6574 2074 6865 2063 6f6c 6f72 7320   set the colors 
 000001f0: 6170 7072 6f70 7269 6174 656c 790a 2020  appropriately.  
 00000200: 2020 2020 2022 3a70 6172 616d 2061 7070       ":param app
 00000210: 6561 7261 6e63 655f 6d6f 6465 3a20 636f  earance_mode: co
 00000220: 6c6f 7220 6d6f 6465 3a20 4461 726b 206f  lor mode: Dark o
 00000230: 7220 4c69 6768 740a 2020 2020 2020 2022  r Light.       "
 00000240: 3a70 6172 616d 2063 6f6c 6f72 6d61 703a  :param colormap:
 00000250: 2063 6f6c 6f72 7320 746f 2075 7365 2069   colors to use i
 00000260: 6e20 6f75 7470 7574 0a20 2020 2020 2020  n output.       
 00000270: 223a 7265 7475 726e 206e 6577 2063 6f6c  ":return new col
 00000280: 6f72 6d61 700a 2020 2020 5a06 5379 7374  ormap.    Z.Syst
-00000290: 656d 5a04 4461 726b 5a05 4c69 6768 74da  emZ.DarkZ.Light.
+00000290: 656d da04 4461 726b da05 4c69 6768 74da  em..Dark..Light.
 000002a0: 0d70 726f 6a65 6374 5f63 6f6c 6f72 da05  .project_color..
 000002b0: 5768 6974 65da 0d70 726f 6669 6c65 5f63  White..profile_c
 000002c0: 6f6c 6f72 da04 4171 7561 da16 6469 7361  olor..Aqua..disa
 000002d0: 626c 6564 5f70 726f 6669 6c65 5f63 6f6c  bled_profile_col
 000002e0: 6f72 da03 5265 64da 136c 6175 6e63 6865  or..Red..launche
-000002f0: 725f 7461 736b 5f63 6f6c 6f72 da0a 4368  r_task_color..Ch
-00000300: 6172 7472 6575 7365 da0a 7461 736b 5f63  artreuse..task_c
-00000310: 6f6c 6f72 da06 5965 6c6c 6f77 da12 756e  olor..Yellow..un
-00000320: 6b6e 6f77 6e5f 7461 736b 5f63 6f6c 6f72  known_task_color
-00000330: da0b 7363 656e 655f 636f 6c6f 72da 044c  ..scene_color..L
-00000340: 696d 65da 0c62 756c 6c65 745f 636f 6c6f  ime..bullet_colo
-00000350: 72da 1161 6374 696f 6e5f 6e61 6d65 5f63  r..action_name_c
-00000360: 6f6c 6f72 da0d 5061 6c65 476f 6c64 656e  olor..PaleGolden
-00000370: 726f 64da 0c61 6374 696f 6e5f 636f 6c6f  rod..action_colo
-00000380: 72da 0a44 6172 6b4f 7261 6e67 65da 1261  r..DarkOrange..a
-00000390: 6374 696f 6e5f 6c61 6265 6c5f 636f 6c6f  ction_label_colo
-000003a0: 72da 074d 6167 656e 7461 da16 6163 7469  r..Magenta..acti
-000003b0: 6f6e 5f63 6f6e 6469 7469 6f6e 5f63 6f6c  on_condition_col
-000003c0: 6f72 da0a 5061 7061 7961 5768 6970 da15  or..PapayaWhip..
-000003d0: 6469 7361 626c 6564 5f61 6374 696f 6e5f  disabled_action_
-000003e0: 636f 6c6f 72da 0743 7269 6d73 6f6e da17  color..Crimson..
-000003f0: 7072 6f66 696c 655f 636f 6e64 6974 696f  profile_conditio
-00000400: 6e5f 636f 6c6f 72da 0954 7572 7175 6f69  n_color..Turquoi
-00000410: 7365 da10 6261 636b 6772 6f75 6e64 5f63  se..background_c
+000002f0: 725f 7461 736b 5f63 6f6c 6f72 da0b 4772  r_task_color..Gr
+00000300: 6565 6e59 656c 6c6f 77da 0a74 6173 6b5f  eenYellow..task_
+00000310: 636f 6c6f 72da 0659 656c 6c6f 77da 1275  color..Yellow..u
+00000320: 6e6b 6e6f 776e 5f74 6173 6b5f 636f 6c6f  nknown_task_colo
+00000330: 72da 0b73 6365 6e65 5f63 6f6c 6f72 da04  r..scene_color..
+00000340: 4c69 6d65 da0c 6275 6c6c 6574 5f63 6f6c  Lime..bullet_col
+00000350: 6f72 da11 6163 7469 6f6e 5f6e 616d 655f  or..action_name_
+00000360: 636f 6c6f 72da 0d50 616c 6547 6f6c 6465  color..PaleGolde
+00000370: 6e72 6f64 da0c 6163 7469 6f6e 5f63 6f6c  nrod..action_col
+00000380: 6f72 da0a 4461 726b 4f72 616e 6765 da12  or..DarkOrange..
+00000390: 6163 7469 6f6e 5f6c 6162 656c 5f63 6f6c  action_label_col
+000003a0: 6f72 da07 4d61 6765 6e74 61da 1661 6374  or..Magenta..act
+000003b0: 696f 6e5f 636f 6e64 6974 696f 6e5f 636f  ion_condition_co
+000003c0: 6c6f 72da 0a50 6170 6179 6157 6869 70da  lor..PapayaWhip.
+000003d0: 1564 6973 6162 6c65 645f 6163 7469 6f6e  .disabled_action
+000003e0: 5f63 6f6c 6f72 da07 4372 696d 736f 6eda  _color..Crimson.
+000003f0: 1770 726f 6669 6c65 5f63 6f6e 6469 7469  .profile_conditi
+00000400: 6f6e 5f63 6f6c 6f72 da08 4c61 7665 6e64  on_color..Lavend
+00000410: 6572 da10 6261 636b 6772 6f75 6e64 5f63  er..background_c
 00000420: 6f6c 6f72 da08 4461 726b 426c 7565 da17  olor..DarkBlue..
 00000430: 7472 6169 6c69 6e67 5f63 6f6d 6d65 6e74  trailing_comment
 00000440: 735f 636f 6c6f 72da 0950 6561 6368 5075  s_color..PeachPu
 00000450: 6666 da0f 7461 736b 6572 6e65 745f 636f  ff..taskernet_co
 00000460: 6c6f 72da 094c 6967 6874 5069 6e6b da11  lor..LightPink..
 00000470: 7072 6566 6572 656e 6365 735f 636f 6c6f  preferences_colo
 00000480: 72da 0542 6c61 636b da07 4461 726b 5265  r..Black..DarkRe
 00000490: 64da 094c 6177 6e47 7265 656e da09 4461  d..LawnGreen..Da
 000004a0: 726b 4772 6565 6eda 0f4d 6564 6975 6d56  rkGreen..MediumV
 000004b0: 696f 6c65 7452 6564 da06 5075 7270 6c65  ioletRed..Purple
 000004c0: da0d 4461 726b 536c 6174 6547 7261 79da  ..DarkSlateGray.
 000004d0: 0649 6e64 6967 6fda 0c4d 6564 6975 6d4f  .Indigo..MediumO
 000004e0: 7263 6869 64da 0542 726f 776e da09 496e  rchid..Brown..In
-000004f0: 6469 616e 5265 64da 084c 6176 656e 6465  dianRed..Lavende
-00000500: 72da 0654 6f6d 6174 6fda 0952 6f79 616c  r..Tomato..Royal
-00000510: 426c 7565 da0a 446f 6467 6572 426c 7565  Blue..DodgerBlue
-00000520: 2902 da0a 6461 726b 6465 7465 6374 5a06  )...darkdetectZ.
-00000530: 6973 4461 726b 2903 7202 0000 0072 0300  isDark).r....r..
-00000540: 0000 da04 6d6f 6465 a900 7237 0000 00fa  ....mode..r7....
-00000550: 772f 5573 6572 732f 6d69 6b72 7562 696e  w/Users/mikrubin
-00000560: 2f4c 6962 7261 7279 2f43 6c6f 7564 5374  /Library/CloudSt
-00000570: 6f72 6167 652f 476f 6f67 6c65 4472 6976  orage/GoogleDriv
-00000580: 652d 6d69 6b72 7562 696e 4067 6d61 696c  e-mikrubin@gmail
-00000590: 2e63 6f6d 2f4d 7920 4472 6976 652f 5079  .com/My Drive/Py
-000005a0: 7468 6f6e 2f6d 6170 7461 736b 6572 2f6d  thon/maptasker/m
-000005b0: 6170 7461 736b 6572 2f73 7263 2f63 6f6c  aptasker/src/col
-000005c0: 726d 6f64 652e 7079 da0e 7365 745f 636f  rmode.py..set_co
-000005d0: 6c6f 725f 6d6f 6465 1100 0000 73a0 0000  lor_mode....s...
-000005e0: 0008 0912 0104 0208 0202 0104 0102 ff04  ................
-000005f0: 0202 fe04 0302 fd04 0402 fc04 0502 fb04  ................
-00000600: 0602 fa04 0702 f904 0802 f804 0902 f704  ................
-00000610: 0a02 f604 0b02 f504 0c02 f404 0d02 f304  ................
-00000620: 0e02 f204 0f02 f104 1002 f004 1102 ef04  ................
-00000630: 1206 ee04 2a02 eb04 0102 ff04 0202 fe04  ....*...........
-00000640: 0302 fd04 0402 fc04 0502 fb04 0602 fa04  ................
-00000650: 0702 f904 0802 f804 0902 f704 0a02 f604  ................
-00000660: 0b02 f504 0c02 f404 0d02 f304 0e02 f204  ................
-00000670: 0f02 f104 1002 f004 1102 ef04 1206 ee04  ................
-00000680: 1572 3900 0000 2904 7235 0000 00da 0373  .r9...).r5.....s
-00000690: 7472 da04 6469 6374 7239 0000 0072 3700  tr..dictr9...r7.
-000006a0: 0000 7237 0000 0072 3700 0000 7238 0000  ..r7...r7...r8..
-000006b0: 00da 083c 6d6f 6475 6c65 3e01 0000 0073  ...<module>....s
-000006c0: 0400 0000 080d 1a03                      ........
+000004f0: 6469 616e 5265 64da 0654 6f6d 6174 6fda  dianRed..Tomato.
+00000500: 0952 6f79 616c 426c 7565 da0a 446f 6467  .RoyalBlue..Dodg
+00000510: 6572 426c 7565 2902 da0a 6461 726b 6465  erBlue)...darkde
+00000520: 7465 6374 5a06 6973 4461 726b 2903 7202  tectZ.isDark).r.
+00000530: 0000 0072 0300 0000 da04 6d6f 6465 a900  ...r......mode..
+00000540: 7238 0000 00fa 772f 5573 6572 732f 6d69  r8....w/Users/mi
+00000550: 6b72 7562 696e 2f4c 6962 7261 7279 2f43  krubin/Library/C
+00000560: 6c6f 7564 5374 6f72 6167 652f 476f 6f67  loudStorage/Goog
+00000570: 6c65 4472 6976 652d 6d69 6b72 7562 696e  leDrive-mikrubin
+00000580: 4067 6d61 696c 2e63 6f6d 2f4d 7920 4472  @gmail.com/My Dr
+00000590: 6976 652f 5079 7468 6f6e 2f6d 6170 7461  ive/Python/mapta
+000005a0: 736b 6572 2f6d 6170 7461 736b 6572 2f73  sker/maptasker/s
+000005b0: 7263 2f63 6f6c 726d 6f64 652e 7079 da0e  rc/colrmode.py..
+000005c0: 7365 745f 636f 6c6f 725f 6d6f 6465 1100  set_color_mode..
+000005d0: 0000 73a0 0000 0008 0912 0104 0208 0202  ..s.............
+000005e0: 0104 0102 ff04 0202 fe04 0302 fd04 0402  ................
+000005f0: fc04 0502 fb04 0602 fa04 0702 f904 0802  ................
+00000600: f804 0902 f704 0a02 f604 0b02 f504 0c02  ................
+00000610: f404 0d02 f304 0e02 f204 0f02 f104 1002  ................
+00000620: f004 1102 ef04 1206 ee04 2a02 eb04 0102  ..........*.....
+00000630: ff04 0202 fe04 0302 fd04 0402 fc04 0502  ................
+00000640: fb04 0602 fa04 0702 f904 0802 f804 0902  ................
+00000650: f704 0a02 f604 0b02 f504 0c02 f404 0d02  ................
+00000660: f304 0e02 f204 0f02 f104 1002 f004 1102  ................
+00000670: ef04 1206 ee04 1572 3a00 0000 2904 7236  .......r:...).r6
+00000680: 0000 00da 0373 7472 da04 6469 6374 723a  .....str..dictr:
+00000690: 0000 0072 3800 0000 7238 0000 0072 3800  ...r8...r8...r8.
+000006a0: 0000 7239 0000 00da 083c 6d6f 6475 6c65  ..r9.....<module
+000006b0: 3e01 0000 0073 0400 0000 080d 1a03       >....s........
```

### Comparing `maptasker-1.3.1/maptasker/src/__pycache__/condition.cpython-310.pyc` & `maptasker-1.3.2/maptasker/src/__pycache__/condition.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Wed Mar 15 16:55:20 2023 UTC, .py size: 9131 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 12% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 78f8 1164 ab23 0000  o.......x..d.#..
+00000000: 6f0d 0d0a 0000 0000 918f 1c64 ab23 0000  o..........d.#..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0002 0000 0040 0000 0073 7400 0000 6400  .....@...st...d.
 00000030: 6401 6c00 6d01 0200 0100 6d02 5a03 0100  d.l.m.....m.Z...
 00000040: 6400 6401 6c04 6d01 0200 0100 6d05 5a06  d.d.l.m.....m.Z.
 00000050: 0100 6400 6402 6c07 6d08 5a08 0100 6400  ..d.d.l.m.Z...d.
 00000060: 6403 6c09 6d0a 5a0a 0100 6400 6404 6c0b  d.l.m.Z...d.d.l.
 00000070: 6d0c 5a0c 0100 6405 6406 8400 5a0d 6407  m.Z...d.d...Z.d.
@@ -32,46 +32,46 @@
 000001f0: a002 6410 a101 9b00 9d05 7d01 7c01 5300  ..d.......}.|.S.
 00000200: 7c08 738b 7c09 729a 7c01 9b00 640e 7c08  |.s.|.r.|...d.|.
 00000210: 9b00 6411 7c09 9b00 6412 7c06 9b00 9d07  ..d.|...d.|.....
 00000220: 7d01 7c01 5300 7c01 7c0a 6a01 1700 6413  }.|.S.|.|.j...d.
 00000230: 1700 7d01 7c01 5300 2914 4e29 08da 0072  ..}.|.S.).N)...r
 00000240: 0500 0000 7205 0000 0072 0500 0000 7205  ....r....r....r.
 00000250: 0000 0072 0500 0000 7205 0000 0072 0500  ...r....r....r..
-00000260: 0000 5a02 6668 5a02 666d da02 7468 da02  ..Z.fhZ.fm..th..
+00000260: 0000 5a02 6668 5a02 666d 5a02 7468 5a02  ..Z.fhZ.fmZ.thZ.
 00000270: 746d da03 7265 70da 0132 7a09 206d 696e  tm..rep..2z. min
 00000280: 7574 6573 207a 0720 686f 7572 7320 5a06  utes z. hours Z.
 00000290: 7265 7076 616c 7a0e 2072 6570 6561 7420  repvalz. repeat 
 000002a0: 6576 6572 7920 5a07 6672 6f6d 7661 725a  every Z.fromvarZ
 000002b0: 0574 6f76 6172 7a0b 5469 6d65 3a20 6672  .tovarz.Time: fr
 000002c0: 6f6d 20fa 013a e902 0000 007a 0420 746f  om ..:.....z. to
 000002d0: 20fa 0120 7a0f 206e 6f74 2079 6574 206d   .. z. not yet m
 000002e0: 6170 7065 6429 03da 0374 6167 da04 7465  apped)...tag..te
 000002f0: 7874 da05 7a66 696c 6c29 0bda 0874 6865  xt..zfill)...the
 00000300: 5f69 7465 6dda 0b63 6f6e 645f 7374 7269  _item..cond_stri
 00000310: 6e67 5a07 746f 5f68 6f75 725a 0974 6f5f  ngZ.to_hourZ.to_
 00000320: 6d69 6e75 7465 5a09 6672 6f6d 5f68 6f75  minuteZ.from_hou
-00000330: 725a 0b66 726f 6d5f 6d69 6e75 7465 7208  rZ.from_minuter.
+00000330: 725a 0b66 726f 6d5f 6d69 6e75 7465 7206  rZ.from_minuter.
 00000340: 0000 005a 0872 6570 5f74 7970 655a 0d66  ...Z.rep_typeZ.f
 00000350: 726f 6d5f 7661 7269 6162 6c65 5a0b 746f  rom_variableZ.to
 00000360: 5f76 6172 6961 626c 65da 0563 6869 6c64  _variable..child
-00000370: a900 7213 0000 00fa 782f 5573 6572 732f  ..r.....x/Users/
+00000370: a900 7211 0000 00fa 782f 5573 6572 732f  ..r.....x/Users/
 00000380: 6d69 6b72 7562 696e 2f4c 6962 7261 7279  mikrubin/Library
 00000390: 2f43 6c6f 7564 5374 6f72 6167 652f 476f  /CloudStorage/Go
 000003a0: 6f67 6c65 4472 6976 652d 6d69 6b72 7562  ogleDrive-mikrub
 000003b0: 696e 4067 6d61 696c 2e63 6f6d 2f4d 7920  in@gmail.com/My 
 000003c0: 4472 6976 652f 5079 7468 6f6e 2f6d 6170  Drive/Python/map
 000003d0: 7461 736b 6572 2f6d 6170 7461 736b 6572  tasker/maptasker
 000003e0: 2f73 7263 2f63 6f6e 6469 7469 6f6e 2e70  /src/condition.p
 000003f0: 79da 0e63 6f6e 6469 7469 6f6e 5f74 696d  y..condition_tim
 00000400: 651a 0000 0073 4e00 0000 020a 02f7 0201  e....sN.........
 00000410: 0201 0201 0201 0201 0201 0201 0201 080b  ................
 00000420: 0401 0a01 0801 0a01 0801 0a01 0801 0a01  ................
 00000430: 0801 0a01 1401 0a01 1201 0a01 0801 0601  ................
 00000440: 0601 0280 0802 1e01 0802 1a01 0405 08fc  ................
-00000450: 1a01 0403 0eff 0401 7215 0000 0063 0200  ........r....c..
+00000450: 1a01 0403 0eff 0401 7213 0000 0063 0200  ........r....c..
 00000460: 0000 0000 0000 0000 0000 0800 0000 0500  ................
 00000470: 0000 4300 0000 73c6 0000 0067 0064 01a2  ..C...s....g.d..
 00000480: 017d 0267 0064 02a2 017d 0364 037d 0464  .}.g.d...}.d.}.d
 00000490: 037d 0564 037d 067c 0044 005d 337d 0764  .}.d.}.|.D.]3}.d
 000004a0: 047c 076a 0076 0072 257c 047c 0274 017c  .|.j.v.r%|.|.t.|
 000004b0: 076a 0283 0164 0518 0019 0017 0064 0617  .j...d.......d..
 000004c0: 007d 0471 1064 077c 076a 0076 0072 327c  .}.q.d.|.j.v.r2|
@@ -82,37 +82,37 @@
 00000510: 009d 037d 017c 0572 577c 019b 0064 0a7c  ...}.|.rW|...d.|
 00000520: 059b 0064 069d 047d 017c 0672 617c 019b  ...d...}.|.ra|..
 00000530: 0064 0b7c 069b 0064 069d 047d 017c 0153  .d.|...d...}.|.S
 00000540: 0029 0c4e 2907 5a06 5375 6e64 6179 5a06  .).N).Z.SundayZ.
 00000550: 4d6f 6e64 6179 5a07 5475 6573 6461 795a  MondayZ.TuesdayZ
 00000560: 0957 6564 6e65 7364 6179 5a08 5468 7572  .WednesdayZ.Thur
 00000570: 7364 6179 5a06 4672 6964 6179 5a08 5361  sdayZ.FridayZ.Sa
-00000580: 7475 7264 6179 290c da07 4a61 6e75 6172  turday)...Januar
-00000590: 79da 0846 6562 7275 6172 795a 054d 6172  y..FebruaryZ.Mar
-000005a0: 6368 5a05 4170 7269 6cda 034d 6179 5a04  chZ.April..MayZ.
+00000580: 7475 7264 6179 290c 5a07 4a61 6e75 6172  turday).Z.Januar
+00000590: 795a 0846 6562 7275 6172 795a 054d 6172  yZ.FebruaryZ.Mar
+000005a0: 6368 5a05 4170 7269 6c5a 034d 6179 5a04  chZ.AprilZ.MayZ.
 000005b0: 4a75 6e65 5a04 4a75 6c79 5a06 4175 6775  JuneZ.JulyZ.Augu
 000005c0: 7374 5a09 5365 7074 656d 6265 725a 074f  stZ.SeptemberZ.O
 000005d0: 6374 6f62 6572 5a08 4e6f 7665 6d62 6572  ctoberZ.November
 000005e0: 5a08 4465 6365 6d62 6572 7205 0000 005a  Z.Decemberr....Z
-000005f0: 0477 6461 79e9 0100 0000 720c 0000 005a  .wday.....r....Z
+000005f0: 0477 6461 79e9 0100 0000 720a 0000 005a  .wday.....r....Z
 00000600: 046d 6461 795a 046d 6e74 687a 0e44 6179  .mdayZ.mnthz.Day
 00000610: 7320 6f66 2057 6565 6b3a 207a 0f44 6179  s of Week: z.Day
 00000620: 7320 6f66 204d 6f6e 7468 3a20 7a08 4d6f  s of Month: z.Mo
-00000630: 6e74 6873 3a20 2903 720d 0000 00da 0369  nths: ).r......i
-00000640: 6e74 720e 0000 0029 0872 1000 0000 7211  ntr....).r....r.
-00000650: 0000 005a 0877 6565 6b64 6179 73da 066d  ...Z.weekdays..m
+00000630: 6e74 6873 3a20 2903 720b 0000 00da 0369  nths: ).r......i
+00000640: 6e74 720c 0000 0029 0872 0e00 0000 720f  ntr....).r....r.
+00000650: 0000 005a 0877 6565 6b64 6179 735a 066d  ...Z.weekdaysZ.m
 00000660: 6f6e 7468 735a 1074 6865 5f64 6179 735f  onthsZ.the_days_
 00000670: 6f66 5f77 6565 6b5a 0d64 6179 735f 6f66  of_weekZ.days_of
 00000680: 5f6d 6f6e 7468 5a0a 7468 655f 6d6f 6e74  _monthZ.the_mont
-00000690: 6873 7212 0000 0072 1300 0000 7213 0000  hsr....r....r...
-000006a0: 0072 1400 0000 da0d 636f 6e64 6974 696f  .r......conditio
+00000690: 6873 7210 0000 0072 1100 0000 7211 0000  hsr....r....r...
+000006a0: 0072 1200 0000 da0d 636f 6e64 6974 696f  .r......conditio
 000006b0: 6e5f 6461 7950 0000 0073 2800 0000 0801  n_dayP...s(.....
 000006c0: 0809 040f 0401 0401 0801 0a01 1c01 0a01  ................
 000006d0: 1001 0a01 1801 0202 0401 0e01 0401 1001  ................
-000006e0: 0401 1001 0401 721c 0000 0063 0400 0000  ......r....c....
+000006e0: 0401 1001 0401 7216 0000 0063 0400 0000  ......r....c....
 000006f0: 0000 0000 0000 0000 0800 0000 0900 0000  ................
 00000700: 4300 0000 73c6 0000 007c 0044 005d 5e7d  C...s....|.D.]^}
 00000710: 047c 046a 0064 016b 0272 5d74 01a0 0264  .|.j.d.k.r]t...d
 00000720: 027c 046a 039b 009d 02a1 0101 0064 037c  .|.j.........d.|
 00000730: 046a 0376 0172 1d7c 046a 039b 0064 039d  .j.v.r.|.j...d..
 00000740: 026e 027c 046a 037d 057c 0574 0476 0172  .n.|.j.}.|.t.v.r
 00000750: 2c74 05a0 067c 047c 0064 037c 03a1 0401  ,t...|.|.d.|....
@@ -124,58 +124,58 @@
 000007b0: 5d7c 019b 0064 0a7c 046a 039b 0064 0b9d  ]|...d.|.j...d..
 000007c0: 047d 017c 0102 0001 0053 0064 0053 0029  .}.|.....S.d.S.)
 000007d0: 0c4e da04 636f 6465 7a10 636f 6e64 6974  .N..codez.condit
 000007e0: 696f 6e5f 7374 6174 653a da01 7346 7a07  ion_state:..sFz.
 000007f0: 5374 6174 653a 20da 0370 696e da04 7472  State: ..pin..tr
 00000800: 7565 7a14 203c 656d 3e5b 696e 7665 7274  uez. <em>[invert
 00000810: 6564 5d3c 2f65 6d3e da05 6465 6275 67fa  ed]</em>..debug.
-00000820: 0720 2863 6f64 653a fa01 2929 0a72 0d00  . (code:..)).r..
-00000830: 0000 7204 0000 0072 2100 0000 720e 0000  ..r....r!...r...
+00000820: 0720 2863 6f64 653a fa01 2929 0a72 0b00  . (code:..)).r..
+00000830: 0000 7204 0000 0072 1b00 0000 720c 0000  ..r....r....r...
 00000840: 0072 0200 0000 da14 7072 6f63 6573 735f  .r......process_
 00000850: 6163 7469 6f6e 5f63 6f64 6573 da12 6275  action_codes..bu
 00000860: 696c 645f 6163 7469 6f6e 5f63 6f64 6573  ild_action_codes
 00000870: da0f 6163 7469 6f6e 5f65 7661 6c75 6174  ..action_evaluat
 00000880: 65da 0f67 6574 5f61 6374 696f 6e5f 636f  e..get_action_co
-00000890: 6465 da04 6669 6e64 2908 7210 0000 0072  de..find).r....r
-000008a0: 1100 0000 da08 636f 6c6f 726d 6170 da0c  ......colormap..
-000008b0: 7072 6f67 7261 6d5f 6172 6773 7212 0000  program_argsr...
+00000890: 6465 da04 6669 6e64 2908 720e 0000 0072  de..find).r....r
+000008a0: 0f00 0000 da08 636f 6c6f 726d 6170 da0c  ......colormap..
+000008b0: 7072 6f67 7261 6d5f 6172 6773 7210 0000  program_argsr...
 000008c0: 005a 0a73 7461 7465 5f63 6f64 65da 0573  .Z.state_code..s
-000008d0: 7461 7465 da06 696e 7665 7274 7213 0000  tate..invertr...
-000008e0: 0072 1300 0000 7214 0000 00da 0f63 6f6e  .r....r......con
+000008d0: 7461 7465 da06 696e 7665 7274 7211 0000  tate..invertr...
+000008e0: 0072 1100 0000 7212 0000 00da 0f63 6f6e  .r....r......con
 000008f0: 6469 7469 6f6e 5f73 7461 7465 8100 0000  dition_state....
 00000900: 7326 0000 0008 040a 0112 011c 0108 0104  s&..............
 00000910: 0108 0104 ff04 040c 0104 ff0e 050a 0112  ................
-00000920: 010a 0108 0112 0108 0104 0172 2d00 0000  ...........r-...
+00000920: 010a 0108 0112 0108 0104 0172 2700 0000  ...........r'...
 00000930: 6304 0000 0000 0000 0000 0000 0007 0000  c...............
 00000940: 0008 0000 0043 0000 0073 a400 0000 7c00  .....C...s....|.
 00000950: a000 6401 a101 7d04 7401 a002 6402 7c04  ..d...}.t...d.|.
 00000960: 6a03 9b00 9d02 a101 0100 6403 7c04 6a03  j.........d.|.j.
 00000970: 7601 721a 7c04 6a03 9b00 6403 9d02 7d05  v.r.|.j...d...}.
 00000980: 6e03 7c04 6a03 7d05 7c05 7404 7601 7229  n.|.j.}.|.t.v.r)
 00000990: 7405 a006 7c04 7c00 6403 7c03 a104 0100  t...|.|.d.|.....
 000009a0: 7407 a008 7c04 7c00 6404 7c02 6403 7c03  t...|.|.d.|.d.|.
 000009b0: a106 7d06 7c06 9b00 7409 7c00 6405 8302  ..}.|...t.|.d...
 000009c0: 9b00 9d02 7d06 7c01 9b00 6406 7c06 9b00  ....}.|...d.|...
 000009d0: 9d03 7d01 7c03 6407 1900 7250 7c01 9b00  ..}.|.d...rP|...
 000009e0: 6408 7c04 6a03 9b00 6409 9d04 7d01 7c01  d.|.j...d...}.|.
-000009f0: 5300 290a 4e72 1d00 0000 7a05 636f 6465  S.).Nr....z.code
+000009f0: 5300 290a 4e72 1700 0000 7a05 636f 6465  S.).Nr....z.code
 00000a00: 3ada 0165 4654 7a07 4576 656e 743a 2072  :..eFTz.Event: r
-00000a10: 2100 0000 7222 0000 0072 2300 0000 290a  !...r"...r#...).
-00000a20: 7228 0000 0072 0400 0000 7221 0000 0072  r(...r....r!...r
-00000a30: 0e00 0000 7202 0000 0072 2400 0000 7225  ....r....r$...r%
-00000a40: 0000 0072 2600 0000 7227 0000 0072 0300  ...r&...r'...r..
-00000a50: 0000 2907 7210 0000 0072 1100 0000 7229  ..).r....r....r)
-00000a60: 0000 0072 2a00 0000 5a0e 7468 655f 6576  ...r*...Z.the_ev
+00000a10: 1b00 0000 721c 0000 0072 1d00 0000 290a  ....r....r....).
+00000a20: 7222 0000 0072 0400 0000 721b 0000 0072  r"...r....r....r
+00000a30: 0c00 0000 7202 0000 0072 1e00 0000 721f  ....r....r....r.
+00000a40: 0000 0072 2000 0000 7221 0000 0072 0300  ...r ...r!...r..
+00000a50: 0000 2907 720e 0000 0072 0f00 0000 7223  ..).r....r....r#
+00000a60: 0000 0072 2400 0000 5a0e 7468 655f 6576  ...r$...Z.the_ev
 00000a70: 656e 745f 636f 6465 5a0a 6576 656e 745f  ent_codeZ.event_
-00000a80: 636f 6465 da05 6576 656e 7472 1300 0000  code..eventr....
-00000a90: 7213 0000 0072 1400 0000 da0f 636f 6e64  r....r......cond
+00000a80: 636f 6465 da05 6576 656e 7472 1100 0000  code..eventr....
+00000a90: 7211 0000 0072 1200 0000 da0f 636f 6e64  r....r......cond
 00000aa0: 6974 696f 6e5f 6576 656e 74a0 0000 0073  ition_event....s
 00000ab0: 2200 0000 0a01 1203 0a01 0e01 0602 0801  "...............
 00000ac0: 0402 0801 04ff 0404 0c01 04ff 1204 0e02  ................
-00000ad0: 0801 1201 0401 7230 0000 0063 0300 0000  ......r0...c....
+00000ad0: 0801 1201 0401 722a 0000 0063 0300 0000  ......r*...c....
 00000ae0: 0000 0000 0000 0000 0b00 0000 0800 0000  ................
 00000af0: 4300 0000 7344 0100 0067 0064 01a2 017d  C...sD...g.d...}
 00000b00: 0364 027d 047c 0044 005d 8e7d 057c 056a  .d.}.|.D.].}.|.j
 00000b10: 007c 0376 0073 1464 037c 056a 0076 0072  .|.v.s.d.|.j.v.r
 00000b20: 1571 087c 0472 1c7c 049b 0064 049d 027d  .q.|.r.|...d...}
 00000b30: 047c 056a 0004 0064 056b 0272 2901 0074  .|.j...d.k.r)..t
 00000b40: 017c 057c 0483 027d 046e 6d04 0064 066b  .|.|...}.nm..d.k
@@ -196,46 +196,46 @@
 00000c30: 0253 0064 147c 049b 009d 0253 0029 154e  .S.d.|.....S.).N
 00000c40: 2905 da05 6364 6174 65da 0565 6461 7465  )...cdate..edate
 00000c50: da05 666c 6167 73da 0269 64da 0f50 726f  ..flags..id..Pro
 00000c60: 6669 6c65 5661 7269 6162 6c65 7205 0000  fileVariabler...
 00000c70: 00da 036d 6964 7a0e 203c 656d 3e61 6e64  ...midz. <em>and
 00000c80: 3c2f 656d 3e20 5a04 5469 6d65 5a03 4461  </em> Z.TimeZ.Da
 00000c90: 79da 0553 7461 7465 da05 4576 656e 74da  y..State..Event.
-00000ca0: 0341 7070 da05 6c61 6265 6c72 0c00 0000  .App..labelr....
+00000ca0: 0341 7070 da05 6c61 6265 6c72 0a00 0000  .App..labelr....
 00000cb0: 7a0c 4170 706c 6963 6174 696f 6e3a 5a03  z.Application:Z.
 00000cc0: 4c6f 63da 036c 6174 da04 6c6f 6e67 da03  Loc..lat..long..
 00000cd0: 7261 647a 174c 6f63 6174 696f 6e20 7769  radz.Location wi
 00000ce0: 7468 206c 6174 6974 7564 6520 7a0b 206c  th latitude z. l
 00000cf0: 6f6e 6769 7475 6465 207a 0820 7261 6469  ongitude z. radi
 00000d00: 7573 207a 0a63 6f6e 6469 7469 6f6e 2029  us z.condition )
-00000d10: 0772 0d00 0000 7215 0000 0072 1c00 0000  .r....r....r....
-00000d20: 722d 0000 0072 3000 0000 720e 0000 0072  r-...r0...r....r
-00000d30: 2800 0000 290b da0b 7468 655f 7072 6f66  (...)...the_prof
-00000d40: 696c 6572 2900 0000 722a 0000 005a 0c69  iler)...r*...Z.i
+00000d10: 0772 0b00 0000 7213 0000 0072 1600 0000  .r....r....r....
+00000d20: 7227 0000 0072 2a00 0000 720c 0000 0072  r'...r*...r....r
+00000d30: 2200 0000 290b da0b 7468 655f 7072 6f66  "...)...the_prof
+00000d40: 696c 6572 2300 0000 7224 0000 005a 0c69  iler#...r$...Z.i
 00000d50: 676e 6f72 655f 6974 656d 73da 0963 6f6e  gnore_items..con
 00000d60: 6469 7469 6f6e da04 6974 656d 5a08 7468  dition..itemZ.th
-00000d70: 655f 6170 7073 5a04 6170 7073 723b 0000  e_appsZ.appsr;..
-00000d80: 005a 036c 6f6e 723d 0000 0072 1300 0000  .Z.lonr=...r....
-00000d90: 7213 0000 0072 1400 0000 da17 7061 7273  r....r......pars
+00000d70: 655f 6170 7073 5a04 6170 7073 7235 0000  e_appsZ.appsr5..
+00000d80: 005a 036c 6f6e 7237 0000 0072 1100 0000  .Z.lonr7...r....
+00000d90: 7211 0000 0072 1200 0000 da17 7061 7273  r....r......pars
 00000da0: 655f 7072 6f66 696c 655f 636f 6e64 6974  e_profile_condit
 00000db0: 696f 6ebe 0000 0073 4c00 0000 0801 0401  ion....sL.......
 00000dc0: 0801 1402 0202 0401 0a01 0403 0a01 0c01  ................
 00000dd0: 0a02 0c01 0a02 1001 0a02 1001 0a02 0401  ................
 00000de0: 0801 0a01 1001 0280 1001 0602 0c01 0c01  ................
 00000df0: 0c01 0401 0c02 0201 04ff 0201 04ff 04ff  ................
-00000e00: 0205 0201 0280 1602 7241 0000 0029 12da  ........rA...)..
+00000e00: 0205 0201 0280 1602 723b 0000 0029 12da  ........r;...)..
 00000e10: 156d 6170 7461 736b 6572 2e73 7263 2e61  .maptasker.src.a
 00000e20: 6374 696f 6e65 da03 7372 63da 0761 6374  ctione..src..act
-00000e30: 696f 6e65 7226 0000 00da 156d 6170 7461  ioner&.....mapta
+00000e30: 696f 6e65 7220 0000 00da 156d 6170 7461  ioner .....mapta
 00000e40: 736b 6572 2e73 7263 2e61 6374 696f 6e64  sker.src.actiond
-00000e50: da07 6163 7469 6f6e 6472 2400 0000 da15  ..actiondr$.....
+00000e50: da07 6163 7469 6f6e 6472 1e00 0000 da15  ..actiondr......
 00000e60: 6d61 7074 6173 6b65 722e 7372 632e 6163  maptasker.src.ac
 00000e70: 7469 6f6e 6372 0200 0000 da16 6d61 7074  tioncr......mapt
 00000e80: 6173 6b65 722e 7372 632e 7072 696f 7269  asker.src.priori
 00000e90: 7479 7203 0000 00da 166d 6170 7461 736b  tyr......maptask
 00000ea0: 6572 2e73 7263 2e73 7973 636f 6e73 7472  er.src.sysconstr
-00000eb0: 0400 0000 7215 0000 0072 1c00 0000 722d  ....r....r....r-
-00000ec0: 0000 0072 3000 0000 7241 0000 0072 1300  ...r0...rA...r..
-00000ed0: 0000 7213 0000 0072 1300 0000 7214 0000  ..r....r....r...
+00000eb0: 0400 0000 7213 0000 0072 1600 0000 7227  ....r....r....r'
+00000ec0: 0000 0072 2a00 0000 723b 0000 0072 1100  ...r*...r;...r..
+00000ed0: 0000 7211 0000 0072 1100 0000 7212 0000  ..r....r....r...
 00000ee0: 00da 083c 6d6f 6475 6c65 3e01 0000 0073  ...<module>....s
 00000ef0: 1400 0000 120d 1201 0c01 0c03 0c01 0806  ................
 00000f00: 0836 0831 081f 0c1e                      .6.1....
```

### Comparing `maptasker-1.3.1/maptasker/src/__pycache__/debug.cpython-310.pyc` & `maptasker-1.3.2/maptasker/src/__pycache__/debug.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Thu Mar 16 19:15:58 2023 UTC, .py size: 1945 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 15% similar despite different names*

```diff
@@ -1,60 +1,71 @@
-00000000: 6f0d 0d0a 0000 0000 ee6a 1364 9907 0000  o........j.d....
+00000000: 6f0d 0d0a 0000 0000 3cb6 2164 8809 0000  o.......<.!d....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
-00000020: 0008 0000 0040 0000 0073 3800 0000 6400  .....@...s8...d.
+00000020: 0008 0000 0040 0000 0073 3c00 0000 6400  .....@...s<...d.
 00000030: 6401 6c00 5a00 6400 6401 6c01 6d02 0200  d.l.Z.d.d.l.m...
-00000040: 0100 6d03 5a04 0100 6402 6505 6403 6505  ..m.Z...d.e.d.e.
-00000050: 6404 6506 6405 6401 6608 6406 6407 8404  d.e.d.d.f.d.d...
-00000060: 5a07 6401 5300 2908 e900 0000 004e da08  Z.d.S.)......N..
-00000070: 636f 6c6f 726d 6170 da0c 7072 6f67 7261  colormap..progra
-00000080: 6d5f 6172 6773 da0b 6f75 7470 7574 5f6c  m_args..output_l
-00000090: 6973 74da 0672 6574 7572 6e63 0300 0000  ist..returnc....
-000000a0: 0000 0000 0000 0000 0500 0000 0b00 0000  ................
-000000b0: 4300 0000 7380 0000 0074 00a0 017c 007c  C...s....t...|.|
-000000c0: 017c 0264 0164 0274 0274 036a 0483 019b  .|.d.d.t.t.j....
-000000d0: 009d 02a1 0501 007c 01a0 05a1 0044 005d  .......|.....D.]
-000000e0: 125c 027d 037d 0474 00a0 017c 007c 017c  .\.}.}.t...|.|.|
-000000f0: 0264 017c 039b 0064 037c 049b 009d 03a1  .d.|...d.|......
-00000100: 0501 0071 137c 00a0 05a1 0044 005d 135c  ...q.|.....D.].\
-00000110: 027d 037d 0474 00a0 017c 007c 017c 0264  .}.}.t...|.|.|.d
-00000120: 0164 047c 039b 0064 057c 049b 009d 04a1  .d.|...d.|......
-00000130: 0501 0071 2a64 0653 0029 077a b40a 2020  ...q*d.S.).z..  
-00000140: 2020 4f75 7470 7574 206f 7572 2072 756e    Output our run
-00000150: 7469 6d65 2061 7267 756d 656e 7473 0a20  time arguments. 
-00000160: 2020 2020 2020 203a 7061 7261 6d20 636f         :param co
-00000170: 6c6f 726d 6170 3a20 636f 6c6f 7273 2074  lormap: colors t
-00000180: 6f20 7573 650a 2020 2020 2020 2020 3a70  o use.        :p
-00000190: 6172 616d 2070 726f 6772 616d 5f61 7267  aram program_arg
-000001a0: 733a 206f 7468 6572 2072 756e 7469 6d65  s: other runtime
-000001b0: 2061 7267 756d 656e 7473 0a20 2020 2020   arguments.     
-000001c0: 2020 203a 7061 7261 6d20 6f75 7470 7574     :param output
-000001d0: 5f6c 6973 743a 2077 6865 7265 2074 6865  _list: where the
-000001e0: 206f 7574 7075 7420 676f 6573 0a20 2020   output goes.   
-000001f0: 20e9 0400 0000 7a29 3c73 7061 6e20 7374   .....z)<span st
-00000200: 796c 653d 2263 6f6c 6f72 3a47 7265 656e  yle="color:Green
-00000210: 223c 2f73 7061 6e3e 7379 732e 6172 6776  "</span>sys.argv
-00000220: 3a7a 023a 207a 0d63 6f6c 6f72 6d61 7020  :z.: z.colormap 
-00000230: 666f 7220 7a08 2073 6574 2074 6f20 4e29  for z. set to N)
-00000240: 06da 0c62 7569 6c64 5f6f 7574 7075 74da  ...build_output.
-00000250: 096d 795f 6f75 7470 7574 da03 7374 72da  .my_output..str.
-00000260: 0373 7973 da04 6172 6776 da05 6974 656d  .sys..argv..item
-00000270: 7329 0572 0200 0000 7203 0000 0072 0400  s).r....r....r..
-00000280: 0000 da03 6b65 79da 0576 616c 7565 a900  ....key..value..
-00000290: 720f 0000 00fa 742f 5573 6572 732f 6d69  r.....t/Users/mi
-000002a0: 6b72 7562 696e 2f4c 6962 7261 7279 2f43  krubin/Library/C
-000002b0: 6c6f 7564 5374 6f72 6167 652f 476f 6f67  loudStorage/Goog
-000002c0: 6c65 4472 6976 652d 6d69 6b72 7562 696e  leDrive-mikrubin
-000002d0: 4067 6d61 696c 2e63 6f6d 2f4d 7920 4472  @gmail.com/My Dr
-000002e0: 6976 652f 5079 7468 6f6e 2f6d 6170 7461  ive/Python/mapta
-000002f0: 736b 6572 2f6d 6170 7461 736b 6572 2f73  sker/maptasker/s
-00000300: 7263 2f64 6562 7567 2e70 79da 0664 6562  rc/debug.py..deb
-00000310: 7567 3112 0000 0073 2800 0000 0407 0201  ug1....s(.......
-00000320: 0201 0201 0201 0e01 04fb 1007 0401 1401  ................
-00000330: 06ff 1003 0401 0201 0201 0201 0201 0e01  ................
-00000340: 06fb 04ff 7211 0000 0029 0872 0a00 0000  ....r....).r....
-00000350: da15 6d61 7074 6173 6b65 722e 7372 632e  ..maptasker.src.
-00000360: 6f75 7470 7574 6cda 0373 7263 da07 6f75  outputl..src..ou
-00000370: 7470 7574 6c72 0700 0000 da04 6469 6374  tputlr......dict
-00000380: da04 6c69 7374 7211 0000 0072 0f00 0000  ..listr....r....
-00000390: 720f 0000 0072 0f00 0000 7210 0000 00da  r....r....r.....
-000003a0: 083c 6d6f 6475 6c65 3e01 0000 0073 0600  .<module>....s..
-000003b0: 0000 080d 1201 1e03                      ........
+00000040: 0100 6d03 5a04 0100 6402 5a05 6403 6506  ..m.Z...d.Z.d.e.
+00000050: 6404 6506 6405 6507 6406 6401 6608 6407  d.e.d.e.d.d.f.d.
+00000060: 6408 8404 5a08 6401 5300 2909 e900 0000  d...Z.d.S.).....
+00000070: 004e 7a2e 3c73 7061 6e20 7374 796c 653d  .Nz.<span style=
+00000080: 2263 6f6c 6f72 3a57 6869 7465 3b66 6f6e  "color:White;fon
+00000090: 742d 6661 6d69 6c79 3a43 6f75 7269 6572  t-family:Courier
+000000a0: 223e da08 636f 6c6f 726d 6170 da0c 7072  ">..colormap..pr
+000000b0: 6f67 7261 6d5f 6172 6773 da0b 6f75 7470  ogram_args..outp
+000000c0: 7574 5f6c 6973 74da 0672 6574 7572 6e63  ut_list..returnc
+000000d0: 0300 0000 0000 0000 0000 0000 0500 0000  ................
+000000e0: 0d00 0000 4300 0000 73c8 0000 0074 00a0  ....C...s....t..
+000000f0: 017c 007c 017c 0264 0174 029b 0064 0274  .|.|.|.d.t...d.t
+00000100: 0374 046a 0583 019b 0064 039d 04a1 0501  .t.j.....d......
+00000110: 0074 00a0 017c 007c 017c 0264 0164 04a1  .t...|.|.|.d.d..
+00000120: 0501 007c 01a0 06a1 0044 005d 155c 027d  ...|.....D.].\.}
+00000130: 037d 0474 00a0 017c 007c 017c 0264 0174  .}.t...|.|.|.d.t
+00000140: 029b 007c 039b 0064 057c 049b 0064 039d  ...|...d.|...d..
+00000150: 05a1 0501 0071 1f74 00a0 017c 007c 017c  .....q.t...|.|.|
+00000160: 0264 0164 04a1 0501 007c 00a0 06a1 0044  .d.d.....|.....D
+00000170: 005d 165c 027d 037d 0474 00a0 017c 007c  .].\.}.}.t...|.|
+00000180: 017c 0264 0174 029b 0064 067c 039b 0064  .|.d.t...d.|...d
+00000190: 077c 049b 0064 039d 06a1 0501 0071 4274  .|...d.......qBt
+000001a0: 00a0 017c 007c 017c 0264 0164 04a1 0501  ...|.|.|.d.d....
+000001b0: 0064 0853 0029 097a b40a 2020 2020 4f75  .d.S.).z..    Ou
+000001c0: 7470 7574 206f 7572 2072 756e 7469 6d65  tput our runtime
+000001d0: 2061 7267 756d 656e 7473 0a20 2020 2020   arguments.     
+000001e0: 2020 203a 7061 7261 6d20 636f 6c6f 726d     :param colorm
+000001f0: 6170 3a20 636f 6c6f 7273 2074 6f20 7573  ap: colors to us
+00000200: 650a 2020 2020 2020 2020 3a70 6172 616d  e.        :param
+00000210: 2070 726f 6772 616d 5f61 7267 733a 206f   program_args: o
+00000220: 7468 6572 2072 756e 7469 6d65 2061 7267  ther runtime arg
+00000230: 756d 656e 7473 0a20 2020 2020 2020 203a  uments.        :
+00000240: 7061 7261 6d20 6f75 7470 7574 5f6c 6973  param output_lis
+00000250: 743a 2077 6865 7265 2074 6865 206f 7574  t: where the out
+00000260: 7075 7420 676f 6573 0a20 2020 20e9 0400  put goes.    ...
+00000270: 0000 7a09 7379 732e 6172 6776 3a7a 073c  ..z.sys.argv:z.<
+00000280: 2f73 7061 6e3e da00 7a02 3a20 7a0d 636f  /span>..z.: z.co
+00000290: 6c6f 726d 6170 2066 6f72 207a 0820 7365  lormap for z. se
+000002a0: 7420 746f 204e 2907 da0c 6275 696c 645f  t to N)...build_
+000002b0: 6f75 7470 7574 da09 6d79 5f6f 7574 7075  output..my_outpu
+000002c0: 74da 0b64 6562 7567 5f73 7479 6c65 da03  t..debug_style..
+000002d0: 7374 72da 0373 7973 da04 6172 6776 da05  str..sys..argv..
+000002e0: 6974 656d 7329 0572 0200 0000 7203 0000  items).r....r...
+000002f0: 0072 0400 0000 da03 6b65 79da 0576 616c  .r......key..val
+00000300: 7565 a900 7211 0000 00fa 742f 5573 6572  ue..r.....t/User
+00000310: 732f 6d69 6b72 7562 696e 2f4c 6962 7261  s/mikrubin/Libra
+00000320: 7279 2f43 6c6f 7564 5374 6f72 6167 652f  ry/CloudStorage/
+00000330: 476f 6f67 6c65 4472 6976 652d 6d69 6b72  GoogleDrive-mikr
+00000340: 7562 696e 4067 6d61 696c 2e63 6f6d 2f4d  ubin@gmail.com/M
+00000350: 7920 4472 6976 652f 5079 7468 6f6e 2f6d  y Drive/Python/m
+00000360: 6170 7461 736b 6572 2f6d 6170 7461 736b  aptasker/maptask
+00000370: 6572 2f73 7263 2f64 6562 7567 2e70 79da  er/src/debug.py.
+00000380: 0664 6562 7567 3114 0000 0073 5800 0000  .debug1....sX...
+00000390: 0407 0201 0201 0201 0201 1401 04fb 0407  ................
+000003a0: 0201 0201 0201 0201 0201 04fb 1007 0401  ................
+000003b0: 0201 0201 0201 0201 1201 06fb 0407 0201  ................
+000003c0: 0201 0201 0201 0201 04fb 1007 0401 0201  ................
+000003d0: 0201 0201 0201 1401 06fb 0407 0201 0201  ................
+000003e0: 0201 0201 0201 08fb 7213 0000 0029 0972  ........r....).r
+000003f0: 0c00 0000 da15 6d61 7074 6173 6b65 722e  ......maptasker.
+00000400: 7372 632e 6f75 7470 7574 6cda 0373 7263  src.outputl..src
+00000410: da07 6f75 7470 7574 6c72 0800 0000 720a  ..outputlr....r.
+00000420: 0000 00da 0464 6963 74da 046c 6973 7472  .....dict..listr
+00000430: 1300 0000 7211 0000 0072 1100 0000 7211  ....r....r....r.
+00000440: 0000 0072 1200 0000 da08 3c6d 6f64 756c  ...r......<modul
+00000450: 653e 0100 0000 7308 0000 0008 0d12 0104  e>....s.........
+00000460: 021e 03                                  ...
```

### Comparing `maptasker-1.3.1/maptasker/src/__pycache__/getputarg.cpython-310.pyc` & `maptasker-1.3.2/maptasker/src/__pycache__/getputarg.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Sun Feb 19 16:07:46 2023 UTC, .py size: 2142 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 12% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 5249 f263 5e08 0000  o.......RI.c^...
+00000000: 6f0d 0d0a 0000 0000 918f 1c64 5e08 0000  o..........d^...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0002 0000 0040 0000 0073 3800 0000 6400  .....@...s8...d.
 00000030: 6401 6c00 5a00 6400 6402 6c01 6d02 5a02  d.l.Z.d.d.l.m.Z.
 00000040: 0100 6400 6403 6c03 6d04 5a04 0100 6400  ..d.d.l.m.Z...d.
 00000050: 6404 6c03 6d05 5a05 0100 6405 6406 8400  d.l.m.Z...d.d...
 00000060: 5a06 6401 5300 2907 e900 0000 004e 2901  Z.d.S.)......N).
 00000070: da04 5061 7468 2901 da0e 4152 4755 4d45  ..Path)...ARGUME
```

### Comparing `maptasker-1.3.1/maptasker/src/__pycache__/initparg.cpython-310.pyc` & `maptasker-1.3.2/maptasker/src/__pycache__/initparg.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar  3 20:27:21 2023 UTC, .py size: 2366 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 2958 0264 3e09 0000  o.......)X.d>...
+00000000: 6f0d 0d0a 0000 0000 918f 1c64 3e09 0000  o..........d>...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0003 0000 0040 0000 0073 1e00 0000 6400  .....@...s....d.
 00000030: 6401 6c00 6d01 5a01 0100 6402 6502 6602  d.l.m.Z...d.e.f.
 00000040: 6403 6404 8404 5a03 6405 5300 2906 e900  d.d...Z.d.S.)...
 00000050: 0000 00a9 01da 0b46 4f4e 545f 544f 5f55  .......FONT_TO_U
 00000060: 5345 da06 7265 7475 726e 6300 0000 0000  SE..returnc.....
 00000070: 0000 0000 0000 0000 0000 000a 0000 0043  ...............C
```

### Comparing `maptasker-1.3.1/maptasker/src/__pycache__/kidapp.cpython-310.pyc` & `maptasker-1.3.2/maptasker/src/__pycache__/kidapp.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Sun Feb 26 19:09:05 2023 UTC, .py size: 2397 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 51ae fb63 5d09 0000  o.......Q..c]...
+00000000: 6f0d 0d0a 0000 0000 918f 1c64 5d09 0000  o..........d]...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0073 2000 0000 6400  .....@...s ...d.
 00000030: 6401 6c00 5a01 6402 6501 6a02 6403 6503  d.l.Z.d.e.j.d.e.
 00000040: 6604 6404 6405 8404 5a04 6401 5300 2906  f.d.d...Z.d.S.).
 00000050: e900 0000 004e da07 656c 656d 656e 74da  .....N..element.
 00000060: 0672 6574 7572 6e63 0100 0000 0000 0000  .returnc........
 00000070: 0000 0000 0b00 0000 0b00 0000 4300 0000  ............C...
```

### Comparing `maptasker-1.3.1/maptasker/src/__pycache__/mapit.cpython-310.pyc` & `maptasker-1.3.2/maptasker/src/__pycache__/mapit.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Thu Mar 16 19:15:58 2023 UTC, .py size: 17604 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 16% similar despite different names*

```diff
@@ -1,415 +1,325 @@
-00000000: 6f0d 0d0a 0000 0000 ee6a 1364 c444 0000  o........j.d.D..
+00000000: 6f0d 0d0a 0000 0000 7c5f 2c64 ee3b 0000  o.......|_,d.;..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
-00000020: 000e 0000 0040 0000 0073 b001 0000 6400  .....@...s....d.
+00000020: 000e 0000 0040 0000 0073 3c01 0000 6400  .....@...s<...d.
 00000030: 6401 6c00 5a00 6400 6401 6c01 5a01 6400  d.l.Z.d.d.l.Z.d.
-00000040: 6401 6c02 5a02 6400 6401 6c03 5a04 6400  d.l.Z.d.d.l.Z.d.
-00000050: 6402 6c05 6d06 5a06 6d07 5a07 0100 6400  d.l.m.Z.m.Z...d.
-00000060: 6403 6c08 6d09 5a09 0100 6400 6404 6c0a  d.l.m.Z...d.d.l.
-00000070: 6d0b 5a0b 0100 6400 6405 6c0c 6d0d 5a0d  m.Z...d.d.l.m.Z.
-00000080: 0100 6400 6406 6c0e 6d0f 5a0f 6d10 5a10  ..d.d.l.m.Z.m.Z.
-00000090: 0100 6400 6401 6c11 6d12 0200 0100 6d13  ..d.d.l.m.....m.
-000000a0: 5a14 0100 6400 6401 6c15 6d12 0200 0100  Z...d.d.l.m.....
-000000b0: 6d16 5a17 0100 6400 6401 6c18 6d12 0200  m.Z...d.d.l.m...
-000000c0: 0100 6d19 5a19 0100 6400 6401 6c1a 6d12  ..m.Z...d.d.l.m.
-000000d0: 0200 0100 6d1b 5a1c 0100 6400 6407 6c1d  ....m.Z...d.d.l.
-000000e0: 6d1e 5a1e 0100 6400 6408 6c1f 6d20 5a20  m.Z...d.d.l.m Z 
-000000f0: 0100 6400 6409 6c1f 6d21 5a21 0100 6400  ..d.d.l.m!Z!..d.
-00000100: 640a 6c22 6d23 5a23 0100 6400 640b 6c24  d.l"m#Z#..d.d.l$
-00000110: 6d25 5a25 0100 6400 640c 6c26 6d27 5a27  m%Z%..d.d.l&m'Z'
-00000120: 0100 640d 640e 8400 5a28 640f 6410 8400  ..d.d...Z(d.d...
-00000130: 5a29 6528 8300 5a2a 6500 a02b 6529 a101  Z)e(..Z*e..+e)..
-00000140: 0100 6411 6504 6a2c 6a2d 6a2d 6412 6504  ..d.e.j,j-j-d.e.
-00000150: 6a2c 6a2d 6a2e 6413 650f 652f 1900 6414  j,j-j.d.e.e/..d.
-00000160: 6510 652f 650f 6504 6a2c 6a2d 6a2e 1900  e.e/e.e.j,j-j...
-00000170: 6602 1900 6415 6401 660a 6416 6417 8404  f...d.d.f.d.d...
-00000180: 5a30 6413 650f 652f 1900 6418 652f 6419  Z0d.e.e/..d.e/d.
-00000190: 652f 6415 6401 6608 641a 641b 8404 5a31  e/d.d.f.d.d...Z1
-000001a0: 641c 652f 641d 652f 6411 6504 6a2c 6412  d.e/d.e/d.e.j,d.
-000001b0: 6504 6a2c 6413 6532 6414 6533 6415 6401  e.j,d.e2d.e3d.d.
-000001c0: 660e 641e 641f 8404 5a34 0900 6415 6535  f.d.d...Z4..d.e5
-000001d0: 6602 6420 6421 8404 5a36 6401 5300 2922  f.d d!..Z6d.S.)"
-000001e0: e900 0000 004e 2902 da05 6475 6d70 73da  .....N)...dumps.
-000001f0: 056c 6f61 6473 2901 da06 6765 7463 7764  .loads)...getcwd
-00000200: 2901 da04 5061 7468 2901 da0a 6d65 7373  )...Path)...mess
-00000210: 6167 6562 6f78 2902 da04 4c69 7374 da04  agebox)...List..
-00000220: 4469 6374 2901 da0f 6469 7370 6c61 795f  Dict)...display_
-00000230: 6361 7665 6174 7329 01da 0c43 4f55 4e54  caveats)...COUNT
-00000240: 4552 5f46 494c 4529 01da 066c 6f67 6765  ER_FILE)...logge
-00000250: 7229 01da 1067 6574 5f74 6865 5f78 6d6c  r)...get_the_xml
-00000260: 5f64 6174 6129 01da 0f67 6574 5f70 7265  _data)...get_pre
-00000270: 6665 7265 6e63 6573 2901 da06 6465 6275  ferences)...debu
-00000280: 6731 6300 0000 0000 0000 0000 0000 0000  g1c.............
-00000290: 0000 0004 0000 0043 0000 0073 2c00 0000  .......C...s,...
-000002a0: 7400 a001 7400 7402 8301 a003 a100 a101  t...t.t.........
-000002b0: 7214 7404 7405 7402 6401 8302 a006 a100  r.t.t.t.d.......
-000002c0: 8301 6402 1700 5300 6403 5300 2904 7a7f  ..d...S.d.S.).z.
-000002d0: 5265 6164 2074 6865 2070 726f 6772 616d  Read the program
-000002e0: 2063 6f75 6e74 6572 0a0a 2020 2020 5061   counter..    Pa
-000002f0: 7261 6d65 7465 7273 3a20 6e6f 6e65 0a0a  rameters: none..
-00000300: 2020 2020 5265 7475 726e 733a 2074 6865      Returns: the
-00000310: 2063 6f75 6e74 206f 6620 7468 6520 6e75   count of the nu
-00000320: 6d62 6572 206f 6620 7469 6d65 7320 7468  mber of times th
-00000330: 6520 7072 6f67 7261 6d20 6861 7320 6265  e program has be
-00000340: 656e 2063 616c 6c65 640a 0a20 2020 20da  en called..    .
-00000350: 0172 e901 0000 0072 0100 0000 2907 7205  .r.....r....).r.
-00000360: 0000 00da 0665 7869 7374 7372 0a00 0000  .....existsr....
-00000370: 5a07 7265 736f 6c76 6572 0300 0000 da04  Z.resolver......
-00000380: 6f70 656e da04 7265 6164 a900 7214 0000  open..read..r...
-00000390: 0072 1400 0000 fa74 2f55 7365 7273 2f6d  .r.....t/Users/m
-000003a0: 696b 7275 6269 6e2f 4c69 6272 6172 792f  ikrubin/Library/
-000003b0: 436c 6f75 6453 746f 7261 6765 2f47 6f6f  CloudStorage/Goo
-000003c0: 676c 6544 7269 7665 2d6d 696b 7275 6269  gleDrive-mikrubi
-000003d0: 6e40 676d 6169 6c2e 636f 6d2f 4d79 2044  n@gmail.com/My D
-000003e0: 7269 7665 2f50 7974 686f 6e2f 6d61 7074  rive/Python/mapt
-000003f0: 6173 6b65 722f 6d61 7074 6173 6b65 722f  asker/maptasker/
-00000400: 7372 632f 6d61 7069 742e 7079 da0c 7265  src/mapit.py..re
-00000410: 6164 5f63 6f75 6e74 6572 4000 0000 730a  ad_counter@...s.
-00000420: 0000 0010 0a16 ff02 ff02 0302 fd72 1600  .............r..
-00000430: 0000 6300 0000 0000 0000 0000 0000 0001  ..c.............
-00000440: 0000 0008 0000 0043 0000 0073 3e00 0000  .......C...s>...
-00000450: 7400 7401 6401 8302 8f10 7d00 7c00 a002  t.t.d.....}.|...
-00000460: 7403 7404 8301 a101 0100 5700 6402 0400  t.t.......W.d...
-00000470: 0400 8303 0100 6402 5300 3100 7318 7701  ......d.S.1.s.w.
-00000480: 0100 0100 0100 5900 0100 6402 5300 2903  ......Y...d.S.).
-00000490: 7a48 5772 6974 6520 7468 6520 7072 6f67  zHWrite the prog
-000004a0: 7261 6d20 636f 756e 7465 720a 0a20 2020  ram counter..   
-000004b0: 2050 6172 616d 6574 6572 733a 206e 6f6e   Parameters: non
-000004c0: 650a 0a20 2020 2052 6574 7572 6e73 3a20  e..    Returns: 
-000004d0: 6e6f 6e65 0a0a 2020 2020 da01 774e 2905  none..    ..wN).
-000004e0: 7212 0000 0072 0a00 0000 da05 7772 6974  r....r......writ
-000004f0: 6572 0200 0000 da0b 7275 6e5f 636f 756e  er......run_coun
-00000500: 7465 7229 01da 0166 7214 0000 0072 1400  ter)...fr....r..
-00000510: 0000 7215 0000 00da 0d77 7269 7465 5f63  ..r......write_c
-00000520: 6f75 6e74 6572 4f00 0000 730c 0000 000c  ounterO...s.....
-00000530: 0810 010a ff04 0210 fe04 0272 1b00 0000  ...........r....
-00000540: da04 7472 6565 da04 726f 6f74 da0b 6f75  ..tree..root..ou
-00000550: 7470 7574 5f6c 6973 74da 1061 6c6c 5f74  tput_list..all_t
-00000560: 6173 6b65 725f 6974 656d 73da 0672 6574  asker_items..ret
-00000570: 7572 6e63 0400 0000 0000 0000 0000 0000  urnc............
-00000580: 0500 0000 0300 0000 4300 0000 735a 0000  ........C...sZ..
-00000590: 007c 00a0 00a1 0044 005d 067d 047c 04a0  .|.....D.].}.|..
-000005a0: 01a1 0001 0071 047c 0364 0119 00a0 01a1  .....q.|.d......
-000005b0: 0001 007c 0364 0219 00a0 01a1 0001 007c  ...|.d.........|
-000005c0: 0364 0319 00a0 01a1 0001 007c 0364 0419  .d.........|.d..
-000005d0: 00a0 01a1 0001 007c 01a0 01a1 0001 007c  .......|.......|
-000005e0: 02a0 01a1 0001 0064 0553 0029 0661 1701  .......d.S.).a..
-000005f0: 0000 0a20 2020 2043 6c65 616e 2075 7020  ...    Clean up 
-00000600: 6f75 7220 6d65 6d6f 7279 2068 6f67 730a  our memory hogs.
-00000610: 2020 2020 2020 2020 3a70 6172 616d 2074          :param t
-00000620: 7265 653a 2078 6d6c 2074 7265 6520 746f  ree: xml tree to
-00000630: 2065 6d70 7479 0a20 2020 2020 2020 203a   empty.        :
-00000640: 7061 7261 6d20 726f 6f74 3a20 726f 6f74  param root: root
-00000650: 2078 6d6c 2074 6861 7420 7761 7320 7061   xml that was pa
-00000660: 7273 6564 2066 726f 6d20 6261 636b 7570  rsed from backup
-00000670: 2066 696c 650a 2020 2020 2020 2020 3a70   file.        :p
-00000680: 6172 616d 206f 7574 7075 745f 6c69 7374  aram output_list
-00000690: 3a20 6c69 7374 206f 6620 6f75 7470 7574  : list of output
-000006a0: 206c 696e 6573 2074 6f20 636c 6561 720a   lines to clear.
-000006b0: 2020 2020 2020 2020 3a70 6172 616d 2061          :param a
-000006c0: 6c6c 5f74 6173 6b65 725f 6974 656d 733a  ll_tasker_items:
-000006d0: 2041 6c6c 2050 726f 6a65 6374 732f 5072   All Projects/Pr
-000006e0: 6f66 696c 6573 2f54 6173 6b73 2f53 6365  ofiles/Tasks/Sce
-000006f0: 6e65 730a 2020 2020 2020 2020 3a72 6574  nes.        :ret
-00000700: 7572 6e3a 0a20 2020 205a 0c61 6c6c 5f70  urn:.    Z.all_p
-00000710: 726f 6a65 6374 735a 0c61 6c6c 5f70 726f  rojectsZ.all_pro
-00000720: 6669 6c65 73da 0961 6c6c 5f74 6173 6b73  files..all_tasks
-00000730: 5a0a 616c 6c5f 7363 656e 6573 4e29 02da  Z.all_scenesN)..
-00000740: 0469 7465 72da 0563 6c65 6172 2905 721c  .iter..clear).r.
-00000750: 0000 0072 1d00 0000 721e 0000 0072 1f00  ...r....r....r..
-00000760: 0000 da04 656c 656d 7214 0000 0072 1400  ....elemr....r..
-00000770: 0000 7215 0000 00da 0f63 6c65 616e 5f75  ..r......clean_u
-00000780: 705f 6d65 6d6f 7279 6300 0000 7312 0000  p_memoryc...s...
-00000790: 000c 0e0a 010c 010c 010c 010c 0108 0108  ................
-000007a0: 0104 0172 2500 0000 da0d 6d79 5f6f 7574  ...r%.....my_out
-000007b0: 7075 745f 6469 72da 0c6d 795f 6669 6c65  put_dir..my_file
-000007c0: 5f6e 616d 6563 0300 0000 0000 0000 0000  _namec..........
-000007d0: 0000 0a00 0000 0800 0000 4300 0000 73c6  ..........C...s.
-000007e0: 0000 0074 00a0 0164 017c 019b 009d 02a1  ...t...d.|......
-000007f0: 0101 0074 027c 017c 0217 0064 0283 028f  ...t.|.|...d....
-00000800: 457d 037c 0044 005d 3a7d 047c 04a0 0364  E}.|.D.]:}.|...d
-00000810: 03a1 017d 057c 0564 046b 0372 457c 047c  ...}.|.d.k.rE|.|
-00000820: 0564 0517 0064 0685 0219 00a0 0464 07a1  .d...d.......d..
-00000830: 017d 067c 0664 0819 007d 077c 0464 067c  .}.|.d...}.|.d.|
-00000840: 0585 0219 007c 0717 0064 0917 007c 047c  .....|...d...|.|
-00000850: 0564 0517 0074 057c 0783 0117 0064 0685  .d...t.|.....d..
-00000860: 0219 0017 007d 087c 087d 096e 027c 047d  .....}.|.}.n.|.}
-00000870: 097c 03a0 067c 09a1 0101 0071 1257 0064  .|...|.....q.W.d
-00000880: 0604 0004 0083 0301 006e 0831 0073 5777  .........n.1.sWw
-00000890: 0101 0001 0001 0059 0001 0074 00a0 0164  .......Y...t...d
-000008a0: 0aa1 0101 0064 0653 0029 0b61 0c01 0000  .....d.S.).a....
-000008b0: 0a20 2020 2077 7269 7465 5f6f 7574 5f74  .    write_out_t
-000008c0: 6865 5f66 696c 653a 2077 6520 6861 7665  he_file: we have
-000008d0: 2061 206c 6973 7420 6f66 206f 7574 7075   a list of outpu
-000008e0: 7420 6c69 6e65 732e 2020 5772 6974 6520  t lines.  Write 
-000008f0: 7468 656d 206f 7574 2e0a 2020 2020 2020  them out..      
-00000900: 2020 3a70 6172 616d 206f 7574 7075 745f    :param output_
-00000910: 6c69 7374 3a20 6c69 7374 206f 6620 616c  list: list of al
-00000920: 6c20 6f75 7470 7574 206c 696e 6573 2067  l output lines g
-00000930: 656e 6572 6174 6564 0a20 2020 2020 2020  enerated.       
-00000940: 203a 7061 7261 6d20 6d79 5f6f 7574 7075   :param my_outpu
-00000950: 745f 6469 723a 2064 6972 6563 746f 7279  t_dir: directory
-00000960: 2074 6f20 6f75 7470 7574 2074 6f0a 2020   to output to.  
-00000970: 2020 2020 2020 3a70 6172 616d 206d 795f        :param my_
-00000980: 6669 6c65 5f6e 616d 653a 206e 616d 6520  file_name: name 
-00000990: 6f66 2066 696c 6520 746f 2075 7365 0a20  of file to use. 
-000009a0: 2020 2020 2020 203a 7265 7475 726e 3a20         :return: 
-000009b0: 6e6f 7468 696e 670a 2020 2020 7a27 4675  nothing.    z'Fu
-000009c0: 6e63 7469 6f6e 2045 6e74 7279 3a20 7772  nction Entry: wr
-000009d0: 6974 655f 6f75 745f 7468 655f 6669 6c65  ite_out_the_file
-000009e0: 2064 6972 3a72 1700 0000 7a08 4163 7469   dir:r....z.Acti
-000009f0: 6f6e 3a20 e9ff ffff ffe9 0800 0000 4efa  on: ..........N.
-00000a00: 0120 7201 0000 00fa 013a 7a21 4675 6e63  . r......:z!Func
-00000a10: 7469 6f6e 2045 7869 743a 2077 7269 7465  tion Exit: write
-00000a20: 5f6f 7574 5f74 6865 5f66 696c 6529 0772  _out_the_file).r
-00000a30: 0b00 0000 da04 696e 666f 7212 0000 00da  ......infor.....
-00000a40: 0466 696e 64da 0573 706c 6974 da03 6c65  .find..split..le
-00000a50: 6e72 1800 0000 290a 721e 0000 0072 2600  nr....).r....r&.
-00000a60: 0000 7227 0000 005a 086f 7574 5f66 696c  ..r'...Z.out_fil
-00000a70: 65da 0469 7465 6d5a 0f61 6374 696f 6e5f  e..itemZ.action_
-00000a80: 706f 7369 7469 6f6e 5a12 6163 7469 6f6e  positionZ.action
-00000a90: 5f6e 756d 6265 725f 6c69 7374 5a0d 6163  _number_listZ.ac
-00000aa0: 7469 6f6e 5f6e 756d 6265 725a 0474 656d  tion_numberZ.tem
-00000ab0: 705a 0b6f 7574 7075 745f 6c69 6e65 7214  pZ.output_liner.
-00000ac0: 0000 0072 1400 0000 7215 0000 00da 1277  ...r....r......w
-00000ad0: 7269 7465 5f6f 7574 5f74 6865 5f66 696c  rite_out_the_fil
-00000ae0: 657f 0000 0073 2c00 0000 100a 1001 0801  e....s,.........
-00000af0: 0a02 0801 1601 0801 0a02 0201 02ff 0202  ................
-00000b00: 02fe 1603 02fd 02ff 0606 0402 0c01 02f1  ................
-00000b10: 1cff 0a11 0401 7231 0000 00da 046e 616d  ......r1.....nam
-00000b20: 65da 1470 726f 6669 6c65 5f6f 725f 7461  e..profile_or_ta
-00000b30: 736b 5f6e 616d 6563 0600 0000 0000 0000  sk_namec........
-00000b40: 0000 0000 0700 0000 0500 0000 4300 0000  ............C...
-00000b50: 7346 0000 007c 04a0 00a1 0001 007c 009b  sF...|.......|..
-00000b60: 0064 017c 019b 0064 029d 047d 0674 017c  .d.|...d...}.t.|
-00000b70: 0683 0101 0074 02a0 037c 06a1 0101 0074  .....t...|.....t
-00000b80: 047c 027c 037c 047c 0583 0401 0074 05a0  .|.|.|.|.....t..
-00000b90: 0664 03a1 0101 0064 0453 0029 0561 e001  .d.....d.S.).a..
-00000ba0: 0000 0a20 2020 2043 6c65 616e 7570 206d  ...    Cleanup m
-00000bb0: 656d 6f72 7920 616e 6420 6c65 7420 7573  emory and let us
-00000bc0: 6572 206b 6e6f 7720 7468 6572 6520 7761  er know there wa
-00000bd0: 7320 6e6f 206d 6174 6368 2066 6f75 6e64  s no match found
-00000be0: 2066 6f72 2054 6173 6b2f 5072 6f66 696c   for Task/Profil
-00000bf0: 650a 2020 2020 2020 2020 3a70 6172 616d  e.        :param
-00000c00: 206e 616d 653a 2074 6865 206e 616d 6520   name: the name 
-00000c10: 746f 2061 6464 2074 6f20 7468 6520 6c6f  to add to the lo
-00000c20: 672f 7072 696e 7420 6f75 7470 7574 0a20  g/print output. 
-00000c30: 2020 2020 2020 203a 7061 7261 6d20 7072         :param pr
-00000c40: 6f66 696c 655f 6f72 5f74 6173 6b5f 6e61  ofile_or_task_na
-00000c50: 6d65 3a20 6e61 6d65 206f 6620 7468 6520  me: name of the 
-00000c60: 5072 6f66 696c 6520 6f72 2054 6173 6b20  Profile or Task 
-00000c70: 746f 2063 6c65 616e 0a20 2020 2020 2020  to clean.       
-00000c80: 203a 7061 7261 6d20 7472 6565 3a20 786d   :param tree: xm
-00000c90: 6c20 7472 6565 2074 6f20 636c 6561 720a  l tree to clear.
-00000ca0: 2020 2020 2020 2020 3a70 6172 616d 2072          :param r
-00000cb0: 6f6f 743a 2072 6f6f 7420 6f66 2078 6d6c  oot: root of xml
-00000cc0: 2070 6172 7365 6420 6672 6f6d 2066 696c   parsed from fil
-00000cd0: 6520 746f 2063 6c65 6172 0a20 2020 2020  e to clear.     
-00000ce0: 2020 203a 7061 7261 6d20 6f75 7470 7574     :param output
-00000cf0: 5f6c 6973 743a 206c 6973 7420 6f66 206f  _list: list of o
-00000d00: 7574 7075 7420 6c69 6e65 7320 746f 2065  utput lines to e
-00000d10: 6d70 7479 0a20 2020 2020 2020 203a 7061  mpty.        :pa
-00000d20: 7261 6d20 616c 6c5f 7461 736b 6572 5f69  ram all_tasker_i
-00000d30: 7465 6d73 3a20 616c 6c20 5461 736b 6572  tems: all Tasker
-00000d40: 2050 726f 6a65 6374 732f 5072 6f66 696c   Projects/Profil
-00000d50: 6573 2f54 6173 6b73 2f53 6365 6e65 7320  es/Tasks/Scenes 
-00000d60: 746f 2063 6c65 6172 0a20 2020 2020 2020  to clear.       
-00000d70: 203a 7274 7970 653a 206e 6f6e 650a 2020   :rtype: none.  
-00000d80: 2020 722a 0000 007a 0c20 6e6f 7420 666f    r*...z. not fo
-00000d90: 756e 6421 21e9 0500 0000 4e29 0772 2300  und!!.....N).r#.
-00000da0: 0000 da05 7072 696e 7472 0b00 0000 da05  ....printr......
-00000db0: 6465 6275 6772 2500 0000 da03 7379 73da  debugr%.....sys.
-00000dc0: 0465 7869 7429 0772 3200 0000 7233 0000  .exit).r2...r3..
-00000dd0: 0072 1c00 0000 721d 0000 0072 1e00 0000  .r....r....r....
-00000de0: 721f 0000 00da 0d65 7272 6f72 5f6d 6573  r......error_mes
-00000df0: 7361 6765 7214 0000 0072 1400 0000 7215  sager....r....r.
-00000e00: 0000 00da 1163 6c65 616e 5f75 705f 616e  .....clean_up_an
-00000e10: 645f 6578 6974 a200 0000 730c 0000 0008  d_exit....s.....
-00000e20: 1210 0108 010a 010e 010e 0172 3a00 0000  ...........r:...
-00000e30: 6300 0000 0000 0000 0000 0000 0013 0000  c...............
-00000e40: 000a 0000 0043 0000 0073 ec02 0000 6700  .....C...s....g.
-00000e50: 6700 6700 6700 6604 5c04 7d00 7d01 7d02  g.g.g.f.\.}.}.}.
-00000e60: 7d03 7400 a001 a100 5c04 7d04 7d05 7d06  }.t.....\.}.}.}.
-00000e70: 7d07 7c05 6401 1900 721c 7402 7c04 7c05  }.|.d...r.t.|.|.
-00000e80: 7c01 8303 0100 7403 6402 6b00 722a 6403  |.....t.d.k.r*d.
-00000e90: 7d08 6404 7d09 7404 a005 7c09 7c08 a102  }.d.}.t...|.|...
-00000ea0: 0100 7400 a006 7c05 a101 7d0a 7407 7c0a  ..t...|...}.t.|.
-00000eb0: 8301 5c03 7d0b 7d0c 7d0d 7c0c 6a08 6405  ..\.}.}.}.|.j.d.
-00000ec0: 6b03 7254 6406 7d0e 7409 a00a 7c04 7c05  k.rTd.}.t...|.|.
-00000ed0: 7c01 6407 7c0e a105 0100 740b a00c 7c0e  |.d.|.....t...|.
-00000ee0: 9b00 6408 9d02 a101 0100 740d a00e 6409  ..d.......t...d.
-00000ef0: a101 0100 6e0b 640a 7c07 9b00 640b 7c0c  ....n.d.|...d.|.
-00000f00: 6a0f 640c 1900 9b00 9d04 7d07 7409 a00a  j.d.......}.t...
-00000f10: 7c04 7c05 7c01 6407 7c07 a105 0100 7409  |.|.|.d.|.....t.
-00000f20: a00a 7c04 7c05 7c01 6402 640d a105 0100  ..|.|.|.d.d.....
-00000f30: 7c05 640e 1900 727c 7410 7c01 7c05 7c04  |.d...r|t.|.|.|.
-00000f40: 7c0d 8304 0100 7411 a012 7c01 7c00 7c02  |.....t...|.|.|.
-00000f50: 7c05 7c06 7c07 7c04 7c0d a108 7d00 7c05  |.|.|.|.|...}.|.
-00000f60: 640f 1900 729b 7c06 6410 1900 739b 7413  d...r.|.d...s.t.
-00000f70: 6411 7c05 640f 1900 7c0b 7c0c 7c01 7c0d  d.|.d...|.|.|.|.
-00000f80: 8306 0100 7c05 6412 1900 72ae 7c06 6413  ....|.d...r.|.d.
-00000f90: 1900 73ae 7413 6414 7c05 6412 1900 7c0b  ..s.t.d.|.d...|.
-00000fa0: 7c0c 7c01 7c0d 8306 0100 7c05 6415 1900  |.|.|.....|.d...
-00000fb0: 73d0 7c05 640f 1900 73d0 7c05 6412 1900  s.|.d...s.|.d...
-00000fc0: 73d0 7414 a015 7c01 7c03 7c00 7c05 7c06  s.t...|.|.|.|.|.
-00000fd0: 7c07 7c04 7c0d a108 0100 7414 a016 7c01  |.|.|.....t...|.
-00000fe0: 7c03 7c02 7c06 7c04 7c05 a106 0100 7c05  |.|.|.|.|.....|.
-00000ff0: 6415 1900 72f3 7c06 6416 1900 73f3 7c05  d...r.|.d...s.|.
-00001000: 6412 1900 72e0 7c06 6413 1900 72f3 7c05  d...r.|.d...r.|.
-00001010: 640f 1900 72e8 7c06 6410 1900 72f3 7413  d...r.|.d...r.t.
-00001020: 6417 7c05 6415 1900 7c0b 7c0c 7c01 7c0d  d.|.d...|.|.|.|.
-00001030: 8306 0100 7417 7c01 7c05 7c04 8303 0100  ....t.|.|.|.....
-00001040: 6418 7d0e 7409 a00a 7c04 7c05 7c01 6407  d.}.t...|.|.|.d.
-00001050: 7c0e a105 0100 7418 8300 7d0f 740b a00c  |.....t...}.t...
-00001060: 6419 7c0f 9b00 9d02 a101 0100 7c0f 6400  d.|.........|.d.
-00001070: 7500 9001 722b 641a 7d0e 740b a00c 7c0e  u...r+d.}.t...|.
-00001080: a101 0100 7419 7c0e 8301 0100 741a 7c0b  ....t.|.....t.|.
-00001090: 7c0c 7c01 7c0d 8304 0100 740d a00e 641b  |.|.|.....t...d.
-000010a0: a101 0100 641c 7d10 741b 7c01 7c0f 7c10  ....d.}.t.|.|.|.
-000010b0: 8303 0100 741a 7c0b 7c0c 7c01 7c0d 8304  ....t.|.|.|.|...
-000010c0: 0100 740b a00c 641d a101 0100 6407 7d11  ..t...d.....d.}.
-000010d0: 7a0e 741c 6a1d 641e 7c0f 9b00 7c10 9b00  z.t.j.d.|...|...
-000010e0: 9d03 641b 641f 8d02 0100 5700 6e20 0400  ..d.d.....W.n ..
-000010f0: 741e 9001 796f 0100 7d12 0100 7a13 6420  t...yo..}...z.d 
-00001100: 7d0e 7419 7c0e 8301 0100 740b a00c 7c0e  }.t.|.....t...|.
-00001110: a101 0100 6402 7d11 5700 5900 6400 7d12  ....d.}.W.Y.d.}.
-00001120: 7e12 6e05 6400 7d12 7e12 7701 7700 7419  ~.n.d.}.~.w.w.t.
-00001130: 6421 8301 0100 7c11 5300 2922 4e72 3600  d!....|.S.)"Nr6.
-00001140: 0000 7210 0000 007a 474c 6f63 6174 6520  ..r....zGLocate 
-00001150: 7468 6520 5461 736b 6572 2062 6163 6b75  the Tasker backu
-00001160: 7020 786d 6c20 6669 6c65 2074 6f20 7573  p xml file to us
-00001170: 6520 746f 206d 6170 2079 6f75 7220 5461  e to map your Ta
-00001180: 736b 6572 2065 6e76 6972 6f6e 6d65 6e74  sker environment
-00001190: 5a09 4d61 7054 6173 6b65 725a 0a54 6173  Z.MapTaskerZ.Tas
-000011a0: 6b65 7244 6174 617a 3459 6f75 2064 6964  kerDataz4You did
-000011b0: 206e 6f74 2073 656c 6563 7420 6120 5461   not select a Ta
-000011c0: 736b 6572 2062 6163 6b75 7020 584d 4c20  sker backup XML 
-000011d0: 6669 6c65 2e2e 2e65 7869 7420 3272 0100  file...exit 2r..
-000011e0: 0000 7a06 6578 6974 2033 e903 0000 007a  ..z.exit 3.....z
-000011f0: 203c 7370 616e 2073 7479 6c65 3d22 636f   <span style="co
-00001200: 6c6f 723a 4772 6565 6e22 3c2f 7370 616e  lor:Green"</span
-00001210: 3e7a 1420 2020 2054 6173 6b65 7220 7665  >z.    Tasker ve
-00001220: 7273 696f 6e3a 205a 0274 76da 005a 1364  rsion: Z.tv..Z.d
-00001230: 6973 706c 6179 5f70 7265 6665 7265 6e63  isplay_preferenc
-00001240: 6573 5a13 7369 6e67 6c65 5f70 726f 6a65  esZ.single_proje
-00001250: 6374 5f6e 616d 655a 1473 696e 676c 655f  ct_nameZ.single_
-00001260: 7072 6f6a 6563 745f 666f 756e 645a 0750  project_foundZ.P
-00001270: 726f 6a65 6374 5a13 7369 6e67 6c65 5f70  rojectZ.single_p
-00001280: 726f 6669 6c65 5f6e 616d 655a 1473 696e  rofile_nameZ.sin
-00001290: 676c 655f 7072 6f66 696c 655f 666f 756e  gle_profile_foun
-000012a0: 645a 0750 726f 6669 6c65 5a10 7369 6e67  dZ.ProfileZ.sing
-000012b0: 6c65 5f74 6173 6b5f 6e61 6d65 5a11 7369  le_task_nameZ.si
-000012c0: 6e67 6c65 5f74 6173 6b5f 666f 756e 64da  ngle_task_found.
-000012d0: 0454 6173 6b7a 0f3c 2f62 6f64 793e 0a3c  .Taskz.</body>.<
-000012e0: 2f68 746d 6c3e 7a11 6f75 7470 7574 2064  /html>z.output d
-000012f0: 6972 6563 746f 7279 3a7a 3c4d 6170 5461  irectory:z<MapTa
-00001300: 736b 6572 2063 616e 6365 6c6c 6564 2e20  sker cancelled. 
-00001310: 2041 6e20 6572 726f 7220 6f63 6375 7272   An error occurr
-00001320: 6564 2e20 2050 726f 6772 616d 2063 616e  ed.  Program can
-00001330: 6365 6c6c 6564 2ee9 0200 0000 7a0f 2f4d  celled......z./M
-00001340: 6170 5461 736b 6572 2e68 746d 6c7a 204d  apTasker.htmlz M
-00001350: 6170 5461 736b 6572 2070 726f 6772 616d  apTasker program
-00001360: 2065 6e64 6564 206e 6f72 6d61 6c6c 797a   ended normallyz
-00001370: 0766 696c 653a 2f2f 2901 da03 6e65 777a  .file://)...newz
-00001380: 4745 7272 6f72 3a20 4661 696c 6564 2074  GError: Failed t
-00001390: 6f20 6f70 656e 206f 7574 7075 7420 696e  o open output in
-000013a0: 2062 726f 7773 6572 3a20 796f 7572 2062   browser: your b
-000013b0: 726f 7773 6572 2069 7320 6e6f 7420 7375  rowser is not su
-000013c0: 7070 6f72 7465 642e 7a42 596f 7520 6361  pported.zBYou ca
-000013d0: 6e20 6669 6e64 2027 4d61 7054 6173 6b65  n find 'MapTaske
-000013e0: 722e 6874 6d6c 2720 696e 2074 6865 2063  r.html' in the c
-000013f0: 7572 7265 6e74 2066 6f6c 6465 722e 2020  urrent folder.  
-00001400: 5072 6f67 7261 6d20 656e 642e 291f da0a  Program end.)...
-00001410: 696e 6974 6961 6c69 7a65 5a08 7374 6172  initializeZ.star
-00001420: 745f 7570 720e 0000 0072 1900 0000 7206  t_upr....r....r.
-00001430: 0000 005a 0873 686f 7769 6e66 6f5a 1c6f  ...Z.showinfoZ.o
-00001440: 7065 6e5f 616e 645f 6765 745f 6261 636b  pen_and_get_back
-00001450: 7570 5f78 6d6c 5f66 696c 6572 0c00 0000  up_xml_filer....
-00001460: da03 7461 67da 0c62 7569 6c64 5f6f 7574  ..tag..build_out
-00001470: 7075 745a 096d 795f 6f75 7470 7574 720b  putZ.my_outputr.
-00001480: 0000 0072 3600 0000 7237 0000 0072 3800  ...r6...r7...r8.
-00001490: 0000 5a06 6174 7472 6962 720d 0000 00da  ..Z.attribr.....
-000014a0: 0870 726f 6a65 6374 735a 2370 726f 6365  .projectsZ#proce
-000014b0: 7373 5f70 726f 6a65 6374 735f 616e 645f  ss_projects_and_
-000014c0: 7468 6569 725f 7072 6f66 696c 6573 723a  their_profilesr:
-000014d0: 0000 00da 0d73 7065 6369 616c 5f74 6173  .....special_tas
-000014e0: 6b73 5a23 7072 6f63 6573 735f 7461 736b  ksZ#process_task
-000014f0: 735f 6e6f 745f 6361 6c6c 6564 5f62 795f  s_not_called_by_
-00001500: 7072 6f66 696c 655a 2270 726f 6365 7373  profileZ"process
-00001510: 5f6d 6973 7369 6e67 5f74 6173 6b73 5f61  _missing_tasks_a
-00001520: 6e64 5f70 726f 6669 6c65 7372 0900 0000  nd_profilesr....
-00001530: 7204 0000 0072 3500 0000 7225 0000 0072  r....r5...r%...r
-00001540: 3100 0000 da0a 7765 6262 726f 7773 6572  1.....webbrowser
-00001550: 7212 0000 00da 0945 7863 6570 7469 6f6e  r......Exception
-00001560: 2913 5a0b 666f 756e 645f 7461 736b 7372  ).Z.found_tasksr
-00001570: 1e00 0000 5a19 7072 6f6a 6563 7473 5f77  ....Z.projects_w
-00001580: 6974 686f 7574 5f70 726f 6669 6c65 735a  ithout_profilesZ
-00001590: 1670 726f 6a65 6374 735f 7769 7468 5f6e  .projects_with_n
-000015a0: 6f5f 7461 736b 735a 0863 6f6c 6f72 6d61  o_tasksZ.colorma
-000015b0: 705a 0c70 726f 6772 616d 5f61 7267 735a  pZ.program_argsZ
-000015c0: 0b66 6f75 6e64 5f69 7465 6d73 da07 6865  .found_items..he
-000015d0: 6164 696e 67da 036d 7367 da05 7469 746c  ading..msg..titl
-000015e0: 65da 0866 696c 656e 616d 6572 1c00 0000  e..filenamer....
-000015f0: 721d 0000 0072 1f00 0000 5a09 6572 726f  r....r....Z.erro
-00001600: 725f 6d73 6772 2600 0000 7227 0000 005a  r_msgr&...r'...Z
-00001610: 056d 795f 7263 da01 6572 1400 0000 7214  .my_rc..er....r.
-00001620: 0000 0072 1500 0000 da09 6d61 7069 745f  ...r......mapit_
-00001630: 616c 6cec 0000 0073 0801 0000 0203 0201  all....s........
-00001640: 0201 0201 0cfc 1008 080a 0c01 0802 0401  ................
-00001650: 0401 0c01 0a03 0e03 0a03 0401 1201 1001  ................
-00001660: 0c01 0803 0801 04ff 02ff 1206 1202 0805  ................
-00001670: 0201 0201 0201 0201 0201 04fc 040a 0201  ................
-00001680: 0201 0201 0201 0201 0201 0201 0201 04f8  ................
-00001690: 100c 0201 0201 0601 0201 0201 0201 0201  ................
-000016a0: 04fa 1009 0201 0201 0601 0201 0201 0201  ................
-000016b0: 0201 04fa 060d 02ff 0602 02fe 0603 02fd  ................
-000016c0: 0405 0201 0201 0201 0201 0201 0201 0201  ................
-000016d0: 0201 04f8 040e 0201 0201 0201 0201 0201  ................
-000016e0: 0201 04fa 060b 02ff 0602 02fe 0604 02fc  ................
-000016f0: 0605 02fb 0608 02f8 0609 02f7 020c 0201  ................
-00001700: 0601 0201 0201 0201 0201 04fa 0c0d 0403  ................
-00001710: 1201 0604 1001 0a01 0401 0a01 0801 0e01  ................
-00001720: 0a01 0402 0c02 0e03 0a03 0401 0201 1c01  ................
-00001730: 1001 0202 02ff 0803 0a01 1001 0880 02fa  ................
-00001740: 0807 0401 724c 0000 0029 37da 0661 7465  ....rL...)7..ate
-00001750: 7869 7472 3700 0000 7245 0000 005a 1578  xitr7...rE...Z.x
-00001760: 6d6c 2e65 7472 6565 2e45 6c65 6d65 6e74  ml.etree.Element
-00001770: 5472 6565 5a03 786d 6c5a 046a 736f 6e72  TreeZ.xmlZ.jsonr
-00001780: 0200 0000 7203 0000 00da 026f 7372 0400  ....r......osr..
-00001790: 0000 5a07 7061 7468 6c69 6272 0500 0000  ..Z.pathlibr....
-000017a0: 5a07 746b 696e 7465 7272 0600 0000 da06  Z.tkinterr......
-000017b0: 7479 7069 6e67 7207 0000 0072 0800 0000  typingr....r....
-000017c0: 5a15 6d61 7074 6173 6b65 722e 7372 632e  Z.maptasker.src.
-000017d0: 6f75 7470 7574 6cda 0373 7263 5a07 6f75  outputl..srcZ.ou
-000017e0: 7470 7574 6c72 4200 0000 5a16 6d61 7074  tputlrB...Z.mapt
-000017f0: 6173 6b65 722e 7372 632e 7072 6f67 696e  asker.src.progin
-00001800: 6974 5a08 7072 6f67 696e 6974 7240 0000  itZ.proginitr@..
-00001810: 005a 166d 6170 7461 736b 6572 2e73 7263  .Z.maptasker.src
-00001820: 2e70 726f 6a65 6374 7372 4300 0000 5a16  .projectsrC...Z.
-00001830: 6d61 7074 6173 6b65 722e 7372 632e 7461  maptasker.src.ta
-00001840: 736b 756e 6971 5a08 7461 736b 756e 6971  skuniqZ.taskuniq
-00001850: 7244 0000 005a 156d 6170 7461 736b 6572  rD...Z.maptasker
-00001860: 2e73 7263 2e63 6176 6561 7473 7209 0000  .src.caveatsr...
-00001870: 005a 166d 6170 7461 736b 6572 2e73 7263  .Z.maptasker.src
-00001880: 2e73 7973 636f 6e73 7472 0a00 0000 720b  .sysconstr....r.
-00001890: 0000 005a 156d 6170 7461 736b 6572 2e73  ...Z.maptasker.s
-000018a0: 7263 2e74 6173 6b65 7264 720c 0000 005a  rc.taskerdr....Z
-000018b0: 156d 6170 7461 736b 6572 2e73 7263 2e70  .maptasker.src.p
-000018c0: 7265 6665 7273 720d 0000 005a 136d 6170  refersr....Z.map
-000018d0: 7461 736b 6572 2e73 7263 2e64 6562 7567  tasker.src.debug
-000018e0: 720e 0000 0072 1600 0000 721b 0000 0072  r....r....r....r
-000018f0: 1900 0000 da08 7265 6769 7374 6572 5a05  ......registerZ.
-00001900: 6574 7265 655a 0b45 6c65 6d65 6e74 5472  etreeZ.ElementTr
-00001910: 6565 5a07 456c 656d 656e 74da 0373 7472  eeZ.Element..str
-00001920: 7225 0000 0072 3100 0000 da04 6c69 7374  r%...r1.....list
-00001930: da04 6469 6374 723a 0000 00da 0369 6e74  ..dictr:.....int
-00001940: 724c 0000 0072 1400 0000 7214 0000 0072  rL...r....r....r
-00001950: 1400 0000 7215 0000 00da 083c 6d6f 6475  ....r......<modu
-00001960: 6c65 3e01 0000 0073 7800 0000 0820 0801  le>....sx.... ..
-00001970: 0801 0801 1001 0c01 0c01 0c01 1001 1202  ................
-00001980: 1201 1201 1201 0c01 0c01 0c01 0c01 0c01  ................
-00001990: 0c01 080c 080f 060d 0a01 0206 0801 02ff  ................
-000019a0: 0802 02fe 0603 02fd 1404 02fc 0205 0afb  ................
-000019b0: 021c 0601 02ff 0201 02ff 0201 02ff 0202  ................
-000019c0: 0afe 0223 0201 02ff 0202 02fe 0403 02fd  ...#............
-000019d0: 0404 02fc 0205 02fb 0206 02fa 0207 0af9  ................
-000019e0: 021f 122b                                ...+
+00000040: 6401 6c02 5a03 6400 6402 6c04 6d05 5a05  d.l.Z.d.d.l.m.Z.
+00000050: 0100 6400 6403 6c06 6d07 5a07 6d08 5a08  ..d.d.l.m.Z.m.Z.
+00000060: 0100 6400 6401 6c09 6d0a 0200 0100 6d0b  ..d.d.l.m.....m.
+00000070: 5a0c 0100 6400 6401 6c0d 6d0a 0200 0100  Z...d.d.l.m.....
+00000080: 6d0e 5a0f 0100 6400 6401 6c10 6d0a 0200  m.Z...d.d.l.m...
+00000090: 0100 6d11 5a11 0100 6400 6401 6c12 6d0a  ..m.Z...d.d.l.m.
+000000a0: 0200 0100 6d13 5a14 0100 6400 6404 6c15  ....m.Z...d.d.l.
+000000b0: 6d16 5a16 0100 6400 6405 6c17 6d18 5a18  m.Z...d.d.l.m.Z.
+000000c0: 0100 6400 6406 6c19 6d1a 5a1a 0100 6407  ..d.d.l.m.Z...d.
+000000d0: 6503 6a1b 6a1c 6a1c 6408 6503 6a1b 6a1c  e.j.j.j.d.e.j.j.
+000000e0: 6a1d 6409 6507 651e 1900 640a 6508 651e  j.d.e.e...d.e.e.
+000000f0: 6507 6503 6a1b 6a1c 6a1d 1900 6602 1900  e.e.j.j.j...f...
+00000100: 640b 6401 660a 640c 640d 8404 5a1f 6409  d.d.f.d.d...Z.d.
+00000110: 6507 651e 1900 640e 651e 640f 651e 640b  e.e...d.e.d.e.d.
+00000120: 6401 6608 6410 6411 8404 5a20 6412 651e  d.f.d.d...Z d.e.
+00000130: 6413 651e 6407 6503 6a1b 6408 6503 6a1b  d.e.d.e.j.d.e.j.
+00000140: 6409 6521 640a 6522 640b 6401 660e 6414  d.e!d.e"d.d.f.d.
+00000150: 6415 8404 5a23 0900 640b 6524 6602 6416  d...Z#..d.e$f.d.
+00000160: 6417 8404 5a25 6401 5300 2918 e900 0000  d...Z%d.S.).....
+00000170: 004e 2901 da06 6765 7463 7764 2902 da04  .N)...getcwd)...
+00000180: 4c69 7374 da04 4469 6374 2901 da0f 6469  List..Dict)...di
+00000190: 7370 6c61 795f 6361 7665 6174 7329 01da  splay_caveats)..
+000001a0: 0f67 6574 5f70 7265 6665 7265 6e63 6573  .get_preferences
+000001b0: 2901 da06 6c6f 6767 6572 da04 7472 6565  )...logger..tree
+000001c0: da04 726f 6f74 da0b 6f75 7470 7574 5f6c  ..root..output_l
+000001d0: 6973 74da 1061 6c6c 5f74 6173 6b65 725f  ist..all_tasker_
+000001e0: 6974 656d 73da 0672 6574 7572 6e63 0400  items..returnc..
+000001f0: 0000 0000 0000 0000 0000 0500 0000 0300  ................
+00000200: 0000 4300 0000 735a 0000 007c 00a0 00a1  ..C...sZ...|....
+00000210: 0044 005d 067d 047c 04a0 01a1 0001 0071  .D.].}.|.......q
+00000220: 047c 0364 0119 00a0 01a1 0001 007c 0364  .|.d.........|.d
+00000230: 0219 00a0 01a1 0001 007c 0364 0319 00a0  .........|.d....
+00000240: 01a1 0001 007c 0364 0419 00a0 01a1 0001  .....|.d........
+00000250: 007c 01a0 01a1 0001 007c 02a0 01a1 0001  .|.......|......
+00000260: 0064 0553 0029 0661 1701 0000 0a20 2020  .d.S.).a.....   
+00000270: 2043 6c65 616e 2075 7020 6f75 7220 6d65   Clean up our me
+00000280: 6d6f 7279 2068 6f67 730a 2020 2020 2020  mory hogs.      
+00000290: 2020 3a70 6172 616d 2074 7265 653a 2078    :param tree: x
+000002a0: 6d6c 2074 7265 6520 746f 2065 6d70 7479  ml tree to empty
+000002b0: 0a20 2020 2020 2020 203a 7061 7261 6d20  .        :param 
+000002c0: 726f 6f74 3a20 726f 6f74 2078 6d6c 2074  root: root xml t
+000002d0: 6861 7420 7761 7320 7061 7273 6564 2066  hat was parsed f
+000002e0: 726f 6d20 6261 636b 7570 2066 696c 650a  rom backup file.
+000002f0: 2020 2020 2020 2020 3a70 6172 616d 206f          :param o
+00000300: 7574 7075 745f 6c69 7374 3a20 6c69 7374  utput_list: list
+00000310: 206f 6620 6f75 7470 7574 206c 696e 6573   of output lines
+00000320: 2074 6f20 636c 6561 720a 2020 2020 2020   to clear.      
+00000330: 2020 3a70 6172 616d 2061 6c6c 5f74 6173    :param all_tas
+00000340: 6b65 725f 6974 656d 733a 2041 6c6c 2050  ker_items: All P
+00000350: 726f 6a65 6374 732f 5072 6f66 696c 6573  rojects/Profiles
+00000360: 2f54 6173 6b73 2f53 6365 6e65 730a 2020  /Tasks/Scenes.  
+00000370: 2020 2020 2020 3a72 6574 7572 6e3a 0a20        :return:. 
+00000380: 2020 205a 0c61 6c6c 5f70 726f 6a65 6374     Z.all_project
+00000390: 735a 0c61 6c6c 5f70 726f 6669 6c65 735a  sZ.all_profilesZ
+000003a0: 0961 6c6c 5f74 6173 6b73 5a0a 616c 6c5f  .all_tasksZ.all_
+000003b0: 7363 656e 6573 4e29 02da 0469 7465 72da  scenesN)...iter.
+000003c0: 0563 6c65 6172 2905 7208 0000 0072 0900  .clear).r....r..
+000003d0: 0000 720a 0000 0072 0b00 0000 da04 656c  ..r....r......el
+000003e0: 656d a900 7210 0000 00fa 742f 5573 6572  em..r.....t/User
+000003f0: 732f 6d69 6b72 7562 696e 2f4c 6962 7261  s/mikrubin/Libra
+00000400: 7279 2f43 6c6f 7564 5374 6f72 6167 652f  ry/CloudStorage/
+00000410: 476f 6f67 6c65 4472 6976 652d 6d69 6b72  GoogleDrive-mikr
+00000420: 7562 696e 4067 6d61 696c 2e63 6f6d 2f4d  ubin@gmail.com/M
+00000430: 7920 4472 6976 652f 5079 7468 6f6e 2f6d  y Drive/Python/m
+00000440: 6170 7461 736b 6572 2f6d 6170 7461 736b  aptasker/maptask
+00000450: 6572 2f73 7263 2f6d 6170 6974 2e70 79da  er/src/mapit.py.
+00000460: 0f63 6c65 616e 5f75 705f 6d65 6d6f 7279  .clean_up_memory
+00000470: 3700 0000 7312 0000 000c 0e0a 010c 010c  7...s...........
+00000480: 010c 010c 0108 0108 0104 0172 1200 0000  ...........r....
+00000490: da0d 6d79 5f6f 7574 7075 745f 6469 72da  ..my_output_dir.
+000004a0: 0c6d 795f 6669 6c65 5f6e 616d 6563 0300  .my_file_namec..
+000004b0: 0000 0000 0000 0000 0000 0a00 0000 0800  ................
+000004c0: 0000 4300 0000 73c6 0000 0074 00a0 0164  ..C...s....t...d
+000004d0: 017c 019b 009d 02a1 0101 0074 027c 017c  .|.........t.|.|
+000004e0: 0217 0064 0283 028f 457d 037c 0044 005d  ...d....E}.|.D.]
+000004f0: 3a7d 047c 04a0 0364 03a1 017d 057c 0564  :}.|...d...}.|.d
+00000500: 046b 0372 457c 047c 0564 0517 0064 0685  .k.rE|.|.d...d..
+00000510: 0219 00a0 0464 07a1 017d 067c 0664 0819  .....d...}.|.d..
+00000520: 007d 077c 0464 067c 0585 0219 007c 0717  .}.|.d.|.....|..
+00000530: 0064 0917 007c 047c 0564 0517 0074 057c  .d...|.|.d...t.|
+00000540: 0783 0117 0064 0685 0219 0017 007d 087c  .....d.......}.|
+00000550: 087d 096e 027c 047d 097c 03a0 067c 09a1  .}.n.|.}.|...|..
+00000560: 0101 0071 1257 0064 0604 0004 0083 0301  ...q.W.d........
+00000570: 006e 0831 0073 5777 0101 0001 0001 0059  .n.1.sWw.......Y
+00000580: 0001 0074 00a0 0164 0aa1 0101 0064 0653  ...t...d.....d.S
+00000590: 0029 0b61 0c01 0000 0a20 2020 2077 7269  .).a.....    wri
+000005a0: 7465 5f6f 7574 5f74 6865 5f66 696c 653a  te_out_the_file:
+000005b0: 2077 6520 6861 7665 2061 206c 6973 7420   we have a list 
+000005c0: 6f66 206f 7574 7075 7420 6c69 6e65 732e  of output lines.
+000005d0: 2020 5772 6974 6520 7468 656d 206f 7574    Write them out
+000005e0: 2e0a 2020 2020 2020 2020 3a70 6172 616d  ..        :param
+000005f0: 206f 7574 7075 745f 6c69 7374 3a20 6c69   output_list: li
+00000600: 7374 206f 6620 616c 6c20 6f75 7470 7574  st of all output
+00000610: 206c 696e 6573 2067 656e 6572 6174 6564   lines generated
+00000620: 0a20 2020 2020 2020 203a 7061 7261 6d20  .        :param 
+00000630: 6d79 5f6f 7574 7075 745f 6469 723a 2064  my_output_dir: d
+00000640: 6972 6563 746f 7279 2074 6f20 6f75 7470  irectory to outp
+00000650: 7574 2074 6f0a 2020 2020 2020 2020 3a70  ut to.        :p
+00000660: 6172 616d 206d 795f 6669 6c65 5f6e 616d  aram my_file_nam
+00000670: 653a 206e 616d 6520 6f66 2066 696c 6520  e: name of file 
+00000680: 746f 2075 7365 0a20 2020 2020 2020 203a  to use.        :
+00000690: 7265 7475 726e 3a20 6e6f 7468 696e 670a  return: nothing.
+000006a0: 2020 2020 7a27 4675 6e63 7469 6f6e 2045      z'Function E
+000006b0: 6e74 7279 3a20 7772 6974 655f 6f75 745f  ntry: write_out_
+000006c0: 7468 655f 6669 6c65 2064 6972 3ada 0177  the_file dir:..w
+000006d0: 7a08 4163 7469 6f6e 3a20 e9ff ffff ffe9  z.Action: ......
+000006e0: 0800 0000 4efa 0120 7201 0000 00fa 013a  ....N.. r......:
+000006f0: 7a21 4675 6e63 7469 6f6e 2045 7869 743a  z!Function Exit:
+00000700: 2077 7269 7465 5f6f 7574 5f74 6865 5f66   write_out_the_f
+00000710: 696c 6529 0772 0700 0000 da04 696e 666f  ile).r......info
+00000720: da04 6f70 656e da04 6669 6e64 da05 7370  ..open..find..sp
+00000730: 6c69 74da 036c 656e da05 7772 6974 6529  lit..len..write)
+00000740: 0a72 0a00 0000 7213 0000 0072 1400 0000  .r....r....r....
+00000750: 5a08 6f75 745f 6669 6c65 da04 6974 656d  Z.out_file..item
+00000760: 5a0f 6163 7469 6f6e 5f70 6f73 6974 696f  Z.action_positio
+00000770: 6e5a 1261 6374 696f 6e5f 6e75 6d62 6572  nZ.action_number
+00000780: 5f6c 6973 745a 0d61 6374 696f 6e5f 6e75  _listZ.action_nu
+00000790: 6d62 6572 5a04 7465 6d70 5a0b 6f75 7470  mberZ.tempZ.outp
+000007a0: 7574 5f6c 696e 6572 1000 0000 7210 0000  ut_liner....r...
+000007b0: 0072 1100 0000 da12 7772 6974 655f 6f75  .r......write_ou
+000007c0: 745f 7468 655f 6669 6c65 5300 0000 732c  t_the_fileS...s,
+000007d0: 0000 0010 0a10 0108 010a 0208 0116 0108  ................
+000007e0: 010a 0202 0102 ff02 0202 fe16 0302 fd02  ................
+000007f0: ff06 0604 020c 0102 f11c ff0a 1104 0172  ...............r
+00000800: 2100 0000 da04 6e61 6d65 da14 7072 6f66  !.....name..prof
+00000810: 696c 655f 6f72 5f74 6173 6b5f 6e61 6d65  ile_or_task_name
+00000820: 6306 0000 0000 0000 0000 0000 0007 0000  c...............
+00000830: 0005 0000 0043 0000 0073 4600 0000 7c04  .....C...sF...|.
+00000840: a000 a100 0100 7c00 9b00 6401 7c01 9b00  ......|...d.|...
+00000850: 6402 9d04 7d06 7401 7c06 8301 0100 7402  d...}.t.|.....t.
+00000860: a003 7c06 a101 0100 7404 7c02 7c03 7c04  ..|.....t.|.|.|.
+00000870: 7c05 8304 0100 7405 a006 6403 a101 0100  |.....t...d.....
+00000880: 6404 5300 2905 61f6 0100 000a 2020 2020  d.S.).a.....    
+00000890: 436c 6561 6e75 7020 6d65 6d6f 7279 2061  Cleanup memory a
+000008a0: 6e64 206c 6574 2075 7365 7220 6b6e 6f77  nd let user know
+000008b0: 2074 6865 7265 2077 6173 206e 6f20 6d61   there was no ma
+000008c0: 7463 6820 666f 756e 6420 666f 7220 5461  tch found for Ta
+000008d0: 736b 2f50 726f 6669 6c65 0a20 2020 2020  sk/Profile.     
+000008e0: 2020 203a 7061 7261 6d20 6e61 6d65 3a20     :param name: 
+000008f0: 7468 6520 6e61 6d65 2074 6f20 6164 6420  the name to add 
+00000900: 746f 2074 6865 206c 6f67 2f70 7269 6e74  to the log/print
+00000910: 206f 7574 7075 740a 2020 2020 2020 2020   output.        
+00000920: 3a70 6172 616d 2070 726f 6669 6c65 5f6f  :param profile_o
+00000930: 725f 7461 736b 5f6e 616d 653a 206e 616d  r_task_name: nam
+00000940: 6520 6f66 2074 6865 2050 726f 6669 6c65  e of the Profile
+00000950: 206f 7220 5461 736b 2074 6f20 636c 6561   or Task to clea
+00000960: 6e0a 2020 2020 2020 2020 3a70 6172 616d  n.        :param
+00000970: 2074 7265 653a 2078 6d6c 2074 7265 6520   tree: xml tree 
+00000980: 746f 2063 6c65 6172 0a20 2020 2020 2020  to clear.       
+00000990: 203a 7061 7261 6d20 726f 6f74 3a20 726f   :param root: ro
+000009a0: 6f74 206f 6620 786d 6c20 7061 7273 6564  ot of xml parsed
+000009b0: 2066 726f 6d20 6669 6c65 2074 6f20 636c   from file to cl
+000009c0: 6561 720a 2020 2020 2020 2020 3a70 6172  ear.        :par
+000009d0: 616d 206f 7574 7075 745f 6c69 7374 3a20  am output_list: 
+000009e0: 6c69 7374 206f 6620 6f75 7470 7574 206c  list of output l
+000009f0: 696e 6573 2074 6f20 656d 7074 790a 2020  ines to empty.  
+00000a00: 2020 2020 2020 3a70 6172 616d 2061 6c6c        :param all
+00000a10: 5f74 6173 6b65 725f 6974 656d 733a 2061  _tasker_items: a
+00000a20: 6c6c 2054 6173 6b65 7220 5072 6f6a 6563  ll Tasker Projec
+00000a30: 7473 2f50 726f 6669 6c65 732f 5461 736b  ts/Profiles/Task
+00000a40: 732f 5363 656e 6573 2074 6f20 636c 6561  s/Scenes to clea
+00000a50: 720a 2020 2020 2020 2020 3a72 7479 7065  r.        :rtype
+00000a60: 3a20 636f 6c6f 7273 2c20 7275 6e74 696d  : colors, runtim
+00000a70: 6520 6172 6775 6d65 6e74 732c 0a20 2020  e arguments,.   
+00000a80: 2072 1800 0000 7a0c 206e 6f74 2066 6f75   r....z. not fou
+00000a90: 6e64 2121 e905 0000 004e 2907 720e 0000  nd!!.....N).r...
+00000aa0: 00da 0570 7269 6e74 7207 0000 00da 0564  ...printr......d
+00000ab0: 6562 7567 7212 0000 00da 0373 7973 da04  ebugr......sys..
+00000ac0: 6578 6974 2907 7222 0000 0072 2300 0000  exit).r"...r#...
+00000ad0: 7208 0000 0072 0900 0000 720a 0000 0072  r....r....r....r
+00000ae0: 0b00 0000 5a0d 6572 726f 725f 6d65 7373  ....Z.error_mess
+00000af0: 6167 6572 1000 0000 7210 0000 0072 1100  ager....r....r..
+00000b00: 0000 da11 636c 6561 6e5f 7570 5f61 6e64  ....clean_up_and
+00000b10: 5f65 7869 7476 0000 0073 0c00 0000 0813  _exitv...s......
+00000b20: 1001 0801 0a01 0e01 0e01 7229 0000 0063  ..........r)...c
+00000b30: 0000 0000 0000 0000 0000 0000 1100 0000  ................
+00000b40: 0a00 0000 4300 0000 7338 0200 0067 0067  ....C...s8...g.g
+00000b50: 0067 0067 0066 045c 047d 007d 017d 027d  .g.g.f.\.}.}.}.}
+00000b60: 0374 00a0 017c 01a1 015c 097d 047d 057d  .t...|...\.}.}.}
+00000b70: 067d 077d 017d 087d 097d 0a7d 0b7c 0564  .}.}.}.}.}.}.|.d
+00000b80: 0119 0072 2374 027c 017c 057c 047c 0b83  ...r#t.|.|.|.|..
+00000b90: 0401 0074 03a0 047c 017c 007c 027c 057c  ...t...|.|.|.|.|
+00000ba0: 067c 077c 047c 0ba1 087d 007c 0564 0219  .|.|.|...}.|.d..
+00000bb0: 0072 427c 0664 0319 0073 4274 0564 047c  .rB|.d...sBt.d.|
+00000bc0: 0564 0219 007c 087c 097c 017c 0b83 0601  .d...|.|.|.|....
+00000bd0: 007c 0564 0519 0072 557c 0664 0619 0073  .|.d...rU|.d...s
+00000be0: 5574 0564 077c 0564 0519 007c 087c 097c  Ut.d.|.d...|.|.|
+00000bf0: 017c 0b83 0601 007c 0564 0819 0073 777c  .|.....|.d...sw|
+00000c00: 0564 0219 0073 777c 0564 0519 0073 7774  .d...sw|.d...swt
+00000c10: 06a0 077c 017c 037c 007c 057c 067c 077c  ...|.|.|.|.|.|.|
+00000c20: 047c 0ba1 0801 0074 06a0 087c 017c 037c  .|.....t...|.|.|
+00000c30: 027c 067c 047c 05a1 0601 007c 0564 0819  .|.|.|.....|.d..
+00000c40: 0072 9a7c 0664 0919 0073 9a7c 0564 0519  .r.|.d...s.|.d..
+00000c50: 0072 877c 0664 0619 0072 9a7c 0564 0219  .r.|.d...r.|.d..
+00000c60: 0072 8f7c 0664 0319 0072 9a74 0564 0a7c  .r.|.d...r.t.d.|
+00000c70: 0564 0819 007c 087c 097c 017c 0b83 0601  .d...|.|.|.|....
+00000c80: 0074 097c 017c 057c 0483 0301 0064 0b7d  .t.|.|.|.....d.}
+00000c90: 0c74 0aa0 0b7c 047c 057c 0164 0c7c 0ca1  .t...|.|.|.d.|..
+00000ca0: 0501 0074 0c83 007d 0d74 0da0 0e64 0d7c  ...t...}.t...d.|
+00000cb0: 0d9b 009d 02a1 0101 007c 0d64 0075 0072  .........|.d.u.r
+00000cc0: d164 0e7d 0c74 0da0 0e7c 0ca1 0101 0074  .d.}.t...|.....t
+00000cd0: 0f7c 0c83 0101 0074 107c 087c 097c 017c  .|.....t.|.|.|.|
+00000ce0: 0b83 0401 0074 11a0 1264 0fa1 0101 0064  .....t...d.....d
+00000cf0: 107d 0e74 137c 017c 0d7c 0e83 0301 0074  .}.t.|.|.|.....t
+00000d00: 107c 087c 097c 017c 0b83 0401 0074 0da0  .|.|.|.|.....t..
+00000d10: 0e64 11a1 0101 0064 0c7d 0f7a 0e74 146a  .d.....d.}.z.t.j
+00000d20: 1564 127c 0d9b 007c 0e9b 009d 0364 0f64  .d.|...|.....d.d
+00000d30: 138d 0201 0057 006e 2004 0074 1690 0179  .....W.n ..t...y
+00000d40: 1501 007d 1001 007a 1364 147d 0c74 0f7c  ...}...z.d.}.t.|
+00000d50: 0c83 0101 0074 0da0 0e7c 0ca1 0101 0064  .....t...|.....d
+00000d60: 157d 0f57 0059 0064 007d 107e 106e 0564  .}.W.Y.d.}.~.n.d
+00000d70: 007d 107e 1077 0177 0074 0f64 1683 0101  .}.~.w.w.t.d....
+00000d80: 007c 0f53 0029 174e 5a13 6469 7370 6c61  .|.S.).NZ.displa
+00000d90: 795f 7072 6566 6572 656e 6365 735a 1373  y_preferencesZ.s
+00000da0: 696e 676c 655f 7072 6f6a 6563 745f 6e61  ingle_project_na
+00000db0: 6d65 5a14 7369 6e67 6c65 5f70 726f 6a65  meZ.single_proje
+00000dc0: 6374 5f66 6f75 6e64 5a07 5072 6f6a 6563  ct_foundZ.Projec
+00000dd0: 745a 1373 696e 676c 655f 7072 6f66 696c  tZ.single_profil
+00000de0: 655f 6e61 6d65 5a14 7369 6e67 6c65 5f70  e_nameZ.single_p
+00000df0: 726f 6669 6c65 5f66 6f75 6e64 5a07 5072  rofile_foundZ.Pr
+00000e00: 6f66 696c 655a 1073 696e 676c 655f 7461  ofileZ.single_ta
+00000e10: 736b 5f6e 616d 655a 1173 696e 676c 655f  sk_nameZ.single_
+00000e20: 7461 736b 5f66 6f75 6e64 5a04 5461 736b  task_foundZ.Task
+00000e30: 7a0f 3c2f 626f 6479 3e0a 3c2f 6874 6d6c  z.</body>.</html
+00000e40: 3e72 0100 0000 7a11 6f75 7470 7574 2064  >r....z.output d
+00000e50: 6972 6563 746f 7279 3a7a 3c4d 6170 5461  irectory:z<MapTa
+00000e60: 736b 6572 2063 616e 6365 6c6c 6564 2e20  sker cancelled. 
+00000e70: 2041 6e20 6572 726f 7220 6f63 6375 7272   An error occurr
+00000e80: 6564 2e20 2050 726f 6772 616d 2063 616e  ed.  Program can
+00000e90: 6365 6c6c 6564 2ee9 0200 0000 7a0f 2f4d  celled......z./M
+00000ea0: 6170 5461 736b 6572 2e68 746d 6c7a 204d  apTasker.htmlz M
+00000eb0: 6170 5461 736b 6572 2070 726f 6772 616d  apTasker program
+00000ec0: 2065 6e64 6564 206e 6f72 6d61 6c6c 797a   ended normallyz
+00000ed0: 0766 696c 653a 2f2f 2901 da03 6e65 777a  .file://)...newz
+00000ee0: 4745 7272 6f72 3a20 4661 696c 6564 2074  GError: Failed t
+00000ef0: 6f20 6f70 656e 206f 7574 7075 7420 696e  o open output in
+00000f00: 2062 726f 7773 6572 3a20 796f 7572 2062   browser: your b
+00000f10: 726f 7773 6572 2069 7320 6e6f 7420 7375  rowser is not su
+00000f20: 7070 6f72 7465 642e e901 0000 007a 4259  pported......zBY
+00000f30: 6f75 2063 616e 2066 696e 6420 274d 6170  ou can find 'Map
+00000f40: 5461 736b 6572 2e68 746d 6c27 2069 6e20  Tasker.html' in 
+00000f50: 7468 6520 6375 7272 656e 7420 666f 6c64  the current fold
+00000f60: 6572 2e20 2050 726f 6772 616d 2065 6e64  er.  Program end
+00000f70: 2e29 17da 0a69 6e69 7469 616c 697a 655a  .)...initializeZ
+00000f80: 0873 7461 7274 5f75 7072 0600 0000 da08  .start_upr......
+00000f90: 7072 6f6a 6563 7473 5a23 7072 6f63 6573  projectsZ#proces
+00000fa0: 735f 7072 6f6a 6563 7473 5f61 6e64 5f74  s_projects_and_t
+00000fb0: 6865 6972 5f70 726f 6669 6c65 7372 2900  heir_profilesr).
+00000fc0: 0000 da0d 7370 6563 6961 6c5f 7461 736b  ....special_task
+00000fd0: 735a 2370 726f 6365 7373 5f74 6173 6b73  sZ#process_tasks
+00000fe0: 5f6e 6f74 5f63 616c 6c65 645f 6279 5f70  _not_called_by_p
+00000ff0: 726f 6669 6c65 5a22 7072 6f63 6573 735f  rofileZ"process_
+00001000: 6d69 7373 696e 675f 7461 736b 735f 616e  missing_tasks_an
+00001010: 645f 7072 6f66 696c 6573 7205 0000 00da  d_profilesr.....
+00001020: 0c62 7569 6c64 5f6f 7574 7075 745a 096d  .build_outputZ.m
+00001030: 795f 6f75 7470 7574 7202 0000 0072 0700  y_outputr....r..
+00001040: 0000 7226 0000 0072 2500 0000 7212 0000  ..r&...r%...r...
+00001050: 0072 2700 0000 7228 0000 0072 2100 0000  .r'...r(...r!...
+00001060: da0a 7765 6262 726f 7773 6572 721b 0000  ..webbrowserr...
+00001070: 00da 0945 7863 6570 7469 6f6e 2911 5a0b  ...Exception).Z.
+00001080: 666f 756e 645f 7461 736b 7372 0a00 0000  found_tasksr....
+00001090: 5a19 7072 6f6a 6563 7473 5f77 6974 686f  Z.projects_witho
+000010a0: 7574 5f70 726f 6669 6c65 735a 1670 726f  ut_profilesZ.pro
+000010b0: 6a65 6374 735f 7769 7468 5f6e 6f5f 7461  jects_with_no_ta
+000010c0: 736b 735a 0863 6f6c 6f72 6d61 705a 0c70  sksZ.colormapZ.p
+000010d0: 726f 6772 616d 5f61 7267 735a 0b66 6f75  rogram_argsZ.fou
+000010e0: 6e64 5f69 7465 6d73 5a07 6865 6164 696e  nd_itemsZ.headin
+000010f0: 6772 0800 0000 7209 0000 00da 0866 696c  gr....r......fil
+00001100: 656e 616d 6572 0b00 0000 5a09 6572 726f  enamer....Z.erro
+00001110: 725f 6d73 6772 1300 0000 7214 0000 005a  r_msgr....r....Z
+00001120: 056d 795f 7263 da01 6572 1000 0000 7210  .my_rc..er....r.
+00001130: 0000 0072 1100 0000 da09 6d61 7069 745f  ...r......mapit_
+00001140: 616c 6cc1 0000 0073 f600 0000 0203 0201  all....s........
+00001150: 0201 0201 0cfc 0812 02f6 0201 0201 0201  ................
+00001160: 0201 0201 0201 0201 0201 0201 080d 0201  ................
+00001170: 0201 0201 0201 0201 04fc 040a 0201 0201  ................
+00001180: 0201 0201 0201 0201 0201 0201 04f8 100c  ................
+00001190: 0201 0201 0601 0201 0201 0201 0201 04fa  ................
+000011a0: 1009 0201 0201 0601 0201 0201 0201 0201  ................
+000011b0: 04fa 060d 02ff 0602 02fe 0603 02fd 0405  ................
+000011c0: 0201 0201 0201 0201 0201 0201 0201 0201  ................
+000011d0: 04f8 040e 0201 0201 0201 0201 0201 0201  ................
+000011e0: 04fa 060b 02ff 0602 02fe 0604 02fc 0605  ................
+000011f0: 02fb 0608 02f8 0609 02f7 020c 0201 0601  ................
+00001200: 0201 0201 0201 0201 04fa 0c0d 0403 1201  ................
+00001210: 0604 1001 0801 0401 0a01 0801 0e01 0a01  ................
+00001220: 0402 0c02 0e03 0a03 0401 0201 1c01 1001  ................
+00001230: 0202 02ff 0803 0a01 1001 0880 02fa 0807  ................
+00001240: 0401 7235 0000 0029 2672 2700 0000 7231  ..r5...)&r'...r1
+00001250: 0000 005a 1578 6d6c 2e65 7472 6565 2e45  ...Z.xml.etree.E
+00001260: 6c65 6d65 6e74 5472 6565 5a03 786d 6cda  lementTreeZ.xml.
+00001270: 026f 7372 0200 0000 da06 7479 7069 6e67  .osr......typing
+00001280: 7203 0000 0072 0400 0000 5a15 6d61 7074  r....r....Z.mapt
+00001290: 6173 6b65 722e 7372 632e 6f75 7470 7574  asker.src.output
+000012a0: 6cda 0373 7263 5a07 6f75 7470 7574 6c72  l..srcZ.outputlr
+000012b0: 3000 0000 5a16 6d61 7074 6173 6b65 722e  0...Z.maptasker.
+000012c0: 7372 632e 7072 6f67 696e 6974 5a08 7072  src.proginitZ.pr
+000012d0: 6f67 696e 6974 722d 0000 005a 166d 6170  oginitr-...Z.map
+000012e0: 7461 736b 6572 2e73 7263 2e70 726f 6a65  tasker.src.proje
+000012f0: 6374 7372 2e00 0000 5a16 6d61 7074 6173  ctsr....Z.maptas
+00001300: 6b65 722e 7372 632e 7461 736b 756e 6971  ker.src.taskuniq
+00001310: 5a08 7461 736b 756e 6971 722f 0000 005a  Z.taskuniqr/...Z
+00001320: 156d 6170 7461 736b 6572 2e73 7263 2e63  .maptasker.src.c
+00001330: 6176 6561 7473 7205 0000 005a 156d 6170  aveatsr....Z.map
+00001340: 7461 736b 6572 2e73 7263 2e70 7265 6665  tasker.src.prefe
+00001350: 7273 7206 0000 005a 166d 6170 7461 736b  rsr....Z.maptask
+00001360: 6572 2e73 7263 2e73 7973 636f 6e73 7472  er.src.sysconstr
+00001370: 0700 0000 5a05 6574 7265 655a 0b45 6c65  ....Z.etreeZ.Ele
+00001380: 6d65 6e74 5472 6565 5a07 456c 656d 656e  mentTreeZ.Elemen
+00001390: 74da 0373 7472 7212 0000 0072 2100 0000  t..strr....r!...
+000013a0: da04 6c69 7374 da04 6469 6374 7229 0000  ..list..dictr)..
+000013b0: 00da 0369 6e74 7235 0000 0072 1000 0000  ...intr5...r....
+000013c0: 7210 0000 0072 1000 0000 7211 0000 00da  r....r....r.....
+000013d0: 083c 6d6f 6475 6c65 3e01 0000 0073 6200  .<module>....sb.
+000013e0: 0000 0820 0801 0801 0c01 1001 1202 1201  ... ............
+000013f0: 1201 1201 0c01 0c01 0c01 020a 0801 02ff  ................
+00001400: 0802 02fe 0603 02fd 1404 02fc 0205 0afb  ................
+00001410: 021c 0601 02ff 0201 02ff 0201 02ff 0202  ................
+00001420: 0afe 0223 0201 02ff 0202 02fe 0403 02fd  ...#............
+00001430: 0404 02fc 0205 02fb 0206 02fa 0207 0af9  ................
+00001440: 0220 122b                                . .+
```

### Comparing `maptasker-1.3.1/maptasker/src/__pycache__/parsearg.cpython-310.pyc` & `maptasker-1.3.2/maptasker/src/__pycache__/parsearg.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Mon Mar  6 15:38:34 2023 UTC, .py size: 8092 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 fa08 0664 9c1f 0000  o..........d....
+00000000: 6f0d 0d0a 0000 0000 918f 1c64 9c1f 0000  o..........d....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0002 0000 0040 0000 0073 5400 0000 6400  .....@...sT...d.
 00000030: 6401 6c00 5a00 6400 6401 6c01 5a01 6400  d.l.Z.d.d.l.Z.d.
 00000040: 6402 6c00 6d02 5a02 0100 6400 6403 6c03  d.l.m.Z...d.d.l.
 00000050: 6d04 5a04 0100 6400 6404 6c05 6d06 5a06  m.Z...d.d.l.m.Z.
 00000060: 0100 6400 6405 6c05 6d07 5a07 0100 6406  ..d.d.l.m.Z...d.
 00000070: 6407 8400 5a08 6408 6409 8400 5a09 6401  d...Z.d.d...Z.d.
```

### Comparing `maptasker-1.3.1/maptasker/src/__pycache__/prefers.cpython-310.pyc` & `maptasker-1.3.2/maptasker/src/__pycache__/prefers.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 10 20:29:05 2023 UTC, .py size: 7224 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 22% similar despite different names*

```diff
@@ -1,236 +1,242 @@
-00000000: 6f0d 0d0a 0000 0000 1193 0b64 381c 0000  o..........d8...
+00000000: 6f0d 0d0a 0000 0000 51d7 2564 8e1c 0000  o.......Q.%d....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
-00000020: 000a 0000 0040 0000 0073 7400 0000 6400  .....@...st...d.
+00000020: 000a 0000 0040 0000 0073 8000 0000 6400  .....@...s....d.
 00000030: 6401 6c00 5a00 6400 6401 6c01 5a01 6400  d.l.Z.d.d.l.Z.d.
 00000040: 6402 6c02 6d03 5a03 0100 6400 6403 6c04  d.l.m.Z...d.d.l.
 00000050: 6d05 5a05 0100 6400 6404 6c06 6d07 5a07  m.Z...d.d.l.m.Z.
-00000060: 0100 6405 6508 6406 6509 6407 6509 6408  ..d.e.d.e.d.e.d.
-00000070: 650a 6409 6401 660a 640a 640b 8404 5a0b  e.d.d.f.d.d...Z.
-00000080: 640c 650a 640d 6508 6405 6508 640e 6508  d.e.d.e.d.e.d.e.
-00000090: 6409 6401 660a 640f 6410 8404 5a0c 6401  d.d.f.d.d...Z.d.
-000000a0: 5300 2911 e900 0000 004e 2901 da0a 6974  S.)......N)...it
-000000b0: 656d 6765 7474 6572 2901 da09 6d79 5f6f  emgetter)...my_o
-000000c0: 7574 7075 7429 01da 0d73 6572 7669 6365  utput)...service
-000000d0: 5f63 6f64 6573 da08 636f 6c6f 726d 6170  _codes..colormap
-000000e0: da0c 7365 7276 6963 655f 6e61 6d65 da0d  ..service_name..
-000000f0: 7365 7276 6963 655f 7661 6c75 65da 0c6f  service_value..o
-00000100: 7574 7075 745f 6c69 6e65 73da 0672 6574  utput_lines..ret
-00000110: 7572 6e63 0400 0000 0000 0000 0000 0000  urnc............
-00000120: 0c00 0000 0800 0000 4300 0000 7304 0100  ........C...s...
-00000130: 0064 017c 0064 0219 0017 0064 0317 007d  .d.|.d.....d...}
-00000140: 0464 047d 0574 007c 0119 0064 0519 007d  .d.}.t.|...d...}
-00000150: 067c 06a0 0164 0664 07a1 027d 0664 0874  .|...d.d...}.d.t
-00000160: 007c 0119 0076 0072 2674 007c 0119 0064  .|...v.r&t.|...d
-00000170: 0819 0074 027c 0283 0119 007d 027c 0264  ...t.|.....}.|.d
-00000180: 096b 0272 2d64 0a7d 026e 3a7c 0164 0b6b  .k.r-d.}.n:|.d.k
-00000190: 0272 6764 0c7d 0764 0d64 0e84 0074 03a0  .rgd.}.d.d...t..
-000001a0: 0464 0f7c 02a1 0244 0083 017d 0864 1064  .d.|...D...}.d.d
-000001b0: 0e84 0074 03a0 0464 117c 02a1 0244 0083  ...t...d.|...D..
-000001c0: 017d 0974 057c 0883 0144 005d 175c 027d  .}.t.|...D.].\.}
-000001d0: 0a7d 0b7c 079b 0064 127c 0564 1314 009b  .}.|...d.|.d....
-000001e0: 007c 027c 0b64 1417 007c 097c 0a19 0085  .|.|.d...|.|....
-000001f0: 0219 009b 009d 047d 0771 4d7c 077d 027c  .......}.qM|.}.|
-00000200: 03a0 0674 007c 0119 0064 1519 007c 049b  ...t.|...d...|..
-00000210: 007c 0564 1614 009b 007c 069b 007c 0564  .|.d.....|...|.d
-00000220: 1714 009b 007c 029b 009d 0567 02a1 0101  .....|.....g....
-00000230: 0064 1853 0029 1961 6c01 0000 0a20 2020  .d.S.).al....   
-00000240: 2057 6520 6861 7665 2061 2073 6572 7669   We have a servi
-00000250: 6365 2078 6d6c 2065 6c65 6d65 6e74 2074  ce xml element t
-00000260: 6861 7420 7765 2068 6176 6520 6d61 7070  hat we have mapp
-00000270: 6564 2061 7320 6120 7072 6566 6572 656e  ed as a preferen
-00000280: 6365 2e20 2050 726f 6365 7373 2069 742e  ce.  Process it.
-00000290: 0a20 2020 2020 2020 203a 7061 7261 6d20  .        :param 
-000002a0: 636f 6c6f 726d 6170 3a20 636f 6c6f 7273  colormap: colors
-000002b0: 2074 6f20 7573 6520 696e 206f 7574 7075   to use in outpu
-000002c0: 740a 2020 2020 2020 2020 3a70 6172 616d  t.        :param
-000002d0: 2073 6572 7669 6365 5f6e 616d 653a 206e   service_name: n
-000002e0: 616d 6520 6f66 2074 6865 2070 7265 6665  ame of the prefe
-000002f0: 7265 6e63 6520 696e 203c 5365 7276 6963  rence in <Servic
-00000300: 6520 786d 6c0a 2020 2020 2020 2020 3a70  e xml.        :p
-00000310: 6172 616d 2073 6572 7669 6365 5f76 616c  aram service_val
-00000320: 7565 3a20 7661 6c75 6520 6f66 2074 6865  ue: value of the
-00000330: 2070 7265 6665 7265 6e63 6520 696e 203c   preference in <
-00000340: 5365 7276 6963 6520 786d 6c0a 2020 2020  Service xml.    
-00000350: 2020 2020 3a70 6172 616d 206f 7574 7075      :param outpu
-00000360: 745f 6c69 6e65 733a 2061 6363 756d 756c  t_lines: accumul
-00000370: 6174 6564 206f 7574 7075 7420 6c69 6e65  ated output line
-00000380: 7320 6765 6e65 7261 7465 6420 7468 7573  s generated thus
-00000390: 2066 6172 2028 746f 2061 7070 656e 6420   far (to append 
-000003a0: 746f 290a 2020 2020 fa16 203c 7370 616e  to).    .. <span
-000003b0: 2073 7479 6c65 203d 2022 636f 6c6f 723a   style = "color:
-000003c0: da11 7072 6566 6572 656e 6365 735f 636f  ..preferences_co
-000003d0: 6c6f 72fa 0822 3c2f 7370 616e 3efa 0626  lor.."</span>..&
-000003e0: 6e62 7370 3bda 0764 6973 706c 6179 e92d  nbsp;..display.-
-000003f0: 0000 00da 012e da06 7661 6c75 6573 5a11  ........valuesZ.
-00000400: 6375 7374 5f6e 6f74 6966 6963 6174 696f  cust_notificatio
-00000410: 6e5a 0744 6566 6175 6c74 5a28 5052 4546  nZ.DefaultZ(PREF
-00000420: 5f4b 4545 505f 4143 4345 5353 4942 494c  _KEEP_ACCESSIBIL
-00000430: 4954 595f 5345 5256 4943 4553 5f52 554e  ITY_SERVICES_RUN
-00000440: 4e49 4e47 da00 6301 0000 0000 0000 0000  NING..c.........
-00000450: 0000 0002 0000 0004 0000 0053 0000 00f3  ...........S....
-00000460: 1400 0000 6700 7c00 5d06 7d01 7c01 a000  ....g.|.].}.|...
-00000470: a100 9102 7102 5300 a900 a901 da05 7374  ....q.S.......st
-00000480: 6172 74a9 02da 022e 30da 016d 7214 0000  art.....0..mr...
-00000490: 0072 1400 0000 fa76 2f55 7365 7273 2f6d  .r.....v/Users/m
-000004a0: 696b 7275 6269 6e2f 4c69 6272 6172 792f  ikrubin/Library/
-000004b0: 436c 6f75 6453 746f 7261 6765 2f47 6f6f  CloudStorage/Goo
-000004c0: 676c 6544 7269 7665 2d6d 696b 7275 6269  gleDrive-mikrubi
-000004d0: 6e40 676d 6169 6c2e 636f 6d2f 4d79 2044  n@gmail.com/My D
-000004e0: 7269 7665 2f50 7974 686f 6e2f 6d61 7074  rive/Python/mapt
-000004f0: 6173 6b65 722f 6d61 7074 6173 6b65 722f  asker/maptasker/
-00000500: 7372 632f 7072 6566 6572 732e 7079 da0a  src/prefers.py..
-00000510: 3c6c 6973 7463 6f6d 703e 3500 0000 f302  <listcomp>5.....
-00000520: 0000 0014 007a 2370 726f 6365 7373 5f73  .....z#process_s
-00000530: 6572 7669 6365 2e3c 6c6f 6361 6c73 3e2e  ervice.<locals>.
-00000540: 3c6c 6973 7463 6f6d 703e 7a0e 2270 6163  <listcomp>z."pac
-00000550: 6b61 6765 4e61 6d65 223a 6301 0000 0000  kageName":c.....
-00000560: 0000 0000 0000 0002 0000 0004 0000 0053  ...............S
-00000570: 0000 0072 1300 0000 7214 0000 0072 1500  ...r....r....r..
-00000580: 0000 7217 0000 0072 1400 0000 7214 0000  ..r....r....r...
-00000590: 0072 1a00 0000 721b 0000 0036 0000 0072  .r....r....6...r
-000005a0: 1c00 0000 da01 7dfa 043c 6272 3ee9 3200  ......}..<br>.2.
-000005b0: 0000 e90e 0000 00da 036e 756d e902 0000  .........num....
-000005c0: 00e9 0400 0000 4e29 0772 0400 0000 da05  ......N).r......
-000005d0: 6c6a 7573 74da 0369 6e74 da02 7265 da08  ljust..int..re..
-000005e0: 6669 6e64 6974 6572 da09 656e 756d 6572  finditer..enumer
-000005f0: 6174 65da 0661 7070 656e 6429 0c72 0500  ate..append).r..
-00000600: 0000 7206 0000 0072 0700 0000 7208 0000  ..r....r....r...
-00000610: 00da 1070 7265 6665 7265 6e63 6573 5f68  ...preferences_h
-00000620: 746d 6cda 0562 6c61 6e6b 5a13 6f75 7470  tml..blankZ.outp
-00000630: 7574 5f73 6572 7669 6365 5f6e 616d 655a  ut_service_nameZ
-00000640: 0d70 6163 6b61 6765 5f6e 616d 6573 5a08  .package_namesZ.
-00000650: 7061 636b 6167 6573 5a0c 7061 636b 6167  packagesZ.packag
-00000660: 6573 5f65 6e64 da06 6e75 6d62 6572 da08  es_end..number..
-00000670: 706f 7369 7469 6f6e 7214 0000 0072 1400  positionr....r..
-00000680: 0000 721a 0000 00da 0f70 726f 6365 7373  ..r......process
-00000690: 5f73 6572 7669 6365 1600 0000 732c 0000  _service....s,..
-000006a0: 000e 0b02 ff04 030c 030c 020c 0314 0108  ................
-000006b0: 0406 0108 0204 0116 0116 0110 0124 0204  .............$..
-000006c0: ff04 0304 030a 021e 0202 fd08 ff72 2e00  .............r..
-000006d0: 0000 da0b 6f75 7470 7574 5f6c 6973 74da  ....output_list.
-000006e0: 0c70 726f 6772 616d 5f61 7267 73da 1061  .program_args..a
-000006f0: 6c6c 5f74 6173 6b65 725f 6974 656d 7363  ll_tasker_itemsc
-00000700: 0400 0000 0000 0000 0000 0000 1300 0000  ................
-00000710: 0d00 0000 4300 0000 73b6 0100 0067 0064  ....C...s....g.d
-00000720: 01a2 017d 0467 007d 0564 027c 0264 0319  ...}.g.}.d.|.d..
-00000730: 0017 0064 0417 007d 0664 057d 0764 067d  ...d...}.d.}.d.}
-00000740: 0874 007c 027c 017c 0064 077c 069b 0064  .t.|.|.|.d.|...d
-00000750: 089d 0283 0501 0064 097d 0964 0a7d 0a7c  .......d.}.d.}.|
-00000760: 0364 0b19 0044 005d 4d7d 0b7c 0ba0 0164  .d...D.]M}.|...d
-00000770: 0ca1 016a 027d 0c7c 0ba0 0164 0da1 016a  ...j.}.|...d...j
-00000780: 027d 0d7c 0ba0 0164 0ea1 016a 027d 0e7c  .}.|...d...j.}.|
-00000790: 0c74 0376 0072 4574 047c 027c 0c7c 0e7c  .t.v.rEt.|.|.|.|
-000007a0: 0583 0401 0071 257c 0164 0f19 0072 727c  .....q%|.d...rr|
-000007b0: 0872 5464 107d 087c 05a0 057c 0a64 1167  .rTd.}.|...|.d.g
-000007c0: 02a1 0101 007c 05a0 057c 0a7c 069b 0064  .....|...|.|...d
-000007d0: 127c 0c9b 007c 0764 0714 009b 0064 137c  .|...|.d.....d.|
-000007e0: 0d9b 007c 0764 0714 009b 0064 147c 0e9b  ...|.d.....d.|..
-000007f0: 009d 0967 02a1 0101 007c 0a64 1537 007d  ...g.....|.d.7.}
-00000800: 0a71 2574 067c 0574 0764 1683 0164 178d  .q%t.|.t.d...d..
-00000810: 027d 0f7c 0f44 005d 417d 107c 1064 1619  .}.|.D.]A}.|.d..
-00000820: 007d 1174 03a0 08a1 0044 005d 2c7d 127c  .}.t.....D.],}.|
-00000830: 1264 1519 0064 1819 007c 116b 0272 b37c  .d...d...|.k.r.|
-00000840: 097c 1264 1519 0064 1919 006b 0372 b374  .|.d...d...k.r.t
-00000850: 007c 027c 017c 0064 0764 117c 069b 0064  .|.|.|.d.d.|...d
-00000860: 1a7c 047c 1264 1519 0064 1919 0019 009b  .|.|.d...d......
-00000870: 009d 0483 0501 007c 1264 1519 0064 1919  .......|.d...d..
-00000880: 007d 0971 8774 007c 027c 017c 0064 077c  .}.q.t.|.|.|.d.|
-00000890: 1064 1519 0083 0501 0071 7d74 007c 027c  .d.......q}t.|.|
-000008a0: 017c 0064 077c 069b 0064 1b9d 0283 0501  .|.d.|...d......
-000008b0: 0074 007c 027c 017c 0064 0764 1c83 0501  .t.|.|.|.d.d....
-000008c0: 007c 0364 0b3d 0074 09a0 0aa1 0001 0064  .|.d.=.t.......d
-000008d0: 1d53 0029 1e61 2b01 0000 0a20 2020 2047  .S.).a+....    G
-000008e0: 6574 2054 6173 6b65 7220 2770 7265 6665  et Tasker 'prefe
-000008f0: 7265 6e63 6573 2720 616e 6420 6f75 7470  rences' and outp
-00000900: 7574 2074 6865 6d0a 2020 2020 2020 2020  ut them.        
-00000910: 3a70 6172 616d 206f 7574 7075 745f 6c69  :param output_li
-00000920: 7374 3a20 6c69 7374 206f 6620 6f75 7470  st: list of outp
-00000930: 7574 206c 696e 6573 2067 656e 6572 6174  ut lines generat
-00000940: 6564 2074 6875 7320 6661 720a 2020 2020  ed thus far.    
-00000950: 2020 2020 3a70 6172 616d 2070 726f 6772      :param progr
-00000960: 616d 5f61 7267 733a 2072 756e 7469 6d65  am_args: runtime
-00000970: 2061 7267 756d 656e 7473 0a20 2020 2020   arguments.     
-00000980: 2020 203a 7061 7261 6d20 636f 6c6f 726d     :param colorm
-00000990: 6170 3a20 636f 6c6f 7273 2074 6f20 7573  ap: colors to us
-000009a0: 6520 696e 2070 7574 7075 740a 2020 2020  e in putput.    
-000009b0: 2020 2020 3a70 6172 616d 2061 6c6c 5f74      :param all_t
-000009c0: 6173 6b65 725f 6974 656d 733a 2061 6c6c  asker_items: all
-000009d0: 2050 726f 6a65 6374 2f50 726f 6669 6c65   Project/Profile
-000009e0: 2f54 6173 6b2f 5363 656e 652f 5365 7276  /Task/Scene/Serv
-000009f0: 6963 6520 786d 6c20 656c 656d 656e 7473  ice xml elements
-00000a00: 0a20 2020 2029 0e7a 0c55 4920 3e20 4765  .    ).z.UI > Ge
-00000a10: 6e65 7261 6c7a 1055 4920 3e20 4d61 696e  neralz.UI > Main
-00000a20: 2053 6372 6565 6e7a 0c55 4920 3e20 5549   Screenz.UI > UI
-00000a30: 204c 6f63 6b7a 1155 4920 3e20 4c6f 6361   Lockz.UI > Loca
-00000a40: 6c69 7a61 7469 6f6e 7a11 4d6f 6e69 746f  lizationz.Monito
-00000a50: 7220 3e20 4765 6e65 7261 6c7a 1f4d 6f6e  r > Generalz.Mon
-00000a60: 6974 6f72 203e 2044 6973 706c 6179 204f  itor > Display O
-00000a70: 6e20 4d6f 6e69 746f 7269 6e67 7a20 4d6f  n Monitoringz Mo
-00000a80: 6e69 746f 7220 3e20 4469 7370 6c61 7920  nitor > Display 
-00000a90: 4f66 6620 4d6f 6e69 746f 7269 6e67 7a1c  Off Monitoringz.
-00000aa0: 4d6f 6e69 746f 7220 3e20 4765 6e65 7261  Monitor > Genera
-00000ab0: 6c20 4d6f 6e69 746f 7269 6e67 7a13 4d6f  l Monitoringz.Mo
-00000ac0: 6e69 746f 7220 3e20 4361 6c69 6272 6174  nitor > Calibrat
-00000ad0: 65da 0641 6374 696f 6e7a 2241 6374 696f  e..Actionz"Actio
-00000ae0: 6e20 3e20 5265 7365 7420 4572 726f 7220  n > Reset Error 
-00000af0: 4e6f 7469 6669 6361 7469 6f6e 73da 044d  Notifications..M
-00000b00: 6973 637a 104d 6973 6320 3e20 4465 6275  iscz.Misc > Debu
-00000b10: 6767 696e 677a 1d55 6e6c 6973 7465 6420  ggingz.Unlisted 
-00000b20: 2850 6572 6861 7073 2044 6570 7265 6361  (Perhaps Depreca
-00000b30: 7465 6429 720a 0000 0072 0b00 0000 720c  ted)r....r....r.
-00000b40: 0000 0072 0d00 0000 5472 2300 0000 7a3b  ...r....Tr#...z;
-00000b50: 5461 736b 6572 2050 7265 6665 7265 6e63  Tasker Preferenc
-00000b60: 6573 203e 3e3e 3e3e 3e3e 3e3e 3e3e 3e3e  es >>>>>>>>>>>>>
-00000b70: 3e3e 3e3e 3e3e 3e3e 3e3e 3e3e 3e3e 3e3e  >>>>>>>>>>>>>>>>
-00000b80: 3e3e 3e3e 3e3e 3e3e 3e3e 3e69 e703 0000  >>>>>>>>>>>i....
-00000b90: e964 0000 00da 0c61 6c6c 5f73 6572 7669  .d.....all_servi
-00000ba0: 6365 73da 016e da01 74da 0176 da05 6465  ces..n..t..v..de
-00000bb0: 6275 6746 721e 0000 007a 1c26 6e62 7370  bugFr....z.&nbsp
-00000bc0: 3b26 6e62 7370 3b4e 6f74 2079 6574 206d  ;&nbsp;Not yet m
-00000bd0: 6170 7065 643a 207a 0574 7970 653a 7a06  apped: z.type:z.
-00000be0: 7661 6c75 653a e901 0000 0072 0100 0000  value:.....r....
-00000bf0: 2901 da03 6b65 7972 2100 0000 da07 7365  )...keyr!.....se
-00000c00: 6374 696f 6e7a 0f26 6e62 7370 3b53 6563  ctionz.&nbsp;Sec
-00000c10: 7469 6f6e 3a20 7a36 3c62 723e 266e 6273  tion: z6<br>&nbs
-00000c20: 703b 5468 6520 7265 6d61 696e 696e 6720  p;The remaining 
-00000c30: 7072 6566 6572 656e 6365 7320 6172 6520  preferences are 
-00000c40: 6e6f 7420 7965 7420 6d61 7070 6564 7212  not yet mappedr.
-00000c50: 0000 004e 290b 7203 0000 00da 0466 696e  ...N).r......fin
-00000c60: 64da 0474 6578 7472 0400 0000 722e 0000  d..textr....r...
-00000c70: 0072 2900 0000 da06 736f 7274 6564 7202  .r).....sortedr.
-00000c80: 0000 00da 0569 7465 6d73 da02 6763 5a07  .....items..gcZ.
-00000c90: 636f 6c6c 6563 7429 1372 2f00 0000 7230  collect).r/...r0
-00000ca0: 0000 0072 0500 0000 7231 0000 005a 0d73  ...r....r1...Z.s
-00000cb0: 6563 7469 6f6e 5f6e 616d 6573 7208 0000  ection_namesr...
-00000cc0: 0072 2a00 0000 722b 0000 005a 0a66 6972  .r*...r+...Z.fir
-00000cd0: 7374 5f74 696d 655a 0f63 7572 7265 6e74  st_timeZ.current
-00000ce0: 5f73 6563 7469 6f6e 5a09 6475 6d6d 795f  _sectionZ.dummy_
-00000cf0: 6e75 6d5a 0773 6572 7669 6365 7206 0000  numZ.servicer...
-00000d00: 005a 0c73 6572 7669 6365 5f74 7970 6572  .Z.service_typer
-00000d10: 0700 0000 5a0d 736f 7274 6564 5f6f 7574  ....Z.sorted_out
-00000d20: 7075 74da 046c 696e 6572 2100 0000 da04  put..liner!.....
-00000d30: 6974 656d 7214 0000 0072 1400 0000 721a  itemr....r....r.
-00000d40: 0000 00da 0f67 6574 5f70 7265 6665 7265  .....get_prefere
-00000d50: 6e63 6573 4800 0000 738c 0000 0008 0b04  ncesH...s.......
-00000d60: 100e 0202 ff04 0304 0102 0302 0102 0102  ................
-00000d70: 0102 0108 0204 fa04 0c04 010c 010c 010c  ................
-00000d80: 010c 0108 0210 0208 0304 0204 010e 0104  ................
-00000d90: 0202 0206 0202 0102 ff06 0104 ff02 0102  ................
-00000da0: ff06 0104 ff02 0104 ff02 fd04 ff08 0902  ................
-00000db0: 8010 0408 0308 020c 0220 0102 0202 0102  ......... ......
-00000dc0: 0102 0102 0108 020e 0104 ff04 fa0c 0a02  ................
-00000dd0: 8016 0102 0202 0102 0102 0102 0108 0104  ................
-00000de0: fb10 0706 0308 0104 0172 4400 0000 290d  .........rD...).
-00000df0: 7241 0000 0072 2600 0000 da08 6f70 6572  rA...r&.....oper
-00000e00: 6174 6f72 7202 0000 00da 156d 6170 7461  atorr......mapta
-00000e10: 736b 6572 2e73 7263 2e6f 7574 7075 746c  sker.src.outputl
-00000e20: 7203 0000 005a 166d 6170 7461 736b 6572  r....Z.maptasker
-00000e30: 2e73 7263 2e73 6572 7669 6365 6372 0400  .src.servicecr..
-00000e40: 0000 da04 6469 6374 da03 7374 72da 046c  ....dict..str..l
-00000e50: 6973 7472 2e00 0000 7244 0000 0072 1400  istr....rD...r..
-00000e60: 0000 7214 0000 0072 1400 0000 721a 0000  ..r....r....r...
-00000e70: 00da 083c 6d6f 6475 6c65 3e01 0000 0073  ...<module>....s
-00000e80: 3600 0000 080d 0801 0c01 0c02 0c01 0203  6...............
-00000e90: 0201 02ff 0201 02ff 0201 02ff 0201 02ff  ................
-00000ea0: 0202 0afe 0232 0201 02ff 0201 02ff 0201  .....2..........
-00000eb0: 02ff 0201 02ff 0202 0efe                 ..........
+00000060: 0100 6400 6405 6c08 6d09 5a09 0100 6406  ..d.d.l.m.Z...d.
+00000070: 650a 6407 650b 6408 650b 6409 650c 640a  e.d.e.d.e.d.e.d.
+00000080: 6401 660a 640b 640c 8404 5a0d 640d 650c  d.f.d.d...Z.d.e.
+00000090: 640e 650a 6406 650a 640f 650a 640a 6401  d.e.d.e.d.e.d.d.
+000000a0: 660a 6410 6411 8404 5a0e 6401 5300 2912  f.d.d...Z.d.S.).
+000000b0: e900 0000 004e 2901 da0a 6974 656d 6765  .....N)...itemge
+000000c0: 7474 6572 2901 da09 6d79 5f6f 7574 7075  tter)...my_outpu
+000000d0: 7429 01da 0d73 6572 7669 6365 5f63 6f64  t)...service_cod
+000000e0: 6573 2901 da0b 464f 4e54 5f54 4f5f 5553  es)...FONT_TO_US
+000000f0: 45da 0863 6f6c 6f72 6d61 70da 0c73 6572  E..colormap..ser
+00000100: 7669 6365 5f6e 616d 65da 0d73 6572 7669  vice_name..servi
+00000110: 6365 5f76 616c 7565 da0c 6f75 7470 7574  ce_value..output
+00000120: 5f6c 696e 6573 da06 7265 7475 726e 6304  _lines..returnc.
+00000130: 0000 0000 0000 0000 0000 000c 0000 0009  ................
+00000140: 0000 0043 0000 0073 0a01 0000 6401 7c00  ...C...s....d.|.
+00000150: 6402 1900 1700 7400 1700 6403 1700 7d04  d.....t...d...}.
+00000160: 6404 7d05 7401 7c01 1900 6405 1900 7d06  d.}.t.|...d...}.
+00000170: 7c06 a002 6406 6407 a102 7d06 6408 7401  |...d.d...}.d.t.
+00000180: 7c01 1900 7600 7228 7401 7c01 1900 6408  |...v.r(t.|...d.
+00000190: 1900 7403 7c02 8301 1900 7d02 7c02 6409  ..t.|.....}.|.d.
+000001a0: 6b02 722f 640a 7d02 6e3a 7c01 640b 6b02  k.r/d.}.n:|.d.k.
+000001b0: 7269 640c 7d07 640d 640e 8400 7404 a005  rid.}.d.d...t...
+000001c0: 640f 7c02 a102 4400 8301 7d08 6410 640e  d.|...D...}.d.d.
+000001d0: 8400 7404 a005 6411 7c02 a102 4400 8301  ..t...d.|...D...
+000001e0: 7d09 7406 7c08 8301 4400 5d17 5c02 7d0a  }.t.|...D.].\.}.
+000001f0: 7d0b 7c07 9b00 6412 7c05 6413 1400 9b00  }.|...d.|.d.....
+00000200: 7c02 7c0b 6414 1700 7c09 7c0a 1900 8502  |.|.d...|.|.....
+00000210: 1900 9b00 9d04 7d07 714f 7c07 7d02 7c03  ......}.qO|.}.|.
+00000220: a007 7401 7c01 1900 6415 1900 7c04 9b00  ..t.|...d...|...
+00000230: 7c05 6416 1400 9b00 7c06 9b00 7c05 6417  |.d.....|...|.d.
+00000240: 1400 9b00 7c02 9b00 6418 9d06 6702 a101  ....|...d...g...
+00000250: 0100 6419 5300 291a 616c 0100 000a 2020  ..d.S.).al....  
+00000260: 2020 5765 2068 6176 6520 6120 7365 7276    We have a serv
+00000270: 6963 6520 786d 6c20 656c 656d 656e 7420  ice xml element 
+00000280: 7468 6174 2077 6520 6861 7665 206d 6170  that we have map
+00000290: 7065 6420 6173 2061 2070 7265 6665 7265  ped as a prefere
+000002a0: 6e63 652e 2020 5072 6f63 6573 7320 6974  nce.  Process it
+000002b0: 2e0a 2020 2020 2020 2020 3a70 6172 616d  ..        :param
+000002c0: 2063 6f6c 6f72 6d61 703a 2063 6f6c 6f72   colormap: color
+000002d0: 7320 746f 2075 7365 2069 6e20 6f75 7470  s to use in outp
+000002e0: 7574 0a20 2020 2020 2020 203a 7061 7261  ut.        :para
+000002f0: 6d20 7365 7276 6963 655f 6e61 6d65 3a20  m service_name: 
+00000300: 6e61 6d65 206f 6620 7468 6520 7072 6566  name of the pref
+00000310: 6572 656e 6365 2069 6e20 3c53 6572 7669  erence in <Servi
+00000320: 6365 2078 6d6c 0a20 2020 2020 2020 203a  ce xml.        :
+00000330: 7061 7261 6d20 7365 7276 6963 655f 7661  param service_va
+00000340: 6c75 653a 2076 616c 7565 206f 6620 7468  lue: value of th
+00000350: 6520 7072 6566 6572 656e 6365 2069 6e20  e preference in 
+00000360: 3c53 6572 7669 6365 2078 6d6c 0a20 2020  <Service xml.   
+00000370: 2020 2020 203a 7061 7261 6d20 6f75 7470       :param outp
+00000380: 7574 5f6c 696e 6573 3a20 6163 6375 6d75  ut_lines: accumu
+00000390: 6c61 7465 6420 6f75 7470 7574 206c 696e  lated output lin
+000003a0: 6573 2067 656e 6572 6174 6564 2074 6875  es generated thu
+000003b0: 7320 6661 7220 2874 6f20 6170 7065 6e64  s far (to append
+000003c0: 2074 6f29 0a20 2020 20fa 1420 3c73 7061   to).    .. <spa
+000003d0: 6e20 7374 796c 653d 2263 6f6c 6f72 3ada  n style="color:.
+000003e0: 1170 7265 6665 7265 6e63 6573 5f63 6f6c  .preferences_col
+000003f0: 6f72 fa01 3efa 0626 6e62 7370 3bda 0764  or..>..&nbsp;..d
+00000400: 6973 706c 6179 e92d 0000 00da 012e da06  isplay.-........
+00000410: 7661 6c75 6573 5a11 6375 7374 5f6e 6f74  valuesZ.cust_not
+00000420: 6966 6963 6174 696f 6e5a 0744 6566 6175  ificationZ.Defau
+00000430: 6c74 5a28 5052 4546 5f4b 4545 505f 4143  ltZ(PREF_KEEP_AC
+00000440: 4345 5353 4942 494c 4954 595f 5345 5256  CESSIBILITY_SERV
+00000450: 4943 4553 5f52 554e 4e49 4e47 da00 6301  ICES_RUNNING..c.
+00000460: 0000 0000 0000 0000 0000 0002 0000 0004  ................
+00000470: 0000 0053 0000 00f3 1400 0000 6700 7c00  ...S........g.|.
+00000480: 5d06 7d01 7c01 a000 a100 9102 7102 5300  ].}.|.......q.S.
+00000490: a900 a901 da05 7374 6172 74a9 02da 022e  ......start.....
+000004a0: 30da 016d 7215 0000 0072 1500 0000 fa76  0..mr....r.....v
+000004b0: 2f55 7365 7273 2f6d 696b 7275 6269 6e2f  /Users/mikrubin/
+000004c0: 4c69 6272 6172 792f 436c 6f75 6453 746f  Library/CloudSto
+000004d0: 7261 6765 2f47 6f6f 676c 6544 7269 7665  rage/GoogleDrive
+000004e0: 2d6d 696b 7275 6269 6e40 676d 6169 6c2e  -mikrubin@gmail.
+000004f0: 636f 6d2f 4d79 2044 7269 7665 2f50 7974  com/My Drive/Pyt
+00000500: 686f 6e2f 6d61 7074 6173 6b65 722f 6d61  hon/maptasker/ma
+00000510: 7074 6173 6b65 722f 7372 632f 7072 6566  ptasker/src/pref
+00000520: 6572 732e 7079 da0a 3c6c 6973 7463 6f6d  ers.py..<listcom
+00000530: 703e 3600 0000 f302 0000 0014 007a 2370  p>6..........z#p
+00000540: 726f 6365 7373 5f73 6572 7669 6365 2e3c  rocess_service.<
+00000550: 6c6f 6361 6c73 3e2e 3c6c 6973 7463 6f6d  locals>.<listcom
+00000560: 703e 7a0e 2270 6163 6b61 6765 4e61 6d65  p>z."packageName
+00000570: 223a 6301 0000 0000 0000 0000 0000 0002  ":c.............
+00000580: 0000 0004 0000 0053 0000 0072 1400 0000  .......S...r....
+00000590: 7215 0000 0072 1600 0000 7218 0000 0072  r....r....r....r
+000005a0: 1500 0000 7215 0000 0072 1b00 0000 721c  ....r....r....r.
+000005b0: 0000 0037 0000 0072 1d00 0000 da01 7dfa  ...7...r......}.
+000005c0: 043c 6272 3ee9 3200 0000 e90e 0000 00da  .<br>.2.........
+000005d0: 036e 756d e902 0000 00e9 0400 0000 fa07  .num............
+000005e0: 3c2f 7370 616e 3e4e 2908 7205 0000 0072  </span>N).r....r
+000005f0: 0400 0000 da05 6c6a 7573 74da 0369 6e74  ......ljust..int
+00000600: da02 7265 da08 6669 6e64 6974 6572 da09  ..re..finditer..
+00000610: 656e 756d 6572 6174 65da 0661 7070 656e  enumerate..appen
+00000620: 6429 0c72 0600 0000 7207 0000 0072 0800  d).r....r....r..
+00000630: 0000 7209 0000 00da 1070 7265 6665 7265  ..r......prefere
+00000640: 6e63 6573 5f68 746d 6cda 0562 6c61 6e6b  nces_html..blank
+00000650: 5a13 6f75 7470 7574 5f73 6572 7669 6365  Z.output_service
+00000660: 5f6e 616d 655a 0d70 6163 6b61 6765 5f6e  _nameZ.package_n
+00000670: 616d 6573 5a08 7061 636b 6167 6573 5a0c  amesZ.packagesZ.
+00000680: 7061 636b 6167 6573 5f65 6e64 da06 6e75  packages_end..nu
+00000690: 6d62 6572 da08 706f 7369 7469 6f6e 7215  mber..positionr.
+000006a0: 0000 0072 1500 0000 721b 0000 00da 0f70  ...r....r......p
+000006b0: 726f 6365 7373 5f73 6572 7669 6365 1700  rocess_service..
+000006c0: 0000 732c 0000 0012 0b02 ff04 030c 030c  ..s,............
+000006d0: 020c 0314 0108 0406 0108 0204 0116 0116  ................
+000006e0: 0110 0124 0204 ff04 0304 030a 0220 0202  ...$......... ..
+000006f0: fd08 ff72 3000 0000 da0b 6f75 7470 7574  ...r0.....output
+00000700: 5f6c 6973 74da 0c70 726f 6772 616d 5f61  _list..program_a
+00000710: 7267 73da 1061 6c6c 5f74 6173 6b65 725f  rgs..all_tasker_
+00000720: 6974 656d 7363 0400 0000 0000 0000 0000  itemsc..........
+00000730: 0000 1300 0000 0e00 0000 4300 0000 73be  ..........C...s.
+00000740: 0100 0067 0064 01a2 017d 0467 007d 0564  ...g.d...}.g.}.d
+00000750: 027c 0264 0319 0017 0074 0017 0064 0417  .|.d.....t...d..
+00000760: 007d 0664 057d 0764 067d 0874 017c 027c  .}.d.}.d.}.t.|.|
+00000770: 017c 0064 077c 069b 0064 089d 0283 0501  .|.d.|...d......
+00000780: 0064 097d 0964 0a7d 0a7c 0364 0b19 0044  .d.}.d.}.|.d...D
+00000790: 005d 4e7d 0b7c 0ba0 0264 0ca1 016a 037d  .]N}.|...d...j.}
+000007a0: 0c7c 0ba0 0264 0da1 016a 037d 0d7c 0ba0  .|...d...j.}.|..
+000007b0: 0264 0ea1 016a 037d 0e7c 0c74 0476 0072  .d...j.}.|.t.v.r
+000007c0: 4774 057c 027c 0c7c 0e7c 0583 0401 0071  Gt.|.|.|.|.....q
+000007d0: 277c 0164 0f19 0072 757c 0872 5664 107d  '|.d...ru|.rVd.}
+000007e0: 087c 05a0 067c 0a64 1167 02a1 0101 007c  .|...|.d.g.....|
+000007f0: 05a0 067c 0a7c 069b 0064 127c 0c9b 007c  ...|.|...d.|...|
+00000800: 0764 0714 009b 0064 137c 0d9b 007c 0764  .d.....d.|...|.d
+00000810: 0714 009b 0064 147c 0e9b 0064 159d 0a67  .....d.|...d...g
+00000820: 02a1 0101 007c 0a64 1637 007d 0a71 2774  .....|.d.7.}.q't
+00000830: 077c 0574 0864 1783 0164 188d 027d 0f7c  .|.t.d...d...}.|
+00000840: 0f44 005d 427d 107c 1064 1719 007d 1174  .D.]B}.|.d...}.t
+00000850: 04a0 09a1 0044 005d 2d7d 127c 1264 1619  .....D.]-}.|.d..
+00000860: 0064 1919 007c 116b 0272 b77c 097c 1264  .d...|.k.r.|.|.d
+00000870: 1619 0064 1a19 006b 0372 b774 017c 027c  ...d...k.r.t.|.|
+00000880: 017c 0064 0764 117c 069b 0064 1b7c 047c  .|.d.d.|...d.|.|
+00000890: 1264 1619 0064 1a19 0019 009b 0064 159d  .d...d.......d..
+000008a0: 0583 0501 007c 1264 1619 0064 1a19 007d  .....|.d...d...}
+000008b0: 0971 8a74 017c 027c 017c 0064 077c 1064  .q.t.|.|.|.d.|.d
+000008c0: 1619 0083 0501 0071 8074 017c 027c 017c  .......q.t.|.|.|
+000008d0: 0064 077c 069b 0064 1c9d 0283 0501 0074  .d.|...d.......t
+000008e0: 017c 027c 017c 0064 0764 1d83 0501 007c  .|.|.|.d.d.....|
+000008f0: 0364 0b3d 0074 0aa0 0ba1 0001 0064 1e53  .d.=.t.......d.S
+00000900: 0029 1f61 2b01 0000 0a20 2020 2047 6574  .).a+....    Get
+00000910: 2054 6173 6b65 7220 2770 7265 6665 7265   Tasker 'prefere
+00000920: 6e63 6573 2720 616e 6420 6f75 7470 7574  nces' and output
+00000930: 2074 6865 6d0a 2020 2020 2020 2020 3a70   them.        :p
+00000940: 6172 616d 206f 7574 7075 745f 6c69 7374  aram output_list
+00000950: 3a20 6c69 7374 206f 6620 6f75 7470 7574  : list of output
+00000960: 206c 696e 6573 2067 656e 6572 6174 6564   lines generated
+00000970: 2074 6875 7320 6661 720a 2020 2020 2020   thus far.      
+00000980: 2020 3a70 6172 616d 2070 726f 6772 616d    :param program
+00000990: 5f61 7267 733a 2072 756e 7469 6d65 2061  _args: runtime a
+000009a0: 7267 756d 656e 7473 0a20 2020 2020 2020  rguments.       
+000009b0: 203a 7061 7261 6d20 636f 6c6f 726d 6170   :param colormap
+000009c0: 3a20 636f 6c6f 7273 2074 6f20 7573 6520  : colors to use 
+000009d0: 696e 2070 7574 7075 740a 2020 2020 2020  in putput.      
+000009e0: 2020 3a70 6172 616d 2061 6c6c 5f74 6173    :param all_tas
+000009f0: 6b65 725f 6974 656d 733a 2061 6c6c 2050  ker_items: all P
+00000a00: 726f 6a65 6374 2f50 726f 6669 6c65 2f54  roject/Profile/T
+00000a10: 6173 6b2f 5363 656e 652f 5365 7276 6963  ask/Scene/Servic
+00000a20: 6520 786d 6c20 656c 656d 656e 7473 0a20  e xml elements. 
+00000a30: 2020 2029 0e7a 0c55 4920 3e20 4765 6e65     ).z.UI > Gene
+00000a40: 7261 6c7a 1055 4920 3e20 4d61 696e 2053  ralz.UI > Main S
+00000a50: 6372 6565 6e7a 0c55 4920 3e20 5549 204c  creenz.UI > UI L
+00000a60: 6f63 6b7a 1155 4920 3e20 4c6f 6361 6c69  ockz.UI > Locali
+00000a70: 7a61 7469 6f6e 7a11 4d6f 6e69 746f 7220  zationz.Monitor 
+00000a80: 3e20 4765 6e65 7261 6c7a 1f4d 6f6e 6974  > Generalz.Monit
+00000a90: 6f72 203e 2044 6973 706c 6179 204f 6e20  or > Display On 
+00000aa0: 4d6f 6e69 746f 7269 6e67 7a20 4d6f 6e69  Monitoringz Moni
+00000ab0: 746f 7220 3e20 4469 7370 6c61 7920 4f66  tor > Display Of
+00000ac0: 6620 4d6f 6e69 746f 7269 6e67 7a1c 4d6f  f Monitoringz.Mo
+00000ad0: 6e69 746f 7220 3e20 4765 6e65 7261 6c20  nitor > General 
+00000ae0: 4d6f 6e69 746f 7269 6e67 7a13 4d6f 6e69  Monitoringz.Moni
+00000af0: 746f 7220 3e20 4361 6c69 6272 6174 65da  tor > Calibrate.
+00000b00: 0641 6374 696f 6e7a 2241 6374 696f 6e20  .Actionz"Action 
+00000b10: 3e20 5265 7365 7420 4572 726f 7220 4e6f  > Reset Error No
+00000b20: 7469 6669 6361 7469 6f6e 73da 044d 6973  tifications..Mis
+00000b30: 637a 104d 6973 6320 3e20 4465 6275 6767  cz.Misc > Debugg
+00000b40: 696e 677a 1d55 6e6c 6973 7465 6420 2850  ingz.Unlisted (P
+00000b50: 6572 6861 7073 2044 6570 7265 6361 7465  erhaps Deprecate
+00000b60: 6429 720b 0000 0072 0c00 0000 720d 0000  d)r....r....r...
+00000b70: 0072 0e00 0000 5472 2400 0000 7a42 5461  .r....Tr$...zBTa
+00000b80: 736b 6572 2050 7265 6665 7265 6e63 6573  sker Preferences
+00000b90: 203e 3e3e 3e3e 3e3e 3e3e 3e3e 3e3e 3e3e   >>>>>>>>>>>>>>>
+00000ba0: 3e3e 3e3e 3e3e 3e3e 3e3e 3e3e 3e3e 3e3e  >>>>>>>>>>>>>>>>
+00000bb0: 3e3e 3e3e 3e3e 3e3e 3e3c 2f73 7061 6e3e  >>>>>>>>></span>
+00000bc0: 69e7 0300 00e9 6400 0000 da0c 616c 6c5f  i.....d.....all_
+00000bd0: 7365 7276 6963 6573 da01 6eda 0174 da01  services..n..t..
+00000be0: 76da 0564 6562 7567 4672 1f00 0000 7a1c  v..debugFr....z.
+00000bf0: 266e 6273 703b 266e 6273 703b 4e6f 7420  &nbsp;&nbsp;Not 
+00000c00: 7965 7420 6d61 7070 6564 3a20 7a05 7479  yet mapped: z.ty
+00000c10: 7065 3a7a 0676 616c 7565 3a72 2500 0000  pe:z.value:r%...
+00000c20: e901 0000 0072 0100 0000 2901 da03 6b65  .....r....)...ke
+00000c30: 7972 2200 0000 da07 7365 6374 696f 6e7a  yr".....sectionz
+00000c40: 0f26 6e62 7370 3b53 6563 7469 6f6e 3a20  .&nbsp;Section: 
+00000c50: 7a36 3c62 723e 266e 6273 703b 5468 6520  z6<br>&nbsp;The 
+00000c60: 7265 6d61 696e 696e 6720 7072 6566 6572  remaining prefer
+00000c70: 656e 6365 7320 6172 6520 6e6f 7420 7965  ences are not ye
+00000c80: 7420 6d61 7070 6564 7213 0000 004e 290c  t mappedr....N).
+00000c90: 7205 0000 0072 0300 0000 da04 6669 6e64  r....r......find
+00000ca0: da04 7465 7874 7204 0000 0072 3000 0000  ..textr....r0...
+00000cb0: 722b 0000 00da 0673 6f72 7465 6472 0200  r+.....sortedr..
+00000cc0: 0000 da05 6974 656d 73da 0267 635a 0763  ....items..gcZ.c
+00000cd0: 6f6c 6c65 6374 2913 7231 0000 0072 3200  ollect).r1...r2.
+00000ce0: 0000 7206 0000 0072 3300 0000 5a0d 7365  ..r....r3...Z.se
+00000cf0: 6374 696f 6e5f 6e61 6d65 7372 0900 0000  ction_namesr....
+00000d00: 722c 0000 0072 2d00 0000 5a0a 6669 7273  r,...r-...Z.firs
+00000d10: 745f 7469 6d65 5a0f 6375 7272 656e 745f  t_timeZ.current_
+00000d20: 7365 6374 696f 6e5a 0964 756d 6d79 5f6e  sectionZ.dummy_n
+00000d30: 756d 5a07 7365 7276 6963 6572 0700 0000  umZ.servicer....
+00000d40: 5a0c 7365 7276 6963 655f 7479 7065 7208  Z.service_typer.
+00000d50: 0000 005a 0d73 6f72 7465 645f 6f75 7470  ...Z.sorted_outp
+00000d60: 7574 da04 6c69 6e65 7222 0000 00da 0469  ut..liner".....i
+00000d70: 7465 6d72 1500 0000 7215 0000 0072 1b00  temr....r....r..
+00000d80: 0000 da0f 6765 745f 7072 6566 6572 656e  ....get_preferen
+00000d90: 6365 7349 0000 0073 8c00 0000 080b 0410  cesI...s........
+00000da0: 1202 02ff 0403 0401 0203 0201 0201 0201  ................
+00000db0: 0201 0802 04fa 040c 0401 0c01 0c01 0c01  ................
+00000dc0: 0c01 0802 1002 0803 0402 0401 0e01 0402  ................
+00000dd0: 0202 0602 0201 02ff 0601 04ff 0201 02ff  ................
+00000de0: 0601 04ff 0201 06ff 02fd 04ff 0809 0280  ................
+00000df0: 1004 0803 0802 0c02 2001 0202 0201 0201  ........ .......
+00000e00: 0201 0201 0802 0e01 06ff 04fa 0c0a 0280  ................
+00000e10: 1601 0202 0201 0201 0201 0201 0801 04fb  ................
+00000e20: 1007 0603 0801 0401 7246 0000 0029 0f72  ........rF...).r
+00000e30: 4300 0000 7228 0000 00da 086f 7065 7261  C...r(.....opera
+00000e40: 746f 7272 0200 0000 da15 6d61 7074 6173  torr......maptas
+00000e50: 6b65 722e 7372 632e 6f75 7470 7574 6c72  ker.src.outputlr
+00000e60: 0300 0000 5a16 6d61 7074 6173 6b65 722e  ....Z.maptasker.
+00000e70: 7372 632e 7365 7276 6963 6563 7204 0000  src.servicecr...
+00000e80: 00da 166d 6170 7461 736b 6572 2e73 7263  ...maptasker.src
+00000e90: 2e73 7973 636f 6e73 7472 0500 0000 da04  .sysconstr......
+00000ea0: 6469 6374 da03 7374 72da 046c 6973 7472  dict..str..listr
+00000eb0: 3000 0000 7246 0000 0072 1500 0000 7215  0...rF...r....r.
+00000ec0: 0000 0072 1500 0000 721b 0000 00da 083c  ...r....r......<
+00000ed0: 6d6f 6475 6c65 3e01 0000 0073 3800 0000  module>....s8...
+00000ee0: 080d 0801 0c01 0c02 0c01 0c01 0203 0201  ................
+00000ef0: 02ff 0201 02ff 0201 02ff 0201 02ff 0202  ................
+00000f00: 0afe 0232 0201 02ff 0201 02ff 0201 02ff  ...2............
+00000f10: 0201 02ff 0202 0efe                      ........
```

### Comparing `maptasker-1.3.1/maptasker/src/__pycache__/priority.cpython-310.pyc` & `maptasker-1.3.2/maptasker/src/__pycache__/priority.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Sun Feb 26 20:27:39 2023 UTC, .py size: 1649 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 3% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 bbc0 fb63 7106 0000  o..........cq...
+00000000: 6f0d 0d0a 0000 0000 918f 1c64 7106 0000  o..........dq...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 2400 0000 6400  .....@...s$...d.
 00000030: 6401 6c00 5a01 6402 6501 6a02 6403 6503  d.l.Z.d.e.j.d.e.
 00000040: 6404 6504 6606 6405 6406 8404 5a05 6401  d.e.f.d.d...Z.d.
 00000050: 5300 2907 e900 0000 004e da07 656c 656d  S.)......N..elem
 00000060: 656e 74da 0565 7665 6e74 da06 7265 7475  ent..event..retu
 00000070: 726e 6302 0000 0000 0000 0000 0000 0003  rnc.............
```

### Comparing `maptasker-1.3.1/maptasker/src/__pycache__/proclist.cpython-310.pyc` & `maptasker-1.3.2/maptasker/src/__pycache__/proclist.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 17 18:33:26 2023 UTC, .py size: 4386 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 6% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 76b2 1464 2211 0000  o.......v..d"...
+00000000: 6f0d 0d0a 0000 0000 c424 2b64 5012 0000  o........$+dP...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0012 0000 0040 0000 0073 6c00 0000 6400  .....@...sl...d.
 00000030: 6401 6c00 5a01 6400 6402 6c02 6d03 5a03  d.l.Z.d.d.l.m.Z.
 00000040: 0100 6400 6403 6c04 6d05 5a05 0100 6400  ..d.d.l.m.Z...d.
 00000050: 6404 6c06 6d07 5a07 0100 6400 6405 6c06  d.l.m.Z...d.d.l.
 00000060: 6d08 5a08 0100 6406 6509 6407 650a 6408  m.Z...d.e.d.e.d.
 00000070: 650a 6409 6501 6a0b 640a 650a 640b 650c  e.d.e.j.d.e.d.e.
@@ -17,114 +17,115 @@
 00000100: 5f6c 6973 74da 0874 6865 5f6c 6973 74da  _list..the_list.
 00000110: 0874 6865 5f74 6173 6bda 0b74 6173 6b73  .the_task..tasks
 00000120: 5f66 6f75 6e64 da0c 7072 6f67 7261 6d5f  _found..program_
 00000130: 6172 6773 da08 636f 6c6f 726d 6170 da10  args..colormap..
 00000140: 616c 6c5f 7461 736b 6572 5f69 7465 6d73  all_tasker_items
 00000150: da06 7265 7475 726e 6308 0000 0000 0000  ..returnc.......
 00000160: 0000 0000 000e 0000 000b 0000 0043 0000  .............C..
-00000170: 0073 1201 0000 6401 6402 6c00 6d01 7d08  .s....d.d.l.m.}.
-00000180: 0100 7402 7c02 8301 4400 5d7c 5c02 7d09  ..t.|...D.]|\.}.
+00000170: 0073 1c01 0000 6401 6402 6c00 6d01 7d08  .s....d.d.l.m.}.
+00000180: 0100 7402 7c02 8301 4400 5d81 5c02 7d09  ..t.|...D.].\.}.
 00000190: 7d0a 6403 7d0b 6403 7d0c 7c05 6404 1900  }.d.}.d.}.|.d...
-000001a0: 7227 7403 a004 6405 7405 7c0a 8301 9b00  r't...d.t.|.....
+000001a0: 7226 7403 a004 6405 7405 7c0a 8301 9b00  r&t...d.t.|.....
 000001b0: 6406 7c02 9b00 6407 7c00 9b00 9d06 a101  d.|...d.|.......
-000001c0: 0100 6e19 6408 7c00 7600 7240 7c0a 7d0b  ..n.d.|.v.r@|.}.
-000001d0: 7c00 7d0c 6403 7d0a 7c00 a006 6409 a101  |.}.d.}.|...d...
-000001e0: 7d0d 7c0d 640a 6b03 7240 7c00 640b 7c0d  }.|.d.k.r@|.d.|.
-000001f0: 8502 1900 7d00 7407 7c06 7c05 7c01 640c  ....}.t.|.|.|.d.
-00000200: 7c00 9b00 640d 7c0a 9b00 9d03 8305 0100  |...d.|.........
-00000210: 7c0b 7253 7c0b 7d0a 7c0c 7d00 7c03 725d  |.rS|.}.|.}.|.r]
-00000220: 640e 7c00 7600 725d 7408 7c0a 7600 7361  d.|.v.r]t.|.v.sa
-00000230: 640e 7c00 7600 7273 640f 7c0a 7601 7273  d.|.v.rsd.|.v.rs
-00000240: 7409 7c03 7c01 7c05 7c00 7c0a 7c04 7c06  t.|.|.|.|.|.|.|.
-00000250: 7c07 6410 1900 8308 0100 710a 7c00 6411  |.d.......q.|.d.
-00000260: 6b02 7286 7c05 6412 1900 6413 6b04 7286  k.r.|.d...d.k.r.
-00000270: 7c08 7c0a 7c01 7c04 7c05 7c06 7c07 8306  |.|.|.|.|.|.|...
-00000280: 0100 710a 640b 5300 2914 6129 0200 000a  ..q.d.S.).a)....
-00000290: 2020 2020 5072 6f63 6573 7320 5461 736b      Process Task
-000002a0: 2f53 6365 6e65 2074 6578 742f 6c69 6e65  /Scene text/line
-000002b0: 2069 7465 6d3a 2063 616c 6c20 7265 6375   item: call recu
-000002c0: 7273 6976 656c 7920 666f 7220 5461 736b  rsively for Task
-000002d0: 7320 7769 7468 696e 2053 6365 6e65 730a  s within Scenes.
-000002e0: 2020 2020 2020 2020 3a70 6172 616d 206c          :param l
-000002f0: 6973 745f 7479 7065 3a20 5461 736b 206f  ist_type: Task o
-00000300: 7220 5363 656e 650a 2020 2020 2020 2020  r Scene.        
-00000310: 3a70 6172 616d 206f 7574 7075 745f 6c69  :param output_li
-00000320: 7374 3a20 6c69 7374 206f 6620 6f75 7470  st: list of outp
-00000330: 7574 206c 696e 6573 0a20 2020 2020 2020  ut lines.       
-00000340: 203a 7061 7261 6d20 7468 655f 6c69 7374   :param the_list
-00000350: 3a20 6c69 7374 206f 6620 5461 736b 206e  : list of Task n
-00000360: 616d 6573 2074 726f 2070 726f 6365 7373  ames tro process
-00000370: 0a20 2020 2020 2020 203a 7061 7261 6d20  .        :param 
-00000380: 7468 655f 7461 736b 3a20 5461 736b 2f53  the_task: Task/S
-00000390: 6365 6e65 2078 6d6c 2065 6c65 6d65 6e74  cene xml element
-000003a0: 0a20 2020 2020 2020 203a 7061 7261 6d20  .        :param 
-000003b0: 7461 736b 735f 666f 756e 643a 206c 6973  tasks_found: lis
-000003c0: 7420 6f66 2054 6173 6b73 2066 6f75 6e64  t of Tasks found
-000003d0: 2073 6f20 6661 720a 2020 2020 2020 2020   so far.        
-000003e0: 3a70 6172 616d 2070 726f 6772 616d 5f61  :param program_a
-000003f0: 7267 733a 2064 6963 7469 6f6e 6172 7920  rgs: dictionary 
-00000400: 6f66 2072 756e 7469 6d65 2061 7267 756d  of runtime argum
-00000410: 656e 7473 0a20 2020 2020 2020 203a 7061  ents.        :pa
-00000420: 7261 6d20 636f 6c6f 726d 6170 3a20 6469  ram colormap: di
-00000430: 6374 696f 6e61 7279 206f 6620 636f 6c6f  ctionary of colo
-00000440: 7273 2074 6f20 7573 650a 2020 2020 2020  rs to use.      
-00000450: 2020 3a70 6172 616d 2061 6c6c 5f74 6173    :param all_tas
-00000460: 6b65 725f 6974 656d 733a 2064 6963 7469  ker_items: dicti
-00000470: 6f6e 6172 7920 6f66 2061 6c6c 2054 6173  onary of all Tas
-00000480: 6b65 7220 5072 6f6a 6563 7473 2f50 726f  ker Projects/Pro
-00000490: 6669 6c65 732f 5461 736b 732f 5363 656e  files/Tasks/Scen
-000004a0: 6573 0a20 2020 2020 2020 203a 7265 7475  es.        :retu
-000004b0: 726e 3a0a 2020 2020 7201 0000 0029 01da  rn:.    r....)..
-000004c0: 0d70 726f 6365 7373 5f73 6365 6e65 da00  .process_scene..
-000004d0: da05 6465 6275 677a 1770 726f 6365 7373  ..debugz.process
-000004e0: 5f6c 6973 7420 2074 6865 5f69 7465 6d3a  _list  the_item:
-000004f0: 7a0a 2074 6865 5f6c 6973 743a 7a0b 206c  z. the_list:z. l
-00000500: 6973 745f 7479 7065 3a75 0800 0000 e28e  ist_type:u......
-00000510: af54 6173 6b3a 7a03 4944 3ae9 ffff ffff  .Task:z.ID:.....
-00000520: 4ee9 0200 0000 7a06 266e 6273 703b 7a05  N.....z.&nbsp;z.
-00000530: 5461 736b 3a7a 0e3c 656d 3e4e 6f20 5072  Task:z.<em>No Pr
-00000540: 6f66 696c 65da 0961 6c6c 5f74 6173 6b73  ofile..all_tasks
-00000550: 7a06 5363 656e 653a da14 6469 7370 6c61  z.Scene:..displa
-00000560: 795f 6465 7461 696c 5f6c 6576 656c e901  y_detail_level..
-00000570: 0000 0029 0ada 146d 6170 7461 736b 6572  ...)...maptasker
-00000580: 2e73 7263 2e73 6365 6e65 7372 0f00 0000  .src.scenesr....
-00000590: da09 656e 756d 6572 6174 6572 0400 0000  ..enumerater....
-000005a0: 7211 0000 00da 0373 7472 da04 6669 6e64  r......str..find
-000005b0: 7202 0000 0072 0500 0000 7203 0000 0029  r....r....r....)
-000005c0: 0e72 0600 0000 7207 0000 0072 0800 0000  .r....r....r....
-000005d0: 7209 0000 0072 0a00 0000 720b 0000 0072  r....r....r....r
-000005e0: 0c00 0000 720d 0000 0072 0f00 0000 5a08  ....r....r....Z.
-000005f0: 6d79 5f63 6f75 6e74 da08 7468 655f 6974  my_count..the_it
-00000600: 656d 5a09 7465 6d70 5f69 7465 6d5a 0974  emZ.temp_itemZ.t
-00000610: 656d 705f 6c69 7374 5a06 6964 5f6c 6f63  emp_listZ.id_loc
-00000620: a900 721c 0000 00fa 772f 5573 6572 732f  ..r.....w/Users/
-00000630: 6d69 6b72 7562 696e 2f4c 6962 7261 7279  mikrubin/Library
-00000640: 2f43 6c6f 7564 5374 6f72 6167 652f 476f  /CloudStorage/Go
-00000650: 6f67 6c65 4472 6976 652d 6d69 6b72 7562  ogleDrive-mikrub
-00000660: 696e 4067 6d61 696c 2e63 6f6d 2f4d 7920  in@gmail.com/My 
-00000670: 4472 6976 652f 5079 7468 6f6e 2f6d 6170  Drive/Python/map
-00000680: 7461 736b 6572 2f6d 6170 7461 736b 6572  tasker/maptasker
-00000690: 2f73 7263 2f70 726f 636c 6973 742e 7079  /src/proclist.py
-000006a0: da0c 7072 6f63 6573 735f 6c69 7374 1a00  ..process_list..
-000006b0: 0000 736a 0000 000c 1810 0304 0104 0108  ..sj............
-000006c0: 0104 0102 0106 0104 ff02 0104 ff02 0104  ................
-000006d0: ff06 ff08 0404 0104 0104 010a 0108 010c  ................
-000006e0: 0102 0314 0104 ff04 0304 0104 0102 0602  ................
-000006f0: ff10 0108 0108 0102 0102 0102 0102 0102  ................
-00000700: 0102 0102 0102 0106 0106 f814 0a02 0202  ................
-00000710: 0102 0102 0102 0102 0102 0104 fa02 8004  ................
-00000720: 0972 1e00 0000 290e da15 786d 6c2e 6574  .r....)...xml.et
-00000730: 7265 652e 456c 656d 656e 7454 7265 65da  ree.ElementTree.
-00000740: 0378 6d6c da15 6d61 7074 6173 6b65 722e  .xml..maptasker.
-00000750: 7372 632e 6f75 7470 7574 6c72 0200 0000  src.outputlr....
-00000760: 5a16 6d61 7074 6173 6b65 722e 7372 632e  Z.maptasker.src.
-00000770: 7461 736b 6163 746e 7203 0000 00da 166d  taskactnr......m
-00000780: 6170 7461 736b 6572 2e73 7263 2e73 7973  aptasker.src.sys
-00000790: 636f 6e73 7472 0400 0000 7205 0000 0072  constr....r....r
-000007a0: 1900 0000 da04 6c69 7374 da05 6574 7265  ......list..etre
-000007b0: 65da 0464 6963 7472 1e00 0000 721c 0000  e..dictr....r...
-000007c0: 0072 1c00 0000 721c 0000 0072 1d00 0000  .r....r....r....
-000007d0: da08 3c6d 6f64 756c 653e 0100 0000 7330  ..<module>....s0
-000007e0: 0000 0008 0d0c 020c 020c 010c 0102 0602  ................
-000007f0: 0102 ff02 0202 fe02 0302 fd04 0402 fc02  ................
-00000800: 0502 fb02 0602 fa02 0702 f902 0802 f802  ................
-00000810: 090e f7                                  ...
+000001c0: 0100 6408 7c00 7600 7245 7c0a 7d0b 7c00  ..d.|.v.rE|.}.|.
+000001d0: 7d0c 6403 7d0a 7c05 6404 1900 7245 7c00  }.d.}.|.d...rE|.
+000001e0: a006 6409 a101 7d0d 7c0d 640a 6b03 7245  ..d...}.|.d.k.rE
+000001f0: 7c00 9b00 7405 7c0d 8301 9b00 9d02 7d00  |...t.|.......}.
+00000200: 7407 7c06 7c05 7c01 640b 7c00 9b00 640c  t.|.|.|.d.|...d.
+00000210: 7c0a 9b00 9d03 8305 0100 7c0b 7258 7c0b  |.........|.rX|.
+00000220: 7d0a 7c0c 7d00 7c03 7262 640d 7c00 7600  }.|.}.|.rbd.|.v.
+00000230: 7262 7408 7c0a 7600 7366 640d 7c00 7600  rbt.|.v.sfd.|.v.
+00000240: 7278 640e 7c0a 7601 7278 7409 7c03 7c01  rxd.|.v.rxt.|.|.
+00000250: 7c05 7c00 7c0a 7c04 7c06 7c07 640f 1900  |.|.|.|.|.|.d...
+00000260: 8308 0100 710a 7c00 6410 6b02 728b 7c05  ....q.|.d.k.r.|.
+00000270: 6411 1900 6412 6b04 728b 7c08 7c0a 7c01  d...d.k.r.|.|.|.
+00000280: 7c04 7c05 7c06 7c07 8306 0100 710a 6413  |.|.|.|.....q.d.
+00000290: 5300 2914 6129 0200 000a 2020 2020 5072  S.).a)....    Pr
+000002a0: 6f63 6573 7320 5461 736b 2f53 6365 6e65  ocess Task/Scene
+000002b0: 2074 6578 742f 6c69 6e65 2069 7465 6d3a   text/line item:
+000002c0: 2063 616c 6c20 7265 6375 7273 6976 656c   call recursivel
+000002d0: 7920 666f 7220 5461 736b 7320 7769 7468  y for Tasks with
+000002e0: 696e 2053 6365 6e65 730a 2020 2020 2020  in Scenes.      
+000002f0: 2020 3a70 6172 616d 206c 6973 745f 7479    :param list_ty
+00000300: 7065 3a20 5461 736b 206f 7220 5363 656e  pe: Task or Scen
+00000310: 650a 2020 2020 2020 2020 3a70 6172 616d  e.        :param
+00000320: 206f 7574 7075 745f 6c69 7374 3a20 6c69   output_list: li
+00000330: 7374 206f 6620 6f75 7470 7574 206c 696e  st of output lin
+00000340: 6573 0a20 2020 2020 2020 203a 7061 7261  es.        :para
+00000350: 6d20 7468 655f 6c69 7374 3a20 6c69 7374  m the_list: list
+00000360: 206f 6620 5461 736b 206e 616d 6573 2074   of Task names t
+00000370: 726f 2070 726f 6365 7373 0a20 2020 2020  ro process.     
+00000380: 2020 203a 7061 7261 6d20 7468 655f 7461     :param the_ta
+00000390: 736b 3a20 5461 736b 2f53 6365 6e65 2078  sk: Task/Scene x
+000003a0: 6d6c 2065 6c65 6d65 6e74 0a20 2020 2020  ml element.     
+000003b0: 2020 203a 7061 7261 6d20 7461 736b 735f     :param tasks_
+000003c0: 666f 756e 643a 206c 6973 7420 6f66 2054  found: list of T
+000003d0: 6173 6b73 2066 6f75 6e64 2073 6f20 6661  asks found so fa
+000003e0: 720a 2020 2020 2020 2020 3a70 6172 616d  r.        :param
+000003f0: 2070 726f 6772 616d 5f61 7267 733a 2064   program_args: d
+00000400: 6963 7469 6f6e 6172 7920 6f66 2072 756e  ictionary of run
+00000410: 7469 6d65 2061 7267 756d 656e 7473 0a20  time arguments. 
+00000420: 2020 2020 2020 203a 7061 7261 6d20 636f         :param co
+00000430: 6c6f 726d 6170 3a20 6469 6374 696f 6e61  lormap: dictiona
+00000440: 7279 206f 6620 636f 6c6f 7273 2074 6f20  ry of colors to 
+00000450: 7573 650a 2020 2020 2020 2020 3a70 6172  use.        :par
+00000460: 616d 2061 6c6c 5f74 6173 6b65 725f 6974  am all_tasker_it
+00000470: 656d 733a 2064 6963 7469 6f6e 6172 7920  ems: dictionary 
+00000480: 6f66 2061 6c6c 2054 6173 6b65 7220 5072  of all Tasker Pr
+00000490: 6f6a 6563 7473 2f50 726f 6669 6c65 732f  ojects/Profiles/
+000004a0: 5461 736b 732f 5363 656e 6573 0a20 2020  Tasks/Scenes.   
+000004b0: 2020 2020 203a 7265 7475 726e 3a0a 2020       :return:.  
+000004c0: 2020 7201 0000 0029 01da 0d70 726f 6365    r....)...proce
+000004d0: 7373 5f73 6365 6e65 da00 da05 6465 6275  ss_scene....debu
+000004e0: 677a 1770 726f 6365 7373 5f6c 6973 7420  gz.process_list 
+000004f0: 2074 6865 5f69 7465 6d3a 7a0a 2074 6865   the_item:z. the
+00000500: 5f6c 6973 743a 7a0b 206c 6973 745f 7479  _list:z. list_ty
+00000510: 7065 3a7a 0f26 2334 353b 2623 3435 3b54  pe:z.&#45;&#45;T
+00000520: 6173 6b3a 7a03 4944 3ae9 ffff ffff e902  ask:z.ID:.......
+00000530: 0000 007a 0626 6e62 7370 3b7a 0554 6173  ...z.&nbsp;z.Tas
+00000540: 6b3a 7a0e 3c65 6d3e 4e6f 2050 726f 6669  k:z.<em>No Profi
+00000550: 6c65 da09 616c 6c5f 7461 736b 737a 0653  le..all_tasksz.S
+00000560: 6365 6e65 3ada 1464 6973 706c 6179 5f64  cene:..display_d
+00000570: 6574 6169 6c5f 6c65 7665 6ce9 0100 0000  etail_level.....
+00000580: 4e29 0ada 146d 6170 7461 736b 6572 2e73  N)...maptasker.s
+00000590: 7263 2e73 6365 6e65 7372 0f00 0000 da09  rc.scenesr......
+000005a0: 656e 756d 6572 6174 6572 0400 0000 7211  enumerater....r.
+000005b0: 0000 00da 0373 7472 da04 6669 6e64 7202  .....str..findr.
+000005c0: 0000 0072 0500 0000 7203 0000 0029 0e72  ...r....r....).r
+000005d0: 0600 0000 7207 0000 0072 0800 0000 7209  ....r....r....r.
+000005e0: 0000 0072 0a00 0000 720b 0000 0072 0c00  ...r....r....r..
+000005f0: 0000 720d 0000 0072 0f00 0000 5a08 6d79  ..r....r....Z.my
+00000600: 5f63 6f75 6e74 da08 7468 655f 6974 656d  _count..the_item
+00000610: 5a09 7465 6d70 5f69 7465 6d5a 0974 656d  Z.temp_itemZ.tem
+00000620: 705f 6c69 7374 5a06 6964 5f6c 6f63 a900  p_listZ.id_loc..
+00000630: 721c 0000 00fa 772f 5573 6572 732f 6d69  r.....w/Users/mi
+00000640: 6b72 7562 696e 2f4c 6962 7261 7279 2f43  krubin/Library/C
+00000650: 6c6f 7564 5374 6f72 6167 652f 476f 6f67  loudStorage/Goog
+00000660: 6c65 4472 6976 652d 6d69 6b72 7562 696e  leDrive-mikrubin
+00000670: 4067 6d61 696c 2e63 6f6d 2f4d 7920 4472  @gmail.com/My Dr
+00000680: 6976 652f 5079 7468 6f6e 2f6d 6170 7461  ive/Python/mapta
+00000690: 736b 6572 2f6d 6170 7461 736b 6572 2f73  sker/maptasker/s
+000006a0: 7263 2f70 726f 636c 6973 742e 7079 da0c  rc/proclist.py..
+000006b0: 7072 6f63 6573 735f 6c69 7374 1a00 0000  process_list....
+000006c0: 736c 0000 000c 1810 0304 0104 0108 0104  sl..............
+000006d0: 0102 0106 0104 ff02 0104 ff02 0104 ff04  ................
+000006e0: ff08 0604 0104 0104 0108 010a 0108 0110  ................
+000006f0: 0102 0414 0104 ff04 0304 0104 0102 0602  ................
+00000700: ff10 0108 0108 0102 0102 0102 0102 0102  ................
+00000710: 0102 0102 0102 0106 0106 f814 0a02 0202  ................
+00000720: 0102 0102 0102 0102 0102 0104 fa02 8004  ................
+00000730: 0972 1e00 0000 290e da15 786d 6c2e 6574  .r....)...xml.et
+00000740: 7265 652e 456c 656d 656e 7454 7265 65da  ree.ElementTree.
+00000750: 0378 6d6c da15 6d61 7074 6173 6b65 722e  .xml..maptasker.
+00000760: 7372 632e 6f75 7470 7574 6c72 0200 0000  src.outputlr....
+00000770: 5a16 6d61 7074 6173 6b65 722e 7372 632e  Z.maptasker.src.
+00000780: 7461 736b 6163 746e 7203 0000 00da 166d  taskactnr......m
+00000790: 6170 7461 736b 6572 2e73 7263 2e73 7973  aptasker.src.sys
+000007a0: 636f 6e73 7472 0400 0000 7205 0000 0072  constr....r....r
+000007b0: 1900 0000 da04 6c69 7374 da05 6574 7265  ......list..etre
+000007c0: 65da 0464 6963 7472 1e00 0000 721c 0000  e..dictr....r...
+000007d0: 0072 1c00 0000 721c 0000 0072 1d00 0000  .r....r....r....
+000007e0: da08 3c6d 6f64 756c 653e 0100 0000 7330  ..<module>....s0
+000007f0: 0000 0008 0d0c 020c 020c 010c 0102 0602  ................
+00000800: 0102 ff02 0202 fe02 0302 fd04 0402 fc02  ................
+00000810: 0502 fb02 0602 fa02 0702 f902 0802 f802  ................
+00000820: 090e f7                                  ...
```

### Comparing `maptasker-1.3.1/maptasker/src/__pycache__/profiles.cpython-310.pyc` & `maptasker-1.3.2/maptasker/src/__pycache__/profiles.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 10 17:21:57 2023 UTC, .py size: 10183 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 12% similar despite different names*

```diff
@@ -1,287 +1,287 @@
-00000000: 6f0d 0d0a 0000 0000 3567 0b64 c727 0000  o.......5g.d.'..
+00000000: 6f0d 0d0a 0000 0000 545d 2c64 f428 0000  o.......T],d.(..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
-00000020: 0016 0000 0040 0000 0073 0a01 0000 6400  .....@...s....d.
+00000020: 0016 0000 0040 0000 0073 f200 0000 6400  .....@...s....d.
 00000030: 6401 6c00 5a01 6400 6401 6c02 6d03 0200  d.l.Z.d.d.l.m...
 00000040: 0100 6d04 5a04 0100 6400 6401 6c05 6d03  ..m.Z...d.d.l.m.
 00000050: 0200 0100 6d06 5a06 0100 6400 6402 6c07  ....m.Z...d.d.l.
-00000060: 6d08 5a08 0100 6400 6403 6c09 6d0a 5a0a  m.Z...d.d.l.m.Z.
-00000070: 0100 6400 6404 6c09 6d0b 5a0b 0100 6400  ..d.d.l.m.Z...d.
-00000080: 6405 6c0c 6d0d 5a0d 0100 6400 6406 6c0e  d.l.m.Z...d.d.l.
-00000090: 6d0f 5a0f 0100 6400 6407 6c10 6d11 5a11  m.Z...d.d.l.m.Z.
-000000a0: 0100 6408 6501 6a12 6409 6513 640a 6513  ..d.e.j.d.e.d.e.
-000000b0: 640b 6514 640c 6514 640d 6514 640e 6515  d.e.d.e.d.e.d.e.
-000000c0: 6501 6a12 6516 6602 1900 660e 640f 6410  e.j.e.f...f.d.d.
-000000d0: 8404 5a17 6411 6501 6a12 6412 6501 6a12  ..Z.d.e.j.d.e.j.
-000000e0: 6413 6513 640b 6514 6414 6514 640e 6515  d.e.d.e.d.e.d.e.
-000000f0: 660c 6415 6416 8404 5a18 6413 6513 6411  f.d.d...Z.d.e.d.
-00000100: 6501 6a12 6417 6516 6418 6513 6419 6513  e.j.d.e.d.e.d.e.
-00000110: 640b 6514 641a 6516 6414 6514 641b 6514  d.e.d.e.d.e.d.e.
-00000120: 640d 6514 640e 6501 6a12 6616 641c 641d  d.e.d.e.j.f.d.d.
-00000130: 8404 5a19 6401 5300 291e e900 0000 004e  ..Z.d.S.)......N
-00000140: 2901 da0b 6765 745f 6b69 645f 6170 7029  )...get_kid_app)
-00000150: 01da 096d 795f 6f75 7470 7574 2901 da12  ...my_output)...
-00000160: 7265 6672 6573 685f 6f75 725f 6f75 7470  refresh_our_outp
-00000170: 7574 2901 da0c 6765 745f 7072 696f 7269  ut)...get_priori
-00000180: 7479 2901 da05 7368 6172 6529 01da 0a4e  ty)...share)...N
-00000190: 4f5f 5052 4f46 494c 45da 0b74 6865 5f70  O_PROFILE..the_p
-000001a0: 726f 6669 6c65 da10 666f 756e 645f 7461  rofile..found_ta
-000001b0: 736b 735f 6c69 7374 da10 7461 736b 5f6f  sks_list..task_o
-000001c0: 7574 7075 745f 6c69 6e65 da0c 7072 6f67  utput_line..prog
-000001d0: 7261 6d5f 6172 6773 da09 616c 6c5f 7461  ram_args..all_ta
-000001e0: 736b 73da 0b66 6f75 6e64 5f69 7465 6d73  sks..found_items
-000001f0: da06 7265 7475 726e 6306 0000 0000 0000  ..returnc.......
-00000200: 0000 0000 000c 0000 0008 0000 0043 0000  .............C..
-00000210: 0073 a200 0000 6700 6401 a201 7d06 6402  .s....g.d...}.d.
-00000220: 5c02 7d07 7d08 7c00 4400 5d42 7d09 7c09  \.}.}.|.D.]B}.|.
-00000230: 6a00 7c06 7600 7212 710a 6403 7c09 6a00  j.|.v.r.q.d.|.j.
-00000240: 7600 7242 6404 7d0a 7c09 6a00 6405 6b02  v.rBd.}.|.j.d.k.
-00000250: 7220 6406 7d0a 7c09 6a01 7d0b 7402 a003  r d.}.|.j.}.t...
-00000260: 7c0b 7c01 7c02 7c0a 7c04 a105 5c02 7d07  |.|.|.|.|...\.}.
-00000270: 7d08 7c03 6407 1900 7241 7c03 6407 1900  }.|.d...rA|.d...
-00000280: 7c08 6b02 7241 6408 7c05 6409 3c00 0100  |.k.rAd.|.d.<...
-00000290: 7c07 7c08 6602 5300 710a 7c09 6a00 640a  |.|.f.S.q.|.j.d.
-000002a0: 6b02 724c 0100 7c07 7c08 6602 5300 710a  k.rL..|.|.f.S.q.
-000002b0: 7c07 7c08 6602 5300 290b 4e29 04da 0563  |.|.f.S.).N)...c
-000002c0: 6461 7465 da05 6564 6174 65da 0566 6c61  date..edate..fla
-000002d0: 6773 da02 6964 2902 da00 7213 0000 005a  gs..id)...r....Z
-000002e0: 036d 6964 da05 456e 7472 795a 046d 6964  .mid..EntryZ.mid
-000002f0: 31da 0445 7869 74da 1073 696e 676c 655f  1..Exit..single_
-00000300: 7461 736b 5f6e 616d 6554 da11 7369 6e67  task_nameT..sing
-00000310: 6c65 5f74 6173 6b5f 666f 756e 64da 036e  le_task_found..n
-00000320: 6d65 2904 da03 7461 67da 0474 6578 74da  me)...tag..text.
-00000330: 0574 6173 6b73 da0d 6765 745f 7461 736b  .tasks..get_task
-00000340: 5f6e 616d 6529 0c72 0800 0000 7209 0000  _name).r....r...
-00000350: 0072 0a00 0000 720b 0000 0072 0c00 0000  .r....r....r....
-00000360: 720d 0000 005a 116b 6579 735f 7765 5f64  r....Z.keys_we_d
-00000370: 6f6e 745f 7761 6e74 5a10 7468 655f 7461  ont_wantZ.the_ta
-00000380: 736b 5f65 6c65 6d65 6e74 da0d 7468 655f  sk_element..the_
-00000390: 7461 736b 5f6e 616d 65da 0563 6869 6c64  task_name..child
-000003a0: da09 7461 736b 5f74 7970 65da 0774 6173  ..task_type..tas
-000003b0: 6b5f 6964 a900 7221 0000 00fa 772f 5573  k_id..r!....w/Us
-000003c0: 6572 732f 6d69 6b72 7562 696e 2f4c 6962  ers/mikrubin/Lib
-000003d0: 7261 7279 2f43 6c6f 7564 5374 6f72 6167  rary/CloudStorag
-000003e0: 652f 476f 6f67 6c65 4472 6976 652d 6d69  e/GoogleDrive-mi
-000003f0: 6b72 7562 696e 4067 6d61 696c 2e63 6f6d  krubin@gmail.com
-00000400: 2f4d 7920 4472 6976 652f 5079 7468 6f6e  /My Drive/Python
-00000410: 2f6d 6170 7461 736b 6572 2f6d 6170 7461  /maptasker/mapta
-00000420: 736b 6572 2f73 7263 2f70 726f 6669 6c65  sker/src/profile
-00000430: 732e 7079 da11 6765 745f 7072 6f66 696c  s.py..get_profil
-00000440: 655f 7461 736b 731d 0000 0073 3200 0000  e_tasks....s2...
-00000450: 0808 0801 0802 0a01 0201 0a01 0401 0a01  ................
-00000460: 0401 0601 0401 0a01 08ff 0604 02ff 0c02  ................
-00000470: 0802 0201 0805 0280 0afd 0202 0801 02fd  ................
-00000480: 0803 7223 0000 00da 0770 726f 6a65 6374  ..r#.....project
-00000490: da07 7072 6f66 696c 65da 0b6f 7574 7075  ..profile..outpu
-000004a0: 745f 6c69 7374 da08 636f 6c6f 726d 6170  t_list..colormap
-000004b0: 6305 0000 0000 0000 0000 0000 0013 0000  c...............
-000004c0: 000a 0000 0043 0000 0073 cc01 0000 6401  .....C...s....d.
-000004d0: 7c04 6402 1900 1700 6403 1700 7c03 6404  |.d.....d...|.d.
-000004e0: 1900 1700 7d05 6405 7c04 6406 1900 1700  ....}.d.|.d.....
-000004f0: 6407 1700 7d06 6405 7c04 6408 1900 1700  d...}.d.|.d.....
-00000500: 6409 1700 7c05 1700 7d07 6405 7c04 640a  d...|...}.d.|.d.
-00000510: 1900 1700 6403 1700 7d08 640b 7d09 7c01  ....d...}.d.}.|.
-00000520: a000 640c a101 7d0a 7c0a 6400 7501 7239  ..d...}.|.d.u.r9
-00000530: 7c0a 6a01 640d 6b02 7239 7c06 7d0b 6e02  |.j.d.k.r9|.}.n.
-00000540: 640b 7d0b 7c00 a000 640e a101 7d0c 7c0c  d.}.|...d...}.|.
-00000550: 6400 7501 7246 7c07 6e01 640b 7d0d 640b  d.u.rF|.n.d.}.d.
-00000560: 7d0e 7c03 640f 1900 6410 6b02 7259 7402  }.|.d...d.k.rYt.
-00000570: 7c01 8301 7d0e 7403 7c01 6411 8302 7d0f  |...}.t.|.d...}.
-00000580: 640b 7d10 7c03 6412 1900 7276 7404 a005  d.}.|.d...rvt...
-00000590: 7c01 7c04 7c03 a103 7d09 7c09 7276 7c08  |.|.|...}.|.rv|.
-000005a0: 9b00 6413 7c09 9b00 6414 7c10 9b00 7c0d  ..d.|...d.|...|.
-000005b0: 9b00 7c0b 9b00 9d07 7d10 7a0a 7c01 a000  ..|.....}.z.|...
-000005c0: 6415 a101 6a01 7c10 1700 7d10 5700 6e41  d...j.|...}.W.nA
-000005d0: 0400 7406 79c1 0100 7d11 0100 7a35 7c03  ..t.y...}...z5|.
-000005e0: 6412 1900 72af 7404 a005 7c01 7c04 7c03  d...r.t...|.|.|.
-000005f0: a103 7d09 7c09 72a6 7407 7c08 1700 6413  ..}.|.r.t.|...d.
-00000600: 1700 7c09 1700 6414 1700 7c05 1700 7c0d  ..|...d...|...|.
-00000610: 1700 7c0b 1700 7d10 6e11 7c10 7407 1700  ..|...}.n.|.t...
-00000620: 7c0d 1700 7c0b 1700 7d10 6e08 7c10 7407  |...|...}.n.|.t.
-00000630: 1700 7c0d 1700 7c0b 1700 7d10 5700 5900  ..|...|...}.W.Y.
-00000640: 6400 7d11 7e11 6e05 6400 7d11 7e11 7701  d.}.~.n.d.}.~.w.
-00000650: 7700 7c03 6416 1900 72d3 7c01 a000 6417  w.|.d...r.|...d.
-00000660: a101 6a01 7d12 7c10 9b00 6418 7c12 9b00  ..j.}.|...d.|...
-00000670: 9d03 7d10 7408 7c04 7c03 7c02 6419 7c05  ..}.t.|.|.|.d.|.
-00000680: 9b00 641a 7c10 9b00 9d03 8305 0100 7c0a  ..d.|.........|.
-00000690: 7c0d 7c09 7c10 6604 5300 291b 4e7a 153c  |.|.|.f.S.).Nz.<
-000006a0: 7370 616e 2073 7479 6c65 203d 2022 636f  span style = "co
-000006b0: 6c6f 723a da0d 7072 6f66 696c 655f 636f  lor:..profile_co
-000006c0: 6c6f 727a 0822 3c2f 7370 616e 3eda 0b66  lorz."</span>..f
-000006d0: 6f6e 745f 746f 5f75 7365 7a16 203c 7370  ont_to_usez. <sp
-000006e0: 616e 2073 7479 6c65 203d 2022 636f 6c6f  an style = "colo
-000006f0: 723a da16 6469 7361 626c 6564 5f70 726f  r:..disabled_pro
-00000700: 6669 6c65 5f63 6f6c 6f72 7a13 223c 2f73  file_colorz."</s
-00000710: 7061 6e3e 5b44 4953 4142 4c45 445d 20da  pan>[DISABLED] .
-00000720: 136c 6175 6e63 6865 725f 7461 736b 5f63  .launcher_task_c
-00000730: 6f6c 6f72 7a18 223c 2f73 7061 6e3e 5b4c  olorz."</span>[L
-00000740: 6175 6e63 6865 7220 5461 736b 5d20 da17  auncher Task] ..
-00000750: 7072 6f66 696c 655f 636f 6e64 6974 696f  profile_conditio
-00000760: 6e5f 636f 6c6f 7272 1300 0000 da05 6c69  n_colorr......li
-00000770: 6d69 74da 0474 7275 655a 0f50 726f 6669  mit..trueZ.Profi
-00000780: 6c65 5661 7269 6162 6c65 da14 6469 7370  leVariable..disp
-00000790: 6c61 795f 6465 7461 696c 5f6c 6576 656c  lay_detail_level
-000007a0: e903 0000 0046 da1a 6469 7370 6c61 795f  .....F..display_
-000007b0: 7072 6f66 696c 655f 636f 6e64 6974 696f  profile_conditio
-000007c0: 6e73 7a02 2028 7a02 2920 7218 0000 00da  nsz. (z.) r.....
-000007d0: 0564 6562 7567 7212 0000 007a 0420 4944  .debugr....z. ID
-000007e0: 3ae9 0200 0000 7a09 5072 6f66 696c 653a  :.....z.Profile:
-000007f0: 2029 09da 0466 696e 6472 1a00 0000 7202   )...findr....r.
-00000800: 0000 0072 0500 0000 da09 636f 6e64 6974  ...r......condit
-00000810: 696f 6e5a 1770 6172 7365 5f70 726f 6669  ionZ.parse_profi
-00000820: 6c65 5f63 6f6e 6469 7469 6f6e da09 4578  le_condition..Ex
-00000830: 6365 7074 696f 6e72 0700 0000 7203 0000  ceptionr....r...
-00000840: 0029 1372 2400 0000 7225 0000 0072 2600  .).r$...r%...r&.
-00000850: 0000 720b 0000 0072 2700 0000 5a12 7072  ..r....r'...Z.pr
-00000860: 6f66 696c 655f 636f 6c6f 725f 6874 6d6c  ofile_color_html
-00000870: 5a15 6469 7361 626c 6564 5f70 726f 6669  Z.disabled_profi
-00000880: 6c65 5f68 746d 6c5a 126c 6175 6e63 6865  le_htmlZ.launche
-00000890: 725f 7461 736b 5f68 746d 6c5a 1463 6f6e  r_task_htmlZ.con
-000008a0: 6469 7469 6f6e 5f63 6f6c 6f72 5f68 746d  dition_color_htm
-000008b0: 6cda 1170 726f 6669 6c65 5f63 6f6e 6469  l..profile_condi
-000008c0: 7469 6f6e 722d 0000 00da 0864 6973 6162  tionr-.....disab
-000008d0: 6c65 645a 0c6c 6175 6e63 6865 725f 786d  ledZ.launcher_xm
-000008e0: 6cda 086c 6175 6e63 6865 72da 0c6b 6964  l..launcher..kid
-000008f0: 5f61 7070 5f69 6e66 6fda 0870 7269 6f72  _app_info..prior
-00000900: 6974 79da 0c70 726f 6669 6c65 5f6e 616d  ity..profile_nam
-00000910: 65da 0165 5a0a 7072 6f66 696c 655f 6964  e..eZ.profile_id
-00000920: 7221 0000 0072 2100 0000 7222 0000 00da  r!...r!...r"....
-00000930: 1262 7569 6c64 5f70 726f 6669 6c65 5f6c  .build_profile_l
-00000940: 696e 6543 0000 0073 b400 0000 0209 0601  ineC...s........
-00000950: 02ff 0202 02fe 0603 02fd 02ff 0207 0601  ................
-00000960: 02ff 0202 02fe 02ff 0206 0601 02ff 0202  ................
-00000970: 02fe 0203 02fd 02ff 0e07 02ff 0403 0a03  ................
-00000980: 1201 0601 0402 0401 0201 04ff 1003 0403  ................
-00000990: 0c01 0801 0a01 0403 0801 0401 0601 04ff  ................
-000009a0: 0403 0c02 0201 02ff 0201 02ff 0201 04ff  ................
-000009b0: 02ff 0206 1401 0e01 0801 0401 0601 04ff  ................
-000009c0: 0403 0202 0201 02ff 0202 02fe 0203 02fd  ................
-000009d0: 0204 02fc 0205 02fb 0206 02fa 0207 02f9  ................
-000009e0: 04ff 120b 1002 1480 02ed 0814 0c01 0e01  ................
-000009f0: 0202 0201 0201 0201 0201 0c01 04fb 0c07  ................
-00000a00: 723e 0000 00da 0c70 726f 6a65 6374 5f6e  r>.....project_n
-00000a10: 616d 65da 0b70 726f 6669 6c65 5f69 6473  ame..profile_ids
-00000a20: da13 6c69 7374 5f6f 665f 666f 756e 645f  ..list_of_found_
-00000a30: 7461 736b 73da 0768 6561 6469 6e67 da10  tasks..heading..
-00000a40: 616c 6c5f 7461 736b 6572 5f69 7465 6d73  all_tasker_items
-00000a50: 630a 0000 0000 0000 0000 0000 0016 0000  c...............
-00000a60: 000f 0000 0043 0000 0073 3201 0000 6401  .....C...s2...d.
-00000a70: 7d0a 7c03 4400 5d92 7d0b 7c08 6402 1900  }.|.D.].}.|.d...
-00000a80: 7c0b 1900 7d0c 7c0c 6403 7500 7213 0100  |...}.|.d.u.r...
-00000a90: 6403 5300 7c05 6404 1900 7248 7a1e 7c0c  d.S.|.d...rHz.|.
-00000aa0: a000 6405 a101 6a01 7d0d 7c05 6404 1900  ..d...j.}.|.d...
-00000ab0: 7c0d 6b03 7226 5700 7104 6406 7c09 6407  |.k.r&W.q.d.|.d.
-00000ac0: 3c00 7402 6408 7c00 7c02 6401 7c06 7c07  <.t.d.|.|.d.|.|.
-00000ad0: 7c05 8307 0100 5700 6e12 0400 7403 7947  |.....W.n...t.yG
-00000ae0: 0100 7d0e 0100 7a06 5700 5900 6403 7d0e  ..}...z.W.Y.d.}.
-00000af0: 7e0e 7104 6403 7d0e 7e0e 7701 7700 6700  ~.q.d.}.~.w.w.g.
-00000b00: 7d0f 6409 7d10 7404 7c0c 7c04 7c0f 7c05  }.d.}.t.|.|.|.|.
-00000b10: 7c08 640a 1900 7c09 8306 5c02 7d0a 7d11  |.d...|...\.}.}.
-00000b20: 7405 7c01 7c0c 7c00 7c05 7c07 8305 5c04  t.|.|.|.|.|...\.
-00000b30: 7d12 7d13 7d14 7d0d 7c05 640b 1900 7270  }.}.}.}.|.d...rp
-00000b40: 7406 7c0c 7c07 7c05 7c00 8304 0100 7407  t.|.|.|.|.....t.
-00000b50: a008 7c00 7c11 7c0a 7c0f 7c02 7c0d 7c04  ..|.|.|.|.|.|.|.
-00000b60: 7c06 7c07 7c05 7c08 7c09 a10c 7d15 7c15  |.|.|.|.|...}.|.
-00000b70: 728a 7c05 640c 1900 728a 7c09 640d 1900  r.|.d...r.|.d...
-00000b80: 7390 7c15 7393 7c09 6407 1900 7293 0100  s.|.s.|.d...r...
-00000b90: 7c0a 5300 7c15 7396 7104 7104 7c0a 5300  |.S.|.s.q.q.|.S.
-00000ba0: 290e 619c 0200 000a 2020 2020 476f 2074  ).a.....    Go t
-00000bb0: 6872 6f75 6768 2050 726f 6a65 6374 2773  hrough Project's
-00000bc0: 2050 726f 6669 6c65 7320 616e 6420 6f75   Profiles and ou
-00000bd0: 7470 7574 2065 6163 680a 2020 2020 2020  tput each.      
-00000be0: 2020 3a70 6172 616d 206f 7574 7075 745f    :param output_
-00000bf0: 6c69 7374 3a20 6c69 7374 206f 6620 6561  list: list of ea
-00000c00: 6368 206f 7574 7075 7420 6c69 6e65 2067  ch output line g
-00000c10: 656e 6572 6174 6564 2073 6f20 6661 720a  enerated so far.
-00000c20: 2020 2020 2020 2020 3a70 6172 616d 2070          :param p
-00000c30: 726f 6a65 6374 3a20 5072 6f6a 6563 7420  roject: Project 
-00000c40: 746f 2070 726f 6365 7373 0a20 2020 2020  to process.     
-00000c50: 2020 203a 7061 7261 6d20 7072 6f6a 6563     :param projec
-00000c60: 745f 6e61 6d65 3a20 5072 6f6a 6563 7427  t_name: Project'
-00000c70: 7320 6e61 6d65 0a20 2020 2020 2020 203a  s name.        :
-00000c80: 7061 7261 6d20 7072 6f66 696c 655f 6964  param profile_id
-00000c90: 733a 206c 6973 7420 6f66 2050 726f 6669  s: list of Profi
-00000ca0: 6c65 7320 696e 2050 726f 6a65 6374 0a20  les in Project. 
-00000cb0: 2020 2020 2020 203a 7061 7261 6d20 6c69         :param li
-00000cc0: 7374 5f6f 665f 666f 756e 645f 7461 736b  st_of_found_task
-00000cd0: 733a 206c 6973 7420 6f66 2054 6173 6b73  s: list of Tasks
-00000ce0: 2066 6f75 6e64 0a20 2020 2020 2020 203a   found.        :
-00000cf0: 7061 7261 6d20 7072 6f67 7261 6d5f 6172  param program_ar
-00000d00: 6773 3a20 7275 6e74 696d 6520 6172 6775  gs: runtime argu
-00000d10: 6d65 6e74 730a 2020 2020 2020 2020 3a70  ments.        :p
-00000d20: 6172 616d 2068 6561 6469 6e67 3a20 7468  aram heading: th
-00000d30: 6520 6f75 7470 7574 2068 6561 6469 6e67  e output heading
-00000d40: 0a20 2020 2020 2020 203a 7061 7261 6d20  .        :param 
-00000d50: 636f 6c6f 726d 6170 3a20 7468 6520 636f  colormap: the co
-00000d60: 6c6f 7273 2074 6f20 7573 6520 696e 206f  lors to use in o
-00000d70: 7570 7574 0a20 2020 2020 2020 203a 7061  uput.        :pa
-00000d80: 7261 6d20 616c 6c5f 7461 736b 6572 5f69  ram all_tasker_i
-00000d90: 7465 6d73 3a20 616c 6c20 5461 736b 6572  tems: all Tasker
-00000da0: 2050 726f 6a65 6374 732f 5072 6f66 696c   Projects/Profil
-00000db0: 6573 2f54 6173 6b73 2f53 6365 6e65 730a  es/Tasks/Scenes.
-00000dc0: 2020 2020 2020 2020 3a70 6172 616d 2066          :param f
-00000dd0: 6f75 6e64 5f69 7465 6d73 3a20 616c 6c20  ound_items: all 
-00000de0: 2266 6f75 6e64 2220 6974 656d 7320 2873  "found" items (s
-00000df0: 696e 676c 6520 5072 6f6a 6563 742f 5072  ingle Project/Pr
-00000e00: 6f66 696c 652f 5461 736b 2920 6e61 6d65  ofile/Task) name
-00000e10: 2061 6e64 2066 6c61 670a 2020 2020 2020   and flag.      
-00000e20: 2020 3a72 6574 7572 6e3a 2078 6d6c 2065    :return: xml e
-00000e30: 6c65 6d65 6e74 206f 6620 5461 736b 0a20  lement of Task. 
-00000e40: 2020 2072 1300 0000 da0c 616c 6c5f 7072     r......all_pr
-00000e50: 6f66 696c 6573 4eda 1373 696e 676c 655f  ofilesN..single_
-00000e60: 7072 6f66 696c 655f 6e61 6d65 7218 0000  profile_namer...
-00000e70: 0054 da14 7369 6e67 6c65 5f70 726f 6669  .T..single_profi
-00000e80: 6c65 5f66 6f75 6e64 46fa 0120 720c 0000  le_foundF.. r...
-00000e90: 00da 1164 6973 706c 6179 5f74 6173 6b65  ...display_taske
-00000ea0: 726e 6574 7216 0000 0072 1700 0000 2909  rnetr....r....).
-00000eb0: 7234 0000 0072 1a00 0000 7204 0000 0072  r4...r....r....r
-00000ec0: 3600 0000 7223 0000 0072 3e00 0000 7206  6...r#...r>...r.
-00000ed0: 0000 0072 1b00 0000 da0b 6f75 7470 7574  ...r......output
-00000ee0: 5f74 6173 6b29 1672 2600 0000 7224 0000  _task).r&...r$..
-00000ef0: 0072 3f00 0000 7240 0000 0072 4100 0000  .r?...r@...rA...
-00000f00: 720b 0000 0072 4200 0000 7227 0000 0072  r....rB...r'...r
-00000f10: 4300 0000 720d 0000 00da 106f 7572 5f74  C...r......our_t
-00000f20: 6173 6b5f 656c 656d 656e 74da 0469 7465  ask_element..ite
-00000f30: 6d72 2500 0000 723c 0000 0072 3d00 0000  mr%...r<...r=...
-00000f40: da09 7461 736b 5f6c 6973 7472 0a00 0000  ..task_listr....
-00000f50: da0d 6f75 725f 7461 736b 5f6e 616d 6572  ..our_task_namer
-00000f60: 2d00 0000 7239 0000 0072 3700 0000 da0d  -...r9...r7.....
-00000f70: 7370 6563 6966 6963 5f74 6173 6b72 2100  specific_taskr!.
-00000f80: 0000 7221 0000 0072 2200 0000 da10 7072  ..r!...r".....pr
-00000f90: 6f63 6573 735f 7072 6f66 696c 6573 a600  ocess_profiles..
-00000fa0: 0000 738a 0000 0004 1a08 030c 0108 0106  ..s.............
-00000fb0: 0108 0202 010c 010c 0104 0108 0102 0102  ................
-00000fc0: 0102 0102 0102 0102 0102 0102 0108 f90e  ................
-00000fd0: 090c 0108 8002 ff04 0204 0102 0102 0102  ................
-00000fe0: 0102 0102 0106 0102 0108 fa02 0a0a 010c  ................
-00000ff0: ff08 050e 0104 0502 0102 0102 0102 0102  ................
-00001000: 0102 0102 0102 0102 0102 0102 0102 0104  ................
-00001010: f402 1102 ff06 0202 fe06 0302 fd02 0402  ................
-00001020: fc06 0502 fb02 0704 0404 fd02 0102 ff04  ................
-00001030: 0372 4f00 0000 291a da15 786d 6c2e 6574  .rO...)...xml.et
-00001040: 7265 652e 456c 656d 656e 7454 7265 65da  ree.ElementTree.
-00001050: 0378 6d6c 5a17 6d61 7074 6173 6b65 722e  .xmlZ.maptasker.
-00001060: 7372 632e 636f 6e64 6974 696f 6eda 0373  src.condition..s
-00001070: 7263 7235 0000 00da 136d 6170 7461 736b  rcr5.....maptask
-00001080: 6572 2e73 7263 2e74 6173 6b73 721b 0000  er.src.tasksr...
-00001090: 00da 146d 6170 7461 736b 6572 2e73 7263  ...maptasker.src
-000010a0: 2e6b 6964 6170 7072 0200 0000 da15 6d61  .kidappr......ma
-000010b0: 7074 6173 6b65 722e 7372 632e 6f75 7470  ptasker.src.outp
-000010c0: 7574 6c72 0300 0000 7204 0000 00da 166d  utlr....r......m
-000010d0: 6170 7461 736b 6572 2e73 7263 2e70 7269  aptasker.src.pri
-000010e0: 6f72 6974 7972 0500 0000 da13 6d61 7074  orityr......mapt
-000010f0: 6173 6b65 722e 7372 632e 7368 6172 6572  asker.src.sharer
-00001100: 0600 0000 da16 6d61 7074 6173 6b65 722e  ......maptasker.
-00001110: 7372 632e 7379 7363 6f6e 7374 7207 0000  src.sysconstr...
-00001120: 00da 0565 7472 6565 da04 6c69 7374 da04  ...etree..list..
-00001130: 6469 6374 da05 7475 706c 65da 0373 7472  dict..tuple..str
-00001140: 7223 0000 0072 3e00 0000 724f 0000 0072  r#...r>...rO...r
-00001150: 2100 0000 7221 0000 0072 2100 0000 7222  !...r!...r!...r"
-00001160: 0000 00da 083c 6d6f 6475 6c65 3e01 0000  .....<module>...
-00001170: 0073 7800 0000 080d 1202 1201 0c01 0c01  .sx.............
-00001180: 0c01 0c01 0c01 0c01 0206 0401 02ff 0202  ................
-00001190: 02fe 0203 02fd 0204 02fc 0205 02fb 0206  ................
-000011a0: 02fa 0c07 0af9 0226 0401 02ff 0402 02fe  .......&........
-000011b0: 0203 02fd 0204 02fc 0205 02fb 0206 0afa  ................
-000011c0: 0263 0201 02ff 0402 02fe 0203 02fd 0204  .c..............
-000011d0: 02fc 0205 02fb 0206 02fa 0207 02f9 0208  ................
-000011e0: 02f8 0209 02f7 020a 02f6 040b 0ef5       ..............
+00000060: 6d08 5a08 0100 6400 6403 6c07 6d09 5a09  m.Z...d.d.l.m.Z.
+00000070: 0100 6400 6404 6c0a 6d0b 5a0b 0100 6400  ..d.d.l.m.Z...d.
+00000080: 6405 6c0c 6d0d 5a0d 0100 6406 6501 6a0e  d.l.m.Z...d.e.j.
+00000090: 6407 650f 6408 650f 6409 6510 640a 6510  d.e.d.e.d.e.d.e.
+000000a0: 640b 6510 640c 6511 6501 6a0e 6512 6602  d.e.d.e.e.j.e.f.
+000000b0: 1900 660e 640d 640e 8404 5a13 640f 6501  ..f.d.d...Z.d.e.
+000000c0: 6a0e 6410 6501 6a0e 6411 650f 6409 6510  j.d.e.j.d.e.d.e.
+000000d0: 6412 6510 640c 6511 660c 6413 6414 8404  d.e.d.e.f.d.d...
+000000e0: 5a14 6411 650f 640f 6501 6a0e 6415 6512  Z.d.e.d.e.j.d.e.
+000000f0: 6416 650f 6417 650f 6409 6510 6418 6512  d.e.d.e.d.e.d.e.
+00000100: 6412 6510 6419 6510 640b 6510 640c 6501  d.e.d.e.d.e.d.e.
+00000110: 6a0e 6616 641a 641b 8404 5a15 6401 5300  j.f.d.d...Z.d.S.
+00000120: 291c e900 0000 004e 2901 da09 6d79 5f6f  )......N)...my_o
+00000130: 7574 7075 7429 01da 1272 6566 7265 7368  utput)...refresh
+00000140: 5f6f 7572 5f6f 7574 7075 7429 01da 0573  _our_output)...s
+00000150: 6861 7265 2901 da0a 4e4f 5f50 524f 4649  hare)...NO_PROFI
+00000160: 4c45 da0b 7468 655f 7072 6f66 696c 65da  LE..the_profile.
+00000170: 1066 6f75 6e64 5f74 6173 6b73 5f6c 6973  .found_tasks_lis
+00000180: 74da 1074 6173 6b5f 6f75 7470 7574 5f6c  t..task_output_l
+00000190: 696e 65da 0c70 726f 6772 616d 5f61 7267  ine..program_arg
+000001a0: 73da 0961 6c6c 5f74 6173 6b73 da0b 666f  s..all_tasks..fo
+000001b0: 756e 645f 6974 656d 73da 0672 6574 7572  und_items..retur
+000001c0: 6e63 0600 0000 0000 0000 0000 0000 0c00  nc..............
+000001d0: 0000 0800 0000 4300 0000 73a2 0000 0067  ......C...s....g
+000001e0: 0064 01a2 017d 0664 025c 027d 077d 087c  .d...}.d.\.}.}.|
+000001f0: 0044 005d 427d 097c 096a 007c 0676 0072  .D.]B}.|.j.|.v.r
+00000200: 1271 0a64 037c 096a 0076 0072 4264 047d  .q.d.|.j.v.rBd.}
+00000210: 0a7c 096a 0064 056b 0272 2064 067d 0a7c  .|.j.d.k.r d.}.|
+00000220: 096a 017d 0b74 02a0 037c 0b7c 017c 027c  .j.}.t...|.|.|.|
+00000230: 0a7c 04a1 055c 027d 077d 087c 0364 0719  .|...\.}.}.|.d..
+00000240: 0072 417c 0364 0719 007c 086b 0272 4164  .rA|.d...|.k.rAd
+00000250: 087c 0564 093c 0001 007c 077c 0866 0253  .|.d.<...|.|.f.S
+00000260: 0071 0a7c 096a 0064 0a6b 0272 4c01 007c  .q.|.j.d.k.rL..|
+00000270: 077c 0866 0253 0071 0a7c 077c 0866 0253  .|.f.S.q.|.|.f.S
+00000280: 0029 0b4e 2904 5a05 6364 6174 655a 0565  .).N).Z.cdateZ.e
+00000290: 6461 7465 da05 666c 6167 73da 0269 6429  date..flags..id)
+000002a0: 02da 0072 0f00 0000 5a03 6d69 64da 0545  ...r....Z.mid..E
+000002b0: 6e74 7279 5a04 6d69 6431 5a04 4578 6974  ntryZ.mid1Z.Exit
+000002c0: da10 7369 6e67 6c65 5f74 6173 6b5f 6e61  ..single_task_na
+000002d0: 6d65 54da 1173 696e 676c 655f 7461 736b  meT..single_task
+000002e0: 5f66 6f75 6e64 da03 6e6d 6529 04da 0374  _found..nme)...t
+000002f0: 6167 da04 7465 7874 da05 7461 736b 73da  ag..text..tasks.
+00000300: 0d67 6574 5f74 6173 6b5f 6e61 6d65 290c  .get_task_name).
+00000310: 7206 0000 0072 0700 0000 7208 0000 0072  r....r....r....r
+00000320: 0900 0000 720a 0000 0072 0b00 0000 5a11  ....r....r....Z.
+00000330: 6b65 7973 5f77 655f 646f 6e74 5f77 616e  keys_we_dont_wan
+00000340: 745a 1074 6865 5f74 6173 6b5f 656c 656d  tZ.the_task_elem
+00000350: 656e 745a 0d74 6865 5f74 6173 6b5f 6e61  entZ.the_task_na
+00000360: 6d65 da05 6368 696c 645a 0974 6173 6b5f  me..childZ.task_
+00000370: 7479 7065 5a07 7461 736b 5f69 64a9 0072  typeZ.task_id..r
+00000380: 1900 0000 fa77 2f55 7365 7273 2f6d 696b  .....w/Users/mik
+00000390: 7275 6269 6e2f 4c69 6272 6172 792f 436c  rubin/Library/Cl
+000003a0: 6f75 6453 746f 7261 6765 2f47 6f6f 676c  oudStorage/Googl
+000003b0: 6544 7269 7665 2d6d 696b 7275 6269 6e40  eDrive-mikrubin@
+000003c0: 676d 6169 6c2e 636f 6d2f 4d79 2044 7269  gmail.com/My Dri
+000003d0: 7665 2f50 7974 686f 6e2f 6d61 7074 6173  ve/Python/maptas
+000003e0: 6b65 722f 6d61 7074 6173 6b65 722f 7372  ker/maptasker/sr
+000003f0: 632f 7072 6f66 696c 6573 2e70 79da 1167  c/profiles.py..g
+00000400: 6574 5f70 726f 6669 6c65 5f74 6173 6b73  et_profile_tasks
+00000410: 1e00 0000 7332 0000 0008 0808 0108 020a  ....s2..........
+00000420: 0102 010a 0104 010a 0104 0106 0104 010a  ................
+00000430: 0108 ff06 0402 ff0c 0208 0202 0108 0502  ................
+00000440: 800a fd02 0208 0102 fd08 0372 1b00 0000  ...........r....
+00000450: da07 7072 6f6a 6563 74da 0770 726f 6669  ..project..profi
+00000460: 6c65 da0b 6f75 7470 7574 5f6c 6973 74da  le..output_list.
+00000470: 0863 6f6c 6f72 6d61 7063 0500 0000 0000  .colormapc......
+00000480: 0000 0000 0000 1200 0000 0d00 0000 4300  ..............C.
+00000490: 0000 7302 0200 0064 017c 0464 0219 0017  ..s....d.|.d....
+000004a0: 007c 0364 0319 0017 0064 0417 007d 0564  .|.d.....d...}.d
+000004b0: 017c 0464 0519 0017 007c 0364 0319 0017  .|.d.....|.d....
+000004c0: 0064 0617 007d 0664 077c 0464 0819 0017  .d...}.d.|.d....
+000004d0: 0064 0917 007c 0517 007d 0764 017c 0464  .d...|...}.d.|.d
+000004e0: 0a19 0017 007c 0364 0319 0017 0064 0b17  .....|.d.....d..
+000004f0: 007d 0864 0c7d 097c 01a0 0064 0da1 017d  .}.d.}.|...d...}
+00000500: 0a7c 0a64 0075 0172 417c 0a6a 0164 0e6b  .|.d.u.rA|.j.d.k
+00000510: 0272 417c 067d 0b6e 0264 0c7d 0b7c 00a0  .rA|.}.n.d.}.|..
+00000520: 0064 0fa1 017d 0c7c 0c64 0075 0172 4e7c  .d...}.|.d.u.rN|
+00000530: 076e 0164 0c7d 0d64 0c7d 0e7c 0364 1019  .n.d.}.d.}.|.d..
+00000540: 0072 707c 01a0 0064 11a1 017d 0e7c 0e64  .rp|...d...}.|.d
+00000550: 0075 0172 7064 127c 0364 0319 009b 0064  .u.rpd.|.d.....d
+00000560: 137c 0e6a 019b 0064 147c 0364 0319 009b  .|.j...d.|.d....
+00000570: 0064 0b9d 077d 0e64 0c7d 0f7c 0364 1519  .d...}.d.}.|.d..
+00000580: 0072 9174 02a0 037c 017c 047c 03a1 037d  .r.t...|.|.|...}
+00000590: 097c 0972 917c 089b 0064 167c 099b 0064  .|.r.|...d.|...d
+000005a0: 177c 0f9b 007c 0d9b 007c 0b9b 0064 187c  .|...|...|...d.|
+000005b0: 0e9b 0064 199d 0a7d 0f7a 0a7c 01a0 0064  ...d...}.z.|...d
+000005c0: 1aa1 016a 017c 0f17 007d 0f57 006e 4304  ...j.|...}.W.nC.
+000005d0: 0074 0479 de01 007d 1001 007a 377c 0364  .t.y...}...z7|.d
+000005e0: 1519 0072 cc74 02a0 037c 017c 047c 03a1  ...r.t...|.|.|..
+000005f0: 037d 097c 0972 c374 059b 0064 197c 089b  .}.|.r.t...d.|..
+00000600: 0064 167c 099b 0064 177c 059b 007c 0d9b  .d.|...d.|...|..
+00000610: 007c 0b9b 007c 0e9b 009d 0a6e 077c 0f74  .|...|.....n.|.t
+00000620: 0517 007c 0d17 007c 0b17 007d 0f6e 087c  ...|...|...}.n.|
+00000630: 0f74 0517 007c 0d17 007c 0b17 007d 0f57  .t...|...|...}.W
+00000640: 0059 0064 007d 107e 106e 0564 007d 107e  .Y.d.}.~.n.d.}.~
+00000650: 1077 0177 007c 0364 1019 0072 f07c 01a0  .w.w.|.d...r.|..
+00000660: 0064 1ba1 016a 017d 117c 0f9b 0064 1c7c  .d...j.}.|...d.|
+00000670: 119b 009d 037d 0f74 067c 047c 037c 0264  .....}.t.|.|.|.d
+00000680: 1d64 1e7c 0f9b 009d 0283 0501 007c 0a7c  .d.|.........|.|
+00000690: 0d7c 097c 0f66 0453 0029 1f4e 7a13 3c73  .|.|.f.S.).Nz.<s
+000006a0: 7061 6e20 7374 796c 653d 2263 6f6c 6f72  pan style="color
+000006b0: 3ada 0d70 726f 6669 6c65 5f63 6f6c 6f72  :..profile_color
+000006c0: da0b 666f 6e74 5f74 6f5f 7573 657a 083e  ..font_to_usez.>
+000006d0: 3c2f 7370 616e 3eda 1664 6973 6162 6c65  </span>..disable
+000006e0: 645f 7072 6f66 696c 655f 636f 6c6f 727a  d_profile_colorz
+000006f0: 123e 5b44 4953 4142 4c45 445d 3c2f 7370  .>[DISABLED]</sp
+00000700: 616e 3e7a 0f20 2073 7479 6c65 3d22 636f  an>z.  style="co
+00000710: 6c6f 723a da13 6c61 756e 6368 6572 5f74  lor:..launcher_t
+00000720: 6173 6b5f 636f 6c6f 727a 1022 5b4c 6175  ask_colorz."[Lau
+00000730: 6e63 6865 7220 5461 736b 5dda 1770 726f  ncher Task]..pro
+00000740: 6669 6c65 5f63 6f6e 6469 7469 6f6e 5f63  file_condition_c
+00000750: 6f6c 6f72 fa01 3e72 0f00 0000 da05 6c69  olor..>r......li
+00000760: 6d69 74da 0474 7275 655a 0f50 726f 6669  mit..trueZ.Profi
+00000770: 6c65 5661 7269 6162 6c65 da05 6465 6275  leVariable..debu
+00000780: 6772 0d00 0000 7a1f 203c 7370 616e 2073  gr....z. <span s
+00000790: 7479 6c65 3d22 636f 6c6f 723a 4772 6565  tyle="color:Gree
+000007a0: 6e59 656c 6c6f 777a 083e 666c 6167 733a  nYellowz.>flags:
+000007b0: 207a 1d3c 2f73 7061 6e3e 3c73 7061 6e20   z.</span><span 
+000007c0: 7374 796c 653d 2263 6f6c 6f72 3a52 6564  style="color:Red
+000007d0: da1a 6469 7370 6c61 795f 7072 6f66 696c  ..display_profil
+000007e0: 655f 636f 6e64 6974 696f 6e73 7a02 2028  e_conditionsz. (
+000007f0: 7a09 293c 2f73 7061 6e3e 20fa 0120 7a07  z.)</span> .. z.
+00000800: 3c2f 7370 616e 3e72 1300 0000 720e 0000  </span>r....r...
+00000810: 007a 0420 4944 3ae9 0200 0000 7a09 5072  .z. ID:.....z.Pr
+00000820: 6f66 696c 653a 2029 07da 0466 696e 6472  ofile: )...findr
+00000830: 1500 0000 da09 636f 6e64 6974 696f 6e5a  ......conditionZ
+00000840: 1770 6172 7365 5f70 726f 6669 6c65 5f63  .parse_profile_c
+00000850: 6f6e 6469 7469 6f6e da09 4578 6365 7074  ondition..Except
+00000860: 696f 6e72 0500 0000 7202 0000 0029 1272  ionr....r....).r
+00000870: 1c00 0000 721d 0000 0072 1e00 0000 7209  ....r....r....r.
+00000880: 0000 0072 1f00 0000 5a12 7072 6f66 696c  ...r....Z.profil
+00000890: 655f 636f 6c6f 725f 6874 6d6c 5a15 6469  e_color_htmlZ.di
+000008a0: 7361 626c 6564 5f70 726f 6669 6c65 5f68  sabled_profile_h
+000008b0: 746d 6c5a 126c 6175 6e63 6865 725f 7461  tmlZ.launcher_ta
+000008c0: 736b 5f68 746d 6c5a 1463 6f6e 6469 7469  sk_htmlZ.conditi
+000008d0: 6f6e 5f63 6f6c 6f72 5f68 746d 6cda 1170  on_color_html..p
+000008e0: 726f 6669 6c65 5f63 6f6e 6469 7469 6f6e  rofile_condition
+000008f0: 7226 0000 00da 0864 6973 6162 6c65 645a  r&.....disabledZ
+00000900: 0c6c 6175 6e63 6865 725f 786d 6cda 086c  .launcher_xml..l
+00000910: 6175 6e63 6865 7272 0d00 0000 da0c 7072  auncherr......pr
+00000920: 6f66 696c 655f 6e61 6d65 da01 655a 0a70  ofile_name..eZ.p
+00000930: 726f 6669 6c65 5f69 6472 1900 0000 7219  rofile_idr....r.
+00000940: 0000 0072 1a00 0000 da12 6275 696c 645f  ...r......build_
+00000950: 7072 6f66 696c 655f 6c69 6e65 4400 0000  profile_lineD...
+00000960: 73c8 0000 0002 0906 0102 ff06 0202 fe02  s...............
+00000970: 0302 fd02 ff02 0706 0102 ff06 0202 fe02  ................
+00000980: 0302 fd02 ff02 0706 0102 ff02 0202 fe02  ................
+00000990: 0302 fd02 ff02 0706 0102 ff06 0202 fe02  ................
+000009a0: 0302 fd02 ff04 060a 0312 0106 0104 0204  ................
+000009b0: 0102 0104 ff10 0304 0908 010a 0108 010c  ................
+000009c0: 0204 0104 ff06 0206 fe02 ff04 0708 0104  ................
+000009d0: 0106 0104 ff04 030c 0202 0102 ff02 0102  ................
+000009e0: ff02 0104 ff02 0106 ff02 ff02 0614 010e  ................
+000009f0: 0108 0104 0106 0104 ff02 0614 fe02 0102  ................
+00000a00: ff02 0102 ff02 0102 ff02 0106 ff0e 0304  ................
+00000a10: fc10 0714 8002 f408 0e0c 010e 0102 0202  ................
+00000a20: 0102 0102 0102 0108 0104 fb0c 0772 3400  .............r4.
+00000a30: 0000 da0c 7072 6f6a 6563 745f 6e61 6d65  ....project_name
+00000a40: da0b 7072 6f66 696c 655f 6964 73da 136c  ..profile_ids..l
+00000a50: 6973 745f 6f66 5f66 6f75 6e64 5f74 6173  ist_of_found_tas
+00000a60: 6b73 da07 6865 6164 696e 67da 1061 6c6c  ks..heading..all
+00000a70: 5f74 6173 6b65 725f 6974 656d 7363 0a00  _tasker_itemsc..
+00000a80: 0000 0000 0000 0000 0000 1600 0000 1000  ................
+00000a90: 0000 4300 0000 7334 0100 0064 017d 0a7c  ..C...s4...d.}.|
+00000aa0: 0344 005d 937d 0b7c 0864 0219 007c 0b19  .D.].}.|.d...|..
+00000ab0: 007d 0c7c 0c64 0375 0072 1301 0064 0353  .}.|.d.u.r...d.S
+00000ac0: 007c 0564 0419 0072 487a 1e7c 0ca0 0064  .|.d...rHz.|...d
+00000ad0: 05a1 016a 017d 0d7c 0564 0419 007c 0d6b  ...j.}.|.d...|.k
+00000ae0: 0372 2657 0071 0464 067c 0964 073c 0074  .r&W.q.d.|.d.<.t
+00000af0: 0264 087c 007c 0264 017c 067c 077c 0583  .d.|.|.d.|.|.|..
+00000b00: 0701 0057 006e 1204 0074 0379 4701 007d  ...W.n...t.yG..}
+00000b10: 0e01 007a 0657 0059 0064 037d 0e7e 0e71  ...z.W.Y.d.}.~.q
+00000b20: 0464 037d 0e7e 0e77 0177 0067 007d 0f64  .d.}.~.w.w.g.}.d
+00000b30: 097d 1074 047c 0c7c 047c 0f7c 057c 0864  .}.t.|.|.|.|.|.d
+00000b40: 0a19 007c 0983 065c 027d 0a7d 1174 057c  ...|...\.}.}.t.|
+00000b50: 017c 0c7c 007c 057c 0783 055c 047d 127d  .|.|.|.|...\.}.}
+00000b60: 137d 147d 0d7c 0564 0b19 0072 7074 067c  .}.}.|.d...rpt.|
+00000b70: 0c7c 077c 057c 0083 0401 0074 07a0 087c  .|.|.|.....t...|
+00000b80: 007c 117c 0a7c 0f7c 027c 0d7c 047c 067c  .|.|.|.|.|.|.|.|
+00000b90: 077c 057c 087c 0964 06a1 0d7d 157c 1572  .|.|.|.d...}.|.r
+00000ba0: 8b7c 0564 0c19 0072 8b7c 0964 0d19 0073  .|.d...r.|.d...s
+00000bb0: 917c 1573 947c 0964 0719 0072 9401 007c  .|.s.|.d...r...|
+00000bc0: 0a53 007c 1573 9771 0471 047c 0a53 0029  .S.|.s.q.q.|.S.)
+00000bd0: 0e61 9c02 0000 0a20 2020 2047 6f20 7468  .a.....    Go th
+00000be0: 726f 7567 6820 5072 6f6a 6563 7427 7320  rough Project's 
+00000bf0: 5072 6f66 696c 6573 2061 6e64 206f 7574  Profiles and out
+00000c00: 7075 7420 6561 6368 0a20 2020 2020 2020  put each.       
+00000c10: 203a 7061 7261 6d20 6f75 7470 7574 5f6c   :param output_l
+00000c20: 6973 743a 206c 6973 7420 6f66 2065 6163  ist: list of eac
+00000c30: 6820 6f75 7470 7574 206c 696e 6520 6765  h output line ge
+00000c40: 6e65 7261 7465 6420 736f 2066 6172 0a20  nerated so far. 
+00000c50: 2020 2020 2020 203a 7061 7261 6d20 7072         :param pr
+00000c60: 6f6a 6563 743a 2050 726f 6a65 6374 2074  oject: Project t
+00000c70: 6f20 7072 6f63 6573 730a 2020 2020 2020  o process.      
+00000c80: 2020 3a70 6172 616d 2070 726f 6a65 6374    :param project
+00000c90: 5f6e 616d 653a 2050 726f 6a65 6374 2773  _name: Project's
+00000ca0: 206e 616d 650a 2020 2020 2020 2020 3a70   name.        :p
+00000cb0: 6172 616d 2070 726f 6669 6c65 5f69 6473  aram profile_ids
+00000cc0: 3a20 6c69 7374 206f 6620 5072 6f66 696c  : list of Profil
+00000cd0: 6573 2069 6e20 5072 6f6a 6563 740a 2020  es in Project.  
+00000ce0: 2020 2020 2020 3a70 6172 616d 206c 6973        :param lis
+00000cf0: 745f 6f66 5f66 6f75 6e64 5f74 6173 6b73  t_of_found_tasks
+00000d00: 3a20 6c69 7374 206f 6620 5461 736b 7320  : list of Tasks 
+00000d10: 666f 756e 640a 2020 2020 2020 2020 3a70  found.        :p
+00000d20: 6172 616d 2070 726f 6772 616d 5f61 7267  aram program_arg
+00000d30: 733a 2072 756e 7469 6d65 2061 7267 756d  s: runtime argum
+00000d40: 656e 7473 0a20 2020 2020 2020 203a 7061  ents.        :pa
+00000d50: 7261 6d20 6865 6164 696e 673a 2074 6865  ram heading: the
+00000d60: 206f 7574 7075 7420 6865 6164 696e 670a   output heading.
+00000d70: 2020 2020 2020 2020 3a70 6172 616d 2063          :param c
+00000d80: 6f6c 6f72 6d61 703a 2074 6865 2063 6f6c  olormap: the col
+00000d90: 6f72 7320 746f 2075 7365 2069 6e20 6f75  ors to use in ou
+00000da0: 7075 740a 2020 2020 2020 2020 3a70 6172  put.        :par
+00000db0: 616d 2061 6c6c 5f74 6173 6b65 725f 6974  am all_tasker_it
+00000dc0: 656d 733a 2061 6c6c 2054 6173 6b65 7220  ems: all Tasker 
+00000dd0: 5072 6f6a 6563 7473 2f50 726f 6669 6c65  Projects/Profile
+00000de0: 732f 5461 736b 732f 5363 656e 6573 0a20  s/Tasks/Scenes. 
+00000df0: 2020 2020 2020 203a 7061 7261 6d20 666f         :param fo
+00000e00: 756e 645f 6974 656d 733a 2061 6c6c 2022  und_items: all "
+00000e10: 666f 756e 6422 2069 7465 6d73 2028 7369  found" items (si
+00000e20: 6e67 6c65 2050 726f 6a65 6374 2f50 726f  ngle Project/Pro
+00000e30: 6669 6c65 2f54 6173 6b29 206e 616d 6520  file/Task) name 
+00000e40: 616e 6420 666c 6167 0a20 2020 2020 2020  and flag.       
+00000e50: 203a 7265 7475 726e 3a20 786d 6c20 656c   :return: xml el
+00000e60: 656d 656e 7420 6f66 2054 6173 6b0a 2020  ement of Task.  
+00000e70: 2020 720f 0000 00da 0c61 6c6c 5f70 726f    r......all_pro
+00000e80: 6669 6c65 734e da13 7369 6e67 6c65 5f70  filesN..single_p
+00000e90: 726f 6669 6c65 5f6e 616d 6572 1300 0000  rofile_namer....
+00000ea0: 54da 1473 696e 676c 655f 7072 6f66 696c  T..single_profil
+00000eb0: 655f 666f 756e 6446 722a 0000 0072 0a00  e_foundFr*...r..
+00000ec0: 0000 da11 6469 7370 6c61 795f 7461 736b  ....display_task
+00000ed0: 6572 6e65 7472 1100 0000 7212 0000 0029  ernetr....r....)
+00000ee0: 0972 2c00 0000 7215 0000 0072 0300 0000  .r,...r....r....
+00000ef0: 722e 0000 0072 1b00 0000 7234 0000 0072  r....r....r4...r
+00000f00: 0400 0000 7216 0000 00da 0b6f 7574 7075  ....r......outpu
+00000f10: 745f 7461 736b 2916 721e 0000 0072 1c00  t_task).r....r..
+00000f20: 0000 7235 0000 0072 3600 0000 7237 0000  ..r5...r6...r7..
+00000f30: 0072 0900 0000 7238 0000 0072 1f00 0000  .r....r8...r....
+00000f40: 7239 0000 0072 0b00 0000 da10 6f75 725f  r9...r......our_
+00000f50: 7461 736b 5f65 6c65 6d65 6e74 da04 6974  task_element..it
+00000f60: 656d 721d 0000 0072 3200 0000 7233 0000  emr....r2...r3..
+00000f70: 00da 0974 6173 6b5f 6c69 7374 7208 0000  ...task_listr...
+00000f80: 00da 0d6f 7572 5f74 6173 6b5f 6e61 6d65  ...our_task_name
+00000f90: 7226 0000 0072 3100 0000 722f 0000 005a  r&...r1...r/...Z
+00000fa0: 0d73 7065 6369 6669 635f 7461 736b 7219  .specific_taskr.
+00000fb0: 0000 0072 1900 0000 721a 0000 00da 1070  ...r....r......p
+00000fc0: 726f 6365 7373 5f70 726f 6669 6c65 73b0  rocess_profiles.
+00000fd0: 0000 0073 8c00 0000 041a 0803 0c01 0801  ...s............
+00000fe0: 0601 0802 0201 0c01 0c01 0401 0801 0201  ................
+00000ff0: 0201 0201 0201 0201 0201 0201 0201 08f9  ................
+00001000: 0e09 0c01 0880 02ff 0402 0401 0201 0201  ................
+00001010: 0201 0201 0201 0601 0201 08fa 020a 0a01  ................
+00001020: 0cff 0805 0e01 0405 0201 0201 0201 0201  ................
+00001030: 0201 0201 0201 0201 0201 0201 0201 0201  ................
+00001040: 0201 04f3 0212 02ff 0602 02fe 0603 02fd  ................
+00001050: 0204 02fc 0605 02fb 0207 0404 04fd 0201  ................
+00001060: 02ff 0403 7243 0000 0029 16da 1578 6d6c  ....rC...)...xml
+00001070: 2e65 7472 6565 2e45 6c65 6d65 6e74 5472  .etree.ElementTr
+00001080: 6565 da03 786d 6c5a 176d 6170 7461 736b  ee..xmlZ.maptask
+00001090: 6572 2e73 7263 2e63 6f6e 6469 7469 6f6e  er.src.condition
+000010a0: da03 7372 6372 2d00 0000 da13 6d61 7074  ..srcr-.....mapt
+000010b0: 6173 6b65 722e 7372 632e 7461 736b 7372  asker.src.tasksr
+000010c0: 1600 0000 da15 6d61 7074 6173 6b65 722e  ......maptasker.
+000010d0: 7372 632e 6f75 7470 7574 6c72 0200 0000  src.outputlr....
+000010e0: 7203 0000 00da 136d 6170 7461 736b 6572  r......maptasker
+000010f0: 2e73 7263 2e73 6861 7265 7204 0000 00da  .src.sharer.....
+00001100: 166d 6170 7461 736b 6572 2e73 7263 2e73  .maptasker.src.s
+00001110: 7973 636f 6e73 7472 0500 0000 da05 6574  ysconstr......et
+00001120: 7265 65da 046c 6973 74da 0464 6963 74da  ree..list..dict.
+00001130: 0574 7570 6c65 da03 7374 7272 1b00 0000  .tuple..strr....
+00001140: 7234 0000 0072 4300 0000 7219 0000 0072  r4...rC...r....r
+00001150: 1900 0000 7219 0000 0072 1a00 0000 da08  ....r....r......
+00001160: 3c6d 6f64 756c 653e 0100 0000 7374 0000  <module>....st..
+00001170: 0008 0d12 0212 010c 030c 010c 020c 0102  ................
+00001180: 0604 0102 ff02 0202 fe02 0302 fd02 0402  ................
+00001190: fc02 0502 fb02 0602 fa0c 070a f902 2604  ..............&.
+000011a0: 0102 ff04 0202 fe02 0302 fd02 0402 fc02  ................
+000011b0: 0502 fb02 060a fa02 6c02 0102 ff04 0202  ........l.......
+000011c0: fe02 0302 fd02 0402 fc02 0502 fb02 0602  ................
+000011d0: fa02 0702 f902 0802 f802 0902 f702 0a02  ................
+000011e0: f604 0b0e f5                             .....
```

### Comparing `maptasker-1.3.1/maptasker/src/__pycache__/progargs.cpython-310.pyc` & `maptasker-1.3.2/maptasker/src/__pycache__/progargs.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar  3 18:37:39 2023 UTC, .py size: 1934 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 6% similar despite different names*

```diff
@@ -1,43 +1,43 @@
-00000000: 6f0d 0d0a 0000 0000 733e 0264 8e07 0000  o.......s>.d....
+00000000: 6f0d 0d0a 0000 0000 918f 1c64 9b07 0000  o..........d....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0003 0000 0040 0000 0073 4200 0000 6400  .....@...sB...d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 0100 6400 6403 6c04 6d05 5a05  m.Z...d.d.l.m.Z.
 00000050: 0100 6400 6404 6c06 6d07 5a07 0100 6405  ..d.d.l.m.Z...d.
 00000060: 6508 6602 6406 6407 8404 5a09 6408 5300  e.f.d.d...Z.d.S.
 00000070: 2909 e900 0000 0029 01da 0347 5549 2901  )......)...GUI).
 00000080: da0b 7072 6f63 6573 735f 636c 6929 01da  ..process_cli)..
 00000090: 0b70 726f 6365 7373 5f67 7569 2901 da0d  .process_gui)...
 000000a0: 4445 4255 475f 5052 4f47 5241 4dda 0863  DEBUG_PROGRAM..c
 000000b0: 6f6c 6f72 6d61 7063 0100 0000 0000 0000  olormapc........
-000000c0: 0000 0000 0300 0000 0300 0000 4300 0000  ............C...
-000000d0: 7330 0000 0074 0072 0a74 017c 0064 0183  s0...t.r.t.|.d..
+000000c0: 0000 0000 0200 0000 0300 0000 4300 0000  ............C...
+000000d0: 7334 0000 0074 0072 0a74 017c 0064 0183  s4...t.r.t.|.d..
 000000e0: 025c 027d 017d 006e 0674 027c 0083 015c  .\.}.}.n.t.|...\
-000000f0: 027d 017d 0074 0372 1464 017d 027c 017c  .}.}.t.r.d.}.|.|
-00000100: 0066 0253 0029 024e 5429 0472 0200 0000  .f.S.).NT).r....
-00000110: 7204 0000 0072 0300 0000 7205 0000 0029  r....r....r....)
-00000120: 0372 0600 0000 5a09 7072 6f67 5f61 7267  .r....Z.prog_arg
-00000130: 73da 0564 6562 7567 a900 7208 0000 00fa  s..debug..r.....
-00000140: 772f 5573 6572 732f 6d69 6b72 7562 696e  w/Users/mikrubin
-00000150: 2f4c 6962 7261 7279 2f43 6c6f 7564 5374  /Library/CloudSt
-00000160: 6f72 6167 652f 476f 6f67 6c65 4472 6976  orage/GoogleDriv
-00000170: 652d 6d69 6b72 7562 696e 4067 6d61 696c  e-mikrubin@gmail
-00000180: 2e63 6f6d 2f4d 7920 4472 6976 652f 5079  .com/My Drive/Py
-00000190: 7468 6f6e 2f6d 6170 7461 736b 6572 2f6d  thon/maptasker/m
-000001a0: 6170 7461 736b 6572 2f73 7263 2f70 726f  aptasker/src/pro
-000001b0: 6761 7267 732e 7079 da15 6765 745f 7072  gargs.py..get_pr
-000001c0: 6f67 7261 6d5f 6172 6775 6d65 6e74 7319  ogram_arguments.
-000001d0: 0000 0073 1800 0000 0402 0804 02fd 0201  ...s............
-000001e0: 0401 0608 02fd 0201 0201 0404 0401 0802  ................
-000001f0: 720a 0000 004e 290a da14 6d61 7074 6173  r....N)...maptas
-00000200: 6b65 722e 7372 632e 636f 6e66 6967 7202  ker.src.configr.
-00000210: 0000 005a 146d 6170 7461 736b 6572 2e73  ...Z.maptasker.s
-00000220: 7263 2e72 756e 636c 6972 0300 0000 5a14  rc.runclir....Z.
-00000230: 6d61 7074 6173 6b65 722e 7372 632e 7275  maptasker.src.ru
-00000240: 6e67 7569 7204 0000 00da 166d 6170 7461  nguir......mapta
-00000250: 736b 6572 2e73 7263 2e73 7973 636f 6e73  sker.src.syscons
-00000260: 7472 0500 0000 da04 6469 6374 720a 0000  tr......dictr...
-00000270: 0072 0800 0000 7208 0000 0072 0800 0000  .r....r....r....
-00000280: 7209 0000 00da 083c 6d6f 6475 6c65 3e01  r......<module>.
-00000290: 0000 0073 0a00 0000 0c0e 0c01 0c01 0c02  ...s............
-000002a0: 1206                                     ..
+000000f0: 027d 017d 0074 0372 1664 017c 0164 023c  .}.}.t.r.d.|.d.<
+00000100: 007c 017c 0066 0253 0029 034e 54da 0564  .|.|.f.S.).NT..d
+00000110: 6562 7567 2904 7202 0000 0072 0400 0000  ebug).r....r....
+00000120: 7203 0000 0072 0500 0000 2902 7206 0000  r....r....).r...
+00000130: 005a 0970 726f 675f 6172 6773 a900 7208  .Z.prog_args..r.
+00000140: 0000 00fa 772f 5573 6572 732f 6d69 6b72  ....w/Users/mikr
+00000150: 7562 696e 2f4c 6962 7261 7279 2f43 6c6f  ubin/Library/Clo
+00000160: 7564 5374 6f72 6167 652f 476f 6f67 6c65  udStorage/Google
+00000170: 4472 6976 652d 6d69 6b72 7562 696e 4067  Drive-mikrubin@g
+00000180: 6d61 696c 2e63 6f6d 2f4d 7920 4472 6976  mail.com/My Driv
+00000190: 652f 5079 7468 6f6e 2f6d 6170 7461 736b  e/Python/maptask
+000001a0: 6572 2f6d 6170 7461 736b 6572 2f73 7263  er/maptasker/src
+000001b0: 2f70 726f 6761 7267 732e 7079 da15 6765  /progargs.py..ge
+000001c0: 745f 7072 6f67 7261 6d5f 6172 6775 6d65  t_program_argume
+000001d0: 6e74 7319 0000 0073 1800 0000 0402 0804  nts....s........
+000001e0: 02fd 0201 0401 0608 02fd 0201 0201 0404  ................
+000001f0: 0801 0802 720a 0000 004e 290a da14 6d61  ....r....N)...ma
+00000200: 7074 6173 6b65 722e 7372 632e 636f 6e66  ptasker.src.conf
+00000210: 6967 7202 0000 005a 146d 6170 7461 736b  igr....Z.maptask
+00000220: 6572 2e73 7263 2e72 756e 636c 6972 0300  er.src.runclir..
+00000230: 0000 5a14 6d61 7074 6173 6b65 722e 7372  ..Z.maptasker.sr
+00000240: 632e 7275 6e67 7569 7204 0000 00da 166d  c.runguir......m
+00000250: 6170 7461 736b 6572 2e73 7263 2e73 7973  aptasker.src.sys
+00000260: 636f 6e73 7472 0500 0000 da04 6469 6374  constr......dict
+00000270: 720a 0000 0072 0800 0000 7208 0000 0072  r....r....r....r
+00000280: 0800 0000 7209 0000 00da 083c 6d6f 6475  ....r......<modu
+00000290: 6c65 3e01 0000 0073 0a00 0000 0c0e 0c01  le>....s........
+000002a0: 0c01 0c02 1206                           ......
```

### Comparing `maptasker-1.3.1/maptasker/src/__pycache__/projects.cpython-310.pyc` & `maptasker-1.3.2/maptasker/src/__pycache__/projects.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 17 19:28:02 2023 UTC, .py size: 14410 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 12% similar despite different names*

```diff
@@ -1,447 +1,463 @@
-00000000: 6f0d 0d0a 0000 0000 42bf 1464 4a38 0000  o.......B..dJ8..
+00000000: 6f0d 0d0a 0000 0000 145e 2c64 a73a 0000  o........^,d.:..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
-00000020: 0014 0000 0040 0000 0073 6a01 0000 6400  .....@...sj...d.
+00000020: 0014 0000 0040 0000 0073 7601 0000 6400  .....@...sv...d.
 00000030: 6401 6c00 5a01 6400 6402 6c02 6d03 5a03  d.l.Z.d.d.l.m.Z.
 00000040: 0100 6400 6403 6c02 6d04 5a04 0100 6400  ..d.d.l.m.Z...d.
 00000050: 6404 6c05 6d06 5a06 0100 6400 6405 6c07  d.l.m.Z...d.d.l.
 00000060: 6d08 5a08 0100 6400 6406 6c09 6d0a 5a0a  m.Z...d.d.l.m.Z.
 00000070: 0100 6400 6407 6c0b 6d0c 5a0c 0100 6400  ..d.d.l.m.Z...d.
 00000080: 6408 6c0d 6d0e 5a0e 0100 6400 6409 6c0f  d.l.m.Z...d.d.l.
 00000090: 6d10 5a10 0100 6400 6401 6c11 6d12 0200  m.Z...d.d.l.m...
 000000a0: 0100 6d13 5a13 0100 6400 640a 6c14 6d15  ..m.Z...d.d.l.m.
-000000b0: 5a15 0100 640b 6516 640c 6516 640d 6516  Z...d.e.d.e.d.e.
-000000c0: 640e 6517 640f 6517 6410 6518 6411 6517  d.e.d.e.d.e.d.e.
-000000d0: 6412 6517 6413 6516 6612 6414 6415 8404  d.e.d.e.f.d.d...
-000000e0: 5a19 6416 6501 6a1a 6411 6517 6417 6518  Z.d.e.j.d.e.d.e.
-000000f0: 6413 6518 6608 6418 6419 8404 5a1b 641a  d.e.f.d.d...Z.d.
-00000100: 6516 640c 6516 640b 6516 641b 6518 6411  e.d.e.d.e.d.e.d.
-00000110: 6517 640e 6517 6410 6518 6412 6517 640f  e.d.e.d.e.d.e.d.
-00000120: 6517 6413 6401 6614 641c 641d 8404 5a1c  e.d.d.f.d.d...Z.
-00000130: 640e 6517 6411 6517 6416 6501 6a1a 641b  d.e.d.e.d.e.j.d.
-00000140: 6518 640f 6517 6410 6518 640b 6516 641e  e.d.e.d.e.d.e.d.
-00000150: 6518 6413 651d 6612 641f 6420 8404 5a1e  e.d.e.f.d.d ..Z.
-00000160: 640f 6517 640b 6516 6410 6518 640d 6516  d.e.d.e.d.e.d.e.
-00000170: 640c 6516 6421 6501 6a1a 6411 6517 640e  d.e.d!e.j.d.e.d.
-00000180: 6517 6412 6517 6413 6516 6614 6422 6423  e.d.e.d.e.f.d"d#
-00000190: 8404 5a1f 6401 5300 2924 e900 0000 004e  ..Z.d.S.)$.....N
-000001a0: 2901 da09 6d79 5f6f 7574 7075 7429 01da  )...my_output)..
-000001b0: 1272 6566 7265 7368 5f6f 7572 5f6f 7574  .refresh_our_out
-000001c0: 7075 7429 01da 1070 726f 6365 7373 5f70  put)...process_p
-000001d0: 726f 6669 6c65 7329 01da 0573 6861 7265  rofiles)...share
-000001e0: 2901 da0b 6765 745f 6b69 645f 6170 7029  )...get_kid_app)
-000001f0: 01da 0c67 6574 5f70 7269 6f72 6974 7929  ...get_priority)
-00000200: 01da 0767 6574 5f69 6473 2901 da16 7072  ...get_ids)...pr
-00000210: 6f63 6573 735f 7072 6f6a 6563 745f 7363  ocess_project_sc
-00000220: 656e 6573 2901 da0a 4e4f 5f50 524f 4649  enes)...NO_PROFI
-00000230: 4c45 da0b 6f75 7470 7574 5f6c 6973 74da  LE..output_list.
-00000240: 0b66 6f75 6e64 5f74 6173 6b73 da19 7072  .found_tasks..pr
-00000250: 6f6a 6563 7473 5f77 6974 686f 7574 5f70  ojects_without_p
-00000260: 726f 6669 6c65 73da 0c70 726f 6772 616d  rofiles..program
-00000270: 5f61 7267 73da 0b66 6f75 6e64 5f69 7465  _args..found_ite
-00000280: 6d73 da07 6865 6164 696e 67da 0863 6f6c  ms..heading..col
-00000290: 6f72 6d61 70da 1061 6c6c 5f74 6173 6b65  ormap..all_taske
-000002a0: 725f 6974 656d 73da 0672 6574 7572 6e63  r_items..returnc
-000002b0: 0800 0000 0000 0000 0000 0000 0900 0000  ................
-000002c0: 0a00 0000 4300 0000 733e 0000 0064 017d  ....C...s>...d.}
-000002d0: 0874 007c 047c 007c 057c 027c 017c 087c  .t.|.|.|.|.|.|.|
-000002e0: 067c 037c 0783 0901 0074 017c 067c 037c  .|.|.....t.|.|.|
-000002f0: 0064 0264 0183 0501 0074 0274 03a0 047c  .d.d.....t.t...|
-00000300: 01a1 01a0 05a1 0083 0153 0029 0361 cc02  .........S.).a..
-00000310: 0000 0a20 2020 2047 6f20 7468 726f 7567  ...    Go throug
-00000320: 6820 616c 6c20 5072 6f6a 6563 7473 2c20  h all Projects, 
-00000330: 7072 6f63 6573 7320 7468 656d 2061 6e64  process them and
-00000340: 2074 6865 6972 2050 726f 6669 6c65 7320   their Profiles 
-00000350: 616e 6420 5461 736b 7320 2861 6e64 2061  and Tasks (and a
-00000360: 6464 2074 6f20 6f75 7220 6f75 7470 7574  dd to our output
-00000370: 206c 6973 7429 0a20 2020 2020 2020 203a   list).        :
-00000380: 7061 7261 6d20 6f75 7470 7574 5f6c 6973  param output_lis
-00000390: 743a 206c 6973 7420 6f66 206f 7574 7075  t: list of outpu
-000003a0: 7420 6c69 6e65 7320 6765 6e65 7261 7465  t lines generate
-000003b0: 6420 7468 7573 2066 6172 0a20 2020 2020  d thus far.     
-000003c0: 2020 203a 7061 7261 6d20 666f 756e 645f     :param found_
-000003d0: 7461 736b 733a 206c 6973 7420 6f66 2054  tasks: list of T
-000003e0: 6173 6b73 2066 6f75 6e64 2074 6875 7320  asks found thus 
-000003f0: 6661 720a 2020 2020 2020 2020 3a70 6172  far.        :par
-00000400: 616d 2070 726f 6a65 6374 735f 7769 7468  am projects_with
-00000410: 6f75 745f 7072 6f66 696c 6573 3a20 6c69  out_profiles: li
-00000420: 7374 206f 6620 5072 6f6a 6563 7473 2074  st of Projects t
-00000430: 6861 7420 646f 6e27 7420 6861 7665 2061  hat don't have a
-00000440: 6e79 2050 726f 6669 6c65 730a 2020 2020  ny Profiles.    
-00000450: 2020 2020 3a70 6172 616d 2070 726f 6772      :param progr
-00000460: 616d 5f61 7267 733a 2072 756e 7469 6d65  am_args: runtime
-00000470: 2061 7267 756d 656e 7473 0a20 2020 2020   arguments.     
-00000480: 2020 203a 7061 7261 6d20 666f 756e 645f     :param found_
-00000490: 6974 656d 733a 2069 6620 7365 6172 6368  items: if search
-000004a0: 696e 6720 666f 7220 6120 7369 6e67 6c65  ing for a single
-000004b0: 2050 726f 6a65 6374 2f50 726f 6669 6c65   Project/Profile
-000004c0: 2f54 6173 6b2c 206e 616d 6520 6f66 2073  /Task, name of s
-000004d0: 696e 676c 6520 6974 656d 0a20 2020 2020  ingle item.     
-000004e0: 2020 203a 7061 7261 6d20 6865 6164 696e     :param headin
-000004f0: 673a 2068 6561 6469 6e67 2070 7269 6e74  g: heading print
-00000500: 6564 0a20 2020 2020 2020 203a 7061 7261  ed.        :para
-00000510: 6d20 636f 6c6f 726d 6170 3a20 636f 6c6f  m colormap: colo
-00000520: 7273 2074 6f20 7573 6520 696e 206f 7574  rs to use in out
-00000530: 7075 740a 2020 2020 2020 2020 3a70 6172  put.        :par
-00000540: 616d 2061 6c6c 5f74 6173 6b65 725f 6974  am all_tasker_it
-00000550: 656d 733a 2061 6c6c 2050 726f 6a65 6374  ems: all Project
-00000560: 2f50 726f 6669 6c65 2f54 6173 6b2f 5363  /Profile/Task/Sc
-00000570: 656e 652f 5072 6566 6572 656e 6365 2054  ene/Preference T
-00000580: 6173 6b65 7220 786d 6c20 656c 656d 656e  asker xml elemen
-00000590: 7473 0a20 2020 2020 2020 203a 7265 7475  ts.        :retu
-000005a0: 726e 3a20 6c69 7374 206f 6620 5461 736b  rn: list of Task
-000005b0: 7320 666f 756e 6420 7468 7573 2066 6172  s found thus far
-000005c0: 2c20 7769 7468 2064 7570 6c69 6361 7465  , with duplicate
-000005d0: 7320 7265 6d6f 7665 640a 2020 2020 da00  s removed.    ..
-000005e0: e903 0000 0029 06da 1070 726f 6365 7373  .....)...process
-000005f0: 5f70 726f 6a65 6374 7372 0200 0000 da04  _projectsr......
-00000600: 6c69 7374 da04 6469 6374 da08 6672 6f6d  list..dict..from
-00000610: 6b65 7973 da04 6b65 7973 2909 720b 0000  keys..keys).r...
-00000620: 0072 0c00 0000 720d 0000 0072 0e00 0000  .r....r....r....
-00000630: 720f 0000 0072 1000 0000 7211 0000 0072  r....r....r....r
-00000640: 1200 0000 da10 6f75 725f 7461 736b 5f65  ......our_task_e
-00000650: 6c65 6d65 6e74 a900 721c 0000 00fa 772f  lement..r.....w/
-00000660: 5573 6572 732f 6d69 6b72 7562 696e 2f4c  Users/mikrubin/L
-00000670: 6962 7261 7279 2f43 6c6f 7564 5374 6f72  ibrary/CloudStor
-00000680: 6167 652f 476f 6f67 6c65 4472 6976 652d  age/GoogleDrive-
-00000690: 6d69 6b72 7562 696e 4067 6d61 696c 2e63  mikrubin@gmail.c
-000006a0: 6f6d 2f4d 7920 4472 6976 652f 5079 7468  om/My Drive/Pyth
-000006b0: 6f6e 2f6d 6170 7461 736b 6572 2f6d 6170  on/maptasker/map
-000006c0: 7461 736b 6572 2f73 7263 2f70 726f 6a65  tasker/src/proje
-000006d0: 6374 732e 7079 da23 7072 6f63 6573 735f  cts.py.#process_
-000006e0: 7072 6f6a 6563 7473 5f61 6e64 5f74 6865  projects_and_the
-000006f0: 6972 5f70 726f 6669 6c65 7320 0000 0073  ir_profiles ...s
-00000700: 1c00 0000 0416 0202 0201 0201 0201 0201  ................
-00000710: 0201 0201 0201 0201 0201 04f7 100b 1204  ................
-00000720: 721e 0000 00da 0770 726f 6a65 6374 da12  r......project..
-00000730: 7072 6f6a 6563 745f 636f 6c6f 725f 6874  project_color_ht
-00000740: 6d6c 6303 0000 0000 0000 0000 0000 0006  mlc.............
-00000750: 0000 0004 0000 0043 0000 0073 5400 0000  .......C...sT...
-00000760: 6401 7d03 7c00 a000 6402 a101 7d04 7c04  d.}.|...d...}.|.
-00000770: 6403 7501 7228 7c04 a000 6404 a101 7d05  d.u.r(|...d...}.
-00000780: 7c05 6403 7501 7228 7c05 6a01 6403 7501  |.d.u.r(|.j.d.u.
-00000790: 7228 6405 7c01 6406 1900 1700 6407 7c05  r(d.|.d.....d.|.
-000007a0: 6a01 9b00 6408 9d03 1700 7c02 1700 7d03  j...d.....|...}.
-000007b0: 7c03 5300 2909 611e 0100 000a 2020 2020  |.S.).a.....    
-000007c0: 4966 2050 726f 6a65 6374 2068 6173 2061  If Project has a
-000007d0: 206c 6175 6e63 6865 7220 5461 736b 2c20   launcher Task, 
-000007e0: 6765 7420 6974 0a20 2020 2020 2020 203a  get it.        :
-000007f0: 7061 7261 6d20 7072 6f6a 6563 743a 2078  param project: x
-00000800: 6d6c 2065 6c65 6d65 6e74 206f 6620 5072  ml element of Pr
-00000810: 6f6a 6563 7420 7765 2061 7265 2070 726f  oject we are pro
-00000820: 6365 7373 696e 670a 2020 2020 2020 2020  cessing.        
-00000830: 3a70 6172 616d 2063 6f6c 6f72 6d61 703a  :param colormap:
-00000840: 2063 6f6c 6f72 7320 746f 2075 7365 2069   colors to use i
-00000850: 6e20 6f75 7470 7574 0a20 2020 2020 2020  n output.       
-00000860: 203a 7061 7261 6d20 7072 6f6a 6563 745f   :param project_
-00000870: 636f 6c6f 725f 6874 6d6c 3a20 6874 6d6c  color_html: html
-00000880: 2074 6f20 7573 6520 7468 6174 2064 6566   to use that def
-00000890: 696e 6573 2074 6865 2063 6f6c 6f72 0a20  ines the color. 
-000008a0: 2020 2020 2020 203a 7265 7475 726e 3a20         :return: 
-000008b0: 696e 666f 726d 6174 696f 6e20 7265 6c61  information rela
-000008c0: 7465 6420 746f 206c 6175 6e63 6865 7220  ted to launcher 
-000008d0: 5461 736b 0a20 2020 2072 1400 0000 5a05  Task.    r....Z.
-000008e0: 5368 6172 654e da01 747a 1620 3c73 7061  ShareN..tz. <spa
-000008f0: 6e20 7374 796c 6520 3d20 2263 6f6c 6f72  n style = "color
-00000900: 3ada 136c 6175 6e63 6865 725f 7461 736b  :..launcher_task
-00000910: 5f63 6f6c 6f72 7a18 223c 2f73 7061 6e3e  _colorz."</span>
-00000920: 5b4c 6175 6e63 6865 7220 5461 736b 3a20  [Launcher Task: 
-00000930: 7a02 5d20 2902 da04 6669 6e64 da04 7465  z.] )...find..te
-00000940: 7874 2906 721f 0000 0072 1100 0000 7220  xt).r....r....r 
-00000950: 0000 00da 126c 6175 6e63 6865 725f 7461  .....launcher_ta
-00000960: 736b 5f69 6e66 6f5a 0d73 6861 7265 5f65  sk_infoZ.share_e
-00000970: 6c65 6d65 6e74 5a15 6c61 756e 6368 6572  lementZ.launcher
-00000980: 5f74 6173 6b5f 656c 656d 656e 7472 1c00  _task_elementr..
-00000990: 0000 721c 0000 0072 1d00 0000 da11 6765  ..r....r......ge
-000009a0: 745f 6c61 756e 6368 6572 5f74 6173 6b4a  t_launcher_taskJ
-000009b0: 0000 0073 1c00 0000 040a 0a01 0801 0a01  ...s............
-000009c0: 1201 0202 0601 02ff 0c02 02fe 0203 02fd  ................
-000009d0: 02ff 0406 7226 0000 00da 0874 6173 6b5f  ....r&.....task_
-000009e0: 6964 73da 0c70 726f 6a65 6374 5f6e 616d  ids..project_nam
-000009f0: 6563 0900 0000 0000 0000 0000 0000 0f00  ec..............
-00000a00: 0000 0f00 0000 4300 0000 73be 0000 0064  ......C...s....d
-00000a10: 017d 097c 0044 005d 587d 0a7c 0a7c 0176  .}.|.D.]X}.|.|.v
-00000a20: 0172 5c7c 0864 0219 0073 5c7c 0864 0319  .r\|.d...s\|.d..
-00000a30: 0073 5c74 00a0 017c 0a7c 0167 0064 047c  .s\t...|.|.g.d.|
-00000a40: 0764 0519 00a1 055c 027d 0b7d 0c7c 01a0  .d.....\.}.}.|..
-00000a50: 027c 0aa1 0101 007c 0972 437c 0072 437c  .|.....|.rC|.rC|
-00000a60: 0864 0219 0073 437c 0864 0319 0073 4374  .d...sC|.d...sCt
-00000a70: 037c 047c 057c 0264 0664 077c 0464 0819  .|.|.|.d.d.|.d..
-00000a80: 009b 0064 097c 039b 0064 0a9d 0583 0501  ...d.|...d......
-00000a90: 0064 0b7d 097c 0c9b 0064 0c7c 039b 0064  .d.}.|...d.|...d
-00000aa0: 0d9d 0467 017d 0d74 00a0 047c 027c 0c7c  ...g.}.t...|.|.|
-00000ab0: 0b7c 0d7c 0374 057c 017c 067c 047c 057c  .|.|.t.|.|.|.|.|
-00000ac0: 077c 08a1 0c7d 0e71 0464 0e53 0029 0f61  .|...}.q.d.S.).a
-00000ad0: 6602 0000 0a20 2020 2050 726f 6365 7373  f....    Process
-00000ae0: 2061 6c6c 2054 6173 6b73 2069 6e20 5072   all Tasks in Pr
-00000af0: 6f6a 6563 7420 7468 6174 2061 7265 206e  oject that are n
-00000b00: 6f74 2072 6566 6572 656e 6365 6420 6279  ot referenced by
-00000b10: 2061 2050 726f 6669 6c65 0a20 2020 2020   a Profile.     
-00000b20: 2020 203a 7061 7261 6d20 7461 736b 5f69     :param task_i
-00000b30: 6473 3a20 4c69 7374 206f 6620 5461 736b  ds: List of Task
-00000b40: 2049 4473 0a20 2020 2020 2020 203a 7061   IDs.        :pa
-00000b50: 7261 6d20 666f 756e 645f 7461 736b 733a  ram found_tasks:
-00000b60: 206c 6973 7420 6f66 2054 6173 6b73 2066   list of Tasks f
-00000b70: 6f75 6e64 2074 6875 7320 6661 720a 2020  ound thus far.  
-00000b80: 2020 2020 2020 3a70 6172 616d 206f 7574        :param out
-00000b90: 7075 745f 6c69 7374 3a20 6f75 7470 7574  put_list: output
-00000ba0: 206c 696e 6573 2067 656e 6572 6174 6564   lines generated
-00000bb0: 2074 6875 7320 6661 7220 6f6e 746f 2077   thus far onto w
-00000bc0: 6869 6368 2077 6520 7769 6c6c 2061 7070  hich we will app
-00000bd0: 656e 6420 6d6f 7265 0a20 2020 2020 2020  end more.       
-00000be0: 203a 7061 7261 6d20 7072 6f6a 6563 745f   :param project_
-00000bf0: 6e61 6d65 3a20 6e61 6d65 206f 6620 6375  name: name of cu
-00000c00: 7272 656e 7420 5072 6f6a 6563 740a 2020  rrent Project.  
-00000c10: 2020 2020 2020 3a70 6172 616d 2063 6f6c        :param col
-00000c20: 6f72 6d61 703a 2063 6f6c 6f72 7320 746f  ormap: colors to
-00000c30: 2075 7365 2069 6e20 6f75 7470 7574 0a20   use in output. 
-00000c40: 2020 2020 2020 203a 7061 7261 6d20 7072         :param pr
-00000c50: 6f67 7261 6d5f 6172 6773 3a20 7275 6e74  ogram_args: runt
-00000c60: 696d 6520 6172 6775 6d65 6e74 730a 2020  ime arguments.  
-00000c70: 2020 2020 2020 3a70 6172 616d 2068 6561        :param hea
-00000c80: 6469 6e67 3a20 6375 7272 656e 7420 6865  ding: current he
-00000c90: 6164 696e 670a 2020 2020 2020 2020 3a70  ading.        :p
-00000ca0: 6172 616d 2061 6c6c 5f74 6173 6b65 725f  aram all_tasker_
-00000cb0: 6974 656d 733a 2061 6c6c 2050 726f 6a65  items: all Proje
-00000cc0: 6374 732f 5072 6f66 696c 6573 2f54 6173  cts/Profiles/Tas
-00000cd0: 6b73 2f53 6365 6e65 730a 2020 2020 2020  ks/Scenes.      
-00000ce0: 2020 3a70 6172 616d 2066 6f75 6e64 5f69    :param found_i
-00000cf0: 7465 6d73 3a20 7369 6e67 6c65 2069 7465  tems: single ite
-00000d00: 6d20 6e61 6d65 2066 6f72 2050 726f 6a65  m name for Proje
-00000d10: 6374 2f50 726f 6669 6c65 2f54 6173 6b0a  ct/Profile/Task.
-00000d20: 2020 2020 2020 2020 3a72 6574 7572 6e3a          :return:
-00000d30: 206e 6f6e 650a 2020 2020 54da 1473 696e   none.    T..sin
-00000d40: 676c 655f 7072 6f66 696c 655f 666f 756e  gle_profile_foun
-00000d50: 64da 1173 696e 676c 655f 7461 736b 5f66  d..single_task_f
-00000d60: 6f75 6e64 7214 0000 00da 0961 6c6c 5f74  oundr......all_t
-00000d70: 6173 6b73 e904 0000 007a 173c 6272 3e3c  asks.....z.<br><
-00000d80: 7370 616e 2073 7479 6c65 3d22 636f 6c6f  span style="colo
-00000d90: 723a da0a 7461 736b 5f63 6f6c 6f72 7a33  r:..task_colorz3
-00000da0: 223e 266e 6273 703b 266e 6273 703b 266e  ">&nbsp;&nbsp;&n
-00000db0: 6273 703b 5468 6520 666f 6c6c 6f77 696e  bsp;The followin
-00000dc0: 6720 5461 736b 7320 696e 2050 726f 6a65  g Tasks in Proje
-00000dd0: 6374 207a 2520 6172 6520 6e6f 7420 696e  ct z% are not in
-00000de0: 2061 6e79 2050 726f 6669 6c65 2e2e 2e3c   any Profile...<
-00000df0: 2f73 7061 6e3e 3c62 723e 467a 2f20 3c65  /span><br>Fz/ <e
-00000e00: 6d3e 284e 6f74 2072 6566 6572 656e 6365  m>(Not reference
-00000e10: 6420 6279 2061 6e79 2050 726f 6669 6c65  d by any Profile
-00000e20: 2069 6e20 5072 6f6a 6563 7420 7a06 293c   in Project z.)<
-00000e30: 2f65 6d3e 4e29 06da 0574 6173 6b73 5a0d  /em>N)...tasksZ.
-00000e40: 6765 745f 7461 736b 5f6e 616d 65da 0672  get_task_name..r
-00000e50: 656d 6f76 6572 0200 0000 5a0b 6f75 7470  emover....Z.outp
-00000e60: 7574 5f74 6173 6b72 0a00 0000 290f 7227  ut_taskr....).r'
-00000e70: 0000 0072 0c00 0000 720b 0000 0072 2800  ...r....r....r(.
-00000e80: 0000 7211 0000 0072 0e00 0000 7210 0000  ..r....r....r...
-00000e90: 0072 1200 0000 720f 0000 005a 126f 7574  .r....r....Z.out
-00000ea0: 7075 745f 7468 655f 6865 6164 696e 675a  put_the_headingZ
-00000eb0: 0674 6865 5f69 6472 1b00 0000 5a0d 6f75  .the_idr....Z.ou
-00000ec0: 725f 7461 736b 5f6e 616d 655a 0974 6173  r_task_nameZ.tas
-00000ed0: 6b5f 6c69 7374 5a04 6b61 6b61 721c 0000  k_listZ.kakar...
-00000ee0: 0072 1c00 0000 721d 0000 00da 1574 6173  .r....r......tas
-00000ef0: 6b73 5f6e 6f74 5f69 6e5f 7072 6f66 696c  ks_not_in_profil
-00000f00: 6573 6500 0000 7368 0000 0002 1a02 ff08  ese...sh........
-00000f10: 0508 0206 0202 fe06 0302 fd04 060e 0108  ................
-00000f20: ff0a 0402 0402 ff02 0202 fe06 0302 fd06  ................
-00000f30: 0402 fc02 0602 0102 0102 0102 0102 0206  ................
-00000f40: 0104 ff02 0206 fe04 fa04 0c06 0402 0106  ................
-00000f50: ff04 ff04 0602 0102 0102 0102 0102 0102  ................
-00000f60: 0102 0102 0102 0102 0102 0102 0104 f402  ................
-00000f70: 8004 0e72 3000 0000 7225 0000 0063 0800  ...r0...r%...c..
-00000f80: 0000 0000 0000 0000 0000 0a00 0000 0b00  ................
-00000f90: 0000 4300 0000 7386 0000 0064 0104 007d  ..C...s....d...}
-00000fa0: 087d 097c 0064 0219 0064 036b 0272 1374  .}.|.d...d.k.r.t
-00000fb0: 007c 0283 017d 0874 017c 0264 0483 027d  .|...}.t.|.d...}
-00000fc0: 097c 0064 0519 0072 2f7c 037c 0064 0519  .|.d...r/|.|.d..
-00000fd0: 006b 0372 1f64 0653 0064 067c 0464 073c  .k.r.d.S.d.|.d.<
-00000fe0: 0074 0264 047c 067c 0364 017c 057c 017c  .t.d.|.|.d.|.|.|
-00000ff0: 0083 0701 0064 0453 0074 037c 017c 007c  .....d.S.t.|.|.|
-00001000: 0664 0864 097c 039b 0064 0a7c 079b 007c  .d.d.|...d.|...|
-00001010: 099b 007c 089b 009d 0683 0501 0064 0453  ...|.........d.S
-00001020: 0029 0b61 6f02 0000 0a20 2020 2041 6464  .).ao....    Add
-00001030: 2065 7874 7261 2069 6e66 6f20 746f 2050   extra info to P
-00001040: 726f 6a65 6374 206f 7574 7075 7420 6c69  roject output li
-00001050: 6e65 2061 7320 6170 7072 6f70 7269 6174  ne as appropriat
-00001060: 6520 616e 6420 7468 656e 206f 7574 7075  e and then outpu
-00001070: 7420 6974 2e0a 2020 2020 2020 2020 3a70  t it..        :p
-00001080: 6172 616d 2070 726f 6772 616d 5f61 7267  aram program_arg
-00001090: 733a 2072 756e 7469 6d65 2061 7267 756d  s: runtime argum
-000010a0: 656e 7473 0a20 2020 2020 2020 203a 7061  ents.        :pa
-000010b0: 7261 6d20 636f 6c6f 726d 6170 3a20 636f  ram colormap: co
-000010c0: 6c6f 7273 2074 6f20 7573 6520 696e 2070  lors to use in p
-000010d0: 7574 7075 740a 2020 2020 2020 2020 3a70  utput.        :p
-000010e0: 6172 616d 2070 726f 6a65 6374 3a20 5072  aram project: Pr
-000010f0: 6f6a 6563 7420 786d 6c20 656c 656d 656e  oject xml elemen
-00001100: 740a 2020 2020 2020 2020 3a70 6172 616d  t.        :param
-00001110: 2070 726f 6a65 6374 5f6e 616d 653a 206e   project_name: n
-00001120: 616d 6520 6f66 2050 726f 6a65 6374 0a20  ame of Project. 
-00001130: 2020 2020 2020 203a 7061 7261 6d20 666f         :param fo
-00001140: 756e 645f 6974 656d 733a 2073 696e 676c  und_items: singl
-00001150: 6520 6e61 6d65 2066 6f72 2050 726f 6a65  e name for Proje
-00001160: 6374 2f50 726f 6669 6c65 2f54 6173 6b20  ct/Profile/Task 
-00001170: 6966 2070 726f 7669 6465 640a 2020 2020  if provided.    
-00001180: 2020 2020 3a70 6172 616d 2068 6561 6469      :param headi
-00001190: 6e67 3a20 6c61 7374 206f 7574 7075 7420  ng: last output 
-000011a0: 6865 6164 696e 670a 2020 2020 2020 2020  heading.        
-000011b0: 3a70 6172 616d 206f 7574 7075 745f 6c69  :param output_li
-000011c0: 7374 3a20 6c69 7374 206f 6620 6f75 7470  st: list of outp
-000011d0: 7574 206c 696e 6573 2067 656e 6572 6174  ut lines generat
-000011e0: 6564 2074 6875 7320 6661 720a 2020 2020  ed thus far.    
-000011f0: 2020 2020 3a70 6172 616d 206c 6175 6e63      :param launc
-00001200: 6865 725f 7461 736b 5f69 6e66 6f3a 2064  her_task_info: d
-00001210: 6574 6169 6c73 2061 626f 7574 2028 616e  etails about (an
-00001220: 7929 206c 6175 6e63 6865 7220 5461 736b  y) launcher Task
-00001230: 0a20 2020 2020 2020 203a 7265 7475 726e  .        :return
-00001240: 3a20 5472 7565 2069 6620 7765 2061 7265  : True if we are
-00001250: 206c 6f6f 6b69 6e67 2066 6f72 2061 2073   looking for a s
-00001260: 696e 676c 6520 5072 6f6a 6563 7420 616e  ingle Project an
-00001270: 6420 7468 6973 2069 736e 2774 2069 742e  d this isn't it.
-00001280: 2020 4661 6c73 6520 6f74 6865 7277 6973    False otherwis
-00001290: 652e 0a20 2020 2072 1400 0000 da14 6469  e..    r......di
-000012a0: 7370 6c61 795f 6465 7461 696c 5f6c 6576  splay_detail_lev
-000012b0: 656c 7215 0000 0046 da13 7369 6e67 6c65  elr....F..single
-000012c0: 5f70 726f 6a65 6374 5f6e 616d 6554 da14  _project_nameT..
-000012d0: 7369 6e67 6c65 5f70 726f 6a65 6374 5f66  single_project_f
-000012e0: 6f75 6e64 e902 0000 007a 0950 726f 6a65  ound.....z.Proje
-000012f0: 6374 3a20 fa01 2029 0472 0600 0000 7207  ct: .. ).r....r.
-00001300: 0000 0072 0300 0000 7202 0000 0029 0a72  ...r....r....).r
-00001310: 0e00 0000 7211 0000 0072 1f00 0000 7228  ....r....r....r(
-00001320: 0000 0072 0f00 0000 7210 0000 0072 0b00  ...r....r....r..
-00001330: 0000 7225 0000 005a 0c6b 6964 5f61 7070  ..r%...Z.kid_app
-00001340: 5f69 6e66 6fda 0870 7269 6f72 6974 7972  _info..priorityr
-00001350: 1c00 0000 721c 0000 0072 1d00 0000 da1c  ....r....r......
-00001360: 6765 745f 6578 7472 615f 616e 645f 6f75  get_extra_and_ou
-00001370: 7470 7574 5f70 726f 6a65 6374 c100 0000  tput_project....
-00001380: 7328 0000 0008 170c 0108 010a 0108 030c  s(..............
-00001390: 0104 0108 0202 010e 0104 ff04 0b02 f902  ................
-000013a0: 0102 0102 0102 0116 0104 fb04 0772 3700  .............r7.
-000013b0: 0000 721b 0000 0063 0900 0000 0000 0000  ..r....c........
-000013c0: 0000 0000 0f00 0000 0c00 0000 4300 0000  ............C...
-000013d0: 736a 0100 0064 017c 0664 0219 0017 0064  sj...d.|.d.....d
-000013e0: 0317 007c 0764 0419 0017 007d 097c 0864  ...|.d.....}.|.d
-000013f0: 0519 0044 005d a27d 0a7c 0064 0619 0073  ...D.].}.|.d...s
-00001400: 1a7c 0064 0719 0072 1d01 0067 0053 007c  .|.d...r...g.S.|
-00001410: 0aa0 0064 08a1 016a 017d 0b74 027c 0a7c  ...d...j.}.t.|.|
-00001420: 067c 0983 037d 0c74 037c 077c 067c 0a7c  .|...}.t.|.|.|.|
-00001430: 0b7c 007c 027c 017c 0c83 0872 3571 107c  .|.|.|.|...r5q.|
-00001440: 0764 0919 0072 4074 047c 0a7c 067c 077c  .d...r@t.|.|.|.|
-00001450: 0183 0401 0074 0564 0a7c 077c 067c 017c  .....t.d.|.|.|.|
-00001460: 0a7c 0b7c 0383 077d 0d7c 0d64 0b6b 0372  .|.|...}.|.d.k.r
-00001470: 6474 067c 017c 0a7c 0b7c 0d7c 047c 077c  dt.|.|.|.|.|.|.|
-00001480: 027c 067c 087c 0083 0a7d 057c 0764 0c19  .|.|.|...}.|.d..
-00001490: 0072 647c 0064 0719 0073 6471 1074 077c  .rd|.d...sdq.t.|
-000014a0: 067c 077c 0164 0d64 0b83 0501 0074 0564  .|.|.d.d.....t.d
-000014b0: 0e69 0069 0067 007c 0a7c 0b67 0083 0704  .i.i.g.|.|.g....
-000014c0: 007d 0e72 8474 087c 0e7c 047c 017c 0b7c  .}.r.t.|.|.|.|.|
-000014d0: 067c 077c 027c 087c 0083 0901 007c 0764  .|.|.|.|.....|.d
-000014e0: 0f19 0073 9274 097c 0a7c 067c 077c 017c  ...s.t.|.|.|.|.|
-000014f0: 057c 047c 0883 0701 0074 077c 067c 077c  .|.|.....t.|.|.|
-00001500: 0164 0d64 0b83 0501 007c 0064 1019 0073  .d.d.....|.d...s
-00001510: a67c 0064 0719 0073 a67c 0064 0619 0072  .|.d...s.|.d...r
-00001520: b274 077c 067c 077c 0164 0d64 0b83 0501  .t.|.|.|.d.d....
-00001530: 007c 0402 0001 0053 0071 1067 0053 0029  .|.....S.q.g.S.)
-00001540: 1161 6002 0000 0a20 2020 2047 6f20 7468  .a`....    Go th
-00001550: 726f 7567 6820 616c 6c20 7468 6520 5072  rough all the Pr
-00001560: 6f6a 6563 7473 2c20 6765 7420 7468 6569  ojects, get thei
-00001570: 7220 6465 7461 696c 2061 6e64 206f 7574  r detail and out
-00001580: 7075 7420 6974 0a20 2020 2020 2020 203a  put it.        :
-00001590: 7061 7261 6d20 666f 756e 645f 6974 656d  param found_item
-000015a0: 733a 2061 6c6c 2069 7465 6d73 2066 6f75  s: all items fou
-000015b0: 6e64 2073 6f20 6661 720a 2020 2020 2020  nd so far.      
-000015c0: 2020 3a70 6172 616d 206f 7574 7075 745f    :param output_
-000015d0: 6c69 7374 3a20 6c69 7374 206f 6620 6f75  list: list of ou
-000015e0: 7470 7574 206c 696e 6573 2067 656e 6572  tput lines gener
-000015f0: 6174 6564 2073 6f20 6661 720a 2020 2020  ated so far.    
-00001600: 2020 2020 3a70 6172 616d 2068 6561 6469      :param headi
-00001610: 6e67 3a20 7468 6520 6f75 7470 7574 2068  ng: the output h
-00001620: 6561 6469 6e67 0a20 2020 2020 2020 203a  eading.        :
-00001630: 7061 7261 6d20 7072 6f6a 6563 7473 5f77  param projects_w
-00001640: 6974 686f 7574 5f70 726f 6669 6c65 733a  ithout_profiles:
-00001650: 206c 6973 7420 6f66 2050 726f 6a65 6374   list of Project
-00001660: 7320 7769 7468 206e 6f20 5072 6f66 696c  s with no Profil
-00001670: 6573 0a20 2020 2020 2020 203a 7061 7261  es.        :para
-00001680: 6d20 666f 756e 645f 7461 736b 733a 206c  m found_tasks: l
-00001690: 6973 7420 6f66 2054 6173 6b73 2066 6f75  ist of Tasks fou
-000016a0: 6e64 0a20 2020 2020 2020 203a 7061 7261  nd.        :para
-000016b0: 6d20 6f75 725f 7461 736b 5f65 6c65 6d65  m our_task_eleme
-000016c0: 6e74 3a20 786d 6c20 656c 656d 656e 7420  nt: xml element 
-000016d0: 6f66 206f 7572 2054 6173 6b0a 2020 2020  of our Task.    
-000016e0: 2020 2020 3a70 6172 616d 2063 6f6c 6f72      :param color
-000016f0: 6d61 703a 206f 7574 7075 7420 636f 6c6f  map: output colo
-00001700: 7273 2074 6f20 7573 650a 2020 2020 2020  rs to use.      
-00001710: 2020 3a70 6172 616d 2070 726f 6772 616d    :param program
-00001720: 5f61 7267 733a 2072 756e 7469 6d65 2061  _args: runtime a
-00001730: 7267 756d 656e 7473 0a20 2020 2020 2020  rguments.       
-00001740: 203a 7061 7261 6d20 616c 6c5f 7461 736b   :param all_task
-00001750: 6572 5f69 7465 6d73 3a20 616c 6c20 5072  er_items: all Pr
-00001760: 6f6a 6563 7473 2f50 726f 6669 6c65 732f  ojects/Profiles/
-00001770: 5461 736b 732f 5363 656e 6573 0a20 2020  Tasks/Scenes.   
-00001780: 2020 2020 203a 7265 7475 726e 3a20 6c69       :return: li
-00001790: 7374 206f 6620 666f 756e 6420 5461 736b  st of found Task
-000017a0: 730a 2020 2020 7a15 3c73 7061 6e20 7374  s.    z.<span st
-000017b0: 796c 6520 3d20 2263 6f6c 6f72 3ada 0d70  yle = "color:..p
-000017c0: 726f 6a65 6374 5f63 6f6c 6f72 7a08 223c  roject_colorz."<
-000017d0: 2f73 7061 6e3e da0b 666f 6e74 5f74 6f5f  /span>..font_to_
-000017e0: 7573 65da 0c61 6c6c 5f70 726f 6a65 6374  use..all_project
-000017f0: 7372 2a00 0000 7229 0000 00da 046e 616d  sr*...r).....nam
-00001800: 65da 1164 6973 706c 6179 5f74 6173 6b65  e..display_taske
-00001810: 726e 6574 5472 1400 0000 da13 7369 6e67  rnetTr......sing
-00001820: 6c65 5f70 726f 6669 6c65 5f6e 616d 6572  le_profile_namer
-00001830: 1500 0000 46da 1073 696e 676c 655f 7461  ....F..single_ta
-00001840: 736b 5f6e 616d 6572 3300 0000 290a 7223  sk_namer3...).r#
-00001850: 0000 0072 2400 0000 7226 0000 0072 3700  ...r$...r&...r7.
-00001860: 0000 7205 0000 0072 0800 0000 7204 0000  ..r....r....r...
-00001870: 0072 0200 0000 7230 0000 0072 0900 0000  .r....r0...r....
-00001880: 290f 720f 0000 0072 0b00 0000 7210 0000  ).r....r....r...
-00001890: 0072 0d00 0000 720c 0000 0072 1b00 0000  .r....r....r....
-000018a0: 7211 0000 0072 0e00 0000 7212 0000 0072  r....r....r....r
-000018b0: 2000 0000 721f 0000 0072 2800 0000 7225   ...r....r(...r%
-000018c0: 0000 005a 0b70 726f 6669 6c65 5f69 6473  ...Z.profile_ids
-000018d0: 7227 0000 0072 1c00 0000 721c 0000 0072  r'...r....r....r
-000018e0: 1d00 0000 7216 0000 00f4 0000 0073 b000  ....r........s..
-000018f0: 0000 021a 0601 02ff 0202 02fe 0603 02fd  ................
-00001900: 02ff 0c07 1002 0201 045f 0ca2 0c03 0203  ........._......
-00001910: 0201 0201 0201 0201 0201 0201 0201 0201  ................
-00001920: 04f8 020a 0803 0e01 0203 0201 0201 0201  ................
-00001930: 0201 0201 0201 0201 04f9 080a 0202 0201  ................
-00001940: 0201 0201 0201 0201 0201 0201 0201 0201  ................
-00001950: 0201 04f6 060f 02ff 0602 02fe 0204 1002  ................
-00001960: 1803 0202 0201 0201 0201 0201 0201 0201  ................
-00001970: 0201 0201 0201 04f7 080d 0201 0201 0201  ................
-00001980: 0201 0201 0201 0201 0201 04f9 100a 0602  ................
-00001990: 02ff 0602 02fe 0603 02fd 1005 0801 02fa  ................
-000019a0: 0409 7216 0000 0029 20da 1578 6d6c 2e65  ..r....) ..xml.e
-000019b0: 7472 6565 2e45 6c65 6d65 6e74 5472 6565  tree.ElementTree
-000019c0: da03 786d 6cda 156d 6170 7461 736b 6572  ..xml..maptasker
-000019d0: 2e73 7263 2e6f 7574 7075 746c 7202 0000  .src.outputlr...
-000019e0: 0072 0300 0000 5a16 6d61 7074 6173 6b65  .r....Z.maptaske
-000019f0: 722e 7372 632e 7072 6f66 696c 6573 7204  r.src.profilesr.
-00001a00: 0000 005a 136d 6170 7461 736b 6572 2e73  ...Z.maptasker.s
-00001a10: 7263 2e73 6861 7265 7205 0000 005a 146d  rc.sharer....Z.m
-00001a20: 6170 7461 736b 6572 2e73 7263 2e6b 6964  aptasker.src.kid
-00001a30: 6170 7072 0600 0000 5a16 6d61 7074 6173  appr....Z.maptas
-00001a40: 6b65 722e 7372 632e 7072 696f 7269 7479  ker.src.priority
-00001a50: 7207 0000 005a 146d 6170 7461 736b 6572  r....Z.maptasker
-00001a60: 2e73 7263 2e67 6574 6964 7372 0800 0000  .src.getidsr....
-00001a70: 5a14 6d61 7074 6173 6b65 722e 7372 632e  Z.maptasker.src.
-00001a80: 7363 656e 6573 7209 0000 005a 136d 6170  scenesr....Z.map
-00001a90: 7461 736b 6572 2e73 7263 2e74 6173 6b73  tasker.src.tasks
-00001aa0: da03 7372 6372 2e00 0000 da16 6d61 7074  ..srcr......mapt
-00001ab0: 6173 6b65 722e 7372 632e 7379 7363 6f6e  asker.src.syscon
-00001ac0: 7374 720a 0000 0072 1700 0000 7218 0000  str....r....r...
-00001ad0: 00da 0373 7472 721e 0000 00da 0565 7472  ...strr......etr
-00001ae0: 6565 7226 0000 0072 3000 0000 da04 626f  eer&...r0.....bo
-00001af0: 6f6c 7237 0000 0072 1600 0000 721c 0000  olr7...r....r...
-00001b00: 0072 1c00 0000 721c 0000 0072 1d00 0000  .r....r....r....
-00001b10: da08 3c6d 6f64 756c 653e 0100 0000 73c8  ..<module>....s.
-00001b20: 0000 0008 0e0c 020c 010c 010c 010c 010c  ................
-00001b30: 010c 010c 0112 010c 0102 0602 0102 ff02  ................
-00001b40: 0202 fe02 0302 fd02 0402 fc02 0502 fb02  ................
-00001b50: 0602 fa02 0702 f902 0802 f802 090a f702  ................
-00001b60: 2a04 0102 ff02 0102 ff02 0102 ff02 020a  *...............
-00001b70: fe02 1b02 0102 ff02 0202 fe02 0302 fd02  ................
-00001b80: 0402 fc02 0502 fb02 0602 fa02 0702 f902  ................
-00001b90: 0802 f802 0902 f702 0a0a f602 5c02 0102  ............\...
-00001ba0: ff02 0202 fe04 0302 fd02 0402 fc02 0502  ................
-00001bb0: fb02 0602 fa02 0702 f902 0802 f802 090a  ................
-00001bc0: f702 3302 0102 ff02 0202 fe02 0302 fd02  ..3.............
-00001bd0: 0402 fc02 0502 fb04 0602 fa02 0702 f902  ................
-00001be0: 0802 f802 0902 f702 0a0e f6              ...........
+000000b0: 5a15 0100 6400 640b 6c14 6d16 5a16 0100  Z...d.d.l.m.Z...
+000000c0: 640c 6517 640d 6517 640e 6517 640f 6518  d.e.d.e.d.e.d.e.
+000000d0: 6410 6518 6411 6519 6412 6518 6413 6518  d.e.d.e.d.e.d.e.
+000000e0: 6414 6517 6612 6415 6416 8404 5a1a 6417  d.e.f.d.d...Z.d.
+000000f0: 6501 6a1b 6412 6518 6418 6519 6414 6519  e.j.d.e.d.e.d.e.
+00000100: 6608 6419 641a 8404 5a1c 641b 6517 640d  f.d.d...Z.d.e.d.
+00000110: 6517 640c 6517 641c 6519 6412 6518 640f  e.d.e.d.e.d.e.d.
+00000120: 6518 6411 6519 6413 6518 6410 6518 6414  e.d.e.d.e.d.e.d.
+00000130: 6401 6614 641d 641e 8404 5a1d 640f 6518  d.f.d.d...Z.d.e.
+00000140: 6412 6518 6417 6501 6a1b 641c 6519 6410  d.e.d.e.j.d.e.d.
+00000150: 6518 6411 6519 640c 6517 641f 6519 6414  e.d.e.d.e.d.e.d.
+00000160: 651e 6612 6420 6421 8404 5a1f 6410 6518  e.f.d d!..Z.d.e.
+00000170: 640c 6517 6411 6519 640e 6517 640d 6517  d.e.d.e.d.e.d.e.
+00000180: 6422 6501 6a1b 6412 6518 640f 6518 6413  d"e.j.d.e.d.e.d.
+00000190: 6518 6414 6517 6614 6423 6424 8404 5a20  e.d.e.f.d#d$..Z 
+000001a0: 6401 5300 2925 e900 0000 004e 2901 da09  d.S.)%.....N)...
+000001b0: 6d79 5f6f 7574 7075 7429 01da 1272 6566  my_output)...ref
+000001c0: 7265 7368 5f6f 7572 5f6f 7574 7075 7429  resh_our_output)
+000001d0: 01da 1070 726f 6365 7373 5f70 726f 6669  ...process_profi
+000001e0: 6c65 7329 01da 0573 6861 7265 2901 da0b  les)...share)...
+000001f0: 6765 745f 6b69 645f 6170 7029 01da 0c67  get_kid_app)...g
+00000200: 6574 5f70 7269 6f72 6974 7929 01da 0767  et_priority)...g
+00000210: 6574 5f69 6473 2901 da16 7072 6f63 6573  et_ids)...proces
+00000220: 735f 7072 6f6a 6563 745f 7363 656e 6573  s_project_scenes
+00000230: 2901 da0a 4e4f 5f50 524f 4649 4c45 2901  )...NO_PROFILE).
+00000240: da0b 464f 4e54 5f54 4f5f 5553 45da 0b6f  ..FONT_TO_USE..o
+00000250: 7574 7075 745f 6c69 7374 da0b 666f 756e  utput_list..foun
+00000260: 645f 7461 736b 73da 1970 726f 6a65 6374  d_tasks..project
+00000270: 735f 7769 7468 6f75 745f 7072 6f66 696c  s_without_profil
+00000280: 6573 da0c 7072 6f67 7261 6d5f 6172 6773  es..program_args
+00000290: da0b 666f 756e 645f 6974 656d 73da 0768  ..found_items..h
+000002a0: 6561 6469 6e67 da08 636f 6c6f 726d 6170  eading..colormap
+000002b0: da10 616c 6c5f 7461 736b 6572 5f69 7465  ..all_tasker_ite
+000002c0: 6d73 da06 7265 7475 726e 6308 0000 0000  ms..returnc.....
+000002d0: 0000 0000 0000 0009 0000 000a 0000 0043  ...............C
+000002e0: 0000 0073 3e00 0000 6401 7d08 7400 7c04  ...s>...d.}.t.|.
+000002f0: 7c00 7c05 7c02 7c01 7c08 7c06 7c03 7c07  |.|.|.|.|.|.|.|.
+00000300: 8309 0100 7401 7c06 7c03 7c00 6402 6401  ....t.|.|.|.d.d.
+00000310: 8305 0100 7402 7403 a004 7c01 a101 a005  ....t.t...|.....
+00000320: a100 8301 5300 2903 61cc 0200 000a 2020  ....S.).a.....  
+00000330: 2020 476f 2074 6872 6f75 6768 2061 6c6c    Go through all
+00000340: 2050 726f 6a65 6374 732c 2070 726f 6365   Projects, proce
+00000350: 7373 2074 6865 6d20 616e 6420 7468 6569  ss them and thei
+00000360: 7220 5072 6f66 696c 6573 2061 6e64 2054  r Profiles and T
+00000370: 6173 6b73 2028 616e 6420 6164 6420 746f  asks (and add to
+00000380: 206f 7572 206f 7574 7075 7420 6c69 7374   our output list
+00000390: 290a 2020 2020 2020 2020 3a70 6172 616d  ).        :param
+000003a0: 206f 7574 7075 745f 6c69 7374 3a20 6c69   output_list: li
+000003b0: 7374 206f 6620 6f75 7470 7574 206c 696e  st of output lin
+000003c0: 6573 2067 656e 6572 6174 6564 2074 6875  es generated thu
+000003d0: 7320 6661 720a 2020 2020 2020 2020 3a70  s far.        :p
+000003e0: 6172 616d 2066 6f75 6e64 5f74 6173 6b73  aram found_tasks
+000003f0: 3a20 6c69 7374 206f 6620 5461 736b 7320  : list of Tasks 
+00000400: 666f 756e 6420 7468 7573 2066 6172 0a20  found thus far. 
+00000410: 2020 2020 2020 203a 7061 7261 6d20 7072         :param pr
+00000420: 6f6a 6563 7473 5f77 6974 686f 7574 5f70  ojects_without_p
+00000430: 726f 6669 6c65 733a 206c 6973 7420 6f66  rofiles: list of
+00000440: 2050 726f 6a65 6374 7320 7468 6174 2064   Projects that d
+00000450: 6f6e 2774 2068 6176 6520 616e 7920 5072  on't have any Pr
+00000460: 6f66 696c 6573 0a20 2020 2020 2020 203a  ofiles.        :
+00000470: 7061 7261 6d20 7072 6f67 7261 6d5f 6172  param program_ar
+00000480: 6773 3a20 7275 6e74 696d 6520 6172 6775  gs: runtime argu
+00000490: 6d65 6e74 730a 2020 2020 2020 2020 3a70  ments.        :p
+000004a0: 6172 616d 2066 6f75 6e64 5f69 7465 6d73  aram found_items
+000004b0: 3a20 6966 2073 6561 7263 6869 6e67 2066  : if searching f
+000004c0: 6f72 2061 2073 696e 676c 6520 5072 6f6a  or a single Proj
+000004d0: 6563 742f 5072 6f66 696c 652f 5461 736b  ect/Profile/Task
+000004e0: 2c20 6e61 6d65 206f 6620 7369 6e67 6c65  , name of single
+000004f0: 2069 7465 6d0a 2020 2020 2020 2020 3a70   item.        :p
+00000500: 6172 616d 2068 6561 6469 6e67 3a20 6865  aram heading: he
+00000510: 6164 696e 6720 7072 696e 7465 640a 2020  ading printed.  
+00000520: 2020 2020 2020 3a70 6172 616d 2063 6f6c        :param col
+00000530: 6f72 6d61 703a 2063 6f6c 6f72 7320 746f  ormap: colors to
+00000540: 2075 7365 2069 6e20 6f75 7470 7574 0a20   use in output. 
+00000550: 2020 2020 2020 203a 7061 7261 6d20 616c         :param al
+00000560: 6c5f 7461 736b 6572 5f69 7465 6d73 3a20  l_tasker_items: 
+00000570: 616c 6c20 5072 6f6a 6563 742f 5072 6f66  all Project/Prof
+00000580: 696c 652f 5461 736b 2f53 6365 6e65 2f50  ile/Task/Scene/P
+00000590: 7265 6665 7265 6e63 6520 5461 736b 6572  reference Tasker
+000005a0: 2078 6d6c 2065 6c65 6d65 6e74 730a 2020   xml elements.  
+000005b0: 2020 2020 2020 3a72 6574 7572 6e3a 206c        :return: l
+000005c0: 6973 7420 6f66 2054 6173 6b73 2066 6f75  ist of Tasks fou
+000005d0: 6e64 2074 6875 7320 6661 722c 2077 6974  nd thus far, wit
+000005e0: 6820 6475 706c 6963 6174 6573 2072 656d  h duplicates rem
+000005f0: 6f76 6564 0a20 2020 20da 00e9 0300 0000  oved.    .......
+00000600: 2906 da10 7072 6f63 6573 735f 7072 6f6a  )...process_proj
+00000610: 6563 7473 7202 0000 00da 046c 6973 74da  ectsr......list.
+00000620: 0464 6963 74da 0866 726f 6d6b 6579 73da  .dict..fromkeys.
+00000630: 046b 6579 7329 0972 0c00 0000 720d 0000  .keys).r....r...
+00000640: 0072 0e00 0000 720f 0000 0072 1000 0000  .r....r....r....
+00000650: 7211 0000 0072 1200 0000 7213 0000 00da  r....r....r.....
+00000660: 106f 7572 5f74 6173 6b5f 656c 656d 656e  .our_task_elemen
+00000670: 74a9 0072 1d00 0000 fa77 2f55 7365 7273  t..r.....w/Users
+00000680: 2f6d 696b 7275 6269 6e2f 4c69 6272 6172  /mikrubin/Librar
+00000690: 792f 436c 6f75 6453 746f 7261 6765 2f47  y/CloudStorage/G
+000006a0: 6f6f 676c 6544 7269 7665 2d6d 696b 7275  oogleDrive-mikru
+000006b0: 6269 6e40 676d 6169 6c2e 636f 6d2f 4d79  bin@gmail.com/My
+000006c0: 2044 7269 7665 2f50 7974 686f 6e2f 6d61   Drive/Python/ma
+000006d0: 7074 6173 6b65 722f 6d61 7074 6173 6b65  ptasker/maptaske
+000006e0: 722f 7372 632f 7072 6f6a 6563 7473 2e70  r/src/projects.p
+000006f0: 79da 2370 726f 6365 7373 5f70 726f 6a65  y.#process_proje
+00000700: 6374 735f 616e 645f 7468 6569 725f 7072  cts_and_their_pr
+00000710: 6f66 696c 6573 2100 0000 731c 0000 0004  ofiles!...s.....
+00000720: 1602 0202 0102 0102 0102 0102 0102 0102  ................
+00000730: 0102 0102 0104 f710 0b12 0472 1f00 0000  ...........r....
+00000740: da07 7072 6f6a 6563 74da 1270 726f 6a65  ..project..proje
+00000750: 6374 5f63 6f6c 6f72 5f68 746d 6c63 0300  ct_color_htmlc..
+00000760: 0000 0000 0000 0000 0000 0600 0000 0400  ................
+00000770: 0000 4300 0000 7358 0000 0064 017d 037c  ..C...sX...d.}.|
+00000780: 00a0 0064 02a1 017d 047c 0464 0375 0172  ...d...}.|.d.u.r
+00000790: 2a7c 04a0 0064 04a1 017d 057c 0564 0375  *|...d...}.|.d.u
+000007a0: 0172 2a7c 056a 0164 0375 0172 2a64 057c  .r*|.j.d.u.r*d.|
+000007b0: 0164 0619 0017 0074 0217 0064 077c 056a  .d.....t...d.|.j
+000007c0: 019b 0064 089d 0317 007c 0217 007d 037c  ...d.....|...}.|
+000007d0: 0353 0029 0961 1e01 0000 0a20 2020 2049  .S.).a.....    I
+000007e0: 6620 5072 6f6a 6563 7420 6861 7320 6120  f Project has a 
+000007f0: 6c61 756e 6368 6572 2054 6173 6b2c 2067  launcher Task, g
+00000800: 6574 2069 740a 2020 2020 2020 2020 3a70  et it.        :p
+00000810: 6172 616d 2070 726f 6a65 6374 3a20 786d  aram project: xm
+00000820: 6c20 656c 656d 656e 7420 6f66 2050 726f  l element of Pro
+00000830: 6a65 6374 2077 6520 6172 6520 7072 6f63  ject we are proc
+00000840: 6573 7369 6e67 0a20 2020 2020 2020 203a  essing.        :
+00000850: 7061 7261 6d20 636f 6c6f 726d 6170 3a20  param colormap: 
+00000860: 636f 6c6f 7273 2074 6f20 7573 6520 696e  colors to use in
+00000870: 206f 7574 7075 740a 2020 2020 2020 2020   output.        
+00000880: 3a70 6172 616d 2070 726f 6a65 6374 5f63  :param project_c
+00000890: 6f6c 6f72 5f68 746d 6c3a 2068 746d 6c20  olor_html: html 
+000008a0: 746f 2075 7365 2074 6861 7420 6465 6669  to use that defi
+000008b0: 6e65 7320 7468 6520 636f 6c6f 720a 2020  nes the color.  
+000008c0: 2020 2020 2020 3a72 6574 7572 6e3a 2069        :return: i
+000008d0: 6e66 6f72 6d61 7469 6f6e 2072 656c 6174  nformation relat
+000008e0: 6564 2074 6f20 6c61 756e 6368 6572 2054  ed to launcher T
+000008f0: 6173 6b0a 2020 2020 7215 0000 005a 0553  ask.    r....Z.S
+00000900: 6861 7265 4eda 0174 fa1a 3c2f 7370 616e  hareN..t..</span
+00000910: 3e3c 7370 616e 2073 7479 6c65 3d22 636f  ><span style="co
+00000920: 6c6f 723a da13 6c61 756e 6368 6572 5f74  lor:..launcher_t
+00000930: 6173 6b5f 636f 6c6f 727a 113e 5b4c 6175  ask_colorz.>[Lau
+00000940: 6e63 6865 7220 5461 736b 3a20 7a09 5d3c  ncher Task: z.]<
+00000950: 2f73 7061 6e3e 2029 03da 0466 696e 64da  /span> )...find.
+00000960: 0474 6578 7472 0b00 0000 2906 7220 0000  .textr....).r ..
+00000970: 0072 1200 0000 7221 0000 00da 126c 6175  .r....r!.....lau
+00000980: 6e63 6865 725f 7461 736b 5f69 6e66 6f5a  ncher_task_infoZ
+00000990: 0d73 6861 7265 5f65 6c65 6d65 6e74 5a15  .share_elementZ.
+000009a0: 6c61 756e 6368 6572 5f74 6173 6b5f 656c  launcher_task_el
+000009b0: 656d 656e 7472 1d00 0000 721d 0000 0072  ementr....r....r
+000009c0: 1e00 0000 da11 6765 745f 6c61 756e 6368  ......get_launch
+000009d0: 6572 5f74 6173 6b4b 0000 0073 2000 0000  er_taskK...s ...
+000009e0: 040a 0a01 0801 0a01 1201 0202 0601 02ff  ................
+000009f0: 0202 02fe 0c03 02fd 0204 02fc 02ff 0407  ................
+00000a00: 7228 0000 00da 0874 6173 6b5f 6964 73da  r(.....task_ids.
+00000a10: 0c70 726f 6a65 6374 5f6e 616d 6563 0900  .project_namec..
+00000a20: 0000 0000 0000 0000 0000 0f00 0000 1000  ................
+00000a30: 0000 4300 0000 73ea 0000 0064 017d 097c  ..C...s....d.}.|
+00000a40: 0044 005d 667d 0a7c 0a7c 0176 0172 6a7c  .D.]f}.|.|.v.rj|
+00000a50: 0864 0219 0073 6a7c 0864 0319 0073 6a74  .d...sj|.d...sjt
+00000a60: 00a0 017c 0a7c 0167 0064 047c 0764 0519  ...|.|.g.d.|.d..
+00000a70: 00a1 055c 027d 0b7d 0c7c 01a0 027c 0aa1  ...\.}.}.|...|..
+00000a80: 0101 007c 0972 507c 0072 507c 0864 0219  ...|.rP|.rP|.d..
+00000a90: 0073 507c 0864 0319 0073 5074 037c 047c  .sP|.d...sPt.|.|
+00000aa0: 057c 0264 0664 077c 0464 0819 009b 0064  .|.d.d.|.d.....d
+00000ab0: 097c 0564 0a19 009b 0064 0b7c 039b 0064  .|.d.....d.|...d
+00000ac0: 0c9d 0783 0501 0074 037c 047c 057c 0264  .......t.|.|.|.d
+00000ad0: 0d64 0483 0501 0064 0e7d 097c 0c9b 0064  .d.....d.}.|...d
+00000ae0: 0f7c 039b 0064 109d 0467 017d 0d74 00a0  .|...d...g.}.t..
+00000af0: 047c 027c 0c7c 0b7c 0d7c 0374 057c 017c  .|.|.|.|.|.t.|.|
+00000b00: 067c 047c 057c 077c 0864 01a1 0d7d 0e71  .|.|.|.|.d...}.q
+00000b10: 0474 037c 047c 057c 0264 0664 0483 0501  .t.|.|.|.d.d....
+00000b20: 0064 1153 0029 1261 6602 0000 0a20 2020  .d.S.).af....   
+00000b30: 2050 726f 6365 7373 2061 6c6c 2054 6173   Process all Tas
+00000b40: 6b73 2069 6e20 5072 6f6a 6563 7420 7468  ks in Project th
+00000b50: 6174 2061 7265 206e 6f74 2072 6566 6572  at are not refer
+00000b60: 656e 6365 6420 6279 2061 2050 726f 6669  enced by a Profi
+00000b70: 6c65 0a20 2020 2020 2020 203a 7061 7261  le.        :para
+00000b80: 6d20 7461 736b 5f69 6473 3a20 4c69 7374  m task_ids: List
+00000b90: 206f 6620 5461 736b 2049 4473 0a20 2020   of Task IDs.   
+00000ba0: 2020 2020 203a 7061 7261 6d20 666f 756e       :param foun
+00000bb0: 645f 7461 736b 733a 206c 6973 7420 6f66  d_tasks: list of
+00000bc0: 2054 6173 6b73 2066 6f75 6e64 2074 6875   Tasks found thu
+00000bd0: 7320 6661 720a 2020 2020 2020 2020 3a70  s far.        :p
+00000be0: 6172 616d 206f 7574 7075 745f 6c69 7374  aram output_list
+00000bf0: 3a20 6f75 7470 7574 206c 696e 6573 2067  : output lines g
+00000c00: 656e 6572 6174 6564 2074 6875 7320 6661  enerated thus fa
+00000c10: 7220 6f6e 746f 2077 6869 6368 2077 6520  r onto which we 
+00000c20: 7769 6c6c 2061 7070 656e 6420 6d6f 7265  will append more
+00000c30: 0a20 2020 2020 2020 203a 7061 7261 6d20  .        :param 
+00000c40: 7072 6f6a 6563 745f 6e61 6d65 3a20 6e61  project_name: na
+00000c50: 6d65 206f 6620 6375 7272 656e 7420 5072  me of current Pr
+00000c60: 6f6a 6563 740a 2020 2020 2020 2020 3a70  oject.        :p
+00000c70: 6172 616d 2063 6f6c 6f72 6d61 703a 2063  aram colormap: c
+00000c80: 6f6c 6f72 7320 746f 2075 7365 2069 6e20  olors to use in 
+00000c90: 6f75 7470 7574 0a20 2020 2020 2020 203a  output.        :
+00000ca0: 7061 7261 6d20 7072 6f67 7261 6d5f 6172  param program_ar
+00000cb0: 6773 3a20 7275 6e74 696d 6520 6172 6775  gs: runtime argu
+00000cc0: 6d65 6e74 730a 2020 2020 2020 2020 3a70  ments.        :p
+00000cd0: 6172 616d 2068 6561 6469 6e67 3a20 6375  aram heading: cu
+00000ce0: 7272 656e 7420 6865 6164 696e 670a 2020  rrent heading.  
+00000cf0: 2020 2020 2020 3a70 6172 616d 2061 6c6c        :param all
+00000d00: 5f74 6173 6b65 725f 6974 656d 733a 2061  _tasker_items: a
+00000d10: 6c6c 2050 726f 6a65 6374 732f 5072 6f66  ll Projects/Prof
+00000d20: 696c 6573 2f54 6173 6b73 2f53 6365 6e65  iles/Tasks/Scene
+00000d30: 730a 2020 2020 2020 2020 3a70 6172 616d  s.        :param
+00000d40: 2066 6f75 6e64 5f69 7465 6d73 3a20 7369   found_items: si
+00000d50: 6e67 6c65 2069 7465 6d20 6e61 6d65 2066  ngle item name f
+00000d60: 6f72 2050 726f 6a65 6374 2f50 726f 6669  or Project/Profi
+00000d70: 6c65 2f54 6173 6b0a 2020 2020 2020 2020  le/Task.        
+00000d80: 3a72 6574 7572 6e3a 206e 6f6e 650a 2020  :return: none.  
+00000d90: 2020 54da 1473 696e 676c 655f 7072 6f66    T..single_prof
+00000da0: 696c 655f 666f 756e 64da 1173 696e 676c  ile_found..singl
+00000db0: 655f 7461 736b 5f66 6f75 6e64 7215 0000  e_task_foundr...
+00000dc0: 00da 0961 6c6c 5f74 6173 6b73 e904 0000  ...all_tasks....
+00000dd0: 007a 173c 6272 3e3c 7370 616e 2073 7479  .z.<br><span sty
+00000de0: 6c65 3d22 636f 6c6f 723a da0a 7461 736b  le="color:..task
+00000df0: 5f63 6f6c 6f72 7a0d 3b66 6f6e 742d 6661  _colorz.;font-fa
+00000e00: 6d69 6c79 3ada 0b66 6f6e 745f 746f 5f75  mily:..font_to_u
+00000e10: 7365 7a32 3e26 6e62 7370 3b26 6e62 7370  sez2>&nbsp;&nbsp
+00000e20: 3b26 6e62 7370 3b54 6865 2066 6f6c 6c6f  ;&nbsp;The follo
+00000e30: 7769 6e67 2054 6173 6b73 2069 6e20 5072  wing Tasks in Pr
+00000e40: 6f6a 6563 7420 7a25 2061 7265 206e 6f74  oject z% are not
+00000e50: 2069 6e20 616e 7920 5072 6f66 696c 652e   in any Profile.
+00000e60: 2e2e 3c2f 7370 616e 3e3c 6272 3ee9 0100  ..</span><br>...
+00000e70: 0000 467a 2f20 3c65 6d3e 284e 6f74 2072  ..Fz/ <em>(Not r
+00000e80: 6566 6572 656e 6365 6420 6279 2061 6e79  eferenced by any
+00000e90: 2050 726f 6669 6c65 2069 6e20 5072 6f6a   Profile in Proj
+00000ea0: 6563 7420 7a06 293c 2f65 6d3e 4e29 06da  ect z.)</em>N)..
+00000eb0: 0574 6173 6b73 5a0d 6765 745f 7461 736b  .tasksZ.get_task
+00000ec0: 5f6e 616d 65da 0672 656d 6f76 6572 0200  _name..remover..
+00000ed0: 0000 5a0b 6f75 7470 7574 5f74 6173 6b72  ..Z.output_taskr
+00000ee0: 0a00 0000 290f 7229 0000 0072 0d00 0000  ....).r)...r....
+00000ef0: 720c 0000 0072 2a00 0000 7212 0000 0072  r....r*...r....r
+00000f00: 0f00 0000 7211 0000 0072 1300 0000 7210  ....r....r....r.
+00000f10: 0000 005a 126f 7574 7075 745f 7468 655f  ...Z.output_the_
+00000f20: 6865 6164 696e 675a 0674 6865 5f69 6472  headingZ.the_idr
+00000f30: 1c00 0000 5a0d 6f75 725f 7461 736b 5f6e  ....Z.our_task_n
+00000f40: 616d 655a 0974 6173 6b5f 6c69 7374 5a04  ameZ.task_listZ.
+00000f50: 6b61 6b61 721d 0000 0072 1d00 0000 721e  kakar....r....r.
+00000f60: 0000 00da 1574 6173 6b73 5f6e 6f74 5f69  .....tasks_not_i
+00000f70: 6e5f 7072 6f66 696c 6573 6700 0000 7372  n_profilesg...sr
+00000f80: 0000 0002 1a02 ff08 0508 0206 0202 fe06  ................
+00000f90: 0302 fd04 060e 0108 ff0a 0402 0402 ff02  ................
+00000fa0: 0202 fe06 0302 fd06 0402 fc02 0602 0102  ................
+00000fb0: 0102 0102 0102 0206 0104 ff06 0204 fe02  ................
+00000fc0: 0306 fd04 fa10 0d04 0106 0402 0106 ff04  ................
+00000fd0: ff04 0602 0102 0102 0102 0102 0102 0102  ................
+00000fe0: 0102 0102 0102 0102 0102 0102 0104 f302  ................
+00000ff0: 8010 1004 0172 3400 0000 7227 0000 0063  .....r4...r'...c
+00001000: 0800 0000 0000 0000 0000 0000 0a00 0000  ................
+00001010: 0b00 0000 4300 0000 7386 0000 0064 0104  ....C...s....d..
+00001020: 007d 087d 097c 0064 0219 0064 036b 0272  .}.}.|.d...d.k.r
+00001030: 1374 007c 0283 017d 0874 017c 0264 0483  .t.|...}.t.|.d..
+00001040: 027d 097c 0064 0519 0072 2f7c 037c 0064  .}.|.d...r/|.|.d
+00001050: 0519 006b 0372 1f64 0653 0064 067c 0464  ...k.r.d.S.d.|.d
+00001060: 073c 0074 0264 047c 067c 0364 017c 057c  .<.t.d.|.|.d.|.|
+00001070: 017c 0083 0701 0064 0453 0074 037c 017c  .|.....d.S.t.|.|
+00001080: 007c 0664 0864 097c 039b 0064 0a7c 079b  .|.d.d.|...d.|..
+00001090: 007c 099b 007c 089b 009d 0683 0501 0064  .|...|.........d
+000010a0: 0453 0029 0b61 6f02 0000 0a20 2020 2041  .S.).ao....    A
+000010b0: 6464 2065 7874 7261 2069 6e66 6f20 746f  dd extra info to
+000010c0: 2050 726f 6a65 6374 206f 7574 7075 7420   Project output 
+000010d0: 6c69 6e65 2061 7320 6170 7072 6f70 7269  line as appropri
+000010e0: 6174 6520 616e 6420 7468 656e 206f 7574  ate and then out
+000010f0: 7075 7420 6974 2e0a 2020 2020 2020 2020  put it..        
+00001100: 3a70 6172 616d 2070 726f 6772 616d 5f61  :param program_a
+00001110: 7267 733a 2072 756e 7469 6d65 2061 7267  rgs: runtime arg
+00001120: 756d 656e 7473 0a20 2020 2020 2020 203a  uments.        :
+00001130: 7061 7261 6d20 636f 6c6f 726d 6170 3a20  param colormap: 
+00001140: 636f 6c6f 7273 2074 6f20 7573 6520 696e  colors to use in
+00001150: 2070 7574 7075 740a 2020 2020 2020 2020   putput.        
+00001160: 3a70 6172 616d 2070 726f 6a65 6374 3a20  :param project: 
+00001170: 5072 6f6a 6563 7420 786d 6c20 656c 656d  Project xml elem
+00001180: 656e 740a 2020 2020 2020 2020 3a70 6172  ent.        :par
+00001190: 616d 2070 726f 6a65 6374 5f6e 616d 653a  am project_name:
+000011a0: 206e 616d 6520 6f66 2050 726f 6a65 6374   name of Project
+000011b0: 0a20 2020 2020 2020 203a 7061 7261 6d20  .        :param 
+000011c0: 666f 756e 645f 6974 656d 733a 2073 696e  found_items: sin
+000011d0: 676c 6520 6e61 6d65 2066 6f72 2050 726f  gle name for Pro
+000011e0: 6a65 6374 2f50 726f 6669 6c65 2f54 6173  ject/Profile/Tas
+000011f0: 6b20 6966 2070 726f 7669 6465 640a 2020  k if provided.  
+00001200: 2020 2020 2020 3a70 6172 616d 2068 6561        :param hea
+00001210: 6469 6e67 3a20 6c61 7374 206f 7574 7075  ding: last outpu
+00001220: 7420 6865 6164 696e 670a 2020 2020 2020  t heading.      
+00001230: 2020 3a70 6172 616d 206f 7574 7075 745f    :param output_
+00001240: 6c69 7374 3a20 6c69 7374 206f 6620 6f75  list: list of ou
+00001250: 7470 7574 206c 696e 6573 2067 656e 6572  tput lines gener
+00001260: 6174 6564 2074 6875 7320 6661 720a 2020  ated thus far.  
+00001270: 2020 2020 2020 3a70 6172 616d 206c 6175        :param lau
+00001280: 6e63 6865 725f 7461 736b 5f69 6e66 6f3a  ncher_task_info:
+00001290: 2064 6574 6169 6c73 2061 626f 7574 2028   details about (
+000012a0: 616e 7929 206c 6175 6e63 6865 7220 5461  any) launcher Ta
+000012b0: 736b 0a20 2020 2020 2020 203a 7265 7475  sk.        :retu
+000012c0: 726e 3a20 5472 7565 2069 6620 7765 2061  rn: True if we a
+000012d0: 7265 206c 6f6f 6b69 6e67 2066 6f72 2061  re looking for a
+000012e0: 2073 696e 676c 6520 5072 6f6a 6563 7420   single Project 
+000012f0: 616e 6420 7468 6973 2069 736e 2774 2069  and this isn't i
+00001300: 742e 2020 4661 6c73 6520 6f74 6865 7277  t.  False otherw
+00001310: 6973 652e 0a20 2020 2072 1500 0000 da14  ise..    r......
+00001320: 6469 7370 6c61 795f 6465 7461 696c 5f6c  display_detail_l
+00001330: 6576 656c 7216 0000 0046 da13 7369 6e67  evelr....F..sing
+00001340: 6c65 5f70 726f 6a65 6374 5f6e 616d 6554  le_project_nameT
+00001350: da14 7369 6e67 6c65 5f70 726f 6a65 6374  ..single_project
+00001360: 5f66 6f75 6e64 e902 0000 007a 0950 726f  _found.....z.Pro
+00001370: 6a65 6374 3a20 fa01 2029 0472 0600 0000  ject: .. ).r....
+00001380: 7207 0000 0072 0300 0000 7202 0000 0029  r....r....r....)
+00001390: 0a72 0f00 0000 7212 0000 0072 2000 0000  .r....r....r ...
+000013a0: 722a 0000 0072 1000 0000 7211 0000 0072  r*...r....r....r
+000013b0: 0c00 0000 7227 0000 005a 0c6b 6964 5f61  ....r'...Z.kid_a
+000013c0: 7070 5f69 6e66 6fda 0870 7269 6f72 6974  pp_info..priorit
+000013d0: 7972 1d00 0000 721d 0000 0072 1e00 0000  yr....r....r....
+000013e0: da1c 6765 745f 6578 7472 615f 616e 645f  ..get_extra_and_
+000013f0: 6f75 7470 7574 5f70 726f 6a65 6374 c800  output_project..
+00001400: 0000 7328 0000 0008 170c 0108 010a 0108  ..s(............
+00001410: 030c 0104 0108 0202 010e 0104 ff04 0b02  ................
+00001420: f902 0102 0102 0102 0116 0104 fb04 0772  ...............r
+00001430: 3b00 0000 721c 0000 0063 0900 0000 0000  ;...r....c......
+00001440: 0000 0000 0000 0f00 0000 0c00 0000 4300  ..............C.
+00001450: 0000 7388 0100 0064 017c 0664 0219 0017  ..s....d.|.d....
+00001460: 007c 0764 0319 0017 0064 0417 007d 097c  .|.d.....d...}.|
+00001470: 0864 0519 0044 005d b17d 0a7c 0064 0619  .d...D.].}.|.d..
+00001480: 0073 1a7c 0064 0719 0072 1d01 0067 0053  .s.|.d...r...g.S
+00001490: 007c 0aa0 0064 08a1 016a 017d 0b74 027c  .|...d...j.}.t.|
+000014a0: 0a7c 067c 0983 037d 0c74 037c 077c 067c  .|.|...}.t.|.|.|
+000014b0: 0a7c 0b7c 007c 027c 017c 0c83 0872 3571  .|.|.|.|.|...r5q
+000014c0: 107c 0764 0919 0072 4074 047c 0a7c 067c  .|.d...r@t.|.|.|
+000014d0: 077c 0183 0401 0074 0564 0a7c 077c 067c  .|.....t.d.|.|.|
+000014e0: 017c 0a7c 0b7c 0383 0704 007d 0d72 6374  .|.|.|.....}.rct
+000014f0: 067c 017c 0a7c 0b7c 0d7c 047c 077c 027c  .|.|.|.|.|.|.|.|
+00001500: 067c 087c 0083 0a7d 057c 0764 0b19 0072  .|.|...}.|.d...r
+00001510: 627c 0064 0719 0073 6271 106e 1074 077c  b|.d...sbq.n.t.|
+00001520: 067c 077c 0164 0c64 0d7c 0664 0e19 0017  .|.|.d.d.|.d....
+00001530: 0074 0817 0064 0f17 0083 0501 0074 077c  .t...d.......t.|
+00001540: 067c 077c 0164 1064 1183 0501 0074 0564  .|.|.d.d.....t.d
+00001550: 1269 0069 0067 007c 0a7c 0b67 0083 0704  .i.i.g.|.|.g....
+00001560: 007d 0e72 9374 097c 0e7c 047c 017c 0b7c  .}.r.t.|.|.|.|.|
+00001570: 067c 077c 027c 087c 0083 0901 007c 0764  .|.|.|.|.....|.d
+00001580: 1319 0073 a174 0a7c 0a7c 067c 077c 017c  ...s.t.|.|.|.|.|
+00001590: 057c 047c 0883 0701 0074 077c 067c 077c  .|.|.....t.|.|.|
+000015a0: 0164 1064 1183 0501 007c 0064 1419 0073  .d.d.....|.d...s
+000015b0: b57c 0064 0719 0073 b57c 0064 0619 0072  .|.d...s.|.d...r
+000015c0: c174 077c 067c 077c 0164 1064 1183 0501  .t.|.|.|.d.d....
+000015d0: 007c 0402 0001 0053 0071 1067 0053 0029  .|.....S.q.g.S.)
+000015e0: 1561 6002 0000 0a20 2020 2047 6f20 7468  .a`....    Go th
+000015f0: 726f 7567 6820 616c 6c20 7468 6520 5072  rough all the Pr
+00001600: 6f6a 6563 7473 2c20 6765 7420 7468 6569  ojects, get thei
+00001610: 7220 6465 7461 696c 2061 6e64 206f 7574  r detail and out
+00001620: 7075 7420 6974 0a20 2020 2020 2020 203a  put it.        :
+00001630: 7061 7261 6d20 666f 756e 645f 6974 656d  param found_item
+00001640: 733a 2061 6c6c 2069 7465 6d73 2066 6f75  s: all items fou
+00001650: 6e64 2073 6f20 6661 720a 2020 2020 2020  nd so far.      
+00001660: 2020 3a70 6172 616d 206f 7574 7075 745f    :param output_
+00001670: 6c69 7374 3a20 6c69 7374 206f 6620 6f75  list: list of ou
+00001680: 7470 7574 206c 696e 6573 2067 656e 6572  tput lines gener
+00001690: 6174 6564 2073 6f20 6661 720a 2020 2020  ated so far.    
+000016a0: 2020 2020 3a70 6172 616d 2068 6561 6469      :param headi
+000016b0: 6e67 3a20 7468 6520 6f75 7470 7574 2068  ng: the output h
+000016c0: 6561 6469 6e67 0a20 2020 2020 2020 203a  eading.        :
+000016d0: 7061 7261 6d20 7072 6f6a 6563 7473 5f77  param projects_w
+000016e0: 6974 686f 7574 5f70 726f 6669 6c65 733a  ithout_profiles:
+000016f0: 206c 6973 7420 6f66 2050 726f 6a65 6374   list of Project
+00001700: 7320 7769 7468 206e 6f20 5072 6f66 696c  s with no Profil
+00001710: 6573 0a20 2020 2020 2020 203a 7061 7261  es.        :para
+00001720: 6d20 666f 756e 645f 7461 736b 733a 206c  m found_tasks: l
+00001730: 6973 7420 6f66 2054 6173 6b73 2066 6f75  ist of Tasks fou
+00001740: 6e64 0a20 2020 2020 2020 203a 7061 7261  nd.        :para
+00001750: 6d20 6f75 725f 7461 736b 5f65 6c65 6d65  m our_task_eleme
+00001760: 6e74 3a20 786d 6c20 656c 656d 656e 7420  nt: xml element 
+00001770: 6f66 206f 7572 2054 6173 6b0a 2020 2020  of our Task.    
+00001780: 2020 2020 3a70 6172 616d 2063 6f6c 6f72      :param color
+00001790: 6d61 703a 206f 7574 7075 7420 636f 6c6f  map: output colo
+000017a0: 7273 2074 6f20 7573 650a 2020 2020 2020  rs to use.      
+000017b0: 2020 3a70 6172 616d 2070 726f 6772 616d    :param program
+000017c0: 5f61 7267 733a 2072 756e 7469 6d65 2061  _args: runtime a
+000017d0: 7267 756d 656e 7473 0a20 2020 2020 2020  rguments.       
+000017e0: 203a 7061 7261 6d20 616c 6c5f 7461 736b   :param all_task
+000017f0: 6572 5f69 7465 6d73 3a20 616c 6c20 5072  er_items: all Pr
+00001800: 6f6a 6563 7473 2f50 726f 6669 6c65 732f  ojects/Profiles/
+00001810: 5461 736b 732f 5363 656e 6573 0a20 2020  Tasks/Scenes.   
+00001820: 2020 2020 203a 7265 7475 726e 3a20 6c69       :return: li
+00001830: 7374 206f 6620 666f 756e 6420 5461 736b  st of found Task
+00001840: 730a 2020 2020 7a13 3c73 7061 6e20 7374  s.    z.<span st
+00001850: 796c 653d 2263 6f6c 6f72 3ada 0d70 726f  yle="color:..pro
+00001860: 6a65 6374 5f63 6f6c 6f72 7230 0000 00fa  ject_colorr0....
+00001870: 013e da0c 616c 6c5f 7072 6f6a 6563 7473  .>..all_projects
+00001880: 722c 0000 0072 2b00 0000 da04 6e61 6d65  r,...r+.....name
+00001890: da11 6469 7370 6c61 795f 7461 736b 6572  ..display_tasker
+000018a0: 6e65 7454 da13 7369 6e67 6c65 5f70 726f  netT..single_pro
+000018b0: 6669 6c65 5f6e 616d 6572 3800 0000 7223  file_namer8...r#
+000018c0: 0000 00da 0d70 726f 6669 6c65 5f63 6f6c  .....profile_col
+000018d0: 6f72 7a28 3e3c 656d 3e50 726f 6a65 6374  orz(><em>Project
+000018e0: 2068 6173 206e 6f20 5072 6f66 696c 6573   has no Profiles
+000018f0: 3c2f 656d 3e3c 2f73 7061 6e3e 7216 0000  </em></span>r...
+00001900: 0072 1500 0000 46da 1073 696e 676c 655f  .r....F..single_
+00001910: 7461 736b 5f6e 616d 6572 3700 0000 290b  task_namer7...).
+00001920: 7225 0000 0072 2600 0000 7228 0000 0072  r%...r&...r(...r
+00001930: 3b00 0000 7205 0000 0072 0800 0000 7204  ;...r....r....r.
+00001940: 0000 0072 0200 0000 720b 0000 0072 3400  ...r....r....r4.
+00001950: 0000 7209 0000 0029 0f72 1000 0000 720c  ..r....).r....r.
+00001960: 0000 0072 1100 0000 720e 0000 0072 0d00  ...r....r....r..
+00001970: 0000 721c 0000 0072 1200 0000 720f 0000  ..r....r....r...
+00001980: 0072 1300 0000 7221 0000 0072 2000 0000  .r....r!...r ...
+00001990: 722a 0000 0072 2700 0000 5a0b 7072 6f66  r*...r'...Z.prof
+000019a0: 696c 655f 6964 7372 2900 0000 721d 0000  ile_idsr)...r...
+000019b0: 0072 1d00 0000 721e 0000 0072 1700 0000  .r....r....r....
+000019c0: fb00 0000 73ca 0000 0002 1a06 0102 ff06  ....s...........
+000019d0: 0202 fe02 0302 fd02 ff0c 0710 0202 0104  ................
+000019e0: 670c 9a0c 0302 0302 0102 0102 0102 0102  g...............
+000019f0: 0102 0102 0102 0104 f802 0a08 030e 0102  ................
+00001a00: 0202 0102 0102 0102 0102 0102 0102 0108  ................
+00001a10: f902 0902 0102 0102 0102 0102 0102 0102  ................
+00001a20: 0102 0102 0102 0104 f606 0f02 ff06 0202  ................
+00001a30: fe02 0402 8002 0202 0102 0102 0102 0102  ................
+00001a40: 0206 0102 ff02 0202 fe02 0302 fd04 fa10  ................
+00001a50: 0c18 0302 0202 0102 0102 0102 0102 0102  ................
+00001a60: 0102 0102 0102 0104 f708 0d02 0102 0102  ................
+00001a70: 0102 0102 0102 0102 0102 0104 f910 0a06  ................
+00001a80: 0202 ff06 0202 fe06 0302 fd10 0508 0102  ................
+00001a90: fa04 0972 1700 0000 2921 da15 786d 6c2e  ...r....)!..xml.
+00001aa0: 6574 7265 652e 456c 656d 656e 7454 7265  etree.ElementTre
+00001ab0: 65da 0378 6d6c da15 6d61 7074 6173 6b65  e..xml..maptaske
+00001ac0: 722e 7372 632e 6f75 7470 7574 6c72 0200  r.src.outputlr..
+00001ad0: 0000 7203 0000 005a 166d 6170 7461 736b  ..r....Z.maptask
+00001ae0: 6572 2e73 7263 2e70 726f 6669 6c65 7372  er.src.profilesr
+00001af0: 0400 0000 5a13 6d61 7074 6173 6b65 722e  ....Z.maptasker.
+00001b00: 7372 632e 7368 6172 6572 0500 0000 5a14  src.sharer....Z.
+00001b10: 6d61 7074 6173 6b65 722e 7372 632e 6b69  maptasker.src.ki
+00001b20: 6461 7070 7206 0000 005a 166d 6170 7461  dappr....Z.mapta
+00001b30: 736b 6572 2e73 7263 2e70 7269 6f72 6974  sker.src.priorit
+00001b40: 7972 0700 0000 5a14 6d61 7074 6173 6b65  yr....Z.maptaske
+00001b50: 722e 7372 632e 6765 7469 6473 7208 0000  r.src.getidsr...
+00001b60: 005a 146d 6170 7461 736b 6572 2e73 7263  .Z.maptasker.src
+00001b70: 2e73 6365 6e65 7372 0900 0000 5a13 6d61  .scenesr....Z.ma
+00001b80: 7074 6173 6b65 722e 7372 632e 7461 736b  ptasker.src.task
+00001b90: 73da 0373 7263 7232 0000 00da 166d 6170  s..srcr2.....map
+00001ba0: 7461 736b 6572 2e73 7263 2e73 7973 636f  tasker.src.sysco
+00001bb0: 6e73 7472 0a00 0000 720b 0000 0072 1800  nstr....r....r..
+00001bc0: 0000 7219 0000 00da 0373 7472 721f 0000  ..r......strr...
+00001bd0: 00da 0565 7472 6565 7228 0000 0072 3400  ...etreer(...r4.
+00001be0: 0000 da04 626f 6f6c 723b 0000 0072 1700  ....boolr;...r..
+00001bf0: 0000 721d 0000 0072 1d00 0000 721d 0000  ..r....r....r...
+00001c00: 0072 1e00 0000 da08 3c6d 6f64 756c 653e  .r......<module>
+00001c10: 0100 0000 73ca 0000 0008 0e0c 020c 010c  ....s...........
+00001c20: 010c 010c 010c 010c 010c 0112 010c 010c  ................
+00001c30: 0102 0602 0102 ff02 0202 fe02 0302 fd02  ................
+00001c40: 0402 fc02 0502 fb02 0602 fa02 0702 f902  ................
+00001c50: 0802 f802 090a f702 2a04 0102 ff02 0102  ........*.......
+00001c60: ff02 0102 ff02 020a fe02 1c02 0102 ff02  ................
+00001c70: 0202 fe02 0302 fd02 0402 fc02 0502 fb02  ................
+00001c80: 0602 fa02 0702 f902 0802 f802 0902 f702  ................
+00001c90: 0a0a f602 6102 0102 ff02 0202 fe04 0302  ....a...........
+00001ca0: fd02 0402 fc02 0502 fb02 0602 fa02 0702  ................
+00001cb0: f902 0802 f802 090a f702 3302 0102 ff02  ..........3.....
+00001cc0: 0202 fe02 0302 fd02 0402 fc02 0502 fb04  ................
+00001cd0: 0602 fa02 0702 f902 0802 f802 0902 f702  ................
+00001ce0: 0a0e f6                                  ...
```

### Comparing `maptasker-1.3.1/maptasker/src/__pycache__/runcli.cpython-310.pyc` & `maptasker-1.3.2/maptasker/src/__pycache__/runcli.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Thu Mar 16 15:26:18 2023 UTC, .py size: 8999 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 5% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 1a35 1364 2723 0000  o........5.d'#..
+00000000: 6f0d 0d0a 0000 0000 918f 1c64 2723 0000  o..........d'#..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0008 0000 0040 0000 0073 d400 0000 6400  .....@...s....d.
 00000030: 6401 6c00 5a00 6400 6402 6c01 6d02 5a02  d.l.Z.d.d.l.m.Z.
 00000040: 0100 6400 6403 6c01 6d03 5a03 0100 6400  ..d.d.l.m.Z...d.
 00000050: 6404 6c04 6d05 5a05 0100 6400 6405 6c06  d.l.m.Z...d.d.l.
 00000060: 6d07 5a07 0100 6400 6406 6c08 6d09 5a09  m.Z...d.d.l.m.Z.
 00000070: 0100 6400 6407 6c0a 6d0b 5a0b 0100 6400  ..d.d.l.m.Z...d.
```

### Comparing `maptasker-1.3.1/maptasker/src/__pycache__/rungui.cpython-310.pyc` & `maptasker-1.3.2/maptasker/src/__pycache__/rungui.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Wed Mar 15 16:34:27 2023 UTC, .py size: 4154 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 93f3 1164 3a10 0000  o..........d:...
+00000000: 6f0d 0d0a 0000 0000 918f 1c64 3a10 0000  o..........d:...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0002 0000 0040 0000 0073 6000 0000 6400  .....@...s`...d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 0100 6400 6403 6c04 6d05 5a05  m.Z...d.d.l.m.Z.
 00000050: 0100 6400 6404 6c06 6d07 5a07 0100 6400  ..d.d.l.m.Z...d.
 00000060: 6405 6c06 6d08 5a08 0100 6501 7226 6400  d.l.m.Z...e.r&d.
 00000070: 6406 6c09 6d0a 610a 0100 6407 6408 8400  d.l.m.a...d.d...
@@ -85,15 +85,15 @@
 00000540: 0308 0108 0106 0302 0312 010e 0110 0108  ................
 00000550: 8002 ff0a 030a 010a 010a 010a 010a 010c  ................
 00000560: 0206 0212 010a 010a 030a 0302 0102 0102  ................
 00000570: 0302 0104 fe72 2300 0000 4e29 0dda 146d  .....r#...N)...m
 00000580: 6170 7461 736b 6572 2e73 7263 2e63 6f6e  aptasker.src.con
 00000590: 6669 6772 0200 0000 da16 6d61 7074 6173  figr......maptas
 000005a0: 6b65 722e 7372 632e 696e 6974 7061 7267  ker.src.initparg
-000005b0: 7203 0000 005a 166d 6170 7461 736b 6572  r....Z.maptasker
+000005b0: 7203 0000 00da 166d 6170 7461 736b 6572  r......maptasker
 000005c0: 2e73 7263 2e63 6f6c 726d 6f64 6572 0400  .src.colrmoder..
 000005d0: 0000 da16 6d61 7074 6173 6b65 722e 7372  ....maptasker.sr
 000005e0: 632e 7379 7363 6f6e 7374 7205 0000 0072  c.sysconstr....r
 000005f0: 0600 0000 7217 0000 0072 0800 0000 720d  ....r....r....r.
 00000600: 0000 0072 2300 0000 720b 0000 0072 0b00  ...r#...r....r..
 00000610: 0000 720b 0000 0072 0c00 0000 da08 3c6d  ..r....r......<m
 00000620: 6f64 756c 653e 0100 0000 7312 0000 000c  odule>....s.....
```

### Comparing `maptasker-1.3.1/maptasker/src/__pycache__/scenes.cpython-310.pyc` & `maptasker-1.3.2/maptasker/src/__pycache__/scenes.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 17 19:27:59 2023 UTC, .py size: 7556 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 6% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 3fbf 1464 841d 0000  o.......?..d....
+00000000: 6f0d 0d0a 0000 0000 d437 2c64 521e 0000  o........7,dR...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0010 0000 0040 0000 0073 f200 0000 6400  .....@...s....d.
 00000030: 6401 6c00 5a00 6400 6401 6c01 5a02 6400  d.l.Z.d.d.l.Z.d.
 00000040: 6401 6c03 6d04 0200 0100 6d05 5a05 0100  d.l.m.....m.Z...
 00000050: 6400 6402 6c06 6d07 5a07 0100 6400 6403  d.d.l.m.Z...d.d.
 00000060: 6c08 6d09 5a09 0100 6400 6404 6c0a 6d0b  l.m.Z...d.d.l.m.
 00000070: 5a0b 0100 6405 6406 6407 6408 6409 640a  Z...d.d.d.d.d.d.
@@ -47,215 +47,220 @@
 000002e0: 0a68 6569 6768 744c 616e 645a 0a68 6569  .heightLandZ.hei
 000002f0: 6768 7450 6f72 74da 036e 6d65 5a09 7769  ghtPort..nmeZ.wi
 00000300: 6474 684c 616e 645a 0977 6964 7468 506f  dthLandZ.widthPo
 00000310: 7274 da05 6368 696c 64da 0863 6f6c 6f72  rt..child..color
 00000320: 6d61 70da 0c70 726f 6772 616d 5f61 7267  map..program_arg
 00000330: 73da 0b6f 7574 7075 745f 6c69 7374 da06  s..output_list..
 00000340: 7265 7475 726e 6304 0000 0000 0000 0000  returnc.........
-00000350: 0000 0007 0000 000b 0000 0043 0000 0073  ...........C...s
-00000360: 4a00 0000 7c00 6a00 a001 6401 a101 7d04  J...|.j...d...}.
+00000350: 0000 0007 0000 000d 0000 0043 0000 0073  ...........C...s
+00000360: 5400 0000 7c00 6a00 a001 6401 a101 7d04  T...|.j...d...}.
 00000370: 7c00 a002 6402 a101 7d05 7c05 6a03 7d06  |...d...}.|.j.}.
 00000380: 7404 7c01 7c02 7c03 6403 6404 7c01 6405  t.|.|.|.d.d.|.d.
-00000390: 1900 9b00 6406 7c04 6407 1900 9b00 6408  ....d.|.d.....d.
-000003a0: 7c06 9b00 9d06 8305 0100 6409 5300 290a  |.........d.S.).
-000003b0: 6129 0100 000a 2020 2020 476f 2074 6872  a)....    Go thr
-000003c0: 6f75 6768 2053 6365 6e65 2773 203c 7878  ough Scene's <xx
-000003d0: 7845 6c65 6d65 6e74 3e20 7461 6773 2061  xElement> tags a
-000003e0: 6e64 206f 7574 7075 7420 7468 656d 0a20  nd output them. 
-000003f0: 2020 2020 2020 203a 7061 7261 6d20 6368         :param ch
-00000400: 696c 643a 2070 6f69 6e74 6572 2074 6f20  ild: pointer to 
-00000410: 273c 7878 7845 6c65 6d65 6e74 2720 5363  '<xxxElement' Sc
-00000420: 656e 6520 786d 6c20 7374 6174 656d 656e  ene xml statemen
-00000430: 740a 2020 2020 2020 2020 3a70 6172 616d  t.        :param
-00000440: 2063 6f6c 6f72 6d61 703a 2063 6f6c 6f72   colormap: color
-00000450: 7320 746f 2075 7365 0a20 2020 2020 2020  s to use.       
-00000460: 203a 7061 7261 6d20 7072 6f67 7261 6d5f   :param program_
-00000470: 6172 6773 3a20 7072 6f67 7261 6d20 7275  args: program ru
-00000480: 6e74 696d 6520 6172 6775 6d65 6e74 730a  ntime arguments.
-00000490: 2020 2020 2020 2020 3a70 6172 616d 206f          :param o
-000004a0: 7574 7075 745f 6c69 7374 3a20 6c69 7374  utput_list: list
-000004b0: 206f 6620 6f75 7470 7574 206c 696e 6573   of output lines
-000004c0: 0a20 2020 2020 2020 203a 7265 7475 726e  .        :return
-000004d0: 3a20 6e6f 7468 696e 670a 2020 2020 da07  : nothing.    ..
-000004e0: 456c 656d 656e 74da 0353 7472 e904 0000  Element..Str....
-000004f0: 007a 133c 7370 616e 2073 7479 6c65 3d22  .z.<span style="
-00000500: 636f 6c6f 723a da0b 7363 656e 655f 636f  color:..scene_co
-00000510: 6c6f 727a 1d22 3e26 6e62 7370 3b26 6e62  lorz.">&nbsp;&nb
-00000520: 7370 3b26 6e62 7370 3b45 6c65 6d65 6e74  sp;&nbsp;Element
-00000530: 3a20 7201 0000 007a 0720 6e61 6d65 6420  : r....z. named 
-00000540: 4e29 05da 0374 6167 da05 7370 6c69 74da  N)...tag..split.
-00000550: 0466 696e 64da 0474 6578 7472 0200 0000  .find..textr....
-00000560: 2907 721a 0000 0072 1b00 0000 721c 0000  ).r....r....r...
-00000570: 0072 1d00 0000 5a0c 656c 656d 656e 745f  .r....Z.element_
-00000580: 7479 7065 5a10 6e61 6d65 5f78 6d6c 5f65  typeZ.name_xml_e
-00000590: 6c65 6d65 6e74 5a0c 656c 656d 656e 745f  lementZ.element_
-000005a0: 6e61 6d65 a900 7227 0000 00fa 752f 5573  name..r'....u/Us
-000005b0: 6572 732f 6d69 6b72 7562 696e 2f4c 6962  ers/mikrubin/Lib
-000005c0: 7261 7279 2f43 6c6f 7564 5374 6f72 6167  rary/CloudStorag
-000005d0: 652f 476f 6f67 6c65 4472 6976 652d 6d69  e/GoogleDrive-mi
-000005e0: 6b72 7562 696e 4067 6d61 696c 2e63 6f6d  krubin@gmail.com
-000005f0: 2f4d 7920 4472 6976 652f 5079 7468 6f6e  /My Drive/Python
-00000600: 2f6d 6170 7461 736b 6572 2f6d 6170 7461  /maptasker/mapta
-00000610: 736b 6572 2f73 7263 2f73 6365 6e65 732e  sker/src/scenes.
-00000620: 7079 da12 6765 745f 7363 656e 655f 656c  py..get_scene_el
-00000630: 656d 656e 7473 3100 0000 731e 0000 000c  ements1...s.....
-00000640: 0b0a 0106 0102 0102 0102 0102 0102 010c  ................
-00000650: 0206 0104 ff02 0104 ff04 fa04 0b72 2900  .............r).
-00000660: 0000 da08 6d79 5f73 6365 6e65 da0b 7461  ....my_scene..ta
-00000670: 736b 735f 666f 756e 64da 1061 6c6c 5f74  sks_found..all_t
-00000680: 6173 6b65 725f 6974 656d 7363 0600 0000  asker_itemsc....
-00000690: 0000 0000 0000 0000 0e00 0000 0b00 0000  ................
-000006a0: 4300 0000 7314 0100 0064 0164 026c 006d  C...s....d.d.l.m
-000006b0: 017d 0601 007c 0564 0319 007c 0019 0044  .}...|.d...|...D
-000006c0: 005d 7b7d 077c 076a 0274 0376 0072 1471  .]{}.|.j.t.v.r.q
-000006d0: 0c7c 076a 0264 046b 0272 1c01 0064 0553  .|.j.d.k.r...d.S
-000006e0: 0074 047c 076a 0264 0683 0272 877c 0364  .t.|.j.d...r.|.d
-000006f0: 0719 0064 086b 0272 2f74 057c 077c 047c  ...d.k.r/t.|.|.|
-00000700: 037c 0183 0401 007c 0744 005d 557d 0874  .|.....|.D.]U}.t
-00000710: 047c 086a 0264 0983 0272 7f7c 086a 0667  .|.j.d...r.|.j.g
-00000720: 017d 0964 0a7c 0964 0119 0076 0172 7d74  .}.d.|.d...v.r}t
-00000730: 077c 047c 037c 0164 0b64 0c83 0501 0074  .|.|.|.d.d.....t
-00000740: 08a0 097c 086a 067c 027c 0964 0c7c 0564  ...|.j.|.|.d.|.d
-00000750: 0d19 00a1 055c 027d 0a7d 0b7c 086a 0667  .....\.}.}.|.j.g
-00000760: 017d 0964 0e7d 0c64 0f74 0a7c 086a 0219  .}.d.}.d.t.|.j..
-00000770: 009b 007c 0c9b 009d 037d 0d7c 067c 0d7c  ...|.....}.|.|.|
-00000780: 017c 097c 0a7c 027c 037c 047c 0583 0801  .|.|.|.|.|.|....
-00000790: 0074 077c 047c 037c 0164 0864 0c83 0501  .t.|.|.|.d.d....
-000007a0: 0071 3101 006e 087c 086a 0264 106b 0272  .q1..n.|.j.d.k.r
-000007b0: 8601 006e 0171 3171 0c64 0553 0029 1161  ...n.q1q.d.S.).a
-000007c0: 5c01 0000 0a0a 2020 2020 3a70 6172 616d  \.....    :param
-000007d0: 206d 795f 7363 656e 653a 206e 616d 6520   my_scene: name 
-000007e0: 6f66 2053 6365 6e65 2074 6f20 7072 6f63  of Scene to proc
-000007f0: 6573 730a 2020 2020 3a70 6172 616d 206f  ess.    :param o
-00000800: 7574 7075 745f 6c69 7374 3a20 6c69 7374  utput_list: list
-00000810: 206f 6620 6f75 7470 7574 206c 696e 6573   of output lines
-00000820: 0a20 2020 203a 7061 7261 6d20 7461 736b  .    :param task
-00000830: 735f 666f 756e 643a 206c 6973 7420 6f66  s_found: list of
-00000840: 2054 6173 6b73 2066 6f75 6e64 2073 6f20   Tasks found so 
-00000850: 6661 720a 2020 2020 3a70 6172 616d 2070  far.    :param p
-00000860: 726f 6772 616d 5f61 7267 733a 2064 6963  rogram_args: dic
-00000870: 7469 6f6e 6172 7920 6f66 2072 756e 7469  tionary of runti
-00000880: 6d65 2061 7267 756d 656e 7473 0a20 2020  me arguments.   
-00000890: 203a 7061 7261 6d20 636f 6c6f 726d 6170   :param colormap
-000008a0: 3a20 6469 6374 696f 6e61 7279 206f 6620  : dictionary of 
-000008b0: 636f 6c6f 7273 2074 6f20 7573 650a 2020  colors to use.  
-000008c0: 2020 3a70 6172 616d 2061 6c6c 5f74 6173    :param all_tas
-000008d0: 6b65 725f 6974 656d 733a 2064 6963 7469  ker_items: dicti
-000008e0: 6f6e 6172 7920 6f66 2054 6173 6b65 7220  onary of Tasker 
-000008f0: 5072 6f6a 6563 7473 2f50 726f 6669 6c65  Projects/Profile
-00000900: 732f 5461 736b 732f 5363 656e 6573 0a20  s/Tasks/Scenes. 
-00000910: 2020 203a 7265 7475 726e 3a0a 2020 2020     :return:.    
-00000920: 7201 0000 0072 0400 0000 da0a 616c 6c5f  r....r......all_
-00000930: 7363 656e 6573 5a11 5072 6f70 6572 7469  scenesZ.Properti
-00000940: 6573 456c 656d 656e 744e 54da 1464 6973  esElementNT..dis
-00000950: 706c 6179 5f64 6574 6169 6c5f 6c65 7665  play_detail_leve
-00000960: 6ce9 0300 0000 46fa 012d e901 0000 00da  l.....F..-......
-00000970: 00da 0961 6c6c 5f74 6173 6b73 7a0f 266e  ...all_tasksz.&n
-00000980: 6273 703b 266e 6273 703b 4944 3a75 0900  bsp;&nbsp;ID:u..
-00000990: 0000 e28e af54 6173 6b3a 2072 2000 0000  .....Task: r ...
-000009a0: 290b da16 6d61 7074 6173 6b65 722e 7372  )...maptasker.sr
-000009b0: 632e 7072 6f63 6c69 7374 7205 0000 0072  c.proclistr....r
-000009c0: 2300 0000 da14 5343 454e 455f 5441 4753  #.....SCENE_TAGS
-000009d0: 5f54 4f5f 4947 4e4f 5245 7203 0000 0072  _TO_IGNOREr....r
-000009e0: 2900 0000 7226 0000 0072 0200 0000 da05  )...r&...r......
-000009f0: 7461 736b 73da 0d67 6574 5f74 6173 6b5f  tasks..get_task_
-00000a00: 6e61 6d65 da10 5343 454e 455f 5441 534b  name..SCENE_TASK
-00000a10: 5f54 5950 4553 290e 722a 0000 0072 1d00  _TYPES).r*...r..
-00000a20: 0000 722b 0000 0072 1c00 0000 721b 0000  ..r+...r....r...
-00000a30: 0072 2c00 0000 7205 0000 0072 1a00 0000  .r,...r....r....
-00000a40: 5a09 7375 625f 6368 696c 645a 0e74 656d  Z.sub_childZ.tem
-00000a50: 705f 7461 736b 5f6c 6973 745a 0c74 6173  p_task_listZ.tas
-00000a60: 6b5f 656c 656d 656e 745a 0c6e 616d 655f  k_elementZ.name_
-00000a70: 6f66 5f74 6173 6bda 0565 7874 7261 da09  of_task..extra..
-00000a80: 7461 736b 5f74 7970 6572 2700 0000 7227  task_typer'...r'
-00000a90: 0000 0072 2800 0000 da0d 7072 6f63 6573  ...r(.....proces
-00000aa0: 735f 7363 656e 654d 0000 0073 5600 0000  s_sceneM...sV...
-00000ab0: 0c13 1003 0a01 0201 0a01 0601 0c01 0c02  ................
-00000ac0: 0e01 0801 0c02 0802 0c02 1001 0401 0401  ................
-00000ad0: 0201 0201 0201 0601 08fb 0808 0401 1401  ................
-00000ae0: 0201 0201 0201 0201 0201 0201 0201 0201  ................
-00000af0: 0201 04f8 020a 0a01 06ff 0404 0a01 0401  ................
-00000b00: 02ff 0280 0402 723b 0000 00da 0770 726f  ......r;.....pro
-00000b10: 6a65 6374 da10 6f75 725f 7461 736b 5f65  ject..our_task_e
-00000b20: 6c65 6d65 6e74 da0b 666f 756e 645f 7461  lement..found_ta
-00000b30: 736b 7363 0700 0000 0000 0000 0000 0000  sksc............
-00000b40: 0900 0000 0900 0000 4300 0000 738a 0000  ........C...s...
-00000b50: 0064 017d 0774 00a0 0174 02a1 018f 0e01  .d.}.t...t......
-00000b60: 007c 00a0 0364 02a1 016a 047d 0757 0064  .|...d...j.}.W.d
-00000b70: 0104 0004 0083 0301 006e 0831 0073 1877  .........n.1.s.w
-00000b80: 0101 0001 0001 0059 0001 007c 0764 0175  .......Y...|.d.u
-00000b90: 0172 437c 07a0 0564 03a1 017d 087c 0364  .rC|...d...}.|.d
-00000ba0: 0419 0064 056b 0272 3474 067c 017c 027c  ...d.k.r4t.|.|.|
-00000bb0: 0364 0664 0783 0501 007c 0864 0819 0072  .d.d.....|.d...r
-00000bc0: 4374 0764 097c 037c 087c 047c 057c 027c  Ct.d.|.|.|.|.|.|
-00000bd0: 017c 0683 0801 0064 0153 0029 0a61 0102  .|.....d.S.).a..
-00000be0: 0000 0a20 2020 2047 6f20 7468 726f 7567  ...    Go throug
-00000bf0: 6820 616c 6c20 5363 656e 6573 2066 6f72  h all Scenes for
-00000c00: 2050 726f 6a65 6374 2c20 6765 7420 7468   Project, get th
-00000c10: 6569 7220 6465 7461 696c 2061 6e64 206f  eir detail and o
-00000c20: 7574 7075 7420 6974 0a20 2020 2020 2020  utput it.       
-00000c30: 203a 7061 7261 6d20 7072 6f6a 6563 743a   :param project:
-00000c40: 2078 6d6c 2065 6c65 6d65 6e74 206f 6620   xml element of 
-00000c50: 5072 6f6a 6563 7420 7765 2061 7265 2070  Project we are p
-00000c60: 726f 6365 7373 696e 670a 2020 2020 2020  rocessing.      
-00000c70: 2020 3a70 6172 616d 2063 6f6c 6f72 6d61    :param colorma
-00000c80: 703a 2063 6f6c 6f72 7320 746f 2075 7365  p: colors to use
-00000c90: 2069 6e20 6f75 7470 7574 0a20 2020 2020   in output.     
-00000ca0: 2020 203a 7061 7261 6d20 7072 6f67 7261     :param progra
-00000cb0: 6d5f 6172 6773 3a20 7275 6e74 696d 6520  m_args: runtime 
-00000cc0: 6172 6775 6d65 6e74 730a 2020 2020 2020  arguments.      
-00000cd0: 2020 3a70 6172 616d 206f 7574 7075 745f    :param output_
-00000ce0: 6c69 7374 3a20 6c69 7374 206f 6620 6f75  list: list of ou
-00000cf0: 7470 7574 206c 696e 6573 2063 7265 6174  tput lines creat
-00000d00: 6564 2074 6875 7320 6661 720a 2020 2020  ed thus far.    
-00000d10: 2020 2020 3a70 6172 616d 206f 7572 5f74      :param our_t
-00000d20: 6173 6b5f 656c 656d 656e 743a 2078 6d6c  ask_element: xml
-00000d30: 2065 6c65 6d65 6e74 2070 6f69 6e74 696e   element pointin
-00000d40: 6720 746f 206f 7572 2054 6173 6b0a 2020  g to our Task.  
-00000d50: 2020 2020 2020 3a70 6172 616d 2066 6f75        :param fou
-00000d60: 6e64 5f74 6173 6b73 3a20 6c69 7374 206f  nd_tasks: list o
-00000d70: 6620 5461 736b 7320 666f 756e 6420 736f  f Tasks found so
-00000d80: 2066 6172 0a20 2020 2020 2020 203a 7061   far.        :pa
-00000d90: 7261 6d20 616c 6c5f 7461 736b 6572 5f69  ram all_tasker_i
-00000da0: 7465 6d73 3a20 616c 6c20 5072 6f6a 6563  tems: all Projec
-00000db0: 7473 2f50 726f 6669 6c65 732f 5461 736b  ts/Profiles/Task
-00000dc0: 732f 5363 656e 6573 0a20 2020 2020 2020  s/Scenes.       
-00000dd0: 203a 7265 7475 726e 3a20 6e61 6461 0a20   :return: nada. 
-00000de0: 2020 204e 5a06 7363 656e 6573 fa01 2ce9     NZ.scenes..,.
-00000df0: ffff ffff 7a05 3c2f 756c 3e72 3100 0000  ....z.</ul>r1...
-00000e00: 7232 0000 0072 0100 0000 7a06 5363 656e  r2...r....z.Scen
-00000e10: 653a 2908 da0a 636f 6e74 6578 746c 6962  e:)...contextlib
-00000e20: da08 7375 7070 7265 7373 da09 4578 6365  ..suppress..Exce
-00000e30: 7074 696f 6e72 2500 0000 7226 0000 0072  ptionr%...r&...r
-00000e40: 2400 0000 7202 0000 0072 0500 0000 2909  $...r....r....).
-00000e50: 723c 0000 0072 1b00 0000 721c 0000 0072  r<...r....r....r
-00000e60: 1d00 0000 723d 0000 0072 3e00 0000 722c  ....r=...r>...r,
-00000e70: 0000 005a 0b73 6365 6e65 5f6e 616d 6573  ...Z.scene_names
-00000e80: 5a0a 7363 656e 655f 6c69 7374 7227 0000  Z.scene_listr'..
-00000e90: 0072 2700 0000 7228 0000 00da 1670 726f  .r'...r(.....pro
-00000ea0: 6365 7373 5f70 726f 6a65 6374 5f73 6365  cess_project_sce
-00000eb0: 6e65 7396 0000 0073 2800 0000 0414 0c01  nes....s(.......
-00000ec0: 0e01 1cff 0802 0a01 0c05 1001 0802 0201  ................
-00000ed0: 0201 0201 0201 0201 0201 0201 0201 0201  ................
-00000ee0: 04f8 040a 7244 0000 0029 1572 4100 0000  ....rD...).rA...
-00000ef0: da15 786d 6c2e 6574 7265 652e 456c 656d  ..xml.etree.Elem
-00000f00: 656e 7454 7265 65da 0378 6d6c da13 6d61  entTree..xml..ma
-00000f10: 7074 6173 6b65 722e 7372 632e 7461 736b  ptasker.src.task
-00000f20: 73da 0373 7263 7236 0000 00da 156d 6170  s..srcr6.....map
-00000f30: 7461 736b 6572 2e73 7263 2e6f 7574 7075  tasker.src.outpu
-00000f40: 746c 7202 0000 00da 156d 6170 7461 736b  tlr......maptask
-00000f50: 6572 2e73 7263 2e78 6d6c 6461 7461 7203  er.src.xmldatar.
-00000f60: 0000 0072 3400 0000 7205 0000 0072 3800  ...r4...r....r8.
-00000f70: 0000 7235 0000 00da 0565 7472 6565 da04  ..r5.....etree..
-00000f80: 6469 6374 da04 6c69 7374 7229 0000 00da  dict..listr)....
-00000f90: 0373 7472 723b 0000 0072 4400 0000 7227  .strr;...rD...r'
-00000fa0: 0000 0072 2700 0000 7227 0000 0072 2800  ...r'...r'...r(.
-00000fb0: 0000 da08 3c6d 6f64 756c 653e 0100 0000  ....<module>....
-00000fc0: 7384 0000 0008 0c08 0212 010c 010c 010c  s...............
-00000fd0: 0102 0302 0102 0102 0102 0102 0102 0102  ................
-00000fe0: 0102 0102 0102 0102 0102 0102 0102 0106  ................
-00000ff0: f108 1102 0b04 0102 ff02 0102 ff02 0102  ................
-00001000: ff02 0102 ff02 020a fe02 1c02 0102 ff06  ................
-00001010: 0202 fe06 0302 fd02 0402 fc02 0502 fb02  ................
-00001020: 0602 fa02 070a f902 4904 0102 ff02 0202  ........I.......
-00001030: fe02 0302 fd02 0402 fc04 0502 fb02 0602  ................
-00001040: fa02 0702 f902 080e f8                   .........
+00000390: 1900 9b00 7c02 6406 1900 9b00 6407 7c04  ....|.d.....d.|.
+000003a0: 6408 1900 9b00 6409 7c06 9b00 640a 9d08  d.....d.|...d...
+000003b0: 8305 0100 640b 5300 290c 6129 0100 000a  ....d.S.).a)....
+000003c0: 2020 2020 476f 2074 6872 6f75 6768 2053      Go through S
+000003d0: 6365 6e65 2773 203c 7878 7845 6c65 6d65  cene's <xxxEleme
+000003e0: 6e74 3e20 7461 6773 2061 6e64 206f 7574  nt> tags and out
+000003f0: 7075 7420 7468 656d 0a20 2020 2020 2020  put them.       
+00000400: 203a 7061 7261 6d20 6368 696c 643a 2070   :param child: p
+00000410: 6f69 6e74 6572 2074 6f20 273c 7878 7845  ointer to '<xxxE
+00000420: 6c65 6d65 6e74 2720 5363 656e 6520 786d  lement' Scene xm
+00000430: 6c20 7374 6174 656d 656e 740a 2020 2020  l statement.    
+00000440: 2020 2020 3a70 6172 616d 2063 6f6c 6f72      :param color
+00000450: 6d61 703a 2063 6f6c 6f72 7320 746f 2075  map: colors to u
+00000460: 7365 0a20 2020 2020 2020 203a 7061 7261  se.        :para
+00000470: 6d20 7072 6f67 7261 6d5f 6172 6773 3a20  m program_args: 
+00000480: 7072 6f67 7261 6d20 7275 6e74 696d 6520  program runtime 
+00000490: 6172 6775 6d65 6e74 730a 2020 2020 2020  arguments.      
+000004a0: 2020 3a70 6172 616d 206f 7574 7075 745f    :param output_
+000004b0: 6c69 7374 3a20 6c69 7374 206f 6620 6f75  list: list of ou
+000004c0: 7470 7574 206c 696e 6573 0a20 2020 2020  tput lines.     
+000004d0: 2020 203a 7265 7475 726e 3a20 6e6f 7468     :return: noth
+000004e0: 696e 670a 2020 2020 da07 456c 656d 656e  ing.    ..Elemen
+000004f0: 74da 0353 7472 e904 0000 007a 133c 7370  t..Str.....z.<sp
+00000500: 616e 2073 7479 6c65 3d22 636f 6c6f 723a  an style="color:
+00000510: da0b 7363 656e 655f 636f 6c6f 72da 0b66  ..scene_color..f
+00000520: 6f6e 745f 746f 5f75 7365 7a1c 3e26 6e62  ont_to_usez.>&nb
+00000530: 7370 3b26 6e62 7370 3b26 6e62 7370 3b45  sp;&nbsp;&nbsp;E
+00000540: 6c65 6d65 6e74 3a20 7201 0000 007a 0720  lement: r....z. 
+00000550: 6e61 6d65 6420 7a07 3c2f 7370 616e 3e4e  named z.</span>N
+00000560: 2905 da03 7461 67da 0573 706c 6974 da04  )...tag..split..
+00000570: 6669 6e64 da04 7465 7874 7202 0000 0029  find..textr....)
+00000580: 0772 1a00 0000 721b 0000 0072 1c00 0000  .r....r....r....
+00000590: 721d 0000 005a 0c65 6c65 6d65 6e74 5f74  r....Z.element_t
+000005a0: 7970 655a 106e 616d 655f 786d 6c5f 656c  ypeZ.name_xml_el
+000005b0: 656d 656e 745a 0c65 6c65 6d65 6e74 5f6e  ementZ.element_n
+000005c0: 616d 65a9 0072 2800 0000 fa75 2f55 7365  ame..r(....u/Use
+000005d0: 7273 2f6d 696b 7275 6269 6e2f 4c69 6272  rs/mikrubin/Libr
+000005e0: 6172 792f 436c 6f75 6453 746f 7261 6765  ary/CloudStorage
+000005f0: 2f47 6f6f 676c 6544 7269 7665 2d6d 696b  /GoogleDrive-mik
+00000600: 7275 6269 6e40 676d 6169 6c2e 636f 6d2f  rubin@gmail.com/
+00000610: 4d79 2044 7269 7665 2f50 7974 686f 6e2f  My Drive/Python/
+00000620: 6d61 7074 6173 6b65 722f 6d61 7074 6173  maptasker/maptas
+00000630: 6b65 722f 7372 632f 7363 656e 6573 2e70  ker/src/scenes.p
+00000640: 79da 1267 6574 5f73 6365 6e65 5f65 6c65  y..get_scene_ele
+00000650: 6d65 6e74 7331 0000 0073 2600 0000 0c0b  ments1...s&.....
+00000660: 0a01 0601 0201 0201 0201 0201 0201 0202  ................
+00000670: 0601 02ff 0601 04ff 0602 04fe 0202 06fe  ................
+00000680: 04fa 040c 722a 0000 00da 086d 795f 7363  ....r*.....my_sc
+00000690: 656e 65da 0b74 6173 6b73 5f66 6f75 6e64  ene..tasks_found
+000006a0: da10 616c 6c5f 7461 736b 6572 5f69 7465  ..all_tasker_ite
+000006b0: 6d73 6306 0000 0000 0000 0000 0000 000e  msc.............
+000006c0: 0000 000b 0000 0043 0000 0073 1401 0000  .......C...s....
+000006d0: 6401 6402 6c00 6d01 7d06 0100 7c05 6403  d.d.l.m.}...|.d.
+000006e0: 1900 7c00 1900 4400 5d7b 7d07 7c07 6a02  ..|...D.]{}.|.j.
+000006f0: 7403 7600 7214 710c 7c07 6a02 6404 6b02  t.v.r.q.|.j.d.k.
+00000700: 721c 0100 6405 5300 7404 7c07 6a02 6406  r...d.S.t.|.j.d.
+00000710: 8302 7287 7c03 6407 1900 6408 6b02 722f  ..r.|.d...d.k.r/
+00000720: 7405 7c07 7c04 7c03 7c01 8304 0100 7c07  t.|.|.|.|.....|.
+00000730: 4400 5d55 7d08 7404 7c08 6a02 6409 8302  D.]U}.t.|.j.d...
+00000740: 727f 7c08 6a06 6701 7d09 640a 7c09 6401  r.|.j.g.}.d.|.d.
+00000750: 1900 7601 727d 7407 7c04 7c03 7c01 640b  ..v.r}t.|.|.|.d.
+00000760: 640c 8305 0100 7408 a009 7c08 6a06 7c02  d.....t...|.j.|.
+00000770: 7c09 640c 7c05 640d 1900 a105 5c02 7d0a  |.d.|.d.....\.}.
+00000780: 7d0b 7c08 6a06 6701 7d09 640e 7d0c 640f  }.|.j.g.}.d.}.d.
+00000790: 740a 7c08 6a02 1900 9b00 7c0c 9b00 9d03  t.|.j.....|.....
+000007a0: 7d0d 7c06 7c0d 7c01 7c09 7c0a 7c02 7c03  }.|.|.|.|.|.|.|.
+000007b0: 7c04 7c05 8308 0100 7407 7c04 7c03 7c01  |.|.....t.|.|.|.
+000007c0: 640b 640c 8305 0100 7131 0100 6e08 7c08  d.d.....q1..n.|.
+000007d0: 6a02 6410 6b02 7286 0100 6e01 7131 710c  j.d.k.r...n.q1q.
+000007e0: 6405 5300 2911 615c 0100 000a 0a20 2020  d.S.).a\.....   
+000007f0: 203a 7061 7261 6d20 6d79 5f73 6365 6e65   :param my_scene
+00000800: 3a20 6e61 6d65 206f 6620 5363 656e 6520  : name of Scene 
+00000810: 746f 2070 726f 6365 7373 0a20 2020 203a  to process.    :
+00000820: 7061 7261 6d20 6f75 7470 7574 5f6c 6973  param output_lis
+00000830: 743a 206c 6973 7420 6f66 206f 7574 7075  t: list of outpu
+00000840: 7420 6c69 6e65 730a 2020 2020 3a70 6172  t lines.    :par
+00000850: 616d 2074 6173 6b73 5f66 6f75 6e64 3a20  am tasks_found: 
+00000860: 6c69 7374 206f 6620 5461 736b 7320 666f  list of Tasks fo
+00000870: 756e 6420 736f 2066 6172 0a20 2020 203a  und so far.    :
+00000880: 7061 7261 6d20 7072 6f67 7261 6d5f 6172  param program_ar
+00000890: 6773 3a20 6469 6374 696f 6e61 7279 206f  gs: dictionary o
+000008a0: 6620 7275 6e74 696d 6520 6172 6775 6d65  f runtime argume
+000008b0: 6e74 730a 2020 2020 3a70 6172 616d 2063  nts.    :param c
+000008c0: 6f6c 6f72 6d61 703a 2064 6963 7469 6f6e  olormap: diction
+000008d0: 6172 7920 6f66 2063 6f6c 6f72 7320 746f  ary of colors to
+000008e0: 2075 7365 0a20 2020 203a 7061 7261 6d20   use.    :param 
+000008f0: 616c 6c5f 7461 736b 6572 5f69 7465 6d73  all_tasker_items
+00000900: 3a20 6469 6374 696f 6e61 7279 206f 6620  : dictionary of 
+00000910: 5461 736b 6572 2050 726f 6a65 6374 732f  Tasker Projects/
+00000920: 5072 6f66 696c 6573 2f54 6173 6b73 2f53  Profiles/Tasks/S
+00000930: 6365 6e65 730a 2020 2020 3a72 6574 7572  cenes.    :retur
+00000940: 6e3a 0a20 2020 2072 0100 0000 7204 0000  n:.    r....r...
+00000950: 00da 0a61 6c6c 5f73 6365 6e65 735a 1150  ...all_scenesZ.P
+00000960: 726f 7065 7274 6965 7345 6c65 6d65 6e74  ropertiesElement
+00000970: 4e54 da14 6469 7370 6c61 795f 6465 7461  NT..display_deta
+00000980: 696c 5f6c 6576 656c e903 0000 0046 fa01  il_level.....F..
+00000990: 2de9 0100 0000 da00 da09 616c 6c5f 7461  -.........all_ta
+000009a0: 736b 737a 0f26 6e62 7370 3b26 6e62 7370  sksz.&nbsp;&nbsp
+000009b0: 3b49 443a 7a16 266e 6273 703b 2623 3435  ;ID:z.&nbsp;&#45
+000009c0: 3b26 2334 353b 5461 736b 3a20 7220 0000  ;&#45;Task: r ..
+000009d0: 0029 0bda 166d 6170 7461 736b 6572 2e73  .)...maptasker.s
+000009e0: 7263 2e70 726f 636c 6973 7472 0500 0000  rc.proclistr....
+000009f0: 7224 0000 00da 1453 4345 4e45 5f54 4147  r$.....SCENE_TAG
+00000a00: 535f 544f 5f49 474e 4f52 4572 0300 0000  S_TO_IGNOREr....
+00000a10: 722a 0000 0072 2700 0000 7202 0000 00da  r*...r'...r.....
+00000a20: 0574 6173 6b73 da0d 6765 745f 7461 736b  .tasks..get_task
+00000a30: 5f6e 616d 65da 1053 4345 4e45 5f54 4153  _name..SCENE_TAS
+00000a40: 4b5f 5459 5045 5329 0e72 2b00 0000 721d  K_TYPES).r+...r.
+00000a50: 0000 0072 2c00 0000 721c 0000 0072 1b00  ...r,...r....r..
+00000a60: 0000 722d 0000 0072 0500 0000 721a 0000  ..r-...r....r...
+00000a70: 005a 0973 7562 5f63 6869 6c64 5a0e 7465  .Z.sub_childZ.te
+00000a80: 6d70 5f74 6173 6b5f 6c69 7374 5a0c 7461  mp_task_listZ.ta
+00000a90: 736b 5f65 6c65 6d65 6e74 5a0c 6e61 6d65  sk_elementZ.name
+00000aa0: 5f6f 665f 7461 736b da05 6578 7472 61da  _of_task..extra.
+00000ab0: 0974 6173 6b5f 7479 7065 7228 0000 0072  .task_typer(...r
+00000ac0: 2800 0000 7229 0000 00da 0d70 726f 6365  (...r).....proce
+00000ad0: 7373 5f73 6365 6e65 4e00 0000 735c 0000  ss_sceneN...s\..
+00000ae0: 000c 1310 030a 0102 010a 0106 010c 010c  ................
+00000af0: 020e 0108 010c 0208 020c 0210 0104 0104  ................
+00000b00: 0102 0102 0102 0106 0108 fb08 0804 0102  ................
+00000b10: 0208 0102 ff02 0104 ff02 ff02 0502 0102  ................
+00000b20: 0102 0102 0102 0102 0102 0102 0104 f812  ................
+00000b30: 0a04 020a 0104 0102 ff02 8004 0272 3c00  .............r<.
+00000b40: 0000 da07 7072 6f6a 6563 74da 106f 7572  ....project..our
+00000b50: 5f74 6173 6b5f 656c 656d 656e 74da 0b66  _task_element..f
+00000b60: 6f75 6e64 5f74 6173 6b73 6307 0000 0000  ound_tasksc.....
+00000b70: 0000 0000 0000 0009 0000 0009 0000 0043  ...............C
+00000b80: 0000 0073 9a00 0000 6401 7d07 7400 a001  ...s....d.}.t...
+00000b90: 7402 a101 8f0e 0100 7c00 a003 6402 a101  t.......|...d...
+00000ba0: 6a04 7d07 5700 6401 0400 0400 8303 0100  j.}.W.d.........
+00000bb0: 6e08 3100 7318 7701 0100 0100 0100 5900  n.1.s.w.......Y.
+00000bc0: 0100 7c07 6401 7501 724b 7c07 a005 6403  ..|.d.u.rK|...d.
+00000bd0: a101 7d08 7c03 6404 1900 6405 6b02 7234  ..}.|.d...d.k.r4
+00000be0: 7406 7c01 7c02 7c03 6406 6407 8305 0100  t.|.|.|.d.d.....
+00000bf0: 7c08 6408 1900 724b 7407 6409 7c03 7c08  |.d...rKt.d.|.|.
+00000c00: 7c04 7c05 7c02 7c01 7c06 8308 0100 7406  |.|.|.|.|.....t.
+00000c10: 7c01 7c02 7c03 640a 6407 8305 0100 6401  |.|.|.d.d.....d.
+00000c20: 5300 290b 6101 0200 000a 2020 2020 476f  S.).a.....    Go
+00000c30: 2074 6872 6f75 6768 2061 6c6c 2053 6365   through all Sce
+00000c40: 6e65 7320 666f 7220 5072 6f6a 6563 742c  nes for Project,
+00000c50: 2067 6574 2074 6865 6972 2064 6574 6169   get their detai
+00000c60: 6c20 616e 6420 6f75 7470 7574 2069 740a  l and output it.
+00000c70: 2020 2020 2020 2020 3a70 6172 616d 2070          :param p
+00000c80: 726f 6a65 6374 3a20 786d 6c20 656c 656d  roject: xml elem
+00000c90: 656e 7420 6f66 2050 726f 6a65 6374 2077  ent of Project w
+00000ca0: 6520 6172 6520 7072 6f63 6573 7369 6e67  e are processing
+00000cb0: 0a20 2020 2020 2020 203a 7061 7261 6d20  .        :param 
+00000cc0: 636f 6c6f 726d 6170 3a20 636f 6c6f 7273  colormap: colors
+00000cd0: 2074 6f20 7573 6520 696e 206f 7574 7075   to use in outpu
+00000ce0: 740a 2020 2020 2020 2020 3a70 6172 616d  t.        :param
+00000cf0: 2070 726f 6772 616d 5f61 7267 733a 2072   program_args: r
+00000d00: 756e 7469 6d65 2061 7267 756d 656e 7473  untime arguments
+00000d10: 0a20 2020 2020 2020 203a 7061 7261 6d20  .        :param 
+00000d20: 6f75 7470 7574 5f6c 6973 743a 206c 6973  output_list: lis
+00000d30: 7420 6f66 206f 7574 7075 7420 6c69 6e65  t of output line
+00000d40: 7320 6372 6561 7465 6420 7468 7573 2066  s created thus f
+00000d50: 6172 0a20 2020 2020 2020 203a 7061 7261  ar.        :para
+00000d60: 6d20 6f75 725f 7461 736b 5f65 6c65 6d65  m our_task_eleme
+00000d70: 6e74 3a20 786d 6c20 656c 656d 656e 7420  nt: xml element 
+00000d80: 706f 696e 7469 6e67 2074 6f20 6f75 7220  pointing to our 
+00000d90: 5461 736b 0a20 2020 2020 2020 203a 7061  Task.        :pa
+00000da0: 7261 6d20 666f 756e 645f 7461 736b 733a  ram found_tasks:
+00000db0: 206c 6973 7420 6f66 2054 6173 6b73 2066   list of Tasks f
+00000dc0: 6f75 6e64 2073 6f20 6661 720a 2020 2020  ound so far.    
+00000dd0: 2020 2020 3a70 6172 616d 2061 6c6c 5f74      :param all_t
+00000de0: 6173 6b65 725f 6974 656d 733a 2061 6c6c  asker_items: all
+00000df0: 2050 726f 6a65 6374 732f 5072 6f66 696c   Projects/Profil
+00000e00: 6573 2f54 6173 6b73 2f53 6365 6e65 730a  es/Tasks/Scenes.
+00000e10: 2020 2020 2020 2020 3a72 6574 7572 6e3a          :return:
+00000e20: 206e 6164 610a 2020 2020 4e5a 0673 6365   nada.    NZ.sce
+00000e30: 6e65 73fa 012c e9ff ffff ff7a 053c 2f75  nes..,.....z.</u
+00000e40: 6c3e 7232 0000 0072 3300 0000 7201 0000  l>r2...r3...r...
+00000e50: 007a 0653 6365 6e65 3a72 2100 0000 2908  .z.Scene:r!...).
+00000e60: da0a 636f 6e74 6578 746c 6962 da08 7375  ..contextlib..su
+00000e70: 7070 7265 7373 da09 4578 6365 7074 696f  ppress..Exceptio
+00000e80: 6e72 2600 0000 7227 0000 0072 2500 0000  nr&...r'...r%...
+00000e90: 7202 0000 0072 0500 0000 2909 723d 0000  r....r....).r=..
+00000ea0: 0072 1b00 0000 721c 0000 0072 1d00 0000  .r....r....r....
+00000eb0: 723e 0000 0072 3f00 0000 722d 0000 005a  r>...r?...r-...Z
+00000ec0: 0b73 6365 6e65 5f6e 616d 6573 5a0a 7363  .scene_namesZ.sc
+00000ed0: 656e 655f 6c69 7374 7228 0000 0072 2800  ene_listr(...r(.
+00000ee0: 0000 7229 0000 00da 1670 726f 6365 7373  ..r).....process
+00000ef0: 5f70 726f 6a65 6374 5f73 6365 6e65 7399  _project_scenes.
+00000f00: 0000 0073 2a00 0000 0414 0c01 0e01 1cff  ...s*...........
+00000f10: 0802 0a01 0c05 1001 0802 0201 0201 0201  ................
+00000f20: 0201 0201 0201 0201 0201 0201 04f8 100b  ................
+00000f30: 0401 7245 0000 0029 1572 4200 0000 da15  ..rE...).rB.....
+00000f40: 786d 6c2e 6574 7265 652e 456c 656d 656e  xml.etree.Elemen
+00000f50: 7454 7265 65da 0378 6d6c da13 6d61 7074  tTree..xml..mapt
+00000f60: 6173 6b65 722e 7372 632e 7461 736b 73da  asker.src.tasks.
+00000f70: 0373 7263 7237 0000 00da 156d 6170 7461  .srcr7.....mapta
+00000f80: 736b 6572 2e73 7263 2e6f 7574 7075 746c  sker.src.outputl
+00000f90: 7202 0000 00da 156d 6170 7461 736b 6572  r......maptasker
+00000fa0: 2e73 7263 2e78 6d6c 6461 7461 7203 0000  .src.xmldatar...
+00000fb0: 0072 3500 0000 7205 0000 0072 3900 0000  .r5...r....r9...
+00000fc0: 7236 0000 00da 0565 7472 6565 da04 6469  r6.....etree..di
+00000fd0: 6374 da04 6c69 7374 722a 0000 00da 0373  ct..listr*.....s
+00000fe0: 7472 723c 0000 0072 4500 0000 7228 0000  trr<...rE...r(..
+00000ff0: 0072 2800 0000 7228 0000 0072 2900 0000  .r(...r(...r)...
+00001000: da08 3c6d 6f64 756c 653e 0100 0000 7384  ..<module>....s.
+00001010: 0000 0008 0c08 0212 010c 010c 010c 0102  ................
+00001020: 0302 0102 0102 0102 0102 0102 0102 0102  ................
+00001030: 0102 0102 0102 0102 0102 0102 0106 f108  ................
+00001040: 1102 0b04 0102 ff02 0102 ff02 0102 ff02  ................
+00001050: 0102 ff02 020a fe02 1d02 0102 ff06 0202  ................
+00001060: fe06 0302 fd02 0402 fc02 0502 fb02 0602  ................
+00001070: fa02 070a f902 4b04 0102 ff02 0202 fe02  ......K.........
+00001080: 0302 fd02 0402 fc04 0502 fb02 0602 fa02  ................
+00001090: 0702 f902 080e f8                        .......
```

### Comparing `maptasker-1.3.1/maptasker/src/__pycache__/servicec.cpython-310.pyc` & `maptasker-1.3.2/maptasker/src/__pycache__/servicec.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 10 18:11:52 2023 UTC, .py size: 14219 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 e872 0b64 8b37 0000  o........r.d.7..
+00000000: 6f0d 0d0a 0000 0000 918f 1c64 8b37 0000  o..........d.7..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0010 0000 0040 0000 0073 7a06 0000 6900  .....@...sz...i.
 00000030: 6400 6401 6402 6403 6404 9c03 9301 6405  d.d.d.d.d.....d.
 00000040: 6406 6402 6407 6404 9c03 9301 6408 6409  d.d.d.d.....d.d.
 00000050: 6402 640a 6404 9c03 9301 640b 640c 6402  d.d.d.....d.d.d.
 00000060: 640d 640e 640f 6410 6411 6412 6413 6414  d.d.d.d.d.d.d.d.
 00000070: 6415 6416 6417 6418 9c0a 6419 9c04 9301  d.d.d.d...d.....
@@ -111,57 +111,57 @@
 000006e0: 6d5a 0573 4861 7074 7a0f 4861 7074 6963  mZ.sHaptz.Haptic
 000006f0: 2046 6565 6462 6163 6be9 0200 0000 5a04   Feedback.....Z.
 00000700: 7470 456e 5a04 5469 7073 e903 0000 005a  tpEnZ.Tips.....Z
 00000710: 0d74 6865 6d65 4d61 7465 7269 616c 5a05  .themeMaterialZ.
 00000720: 5468 656d 65e9 0400 0000 7a13 4465 7669  Theme.....z.Devi
 00000730: 6365 2044 6566 6175 6c74 2044 6172 6b7a  ce Default Darkz
 00000740: 1444 6576 6963 6520 4465 6661 756c 7420  .Device Default 
-00000750: 4c69 6768 745a 0444 6172 6b5a 054c 6967  LightZ.DarkZ.Lig
+00000750: 4c69 6768 74da 0444 6172 6bda 054c 6967  Light..Dark..Lig
 00000760: 6874 7a19 4c69 6768 7420 5769 7468 2044  htz.Light With D
 00000770: 6172 6b20 4163 7469 6f6e 4261 72da 0542  ark ActionBar..B
 00000780: 6c61 636b 5a05 436c 6f75 645a 0954 616e  lackZ.CloudZ.Tan
 00000790: 6765 7269 6e65 7a13 4465 7669 6365 2044  gerinez.Device D
 000007a0: 6566 6175 6c74 2041 7574 6f5a 0441 7574  efault AutoZ.Aut
 000007b0: 6f29 0a72 0100 0000 7202 0000 0072 0600  o).r....r....r..
 000007c0: 0000 7207 0000 0072 0800 0000 e905 0000  ..r....r........
 000007d0: 00e9 0600 0000 e907 0000 00e9 0800 0000  ................
 000007e0: e909 0000 0029 0472 0300 0000 7204 0000  .....).r....r...
 000007f0: 0072 0500 0000 da06 7661 6c75 6573 5a0d  .r......valuesZ.
 00000800: 6869 6465 5374 6174 7573 4261 727a 0f48  hideStatusBarz.H
-00000810: 6964 6520 5374 6174 7573 2042 6172 720a  ide Status Barr.
+00000810: 6964 6520 5374 6174 7573 2042 6172 720c  ide Status Barr.
 00000820: 0000 005a 054e 6576 6572 7a13 5768 656e  ...Z.Neverz.When
 00000830: 2045 6469 7469 6e67 2053 6365 6e65 737a   Editing Scenesz
 00000840: 1e57 6865 6e20 5374 6172 7465 6420 696e  .When Started in
 00000850: 204c 616e 6473 6361 7065 204d 6f64 655a   Landscape ModeZ
 00000860: 0641 6c77 6179 7329 0472 0100 0000 7202  .Always).r....r.
 00000870: 0000 0072 0600 0000 7207 0000 005a 0b6f  ...r....r....Z.o
 00000880: 7269 656e 7461 7469 6f6e da0b 4f72 6965  rientation..Orie
-00000890: 6e74 6174 696f 6e72 0b00 0000 5a04 5573  ntationr....Z.Us
+00000890: 6e74 6174 696f 6e72 0d00 0000 5a04 5573  ntationr....Z.Us
 000008a0: 6572 5a08 506f 7274 7261 6974 5a09 4c61  erZ.PortraitZ.La
 000008b0: 6e64 7363 6170 6529 0372 0100 0000 7202  ndscape).r....r.
 000008c0: 0000 0072 0600 0000 5a0b 6472 6167 4d6f  ...r....Z.dragMo
 000008d0: 6465 4e65 777a 124c 6973 7420 4974 656d  deNewz.List Item
-000008e0: 2044 7261 6767 696e 6772 0c00 0000 7a11   Draggingr....z.
+000008e0: 2044 7261 6767 696e 6772 0e00 0000 7a11   Draggingr....z.
 000008f0: 4f6e 2052 6967 6874 2c20 5669 7369 626c  On Right, Visibl
 00000900: 657a 134f 6e20 5269 6768 742c 2049 6e76  ez.On Right, Inv
 00000910: 6973 6962 6c65 7a10 4f6e 204c 6566 742c  isiblez.On Left,
 00000920: 2056 6973 6962 6c65 7a12 4f6e 204c 6566   Visiblez.On Lef
 00000930: 742c 2049 6e76 6973 6962 6c65 7a13 4f6e  t, Invisiblez.On
 00000940: 6c79 2057 6865 6e20 5365 6c65 6374 696e  ly When Selectin
 00000950: 677a 2157 6865 6e20 5365 6c65 6374 696e  gz!When Selectin
 00000960: 672c 2057 6974 6820 4d65 6e75 204f 7074  g, With Menu Opt
 00000970: 696f 6e73 5a08 4469 7361 626c 6564 2907  ionsZ.Disabled).
 00000980: 7201 0000 0072 0200 0000 7206 0000 0072  r....r....r....r
-00000990: 0700 0000 7208 0000 0072 0a00 0000 720b  ....r....r....r.
+00000990: 0700 0000 7208 0000 0072 0c00 0000 720d  ....r....r....r.
 000009a0: 0000 005a 0e6c 6f63 6b49 636f 6e43 6f6c  ...Z.lockIconCol
 000009b0: 6f75 727a 1549 636f 6e20 436f 6c6f 7220  ourz.Icon Color 
-000009c0: 4672 6f6d 2054 6865 6d65 720d 0000 005a  From Themer....Z
+000009c0: 4672 6f6d 2054 6865 6d65 720f 0000 005a  From Themer....Z
 000009d0: 0d68 6172 6477 6172 6541 6363 656c 7a15  .hardwareAccelz.
 000009e0: 4861 7264 7761 7265 2041 6363 656c 6572  Hardware Acceler
-000009f0: 6174 696f 6e72 0e00 0000 5a03 6d53 697a  ationr....Z.mSiz
+000009f0: 6174 696f 6e72 1000 0000 5a03 6d53 697a  ationr....Z.mSiz
 00000a00: 1741 6c77 6179 7320 5368 6f77 2045 6e61  .Always Show Ena
 00000a10: 626c 6520 4963 6f6e e90a 0000 005a 0361  ble Icon.....Z.a
 00000a20: 706e 7a18 4173 6b20 466f 7220 4e65 7720  pnz.Ask For New 
 00000a30: 5072 6f66 696c 6520 4e61 6d65 e90b 0000  Profile Name....
 00000a40: 007a 033f 3f3f 7a17 436f 6e66 6972 6d20  .z.???z.Confirm 
 00000a50: 5072 6f66 696c 6520 4465 6c65 7465 73e9  Profile Deletes.
 00000a60: 0c00 0000 7a04 3f3f 3f3f 7a15 436f 6e66  ....z.????z.Conf
@@ -323,16 +323,16 @@
 00001420: 7a0f 4e6f 2041 7574 6f2d 4261 636b 7570  z.No Auto-Backup
 00001430: 737a 0831 3220 486f 7572 737a 0531 2044  sz.12 Hoursz.1 D
 00001440: 6179 7a06 3220 4461 7973 7a06 3120 5765  ayz.2 Daysz.1 We
 00001450: 656b 7a07 3220 5765 656b 737a 0731 204d  ekz.2 Weeksz.1 M
 00001460: 6f6e 7468 7a08 3220 4d6f 6e74 6873 7a08  onthz.2 Monthsz.
 00001470: 3620 4d6f 6e74 6873 2909 7201 0000 0072  6 Months).r....r
 00001480: 0200 0000 7206 0000 0072 0700 0000 7208  ....r....r....r.
-00001490: 0000 0072 0a00 0000 720b 0000 0072 0c00  ...r....r....r..
-000014a0: 0000 720d 0000 005a 1267 6f6f 676c 6544  ..r....Z.googleD
+00001490: 0000 0072 0c00 0000 720d 0000 0072 0e00  ...r....r....r..
+000014a0: 0000 720f 0000 005a 1267 6f6f 676c 6544  ..r....Z.googleD
 000014b0: 7269 7665 4261 636b 7570 737a 1347 6f6f  riveBackupsz.Goo
 000014c0: 676c 6520 4472 6976 6520 4261 636b 7570  gle Drive Backup
 000014d0: e948 0000 005a 1967 6f6f 676c 6544 7269  .H...Z.googleDri
 000014e0: 7665 4261 636b 7570 7341 6363 6f75 6e74  veBackupsAccount
 000014f0: 7a1b 476f 6f67 6c65 2044 7269 7665 2042  z.Google Drive B
 00001500: 6163 6b75 7020 4163 636f 756e 74e9 4900  ackup Account.I.
 00001510: 0000 5a06 626b 6375 7661 7a16 4261 636b  ..Z.bkcuvaz.Back
@@ -375,15 +375,15 @@
 00001760: 5a19 5052 4546 5f49 535f 5553 494e 475f  Z.PREF_IS_USING_
 00001770: 5445 5354 5f53 4552 5645 525a 0e49 535f  TEST_SERVERZ.IS_
 00001780: 5553 494e 475f 5441 534b 595a 0c62 6567  USING_TASKYZ.beg
 00001790: 696e 6e65 724d 6f64 655a 0b72 756e 6c6f  innerModeZ.runlo
 000017a0: 6750 726f 6673 5a0b 7275 6e6c 6f67 5461  gProfsZ.runlogTa
 000017b0: 736b 735a 0d72 756e 6c6f 6741 6374 696f  sksZ.runlogActio
 000017c0: 6e73 4e29 01da 0d73 6572 7669 6365 5f63  nsN)...service_c
-000017d0: 6f64 6573 a900 7267 0000 0072 6700 0000  odes..rg...rg...
+000017d0: 6f64 6573 a900 7269 0000 0072 6900 0000  odes..ri...ri...
 000017e0: fa77 2f55 7365 7273 2f6d 696b 7275 6269  .w/Users/mikrubi
 000017f0: 6e2f 4c69 6272 6172 792f 436c 6f75 6453  n/Library/CloudS
 00001800: 746f 7261 6765 2f47 6f6f 676c 6544 7269  torage/GoogleDri
 00001810: 7665 2d6d 696b 7275 6269 6e40 676d 6169  ve-mikrubin@gmai
 00001820: 6c2e 636f 6d2f 4d79 2044 7269 7665 2f50  l.com/My Drive/P
 00001830: 7974 686f 6e2f 6d61 7074 6173 6b65 722f  ython/maptasker/
 00001840: 6d61 7074 6173 6b65 722f 7372 632f 7365  maptasker/src/se
```

### Comparing `maptasker-1.3.1/maptasker/src/__pycache__/share.cpython-310.pyc` & `maptasker-1.3.2/maptasker/src/__pycache__/share.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Sun Feb 19 16:04:15 2023 UTC, .py size: 3290 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 24% similar despite different names*

```diff
@@ -1,84 +1,128 @@
-00000000: 6f0d 0d0a 0000 0000 7f48 f263 da0c 0000  o........H.c....
+00000000: 6f0d 0d0a 0000 0000 0f33 2c64 cc10 0000  o........3,d....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
-00000020: 000a 0000 0040 0000 0073 4000 0000 6400  .....@...s@...d.
-00000030: 6401 6c00 5a01 6400 6402 6c02 6d03 5a03  d.l.Z.d.d.l.m.Z.
-00000040: 0100 6403 6501 6a04 6404 6505 6405 6505  ..d.e.j.d.e.d.e.
-00000050: 6406 6506 6407 6401 660a 6408 6409 8404  d.e.d.d.f.d.d...
-00000060: 5a07 640a 640b 8400 5a08 6401 5300 290c  Z.d.d...Z.d.S.).
-00000070: e900 0000 004e 2901 da09 6d79 5f6f 7574  .....N)...my_out
-00000080: 7075 74da 0c72 6f6f 745f 656c 656d 656e  put..root_elemen
-00000090: 74da 0863 6f6c 6f72 6d61 70da 0c70 726f  t..colormap..pro
-000000a0: 6772 616d 5f61 7267 73da 0b6f 7574 7075  gram_args..outpu
-000000b0: 745f 6c69 7374 da06 7265 7475 726e 6304  t_list..returnc.
-000000c0: 0000 0000 0000 0000 0000 0008 0000 0006  ................
-000000d0: 0000 0043 0000 0073 8600 0000 7c00 a000  ...C...s....|...
-000000e0: 6401 a101 7d04 7c04 6400 7501 723d 7c04  d...}.|.d.u.r=|.
-000000f0: a000 6402 a101 7d05 7c05 6400 7501 7219  ..d...}.|.d.u.r.
-00000100: 7401 7c05 7c01 7c02 7c03 8304 0100 7c04  t.|.|.|.|.....|.
-00000110: a000 6403 a101 7d06 7c06 6400 7501 723f  ..d...}.|.d.u.r?
-00000120: 7c06 6a02 7241 7403 7c01 7c02 7c03 6404  |.j.rAt.|.|.|.d.
-00000130: 6405 8305 0100 6406 7c06 6a02 9b00 9d02  d.....d.|.j.....
-00000140: 7d07 7403 7c01 7c02 7c03 6407 7c07 8305  }.t.|.|.|.d.|...
-00000150: 0100 6400 5300 6400 5300 6400 5300 6400  ..d.S.d.S.d.S.d.
-00000160: 5300 2908 4eda 0553 6861 7265 da01 64da  S.).N..Share..d.
-00000170: 0167 e903 0000 00da 007a 1554 6173 6b65  .g.......z.Taske
-00000180: 724e 6574 2073 6561 7263 6820 6f6e 3a20  rNet search on: 
-00000190: e902 0000 0029 04da 0466 696e 64da 1a64  .....)...find..d
-000001a0: 6573 6372 6970 7469 6f6e 5f65 6c65 6d65  escription_eleme
-000001b0: 6e74 5f6f 7574 7075 74da 0474 6578 7472  nt_output..textr
-000001c0: 0200 0000 2908 7203 0000 0072 0400 0000  ....).r....r....
-000001d0: 7205 0000 0072 0600 0000 da0d 7368 6172  r....r......shar
-000001e0: 655f 656c 656d 656e 74da 1364 6573 6372  e_element..descr
-000001f0: 6970 7469 6f6e 5f65 6c65 6d65 6e74 5a0e  iption_elementZ.
-00000200: 7365 6172 6368 5f65 6c65 6d65 6e74 da0a  search_element..
-00000210: 6f75 745f 7374 7269 6e67 a900 7214 0000  out_string..r...
-00000220: 00fa 742f 5573 6572 732f 6d69 6b72 7562  ..t/Users/mikrub
-00000230: 696e 2f4c 6962 7261 7279 2f43 6c6f 7564  in/Library/Cloud
-00000240: 5374 6f72 6167 652f 476f 6f67 6c65 4472  Storage/GoogleDr
-00000250: 6976 652d 6d69 6b72 7562 696e 4067 6d61  ive-mikrubin@gma
-00000260: 696c 2e63 6f6d 2f4d 7920 4472 6976 652f  il.com/My Drive/
-00000270: 5079 7468 6f6e 2f6d 6170 7461 736b 6572  Python/maptasker
-00000280: 2f6d 6170 7461 736b 6572 2f73 7263 2f73  /maptasker/src/s
-00000290: 6861 7265 2e70 79da 0573 6861 7265 1200  hare.py..share..
-000002a0: 0000 731c 0000 000a 0708 010a 0208 0202  ..s.............
-000002b0: 0108 0104 ff0a 040e 0110 020c 0114 0104  ................
-000002c0: f208 0a72 1600 0000 6304 0000 0000 0000  ...r....c.......
-000002d0: 0000 0000 0009 0000 0006 0000 0043 0000  .............C..
-000002e0: 0073 9400 0000 6401 7c00 6a00 9b00 9d02  .s....d.|.j.....
-000002f0: 7d04 6402 7d05 7c04 a001 6403 7c05 a102  }.d.}.|...d.|...
-00000300: 7d04 7c04 a001 6404 7c05 a102 7d04 7c04  }.|...d.|...}.|.
-00000310: a001 6405 7c05 a102 7d04 6406 7d06 7c05  ..d.|...}.d.}.|.
-00000320: 7c04 7601 7240 7402 7c04 8301 4400 5d19  |.v.r@t.|...D.].
-00000330: 5c02 7d07 7d08 7c08 6407 6b02 7239 7c04  \.}.}.|.d.k.r9|.
-00000340: 7c07 6408 1700 1900 6407 6b02 7239 7c06  |.d.....d.k.r9|.
-00000350: 9b00 6402 9d02 6e03 7c06 7c08 1700 7d06  ..d...n.|.|...}.
-00000360: 7124 7c06 7d04 7403 7c01 7c02 7c03 6409  q$|.}.t.|.|.|.d.
-00000370: 7c04 8305 0100 6400 5300 290a 4e7a 1754  |.....d.S.).Nz.T
-00000380: 6173 6b65 724e 6574 2064 6573 6372 6970  askerNet descrip
-00000390: 7469 6f6e 3a20 7a30 3c70 2073 7479 6c65  tion: z0<p style
-000003a0: 3d22 6d61 7267 696e 2d6c 6566 743a 3230  ="margin-left:20
-000003b0: 7078 3b20 6d61 7267 696e 2d72 6967 6874  px; margin-right
-000003c0: 3a35 3070 783b 223e 7a03 3c70 3e7a 053c  :50px;">z.<p>z.<
-000003d0: 6272 2f3e 7a04 3c68 313e 720c 0000 00fa  br/>z.<h1>r.....
-000003e0: 0120 e901 0000 0072 0d00 0000 2904 7210  . .....r....).r.
-000003f0: 0000 00da 0772 6570 6c61 6365 da09 656e  .....replace..en
-00000400: 756d 6572 6174 6572 0200 0000 2909 7212  umerater....).r.
-00000410: 0000 0072 0400 0000 7205 0000 0072 0600  ...r....r....r..
-00000420: 0000 7213 0000 005a 0b69 6e64 656e 745f  ..r....Z.indent_
-00000430: 6874 6d6c 5a08 6e65 775f 6c69 6e65 da08  htmlZ.new_line..
-00000440: 706f 7369 7469 6f6e 5a0f 6368 6172 6163  positionZ.charac
-00000450: 7465 725f 696e 6465 7872 1400 0000 7214  ter_indexr....r.
-00000460: 0000 0072 1500 0000 720f 0000 002c 0000  ...r....r....,..
-00000470: 0073 1c00 0000 0c04 0401 0c03 0c01 0c01  .s..............
-00000480: 0402 0801 1001 1803 0aff 0602 04fd 0405  ................
-00000490: 1403 720f 0000 0029 09da 1578 6d6c 2e65  ..r....)...xml.e
-000004a0: 7472 6565 2e45 6c65 6d65 6e74 5472 6565  tree.ElementTree
-000004b0: da03 786d 6cda 156d 6170 7461 736b 6572  ..xml..maptasker
-000004c0: 2e73 7263 2e6f 7574 7075 746c 7202 0000  .src.outputlr...
-000004d0: 00da 0565 7472 6565 da04 6469 6374 da04  ...etree..dict..
-000004e0: 6c69 7374 7216 0000 0072 0f00 0000 7214  listr....r....r.
-000004f0: 0000 0072 1400 0000 7214 0000 0072 1500  ...r....r....r..
-00000500: 0000 da08 3c6d 6f64 756c 653e 0100 0000  ....<module>....
-00000510: 731c 0000 0008 0d0c 0102 0304 0102 ff02  s...............
-00000520: 0202 fe02 0302 fd02 0402 fc02 050a fb0c  ................
-00000530: 1a                                       .
+00000020: 000a 0000 0040 0000 0073 7600 0000 6400  .....@...sv...d.
+00000030: 6401 6c00 5a00 6400 6401 6c01 5a02 6400  d.l.Z.d.d.l.Z.d.
+00000040: 6402 6c03 6d04 5a04 0100 6400 6403 6c05  d.l.m.Z...d.d.l.
+00000050: 6d06 5a06 0100 6400 6404 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
+00000060: 0100 6405 6502 6a09 6406 650a 6407 650a  ..d.e.j.d.e.d.e.
+00000070: 6408 650b 6409 6401 660a 640a 640b 8404  d.e.d.d.f.d.d...
+00000080: 5a0c 640c 650d 6406 650a 6407 650a 6408  Z.d.e.d.e.d.e.d.
+00000090: 650b 6409 650d 660a 640d 640e 8404 5a0e  e.d.e.f.d.d...Z.
+000000a0: 6401 5300 290f e900 0000 004e 2901 da09  d.S.)......N)...
+000000b0: 6d79 5f6f 7574 7075 7429 01da 1072 656d  my_output)...rem
+000000c0: 6f76 655f 6874 6d6c 5f74 6167 7329 01da  ove_html_tags)..
+000000d0: 0b46 4f4e 545f 544f 5f55 5345 da0c 726f  .FONT_TO_USE..ro
+000000e0: 6f74 5f65 6c65 6d65 6e74 da08 636f 6c6f  ot_element..colo
+000000f0: 726d 6170 da0c 7072 6f67 7261 6d5f 6172  rmap..program_ar
+00000100: 6773 da0b 6f75 7470 7574 5f6c 6973 74da  gs..output_list.
+00000110: 0672 6574 7572 6e63 0400 0000 0000 0000  .returnc........
+00000120: 0000 0000 0800 0000 0600 0000 4300 0000  ............C...
+00000130: 7376 0000 007c 00a0 0064 01a1 017d 047c  sv...|...d...}.|
+00000140: 0464 0075 0172 357c 04a0 0064 02a1 017d  .d.u.r5|...d...}
+00000150: 057c 0564 0075 0172 1974 017c 057c 017c  .|.d.u.r.t.|.|.|
+00000160: 027c 0383 0401 007c 04a0 0064 03a1 017d  .|.....|...d...}
+00000170: 067c 0664 0075 0172 377c 066a 0272 3964  .|.d.u.r7|.j.r9d
+00000180: 047c 066a 029b 009d 027d 0774 037c 017c  .|.j.....}.t.|.|
+00000190: 027c 0364 057c 0783 0501 0064 0053 0064  .|.d.|.....d.S.d
+000001a0: 0053 0064 0053 0064 0053 0029 064e da05  .S.d.S.d.S.).N..
+000001b0: 5368 6172 65da 0164 da01 677a 2126 6e62  Share..d..gz!&nb
+000001c0: 7370 3b26 6e62 7370 3b54 6173 6b65 724e  sp;&nbsp;TaskerN
+000001d0: 6574 2073 6561 7263 6820 6f6e 3a20 e902  et search on: ..
+000001e0: 0000 0029 04da 0466 696e 64da 1a64 6573  ...)...find..des
+000001f0: 6372 6970 7469 6f6e 5f65 6c65 6d65 6e74  cription_element
+00000200: 5f6f 7574 7075 74da 0474 6578 7472 0200  _output..textr..
+00000210: 0000 2908 7205 0000 0072 0600 0000 7207  ..).r....r....r.
+00000220: 0000 0072 0800 0000 da0d 7368 6172 655f  ...r......share_
+00000230: 656c 656d 656e 74da 1364 6573 6372 6970  element..descrip
+00000240: 7469 6f6e 5f65 6c65 6d65 6e74 5a0e 7365  tion_elementZ.se
+00000250: 6172 6368 5f65 6c65 6d65 6e74 da0a 6f75  arch_element..ou
+00000260: 745f 7374 7269 6e67 a900 7214 0000 00fa  t_string..r.....
+00000270: 742f 5573 6572 732f 6d69 6b72 7562 696e  t/Users/mikrubin
+00000280: 2f4c 6962 7261 7279 2f43 6c6f 7564 5374  /Library/CloudSt
+00000290: 6f72 6167 652f 476f 6f67 6c65 4472 6976  orage/GoogleDriv
+000002a0: 652d 6d69 6b72 7562 696e 4067 6d61 696c  e-mikrubin@gmail
+000002b0: 2e63 6f6d 2f4d 7920 4472 6976 652f 5079  .com/My Drive/Py
+000002c0: 7468 6f6e 2f6d 6170 7461 736b 6572 2f6d  thon/maptasker/m
+000002d0: 6170 7461 736b 6572 2f73 7263 2f73 6861  aptasker/src/sha
+000002e0: 7265 2e70 79da 0573 6861 7265 1800 0000  re.py..share....
+000002f0: 731a 0000 000a 0708 010a 0208 0202 0108  s...............
+00000300: 0104 ff0a 040e 010c 0314 0104 f208 0a72  ...............r
+00000310: 1600 0000 7212 0000 0063 0400 0000 0000  ....r....c......
+00000320: 0000 0000 0000 0900 0000 0600 0000 4300  ..............C.
+00000330: 0000 73f6 0000 0064 017c 006a 009b 009d  ..s....d.|.j....
+00000340: 027d 0464 027c 0164 0319 009b 0074 019b  .}.d.|.d.....t..
+00000350: 0064 049d 047d 057c 04a0 0264 057c 05a1  .d...}.|...d.|..
+00000360: 027d 047c 04a0 0264 067c 05a1 027d 047c  .}.|...d.|...}.|
+00000370: 04a0 0264 077c 05a1 027d 047c 04a0 0264  ...d.|...}.|...d
+00000380: 087c 05a1 027d 047c 04a0 0264 097c 059b  .|...}.|...d.|..
+00000390: 00a1 027d 047c 04a0 0264 0a64 0ba1 027d  ...}.|...d.d...}
+000003a0: 0464 0b7d 067c 057c 0476 0172 6e74 037c  .d.}.|.|.v.rnt.|
+000003b0: 0483 0144 005d 2c5c 027d 077d 087c 0864  ...D.],\.}.}.|.d
+000003c0: 0c6b 0272 4f7c 047c 0764 0d17 0019 0064  .k.rO|.|.d.....d
+000003d0: 0c6b 0273 5b7c 0864 0e6b 0272 677c 047c  .k.s[|.d.k.rg|.|
+000003e0: 0764 0d17 0019 0064 0c6b 0272 677c 069b  .d.....d.k.rg|..
+000003f0: 0064 0f7c 0164 0319 009b 0074 019b 0064  .d.|.d.....t...d
+00000400: 049d 056e 037c 067c 0817 007d 0671 3f7c  ...n.|.|...}.q?|
+00000410: 067d 047c 049b 007d 0474 047c 017c 027c  .}.|...}.t.|.|.|
+00000420: 0364 107c 0483 0501 0064 1153 0029 1261  .d.|.....d.S.).a
+00000430: 2c01 0000 0a20 2020 2057 6520 6861 7665  ,....    We have
+00000440: 2061 2054 6173 6b65 726e 6574 2064 6573   a Taskernet des
+00000450: 6372 6970 7469 6f6e 2028 3c53 6861 7265  cription (<Share
+00000460: 3e29 2e20 2050 726f 6365 7373 2069 740a  >).  Process it.
+00000470: 2020 2020 2020 2020 3a70 6172 616d 2064          :param d
+00000480: 6573 6372 6970 7469 6f6e 5f65 6c65 6d65  escription_eleme
+00000490: 6e74 3a20 7468 6520 786d 6c20 656c 656d  nt: the xml elem
+000004a0: 656e 7420 7769 7468 2074 6865 2064 6573  ent with the des
+000004b0: 6372 6970 7469 6f6e 0a20 2020 2020 2020  cription.       
+000004c0: 203a 7061 7261 6d20 636f 6c6f 726d 6170   :param colormap
+000004d0: 3a20 7468 6520 636f 6c6f 7273 2074 6f20  : the colors to 
+000004e0: 7573 6520 666f 7220 7468 6520 6f75 7470  use for the outp
+000004f0: 7574 0a20 2020 2020 2020 203a 7061 7261  ut.        :para
+00000500: 6d20 7072 6f67 7261 6d5f 6172 6773 3a20  m program_args: 
+00000510: 7468 6520 7275 6e74 696d 6520 6172 6775  the runtime argu
+00000520: 6d65 6e74 730a 2020 2020 2020 2020 3a70  ments.        :p
+00000530: 6172 616d 206f 7574 7075 745f 6c69 7374  aram output_list
+00000540: 3a20 7468 6520 6f75 7470 7574 206c 696e  : the output lin
+00000550: 6573 2074 6875 7320 6661 720a 2020 2020  es thus far.    
+00000560: 7a23 266e 6273 703b 266e 6273 703b 5461  z#&nbsp;&nbsp;Ta
+00000570: 736b 6572 4e65 7420 6465 7363 7269 7074  skerNet descript
+00000580: 696f 6e3a 207a 373c 2f70 3e3c 7020 7374  ion: z7</p><p st
+00000590: 796c 653d 226d 6172 6769 6e2d 6c65 6674  yle="margin-left
+000005a0: 3a32 3070 783b 6d61 7267 696e 2d72 6967  :20px;margin-rig
+000005b0: 6874 3a35 3070 783b 636f 6c6f 723a da0f  ht:50px;color:..
+000005c0: 7461 736b 6572 6e65 745f 636f 6c6f 72fa  taskernet_color.
+000005d0: 013e 7a03 3c70 3e7a 053c 6272 2f3e 7a04  .>z.<p>z.<br/>z.
+000005e0: 3c68 313e fa01 0d7a 043c 6c69 3e7a 053c  <h1>...z.<li>z.<
+000005f0: 2f6c 693e da00 fa01 20e9 0100 0000 fa01  /li>.... .......
+00000600: 2d7a 333c 7020 7374 796c 653d 226d 6172  -z3<p style="mar
+00000610: 6769 6e2d 6c65 6674 3a32 3070 783b 6d61  gin-left:20px;ma
+00000620: 7267 696e 2d72 6967 6874 3a35 3070 783b  rgin-right:50px;
+00000630: 636f 6c6f 723a 720d 0000 004e 2905 7210  color:r....N).r.
+00000640: 0000 0072 0400 0000 da07 7265 706c 6163  ...r......replac
+00000650: 65da 0965 6e75 6d65 7261 7465 7202 0000  e..enumerater...
+00000660: 0029 0972 1200 0000 7206 0000 0072 0700  .).r....r....r..
+00000670: 0000 7208 0000 0072 1300 0000 5a0b 696e  ..r....r....Z.in
+00000680: 6465 6e74 5f68 746d 6c5a 086e 6577 5f6c  dent_htmlZ.new_l
+00000690: 696e 655a 0870 6f73 6974 696f 6e5a 0f63  ineZ.positionZ.c
+000006a0: 6861 7261 6374 6572 5f69 6e64 6578 7214  haracter_indexr.
+000006b0: 0000 0072 1400 0000 7215 0000 0072 0f00  ...r....r....r..
+000006c0: 0000 3200 0000 7338 0000 000c 0b02 0206  ..2...s8........
+000006d0: 0102 ff02 0106 ff02 ff0c 060c 010c 010c  ................
+000006e0: 010e 010c 0104 0408 0110 0118 0418 0106  ................
+000006f0: fd06 0102 ff02 0108 ff06 0404 fb04 0706  ................
+00000700: 0114 0272 0f00 0000 290f da02 7265 da15  ...r....)...re..
+00000710: 786d 6c2e 6574 7265 652e 456c 656d 656e  xml.etree.Elemen
+00000720: 7454 7265 65da 0378 6d6c da15 6d61 7074  tTree..xml..mapt
+00000730: 6173 6b65 722e 7372 632e 6f75 7470 7574  asker.src.output
+00000740: 6c72 0200 0000 da15 6d61 7074 6173 6b65  lr......maptaske
+00000750: 722e 7372 632e 786d 6c64 6174 6172 0300  r.src.xmldatar..
+00000760: 0000 da16 6d61 7074 6173 6b65 722e 7372  ....maptasker.sr
+00000770: 632e 7379 7363 6f6e 7374 7204 0000 00da  c.sysconstr.....
+00000780: 0565 7472 6565 da04 6469 6374 da04 6c69  .etree..dict..li
+00000790: 7374 7216 0000 00da 0373 7472 720f 0000  str......strr...
+000007a0: 0072 1400 0000 7214 0000 0072 1400 0000  .r....r....r....
+000007b0: 7215 0000 00da 083c 6d6f 6475 6c65 3e01  r......<module>.
+000007c0: 0000 0073 3600 0000 0802 080d 0c03 0c01  ...s6...........
+000007d0: 0c01 0203 0401 02ff 0202 02fe 0203 02fd  ................
+000007e0: 0204 02fc 0205 0afb 021a 0201 02ff 0201  ................
+000007f0: 02ff 0201 02ff 0201 02ff 0202 0efe       ..............
```

### Comparing `maptasker-1.3.1/maptasker/src/__pycache__/shellsort.cpython-310.pyc` & `maptasker-1.3.2/maptasker/src/__pycache__/shellsort.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Sun Feb 19 16:04:15 2023 UTC, .py size: 3354 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 7f48 f263 1a0d 0000  o........H.c....
+00000000: 6f0d 0d0a 0000 0000 918f 1c64 1a0d 0000  o..........d....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0002 0000 0040 0000 0073 1800 0000 6400  .....@...s....d.
 00000030: 6401 6c00 6d01 5a01 0100 6402 6403 8400  d.l.m.Z...d.d...
 00000040: 5a02 6404 5300 2905 e900 0000 0029 01da  Z.d.S.)......)..
 00000050: 066c 6f67 6765 7263 0300 0000 0000 0000  .loggerc........
 00000060: 0000 0000 0d00 0000 0700 0000 4300 0000  ............C...
 00000070: 736a 0100 0074 007c 0083 017d 037c 0364  sj...t.|...}.|.d
```

### Comparing `maptasker-1.3.1/maptasker/src/__pycache__/sysconst.cpython-310.pyc` & `maptasker-1.3.2/maptasker/src/__pycache__/sysconst.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Thu Mar 16 15:25:34 2023 UTC, .py size: 4071 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 7% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 ee34 1364 e70f 0000  o........4.d....
+00000000: 6f0d 0d0a 0000 0000 b761 2c64 f20f 0000  o........a,d....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0073 9601 0000 6400  .....@...s....d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c00  d.l.m.Z...d.d.l.
 00000040: 6d02 5a02 0100 6403 5a03 6404 5a04 6405  m.Z...d.Z.d.Z.d.
 00000050: 5a05 6406 5a06 6407 5a07 6408 5a08 6409  Z.d.Z.d.Z.d.Z.d.
 00000060: 6501 9b00 640a 9d03 5a09 640b 5a0a 6900  e...d...Z.d.Z.i.
 00000070: 640c 640d 9301 640e 640d 9301 640f 6410  d.d...d.d...d.d.
@@ -25,124 +25,125 @@
 00000180: 642c 642a 9301 642f 6447 9301 6432 6448  d,d*..d/dG..d2dH
 00000190: 9301 6435 6449 9301 6438 644a 9301 643b  ..d5dI..d8dJ..d;
 000001a0: 644b 9301 643e 643c 6901 a501 5a0c 6502  dK..d>d<i...Z.e.
 000001b0: a00d 644c a101 5a0e 644d 5a0f 644d 5a10  ..dL..Z.dMZ.dMZ.
 000001c0: 644e 5300 294f e900 0000 0029 01da 0b4f  dNS.)O.....)...O
 000001d0: 5554 5055 545f 464f 4e54 2901 da07 6c6f  UTPUT_FONT)...lo
 000001e0: 6767 696e 677a 1255 6e6e 616d 6564 2f41  ggingz.Unnamed/A
-000001f0: 6e6f 6e79 6d6f 7573 2e7a 184d 6170 5461  nonymous.z.MapTa
+000001f0: 6e6f 6e79 6d6f 7573 2e7a 174d 6170 5461  nonymous.z.MapTa
 00000200: 736b 6572 2076 6572 7369 6f6e 2031 2e33  sker version 1.3
-00000210: 2e30 317a 3447 4e55 2047 454e 4552 414c  .01z4GNU GENERAL
-00000220: 2050 5542 4c49 4320 4c49 4345 4e53 4520   PUBLIC LICENSE 
-00000230: 2856 6572 7369 6f6e 2033 2c20 3239 204a  (Version 3, 29 J
-00000240: 756e 6520 3230 3037 297a 0c2d 6e6f 6e65  une 2007)z.-none
-00000250: 2066 6f75 6e64 2e7a 172e 4d61 7054 6173   found.z..MapTas
-00000260: 6b65 725f 5275 6e43 6f75 6e74 2e74 7874  ker_RunCount.txt
-00000270: 7a0e 2e61 7267 756d 656e 7473 2e74 7874  z..arguments.txt
-00000280: 7a0b 3c66 6f6e 7420 6661 6365 3dfa 013e  z.<font face=..>
-00000290: 7a10 4e6f 6e65 206f 7220 756e 6e61 6d65  z.None or unname
-000002a0: 6421 5a08 5072 6f6a 6563 7473 da0d 7072  d!Z.Projects..pr
-000002b0: 6f6a 6563 745f 636f 6c6f 72da 0750 726f  oject_color..Pro
-000002c0: 6a65 6374 5a08 5072 6f66 696c 6573 da0d  jectZ.Profiles..
-000002d0: 7072 6f66 696c 655f 636f 6c6f 72da 0750  profile_color..P
-000002e0: 726f 6669 6c65 5a05 5461 736b 73da 0a74  rofileZ.Tasks..t
-000002f0: 6173 6b5f 636f 6c6f 72da 0454 6173 6b7a  ask_color..Taskz
-00000300: 0e28 5461 736b 2920 4163 7469 6f6e 73da  .(Task) Actions.
-00000310: 0c61 6374 696f 6e5f 636f 6c6f 72da 0641  .action_color..A
-00000320: 6374 696f 6e7a 1144 6973 6162 6c65 6420  ctionz.Disabled 
-00000330: 5072 6f66 696c 6573 5a16 6469 7361 626c  ProfilesZ.disabl
-00000340: 6564 5f70 726f 6669 6c65 5f63 6f6c 6f72  ed_profile_color
-00000350: 5a0f 4469 7361 626c 6564 5072 6f66 696c  Z.DisabledProfil
-00000360: 655a 0b55 6e6b 6e6f 776e 5461 736b da12  eZ.UnknownTask..
-00000370: 756e 6b6e 6f77 6e5f 7461 736b 5f63 6f6c  unknown_task_col
-00000380: 6f72 5a0e 4469 7361 626c 6564 4163 7469  orZ.DisabledActi
-00000390: 6f6e 5a15 6469 7361 626c 6564 5f61 6374  onZ.disabled_act
-000003a0: 696f 6e5f 636f 6c6f 727a 1141 6374 696f  ion_colorz.Actio
-000003b0: 6e20 436f 6e64 6974 696f 6e73 5a16 6163  n ConditionsZ.ac
-000003c0: 7469 6f6e 5f63 6f6e 6469 7469 6f6e 5f63  tion_condition_c
-000003d0: 6f6c 6f72 5a0f 4163 7469 6f6e 436f 6e64  olorZ.ActionCond
-000003e0: 6974 696f 6e7a 1250 726f 6669 6c65 2043  itionz.Profile C
-000003f0: 6f6e 6469 7469 6f6e 735a 1770 726f 6669  onditionsZ.profi
-00000400: 6c65 5f63 6f6e 6469 7469 6f6e 5f63 6f6c  le_condition_col
-00000410: 6f72 5a10 5072 6f66 696c 6543 6f6e 6469  orZ.ProfileCondi
-00000420: 7469 6f6e 7a0d 4c61 756e 6368 6572 2054  tionz.Launcher T
-00000430: 6173 6b5a 136c 6175 6e63 6865 725f 7461  askZ.launcher_ta
-00000440: 736b 5f63 6f6c 6f72 5a0c 4c61 756e 6368  sk_colorZ.Launch
-00000450: 6572 5461 736b 5a0a 4261 636b 6772 6f75  erTaskZ.Backgrou
-00000460: 6e64 5a10 6261 636b 6772 6f75 6e64 5f63  ndZ.background_c
-00000470: 6f6c 6f72 5a06 5363 656e 6573 da0b 7363  olorZ.Scenes..sc
-00000480: 656e 655f 636f 6c6f 725a 0553 6365 6e65  ene_colorZ.Scene
-00000490: 5a07 4275 6c6c 6574 73da 0c62 756c 6c65  Z.Bullets..bulle
-000004a0: 745f 636f 6c6f 725a 0642 756c 6c65 747a  t_colorZ.Bulletz
-000004b0: 0d41 6374 696f 6e20 4c61 6265 6c73 5a12  .Action LabelsZ.
-000004c0: 6163 7469 6f6e 5f6c 6162 656c 5f63 6f6c  action_label_col
-000004d0: 6f72 5a0b 4163 7469 6f6e 4c61 6265 6c7a  orZ.ActionLabelz
-000004e0: 0c41 6374 696f 6e20 4e61 6d65 735a 1161  .Action NamesZ.a
-000004f0: 6374 696f 6e5f 6e61 6d65 5f63 6f6c 6f72  ction_name_color
-00000500: 5a0a 4163 7469 6f6e 4e61 6d65 7a15 5461  Z.ActionNamez.Ta
-00000510: 736b 6572 4e65 7420 496e 666f 726d 6174  skerNet Informat
-00000520: 696f 6eda 0f74 6173 6b65 726e 6574 5f63  ion..taskernet_c
-00000530: 6f6c 6f72 5a0d 5461 736b 6572 4e65 7449  olorZ.TaskerNetI
-00000540: 6e66 6f7a 1254 6173 6b65 7220 5072 6566  nfoz.Tasker Pref
-00000550: 6572 656e 6365 735a 1170 7265 6665 7265  erencesZ.prefere
-00000560: 6e63 6573 5f63 6f6c 6f72 5a0b 5072 6566  nces_colorZ.Pref
-00000570: 6572 656e 6365 737a 1154 7261 696c 696e  erencesz.Trailin
-00000580: 6720 436f 6d6d 656e 7473 5a17 7472 6169  g CommentsZ.trai
-00000590: 6c69 6e67 5f63 6f6d 6d65 6e74 735f 636f  ling_comments_co
-000005a0: 6c6f 725a 1054 7261 696c 696e 6743 6f6d  lorZ.TrailingCom
-000005b0: 6d65 6e74 737a 0e54 6173 6b20 2761 6374  mentsz.Task 'act
-000005c0: 696f 6e73 277a 1327 6469 7361 626c 6564  ions'z.'disabled
-000005d0: 2720 5072 6f66 696c 6573 7a0f 2775 6e6b  ' Profilesz.'unk
-000005e0: 6e6f 776e 2720 5461 736b 737a 1764 6973  nown' Tasksz.dis
-000005f0: 6162 6c65 6420 5461 736b 2027 6163 7469  abled Task 'acti
-00000600: 6f6e 7327 7a18 5461 736b 2061 6374 696f  ons'z.Task actio
-00000610: 6e20 2763 6f6e 6469 7469 6f6e 7327 7a14  n 'conditions'z.
-00000620: 5072 6f66 696c 6520 2763 6f6e 6469 7469  Profile 'conditi
-00000630: 6f6e 7327 7a19 5072 6f6a 6563 7427 7320  ons'z.Project's 
-00000640: 276c 6175 6e63 6865 7227 2054 6173 6b7a  'launcher' Taskz
-00000650: 116f 7574 7075 7420 6261 636b 6772 6f75  .output backgrou
-00000660: 6e64 7a0c 6c69 7374 2062 756c 6c65 7473  ndz.list bullets
-00000670: 7a14 5461 736b 2061 6374 696f 6e20 276c  z.Task action 'l
-00000680: 6162 656c 7327 7a13 5461 736b 2061 6374  abels'z.Task act
-00000690: 696f 6e20 276e 616d 6573 277a 1754 6173  ion 'names'z.Tas
-000006a0: 6b65 724e 6574 2027 696e 666f 726d 6174  kerNet 'informat
-000006b0: 696f 6e27 7a14 5461 736b 6572 2027 7072  ion'z.Tasker 'pr
-000006c0: 6566 6572 656e 6365 7327 da09 4d61 7054  eferences'..MapT
-000006d0: 6173 6b65 7246 4e29 115a 146d 6170 7461  askerFN).Z.mapta
-000006e0: 736b 6572 2e73 7263 2e63 6f6e 6669 6772  sker.src.configr
-000006f0: 0200 0000 7203 0000 00da 1155 4e4b 4e4f  ....r......UNKNO
-00000700: 574e 5f54 4153 4b5f 4e41 4d45 5a0a 4d59  WN_TASK_NAMEZ.MY
-00000710: 5f56 4552 5349 4f4e 5a0a 4d59 5f4c 4943  _VERSIONZ.MY_LIC
-00000720: 454e 5345 5a0a 4e4f 5f50 524f 4a45 4354  ENSEZ.NO_PROJECT
-00000730: da0c 434f 554e 5445 525f 4649 4c45 5a0e  ..COUNTER_FILEZ.
-00000740: 4152 4755 4d45 4e54 535f 4649 4c45 da0b  ARGUMENTS_FILE..
-00000750: 464f 4e54 5f54 4f5f 5553 455a 0a4e 4f5f  FONT_TO_USEZ.NO_
-00000760: 5052 4f46 494c 455a 1454 5950 4553 5f4f  PROFILEZ.TYPES_O
-00000770: 465f 434f 4c4f 525f 4e41 4d45 535a 0f54  F_COLOR_NAMESZ.T
-00000780: 5950 4553 5f4f 465f 434f 4c4f 5253 da09  YPES_OF_COLORS..
-00000790: 6765 744c 6f67 6765 72da 066c 6f67 6765  getLogger..logge
-000007a0: 72da 0964 6562 7567 5f6f 7574 5a0d 4445  r..debug_outZ.DE
-000007b0: 4255 475f 5052 4f47 5241 4da9 0072 1800  BUG_PROGRAM..r..
-000007c0: 0000 7218 0000 00fa 772f 5573 6572 732f  ..r.....w/Users/
-000007d0: 6d69 6b72 7562 696e 2f4c 6962 7261 7279  mikrubin/Library
-000007e0: 2f43 6c6f 7564 5374 6f72 6167 652f 476f  /CloudStorage/Go
-000007f0: 6f67 6c65 4472 6976 652d 6d69 6b72 7562  ogleDrive-mikrub
-00000800: 696e 4067 6d61 696c 2e63 6f6d 2f4d 7920  in@gmail.com/My 
-00000810: 4472 6976 652f 5079 7468 6f6e 2f6d 6170  Drive/Python/map
-00000820: 7461 736b 6572 2f6d 6170 7461 736b 6572  tasker/maptasker
-00000830: 2f73 7263 2f73 7973 636f 6e73 742e 7079  /src/sysconst.py
-00000840: da08 3c6d 6f64 756c 653e 0100 0000 73ea  ..<module>....s.
-00000850: 0000 000c 0d0c 0104 0304 0104 0104 0104  ................
-00000860: 0104 010c 0104 0102 0704 0102 ff04 0202  ................
-00000870: fe04 0302 fd04 0402 fc04 0502 fb04 0602  ................
-00000880: fa04 0702 f904 0802 f804 0902 f704 0a02  ................
-00000890: f604 0b02 f504 0c02 f404 0d02 f304 0e02  ................
-000008a0: f204 0f02 f104 1002 f004 1104 ef04 1202  ................
-000008b0: ee04 1302 ed04 1402 ec04 1502 eb04 1602  ................
-000008c0: ea04 1702 e904 1802 e804 1902 e704 1a02  ................
-000008d0: e604 1b02 e504 1c02 e404 1d02 e304 1e02  ................
-000008e0: e204 1f02 e104 2002 e004 2106 df02 2504  ...... ...!...%.
-000008f0: 0102 ff04 0202 fe04 0302 fd04 0402 fc04  ................
-00000900: 0502 fb04 0602 fa04 0702 f904 0802 f804  ................
-00000910: 0902 f704 0a02 f604 0b02 f504 0c02 f404  ................
-00000920: 0d02 f304 0e02 f204 0f02 f104 1002 f004  ................
-00000930: 1102 ef04 1206 ee0a 1504 0108 01         .............
+00000210: 2e32 7a34 474e 5520 4745 4e45 5241 4c20  .2z4GNU GENERAL 
+00000220: 5055 424c 4943 204c 4943 454e 5345 2028  PUBLIC LICENSE (
+00000230: 5665 7273 696f 6e20 332c 2032 3920 4a75  Version 3, 29 Ju
+00000240: 6e65 2032 3030 3729 7a0c 2d6e 6f6e 6520  ne 2007)z.-none 
+00000250: 666f 756e 642e 7a17 2e4d 6170 5461 736b  found.z..MapTask
+00000260: 6572 5f52 756e 436f 756e 742e 7478 747a  er_RunCount.txtz
+00000270: 182e 4d61 7054 6173 6b65 725f 6172 6775  ..MapTasker_argu
+00000280: 6d65 6e74 732e 7478 747a 0d3b 666f 6e74  ments.txtz.;font
+00000290: 2d66 616d 696c 793a fa01 227a 104e 6f6e  -family:.."z.Non
+000002a0: 6520 6f72 2075 6e6e 616d 6564 215a 0850  e or unnamed!Z.P
+000002b0: 726f 6a65 6374 73da 0d70 726f 6a65 6374  rojects..project
+000002c0: 5f63 6f6c 6f72 da07 5072 6f6a 6563 745a  _color..ProjectZ
+000002d0: 0850 726f 6669 6c65 73da 0d70 726f 6669  .Profiles..profi
+000002e0: 6c65 5f63 6f6c 6f72 da07 5072 6f66 696c  le_color..Profil
+000002f0: 655a 0554 6173 6b73 da0a 7461 736b 5f63  eZ.Tasks..task_c
+00000300: 6f6c 6f72 da04 5461 736b 7a0e 2854 6173  olor..Taskz.(Tas
+00000310: 6b29 2041 6374 696f 6e73 da0c 6163 7469  k) Actions..acti
+00000320: 6f6e 5f63 6f6c 6f72 5a06 4163 7469 6f6e  on_colorZ.Action
+00000330: 7a11 4469 7361 626c 6564 2050 726f 6669  z.Disabled Profi
+00000340: 6c65 735a 1664 6973 6162 6c65 645f 7072  lesZ.disabled_pr
+00000350: 6f66 696c 655f 636f 6c6f 725a 0f44 6973  ofile_colorZ.Dis
+00000360: 6162 6c65 6450 726f 6669 6c65 5a0b 556e  abledProfileZ.Un
+00000370: 6b6e 6f77 6e54 6173 6bda 1275 6e6b 6e6f  knownTask..unkno
+00000380: 776e 5f74 6173 6b5f 636f 6c6f 725a 0e44  wn_task_colorZ.D
+00000390: 6973 6162 6c65 6441 6374 696f 6eda 1564  isabledAction..d
+000003a0: 6973 6162 6c65 645f 6163 7469 6f6e 5f63  isabled_action_c
+000003b0: 6f6c 6f72 7a11 4163 7469 6f6e 2043 6f6e  olorz.Action Con
+000003c0: 6469 7469 6f6e 73da 1661 6374 696f 6e5f  ditions..action_
+000003d0: 636f 6e64 6974 696f 6e5f 636f 6c6f 725a  condition_colorZ
+000003e0: 0f41 6374 696f 6e43 6f6e 6469 7469 6f6e  .ActionCondition
+000003f0: 7a12 5072 6f66 696c 6520 436f 6e64 6974  z.Profile Condit
+00000400: 696f 6e73 5a17 7072 6f66 696c 655f 636f  ionsZ.profile_co
+00000410: 6e64 6974 696f 6e5f 636f 6c6f 725a 1050  ndition_colorZ.P
+00000420: 726f 6669 6c65 436f 6e64 6974 696f 6e7a  rofileConditionz
+00000430: 0d4c 6175 6e63 6865 7220 5461 736b 5a13  .Launcher TaskZ.
+00000440: 6c61 756e 6368 6572 5f74 6173 6b5f 636f  launcher_task_co
+00000450: 6c6f 725a 0c4c 6175 6e63 6865 7254 6173  lorZ.LauncherTas
+00000460: 6b5a 0a42 6163 6b67 726f 756e 645a 1062  kZ.BackgroundZ.b
+00000470: 6163 6b67 726f 756e 645f 636f 6c6f 725a  ackground_colorZ
+00000480: 0653 6365 6e65 73da 0b73 6365 6e65 5f63  .Scenes..scene_c
+00000490: 6f6c 6f72 5a05 5363 656e 655a 0742 756c  olorZ.SceneZ.Bul
+000004a0: 6c65 7473 da0c 6275 6c6c 6574 5f63 6f6c  lets..bullet_col
+000004b0: 6f72 5a06 4275 6c6c 6574 7a0d 4163 7469  orZ.Bulletz.Acti
+000004c0: 6f6e 204c 6162 656c 73da 1261 6374 696f  on Labels..actio
+000004d0: 6e5f 6c61 6265 6c5f 636f 6c6f 725a 0b41  n_label_colorZ.A
+000004e0: 6374 696f 6e4c 6162 656c 7a0c 4163 7469  ctionLabelz.Acti
+000004f0: 6f6e 204e 616d 6573 da11 6163 7469 6f6e  on Names..action
+00000500: 5f6e 616d 655f 636f 6c6f 725a 0a41 6374  _name_colorZ.Act
+00000510: 696f 6e4e 616d 657a 1554 6173 6b65 724e  ionNamez.TaskerN
+00000520: 6574 2049 6e66 6f72 6d61 7469 6f6e da0f  et Information..
+00000530: 7461 736b 6572 6e65 745f 636f 6c6f 725a  taskernet_colorZ
+00000540: 0d54 6173 6b65 724e 6574 496e 666f 7a12  .TaskerNetInfoz.
+00000550: 5461 736b 6572 2050 7265 6665 7265 6e63  Tasker Preferenc
+00000560: 6573 5a11 7072 6566 6572 656e 6365 735f  esZ.preferences_
+00000570: 636f 6c6f 725a 0b50 7265 6665 7265 6e63  colorZ.Preferenc
+00000580: 6573 7a11 5472 6169 6c69 6e67 2043 6f6d  esz.Trailing Com
+00000590: 6d65 6e74 735a 1774 7261 696c 696e 675f  mentsZ.trailing_
+000005a0: 636f 6d6d 656e 7473 5f63 6f6c 6f72 5a10  comments_colorZ.
+000005b0: 5472 6169 6c69 6e67 436f 6d6d 656e 7473  TrailingComments
+000005c0: 7a0e 5461 736b 2027 6163 7469 6f6e 7327  z.Task 'actions'
+000005d0: 7a13 2764 6973 6162 6c65 6427 2050 726f  z.'disabled' Pro
+000005e0: 6669 6c65 737a 0f27 756e 6b6e 6f77 6e27  filesz.'unknown'
+000005f0: 2054 6173 6b73 7a17 6469 7361 626c 6564   Tasksz.disabled
+00000600: 2054 6173 6b20 2761 6374 696f 6e73 277a   Task 'actions'z
+00000610: 1854 6173 6b20 6163 7469 6f6e 2027 636f  .Task action 'co
+00000620: 6e64 6974 696f 6e73 277a 1450 726f 6669  nditions'z.Profi
+00000630: 6c65 2027 636f 6e64 6974 696f 6e73 277a  le 'conditions'z
+00000640: 1950 726f 6a65 6374 2773 2027 6c61 756e  .Project's 'laun
+00000650: 6368 6572 2720 5461 736b 7a11 6f75 7470  cher' Taskz.outp
+00000660: 7574 2062 6163 6b67 726f 756e 647a 0c6c  ut backgroundz.l
+00000670: 6973 7420 6275 6c6c 6574 737a 1454 6173  ist bulletsz.Tas
+00000680: 6b20 6163 7469 6f6e 2027 6c61 6265 6c73  k action 'labels
+00000690: 277a 1354 6173 6b20 6163 7469 6f6e 2027  'z.Task action '
+000006a0: 6e61 6d65 7327 7a17 5461 736b 6572 4e65  names'z.TaskerNe
+000006b0: 7420 2769 6e66 6f72 6d61 7469 6f6e 277a  t 'information'z
+000006c0: 1454 6173 6b65 7220 2770 7265 6665 7265  .Tasker 'prefere
+000006d0: 6e63 6573 275a 094d 6170 5461 736b 6572  nces'Z.MapTasker
+000006e0: 464e 2911 da14 6d61 7074 6173 6b65 722e  FN)...maptasker.
+000006f0: 7372 632e 636f 6e66 6967 7202 0000 0072  src.configr....r
+00000700: 0300 0000 da11 554e 4b4e 4f57 4e5f 5441  ......UNKNOWN_TA
+00000710: 534b 5f4e 414d 455a 0a4d 595f 5645 5253  SK_NAMEZ.MY_VERS
+00000720: 494f 4e5a 0a4d 595f 4c49 4345 4e53 455a  IONZ.MY_LICENSEZ
+00000730: 0a4e 4f5f 5052 4f4a 4543 545a 0c43 4f55  .NO_PROJECTZ.COU
+00000740: 4e54 4552 5f46 494c 455a 0e41 5247 554d  NTER_FILEZ.ARGUM
+00000750: 454e 5453 5f46 494c 45da 0b46 4f4e 545f  ENTS_FILE..FONT_
+00000760: 544f 5f55 5345 5a0a 4e4f 5f50 524f 4649  TO_USEZ.NO_PROFI
+00000770: 4c45 5a14 5459 5045 535f 4f46 5f43 4f4c  LEZ.TYPES_OF_COL
+00000780: 4f52 5f4e 414d 4553 5a0f 5459 5045 535f  OR_NAMESZ.TYPES_
+00000790: 4f46 5f43 4f4c 4f52 535a 0967 6574 4c6f  OF_COLORSZ.getLo
+000007a0: 6767 6572 da06 6c6f 6767 6572 da09 6465  gger..logger..de
+000007b0: 6275 675f 6f75 745a 0d44 4542 5547 5f50  bug_outZ.DEBUG_P
+000007c0: 524f 4752 414d a900 7219 0000 0072 1900  ROGRAM..r....r..
+000007d0: 0000 fa77 2f55 7365 7273 2f6d 696b 7275  ...w/Users/mikru
+000007e0: 6269 6e2f 4c69 6272 6172 792f 436c 6f75  bin/Library/Clou
+000007f0: 6453 746f 7261 6765 2f47 6f6f 676c 6544  dStorage/GoogleD
+00000800: 7269 7665 2d6d 696b 7275 6269 6e40 676d  rive-mikrubin@gm
+00000810: 6169 6c2e 636f 6d2f 4d79 2044 7269 7665  ail.com/My Drive
+00000820: 2f50 7974 686f 6e2f 6d61 7074 6173 6b65  /Python/maptaske
+00000830: 722f 6d61 7074 6173 6b65 722f 7372 632f  r/maptasker/src/
+00000840: 7379 7363 6f6e 7374 2e70 79da 083c 6d6f  sysconst.py..<mo
+00000850: 6475 6c65 3e01 0000 0073 ea00 0000 0c0d  dule>....s......
+00000860: 0c01 0403 0401 0401 0401 0401 0401 0c01  ................
+00000870: 0401 0207 0401 02ff 0402 02fe 0403 02fd  ................
+00000880: 0404 02fc 0405 02fb 0406 02fa 0407 02f9  ................
+00000890: 0408 02f8 0409 02f7 040a 02f6 040b 02f5  ................
+000008a0: 040c 02f4 040d 02f3 040e 02f2 040f 02f1  ................
+000008b0: 0410 02f0 0411 04ef 0412 02ee 0413 02ed  ................
+000008c0: 0414 02ec 0415 02eb 0416 02ea 0417 02e9  ................
+000008d0: 0418 02e8 0419 02e7 041a 02e6 041b 02e5  ................
+000008e0: 041c 02e4 041d 02e3 041e 02e2 041f 02e1  ................
+000008f0: 0420 02e0 0421 06df 0225 0401 02ff 0402  . ...!...%......
+00000900: 02fe 0403 02fd 0404 02fc 0405 02fb 0406  ................
+00000910: 02fa 0407 02f9 0408 02f8 0409 02f7 040a  ................
+00000920: 02f6 040b 02f5 040c 02f4 040d 02f3 040e  ................
+00000930: 02f2 040f 02f1 0410 02f0 0411 02ef 0412  ................
+00000940: 06ee 0a15 0401 0801                      ........
```

### Comparing `maptasker-1.3.1/maptasker/src/__pycache__/taskactn.cpython-310.pyc` & `maptasker-1.3.2/maptasker/src/__pycache__/taskactn.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Tue Mar 14 17:04:09 2023 UTC, .py size: 4921 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 7% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 09a9 1064 3913 0000  o..........d9...
+00000000: 6f0d 0d0a 0000 0000 c424 2b64 7f14 0000  o........$+d....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0012 0000 0040 0000 0073 a400 0000 6400  .....@...s....d.
 00000030: 6401 6c00 5a01 6400 6401 6c02 6d03 0200  d.l.Z.d.d.l.m...
 00000040: 0100 6d04 5a04 0100 6400 6402 6c05 6d06  ..m.Z...d.d.l.m.
 00000050: 5a06 0100 6400 6403 6c07 6d08 5a08 0100  Z...d.d.l.m.Z...
 00000060: 6400 6404 6c07 6d09 5a09 0100 6405 6501  d.d.l.m.Z...d.e.
 00000070: 6a0a 6406 650b 650c 1900 6407 650d 6408  j.d.e.e...d.e.d.
@@ -18,128 +18,132 @@
 00000110: da0b 6f75 7470 7574 5f6c 6973 74da 0c70  ..output_list..p
 00000120: 726f 6772 616d 5f61 7267 73da 096c 6973  rogram_args..lis
 00000130: 745f 7479 7065 da08 7468 655f 6974 656d  t_type..the_item
 00000140: da0b 7461 736b 735f 666f 756e 64da 0863  ..tasks_found..c
 00000150: 6f6c 6f72 6d61 70da 0961 6c6c 5f74 6173  olormap..all_tas
 00000160: 6b73 da06 7265 7475 726e 6308 0000 0000  ks..returnc.....
 00000170: 0000 0000 0000 000d 0000 0007 0000 0043  ...............C
-00000180: 0000 0073 c800 0000 7400 7c04 7600 730a  ...s....t.|.v.s.
-00000190: 7c02 6401 1900 6402 6b04 7262 6403 7c03  |.d...d.k.rbd.|.
+00000180: 0000 0073 f000 0000 7400 7c04 7600 730a  ...s....t.|.v.s.
+00000190: 7c02 6401 1900 6402 6b04 7276 6403 7c03  |.d...d.k.rvd.|.
 000001a0: 7600 7210 6404 6e04 7c04 a001 6405 a101  v.r.d.n.|...d...
 000001b0: 7d08 7402 7c08 8301 6406 6b04 7237 7c08  }.t.|...d.k.r7|.
 000001c0: 6406 1900 a001 6407 6406 a102 6402 1900  d.....d.d...d...
 000001d0: 7c08 6406 3c00 7403 a004 7c08 6406 1900  |.d.<.t...|.d...
 000001e0: 7c05 7c08 6406 1900 6701 6408 7c07 a105  |.|.d...g.d.|...
-000001f0: 5c02 7d00 7d09 7c00 7257 7403 a005 7c00  \.}.}.|.rWt...|.
-00000200: 7c06 7c02 a103 0400 7d0a 7255 7406 7c06  |.|.....}.rUt.|.
+000001f0: 5c02 7d00 7d09 7c00 726b 7403 a005 7c00  \.}.}.|.rkt...|.
+00000200: 7c06 7c02 a103 0400 7d0a 7269 7406 7c06  |.|.....}.rit.|.
 00000210: 7c02 7c01 6406 6408 8305 0100 6406 7d0b  |.|.d.d.....d.}.
 00000220: 7407 7c06 7c02 7c01 7c0b 7c0a 7c04 8306  t.|.|.|.|.|.|...
-00000230: 0100 6400 5300 6409 7d0c 7408 a009 7c0c  ..d.S.d.}.t...|.
-00000240: a101 0100 740a 7c0c 8301 0100 6400 5300  ....t.|.....d.S.
-00000250: 290a 4eda 1464 6973 706c 6179 5f64 6574  ).N..display_det
-00000260: 6169 6c5f 6c65 7665 6c72 0100 0000 7508  ail_levelr....u.
-00000270: 0000 00e2 8eaf 5461 736b 3ada 0178 7a09  ......Task:..xz.
-00000280: 5461 736b 2049 443a 20e9 0100 0000 fa01  Task ID: .......
-00000290: 20da 007a 1745 7272 6f72 3a20 4e6f 2054   ..z.Error: No T
-000002a0: 6173 6b20 666f 756e 6421 2121 290b 7204  ask found!!!).r.
-000002b0: 0000 00da 0573 706c 6974 da03 6c65 6eda  .....split..len.
-000002c0: 0574 6173 6b73 da0d 6765 745f 7461 736b  .tasks..get_task
-000002d0: 5f6e 616d 65da 0b67 6574 5f61 6374 696f  _name..get_actio
-000002e0: 6e73 7202 0000 00da 166f 7574 7075 745f  nsr......output_
-000002f0: 6c69 7374 5f6f 665f 6163 7469 6f6e 7372  list_of_actionsr
-00000300: 0300 0000 da05 6465 6275 67da 0570 7269  ......debug..pri
-00000310: 6e74 290d 7205 0000 0072 0600 0000 7207  nt).r....r....r.
-00000320: 0000 0072 0800 0000 7209 0000 0072 0a00  ...r....r....r..
-00000330: 0000 720b 0000 0072 0c00 0000 5a07 7465  ..r....r....Z.te
-00000340: 6d70 5f69 64da 046b 616b 61da 0561 6c69  mp_id..kaka..ali
-00000350: 7374 da0c 6163 7469 6f6e 5f63 6f75 6e74  st..action_count
-00000360: da09 6572 726f 725f 6d73 67a9 0072 1f00  ..error_msg..r..
-00000370: 0000 fa77 2f55 7365 7273 2f6d 696b 7275  ...w/Users/mikru
-00000380: 6269 6e2f 4c69 6272 6172 792f 436c 6f75  bin/Library/Clou
-00000390: 6453 746f 7261 6765 2f47 6f6f 676c 6544  dStorage/GoogleD
-000003a0: 7269 7665 2d6d 696b 7275 6269 6e40 676d  rive-mikrubin@gm
-000003b0: 6169 6c2e 636f 6d2f 4d79 2044 7269 7665  ail.com/My Drive
-000003c0: 2f50 7974 686f 6e2f 6d61 7074 6173 6b65  /Python/maptaske
-000003d0: 722f 6d61 7074 6173 6b65 722f 7372 632f  r/maptasker/src/
-000003e0: 7461 736b 6163 746e 2e70 79da 1b67 6574  taskactn.py..get
-000003f0: 5f74 6173 6b5f 6163 7469 6f6e 735f 616e  _task_actions_an
-00000400: 645f 6f75 7470 7574 1900 0000 732a 0000  d_output....s*..
-00000410: 0014 0b16 020c 0218 0104 0114 0108 ff04  ................
-00000420: 0412 0102 010a 0104 ff04 0302 010c 0104  ................
-00000430: ff04 0704 fd0a 0108 0104 0172 2100 0000  ...........r!...
-00000440: 721d 0000 0072 1c00 0000 6306 0000 0000  r....r....c.....
-00000450: 0000 0000 0000 0007 0000 000a 0000 0043  ...............C
-00000460: 0000 0073 ce00 0000 7c04 4400 5d5a 7d06  ...s....|.D.]Z}.
-00000470: 7c06 6401 7501 725c 6402 7c06 7600 7215  |.d.u.r\d.|.v.r.
-00000480: 7400 7c00 7c01 7c02 6403 7c06 8305 0100  t.|.|.|.d.|.....
-00000490: 6e2b 7c06 6401 6404 8502 1900 6405 6b02  n+|.d.d.....d.k.
-000004a0: 7229 7400 7c00 7c01 7c02 6403 6406 7c06  r)t.|.|.|.d.d.|.
-000004b0: 9b00 9d02 8305 0100 6e17 7400 7c00 7c01  ........n.t.|.|.
-000004c0: 7c02 6403 6406 7401 7c03 8301 a002 6403  |.d.d.t.|.....d.
-000004d0: a101 9b00 6407 7c06 9b00 9d04 8305 0100  ....d.|.........
-000004e0: 7c03 6408 3700 7d03 7c03 6403 6b02 7250  |.d.7.}.|.d.k.rP
-000004f0: 7c01 6409 1900 640a 6b02 7250 7403 7c05  |.d...d.k.rPt.|.
-00000500: 7600 7250 0100 6e0d 7c01 6409 1900 6408  v.rP..n.|.d...d.
-00000510: 6b02 725c 7403 7c05 7601 725c 0100 6e01  k.r\t.|.v.r\..n.
-00000520: 7102 7400 7c00 7c01 7c02 6404 640b 8305  q.t.|.|.|.d.d...
-00000530: 0100 6401 5300 290c 61d8 0100 006f 7574  ..d.S.).a....out
-00000540: 7075 7420 7468 6520 6c69 7374 206f 6620  put the list of 
-00000550: 5461 736b 2041 6374 696f 6e73 0a0a 2020  Task Actions..  
-00000560: 2020 5061 7261 6d65 7465 7273 3a0a 2020    Parameters:.  
-00000570: 2020 2020 2020 3a70 6172 616d 2063 6f6c        :param col
-00000580: 6f72 6d61 703a 2064 6963 7469 6f6e 6172  ormap: dictionar
-00000590: 7920 6f66 2063 6f6c 6f72 7320 746f 2075  y of colors to u
-000005a0: 7365 0a20 2020 2020 2020 203a 7061 7261  se.        :para
-000005b0: 6d20 7072 6f67 7261 6d5f 6172 6773 3a20  m program_args: 
-000005c0: 6469 6374 696f 6e61 7279 206f 6620 7072  dictionary of pr
-000005d0: 6f67 7261 6d20 7275 6e74 696d 6520 6172  ogram runtime ar
-000005e0: 6775 6d65 6e74 730a 2020 2020 2020 2020  guments.        
-000005f0: 3a70 6172 616d 206f 7574 7075 745f 6c69  :param output_li
-00000600: 7374 3a20 6c69 7374 2069 6e74 6f20 7768  st: list into wh
-00000610: 6963 6820 746f 2061 6464 2074 6865 206f  ich to add the o
-00000620: 7574 7075 7420 6c69 6e65 730a 2020 2020  utput lines.    
-00000630: 2020 2020 3a70 6172 616d 2061 6374 696f      :param actio
-00000640: 6e5f 636f 756e 743a 2063 6f75 6e74 206f  n_count: count o
-00000650: 6620 5461 736b 2061 6374 696f 6e73 0a20  f Task actions. 
-00000660: 2020 2020 2020 203a 7061 7261 6d20 616c         :param al
-00000670: 6973 743a 206c 6973 7420 6f66 2074 6173  ist: list of tas
-00000680: 6b20 6163 7469 6f6e 730a 2020 2020 2020  k actions.      
-00000690: 2020 3a70 6172 616d 2074 6865 5f69 7465    :param the_ite
-000006a0: 6d3a 2074 6865 2073 7065 6369 6669 6320  m: the specific 
-000006b0: 5461 736b 2773 2064 6574 6169 6c65 6420  Task's detailed 
-000006c0: 6c69 6e65 0a0a 2020 2020 5265 7475 726e  line..    Return
-000006d0: 733a 2074 6865 2063 6f75 6e74 206f 6620  s: the count of 
-000006e0: 7468 6520 6e75 6d62 6572 206f 6620 7469  the number of ti
-000006f0: 6d65 7320 7468 6520 7072 6f67 7261 6d20  mes the program 
-00000700: 6861 7320 6265 656e 2063 616c 6c65 640a  has been called.
-00000710: 0a20 2020 204e 7a09 4c61 6265 6c20 666f  .    Nz.Label fo
-00000720: 72e9 0200 0000 e903 0000 007a 032e 2e2e  r..........z....
-00000730: 7a08 4163 7469 6f6e 3a20 7211 0000 0072  z.Action: r....r
-00000740: 1000 0000 720e 0000 0072 0100 0000 7212  ....r....r....r.
-00000750: 0000 0029 0472 0200 0000 da03 7374 72da  ...).r......str.
-00000760: 057a 6669 6c6c 7204 0000 0029 0772 0b00  .zfillr....).r..
-00000770: 0000 7207 0000 0072 0600 0000 721d 0000  ..r....r....r...
-00000780: 0072 1c00 0000 7209 0000 005a 0774 6163  .r....r....Z.tac
-00000790: 7469 6f6e 721f 0000 0072 1f00 0000 7220  tionr....r....r 
-000007a0: 0000 0072 1800 0000 4100 0000 7330 0000  ...r....A...s0..
-000007b0: 0008 1508 0108 0112 0110 0118 0102 0202  ................
-000007c0: 0102 0102 0102 0118 0104 fb08 0708 020c  ................
-000007d0: 0108 0104 020c 0208 0104 0202 8010 0104  ................
-000007e0: 0172 1800 0000 2912 da15 786d 6c2e 6574  .r....)...xml.et
-000007f0: 7265 652e 456c 656d 656e 7454 7265 65da  ree.ElementTree.
-00000800: 0378 6d6c da13 6d61 7074 6173 6b65 722e  .xml..maptasker.
-00000810: 7372 632e 7461 736b 73da 0373 7263 7215  src.tasks..srcr.
-00000820: 0000 00da 156d 6170 7461 736b 6572 2e73  .....maptasker.s
-00000830: 7263 2e6f 7574 7075 746c 7202 0000 00da  rc.outputlr.....
-00000840: 166d 6170 7461 736b 6572 2e73 7263 2e73  .maptasker.src.s
-00000850: 7973 636f 6e73 7472 0300 0000 7204 0000  ysconstr....r...
-00000860: 00da 0565 7472 6565 da04 6c69 7374 7224  ...etree..listr$
-00000870: 0000 00da 0464 6963 7472 2100 0000 da03  .....dictr!.....
-00000880: 696e 74da 0b45 6c65 6d65 6e74 5472 6565  int..ElementTree
-00000890: 7218 0000 0072 1f00 0000 721f 0000 0072  r....r....r....r
-000008a0: 1f00 0000 7220 0000 00da 083c 6d6f 6475  ....r .....<modu
-000008b0: 6c65 3e01 0000 0073 4e00 0000 080d 1202  le>....sN.......
-000008c0: 0c01 0c01 0c01 0206 0401 02ff 0602 02fe  ................
-000008d0: 0203 02fd 0204 02fc 0205 02fb 0606 02fa  ................
-000008e0: 0207 02f9 0208 02f8 0209 0af7 0228 0201  .............(..
-000008f0: 02ff 0202 02fe 0203 02fd 0204 02fc 0205  ................
-00000900: 02fb 0606 02fa 0207 0ef9                 ..........
+00000230: 0100 6403 7c03 7600 7269 7406 7c06 7c02  ..d.|.v.rit.|.|.
+00000240: 7c01 6409 6408 8305 0100 7406 7c06 7c02  |.d.d.....t.|.|.
+00000250: 7c01 6409 6408 8305 0100 6400 5300 640a  |.d.d.....d.S.d.
+00000260: 7d0c 7408 a009 7c0c a101 0100 740a 7c0c  }.t...|.....t.|.
+00000270: 8301 0100 6400 5300 290b 4eda 1464 6973  ....d.S.).N..dis
+00000280: 706c 6179 5f64 6574 6169 6c5f 6c65 7665  play_detail_leve
+00000290: 6c72 0100 0000 7a0f 2623 3435 3b26 2334  lr....z.&#45;&#4
+000002a0: 353b 5461 736b 3ada 0178 7a09 5461 736b  5;Task:..xz.Task
+000002b0: 2049 443a 20e9 0100 0000 fa01 20da 00e9   ID: ....... ...
+000002c0: 0300 0000 7a17 4572 726f 723a 204e 6f20  ....z.Error: No 
+000002d0: 5461 736b 2066 6f75 6e64 2121 2129 0b72  Task found!!!).r
+000002e0: 0400 0000 da05 7370 6c69 74da 036c 656e  ......split..len
+000002f0: da05 7461 736b 73da 0d67 6574 5f74 6173  ..tasks..get_tas
+00000300: 6b5f 6e61 6d65 da0b 6765 745f 6163 7469  k_name..get_acti
+00000310: 6f6e 7372 0200 0000 da16 6f75 7470 7574  onsr......output
+00000320: 5f6c 6973 745f 6f66 5f61 6374 696f 6e73  _list_of_actions
+00000330: 7203 0000 00da 0564 6562 7567 da05 7072  r......debug..pr
+00000340: 696e 7429 0d72 0500 0000 7206 0000 0072  int).r....r....r
+00000350: 0700 0000 7208 0000 0072 0900 0000 720a  ....r....r....r.
+00000360: 0000 0072 0b00 0000 720c 0000 005a 0774  ...r....r....Z.t
+00000370: 656d 705f 6964 da04 6b61 6b61 da05 616c  emp_id..kaka..al
+00000380: 6973 74da 0c61 6374 696f 6e5f 636f 756e  ist..action_coun
+00000390: 74da 0965 7272 6f72 5f6d 7367 a900 7220  t..error_msg..r 
+000003a0: 0000 00fa 772f 5573 6572 732f 6d69 6b72  ....w/Users/mikr
+000003b0: 7562 696e 2f4c 6962 7261 7279 2f43 6c6f  ubin/Library/Clo
+000003c0: 7564 5374 6f72 6167 652f 476f 6f67 6c65  udStorage/Google
+000003d0: 4472 6976 652d 6d69 6b72 7562 696e 4067  Drive-mikrubin@g
+000003e0: 6d61 696c 2e63 6f6d 2f4d 7920 4472 6976  mail.com/My Driv
+000003f0: 652f 5079 7468 6f6e 2f6d 6170 7461 736b  e/Python/maptask
+00000400: 6572 2f6d 6170 7461 736b 6572 2f73 7263  er/maptasker/src
+00000410: 2f74 6173 6b61 6374 6e2e 7079 da1b 6765  /taskactn.py..ge
+00000420: 745f 7461 736b 5f61 6374 696f 6e73 5f61  t_task_actions_a
+00000430: 6e64 5f6f 7574 7075 7419 0000 0073 3000  nd_output....s0.
+00000440: 0000 140b 1603 0c02 1801 0401 1401 08ff  ................
+00000450: 0404 1201 0201 0a01 04ff 0403 0201 0c01  ................
+00000460: 04ff 0804 1001 1001 0405 04fd 0a01 0801  ................
+00000470: 0401 7222 0000 0072 1e00 0000 721d 0000  ..r"...r....r...
+00000480: 0063 0600 0000 0000 0000 0000 0000 0700  .c..............
+00000490: 0000 0a00 0000 4300 0000 73ce 0000 007c  ......C...s....|
+000004a0: 0444 005d 5a7d 067c 0664 0175 0172 5c64  .D.]Z}.|.d.u.r\d
+000004b0: 027c 0676 0072 1574 007c 007c 017c 0264  .|.v.r.t.|.|.|.d
+000004c0: 037c 0683 0501 006e 2b7c 0664 0164 0485  .|.....n+|.d.d..
+000004d0: 0219 0064 056b 0272 2974 007c 007c 017c  ...d.k.r)t.|.|.|
+000004e0: 0264 0364 067c 069b 009d 0283 0501 006e  .d.d.|.........n
+000004f0: 1774 007c 007c 017c 0264 0364 0674 017c  .t.|.|.|.d.d.t.|
+00000500: 0383 01a0 0264 03a1 019b 0064 077c 069b  .....d.....d.|..
+00000510: 009d 0483 0501 007c 0364 0837 007d 037c  .......|.d.7.}.|
+00000520: 0364 036b 0272 507c 0164 0919 0064 0a6b  .d.k.rP|.d...d.k
+00000530: 0272 5074 037c 0576 0072 5001 006e 0d7c  .rPt.|.v.rP..n.|
+00000540: 0164 0919 0064 086b 0272 5c74 037c 0576  .d...d.k.r\t.|.v
+00000550: 0172 5c01 006e 0171 0274 007c 007c 017c  .r\..n.q.t.|.|.|
+00000560: 0264 0464 0b83 0501 0064 0153 0029 0c61  .d.d.....d.S.).a
+00000570: d801 0000 6f75 7470 7574 2074 6865 206c  ....output the l
+00000580: 6973 7420 6f66 2054 6173 6b20 4163 7469  ist of Task Acti
+00000590: 6f6e 730a 0a20 2020 2050 6172 616d 6574  ons..    Paramet
+000005a0: 6572 733a 0a20 2020 2020 2020 203a 7061  ers:.        :pa
+000005b0: 7261 6d20 636f 6c6f 726d 6170 3a20 6469  ram colormap: di
+000005c0: 6374 696f 6e61 7279 206f 6620 636f 6c6f  ctionary of colo
+000005d0: 7273 2074 6f20 7573 650a 2020 2020 2020  rs to use.      
+000005e0: 2020 3a70 6172 616d 2070 726f 6772 616d    :param program
+000005f0: 5f61 7267 733a 2064 6963 7469 6f6e 6172  _args: dictionar
+00000600: 7920 6f66 2070 726f 6772 616d 2072 756e  y of program run
+00000610: 7469 6d65 2061 7267 756d 656e 7473 0a20  time arguments. 
+00000620: 2020 2020 2020 203a 7061 7261 6d20 6f75         :param ou
+00000630: 7470 7574 5f6c 6973 743a 206c 6973 7420  tput_list: list 
+00000640: 696e 746f 2077 6869 6368 2074 6f20 6164  into which to ad
+00000650: 6420 7468 6520 6f75 7470 7574 206c 696e  d the output lin
+00000660: 6573 0a20 2020 2020 2020 203a 7061 7261  es.        :para
+00000670: 6d20 6163 7469 6f6e 5f63 6f75 6e74 3a20  m action_count: 
+00000680: 636f 756e 7420 6f66 2054 6173 6b20 6163  count of Task ac
+00000690: 7469 6f6e 730a 2020 2020 2020 2020 3a70  tions.        :p
+000006a0: 6172 616d 2061 6c69 7374 3a20 6c69 7374  aram alist: list
+000006b0: 206f 6620 7461 736b 2061 6374 696f 6e73   of task actions
+000006c0: 0a20 2020 2020 2020 203a 7061 7261 6d20  .        :param 
+000006d0: 7468 655f 6974 656d 3a20 7468 6520 7370  the_item: the sp
+000006e0: 6563 6966 6963 2054 6173 6b27 7320 6465  ecific Task's de
+000006f0: 7461 696c 6564 206c 696e 650a 0a20 2020  tailed line..   
+00000700: 2052 6574 7572 6e73 3a20 7468 6520 636f   Returns: the co
+00000710: 756e 7420 6f66 2074 6865 206e 756d 6265  unt of the numbe
+00000720: 7220 6f66 2074 696d 6573 2074 6865 2070  r of times the p
+00000730: 726f 6772 616d 2068 6173 2062 6565 6e20  rogram has been 
+00000740: 6361 6c6c 6564 0a0a 2020 2020 4e7a 094c  called..    Nz.L
+00000750: 6162 656c 2066 6f72 e902 0000 0072 1300  abel for.....r..
+00000760: 0000 7a03 2e2e 2e7a 0841 6374 696f 6e3a  ..z....z.Action:
+00000770: 207a 0820 3c2f 7370 616e 3e72 1000 0000   z. </span>r....
+00000780: 720e 0000 0072 0100 0000 7212 0000 0029  r....r....r....)
+00000790: 0472 0200 0000 da03 7374 72da 057a 6669  .r......str..zfi
+000007a0: 6c6c 7204 0000 0029 0772 0b00 0000 7207  llr....).r....r.
+000007b0: 0000 0072 0600 0000 721e 0000 0072 1d00  ...r....r....r..
+000007c0: 0000 7209 0000 005a 0774 6163 7469 6f6e  ..r....Z.taction
+000007d0: 7220 0000 0072 2000 0000 7221 0000 0072  r ...r ...r!...r
+000007e0: 1900 0000 4600 0000 7330 0000 0008 1508  ....F...s0......
+000007f0: 0108 0112 0110 0118 0102 0202 0102 0102  ................
+00000800: 0102 0118 0104 fb08 0708 020c 0108 0104  ................
+00000810: 020c 0208 0104 0202 8010 0104 0172 1900  .............r..
+00000820: 0000 2912 da15 786d 6c2e 6574 7265 652e  ..)...xml.etree.
+00000830: 456c 656d 656e 7454 7265 65da 0378 6d6c  ElementTree..xml
+00000840: da13 6d61 7074 6173 6b65 722e 7372 632e  ..maptasker.src.
+00000850: 7461 736b 73da 0373 7263 7216 0000 00da  tasks..srcr.....
+00000860: 156d 6170 7461 736b 6572 2e73 7263 2e6f  .maptasker.src.o
+00000870: 7574 7075 746c 7202 0000 00da 166d 6170  utputlr......map
+00000880: 7461 736b 6572 2e73 7263 2e73 7973 636f  tasker.src.sysco
+00000890: 6e73 7472 0300 0000 7204 0000 00da 0565  nstr....r......e
+000008a0: 7472 6565 da04 6c69 7374 7224 0000 00da  tree..listr$....
+000008b0: 0464 6963 7472 2200 0000 da03 696e 74da  .dictr".....int.
+000008c0: 0b45 6c65 6d65 6e74 5472 6565 7219 0000  .ElementTreer...
+000008d0: 0072 2000 0000 7220 0000 0072 2000 0000  .r ...r ...r ...
+000008e0: 7221 0000 00da 083c 6d6f 6475 6c65 3e01  r!.....<module>.
+000008f0: 0000 0073 4e00 0000 080d 1202 0c01 0c01  ...sN...........
+00000900: 0c01 0206 0401 02ff 0602 02fe 0203 02fd  ................
+00000910: 0204 02fc 0205 02fb 0606 02fa 0207 02f9  ................
+00000920: 0208 02f8 0209 0af7 022d 0201 02ff 0202  .........-......
+00000930: 02fe 0203 02fd 0204 02fc 0205 02fb 0606  ................
+00000940: 02fa 0207 0ef9                           ......
```

### Comparing `maptasker-1.3.1/maptasker/src/__pycache__/taskerd.cpython-310.pyc` & `maptasker-1.3.2/maptasker/src/__pycache__/taskerd.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Tue Mar  7 19:12:33 2023 UTC, .py size: 3107 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 18% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 a18c 0764 230c 0000  o..........d#...
+00000000: 6f0d 0d0a 0000 0000 918f 1c64 230c 0000  o..........d#...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0003 0000 0040 0000 0073 3800 0000 6400  .....@...s8...d.
 00000030: 6401 6c00 6d01 0200 0100 6d02 5a03 0100  d.l.m.....m.Z...
 00000040: 6400 6402 6c04 6d05 5a05 0100 6403 6506  d.d.l.m.Z...d.e.
 00000050: 6602 6404 6405 8404 5a07 6406 6407 8400  f.d.d...Z.d.d...
 00000060: 5a08 6401 5300 2908 e900 0000 004e 2901  Z.d.S.)......N).
 00000070: da06 6c6f 6767 6572 da08 6973 5f73 6365  ..logger..is_sce
```

### Comparing `maptasker-1.3.1/maptasker/src/__pycache__/tasks.cpython-310.pyc` & `maptasker-1.3.2/maptasker/src/__pycache__/tasks.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Thu Mar 16 14:26:19 2023 UTC, .py size: 13873 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 19% similar despite different names*

```diff
@@ -1,10 +1,10 @@
-00000000: 6f0d 0d0a 0000 0000 0b27 1364 3136 0000  o........'.d16..
+00000000: 6f0d 0d0a 0000 0000 f445 2c64 7c3b 0000  o........E,d|;..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
-00000020: 001a 0000 0040 0000 0073 4c01 0000 6400  .....@...sL...d.
+00000020: 001c 0000 0040 0000 0073 9601 0000 6400  .....@...s....d.
 00000030: 6401 6c00 5a01 6400 6401 6c02 6d03 0200  d.l.Z.d.d.l.m...
 00000040: 0100 6d04 5a05 0100 6400 6401 6c06 6d03  ..m.Z...d.d.l.m.
 00000050: 0200 0100 6d07 5a08 0100 6400 6402 6c09  ....m.Z...d.d.l.
 00000060: 6d0a 5a0a 0100 6400 6403 6c0b 6d0c 5a0c  m.Z...d.d.l.m.Z.
 00000070: 0100 6400 6404 6c0d 6d0e 5a0e 0100 6400  ..d.d.l.m.Z...d.
 00000080: 6405 6c0f 6d10 5a10 0100 6400 6406 6c11  d.l.m.Z...d.d.l.
 00000090: 6d12 5a12 0100 6400 6407 6c11 6d13 5a13  m.Z...d.d.l.m.Z.
@@ -12,392 +12,486 @@
 000000b0: 6409 6c15 6d16 5a16 0100 640a 6501 6a17  d.l.m.Z...d.e.j.
 000000c0: 640b 6518 640c 6518 640d 6519 6608 640e  d.e.d.e.d.e.f.d.
 000000d0: 640f 8404 5a1a 6410 651b 6411 6519 6412  d...Z.d.e.d.e.d.
 000000e0: 6519 6413 651b 6414 6518 640d 651c 6501  e.d.e.d.e.d.e.e.
 000000f0: 6a17 651b 6602 1900 660c 6415 6416 8404  j.e.f...f.d.d...
 00000100: 5a1d 6410 651b 6417 6519 6418 6518 640d  Z.d.e.d.e.d.e.d.
 00000110: 651c 651b 6501 6a17 6602 1900 6608 6419  e.e.e.j.f...f.d.
-00000120: 641a 8404 5a1e 641b 641c 8400 5a1f 641d  d...Z.d.d...Z.d.
-00000130: 641e 8400 5a20 641f 6519 6420 651b 6421  d...Z d.e.d e.d!
-00000140: 6501 6a17 6422 6519 6423 651b 6424 651b  e.j.d"e.d#e.d$e.
-00000150: 6425 6519 6426 651b 640b 6518 6427 6518  d%e.d&e.d.e.d'e.
-00000160: 6428 6518 6429 6518 640d 6521 661a 642a  d(e.d)e.d.e!f.d*
-00000170: 642b 8404 5a22 6401 5300 292c e900 0000  d+..Z"d.S.),....
-00000180: 004e 2901 da0b 7461 675f 696e 5f74 7970  .N)...tag_in_typ
-00000190: 6529 01da 0b67 6574 5f6b 6964 5f61 7070  e)...get_kid_app
-000001a0: 2901 da0c 6765 745f 7072 696f 7269 7479  )...get_priority
-000001b0: 2901 da07 6765 745f 6964 7329 01da 1155  )...get_ids)...U
-000001c0: 4e4b 4e4f 574e 5f54 4153 4b5f 4e41 4d45  NKNOWN_TASK_NAME
-000001d0: 2901 da0a 4e4f 5f50 524f 4a45 4354 2901  )...NO_PROJECT).
-000001e0: da06 6c6f 6767 6572 2901 da0a 7368 656c  ..logger)...shel
-000001f0: 6c5f 736f 7274 da0c 6375 7272 656e 745f  l_sort..current_
-00000200: 7461 736b da08 636f 6c6f 726d 6170 da09  task..colormap..
-00000210: 7072 6f67 5f61 7267 73da 0672 6574 7572  prog_args..retur
-00000220: 6e63 0300 0000 0000 0000 0000 0000 0d00  nc..............
-00000230: 0000 0a00 0000 4300 0000 7352 0100 0067  ......C...sR...g
-00000240: 007d 037a 077c 00a0 0064 01a1 017d 0457  .}.z.|...d...}.W
-00000250: 006e 2304 0074 0179 2c01 007d 0501 007a  .n#..t.y,..}...z
-00000260: 1774 027c 0083 0101 0064 027d 0674 027c  .t.|.....d.}.t.|
-00000270: 0683 0101 0074 03a0 047c 06a1 0101 0067  .....t...|.....g
-00000280: 0057 0006 0059 0064 037d 057e 0553 0064  .W...Y.d.}.~.S.d
-00000290: 037d 057e 0577 0177 007c 0472 a764 047d  .}.~.w.w.|.r.d.}
-000002a0: 0764 057d 0874 057c 0483 0164 056b 0472  .d.}.t.|...d.k.r
-000002b0: 3f74 067c 0464 0664 0783 0301 007c 0444  ?t.|.d.d.....|.D
-000002c0: 005d 657d 097c 09a0 0764 08a1 017d 0a74  .]e}.|...d...}.t
-000002d0: 08a0 097c 0a7c 0964 067c 0164 097c 02a1  ...|.|.d.|.d.|..
-000002e0: 067d 0b74 03a0 0464 0a74 0a7c 096a 0b64  .}.t...d.t.|.j.d
-000002f0: 0b19 0083 0117 0064 0c17 007c 0a6a 0c17  .......d...|.j..
-00000300: 0064 0d17 007c 0b17 0064 0e17 0074 0a7c  .d...|...d...t.|
-00000310: 096a 0b83 0117 00a1 0101 0064 0f7c 0b76  .j.........d.|.v
-00000320: 0073 7a64 107c 0b76 0073 7a64 117c 0b76  .szd.|.v.szd.|.v
-00000330: 0072 887c 0864 1238 007d 0874 057c 0783  .r.|.d.8.}.t.|..
-00000340: 017d 0c7c 0764 137c 0c85 0219 007d 0774  .}.|.d.|.....}.t
-00000350: 08a0 0d7c 037c 0b7c 0a7c 087c 07a1 0501  ...|.|.|.|.|....
-00000360: 0064 147c 0b76 0073 9d64 107c 0b76 0073  .d.|.v.s.d.|.v.s
-00000370: 9d64 157c 0b76 0072 a67c 0864 1237 007d  .d.|.v.r.|.d.7.}
-00000380: 087c 079b 0064 169d 027d 0771 417c 0353  .|...d...}.qA|.S
-00000390: 0029 1761 1d01 0000 0a20 2020 2052 6574  .).a.....    Ret
-000003a0: 7572 6e20 6120 6c69 7374 206f 6620 5461  urn a list of Ta
-000003b0: 736b 2773 2061 6374 696f 6e73 2066 6f72  sk's actions for
-000003c0: 2074 6865 2067 6976 656e 2054 6173 6b0a   the given Task.
-000003d0: 2020 2020 2020 2020 3a70 6172 616d 2063          :param c
-000003e0: 7572 7265 6e74 5f74 6173 6b3a 2078 6d6c  urrent_task: xml
-000003f0: 2065 6c65 6d65 6e74 206f 6620 7468 6520   element of the 
-00000400: 5461 736b 2077 6520 6172 6520 6765 7474  Task we are gett
-00000410: 696e 6720 6163 7469 6f6e 7320 666f 720a  ing actions for.
-00000420: 2020 2020 2020 2020 3a70 6172 616d 2063          :param c
-00000430: 6f6c 6f72 6d61 703a 2063 6f6c 6f72 7320  olormap: colors 
-00000440: 746f 2075 7365 2069 6e20 6f75 7470 7574  to use in output
-00000450: 0a20 2020 2020 2020 203a 7061 7261 6d20  .        :param 
-00000460: 7072 6f67 5f61 7267 733a 2072 756e 7469  prog_args: runti
-00000470: 6d65 2061 7267 756d 656e 7473 0a20 2020  me arguments.   
-00000480: 2020 2020 203a 7265 7475 726e 3a20 6c69       :return: li
-00000490: 7374 206f 6620 5461 736b 2027 6163 7469  st of Task 'acti
-000004a0: 6f6e 2720 6f75 7470 7574 206c 696e 6573  on' output lines
-000004b0: 0a20 2020 20da 0641 6374 696f 6e7a 1945  .    ..Actionz.E
-000004c0: 7272 6f72 3a20 4e6f 2061 6374 696f 6e20  rror: No action 
-000004d0: 666f 756e 6421 2121 4eda 0072 0100 0000  found!!!N..r....
-000004e0: 5446 da04 636f 6465 da01 747a 0854 6173  TF..code..tz.Tas
-000004f0: 6b20 4944 3ada 0273 727a 0620 436f 6465  k ID:..srz. Code
-00000500: 3a7a 0b20 7461 736b 5f63 6f64 653a 7a0c  :z. task_code:z.
-00000510: 4163 7469 6f6e 2061 7474 723a 7a0d 3c2f  Action attr:z.</
-00000520: 7370 616e 3e45 6e64 2049 667a 0b3c 2f73  span>End Ifz.</s
-00000530: 7061 6e3e 456c 7365 7a0e 3c2f 7370 616e  pan>Elsez.</span
-00000540: 3e45 6e64 2046 6f72 e901 0000 00e9 1800  >End For........
-00000550: 0000 7a09 3c2f 7370 616e 3e49 667a 0a3c  ..z.</span>Ifz.<
-00000560: 2f73 7061 6e3e 466f 727a 1826 6e62 7370  /span>Forz.&nbsp
-00000570: 3b26 6e62 7370 3b26 6e62 7370 3b26 6e62  ;&nbsp;&nbsp;&nb
-00000580: 7370 3b29 0eda 0766 696e 6461 6c6c da09  sp;)...findall..
-00000590: 4578 6365 7074 696f 6eda 0570 7269 6e74  Exception..print
-000005a0: 7208 0000 00da 0564 6562 7567 da03 6c65  r......debug..le
-000005b0: 6e72 0900 0000 da04 6669 6e64 da0f 6163  nr......find..ac
-000005c0: 7469 6f6e 5f65 7661 6c75 6174 65da 0f67  tion_evaluate..g
-000005d0: 6574 5f61 6374 696f 6e5f 636f 6465 da03  et_action_code..
-000005e0: 7374 72da 0661 7474 7269 62da 0474 6578  str..attrib..tex
-000005f0: 74da 0c62 7569 6c64 5f61 6374 696f 6e29  t..build_action)
-00000600: 0d72 0a00 0000 720b 0000 0072 0c00 0000  .r....r....r....
-00000610: 5a08 7461 736b 6c69 7374 5a0c 7461 736b  Z.tasklistZ.task
-00000620: 5f61 6374 696f 6e73 da01 65da 0965 7272  _actions..e..err
-00000630: 6f72 5f6d 7367 5a12 696e 6465 6e74 6174  or_msgZ.indentat
-00000640: 696f 6e5f 616d 6f75 6e74 5a0b 696e 6465  ion_amountZ.inde
-00000650: 6e74 6174 696f 6eda 0661 6374 696f 6eda  ntation..action.
-00000660: 0563 6869 6c64 5a09 7461 736b 5f63 6f64  .childZ.task_cod
-00000670: 655a 0d6c 656e 6774 685f 696e 6465 6e74  eZ.length_indent
-00000680: a900 7225 0000 00fa 742f 5573 6572 732f  ..r%....t/Users/
-00000690: 6d69 6b72 7562 696e 2f4c 6962 7261 7279  mikrubin/Library
-000006a0: 2f43 6c6f 7564 5374 6f72 6167 652f 476f  /CloudStorage/Go
-000006b0: 6f67 6c65 4472 6976 652d 6d69 6b72 7562  ogleDrive-mikrub
-000006c0: 696e 4067 6d61 696c 2e63 6f6d 2f4d 7920  in@gmail.com/My 
-000006d0: 4472 6976 652f 5079 7468 6f6e 2f6d 6170  Drive/Python/map
-000006e0: 7461 736b 6572 2f6d 6170 7461 736b 6572  tasker/maptasker
-000006f0: 2f73 7263 2f74 6173 6b73 2e70 79da 0b67  /src/tasks.py..g
-00000700: 6574 5f61 6374 696f 6e73 2100 0000 736c  et_actions!...sl
-00000710: 0000 0004 0802 020e 010e 0108 0104 0108  ................
-00000720: 010a 0110 0108 8002 fb04 0604 0104 010c  ................
-00000730: 030c 0108 020a 0104 030c 0104 ff04 0302  ................
-00000740: 010c 0102 ff02 0202 fe04 0302 fd02 0402  ................
-00000750: fc02 0502 fb02 0602 fa08 0702 f904 ff08  ................
-00000760: 0c08 0108 0108 0208 010c 0104 010a 0104  ................
-00000770: ff08 0408 0108 0108 020a 0102 8004 0272  ...............r
-00000780: 2700 0000 da0b 7468 655f 7461 736b 5f69  '.....the_task_i
-00000790: 64da 1a74 6173 6b73 5f74 6861 745f 6861  d..tasks_that_ha
-000007a0: 7665 5f62 6565 6e5f 666f 756e 64da 1174  ve_been_found..t
-000007b0: 6173 6b5f 6f75 7470 7574 5f6c 696e 6573  ask_output_lines
-000007c0: da09 7461 736b 5f74 7970 65da 0961 6c6c  ..task_type..all
-000007d0: 5f74 6173 6b73 6305 0000 0000 0000 0000  _tasksc.........
-000007e0: 0000 0009 0000 000a 0000 0043 0000 0073  ...........C...s
-000007f0: fa00 0000 7c00 a000 a100 7275 7c04 7c00  ....|.....ru|.|.
-00000800: 1900 7d05 7c01 a001 7c00 a101 0100 6401  ..}.|...|.....d.
-00000810: 7c00 9b00 9d02 7d06 7a29 7c05 a002 6402  |.....}.z)|...d.
-00000820: a101 6a03 7d07 7c03 6403 6b02 7228 7c02  ..j.}.|.d.k.r(|.
-00000830: a001 7c07 9b00 6404 7c06 9b00 9d03 a101  ..|...d.|.......
-00000840: 0100 6e0f 7c02 a001 7c07 9b00 6405 7c06  ..n.|...|...d.|.
-00000850: 9b00 9d03 a101 0100 5700 7c05 7c07 6602  ........W.|.|.f.
-00000860: 5300 5700 7c05 7c07 6602 5300 0400 7404  S.W.|.|.f.S...t.
-00000870: 7974 0100 7d08 0100 7a2d 7405 7d07 7c03  yt..}...z-t.}.|.
-00000880: 6403 6b02 7254 7c02 a001 7405 9b00 6404  d.k.rT|...t...d.
-00000890: 7c06 9b00 9d03 a101 0100 6e13 7c02 a001  |.........n.|...
-000008a0: 7405 9b00 6405 7c06 9b00 9d03 a101 0100  t...d.|.........
-000008b0: 5700 5900 6406 7d08 7e08 7c05 7c07 6602  W.Y.d.}.~.|.|.f.
-000008c0: 5300 5700 5900 6406 7d08 7e08 7c05 7c07  S.W.Y.d.}.~.|.|.
-000008d0: 6602 5300 6406 7d08 7e08 7701 7700 6406  f.S.d.}.~.w.w.d.
-000008e0: 7d05 6407 7d07 7c05 7c07 6602 5300 2908  }.d.}.|.|.f.S.).
-000008f0: 6178 0100 000a 2020 2020 4765 7420 7468  ax....    Get th
-00000900: 6520 6e61 6d65 206f 6620 7468 6520 7461  e name of the ta
-00000910: 736b 2067 6976 656e 2074 6865 2054 6173  sk given the Tas
-00000920: 6b20 4944 0a20 2020 2020 2020 203a 7061  k ID.        :pa
-00000930: 7261 6d20 7468 655f 7461 736b 5f69 643a  ram the_task_id:
-00000940: 2074 6865 2054 6173 6b27 7320 4944 2028   the Task's ID (
-00000950: 652e 672e 2027 3437 2729 0a20 2020 2020  e.g. '47').     
-00000960: 2020 203a 7061 7261 6d20 7461 736b 735f     :param tasks_
-00000970: 7468 6174 5f68 6176 655f 6265 656e 5f66  that_have_been_f
-00000980: 6f75 6e64 3a20 6c69 7374 206f 6620 5461  ound: list of Ta
-00000990: 736b 7320 666f 756e 6420 736f 2066 6172  sks found so far
-000009a0: 0a20 2020 2020 2020 203a 7061 7261 6d20  .        :param 
-000009b0: 7461 736b 5f6f 7574 7075 745f 6c69 6e65  task_output_line
-000009c0: 733a 206c 6973 7420 6f66 2054 6173 6b73  s: list of Tasks
-000009d0: 0a20 2020 2020 2020 203a 7061 7261 6d20  .        :param 
-000009e0: 7461 736b 5f74 7970 653a 2054 7970 6520  task_type: Type 
-000009f0: 6f66 2054 6173 6b20 2845 6e74 7279 2c20  of Task (Entry, 
-00000a00: 4578 6974 2c20 5363 656e 6529 0a20 2020  Exit, Scene).   
-00000a10: 2020 2020 203a 7061 7261 6d20 616c 6c5f       :param all_
-00000a20: 7461 736b 733a 2061 6c6c 2054 6173 6b73  tasks: all Tasks
-00000a30: 2069 6e20 786d 6c0a 2020 2020 2020 2020   in xml.        
-00000a40: 3a72 6574 7572 6e3a 2054 6173 6b27 7320  :return: Task's 
-00000a50: 786d 6c20 656c 656d 656e 742c 2054 6173  xml element, Tas
-00000a60: 6b27 7320 6e61 6d65 0a20 2020 207a 1526  k's name.    z.&
-00000a70: 6e62 7370 3b26 6e62 7370 3b54 6173 6b20  nbsp;&nbsp;Task 
-00000a80: 4944 3a20 da03 6e6d 65da 0445 7869 747a  ID: ..nme..Exitz
-00000a90: 2526 6e62 7370 3b26 6e62 7370 3b26 6e62  %&nbsp;&nbsp;&nb
-00000aa0: 7370 3b26 6e62 7370 3b3c 3c3c 2045 7869  sp;&nbsp;<<< Exi
-00000ab0: 7420 5461 736b 7a26 266e 6273 703b 266e  t Taskz&&nbsp;&n
-00000ac0: 6273 703b 266e 6273 703b 266e 6273 703b  bsp;&nbsp;&nbsp;
-00000ad0: 3c3c 3c20 456e 7472 7920 5461 736b 4e72  <<< Entry TaskNr
-00000ae0: 0f00 0000 2906 da07 6973 6469 6769 74da  ....)...isdigit.
-00000af0: 0661 7070 656e 6472 1a00 0000 721f 0000  .appendr....r...
-00000b00: 0072 1600 0000 7206 0000 0029 0972 2800  .r....r....).r(.
-00000b10: 0000 7229 0000 0072 2a00 0000 722b 0000  ..r)...r*...r+..
-00000b20: 0072 2c00 0000 da04 7461 736b da05 6578  .r,.....task..ex
-00000b30: 7472 615a 0974 6173 6b5f 6e61 6d65 7221  traZ.task_namer!
-00000b40: 0000 0072 2500 0000 7225 0000 0072 2600  ...r%...r%...r&.
-00000b50: 0000 da0d 6765 745f 7461 736b 5f6e 616d  ....get_task_nam
-00000b60: 6567 0000 0073 4200 0000 0810 0801 0a01  eg...sB.........
-00000b70: 0a01 0201 0c01 0801 0401 0c01 06ff 0405  ................
-00000b80: 0c01 06ff 0812 02e9 0817 0ef1 0401 0801  ................
-00000b90: 0401 0c01 06ff 0405 0c01 0eff 0807 0af4  ................
-00000ba0: 080c 0880 02f1 040c 0401 0802 7233 0000  ............r3..
-00000bb0: 00da 1670 726f 6a65 6374 735f 7769 7468  ...projects_with
-00000bc0: 5f6e 6f5f 7461 736b 73da 0c61 6c6c 5f70  _no_tasks..all_p
-00000bd0: 726f 6a65 6374 7363 0300 0000 0000 0000  rojectsc........
-00000be0: 0000 0000 0600 0000 0900 0000 4300 0000  ............C...
-00000bf0: 7356 0000 0074 007d 0364 007d 047c 0264  sV...t.}.d.}.|.d
-00000c00: 0075 0172 277c 0244 005d 1c7d 047c 04a0  .u.r'|.D.].}.|..
-00000c10: 0164 01a1 016a 027d 0374 0364 0269 0069  .d...j.}.t.d.i.i
-00000c20: 0067 007c 047c 037c 0183 077d 057c 007c  .g.|.|.|...}.|.|
-00000c30: 0576 0072 267c 037c 0466 0202 0001 0053  .v.r&|.|.f.....S
-00000c40: 0071 0a7c 037c 0466 0253 0029 034e da04  .q.|.|.f.S.).N..
-00000c50: 6e61 6d65 4629 0472 0700 0000 721a 0000  nameF).r....r...
-00000c60: 0072 1f00 0000 7205 0000 0029 0672 2800  .r....r....).r(.
-00000c70: 0000 7234 0000 0072 3500 0000 5a09 7072  ..r4...r5...Z.pr
-00000c80: 6f6a 5f6e 616d 65da 0770 726f 6a65 6374  oj_name..project
-00000c90: da08 7461 736b 5f69 6473 7225 0000 0072  ..task_idsr%...r
-00000ca0: 2500 0000 7226 0000 00da 1967 6574 5f70  %...r&.....get_p
-00000cb0: 726f 6a65 6374 5f66 6f72 5f73 6f6c 6f5f  roject_for_solo_
-00000cc0: 7461 736b 9b00 0000 7318 0000 0004 0304  task....s.......
-00000cd0: 0108 0108 020c 0102 010e 0104 ff08 030c  ................
-00000ce0: 0102 ff08 0272 3900 0000 6302 0000 0000  .....r9...c.....
-00000cf0: 0000 0000 0000 0005 0000 0006 0000 0043  ...............C
-00000d00: 0000 0073 6200 0000 7c01 4400 5d2c 7d02  ...sb...|.D.],}.
-00000d10: 7c01 7c02 1900 4400 5d25 7d03 7400 7c03  |.|...D.]%}.t.|.
-00000d20: 6a01 6401 8302 722d 7c03 4400 5d1a 7d04  j.d...r-|.D.].}.
-00000d30: 7400 7c04 6a01 6402 8302 7225 7c00 7c04  t.|.j.d...r%|.|.
-00000d40: 6a02 6b02 7224 0100 0100 0100 6401 5300  j.k.r$......d.S.
-00000d50: 7112 7c03 6a01 6403 6b02 722c 0100 6e01  q.|.j.d.k.r,..n.
-00000d60: 7112 7108 7102 6402 5300 2904 4e54 46da  q.q.q.d.S.).NTF.
-00000d70: 0353 7472 2903 7202 0000 00da 0374 6167  .Str).r......tag
-00000d80: 721f 0000 0029 0572 2800 0000 da0a 616c  r....).r(.....al
-00000d90: 6c5f 7363 656e 6573 5a05 7363 656e 6572  l_scenesZ.scener
-00000da0: 2400 0000 5a08 7375 6263 6869 6c64 7225  $...Z.subchildr%
-00000db0: 0000 0072 2500 0000 7226 0000 00da 0d74  ...r%...r&.....t
-00000dc0: 6173 6b5f 696e 5f73 6365 6e65 af00 0000  ask_in_scene....
-00000dd0: 731c 0000 0008 010c 010c 0108 010c 010a  s...............
-00000de0: 020a 0202 fe0a 0304 0102 0202 8002 f504  ................
-00000df0: 0c72 3d00 0000 630c 0000 0000 0000 0000  .r=...c.........
-00000e00: 0000 0011 0000 000a 0000 0043 0000 0073  ...........C...s
-00000e10: 1c01 0000 6401 6402 6c00 6d01 7d0c 0100  ....d.d.l.m.}...
-00000e20: 7402 a003 6403 7c0b 6404 1900 9b00 6405  t...d.|.d.....d.
-00000e30: 7c00 9b00 9d04 a101 0100 7c0b 6404 1900  |.........|.d...
-00000e40: 7c00 6b02 7256 6406 7c05 6407 3c00 7404  |.k.rVd.|.d.<.t.
-00000e50: a005 6406 7c01 7c02 7c03 7c04 7c0a 7c0b  ..d.|.|.|.|.|.|.
-00000e60: a107 0100 6700 7d0d 7406 7c06 8301 6408  ....g.}.t.|...d.
-00000e70: 6b04 7247 7406 7c00 8301 7d0e 7c06 4400  k.rGt.|...}.|.D.
-00000e80: 5d0f 7d0f 7c00 7c0f 6400 7c0e 8502 1900  ].}.|.|.d.|.....
-00000e90: 6b02 7245 7c0f 6701 7d0d 0100 6e01 7136  k.rE|.g.}...n.q6
-00000ea0: 6e02 7c06 7d0d 7c0c 6409 7c01 7c0d 7c07  n.|.}.|.d.|.|.|.
-00000eb0: 7c08 7c0b 7c0a 7c09 8308 0100 6400 5300  |.|.|.|.....d.S.
-00000ec0: 7406 7c06 8301 6408 6b04 728a 7c06 4400  t.|...d.k.r.|.D.
-00000ed0: 5d2d 7d10 7c0b 6404 1900 7c10 7600 7289  ]-}.|.d...|.v.r.
-00000ee0: 7404 a007 7c0a 7c0b 7c01 6408 640a a105  t...|.|.|.d.d...
-00000ef0: 0100 7c10 6701 7d06 7c0c 6409 7c01 7c06  ..|.g.}.|.d.|.|.
-00000f00: 7c07 7c08 7c0b 7c0a 7c09 8308 0100 7404  |.|.|.|.|.....t.
-00000f10: a007 7c0a 7c0b 7c01 640b 640a a105 0100  ..|.|.|.d.d.....
-00000f20: 0100 6400 5300 715e 6400 5300 6400 5300  ..d.S.q^d.S.d.S.
-00000f30: 290c 4e72 0100 0000 a901 da0c 7072 6f63  ).Nr........proc
-00000f40: 6573 735f 6c69 7374 7a17 7461 736b 7320  ess_listz.tasks 
-00000f50: 7369 6e67 6c65 2074 6173 6b20 6e61 6d65  single task name
-00000f60: 3ada 1073 696e 676c 655f 7461 736b 5f6e  :..single_task_n
-00000f70: 616d 657a 0f20 6f75 7220 5461 736b 206e  amez. our Task n
-00000f80: 616d 653a 54da 1173 696e 676c 655f 7461  ame:T..single_ta
-00000f90: 736b 5f66 6f75 6e64 7213 0000 00fa 0554  sk_foundr......T
-00000fa0: 6173 6b3a 720f 0000 00e9 0300 0000 2908  ask:r.........).
-00000fb0: da16 6d61 7074 6173 6b65 722e 7372 632e  ..maptasker.src.
-00000fc0: 7072 6f63 6c69 7374 723f 0000 0072 0800  proclistr?...r..
-00000fd0: 0000 7218 0000 00da 0c62 7569 6c64 5f6f  ..r......build_o
-00000fe0: 7574 7075 74da 1272 6566 7265 7368 5f6f  utput..refresh_o
-00000ff0: 7572 5f6f 7574 7075 7472 1900 0000 da09  ur_outputr......
-00001000: 6d79 5f6f 7574 7075 7429 11da 0d6f 7572  my_output)...our
-00001010: 5f74 6173 6b5f 6e61 6d65 da0b 6f75 7470  _task_name..outp
-00001020: 7574 5f6c 6973 74da 0c70 726f 6a65 6374  ut_list..project
-00001030: 5f6e 616d 65da 0c70 726f 6669 6c65 5f6e  _name..profile_n
-00001040: 616d 65da 0768 6561 6469 6e67 da0b 666f  ame..heading..fo
-00001050: 756e 645f 6974 656d 73da 0974 6173 6b5f  und_items..task_
-00001060: 6c69 7374 da10 6f75 725f 7461 736b 5f65  list..our_task_e
-00001070: 6c65 6d65 6e74 da13 6c69 7374 5f6f 665f  lement..list_of_
-00001080: 666f 756e 645f 7461 736b 73da 1061 6c6c  found_tasks..all
-00001090: 5f74 6173 6b65 725f 6974 656d 7372 0b00  _tasker_itemsr..
-000010a0: 0000 da0c 7072 6f67 7261 6d5f 6172 6773  ....program_args
-000010b0: 723f 0000 005a 1374 656d 706f 7261 7279  r?...Z.temporary
-000010c0: 5f74 6173 6b5f 6c69 7374 5a14 7468 655f  _task_listZ.the_
-000010d0: 7461 736b 5f6e 616d 655f 6c65 6e67 7468  task_name_length
-000010e0: da04 6974 656d 5a09 7461 736b 5f69 7465  ..itemZ.task_ite
-000010f0: 6d72 2500 0000 7225 0000 0072 2600 0000  mr%...r%...r&...
-00001100: da0e 646f 5f73 696e 676c 655f 7461 736b  ..do_single_task
-00001110: c300 0000 737a 0000 000c 0f04 020c 0102  ....sz..........
-00001120: 0104 ff04 ff0c 0408 0204 0202 0102 0102  ................
-00001130: 0102 0102 0102 0102 0104 f904 0b0c 0108  ................
-00001140: 0108 0110 0106 0104 0102 fe02 8004 0402  ................
-00001150: 0202 0102 0102 0102 0102 0102 0102 0102  ................
-00001160: 0108 f80c 0b08 020c 0104 010a 0104 ff06  ................
-00001170: 0302 0102 0102 0102 0102 0102 0102 0102  ................
-00001180: 0102 0104 f804 0a0a 0104 ff06 0302 ee04  ................
-00001190: fd04 0272 5400 0000 7249 0000 0072 4800  ...rT...rI...rH.
-000011a0: 0000 724f 0000 0072 4e00 0000 724a 0000  ..rO...rN...rJ..
-000011b0: 0072 4b00 0000 7250 0000 0072 4c00 0000  .rK...rP...rL...
-000011c0: 7252 0000 0072 5100 0000 724d 0000 0063  rR...rQ...rM...c
-000011d0: 0c00 0000 0000 0000 0000 0000 0f00 0000  ................
-000011e0: 0d00 0000 4300 0000 73d2 0000 0064 0164  ....C...s....d.d
-000011f0: 026c 006d 017d 0c01 007c 0964 0319 0064  .l.m.}...|.d...d
-00001200: 046b 0272 2f74 027c 0283 0104 007d 0d72  .k.r/t.|.....}.r
-00001210: 1d7c 0364 0119 009b 0064 057c 0d9b 009d  .|.d.....d.|....
-00001220: 037c 0364 013c 0074 037c 0264 0683 0204  .|.d.<.t.|.d....
-00001230: 007d 0e72 2f7c 0364 0119 009b 0064 057c  .}.r/|.d.....d.|
-00001240: 0e9b 009d 037c 0364 013c 007c 0164 076b  .....|.d.<.|.d.k
-00001250: 0372 487c 0964 0819 0072 4874 047c 017c  .rH|.d...rHt.|.|
-00001260: 007c 047c 057c 077c 0b7c 037c 027c 067c  .|.|.|.|.|.|.|.|
-00001270: 0a7c 087c 0983 0c01 0064 0953 007c 0372  .|.|.....d.S.|.r
-00001280: 6774 05a0 067c 087c 097c 0064 0a64 07a1  gt...|.|.|.d.d..
-00001290: 0501 007c 0c64 0b7c 007c 037c 027c 067c  ...|.d.|.|.|.|.|
-000012a0: 097c 087c 0a83 0801 0074 05a0 067c 087c  .|.|.....t...|.|
-000012b0: 097c 0064 0464 07a1 0501 0064 0653 0029  .|.d.d.....d.S.)
-000012c0: 0c61 2003 0000 0a20 2020 2057 6520 6861  .a ....    We ha
-000012d0: 7665 2061 2073 696e 676c 6520 5461 736b  ve a single Task
-000012e0: 206f 7220 6120 6c69 7374 206f 6620 5461   or a list of Ta
-000012f0: 736b 732e 2020 4f75 7470 7574 2069 742f  sks.  Output it/
-00001300: 7468 656d 2e0a 2020 2020 2020 2020 3a70  them..        :p
-00001310: 6172 616d 206f 7574 7075 745f 6c69 7374  aram output_list
-00001320: 3a20 6c69 7374 206f 6620 6f75 7470 7574  : list of output
-00001330: 206c 696e 6573 2067 656e 6572 6174 6564   lines generated
-00001340: 2074 6875 7320 6661 720a 2020 2020 2020   thus far.      
-00001350: 2020 3a70 6172 616d 206f 7572 5f74 6173    :param our_tas
-00001360: 6b5f 6e61 6d65 3a20 6e61 6d65 206f 6620  k_name: name of 
-00001370: 5461 736b 0a20 2020 2020 2020 203a 7061  Task.        :pa
-00001380: 7261 6d20 6f75 725f 7461 736b 5f65 6c65  ram our_task_ele
-00001390: 6d65 6e74 3a20 5461 736b 2078 6d6c 2065  ment: Task xml e
-000013a0: 6c65 6d65 6e74 0a20 2020 2020 2020 203a  lement.        :
-000013b0: 7061 7261 6d20 7461 736b 5f6c 6973 743a  param task_list:
-000013c0: 2054 6173 6b20 6c69 7374 0a20 2020 2020   Task list.     
-000013d0: 2020 203a 7061 7261 6d20 7072 6f6a 6563     :param projec
-000013e0: 745f 6e61 6d65 3a20 6e61 6d65 206f 6620  t_name: name of 
-000013f0: 6375 7272 656e 7420 5072 6f6a 6563 740a  current Project.
-00001400: 2020 2020 2020 2020 3a70 6172 616d 2070          :param p
-00001410: 726f 6669 6c65 5f6e 616d 653a 206e 616d  rofile_name: nam
-00001420: 6520 6f66 2063 7572 7265 6e74 2050 726f  e of current Pro
-00001430: 6669 6c65 0a20 2020 2020 2020 203a 7061  file.        :pa
-00001440: 7261 6d20 6c69 7374 5f6f 665f 666f 756e  ram list_of_foun
-00001450: 645f 7461 736b 733a 206c 6973 7420 6f66  d_tasks: list of
-00001460: 2054 6173 6b73 2066 6f75 6e64 2073 6f20   Tasks found so 
-00001470: 6661 720a 2020 2020 2020 2020 3a70 6172  far.        :par
-00001480: 616d 2068 6561 6469 6e67 3a20 6375 7272  am heading: curr
-00001490: 656e 7420 6865 6164 696e 670a 2020 2020  ent heading.    
-000014a0: 2020 2020 3a70 6172 616d 2063 6f6c 6f72      :param color
-000014b0: 6d61 703a 2063 6f6c 6f72 7320 746f 2075  map: colors to u
-000014c0: 7365 2069 6e20 6f75 7470 7574 0a20 2020  se in output.   
-000014d0: 2020 2020 203a 7061 7261 6d20 7072 6f67       :param prog
-000014e0: 7261 6d5f 6172 6773 3a20 7275 6e74 696d  ram_args: runtim
-000014f0: 6520 6172 6775 6d65 6e74 730a 2020 2020  e arguments.    
-00001500: 2020 2020 3a70 6172 616d 2061 6c6c 5f74      :param all_t
-00001510: 6173 6b65 725f 6974 656d 733a 2061 6c6c  asker_items: all
-00001520: 2050 726f 6a65 6374 732f 5072 6f66 696c   Projects/Profil
-00001530: 6573 2f54 6173 6b73 2f53 6365 6e65 730a  es/Tasks/Scenes.
-00001540: 2020 2020 2020 2020 3a70 6172 616d 2066          :param f
-00001550: 6f75 6e64 5f69 7465 6d73 3a20 7369 6e67  ound_items: sing
-00001560: 6c65 2050 726f 6a65 6374 2f50 726f 6669  le Project/Profi
-00001570: 6c65 2f54 6173 6b20 746f 2073 6561 7263  le/Task to searc
-00001580: 6820 666f 720a 2020 2020 2020 2020 3a72  h for.        :r
-00001590: 6574 7572 6e3a 2054 7275 6520 6966 2077  eturn: True if w
-000015a0: 6520 6172 6520 7365 6172 6368 696e 6720  e are searching 
-000015b0: 666f 7220 6120 7369 6e67 6c65 2054 6173  for a single Tas
-000015c0: 6b20 616e 6420 666f 756e 6420 6974 2e20  k and found it. 
-000015d0: 204f 7468 6572 7769 7365 2c20 4661 6c73   Otherwise, Fals
-000015e0: 650a 2020 2020 7201 0000 0072 3e00 0000  e.    r....r>...
-000015f0: da14 6469 7370 6c61 795f 6465 7461 696c  ..display_detail
-00001600: 5f6c 6576 656c 7243 0000 00fa 0120 4672  _levelrC..... Fr
-00001610: 0f00 0000 7240 0000 0054 7213 0000 0072  ....r@...Tr....r
-00001620: 4200 0000 2907 7244 0000 0072 3f00 0000  B...).rD...r?...
-00001630: 7203 0000 0072 0400 0000 7254 0000 0072  r....r....rT...r
-00001640: 4500 0000 7247 0000 0029 0f72 4900 0000  E...rG...).rI...
-00001650: 7248 0000 0072 4f00 0000 724e 0000 0072  rH...rO...rN...r
-00001660: 4a00 0000 724b 0000 0072 5000 0000 724c  J...rK...rP...rL
-00001670: 0000 0072 0b00 0000 7252 0000 0072 5100  ...r....rR...rQ.
-00001680: 0000 724d 0000 0072 3f00 0000 da0c 6b69  ..rM...r?.....ki
-00001690: 645f 6170 705f 696e 666f da08 7072 696f  d_app_info..prio
-000016a0: 7269 7479 7225 0000 0072 2500 0000 7226  rityr%...r%...r&
-000016b0: 0000 00da 0b6f 7574 7075 745f 7461 736b  .....output_task
-000016c0: 1701 0000 734c 0000 000c 1f0c 030c 0116  ....sL..........
-000016d0: 010e 0116 0110 0402 0202 0102 0102 0102  ................
-000016e0: 0102 0102 0102 0102 0102 0102 0102 0102  ................
-000016f0: 0104 f404 0f04 0112 0202 0202 0102 0102  ................
-00001700: 0102 0102 0102 0102 0102 0104 f804 0a0a  ................
-00001710: 0104 ff04 0472 5900 0000 2923 da15 786d  .....rY...)#..xm
-00001720: 6c2e 6574 7265 652e 456c 656d 656e 7454  l.etree.ElementT
-00001730: 7265 65da 0378 6d6c da15 6d61 7074 6173  ree..xml..maptas
-00001740: 6b65 722e 7372 632e 6163 7469 6f6e 65da  ker.src.actione.
-00001750: 0373 7263 da07 6163 7469 6f6e 6572 1b00  .src..actioner..
-00001760: 0000 da15 6d61 7074 6173 6b65 722e 7372  ....maptasker.sr
-00001770: 632e 6f75 7470 7574 6cda 076f 7574 7075  c.outputl..outpu
-00001780: 746c 7245 0000 005a 156d 6170 7461 736b  tlrE...Z.maptask
-00001790: 6572 2e73 7263 2e78 6d6c 6461 7461 7202  er.src.xmldatar.
-000017a0: 0000 00da 146d 6170 7461 736b 6572 2e73  .....maptasker.s
-000017b0: 7263 2e6b 6964 6170 7072 0300 0000 da16  rc.kidappr......
-000017c0: 6d61 7074 6173 6b65 722e 7372 632e 7072  maptasker.src.pr
-000017d0: 696f 7269 7479 7204 0000 00da 146d 6170  iorityr......map
-000017e0: 7461 736b 6572 2e73 7263 2e67 6574 6964  tasker.src.getid
-000017f0: 7372 0500 0000 da16 6d61 7074 6173 6b65  sr......maptaske
-00001800: 722e 7372 632e 7379 7363 6f6e 7374 7206  r.src.sysconstr.
-00001810: 0000 0072 0700 0000 7208 0000 00da 176d  ...r....r......m
-00001820: 6170 7461 736b 6572 2e73 7263 2e73 6865  aptasker.src.she
-00001830: 6c6c 736f 7274 7209 0000 00da 0565 7472  llsortr......etr
-00001840: 6565 da04 6469 6374 da04 6c69 7374 7227  ee..dict..listr'
-00001850: 0000 0072 1d00 0000 da05 7475 706c 6572  ...r......tupler
-00001860: 3300 0000 7239 0000 0072 3d00 0000 7254  3...r9...r=...rT
-00001870: 0000 00da 0462 6f6f 6c72 5900 0000 7225  .....boolrY...r%
-00001880: 0000 0072 2500 0000 7225 0000 0072 2600  ...r%...r%...r&.
-00001890: 0000 da08 3c6d 6f64 756c 653e 0100 0000  ....<module>....
-000018a0: 737e 0000 0008 0d12 0112 020c 010c 010c  s~..............
-000018b0: 010c 010c 010c 010c 010c 021c 0702 4602  ..............F.
-000018c0: 0102 ff02 0202 fe02 0302 fd02 0402 fc02  ................
-000018d0: 0502 fb0c 060a fa02 3402 0102 ff02 0102  ........4.......
-000018e0: ff02 0102 ff0c 020a fe08 1408 1402 5402  ..............T.
-000018f0: 0102 ff02 0202 fe04 0302 fd02 0402 fc02  ................
-00001900: 0502 fb02 0602 fa02 0702 f902 0802 f802  ................
-00001910: 0902 f702 0a02 f602 0b02 f502 0c02 f402  ................
-00001920: 0d0e f3                                  ...
+00000120: 641a 8404 5a1e 6410 651b 641b 6518 640d  d...Z.d.e.d.e.d.
+00000130: 651f 6606 641c 641d 8404 5a20 641e 651b  e.f.d.d...Z d.e.
+00000140: 641f 6519 6420 651b 6421 651b 6422 651b  d.e.d e.d!e.d"e.
+00000150: 6423 6518 6424 6519 6425 6501 6a17 6426  d#e.d$e.d%e.j.d&
+00000160: 6519 6427 6518 640b 6518 6428 6518 640d  e.d'e.d.e.d(e.d.
+00000170: 6401 661a 6429 642a 8404 5a21 641f 6519  d.f.d)d*..Z!d.e.
+00000180: 641e 651b 6425 6501 6a17 6424 6519 6420  d.e.d%e.j.d$e.d 
+00000190: 651b 6421 651b 6426 6519 6422 651b 640b  e.d!e.d&e.d"e.d.
+000001a0: 6518 6428 6518 6427 6518 6423 6518 642b  e.d(e.d'e.d#e.d+
+000001b0: 651f 640d 651f 661c 642c 642d 8404 5a22  e.d.e.f.d,d-..Z"
+000001c0: 6401 5300 292e e900 0000 004e 2901 da0b  d.S.)......N)...
+000001d0: 7461 675f 696e 5f74 7970 6529 01da 0b67  tag_in_type)...g
+000001e0: 6574 5f6b 6964 5f61 7070 2901 da0c 6765  et_kid_app)...ge
+000001f0: 745f 7072 696f 7269 7479 2901 da07 6765  t_priority)...ge
+00000200: 745f 6964 7329 01da 1155 4e4b 4e4f 574e  t_ids)...UNKNOWN
+00000210: 5f54 4153 4b5f 4e41 4d45 2901 da0a 4e4f  _TASK_NAME)...NO
+00000220: 5f50 524f 4a45 4354 2901 da06 6c6f 6767  _PROJECT)...logg
+00000230: 6572 2901 da0a 7368 656c 6c5f 736f 7274  er)...shell_sort
+00000240: da0c 6375 7272 656e 745f 7461 736b da08  ..current_task..
+00000250: 636f 6c6f 726d 6170 da09 7072 6f67 5f61  colormap..prog_a
+00000260: 7267 73da 0672 6574 7572 6e63 0300 0000  rgs..returnc....
+00000270: 0000 0000 0000 0000 0d00 0000 0a00 0000  ................
+00000280: 4300 0000 7352 0100 0067 007d 037a 077c  C...sR...g.}.z.|
+00000290: 00a0 0064 01a1 017d 0457 006e 2304 0074  ...d...}.W.n#..t
+000002a0: 0179 2c01 007d 0501 007a 1774 027c 0083  .y,..}...z.t.|..
+000002b0: 0101 0064 027d 0674 027c 0683 0101 0074  ...d.}.t.|.....t
+000002c0: 03a0 047c 06a1 0101 0067 0057 0006 0059  ...|.....g.W...Y
+000002d0: 0064 037d 057e 0553 0064 037d 057e 0577  .d.}.~.S.d.}.~.w
+000002e0: 0177 007c 0472 a764 047d 0764 057d 0874  .w.|.r.d.}.d.}.t
+000002f0: 057c 0483 0164 056b 0472 3f74 067c 0464  .|...d.k.r?t.|.d
+00000300: 0664 0783 0301 007c 0444 005d 657d 097c  .d.....|.D.]e}.|
+00000310: 09a0 0764 08a1 017d 0a74 08a0 097c 0a7c  ...d...}.t...|.|
+00000320: 0964 067c 0164 097c 02a1 067d 0b74 03a0  .d.|.d.|...}.t..
+00000330: 0464 0a74 0a7c 096a 0b64 0b19 0083 0117  .d.t.|.j.d......
+00000340: 0064 0c17 007c 0a6a 0c17 0064 0d17 007c  .d...|.j...d...|
+00000350: 0b17 0064 0e17 0074 0a7c 096a 0b83 0117  ...d...t.|.j....
+00000360: 00a1 0101 0064 0f7c 0b76 0073 7a64 107c  .....d.|.v.szd.|
+00000370: 0b76 0073 7a64 117c 0b76 0072 887c 0864  .v.szd.|.v.r.|.d
+00000380: 1238 007d 0874 057c 0783 017d 0c7c 0764  .8.}.t.|...}.|.d
+00000390: 137c 0c85 0219 007d 0774 08a0 0d7c 037c  .|.....}.t...|.|
+000003a0: 0b7c 0a7c 087c 07a1 0501 0064 147c 0b76  .|.|.|.....d.|.v
+000003b0: 0073 9d64 107c 0b76 0073 9d64 157c 0b76  .s.d.|.v.s.d.|.v
+000003c0: 0072 a67c 0864 1237 007d 087c 079b 0064  .r.|.d.7.}.|...d
+000003d0: 169d 027d 0771 417c 0353 0029 1761 1d01  ...}.qA|.S.).a..
+000003e0: 0000 0a20 2020 2052 6574 7572 6e20 6120  ...    Return a 
+000003f0: 6c69 7374 206f 6620 5461 736b 2773 2061  list of Task's a
+00000400: 6374 696f 6e73 2066 6f72 2074 6865 2067  ctions for the g
+00000410: 6976 656e 2054 6173 6b0a 2020 2020 2020  iven Task.      
+00000420: 2020 3a70 6172 616d 2063 7572 7265 6e74    :param current
+00000430: 5f74 6173 6b3a 2078 6d6c 2065 6c65 6d65  _task: xml eleme
+00000440: 6e74 206f 6620 7468 6520 5461 736b 2077  nt of the Task w
+00000450: 6520 6172 6520 6765 7474 696e 6720 6163  e are getting ac
+00000460: 7469 6f6e 7320 666f 720a 2020 2020 2020  tions for.      
+00000470: 2020 3a70 6172 616d 2063 6f6c 6f72 6d61    :param colorma
+00000480: 703a 2063 6f6c 6f72 7320 746f 2075 7365  p: colors to use
+00000490: 2069 6e20 6f75 7470 7574 0a20 2020 2020   in output.     
+000004a0: 2020 203a 7061 7261 6d20 7072 6f67 5f61     :param prog_a
+000004b0: 7267 733a 2072 756e 7469 6d65 2061 7267  rgs: runtime arg
+000004c0: 756d 656e 7473 0a20 2020 2020 2020 203a  uments.        :
+000004d0: 7265 7475 726e 3a20 6c69 7374 206f 6620  return: list of 
+000004e0: 5461 736b 2027 6163 7469 6f6e 2720 6f75  Task 'action' ou
+000004f0: 7470 7574 206c 696e 6573 0a20 2020 20da  tput lines.    .
+00000500: 0641 6374 696f 6e7a 1945 7272 6f72 3a20  .Actionz.Error: 
+00000510: 4e6f 2061 6374 696f 6e20 666f 756e 6421  No action found!
+00000520: 2121 4eda 0072 0100 0000 5446 da04 636f  !!N..r....TF..co
+00000530: 6465 da01 747a 0854 6173 6b20 4944 3ada  de..tz.Task ID:.
+00000540: 0273 727a 0620 436f 6465 3a7a 0b20 7461  .srz. Code:z. ta
+00000550: 736b 5f63 6f64 653a 7a0c 4163 7469 6f6e  sk_code:z.Action
+00000560: 2061 7474 723a 7a07 3e45 6e64 2049 667a   attr:z.>End Ifz
+00000570: 053e 456c 7365 7a08 3e45 6e64 2046 6f72  .>Elsez.>End For
+00000580: e901 0000 00e9 1800 0000 7a03 3e49 667a  ..........z.>Ifz
+00000590: 043e 466f 727a 1826 6e62 7370 3b26 6e62  .>Forz.&nbsp;&nb
+000005a0: 7370 3b26 6e62 7370 3b26 6e62 7370 3b29  sp;&nbsp;&nbsp;)
+000005b0: 0eda 0766 696e 6461 6c6c da09 4578 6365  ...findall..Exce
+000005c0: 7074 696f 6eda 0570 7269 6e74 7208 0000  ption..printr...
+000005d0: 00da 0564 6562 7567 da03 6c65 6e72 0900  ...debug..lenr..
+000005e0: 0000 da04 6669 6e64 da0f 6163 7469 6f6e  ....find..action
+000005f0: 5f65 7661 6c75 6174 65da 0f67 6574 5f61  _evaluate..get_a
+00000600: 6374 696f 6e5f 636f 6465 da03 7374 72da  ction_code..str.
+00000610: 0661 7474 7269 62da 0474 6578 74da 0c62  .attrib..text..b
+00000620: 7569 6c64 5f61 6374 696f 6e29 0d72 0a00  uild_action).r..
+00000630: 0000 720b 0000 0072 0c00 0000 5a08 7461  ..r....r....Z.ta
+00000640: 736b 6c69 7374 5a0c 7461 736b 5f61 6374  sklistZ.task_act
+00000650: 696f 6e73 da01 65da 0965 7272 6f72 5f6d  ions..e..error_m
+00000660: 7367 5a12 696e 6465 6e74 6174 696f 6e5f  sgZ.indentation_
+00000670: 616d 6f75 6e74 5a0b 696e 6465 6e74 6174  amountZ.indentat
+00000680: 696f 6eda 0661 6374 696f 6eda 0563 6869  ion..action..chi
+00000690: 6c64 5a09 7461 736b 5f63 6f64 655a 0d6c  ldZ.task_codeZ.l
+000006a0: 656e 6774 685f 696e 6465 6e74 a900 7225  ength_indent..r%
+000006b0: 0000 00fa 742f 5573 6572 732f 6d69 6b72  ....t/Users/mikr
+000006c0: 7562 696e 2f4c 6962 7261 7279 2f43 6c6f  ubin/Library/Clo
+000006d0: 7564 5374 6f72 6167 652f 476f 6f67 6c65  udStorage/Google
+000006e0: 4472 6976 652d 6d69 6b72 7562 696e 4067  Drive-mikrubin@g
+000006f0: 6d61 696c 2e63 6f6d 2f4d 7920 4472 6976  mail.com/My Driv
+00000700: 652f 5079 7468 6f6e 2f6d 6170 7461 736b  e/Python/maptask
+00000710: 6572 2f6d 6170 7461 736b 6572 2f73 7263  er/maptasker/src
+00000720: 2f74 6173 6b73 2e70 79da 0b67 6574 5f61  /tasks.py..get_a
+00000730: 6374 696f 6e73 2100 0000 7368 0000 0004  ctions!...sh....
+00000740: 0802 020e 010e 0108 0104 0108 010a 0110  ................
+00000750: 0108 8002 fb04 0604 0104 010c 030c 0108  ................
+00000760: 020a 0104 020c 0104 ff04 0302 010c 0102  ................
+00000770: ff02 0202 fe04 0302 fd02 0402 fc02 0502  ................
+00000780: fb02 0602 fa08 0702 f904 ff08 0c08 0108  ................
+00000790: 0108 0208 010c 0104 010a 0104 ff18 0408  ................
+000007a0: 020a 0102 8004 0272 2700 0000 da0b 7468  .......r'.....th
+000007b0: 655f 7461 736b 5f69 64da 1a74 6173 6b73  e_task_id..tasks
+000007c0: 5f74 6861 745f 6861 7665 5f62 6565 6e5f  _that_have_been_
+000007d0: 666f 756e 64da 1174 6173 6b5f 6f75 7470  found..task_outp
+000007e0: 7574 5f6c 696e 6573 da09 7461 736b 5f74  ut_lines..task_t
+000007f0: 7970 65da 0961 6c6c 5f74 6173 6b73 6305  ype..all_tasksc.
+00000800: 0000 0000 0000 0000 0000 0009 0000 000a  ................
+00000810: 0000 0043 0000 0073 fa00 0000 7c00 a000  ...C...s....|...
+00000820: a100 7275 7c04 7c00 1900 7d05 7c01 a001  ..ru|.|...}.|...
+00000830: 7c00 a101 0100 6401 7c00 9b00 9d02 7d06  |.....d.|.....}.
+00000840: 7a29 7c05 a002 6402 a101 6a03 7d07 7c03  z)|...d...j.}.|.
+00000850: 6403 6b02 7228 7c02 a001 7c07 9b00 6404  d.k.r(|...|...d.
+00000860: 7c06 9b00 9d03 a101 0100 6e0f 7c02 a001  |.........n.|...
+00000870: 7c07 9b00 6405 7c06 9b00 9d03 a101 0100  |...d.|.........
+00000880: 5700 7c05 7c07 6602 5300 5700 7c05 7c07  W.|.|.f.S.W.|.|.
+00000890: 6602 5300 0400 7404 7974 0100 7d08 0100  f.S...t.yt..}...
+000008a0: 7a2d 7405 7d07 7c03 6403 6b02 7254 7c02  z-t.}.|.d.k.rT|.
+000008b0: a001 7405 9b00 6404 7c06 9b00 9d03 a101  ..t...d.|.......
+000008c0: 0100 6e13 7c02 a001 7405 9b00 6405 7c06  ..n.|...t...d.|.
+000008d0: 9b00 9d03 a101 0100 5700 5900 6406 7d08  ........W.Y.d.}.
+000008e0: 7e08 7c05 7c07 6602 5300 5700 5900 6406  ~.|.|.f.S.W.Y.d.
+000008f0: 7d08 7e08 7c05 7c07 6602 5300 6406 7d08  }.~.|.|.f.S.d.}.
+00000900: 7e08 7701 7700 6406 7d05 6407 7d07 7c05  ~.w.w.d.}.d.}.|.
+00000910: 7c07 6602 5300 2908 6178 0100 000a 2020  |.f.S.).ax....  
+00000920: 2020 4765 7420 7468 6520 6e61 6d65 206f    Get the name o
+00000930: 6620 7468 6520 7461 736b 2067 6976 656e  f the task given
+00000940: 2074 6865 2054 6173 6b20 4944 0a20 2020   the Task ID.   
+00000950: 2020 2020 203a 7061 7261 6d20 7468 655f       :param the_
+00000960: 7461 736b 5f69 643a 2074 6865 2054 6173  task_id: the Tas
+00000970: 6b27 7320 4944 2028 652e 672e 2027 3437  k's ID (e.g. '47
+00000980: 2729 0a20 2020 2020 2020 203a 7061 7261  ').        :para
+00000990: 6d20 7461 736b 735f 7468 6174 5f68 6176  m tasks_that_hav
+000009a0: 655f 6265 656e 5f66 6f75 6e64 3a20 6c69  e_been_found: li
+000009b0: 7374 206f 6620 5461 736b 7320 666f 756e  st of Tasks foun
+000009c0: 6420 736f 2066 6172 0a20 2020 2020 2020  d so far.       
+000009d0: 203a 7061 7261 6d20 7461 736b 5f6f 7574   :param task_out
+000009e0: 7075 745f 6c69 6e65 733a 206c 6973 7420  put_lines: list 
+000009f0: 6f66 2054 6173 6b73 0a20 2020 2020 2020  of Tasks.       
+00000a00: 203a 7061 7261 6d20 7461 736b 5f74 7970   :param task_typ
+00000a10: 653a 2054 7970 6520 6f66 2054 6173 6b20  e: Type of Task 
+00000a20: 2845 6e74 7279 2c20 4578 6974 2c20 5363  (Entry, Exit, Sc
+00000a30: 656e 6529 0a20 2020 2020 2020 203a 7061  ene).        :pa
+00000a40: 7261 6d20 616c 6c5f 7461 736b 733a 2061  ram all_tasks: a
+00000a50: 6c6c 2054 6173 6b73 2069 6e20 786d 6c0a  ll Tasks in xml.
+00000a60: 2020 2020 2020 2020 3a72 6574 7572 6e3a          :return:
+00000a70: 2054 6173 6b27 7320 786d 6c20 656c 656d   Task's xml elem
+00000a80: 656e 742c 2054 6173 6b27 7320 6e61 6d65  ent, Task's name
+00000a90: 0a20 2020 207a 1526 6e62 7370 3b26 6e62  .    z.&nbsp;&nb
+00000aa0: 7370 3b54 6173 6b20 4944 3a20 da03 6e6d  sp;Task ID: ..nm
+00000ab0: 65da 0445 7869 747a 2526 6e62 7370 3b26  e..Exitz%&nbsp;&
+00000ac0: 6e62 7370 3b26 6e62 7370 3b26 6e62 7370  nbsp;&nbsp;&nbsp
+00000ad0: 3b3c 3c3c 2045 7869 7420 5461 736b 7a26  ;<<< Exit Taskz&
+00000ae0: 266e 6273 703b 266e 6273 703b 266e 6273  &nbsp;&nbsp;&nbs
+00000af0: 703b 266e 6273 703b 3c3c 3c20 456e 7472  p;&nbsp;<<< Entr
+00000b00: 7920 5461 736b 4e72 0f00 0000 2906 da07  y TaskNr....)...
+00000b10: 6973 6469 6769 74da 0661 7070 656e 6472  isdigit..appendr
+00000b20: 1a00 0000 721f 0000 0072 1600 0000 7206  ....r....r....r.
+00000b30: 0000 0029 0972 2800 0000 7229 0000 0072  ...).r(...r)...r
+00000b40: 2a00 0000 722b 0000 0072 2c00 0000 da04  *...r+...r,.....
+00000b50: 7461 736b da05 6578 7472 61da 0974 6173  task..extra..tas
+00000b60: 6b5f 6e61 6d65 7221 0000 0072 2500 0000  k_namer!...r%...
+00000b70: 7225 0000 0072 2600 0000 da0d 6765 745f  r%...r&.....get_
+00000b80: 7461 736b 5f6e 616d 6564 0000 0073 4200  task_named...sB.
+00000b90: 0000 0810 0801 0a01 0a01 0201 0c01 0801  ................
+00000ba0: 0401 0c01 06ff 0405 0c01 06ff 0812 02e9  ................
+00000bb0: 0817 0ef1 0401 0801 0401 0c01 06ff 0405  ................
+00000bc0: 0c01 0eff 0807 0af4 080c 0880 02f1 040c  ................
+00000bd0: 0401 0802 7234 0000 00da 1670 726f 6a65  ....r4.....proje
+00000be0: 6374 735f 7769 7468 5f6e 6f5f 7461 736b  cts_with_no_task
+00000bf0: 73da 0c61 6c6c 5f70 726f 6a65 6374 7363  s..all_projectsc
+00000c00: 0300 0000 0000 0000 0000 0000 0600 0000  ................
+00000c10: 0900 0000 4300 0000 7356 0000 0074 007d  ....C...sV...t.}
+00000c20: 0364 017d 047c 0264 0175 0172 277c 0244  .d.}.|.d.u.r'|.D
+00000c30: 005d 1c7d 047c 04a0 0164 02a1 016a 027d  .].}.|...d...j.}
+00000c40: 0374 0364 0369 0069 0067 007c 047c 037c  .t.d.i.i.g.|.|.|
+00000c50: 0183 077d 057c 007c 0576 0072 267c 037c  ...}.|.|.v.r&|.|
+00000c60: 0466 0202 0001 0053 0071 0a7c 037c 0466  .f.....S.q.|.|.f
+00000c70: 0253 0029 0461 4b01 0000 0a20 2020 2046  .S.).aK....    F
+00000c80: 696e 6420 7468 6520 5072 6f6a 6563 7420  ind the Project 
+00000c90: 6265 6c6f 6e67 696e 6720 746f 2074 6865  belonging to the
+00000ca0: 2054 6173 6b20 6964 2070 6173 7365 6420   Task id passed 
+00000cb0: 696e 0a20 2020 2020 2020 203a 7061 7261  in.        :para
+00000cc0: 6d20 7468 655f 7461 736b 5f69 643a 2074  m the_task_id: t
+00000cd0: 6865 2049 4420 6f66 2074 6865 2054 6173  he ID of the Tas
+00000ce0: 6b0a 2020 2020 2020 2020 3a70 6172 616d  k.        :param
+00000cf0: 2070 726f 6a65 6374 735f 7769 7468 5f6e   projects_with_n
+00000d00: 6f5f 7461 736b 733a 206c 6973 7420 6f66  o_tasks: list of
+00000d10: 2050 726f 6a65 6374 7320 7468 6174 2064   Projects that d
+00000d20: 6f20 6e6f 7420 6861 7665 2061 6e79 2054  o not have any T
+00000d30: 6173 6b73 0a20 2020 2020 2020 203a 7061  asks.        :pa
+00000d40: 7261 6d20 616c 6c5f 7072 6f6a 6563 7473  ram all_projects
+00000d50: 3a20 616c 6c20 5461 736b 6572 2050 726f  : all Tasker Pro
+00000d60: 6a65 6374 730a 2020 2020 2020 2020 3a72  jects.        :r
+00000d70: 6574 7572 6e3a 206e 616d 6520 6f66 2074  eturn: name of t
+00000d80: 6865 2050 726f 6a65 6374 2074 6861 7420  he Project that 
+00000d90: 6265 6c6f 6e67 7320 746f 2074 6869 7320  belongs to this 
+00000da0: 7461 736b 2061 6e64 2074 6865 2050 726f  task and the Pro
+00000db0: 6a65 6374 2078 6d6c 2065 6c65 6d65 6e74  ject xml element
+00000dc0: 0a20 2020 204e da04 6e61 6d65 4629 0472  .    N..nameF).r
+00000dd0: 0700 0000 721a 0000 0072 1f00 0000 7205  ....r....r....r.
+00000de0: 0000 0029 0672 2800 0000 7235 0000 0072  ...).r(...r5...r
+00000df0: 3600 0000 5a09 7072 6f6a 5f6e 616d 65da  6...Z.proj_name.
+00000e00: 0770 726f 6a65 6374 da08 7461 736b 5f69  .project..task_i
+00000e10: 6473 7225 0000 0072 2500 0000 7226 0000  dsr%...r%...r&..
+00000e20: 00da 1967 6574 5f70 726f 6a65 6374 5f66  ...get_project_f
+00000e30: 6f72 5f73 6f6c 6f5f 7461 736b 9800 0000  or_solo_task....
+00000e40: 7318 0000 0004 0a04 0108 0108 020c 0102  s...............
+00000e50: 010e 0104 ff08 030c 0102 ff08 0272 3a00  .............r:.
+00000e60: 0000 da0a 616c 6c5f 7363 656e 6573 6302  ....all_scenesc.
+00000e70: 0000 0000 0000 0000 0000 0005 0000 0006  ................
+00000e80: 0000 0043 0000 0073 6000 0000 7c01 a000  ...C...s`...|...
+00000e90: a100 4400 5d29 7d02 7c02 4400 5d24 7d03  ..D.])}.|.D.]$}.
+00000ea0: 7401 7c03 6a02 6401 8302 722c 7c03 4400  t.|.j.d...r,|.D.
+00000eb0: 5d19 7d04 7401 7c04 6a02 6402 8302 7224  ].}.t.|.j.d...r$
+00000ec0: 7c00 7c04 6a03 6b02 7224 0100 0100 0100  |.|.j.k.r$......
+00000ed0: 6401 5300 7c03 6a02 6403 6b02 722b 0100  d.S.|.j.d.k.r+..
+00000ee0: 6e01 7112 7108 7104 6402 5300 2904 6118  n.q.q.q.d.S.).a.
+00000ef0: 0100 000a 2020 2020 4964 656e 7469 6679  ....    Identify
+00000f00: 2077 6865 7468 6572 2074 6865 2054 6173   whether the Tas
+00000f10: 6b20 7061 7373 6564 2069 6e20 6973 2070  k passed in is p
+00000f20: 6172 7420 6f66 2061 2053 6365 6e65 3a20  art of a Scene: 
+00000f30: 5472 7565 203d 2079 6573 2c20 4661 6c73  True = yes, Fals
+00000f40: 6520 3d20 6e6f 0a20 2020 2020 2020 203a  e = no.        :
+00000f50: 7061 7261 6d20 7468 655f 7461 736b 5f69  param the_task_i
+00000f60: 643a 2074 6865 2069 6420 6f66 2074 6865  d: the id of the
+00000f70: 2054 6173 6b20 746f 2063 6865 636b 2061   Task to check a
+00000f80: 6761 696e 7374 0a20 2020 2020 2020 203a  gainst.        :
+00000f90: 7061 7261 6d20 616c 6c5f 7363 656e 6573  param all_scenes
+00000fa0: 3a20 616c 6c20 5363 656e 6573 2069 6e20  : all Scenes in 
+00000fb0: 5461 736b 6572 2063 6f6e 6669 6775 7261  Tasker configura
+00000fc0: 7469 6f6e 0a20 2020 2020 2020 203a 7265  tion.        :re
+00000fd0: 7475 726e 3a20 5472 7565 2069 6620 5461  turn: True if Ta
+00000fe0: 736b 2069 7320 7061 7274 206f 6620 6120  sk is part of a 
+00000ff0: 5363 656e 652c 2046 616c 7365 206f 7468  Scene, False oth
+00001000: 6572 7769 7365 0a20 2020 2054 46da 0353  erwise.    TF..S
+00001010: 7472 2904 da06 7661 6c75 6573 7202 0000  tr)...valuesr...
+00001020: 00da 0374 6167 721f 0000 0029 0572 2800  ...tagr....).r(.
+00001030: 0000 723b 0000 00da 0576 616c 7565 7224  ..r;.....valuer$
+00001040: 0000 005a 0873 7562 6368 696c 6472 2500  ...Z.subchildr%.
+00001050: 0000 7225 0000 0072 2600 0000 da0d 7461  ..r%...r&.....ta
+00001060: 736b 5f69 6e5f 7363 656e 65b3 0000 0073  sk_in_scene....s
+00001070: 1c00 0000 0c08 0801 0c01 0801 0a03 02ff  ................
+00001080: 0a02 0a02 0a01 0401 0202 0280 02f4 040d  ................
+00001090: 7240 0000 00da 0d6f 7572 5f74 6173 6b5f  r@.....our_task_
+000010a0: 6e61 6d65 da0b 6f75 7470 7574 5f6c 6973  name..output_lis
+000010b0: 74da 0c70 726f 6a65 6374 5f6e 616d 65da  t..project_name.
+000010c0: 0c70 726f 6669 6c65 5f6e 616d 65da 0768  .profile_name..h
+000010d0: 6561 6469 6e67 da0b 666f 756e 645f 6974  eading..found_it
+000010e0: 656d 73da 0974 6173 6b5f 6c69 7374 da10  ems..task_list..
+000010f0: 6f75 725f 7461 736b 5f65 6c65 6d65 6e74  our_task_element
+00001100: da13 6c69 7374 5f6f 665f 666f 756e 645f  ..list_of_found_
+00001110: 7461 736b 73da 1061 6c6c 5f74 6173 6b65  tasks..all_taske
+00001120: 725f 6974 656d 73da 0c70 726f 6772 616d  r_items..program
+00001130: 5f61 7267 7363 0c00 0000 0000 0000 0000  _argsc..........
+00001140: 0000 1100 0000 0a00 0000 4300 0000 730a  ..........C...s.
+00001150: 0100 0064 0164 026c 006d 017d 0c01 0074  ...d.d.l.m.}...t
+00001160: 02a0 0364 037c 0b64 0419 009b 0064 057c  ...d.|.d.....d.|
+00001170: 009b 009d 04a1 0101 007c 0b64 0419 007c  .........|.d...|
+00001180: 006b 0272 5664 067c 0564 073c 0074 04a0  .k.rVd.|.d.<.t..
+00001190: 0564 067c 017c 027c 037c 047c 0a7c 0ba1  .d.|.|.|.|.|.|..
+000011a0: 0701 0067 007d 0d74 067c 0683 0164 086b  ...g.}.t.|...d.k
+000011b0: 0472 4774 067c 0083 017d 0e7c 0644 005d  .rGt.|...}.|.D.]
+000011c0: 0f7d 0f7c 007c 0f64 097c 0e85 0219 006b  .}.|.|.d.|.....k
+000011d0: 0272 457c 0f67 017d 0d01 006e 0171 366e  .rE|.g.}...n.q6n
+000011e0: 027c 067d 0d7c 0c64 0a7c 017c 0d7c 077c  .|.}.|.d.|.|.|.|
+000011f0: 087c 0b7c 0a7c 0983 0801 0064 0953 0074  .|.|.|.....d.S.t
+00001200: 067c 0683 0164 086b 0472 817c 0644 005d  .|...d.k.r.|.D.]
+00001210: 247d 107c 0b64 0419 007c 1076 0072 8074  $}.|.d...|.v.r.t
+00001220: 04a0 077c 0a7c 0b7c 0164 0864 0ba1 0501  ...|.|.|.d.d....
+00001230: 007c 1067 017d 067c 0c64 0a7c 017c 067c  .|.g.}.|.d.|.|.|
+00001240: 077c 087c 0b7c 0a7c 0983 0801 0001 0064  .|.|.|.|.......d
+00001250: 0953 0071 5e64 0953 0064 0953 0029 0c61  .S.q^d.S.d.S.).a
+00001260: db02 0000 0a20 2020 2050 726f 6365 7373  .....    Process
+00001270: 2061 2073 696e 676c 6520 5461 736b 206f   a single Task o
+00001280: 6e6c 790a 2020 2020 2020 2020 3a70 6172  nly.        :par
+00001290: 616d 206f 7572 5f74 6173 6b5f 6e61 6d65  am our_task_name
+000012a0: 3a20 6e61 6d65 206f 6620 7468 6520 5461  : name of the Ta
+000012b0: 736b 2074 6f20 7072 6f63 6573 730a 2020  sk to process.  
+000012c0: 2020 2020 2020 3a70 6172 616d 206f 7574        :param out
+000012d0: 7075 745f 6c69 7374 3a20 7768 6572 6520  put_list: where 
+000012e0: 7468 6520 6f75 7470 7574 206c 696e 6520  the output line 
+000012f0: 676f 6573 2066 6f72 2054 6173 6b0a 2020  goes for Task.  
+00001300: 2020 2020 2020 3a70 6172 616d 2070 726f        :param pro
+00001310: 6a65 6374 5f6e 616d 653a 206e 616d 6520  ject_name: name 
+00001320: 6f66 2074 6865 2050 726f 6a65 6374 2054  of the Project T
+00001330: 6173 6b20 6265 6c6f 6e67 7320 746f 0a20  ask belongs to. 
+00001340: 2020 2020 2020 203a 7061 7261 6d20 7072         :param pr
+00001350: 6f66 696c 655f 6e61 6d65 3a20 6e61 6d65  ofile_name: name
+00001360: 206f 6620 7468 6520 5072 6f66 696c 6520   of the Profile 
+00001370: 7468 6520 5461 736b 2062 656c 6f6e 6773  the Task belongs
+00001380: 2074 6f0a 2020 2020 2020 2020 3a70 6172   to.        :par
+00001390: 616d 2068 6561 6469 6e67 3a20 7468 6520  am heading: the 
+000013a0: 6865 6164 696e 672c 2069 6620 616e 790a  heading, if any.
+000013b0: 2020 2020 2020 2020 3a70 6172 616d 2066          :param f
+000013c0: 6f75 6e64 5f69 7465 6d73 3a20 7369 6e67  ound_items: sing
+000013d0: 6c65 206e 616d 6520 666f 7220 5072 6f6a  le name for Proj
+000013e0: 6563 742f 5072 6f66 696c 652f 5461 736b  ect/Profile/Task
+000013f0: 0a20 2020 2020 2020 203a 7061 7261 6d20  .        :param 
+00001400: 7461 736b 5f6c 6973 743a 206c 6973 7420  task_list: list 
+00001410: 6f66 2054 6173 6b73 0a20 2020 2020 2020  of Tasks.       
+00001420: 203a 7061 7261 6d20 6f75 725f 7461 736b   :param our_task
+00001430: 5f65 6c65 6d65 6e74 3a20 7468 6520 786d  _element: the xm
+00001440: 6c20 656c 656d 656e 7420 666f 7220 7468  l element for th
+00001450: 6973 2054 6173 6b0a 2020 2020 2020 2020  is Task.        
+00001460: 3a70 6172 616d 206c 6973 745f 6f66 5f66  :param list_of_f
+00001470: 6f75 6e64 5f74 6173 6b73 3a20 616c 6c20  ound_tasks: all 
+00001480: 5461 736b 7320 7072 6f63 6573 7365 6420  Tasks processed 
+00001490: 736f 2066 6172 0a20 2020 2020 2020 203a  so far.        :
+000014a0: 7061 7261 6d20 616c 6c5f 7461 736b 6572  param all_tasker
+000014b0: 5f69 7465 6d73 3a20 616c 6c20 5072 6f6a  _items: all Proj
+000014c0: 6563 7473 2f50 726f 6669 6c65 732f 5461  ects/Profiles/Ta
+000014d0: 736b 732f 5363 656e 6573 0a20 2020 2020  sks/Scenes.     
+000014e0: 2020 203a 7061 7261 6d20 636f 6c6f 726d     :param colorm
+000014f0: 6170 3a20 636f 6c6f 7273 2074 6f20 7573  ap: colors to us
+00001500: 6520 696e 206f 7574 7075 740a 2020 2020  e in output.    
+00001510: 2020 2020 3a70 6172 616d 2070 726f 6772      :param progr
+00001520: 616d 5f61 7267 733a 2072 756e 7469 6d65  am_args: runtime
+00001530: 2061 7267 756d 656e 7473 0a20 2020 2072   arguments.    r
+00001540: 0100 0000 a901 da0c 7072 6f63 6573 735f  ........process_
+00001550: 6c69 7374 7a17 7461 736b 7320 7369 6e67  listz.tasks sing
+00001560: 6c65 2074 6173 6b20 6e61 6d65 3ada 1073  le task name:..s
+00001570: 696e 676c 655f 7461 736b 5f6e 616d 657a  ingle_task_namez
+00001580: 0f20 6f75 7220 5461 736b 206e 616d 653a  . our Task name:
+00001590: 54da 1173 696e 676c 655f 7461 736b 5f66  T..single_task_f
+000015a0: 6f75 6e64 7213 0000 004e fa05 5461 736b  oundr....N..Task
+000015b0: 3a72 0f00 0000 2908 da16 6d61 7074 6173  :r....)...maptas
+000015c0: 6b65 722e 7372 632e 7072 6f63 6c69 7374  ker.src.proclist
+000015d0: 724d 0000 0072 0800 0000 7218 0000 00da  rM...r....r.....
+000015e0: 0c62 7569 6c64 5f6f 7574 7075 74da 1272  .build_output..r
+000015f0: 6566 7265 7368 5f6f 7572 5f6f 7574 7075  efresh_our_outpu
+00001600: 7472 1900 0000 da09 6d79 5f6f 7574 7075  tr......my_outpu
+00001610: 7429 1172 4100 0000 7242 0000 0072 4300  t).rA...rB...rC.
+00001620: 0000 7244 0000 0072 4500 0000 7246 0000  ..rD...rE...rF..
+00001630: 0072 4700 0000 7248 0000 0072 4900 0000  .rG...rH...rI...
+00001640: 724a 0000 0072 0b00 0000 724b 0000 0072  rJ...r....rK...r
+00001650: 4d00 0000 5a13 7465 6d70 6f72 6172 795f  M...Z.temporary_
+00001660: 7461 736b 5f6c 6973 745a 1474 6865 5f74  task_listZ.the_t
+00001670: 6173 6b5f 6e61 6d65 5f6c 656e 6774 68da  ask_name_length.
+00001680: 0469 7465 6d5a 0974 6173 6b5f 6974 656d  .itemZ.task_item
+00001690: 7225 0000 0072 2500 0000 7226 0000 00da  r%...r%...r&....
+000016a0: 0e64 6f5f 7369 6e67 6c65 5f74 6173 6bcf  .do_single_task.
+000016b0: 0000 0073 7400 0000 0c1e 0402 0c01 0201  ...st...........
+000016c0: 04ff 04ff 0c04 0802 0402 0201 0201 0201  ................
+000016d0: 0201 0201 0201 0201 04f9 040b 0c01 0801  ................
+000016e0: 0801 1001 0601 0401 02fe 0280 0404 0202  ................
+000016f0: 0201 0201 0201 0201 0201 0201 0201 0201  ................
+00001700: 08f8 0c0b 0802 0c01 0401 0a01 04ff 0603  ................
+00001710: 0201 0201 0201 0201 0201 0201 0201 0201  ................
+00001720: 0201 04f8 060d 02ee 04fd 0402 7256 0000  ............rV..
+00001730: 00da 0864 6f5f 6578 7472 6163 0d00 0000  ...do_extrac....
+00001740: 0000 0000 0000 0000 1000 0000 0d00 0000  ................
+00001750: 4300 0000 73d6 0000 0064 0164 026c 006d  C...s....d.d.l.m
+00001760: 017d 0d01 007c 0c72 317c 0964 0319 0064  .}...|.r1|.d...d
+00001770: 046b 0272 3174 027c 0283 0104 007d 0e72  .k.r1t.|.....}.r
+00001780: 1f7c 0364 0119 009b 0064 057c 0e9b 009d  .|.d.....d.|....
+00001790: 037c 0364 013c 0074 037c 0264 0683 0204  .|.d.<.t.|.d....
+000017a0: 007d 0f72 317c 0364 0119 009b 0064 057c  .}.r1|.d.....d.|
+000017b0: 0f9b 009d 037c 0364 013c 007c 0164 076b  .....|.d.<.|.d.k
+000017c0: 0372 4a7c 0964 0819 0072 4a74 047c 017c  .rJ|.d...rJt.|.|
+000017d0: 007c 047c 057c 077c 0b7c 037c 027c 067c  .|.|.|.|.|.|.|.|
+000017e0: 0a7c 087c 0983 0c01 0064 0953 007c 0372  .|.|.....d.S.|.r
+000017f0: 6974 05a0 067c 087c 097c 0064 0a64 07a1  it...|.|.|.d.d..
+00001800: 0501 007c 0d64 0b7c 007c 037c 027c 067c  ...|.d.|.|.|.|.|
+00001810: 097c 087c 0a83 0801 0074 05a0 067c 087c  .|.|.....t...|.|
+00001820: 097c 0064 0464 07a1 0501 0064 0653 0029  .|.d.d.....d.S.)
+00001830: 0c61 5c03 0000 0a20 2020 2057 6520 6861  .a\....    We ha
+00001840: 7665 2061 2073 696e 676c 6520 5461 736b  ve a single Task
+00001850: 206f 7220 6120 6c69 7374 206f 6620 5461   or a list of Ta
+00001860: 736b 732e 2020 4f75 7470 7574 2069 742f  sks.  Output it/
+00001870: 7468 656d 2e0a 2020 2020 2020 2020 3a70  them..        :p
+00001880: 6172 616d 206f 7574 7075 745f 6c69 7374  aram output_list
+00001890: 3a20 6c69 7374 206f 6620 6f75 7470 7574  : list of output
+000018a0: 206c 696e 6573 2067 656e 6572 6174 6564   lines generated
+000018b0: 2074 6875 7320 6661 720a 2020 2020 2020   thus far.      
+000018c0: 2020 3a70 6172 616d 206f 7572 5f74 6173    :param our_tas
+000018d0: 6b5f 6e61 6d65 3a20 6e61 6d65 206f 6620  k_name: name of 
+000018e0: 5461 736b 0a20 2020 2020 2020 203a 7061  Task.        :pa
+000018f0: 7261 6d20 6f75 725f 7461 736b 5f65 6c65  ram our_task_ele
+00001900: 6d65 6e74 3a20 5461 736b 2078 6d6c 2065  ment: Task xml e
+00001910: 6c65 6d65 6e74 0a20 2020 2020 2020 203a  lement.        :
+00001920: 7061 7261 6d20 7461 736b 5f6c 6973 743a  param task_list:
+00001930: 2054 6173 6b20 6c69 7374 0a20 2020 2020   Task list.     
+00001940: 2020 203a 7061 7261 6d20 7072 6f6a 6563     :param projec
+00001950: 745f 6e61 6d65 3a20 6e61 6d65 206f 6620  t_name: name of 
+00001960: 6375 7272 656e 7420 5072 6f6a 6563 740a  current Project.
+00001970: 2020 2020 2020 2020 3a70 6172 616d 2070          :param p
+00001980: 726f 6669 6c65 5f6e 616d 653a 206e 616d  rofile_name: nam
+00001990: 6520 6f66 2063 7572 7265 6e74 2050 726f  e of current Pro
+000019a0: 6669 6c65 0a20 2020 2020 2020 203a 7061  file.        :pa
+000019b0: 7261 6d20 6c69 7374 5f6f 665f 666f 756e  ram list_of_foun
+000019c0: 645f 7461 736b 733a 206c 6973 7420 6f66  d_tasks: list of
+000019d0: 2054 6173 6b73 2066 6f75 6e64 2073 6f20   Tasks found so 
+000019e0: 6661 720a 2020 2020 2020 2020 3a70 6172  far.        :par
+000019f0: 616d 2068 6561 6469 6e67 3a20 6375 7272  am heading: curr
+00001a00: 656e 7420 6865 6164 696e 670a 2020 2020  ent heading.    
+00001a10: 2020 2020 3a70 6172 616d 2063 6f6c 6f72      :param color
+00001a20: 6d61 703a 2063 6f6c 6f72 7320 746f 2075  map: colors to u
+00001a30: 7365 2069 6e20 6f75 7470 7574 0a20 2020  se in output.   
+00001a40: 2020 2020 203a 7061 7261 6d20 7072 6f67       :param prog
+00001a50: 7261 6d5f 6172 6773 3a20 7275 6e74 696d  ram_args: runtim
+00001a60: 6520 6172 6775 6d65 6e74 730a 2020 2020  e arguments.    
+00001a70: 2020 2020 3a70 6172 616d 2061 6c6c 5f74      :param all_t
+00001a80: 6173 6b65 725f 6974 656d 733a 2061 6c6c  asker_items: all
+00001a90: 2050 726f 6a65 6374 732f 5072 6f66 696c   Projects/Profil
+00001aa0: 6573 2f54 6173 6b73 2f53 6365 6e65 730a  es/Tasks/Scenes.
+00001ab0: 2020 2020 2020 2020 3a70 6172 616d 2066          :param f
+00001ac0: 6f75 6e64 5f69 7465 6d73 3a20 7369 6e67  ound_items: sing
+00001ad0: 6c65 2050 726f 6a65 6374 2f50 726f 6669  le Project/Profi
+00001ae0: 6c65 2f54 6173 6b20 746f 2073 6561 7263  le/Task to searc
+00001af0: 6820 666f 720a 2020 2020 2020 2020 3a70  h for.        :p
+00001b00: 6172 616d 2064 6f5f 6578 7472 613a 2066  aram do_extra: f
+00001b10: 6c61 6720 746f 2064 6f2f 6f75 7470 7574  lag to do/output
+00001b20: 2065 7874 7261 2054 6173 6b20 7374 7566   extra Task stuf
+00001b30: 660a 2020 2020 2020 2020 3a72 6574 7572  f.        :retur
+00001b40: 6e3a 2054 7275 6520 6966 2077 6520 6172  n: True if we ar
+00001b50: 6520 7365 6172 6368 696e 6720 666f 7220  e searching for 
+00001b60: 6120 7369 6e67 6c65 2054 6173 6b20 616e  a single Task an
+00001b70: 6420 666f 756e 6420 6974 2e20 204f 7468  d found it.  Oth
+00001b80: 6572 7769 7365 2c20 4661 6c73 650a 2020  erwise, False.  
+00001b90: 2020 7201 0000 0072 4c00 0000 da14 6469    r....rL.....di
+00001ba0: 7370 6c61 795f 6465 7461 696c 5f6c 6576  splay_detail_lev
+00001bb0: 656c e903 0000 00fa 0120 4672 0f00 0000  el....... Fr....
+00001bc0: 724e 0000 0054 7213 0000 0072 5000 0000  rN...Tr....rP...
+00001bd0: 2907 7251 0000 0072 4d00 0000 7203 0000  ).rQ...rM...r...
+00001be0: 0072 0400 0000 7256 0000 0072 5200 0000  .r....rV...rR...
+00001bf0: 7254 0000 0029 1072 4200 0000 7241 0000  rT...).rB...rA..
+00001c00: 0072 4800 0000 7247 0000 0072 4300 0000  .rH...rG...rC...
+00001c10: 7244 0000 0072 4900 0000 7245 0000 0072  rD...rI...rE...r
+00001c20: 0b00 0000 724b 0000 0072 4a00 0000 7246  ....rK...rJ...rF
+00001c30: 0000 0072 5700 0000 724d 0000 00da 0c6b  ...rW...rM.....k
+00001c40: 6964 5f61 7070 5f69 6e66 6fda 0870 7269  id_app_info..pri
+00001c50: 6f72 6974 7972 2500 0000 7225 0000 0072  orityr%...r%...r
+00001c60: 2600 0000 da0b 6f75 7470 7574 5f74 6173  &.....output_tas
+00001c70: 6b32 0100 0073 4800 0000 0c21 1003 0c01  k2...sH....!....
+00001c80: 1601 0e01 1601 1003 0201 0201 0201 0201  ................
+00001c90: 0201 0201 0201 0201 0201 0201 0201 0201  ................
+00001ca0: 0201 04f4 040e 0401 1202 0202 0201 0201  ................
+00001cb0: 0201 0201 0201 0201 0201 0201 04f8 120b  ................
+00001cc0: 0402 725d 0000 0029 23da 1578 6d6c 2e65  ..r]...)#..xml.e
+00001cd0: 7472 6565 2e45 6c65 6d65 6e74 5472 6565  tree.ElementTree
+00001ce0: da03 786d 6cda 156d 6170 7461 736b 6572  ..xml..maptasker
+00001cf0: 2e73 7263 2e61 6374 696f 6e65 da03 7372  .src.actione..sr
+00001d00: 63da 0761 6374 696f 6e65 721b 0000 00da  c..actioner.....
+00001d10: 156d 6170 7461 736b 6572 2e73 7263 2e6f  .maptasker.src.o
+00001d20: 7574 7075 746c da07 6f75 7470 7574 6c72  utputl..outputlr
+00001d30: 5200 0000 da15 6d61 7074 6173 6b65 722e  R.....maptasker.
+00001d40: 7372 632e 786d 6c64 6174 6172 0200 0000  src.xmldatar....
+00001d50: da14 6d61 7074 6173 6b65 722e 7372 632e  ..maptasker.src.
+00001d60: 6b69 6461 7070 7203 0000 00da 166d 6170  kidappr......map
+00001d70: 7461 736b 6572 2e73 7263 2e70 7269 6f72  tasker.src.prior
+00001d80: 6974 7972 0400 0000 da14 6d61 7074 6173  ityr......maptas
+00001d90: 6b65 722e 7372 632e 6765 7469 6473 7205  ker.src.getidsr.
+00001da0: 0000 00da 166d 6170 7461 736b 6572 2e73  .....maptasker.s
+00001db0: 7263 2e73 7973 636f 6e73 7472 0600 0000  rc.sysconstr....
+00001dc0: 7207 0000 0072 0800 0000 da17 6d61 7074  r....r......mapt
+00001dd0: 6173 6b65 722e 7372 632e 7368 656c 6c73  asker.src.shells
+00001de0: 6f72 7472 0900 0000 da05 6574 7265 65da  ortr......etree.
+00001df0: 0464 6963 74da 046c 6973 7472 2700 0000  .dict..listr'...
+00001e00: 721d 0000 00da 0574 7570 6c65 7234 0000  r......tupler4..
+00001e10: 0072 3a00 0000 da04 626f 6f6c 7240 0000  .r:.....boolr@..
+00001e20: 0072 5600 0000 725d 0000 0072 2500 0000  .rV...r]...r%...
+00001e30: 7225 0000 0072 2500 0000 7226 0000 00da  r%...r%...r&....
+00001e40: 083c 6d6f 6475 6c65 3e01 0000 0073 b600  .<module>....s..
+00001e50: 0000 080d 1201 1202 0c01 0c01 0c01 0c01  ................
+00001e60: 0c01 0c01 0c01 0c02 1c07 0243 0201 02ff  ...........C....
+00001e70: 0202 02fe 0203 02fd 0204 02fc 0205 02fb  ................
+00001e80: 0c06 0afa 0234 0201 02ff 0201 02ff 0201  .....4..........
+00001e90: 02ff 0c02 0afe 161b 021c 0201 02ff 0202  ................
+00001ea0: 02fe 0203 02fd 0204 02fc 0205 02fb 0206  ................
+00001eb0: 02fa 0207 02f9 0408 02f8 0209 02f7 020a  ................
+00001ec0: 02f6 020b 02f5 020c 02f4 020d 0af3 0263  ...............c
+00001ed0: 0201 02ff 0202 02fe 0403 02fd 0204 02fc  ................
+00001ee0: 0205 02fb 0206 02fa 0207 02f9 0208 02f8  ................
+00001ef0: 0209 02f7 020a 02f6 020b 02f5 020c 02f4  ................
+00001f00: 020d 02f3 020e 0ef2                      ........
```

### Comparing `maptasker-1.3.1/maptasker/src/__pycache__/taskuniq.cpython-310.pyc` & `maptasker-1.3.2/maptasker/src/__pycache__/taskuniq.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Sun Mar 19 16:23:16 2023 UTC, .py size: 9244 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 14% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 f436 1764 1c24 0000  o........6.d.$..
+00000000: 6f0d 0d0a 0000 0000 dd63 2c64 3625 0000  o........c,d6%..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0012 0000 0040 0000 0073 da00 0000 6400  .....@...s....d.
 00000030: 6401 6c00 6d01 5a01 6d02 5a02 0100 6400  d.l.m.Z.m.Z...d.
 00000040: 6402 6c03 6d04 0200 0100 6d05 5a06 0100  d.l.m.....m.Z...
 00000050: 6400 6402 6c07 6d04 0200 0100 6d08 5a08  d.d.l.m.....m.Z.
 00000060: 0100 6400 6403 6c09 6d0a 5a0a 0100 6400  ..d.d.l.m.Z...d.
 00000070: 6404 6c09 6d0b 5a0b 0100 6400 6405 6c09  d.l.m.Z...d.d.l.
@@ -22,193 +22,194 @@
 00000150: 54da 0b6f 7574 7075 745f 6c69 7374 da16  T..output_list..
 00000160: 7072 6f6a 6563 7473 5f77 6974 685f 6e6f  projects_with_no
 00000170: 5f74 6173 6b73 da19 7072 6f6a 6563 7473  _tasks..projects
 00000180: 5f77 6974 686f 7574 5f70 726f 6669 6c65  _without_profile
 00000190: 73da 0b66 6f75 6e64 5f69 7465 6d73 da08  s..found_items..
 000001a0: 636f 6c6f 726d 6170 da0c 7072 6f67 7261  colormap..progra
 000001b0: 6d5f 6172 6773 da06 7265 7475 726e 6306  m_args..returnc.
-000001c0: 0000 0000 0000 0000 0000 0007 0000 000e  ................
-000001d0: 0000 0043 0000 0073 bc00 0000 7400 7c01  ...C...s....t.|.
-000001e0: 8301 6401 6b04 722e 7c03 6402 1900 732e  ..d.k.r.|.d...s.
+000001c0: 0000 0000 0000 0000 0000 0007 0000 000d  ................
+000001d0: 0000 0043 0000 0073 c400 0000 7400 7c01  ...C...s....t.|.
+000001e0: 8301 6401 6b04 7234 7c03 6402 1900 7334  ..d.k.r4|.d...s4
 000001f0: 7401 a002 7c04 7c05 7c00 6401 6403 7c04  t...|.|.|.d.d.|.
-00000200: 6404 1900 9b00 6405 7403 9b00 6406 9d05  d.....d.t...d...
-00000210: a105 0100 7c01 4400 5d0f 7d06 7401 a002  ....|.D.].}.t...
-00000220: 7c04 7c05 7c00 6407 6408 7c06 9b00 6409  |.|.|.d.d.|...d.
-00000230: 9d03 a105 0100 711e 7c02 725c 7401 a002  ......q.|.r\t...
-00000240: 7c04 7c05 7c00 6401 640a 7c04 6404 1900  |.|.|.d.d.|.d...
-00000250: 9b00 640b 7403 9b00 640c 9d05 a105 0100  ..d.t...d.......
-00000260: 7c02 4400 5d17 7d06 7401 a002 7c04 7c05  |.D.].}.t...|.|.
-00000270: 7c00 6407 640d 7c04 6404 1900 9b00 640b  |.d.d.|.d.....d.
-00000280: 7403 9b00 640e 7c06 9b00 640f 9d07 a105  t...d.|...d.....
-00000290: 0100 7144 6400 5300 2910 4e72 0100 0000  ..qDd.S.).Nr....
-000002a0: da11 7369 6e67 6c65 5f74 6173 6b5f 666f  ..single_task_fo
-000002b0: 756e 647a 163c 6872 3e3c 7370 616e 2073  undz.<hr><span s
-000002c0: 7479 6c65 3d63 6f6c 6f72 3dda 1774 7261  tyle=color=..tra
-000002d0: 696c 696e 675f 636f 6d6d 656e 7473 5f63  iling_comments_c
-000002e0: 6f6c 6f72 fa01 227a 303c 2f66 6f6e 743e  olor.."z0</font>
-000002f0: 3c65 6d3e 5072 6f6a 6563 7473 3c2f 666f  <em>Projects</fo
-00000300: 6e74 3e20 5769 7468 6f75 7420 5461 736b  nt> Without Task
-00000310: 732e 2e2e 3c2f 656d 3ee9 0400 0000 7a08  s...</em>.....z.
-00000320: 5072 6f6a 6563 7420 7a0d 2068 6173 206e  Project z. has n
-00000330: 6f20 5461 736b 737a 173c 6872 3e3c 7370  o Tasksz.<hr><sp
-00000340: 616e 2073 7479 6c65 3d22 636f 6c6f 723a  an style="color:
-00000350: 7a02 223e 7a2c 3c2f 666f 6e74 3e3c 656d  z.">z,</font><em
-00000360: 3e50 726f 6a65 6374 7320 5769 7468 6f75  >Projects Withou
-00000370: 7420 5072 6f66 696c 6573 2e2e 2e3c 2f65  t Profiles...</e
-00000380: 6d3e 7a13 3c73 7061 6e20 7374 796c 653d  m>z.<span style=
-00000390: 2263 6f6c 6f72 3a7a 0f3c 2f66 6f6e 743e  "color:z.</font>
-000003a0: 5072 6f6a 6563 7420 7a10 2068 6173 206e  Project z. has n
-000003b0: 6f20 5072 6f66 696c 6573 2904 da03 6c65  o Profiles)...le
-000003c0: 6eda 0c62 7569 6c64 5f6f 7574 7075 74da  n..build_output.
-000003d0: 096d 795f 6f75 7470 7574 7204 0000 0029  .my_outputr....)
-000003e0: 0772 0700 0000 7208 0000 0072 0900 0000  .r....r....r....
-000003f0: 720a 0000 0072 0b00 0000 720c 0000 00da  r....r....r.....
-00000400: 0469 7465 6da9 0072 1600 0000 fa77 2f55  .item..r.....w/U
-00000410: 7365 7273 2f6d 696b 7275 6269 6e2f 4c69  sers/mikrubin/Li
-00000420: 6272 6172 792f 436c 6f75 6453 746f 7261  brary/CloudStora
-00000430: 6765 2f47 6f6f 676c 6544 7269 7665 2d6d  ge/GoogleDrive-m
-00000440: 696b 7275 6269 6e40 676d 6169 6c2e 636f  ikrubin@gmail.co
-00000450: 6d2f 4d79 2044 7269 7665 2f50 7974 686f  m/My Drive/Pytho
-00000460: 6e2f 6d61 7074 6173 6b65 722f 6d61 7074  n/maptasker/mapt
-00000470: 6173 6b65 722f 7372 632f 7461 736b 756e  asker/src/taskun
-00000480: 6971 2e70 79da 2270 726f 6365 7373 5f6d  iq.py."process_m
-00000490: 6973 7369 6e67 5f74 6173 6b73 5f61 6e64  issing_tasks_and
-000004a0: 5f70 726f 6669 6c65 731a 0000 0073 5600  _profiles....sV.
-000004b0: 0000 1409 0401 0201 0201 0201 0201 0202  ................
-000004c0: 0601 04ff 0201 06ff 04fa 080b 0401 1201  ................
-000004d0: 06ff 0405 0401 0201 0201 0201 0201 0202  ................
-000004e0: 0601 04ff 0201 06ff 04fa 080b 0401 0201  ................
-000004f0: 0201 0201 0201 0202 0601 04ff 0201 04ff  ................
-00000500: 0202 06fe 06fa 040b 7218 0000 00da 0c68  ........r......h
-00000510: 6176 655f 6865 6164 696e 6763 0b00 0000  ave_headingc....
-00000520: 0000 0000 0000 0000 1300 0000 0e00 0000  ................
-00000530: 4300 0000 7350 0100 0064 017d 0b64 025c  C...sP...d.}.d.\
-00000540: 027d 0c7d 0d74 00a0 017c 017c 077c 0a64  .}.}.t...|.|.|.d
-00000550: 0319 00a1 035c 027d 0e7d 0f74 00a0 027c  .....\.}.}.t...|
-00000560: 017c 0267 0064 017c 0a64 0419 00a1 055c  .|.g.d.|.d.....\
-00000570: 027d 107d 117c 1174 036b 0272 3974 039b  .}.}.|.t.k.r9t..
-00000580: 0064 057c 019b 009d 037d 1174 00a0 047c  .d.|.....}.t...|
-00000590: 017c 0a64 0619 00a1 0272 367c 067c 0d7c  .|.d.....r6|.|.|
-000005a0: 0566 0353 0064 077d 0c6e 027c 117d 0b7c  .f.S.d.}.n.|.}.|
-000005b0: 0564 0837 007d 057c 0673 6a74 05a0 067c  .d.7.}.|.sjt...|
-000005c0: 097c 037c 0064 0964 0aa1 0501 0074 05a0  .|.|.d.d.....t..
-000005d0: 067c 097c 037c 0064 0964 0b7c 0964 0c19  .|.|.|.d.d.|.d..
-000005e0: 009b 0064 0d9d 037c 0364 0e19 0017 0064  ...d...|.d.....d
-000005f0: 0f17 00a1 0501 0074 05a0 067c 097c 037c  .......t...|.|.|
-00000600: 0064 0864 01a1 0501 0064 077d 067c 0c73  .d.d.....d.}.|.s
-00000610: 887c 0e74 076b 0372 887c 0364 1019 0072  .|.t.k.r.|.d...r
-00000620: 807c 1164 117c 019b 0064 127c 0e9b 0064  .|.d.|...d.|...d
-00000630: 139d 0537 007d 116e 087c 1164 127c 0e9b  ...7.}.n.|.d.|..
-00000640: 0064 139d 0337 007d 117c 0c72 907c 0364  .d...7.}.|.r.|.d
-00000650: 1419 0064 156b 0272 a37c 1167 017d 1274  ...d.k.r.|.g.}.t
-00000660: 00a0 087c 007c 0b7c 107c 127c 0e64 1667  ...|.|.|.|.|.d.g
-00000670: 007c 087c 097c 037c 0a7c 04a1 0c7d 0d7c  .|.|.|.|.|...}.|
-00000680: 067c 0d7c 0566 0353 0029 174e da00 2902  .|.|.f.S.).N..).
-00000690: 4646 da0c 616c 6c5f 7072 6f6a 6563 7473  FF..all_projects
-000006a0: da09 616c 6c5f 7461 736b 737a 1526 6e62  ..all_tasksz.&nb
-000006b0: 7370 3b26 6e62 7370 3b54 6173 6b20 4944  sp;&nbsp;Task ID
-000006c0: 3a20 da0a 616c 6c5f 7363 656e 6573 54e9  : ..all_scenesT.
-000006d0: 0100 0000 7201 0000 007a 043c 6872 3e7a  ....r....z.<hr>z
-000006e0: 0d3c 666f 6e74 2063 6f6c 6f72 3d22 720f  .<font color="r.
-000006f0: 0000 0072 1000 0000 da0b 666f 6e74 5f74  ...r......font_t
-00000700: 6f5f 7573 657a 2b54 6173 6b73 2074 6861  o_usez+Tasks tha
-00000710: 7420 6172 6520 6e6f 7420 6361 6c6c 6564  t are not called
-00000720: 2062 7920 616e 7920 5072 6f66 696c 652e   by any Profile.
-00000730: 2e2e da05 6465 6275 677a 0f20 7769 7468  ....debugz. with
-00000740: 2054 6173 6b20 4944 3a20 7a0f 202e 2e2e   Task ID: z. ...
-00000750: 696e 2050 726f 6a65 6374 207a 1420 3c65  in Project z. <e
-00000760: 6d3e 4e6f 2050 726f 6669 6c65 3c2f 656d  m>No Profile</em
-00000770: 3eda 1464 6973 706c 6179 5f64 6574 6169  >..display_detai
-00000780: 6c5f 6c65 7665 6ce9 0300 0000 da04 4e6f  l_level.......No
-00000790: 6e65 2909 da05 7461 736b 73da 1967 6574  ne)...tasks..get
-000007a0: 5f70 726f 6a65 6374 5f66 6f72 5f73 6f6c  _project_for_sol
-000007b0: 6f5f 7461 736b da0d 6765 745f 7461 736b  o_task..get_task
-000007c0: 5f6e 616d 6572 0500 0000 da0d 7461 736b  _namer......task
-000007d0: 5f69 6e5f 7363 656e 6572 1300 0000 7214  _in_scener....r.
-000007e0: 0000 0072 0600 0000 da0b 6f75 7470 7574  ...r......output
-000007f0: 5f74 6173 6b29 1372 0700 0000 da07 7461  _task).r......ta
-00000800: 736b 5f69 64da 0b66 6f75 6e64 5f74 6173  sk_id..found_tas
-00000810: 6b73 720c 0000 0072 0a00 0000 da12 756e  ksr....r......un
-00000820: 6e61 6d65 645f 7461 736b 5f63 6f75 6e74  named_task_count
-00000830: 7219 0000 0072 0800 0000 da07 6865 6164  r....r......head
-00000840: 696e 6772 0b00 0000 da10 616c 6c5f 7461  ingr......all_ta
-00000850: 736b 6572 5f69 7465 6d73 da0d 7468 655f  sker_items..the_
-00000860: 7461 736b 5f6e 616d 655a 0c75 6e6b 6e6f  task_nameZ.unkno
-00000870: 776e 5f74 6173 6bda 0d73 7065 6369 6669  wn_task..specifi
-00000880: 635f 7461 736b da0c 7072 6f6a 6563 745f  c_task..project_
-00000890: 6e61 6d65 5a0b 7468 655f 7072 6f6a 6563  nameZ.the_projec
-000008a0: 74da 0c74 6173 6b5f 656c 656d 656e 74da  t..task_element.
-000008b0: 0974 6173 6b5f 6e61 6d65 da09 7461 736b  .task_name..task
-000008c0: 5f6c 6973 7472 1600 0000 7216 0000 0072  _listr....r....r
-000008d0: 1700 0000 da21 7072 6f63 6573 735f 736f  .....!process_so
-000008e0: 6c6f 5f74 6173 6b5f 7769 7468 5f6e 6f5f  lo_task_with_no_
-000008f0: 7072 6f66 696c 6553 0000 0073 7400 0000  profileS...st...
-00000900: 040d 0801 0403 0a01 08ff 0405 0e01 08ff  ................
-00000910: 0803 0e01 1002 0a01 0601 0402 0801 0403  ................
-00000920: 0401 0a01 04ff 0403 0201 0201 0201 0201  ................
-00000930: 0e02 0601 02ff 0202 02fe 04fa 040b 0a01  ................
-00000940: 04ff 0403 0c02 0801 0201 1001 06ff 1005  ................
-00000950: 0403 0c01 0602 0403 0201 0201 0201 0201  ................
-00000960: 0201 0201 0201 0201 0201 0201 0201 0201  ................
-00000970: 04f4 0a0e 7234 0000 00da 1066 6f75 6e64  ....r4.....found
-00000980: 5f74 6173 6b73 5f6c 6973 7472 2c00 0000  _tasks_listr,...
-00000990: 722d 0000 0063 0800 0000 0000 0000 0000  r-...c..........
-000009a0: 0000 0d00 0000 0d00 0000 4300 0000 73f8  ..........C...s.
-000009b0: 0000 0064 017d 0864 027d 0964 037d 0a7c  ...d.}.d.}.d.}.|
-000009c0: 0764 0419 0044 005d 217d 0b7c 0464 0519  .d...D.]!}.|.d..
-000009d0: 0072 1201 006e 1a7c 0b7c 0276 0172 2b74  .r...n.|.|.v.r+t
-000009e0: 007c 007c 0b7c 027c 037c 047c 087c 0a7c  .|.|.|.|.|.|.|.|
-000009f0: 017c 057c 067c 0783 0b5c 037d 0a7d 0c7d  .|.|.|...\.}.}.}
-00000a00: 087c 0c72 2b01 006e 0171 0a7c 0864 016b  .|.r+..n.q.|.d.k
-00000a10: 0472 647c 0364 0619 0064 016b 0472 3f74  .rd|.d...d.k.r?t
-00000a20: 01a0 027c 067c 037c 0064 0164 02a1 0501  ...|.|.|.d.d....
-00000a30: 0074 01a0 027c 067c 037c 0064 0764 02a1  .t...|.|.|.d.d..
-00000a40: 0501 007c 0464 0519 0073 647c 0364 0619  ...|.d...sd|.d..
-00000a50: 0064 016b 0372 6474 01a0 027c 067c 037c  .d.k.rdt...|.|.|
-00000a60: 0064 0164 087c 0664 0919 009b 0064 0a7c  .d.d.|.d.....d.|
-00000a70: 089b 0064 0b9d 05a1 0501 007c 0964 0c75  ...d.......|.d.u
-00000a80: 0072 7174 01a0 027c 067c 037c 0064 0764  .rqt...|.|.|.d.d
-00000a90: 02a1 0501 0074 01a0 027c 067c 037c 0064  .....t...|.|.|.d
-00000aa0: 0764 02a1 0501 0064 0053 0029 0d4e 7201  .d.....d.S.).Nr.
-00000ab0: 0000 0072 1a00 0000 4672 1c00 0000 720e  ...r....Fr....r.
-00000ac0: 0000 0072 2100 0000 7222 0000 007a 0c3c  ...r!...r"...z.<
-00000ad0: 666f 6e74 2063 6f6c 6f72 3dda 1275 6e6b  font color=..unk
-00000ae0: 6e6f 776e 5f74 6173 6b5f 636f 6c6f 727a  nown_task_colorz
-00000af0: 163e 5468 6572 6520 6172 6520 6120 746f  .>There are a to
-00000b00: 7461 6c20 6f66 207a 2d20 756e 6e61 6d65  tal of z- unname
-00000b10: 6420 5461 736b 7320 6e6f 7420 6173 736f  d Tasks not asso
-00000b20: 6369 6174 6564 2077 6974 6820 6120 5072  ciated with a Pr
-00000b30: 6f66 696c 6521 5429 0372 3400 0000 7213  ofile!T).r4...r.
-00000b40: 0000 0072 1400 0000 290d 7207 0000 0072  ...r....).r....r
-00000b50: 0800 0000 7235 0000 0072 0c00 0000 720a  ....r5...r....r.
-00000b60: 0000 0072 2c00 0000 720b 0000 0072 2d00  ...r,...r....r-.
-00000b70: 0000 722b 0000 0072 3200 0000 7219 0000  ..r+...r2...r...
-00000b80: 0072 2900 0000 722f 0000 0072 1600 0000  .r)...r/...r....
-00000b90: 7216 0000 0072 1700 0000 da23 7072 6f63  r....r.....#proc
-00000ba0: 6573 735f 7461 736b 735f 6e6f 745f 6361  ess_tasks_not_ca
-00000bb0: 6c6c 6564 5f62 795f 7072 6f66 696c 65af  lled_by_profile.
-00000bc0: 0000 0073 6800 0000 040a 0401 0401 0c03  ...sh...........
-00000bd0: 0201 0201 04ff 0403 0806 0202 0201 0201  ................
-00000be0: 0201 0201 0201 0201 0201 0201 0201 0201  ................
-00000bf0: 0201 02f5 08ff 040f 0401 0280 0803 0c01  ................
-00000c00: 1201 0401 0a01 04ff 0605 02ff 0c02 0402  ................
-00000c10: 0201 0201 0201 0201 0c02 0201 06ff 04fa  ................
-00000c20: 080c 0401 0a01 04ff 0404 0a01 04ff 0403  ................
-00000c30: 7237 0000 0029 13da 0674 7970 696e 6772  r7...)...typingr
-00000c40: 0200 0000 7203 0000 00da 156d 6170 7461  ....r......mapta
-00000c50: 736b 6572 2e73 7263 2e6f 7574 7075 746c  sker.src.outputl
-00000c60: da03 7372 63da 076f 7574 7075 746c 7213  ..src..outputlr.
-00000c70: 0000 00da 136d 6170 7461 736b 6572 2e73  .....maptasker.s
-00000c80: 7263 2e74 6173 6b73 7224 0000 00da 166d  rc.tasksr$.....m
-00000c90: 6170 7461 736b 6572 2e73 7263 2e73 7973  aptasker.src.sys
-00000ca0: 636f 6e73 7472 0400 0000 7205 0000 0072  constr....r....r
-00000cb0: 0600 0000 da03 7374 72da 0464 6963 7472  ......str..dictr
-00000cc0: 1800 0000 da04 626f 6f6c 7234 0000 0072  ......boolr4...r
-00000cd0: 3700 0000 7216 0000 0072 1600 0000 7216  7...r....r....r.
-00000ce0: 0000 0072 1700 0000 da08 3c6d 6f64 756c  ...r......<modul
-00000cf0: 653e 0100 0000 7356 0000 0010 0d12 0212  e>....sV........
-00000d00: 010c 010c 010c 0102 0606 0102 ff0e 0202  ................
-00000d10: fe06 0302 fd02 0402 fc02 0502 fb02 0602  ................
-00000d20: fa02 070a f902 3902 070a f902 5c06 0102  ......9.....\...
-00000d30: ff02 0202 fe06 0302 fd02 0402 fc02 0502  ................
-00000d40: fb02 0602 fa02 0702 f902 0802 f802 090e  ................
-00000d50: f7                                       .
+00000200: 6404 1900 9b00 7403 9b00 6405 9d04 a105  d.....t...d.....
+00000210: 0100 7c01 4400 5d16 7d06 7401 a002 7c04  ..|.D.].}.t...|.
+00000220: 7c05 7c00 6406 6407 7c04 6404 1900 9b00  |.|.d.d.|.d.....
+00000230: 7403 9b00 6408 7c06 9b00 6409 9d06 a105  t...d.|...d.....
+00000240: 0100 711d 7c02 7260 7401 a002 7c04 7c05  ..q.|.r`t...|.|.
+00000250: 7c00 6401 640a 7c04 6404 1900 9b00 7403  |.d.d.|.d.....t.
+00000260: 9b00 640b 9d04 a105 0100 7c02 4400 5d16  ..d.......|.D.].
+00000270: 7d06 7401 a002 7c04 7c05 7c00 6406 6407  }.t...|.|.|.d.d.
+00000280: 7c04 6404 1900 9b00 7403 9b00 6408 7c06  |.d.....t...d.|.
+00000290: 9b00 640c 9d06 a105 0100 7149 6400 5300  ..d.......qId.S.
+000002a0: 290d 4e72 0100 0000 da11 7369 6e67 6c65  ).Nr......single
+000002b0: 5f74 6173 6b5f 666f 756e 647a 173c 6872  _task_foundz.<hr
+000002c0: 3e3c 7370 616e 2073 7479 6c65 3d22 636f  ><span style="co
+000002d0: 6c6f 723a da17 7472 6169 6c69 6e67 5f63  lor:..trailing_c
+000002e0: 6f6d 6d65 6e74 735f 636f 6c6f 727a 2a3e  omments_colorz*>
+000002f0: 3c65 6d3e 5072 6f6a 6563 7473 2057 6974  <em>Projects Wit
+00000300: 686f 7574 2054 6173 6b73 2e2e 2e3c 2f65  hout Tasks...</e
+00000310: 6d3e 3c2f 7370 616e 3ee9 0400 0000 fa13  m></span>.......
+00000320: 3c73 7061 6e20 7374 796c 653d 2263 6f6c  <span style="col
+00000330: 6f72 3a7a 093e 5072 6f6a 6563 7420 7a14  or:z.>Project z.
+00000340: 2068 6173 206e 6f20 5461 736b 733c 2f73   has no Tasks</s
+00000350: 7061 6e3e 7a16 3c68 723e 3c73 7061 6e20  pan>z.<hr><span 
+00000360: 7374 796c 653d 636f 6c6f 723a 7a26 3e3c  style=color:z&><
+00000370: 656d 3e50 726f 6a65 6374 7320 5769 7468  em>Projects With
+00000380: 6f75 7420 5072 6f66 696c 6573 2e2e 2e3c  out Profiles...<
+00000390: 2f65 6d3e 7a10 2068 6173 206e 6f20 5072  /em>z. has no Pr
+000003a0: 6f66 696c 6573 2904 da03 6c65 6eda 0c62  ofiles)...len..b
+000003b0: 7569 6c64 5f6f 7574 7075 74da 096d 795f  uild_output..my_
+000003c0: 6f75 7470 7574 7204 0000 0029 0772 0700  outputr....).r..
+000003d0: 0000 7208 0000 0072 0900 0000 720a 0000  ..r....r....r...
+000003e0: 0072 0b00 0000 720c 0000 00da 0469 7465  .r....r......ite
+000003f0: 6da9 0072 1600 0000 fa77 2f55 7365 7273  m..r.....w/Users
+00000400: 2f6d 696b 7275 6269 6e2f 4c69 6272 6172  /mikrubin/Librar
+00000410: 792f 436c 6f75 6453 746f 7261 6765 2f47  y/CloudStorage/G
+00000420: 6f6f 676c 6544 7269 7665 2d6d 696b 7275  oogleDrive-mikru
+00000430: 6269 6e40 676d 6169 6c2e 636f 6d2f 4d79  bin@gmail.com/My
+00000440: 2044 7269 7665 2f50 7974 686f 6e2f 6d61   Drive/Python/ma
+00000450: 7074 6173 6b65 722f 6d61 7074 6173 6b65  ptasker/maptaske
+00000460: 722f 7372 632f 7461 736b 756e 6971 2e70  r/src/taskuniq.p
+00000470: 79da 2270 726f 6365 7373 5f6d 6973 7369  y."process_missi
+00000480: 6e67 5f74 6173 6b73 5f61 6e64 5f70 726f  ng_tasks_and_pro
+00000490: 6669 6c65 731a 0000 0073 6600 0000 1409  files....sf.....
+000004a0: 0401 0201 0201 0201 0201 0202 0601 02ff  ................
+000004b0: 0201 06ff 04fa 080b 0401 0201 0201 0201  ................
+000004c0: 0201 0a02 0201 04ff 0201 06ff 06fa 040c  ................
+000004d0: 0401 0201 0201 0201 0201 0202 0601 02ff  ................
+000004e0: 0201 06ff 04fa 080b 0401 0201 0201 0201  ................
+000004f0: 0201 0202 0601 02ff 0201 04ff 0202 06fe  ................
+00000500: 06fa 040b 7218 0000 00da 0c68 6176 655f  ....r......have_
+00000510: 6865 6164 696e 6763 0b00 0000 0000 0000  headingc........
+00000520: 0000 0000 1300 0000 0f00 0000 4300 0000  ............C...
+00000530: 7352 0100 0064 017d 0b64 025c 027d 0c7d  sR...d.}.d.\.}.}
+00000540: 0d74 00a0 017c 017c 077c 0a64 0319 00a1  .t...|.|.|.d....
+00000550: 035c 027d 0e7d 0f74 00a0 027c 017c 0267  .\.}.}.t...|.|.g
+00000560: 0064 017c 0a64 0419 00a1 055c 027d 107d  .d.|.d.....\.}.}
+00000570: 117c 1174 036b 0272 3974 039b 0064 057c  .|.t.k.r9t...d.|
+00000580: 019b 009d 037d 1174 00a0 047c 017c 0a64  .....}.t...|.|.d
+00000590: 0619 00a1 0272 367c 067c 0d7c 0566 0353  .....r6|.|.|.f.S
+000005a0: 0064 077d 0c6e 027c 117d 0b7c 0564 0837  .d.}.n.|.}.|.d.7
+000005b0: 007d 057c 0673 6a74 05a0 067c 097c 037c  .}.|.sjt...|.|.|
+000005c0: 0064 0964 0aa1 0501 0074 05a0 067c 097c  .d.d.....t...|.|
+000005d0: 037c 0064 0964 0b7c 0964 0c19 009b 007c  .|.d.d.|.d.....|
+000005e0: 0364 0d19 009b 0064 0e9d 0464 0f17 00a1  .d.....d...d....
+000005f0: 0501 0074 05a0 067c 097c 037c 0064 0864  ...t...|.|.|.d.d
+00000600: 01a1 0501 0064 077d 067c 0c73 887c 0e74  .....d.}.|.s.|.t
+00000610: 076b 0372 887c 0364 1019 0072 807c 1164  .k.r.|.d...r.|.d
+00000620: 117c 019b 0064 127c 0e9b 0064 139d 0537  .|...d.|...d...7
+00000630: 007d 116e 087c 1164 127c 0e9b 0064 139d  .}.n.|.d.|...d..
+00000640: 0337 007d 117c 0c72 907c 0364 1419 0064  .7.}.|.r.|.d...d
+00000650: 156b 0272 a47c 1167 017d 1274 00a0 087c  .k.r.|.g.}.t...|
+00000660: 007c 0b7c 107c 127c 0e64 1667 007c 087c  .|.|.|.|.d.g.|.|
+00000670: 097c 037c 0a7c 0464 17a1 0d7d 0d7c 067c  .|.|.|.d...}.|.|
+00000680: 0d7c 0566 0353 0029 184e da00 2902 4646  .|.f.S.).N..).FF
+00000690: da0c 616c 6c5f 7072 6f6a 6563 7473 da09  ..all_projects..
+000006a0: 616c 6c5f 7461 736b 737a 1526 6e62 7370  all_tasksz.&nbsp
+000006b0: 3b26 6e62 7370 3b54 6173 6b20 4944 3a20  ;&nbsp;Task ID: 
+000006c0: da0a 616c 6c5f 7363 656e 6573 54e9 0100  ..all_scenesT...
+000006d0: 0000 7201 0000 007a 043c 6872 3e72 1100  ..r....z.<hr>r..
+000006e0: 0000 720f 0000 00da 0b66 6f6e 745f 746f  ..r......font_to
+000006f0: 5f75 7365 fa01 3e7a 3154 6173 6b73 2074  _use..>z1Tasks t
+00000700: 6861 7420 6172 6520 6e6f 7420 6361 6c6c  hat are not call
+00000710: 6564 2062 7920 616e 7920 5072 6f66 696c  ed by any Profil
+00000720: 652e 2e2e 3c73 7061 6e3e da05 6465 6275  e...<span>..debu
+00000730: 677a 0f20 7769 7468 2054 6173 6b20 4944  gz. with Task ID
+00000740: 3a20 7a0f 202e 2e2e 696e 2050 726f 6a65  : z. ...in Proje
+00000750: 6374 207a 1420 3c65 6d3e 4e6f 2050 726f  ct z. <em>No Pro
+00000760: 6669 6c65 3c2f 656d 3eda 1464 6973 706c  file</em>..displ
+00000770: 6179 5f64 6574 6169 6c5f 6c65 7665 6ce9  ay_detail_level.
+00000780: 0300 0000 da04 4e6f 6e65 4629 09da 0574  ......NoneF)...t
+00000790: 6173 6b73 da19 6765 745f 7072 6f6a 6563  asks..get_projec
+000007a0: 745f 666f 725f 736f 6c6f 5f74 6173 6bda  t_for_solo_task.
+000007b0: 0d67 6574 5f74 6173 6b5f 6e61 6d65 7205  .get_task_namer.
+000007c0: 0000 00da 0d74 6173 6b5f 696e 5f73 6365  .....task_in_sce
+000007d0: 6e65 7213 0000 0072 1400 0000 7206 0000  ner....r....r...
+000007e0: 00da 0b6f 7574 7075 745f 7461 736b 2913  ...output_task).
+000007f0: 7207 0000 00da 0774 6173 6b5f 6964 da0b  r......task_id..
+00000800: 666f 756e 645f 7461 736b 7372 0c00 0000  found_tasksr....
+00000810: 720a 0000 00da 1275 6e6e 616d 6564 5f74  r......unnamed_t
+00000820: 6173 6b5f 636f 756e 7472 1900 0000 7208  ask_countr....r.
+00000830: 0000 00da 0768 6561 6469 6e67 720b 0000  .....headingr...
+00000840: 00da 1061 6c6c 5f74 6173 6b65 725f 6974  ...all_tasker_it
+00000850: 656d 73da 0d74 6865 5f74 6173 6b5f 6e61  ems..the_task_na
+00000860: 6d65 5a0c 756e 6b6e 6f77 6e5f 7461 736b  meZ.unknown_task
+00000870: da0d 7370 6563 6966 6963 5f74 6173 6bda  ..specific_task.
+00000880: 0c70 726f 6a65 6374 5f6e 616d 655a 0b74  .project_nameZ.t
+00000890: 6865 5f70 726f 6a65 6374 da0c 7461 736b  he_project..task
+000008a0: 5f65 6c65 6d65 6e74 da09 7461 736b 5f6e  _element..task_n
+000008b0: 616d 65da 0974 6173 6b5f 6c69 7374 7216  ame..task_listr.
+000008c0: 0000 0072 1600 0000 7217 0000 00da 2170  ...r....r.....!p
+000008d0: 726f 6365 7373 5f73 6f6c 6f5f 7461 736b  rocess_solo_task
+000008e0: 5f77 6974 685f 6e6f 5f70 726f 6669 6c65  _with_no_profile
+000008f0: 5a00 0000 737a 0000 0004 0d08 0104 030a  Z...sz..........
+00000900: 0108 ff04 050e 0108 ff08 030e 0110 020a  ................
+00000910: 0106 0104 0208 0104 0304 010a 0104 ff04  ................
+00000920: 0302 0102 0102 0102 0102 0206 0102 ff06  ................
+00000930: 0106 ff02 0202 fe04 fa04 0b0a 0104 ff04  ................
+00000940: 030c 0208 0102 0110 0106 ff10 0504 030c  ................
+00000950: 0106 0204 0302 0102 0102 0102 0102 0102  ................
+00000960: 0102 0102 0102 0102 0102 0102 0102 0104  ................
+00000970: f30a 0f72 3500 0000 da10 666f 756e 645f  ...r5.....found_
+00000980: 7461 736b 735f 6c69 7374 722d 0000 0072  tasks_listr-...r
+00000990: 2e00 0000 6308 0000 0000 0000 0000 0000  ....c...........
+000009a0: 000d 0000 000d 0000 0043 0000 0073 0001  .........C...s..
+000009b0: 0000 6401 7d08 6402 7d09 6403 7d0a 7c07  ..d.}.d.}.d.}.|.
+000009c0: 6404 1900 4400 5d21 7d0b 7c04 6405 1900  d...D.]!}.|.d...
+000009d0: 7212 0100 6e1a 7c0b 7c02 7601 722b 7400  r...n.|.|.v.r+t.
+000009e0: 7c00 7c0b 7c02 7c03 7c04 7c08 7c0a 7c01  |.|.|.|.|.|.|.|.
+000009f0: 7c05 7c06 7c07 830b 5c03 7d0a 7d0c 7d08  |.|.|...\.}.}.}.
+00000a00: 7c0c 722b 0100 6e01 710a 7c08 6401 6b04  |.r+..n.q.|.d.k.
+00000a10: 7268 7c03 6406 1900 6401 6b04 723f 7401  rh|.d...d.k.r?t.
+00000a20: a002 7c06 7c03 7c00 6401 6402 a105 0100  ..|.|.|.d.d.....
+00000a30: 7401 a002 7c06 7c03 7c00 6407 6402 a105  t...|.|.|.d.d...
+00000a40: 0100 7c04 6405 1900 7368 7c03 6406 1900  ..|.d...sh|.d...
+00000a50: 6401 6b03 7268 7401 a002 7c06 7c03 7c00  d.k.rht...|.|.|.
+00000a60: 6401 6408 7c06 6409 1900 9b00 7c03 640a  d.d.|.d.....|.d.
+00000a70: 1900 9b00 640b 7c08 9b00 640c 9d06 a105  ....d.|...d.....
+00000a80: 0100 7c09 640d 7500 7275 7401 a002 7c06  ..|.d.u.rut...|.
+00000a90: 7c03 7c00 6407 6402 a105 0100 7401 a002  |.|.d.d.....t...
+00000aa0: 7c06 7c03 7c00 6407 6402 a105 0100 6400  |.|.|.d.d.....d.
+00000ab0: 5300 290e 4e72 0100 0000 721a 0000 0046  S.).Nr....r....F
+00000ac0: 721c 0000 0072 0e00 0000 7222 0000 0072  r....r....r"...r
+00000ad0: 2300 0000 7211 0000 00da 1275 6e6b 6e6f  #...r......unkno
+00000ae0: 776e 5f74 6173 6b5f 636f 6c6f 7272 1f00  wn_task_colorr..
+00000af0: 0000 7a16 3e54 6865 7265 2061 7265 2061  ..z.>There are a
+00000b00: 2074 6f74 616c 206f 6620 7a34 2075 6e6e   total of z4 unn
+00000b10: 616d 6564 2054 6173 6b73 206e 6f74 2061  amed Tasks not a
+00000b20: 7373 6f63 6961 7465 6420 7769 7468 2061  ssociated with a
+00000b30: 2050 726f 6669 6c65 213c 2f73 7061 6e3e   Profile!</span>
+00000b40: 5429 0372 3500 0000 7213 0000 0072 1400  T).r5...r....r..
+00000b50: 0000 290d 7207 0000 0072 0800 0000 7236  ..).r....r....r6
+00000b60: 0000 0072 0c00 0000 720a 0000 0072 2d00  ...r....r....r-.
+00000b70: 0000 720b 0000 0072 2e00 0000 722c 0000  ..r....r....r,..
+00000b80: 0072 3300 0000 7219 0000 0072 2a00 0000  .r3...r....r*...
+00000b90: 7230 0000 0072 1600 0000 7216 0000 0072  r0...r....r....r
+00000ba0: 1700 0000 da23 7072 6f63 6573 735f 7461  .....#process_ta
+00000bb0: 736b 735f 6e6f 745f 6361 6c6c 6564 5f62  sks_not_called_b
+00000bc0: 795f 7072 6f66 696c 65b7 0000 0073 7000  y_profile....sp.
+00000bd0: 0000 040a 0401 0401 0c03 0201 0201 04ff  ................
+00000be0: 0403 0806 0202 0201 0201 0201 0201 0201  ................
+00000bf0: 0201 0201 0201 0201 0201 0201 02f5 08ff  ................
+00000c00: 040f 0401 0280 0803 0c01 1201 0401 0a01  ................
+00000c10: 04ff 0605 02ff 0c02 0402 0201 0201 0201  ................
+00000c20: 0201 0202 0601 02ff 0601 04ff 0202 06fe  ................
+00000c30: 04fa 080d 0401 0a01 04ff 0404 0a01 04ff  ................
+00000c40: 0403 7238 0000 0029 13da 0674 7970 696e  ..r8...)...typin
+00000c50: 6772 0200 0000 7203 0000 00da 156d 6170  gr....r......map
+00000c60: 7461 736b 6572 2e73 7263 2e6f 7574 7075  tasker.src.outpu
+00000c70: 746c da03 7372 63da 076f 7574 7075 746c  tl..src..outputl
+00000c80: 7213 0000 00da 136d 6170 7461 736b 6572  r......maptasker
+00000c90: 2e73 7263 2e74 6173 6b73 7225 0000 00da  .src.tasksr%....
+00000ca0: 166d 6170 7461 736b 6572 2e73 7263 2e73  .maptasker.src.s
+00000cb0: 7973 636f 6e73 7472 0400 0000 7205 0000  ysconstr....r...
+00000cc0: 0072 0600 0000 da03 7374 72da 0464 6963  .r......str..dic
+00000cd0: 7472 1800 0000 da04 626f 6f6c 7235 0000  tr......boolr5..
+00000ce0: 0072 3800 0000 7216 0000 0072 1600 0000  .r8...r....r....
+00000cf0: 7216 0000 0072 1700 0000 da08 3c6d 6f64  r....r......<mod
+00000d00: 756c 653e 0100 0000 7356 0000 0010 0d12  ule>....sV......
+00000d10: 0212 010c 010c 010c 0102 0606 0102 ff0e  ................
+00000d20: 0202 fe06 0302 fd02 0402 fc02 0502 fb02  ................
+00000d30: 0602 fa02 070a f902 4002 070a f902 5d06  ........@.....].
+00000d40: 0102 ff02 0202 fe06 0302 fd02 0402 fc02  ................
+00000d50: 0502 fb02 0602 fa02 0702 f902 0802 f802  ................
+00000d60: 090e f7                                  ...
```

### Comparing `maptasker-1.3.1/maptasker/src/__pycache__/userintr.cpython-310.pyc` & `maptasker-1.3.2/maptasker/src/__pycache__/userintr.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Wed Mar 15 17:54:20 2023 UTC, .py size: 28690 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 18% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 4c06 1264 1270 0000  o.......L..d.p..
+00000000: 6f0d 0d0a 0000 0000 918f 1c64 1270 0000  o..........d.p..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0073 5a00 0000 6400  .....@...sZ...d.
 00000030: 6401 6c00 5a00 6400 6402 6c01 6d02 5a02  d.l.Z.d.d.l.m.Z.
 00000040: 0100 6400 6403 6c03 6d04 5a04 0100 6400  ..d.d.l.m.Z...d.
 00000050: 6404 6c05 6d06 5a06 0100 6500 a007 6405  d.l.m.Z...e...d.
 00000060: a101 0100 6500 a008 6406 a101 0100 6407  ....e...d.....d.
 00000070: 5a09 4700 6408 6409 8400 6409 6500 6a0a  Z.G.d.d...d.e.j.
@@ -219,64 +219,64 @@
 00000da0: 0072 0100 0000 e98c 0000 0029 02da 0577  .r.........)...w
 00000db0: 6964 7468 5a0d 636f 726e 6572 5f72 6164  idthZ.corner_rad
 00000dc0: 6975 73e9 0600 0000 da04 6e73 6577 2904  ius.......nsew).
 00000dd0: da03 726f 77da 0663 6f6c 756d 6e5a 0772  ..row..columnZ.r
 00000de0: 6f77 7370 616e da06 7374 6963 6b79 e909  owspan..sticky..
 00000df0: 0000 00da 094d 6170 5461 736b 6572 e914  .....MapTasker..
 00000e00: 0000 005a 0462 6f6c 6429 02da 0473 697a  ...Z.bold)...siz
-00000e10: 6572 0800 0000 2902 da04 7465 7874 5a04  er....)...textZ.
+00000e10: 6572 0800 0000 2902 da04 7465 7874 da04  er....)...text..
 00000e20: 666f 6e74 2902 7214 0000 00e9 0a00 0000  font).r.........
 00000e30: a904 720f 0000 0072 1000 0000 da04 7061  ..r....r......pa
 00000e40: 6478 da04 7061 6479 7a15 4469 7370 6c61  dx..padyz.Displa
 00000e50: 7920 4465 7461 696c 204c 6576 656c 3ada  y Detail Level:.
 00000e60: 0177 2902 7216 0000 00da 0661 6e63 686f  .w).r......ancho
-00000e70: 7229 0272 1700 0000 7201 0000 00a9 04da  r).r....r.......
+00000e70: 7229 0272 1800 0000 7201 0000 00a9 04da  r).r....r.......
 00000e80: 0130 da01 31da 0132 da01 3329 02da 0676  .0..1..2..3)...v
 00000e90: 616c 7565 73da 0763 6f6d 6d61 6e64 7209  alues..commandr.
 00000ea0: 0000 007a 1244 6973 706c 6179 2043 6f6e  ...z.Display Con
-00000eb0: 6469 7469 6f6e 7354 4629 0472 2300 0000  ditionsTF).r#...
+00000eb0: 6469 7469 6f6e 7354 4629 0472 2400 0000  ditionsTF).r$...
 00000ec0: 7216 0000 00da 076f 6e76 616c 7565 da08  r......onvalue..
-00000ed0: 6f66 6676 616c 7565 720a 0000 0072 1700  offvaluer....r..
-00000ee0: 0000 2905 720f 0000 0072 1000 0000 7219  ..).r....r....r.
-00000ef0: 0000 0072 1a00 0000 7211 0000 007a 1644  ...r....r....z.D
+00000ed0: 6f66 6676 616c 7565 720a 0000 0072 1800  offvaluer....r..
+00000ee0: 0000 2905 720f 0000 0072 1000 0000 721a  ..).r....r....r.
+00000ef0: 0000 0072 1b00 0000 7211 0000 007a 1644  ...r....r....z.D
 00000f00: 6973 706c 6179 2054 6173 6b65 724e 6574  isplay TaskerNet
 00000f10: 2049 6e66 6fe9 0400 0000 7a1a 4469 7370   Info.....z.Disp
 00000f20: 6c61 7920 5461 736b 6572 2050 7265 6665  lay Tasker Prefe
 00000f30: 7265 6e63 6573 e905 0000 007a 0723 3635  rences.....z.#65
 00000f40: 3633 6666 7a0d 5361 7665 2053 6574 7469  63ffz.Save Setti
 00000f50: 6e67 7329 04da 0c62 6f72 6465 725f 636f  ngs)...border_co
 00000f60: 6c6f 72da 0c62 6f72 6465 725f 7769 6474  lor..border_widt
-00000f70: 6872 1600 0000 7223 0000 00da 0173 7a10  hr....r#.....sz.
+00000f70: 6872 1600 0000 7224 0000 00da 0173 7a10  hr....r$.....sz.
 00000f80: 5265 7374 6f72 6520 5365 7474 696e 6773  Restore Settings
 00000f90: e907 0000 00da 016e 7a14 4755 4920 4170  .......nz.GUI Ap
 00000fa0: 7065 6172 616e 6365 204d 6f64 653a e908  pearance Mode:..
 00000fb0: 0000 0029 03da 054c 6967 6874 da04 4461  ...)...Light..Da
 00000fc0: 726b 7205 0000 0029 0472 0f00 0000 7210  rkr....).r....r.
-00000fd0: 0000 0072 1900 0000 7211 0000 007a 0723  ...r....r....z.#
+00000fd0: 0000 0072 1a00 0000 7211 0000 007a 0723  ...r....r....z.#
 00000fe0: 3234 3646 4236 7a0d 5265 7365 7420 4f70  246FB6z.Reset Op
 00000ff0: 7469 6f6e 7329 05da 066d 6173 7465 72da  tions)...master.
-00001000: 0866 675f 636f 6c6f 7272 2900 0000 7216  .fg_colorr)...r.
-00001010: 0000 0072 2300 0000 2902 7214 0000 0072  ...r#...).r....r
+00001000: 0866 675f 636f 6c6f 7272 2a00 0000 7216  .fg_colorr*...r.
+00001010: 0000 0072 2400 0000 2902 7214 0000 0072  ...r$...).r....r
 00001020: 1400 0000 5a03 5275 6e29 027a 0723 3042  ....Z.Run).z.#0B
 00001030: 4630 3735 7a07 2331 4144 3633 4429 0672  F075z.#1AD63D).r
-00001040: 3000 0000 7231 0000 0072 2900 0000 7216  0...r1...r)...r.
-00001050: 0000 0072 2300 0000 da0a 7465 7874 5f63  ...r#.....text_c
-00001060: 6f6c 6f72 5a04 4578 6974 da03 5265 64e9  olorZ.Exit..Red.
+00001040: 3100 0000 7232 0000 0072 2a00 0000 7216  1...r2...r*...r.
+00001050: 0000 0072 2400 0000 da0a 7465 7874 5f63  ...r$.....text_c
+00001060: 6f6c 6f72 da04 4578 6974 da03 5265 64e9  olor..Exit..Red.
 00001070: 6400 0000 e9fa 0000 0029 02da 0668 6569  d........)...hei
 00001080: 6768 7472 0c00 0000 2901 5a16 7363 726f  ghtr....).Z.scro
 00001090: 6c6c 6261 725f 6275 7474 6f6e 5f63 6f6c  llbar_button_col
 000010a0: 6f72 2902 7214 0000 0072 0100 0000 2902  or).r....r....).
 000010b0: 720c 0000 005a 1973 6567 6d65 6e74 6564  r....Z.segmented
 000010c0: 5f62 7574 746f 6e5f 6667 5f63 6f6c 6f72  _button_fg_color
 000010d0: 7a0d 5370 6563 6966 6963 204e 616d 65da  z.Specific Name.
 000010e0: 0643 6f6c 6f72 735a 0544 6562 7567 7a0c  .ColorsZ.Debugz.
 000010f0: 5072 6f6a 6563 7420 4e61 6d65 7a07 2331  Project Namez.#1
-00001100: 6263 3966 6629 0472 1600 0000 7223 0000  bc9ff).r....r#..
-00001110: 0072 3100 0000 7228 0000 0029 0272 1700  .r1...r(...).r..
-00001120: 0000 7217 0000 007a 0c50 726f 6669 6c65  ..r....z.Profile
+00001100: 6263 3966 6629 0472 1600 0000 7224 0000  bc9ff).r....r$..
+00001110: 0072 3200 0000 7229 0000 0029 0272 1800  .r2...r)...).r..
+00001120: 0000 7218 0000 007a 0c50 726f 6669 6c65  ..r....z.Profile
 00001130: 204e 616d 657a 0954 6173 6b20 4e61 6d65   Namez.Task Name
 00001140: 7a0f 2850 6963 6b20 4f4e 4c59 204f 6e65  z.(Pick ONLY One
 00001150: 297a 1f53 6574 2056 6172 696f 7573 2044  )z.Set Various D
 00001160: 6973 706c 6179 2043 6f6c 6f72 7320 4865  isplay Colors He
 00001170: 7265 a901 7216 0000 0029 0fda 0850 726f  re..r....)...Pro
 00001180: 6a65 6374 73da 0850 726f 6669 6c65 737a  jects..Profilesz
 00001190: 1144 6973 6162 6c65 6420 5072 6f66 696c  .Disabled Profil
@@ -288,17 +288,17 @@
 000011f0: 0d41 6374 696f 6e20 4c61 6265 6c73 7a0c  .Action Labelsz.
 00001200: 4163 7469 6f6e 204e 616d 6573 da06 5363  Action Names..Sc
 00001210: 656e 6573 da0a 4261 636b 6772 6f75 6e64  enes..Background
 00001220: da07 4275 6c6c 6574 737a 1554 6173 6b65  ..Bulletsz.Taske
 00001230: 724e 6574 2049 6e66 6f72 6d61 7469 6f6e  rNet Information
 00001240: 7a12 5461 736b 6572 2050 7265 6665 7265  z.Tasker Prefere
 00001250: 6e63 6573 7a0a 4465 6275 6720 4d6f 6465  ncesz.Debug Mode
-00001260: 2904 7216 0000 0072 2300 0000 7224 0000  ).r....r#...r$..
-00001270: 0072 2500 0000 2901 7228 0000 0029 0272  .r%...).r(...).r
-00001280: 1900 0000 721a 0000 0029 3cda 0573 7570  ....r....)<..sup
+00001260: 2904 7216 0000 0072 2400 0000 7225 0000  ).r....r$...r%..
+00001270: 0072 2600 0000 2901 7229 0000 0029 0272  .r&...).r)...).r
+00001280: 1a00 0000 721b 0000 0029 3cda 0573 7570  ....r....)<..sup
 00001290: 6572 da08 5f5f 696e 6974 5f5f da05 7469  er..__init__..ti
 000012a0: 746c 65da 0867 656f 6d65 7472 79da 1467  tle..geometry..g
 000012b0: 7269 645f 636f 6c75 6d6e 636f 6e66 6967  rid_columnconfig
 000012c0: 7572 65da 1167 7269 645f 726f 7763 6f6e  ure..grid_rowcon
 000012d0: 6669 6775 7265 da0d 6375 7374 6f6d 746b  figure..customtk
 000012e0: 696e 7465 725a 0843 546b 4672 616d 655a  interZ.CTkFrameZ
 000012f0: 0d73 6964 6562 6172 5f66 7261 6d65 da04  .sidebar_frame..
@@ -361,15 +361,15 @@
 00001680: 5f5f a900 fa77 2f55 7365 7273 2f6d 696b  __...w/Users/mik
 00001690: 7275 6269 6e2f 4c69 6272 6172 792f 436c  rubin/Library/Cl
 000016a0: 6f75 6453 746f 7261 6765 2f47 6f6f 676c  oudStorage/Googl
 000016b0: 6544 7269 7665 2d6d 696b 7275 6269 6e40  eDrive-mikrubin@
 000016c0: 676d 6169 6c2e 636f 6d2f 4d79 2044 7269  gmail.com/My Dri
 000016d0: 7665 2f50 7974 686f 6e2f 6d61 7074 6173  ve/Python/maptas
 000016e0: 6b65 722f 6d61 7074 6173 6b65 722f 7372  ker/maptasker/sr
-000016f0: 632f 7573 6572 696e 7472 2e70 7972 4000  c/userintr.pyr@.
+000016f0: 632f 7573 6572 696e 7472 2e70 7972 4200  c/userintr.pyrB.
 00001700: 0000 3c00 0000 7362 0100 000a 010a 030a  ..<...sb........
 00001710: 010e 030e 010e 0112 0314 0110 0204 0104  ................
 00001720: 0102 010c 0108 fd14 0504 0308 0108 ff14  ................
 00001730: 0304 0104 0106 0104 0108 fd14 0504 0304  ................
 00001740: 0104 0102 0102 0102 0108 fb16 0704 0304  ................
 00001750: 0104 0102 0102 0102 0108 fb06 070a 0106  ................
 00001760: ff04 0504 0104 0102 0102 0102 0108 fb06  ................
@@ -398,80 +398,80 @@
 000018d0: 005f 0404 007c 005f 0504 007c 005f 0604  ._...|._...|._..
 000018e0: 007c 005f 0704 007c 005f 0804 007c 005f  .|._...|._...|._
 000018f0: 0904 007c 005f 0a7c 005f 0b64 0604 007c  ...|._.|._.d...|
 00001900: 005f 0c04 007c 005f 0d7c 005f 0e64 077c  ._...|._.|._.d.|
 00001910: 005f 0f7c 006a 10a0 0264 08a1 0101 0067  ._.|.j...d.....g
 00001920: 007c 005f 1164 087c 005f 127c 0172 4d7c  .|._.d.|._.|.rM|
 00001930: 006a 13a0 1464 0964 0a74 1517 00a1 0201  .j...d.d.t......
-00001940: 0069 007c 005f 1664 0053 0029 0b4e 721d  .i.|._.d.S.).Nr.
-00001950: 0000 0029 0172 2200 0000 721f 0000 0072  ...).r"...r....r
+00001940: 0069 007c 005f 1664 0053 0029 0b4e 721e  .i.|._.d.S.).Nr.
+00001950: 0000 0029 0172 2300 0000 7220 0000 0072  ...).r#...r ...r
 00001960: 0700 0000 46da 0072 0900 0000 7205 0000  ....F..r....r...
 00001970: 00fa 0330 2e30 7a10 4d61 7054 6173 6b65  ...0.0z.MapTaske
-00001980: 7220 4865 6c70 0a0a 2917 7249 0000 0072  r Help..).rI...r
-00001990: 5900 0000 da03 7365 74da 1464 6973 706c  Y.....set..displ
+00001980: 7220 4865 6c70 0a0a 2917 724b 0000 0072  r Help..).rK...r
+00001990: 5b00 0000 da03 7365 74da 1464 6973 706c  [.....set..displ
 000019a0: 6179 5f64 6574 6169 6c5f 6c65 7665 6cda  ay_detail_level.
 000019b0: 1a64 6973 706c 6179 5f70 726f 6669 6c65  .display_profile
 000019c0: 5f63 6f6e 6469 7469 6f6e 73da 1364 6973  _conditions..dis
 000019d0: 706c 6179 5f70 7265 6665 7265 6e63 6573  play_preferences
 000019e0: da11 6469 7370 6c61 795f 7461 736b 6572  ..display_tasker
 000019f0: 6e65 74da 0564 6562 7567 5a0e 636c 6561  net..debugZ.clea
 00001a00: 725f 7365 7474 696e 6773 da05 7265 7365  r_settings..rese
 00001a10: 74da 0465 7869 74da 0a67 6f5f 7072 6f67  t..exit..go_prog
 00001a20: 7261 6dda 1373 696e 676c 655f 7072 6f6a  ram..single_proj
 00001a30: 6563 745f 6e61 6d65 da13 7369 6e67 6c65  ect_name..single
 00001a40: 5f70 726f 6669 6c65 5f6e 616d 65da 1073  _profile_name..s
 00001a50: 696e 676c 655f 7461 736b 5f6e 616d 65da  ingle_task_name.
 00001a60: 0e63 6f6c 6f72 5f74 6578 745f 726f 7772  .color_text_rowr
-00001a70: 5300 0000 da0c 636f 6c6f 725f 6c61 6265  S.....color_labe
+00001a70: 5500 0000 da0c 636f 6c6f 725f 6c61 6265  U.....color_labe
 00001a80: 6c73 da0f 6170 7065 6172 616e 6365 5f6d  ls..appearance_m
-00001a90: 6f64 6572 5800 0000 da06 696e 7365 7274  oderX.....insert
+00001a90: 6f64 6572 5a00 0000 da06 696e 7365 7274  oderZ.....insert
 00001aa0: da09 494e 464f 5f54 4558 54da 0c63 6f6c  ..INFO_TEXT..col
-00001ab0: 6f72 5f6c 6f6f 6b75 7029 0272 6900 0000  or_lookup).ri...
-00001ac0: 726e 0000 0072 6c00 0000 726c 0000 0072  rn...rl...rl...r
-00001ad0: 6d00 0000 7267 0000 002f 0100 0073 3000  m...rg.../...s0.
+00001ab0: 6f72 5f6c 6f6f 6b75 7029 0272 6b00 0000  or_lookup).rk...
+00001ac0: 7270 0000 0072 6e00 0000 726e 0000 0072  rp...rn...rn...r
+00001ad0: 6f00 0000 7269 0000 002f 0100 0073 3000  o...ri.../...s0.
 00001ae0: 0000 1201 0c01 0601 0207 08fa 0401 02ff  ................
 00001af0: 0403 02fd 0405 02fb 0406 02fa 0406 02fa  ................
 00001b00: 0806 1201 0601 0c01 0601 0601 0401 1201  ................
 00001b10: 0a01 7a12 4d79 4775 692e 7365 745f 6465  ..z.MyGui.set_de
 00001b20: 6661 756c 7473 6302 0000 0000 0000 0000  faultsc.........
 00001b30: 0000 0002 0000 0006 0000 0043 0000 0073  ...........C...s
 00001b40: 5000 0000 7400 6a01 7c00 6401 6402 8d02  P...t.j.|.d.d...
 00001b50: 7c00 5f02 7c00 6a02 6a03 6403 6404 6405  |._.|.j.j.d.d.d.
 00001b60: 6405 6406 8d04 0100 7c00 6a02 a004 6407  d.d.....|.j...d.
 00001b70: 7c01 a102 0100 7c00 6a02 6a05 6408 6409  |.....|.j.j.d.d.
 00001b80: 640a 8d02 0100 7c00 6a02 a006 a100 0100  d.....|.j.......
-00001b90: 6400 5300 290b 4e72 3500 0000 a901 720c  d.S.).Nr5.....r.
-00001ba0: 0000 0072 2600 0000 7209 0000 0072 1400  ...r&...r....r..
-00001bb0: 0000 7218 0000 0072 7000 0000 da08 6469  ..r....rp.....di
-00001bc0: 7361 626c 6564 7233 0000 00a9 02da 0573  sabledr3.......s
-00001bd0: 7461 7465 7232 0000 00a9 0772 4500 0000  tater2.....rE...
-00001be0: 7257 0000 0072 5800 0000 7246 0000 0072  rW...rX...rF...r
-00001bf0: 8000 0000 7259 0000 00da 0966 6f63 7573  ....rY.....focus
-00001c00: 5f73 6574 2902 7269 0000 00da 0d65 7272  _set).ri.....err
-00001c10: 6f72 5f6d 6573 7361 6765 726c 0000 0072  or_messagerl...r
-00001c20: 6c00 0000 726d 0000 00da 1164 6973 706c  l...rm.....displ
+00001b90: 6400 5300 290b 4e72 3700 0000 a901 720c  d.S.).Nr7.....r.
+00001ba0: 0000 0072 2700 0000 7209 0000 0072 1400  ...r'...r....r..
+00001bb0: 0000 7219 0000 0072 7200 0000 da08 6469  ..r....rr.....di
+00001bc0: 7361 626c 6564 7235 0000 00a9 02da 0573  sabledr5.......s
+00001bd0: 7461 7465 7233 0000 00a9 0772 4700 0000  tater3.....rG...
+00001be0: 7259 0000 0072 5a00 0000 7248 0000 0072  rY...rZ...rH...r
+00001bf0: 8200 0000 725b 0000 00da 0966 6f63 7573  ....r[.....focus
+00001c00: 5f73 6574 2902 726b 0000 00da 0d65 7272  _set).rk.....err
+00001c10: 6f72 5f6d 6573 7361 6765 726e 0000 0072  or_messagern...r
+00001c20: 6e00 0000 726f 0000 00da 1164 6973 706c  n...ro.....displ
 00001c30: 6179 5f65 7272 6f72 5f62 6f78 4601 0000  ay_error_boxF...
 00001c40: 730e 0000 0010 0114 010e 0106 0104 0106  s...............
 00001c50: ff0e 037a 174d 7947 7569 2e64 6973 706c  ...z.MyGui.displ
 00001c60: 6179 5f65 7272 6f72 5f62 6f78 6303 0000  ay_error_boxc...
 00001c70: 0000 0000 0000 0000 0004 0000 0006 0000  ................
 00001c80: 0043 0000 0073 6200 0000 7c02 7204 6401  .C...sb...|.r.d.
 00001c90: 6e01 6402 7d03 7400 6a01 7c00 6403 6404  n.d.}.t.j.|.d.d.
 00001ca0: 8d02 7c00 5f02 7c00 6a02 6a03 6405 6406  ..|._.|.j.j.d.d.
 00001cb0: 6407 6407 6408 8d04 0100 7c00 6a02 a004  d.d.d.....|.j...
 00001cc0: 6409 7c01 9b00 640a 9d02 a102 0100 7c00  d.|...d.......|.
 00001cd0: 6a02 6a05 640b 7c03 640c 8d02 0100 7c00  j.j.d.|.d.....|.
 00001ce0: 6a02 a006 a100 0100 6400 5300 290d 4eda  j.......d.S.).N.
-00001cf0: 0547 7265 656e 7233 0000 0069 5802 0000  .Greenr3...iX...
-00001d00: 7283 0000 0072 2600 0000 7207 0000 0072  r....r&...r....r
-00001d10: 1400 0000 7218 0000 0072 7000 0000 da01  ....r....rp.....
-00001d20: 0a72 8400 0000 7285 0000 0072 8700 0000  .r....r....r....
-00001d30: 2904 7269 0000 00da 076d 6573 7361 6765  ).ri.....message
-00001d40: 5a04 676f 6f64 da05 636f 6c6f 7272 6c00  Z.good..colorrl.
-00001d50: 0000 726c 0000 0072 6d00 0000 da13 6469  ..rl...rm.....di
+00001cf0: 0547 7265 656e 7235 0000 0069 5802 0000  .Greenr5...iX...
+00001d00: 7285 0000 0072 2700 0000 7207 0000 0072  r....r'...r....r
+00001d10: 1400 0000 7219 0000 0072 7200 0000 da01  ....r....rr.....
+00001d20: 0a72 8600 0000 7287 0000 0072 8900 0000  .r....r....r....
+00001d30: 2904 726b 0000 00da 076d 6573 7361 6765  ).rk.....message
+00001d40: 5a04 676f 6f64 da05 636f 6c6f 7272 6e00  Z.good..colorrn.
+00001d50: 0000 726e 0000 0072 6f00 0000 da13 6469  ..rn...ro.....di
 00001d60: 7370 6c61 795f 6d65 7373 6167 655f 626f  splay_message_bo
 00001d70: 7852 0100 0073 1000 0000 0c01 1001 1401  xR...s..........
 00001d80: 1401 0601 0401 06ff 0e03 7a19 4d79 4775  ..........z.MyGu
 00001d90: 692e 6469 7370 6c61 795f 6d65 7373 6167  i.display_messag
 00001da0: 655f 626f 7863 0300 0000 0000 0000 0000  e_boxc..........
 00001db0: 0000 0400 0000 0600 0000 4300 0000 738c  ..........C...s.
 00001dc0: 0000 0064 017d 037c 0173 0d64 027c 0217  ...d.}.|.s.d.|..
@@ -479,15 +479,15 @@
 00001de0: 0172 167c 006a 0272 1664 057d 036e 117c  .r.|.j.r.d.}.n.|
 00001df0: 006a 0172 1f7c 006a 0372 1f64 067d 036e  .j.r.|.j.r.d.}.n
 00001e00: 087c 006a 0272 277c 006a 0372 2764 077d  .|.j.r'|.j.r'd.}
 00001e10: 037c 0372 387c 00a0 047c 03a1 0101 0064  .|.r8|...|.....d
 00001e20: 085c 037c 005f 017c 005f 027c 005f 0364  .\.|._.|._.|._.d
 00001e30: 0053 007c 00a0 0564 097c 019b 0064 0a7c  .S.|...d.|...d.|
 00001e40: 029b 009d 0464 0ba1 0201 0064 0053 0029  .....d.....d.S.)
-00001e50: 0c4e 726f 0000 007a 2145 7272 6f72 3a0a  .Nro...z!Error:.
+00001e50: 0c4e 7271 0000 007a 2145 7272 6f72 3a0a  .Nrq...z!Error:.
 00001e60: 0a54 6865 206e 616d 6520 656e 7465 7265  .The name entere
 00001e70: 6420 666f 7220 7468 6520 7a16 2069 7320  d for the z. is 
 00001e80: 626c 616e 6b21 0a0a 5472 7920 6167 6169  blank!..Try agai
 00001e90: 6e2e 467a 5b45 7272 6f72 3a0a 0a59 6f75  n.Fz[Error:..You
 00001ea0: 2068 6176 6520 656e 7465 7265 6420 626f   have entered bo
 00001eb0: 7468 2061 2050 726f 6a65 6374 2061 6e64  th a Project and
 00001ec0: 2061 2050 726f 6669 6c65 206e 616d 6521   a Profile name!
@@ -500,165 +500,165 @@
 00001f30: 6167 6169 6e20 616e 6420 6f6e 6c79 2073  again and only s
 00001f40: 656c 6563 7420 6f6e 652e 7a58 4572 726f  elect one.zXErro
 00001f50: 723a 0a0a 596f 7520 6861 7665 2065 6e74  r:..You have ent
 00001f60: 6572 6564 2062 6f74 6820 6120 5072 6f66  ered both a Prof
 00001f70: 696c 6520 616e 6420 6120 5461 736b 206e  ile and a Task n
 00001f80: 616d 6521 0a0a 5472 7920 6167 6169 6e20  ame!..Try again 
 00001f90: 616e 6420 6f6e 6c79 2073 656c 6563 7420  and only select 
-00001fa0: 6f6e 652e 2903 726f 0000 0072 6f00 0000  one.).ro...ro...
-00001fb0: 726f 0000 007a 1244 6973 706c 6179 206f  ro...z.Display o
+00001fa0: 6f6e 652e 2903 7271 0000 0072 7100 0000  one.).rq...rq...
+00001fb0: 7271 0000 007a 1244 6973 706c 6179 206f  rq...z.Display o
 00001fc0: 6e6c 7920 7468 6520 277a 0227 2054 2906  nly the 'z.' T).
-00001fd0: 5a0a 6e61 6d65 645f 6974 656d 727a 0000  Z.named_itemrz..
-00001fe0: 0072 7b00 0000 727c 0000 0072 8a00 0000  .r{...r|...r....
-00001ff0: 728f 0000 0029 0472 6900 0000 da08 7468  r....).ri.....th
-00002000: 655f 6e61 6d65 5a0c 656c 656d 656e 745f  e_nameZ.element_
-00002010: 6e61 6d65 7289 0000 0072 6c00 0000 726c  namer....rl...rl
-00002020: 0000 0072 6d00 0000 da0a 6368 6563 6b5f  ...rm.....check_
+00001fd0: 5a0a 6e61 6d65 645f 6974 656d 727c 0000  Z.named_itemr|..
+00001fe0: 0072 7d00 0000 727e 0000 0072 8c00 0000  .r}...r~...r....
+00001ff0: 7291 0000 0029 0472 6b00 0000 da08 7468  r....).rk.....th
+00002000: 655f 6e61 6d65 da0c 656c 656d 656e 745f  e_name..element_
+00002010: 6e61 6d65 728b 0000 0072 6e00 0000 726e  namer....rn...rn
+00002020: 0000 0072 6f00 0000 da0a 6368 6563 6b5f  ...ro.....check_
 00002030: 6e61 6d65 5f01 0000 7338 0000 0004 0104  name_...s8......
 00002040: 0102 0202 0102 ff02 0202 fe02 ff06 050c  ................
 00002050: 0102 0204 ff0c 0402 0204 ff0c 0402 0202  ................
 00002060: ff04 050a 0102 0502 fc04 0104 0108 0104  ................
 00002070: 0310 0108 ff7a 104d 7947 7569 2e63 6865  .....z.MyGui.che
 00002080: 636b 5f6e 616d 6563 0100 0000 0000 0000  ck_namec........
 00002090: 0000 0000 0300 0000 0400 0000 4300 0000  ............C...
 000020a0: f34c 0000 0064 017d 017c 00a0 007c 01a1  .L...d.}.|...|..
 000020b0: 0101 007c 006a 01a0 02a1 0001 007c 006a  ...|.j.......|.j
 000020c0: 03a0 02a1 0001 0074 046a 0564 0264 0364  .......t.j.d.d.d
 000020d0: 048d 027d 027c 02a0 06a1 007c 005f 077c  ...}.|.....|._.|
 000020e0: 00a0 087c 006a 0764 05a1 0201 0064 0053  ...|.j.d.....d.S
-000020f0: 0029 064e 726f 0000 007a 1345 6e74 6572  .).Nro...z.Enter
+000020f0: 0029 064e 7271 0000 007a 1345 6e74 6572  .).Nrq...z.Enter
 00002100: 2050 726f 6a65 6374 206e 616d 653a 7a18   Project name:z.
 00002110: 4469 7370 6c61 7920 5370 6563 6966 6963  Display Specific
 00002120: 2050 726f 6a65 6374 a902 7216 0000 0072   Project..r....r
-00002130: 4100 0000 da07 5072 6f6a 6563 7429 0972  A.....Project).r
-00002140: 8a00 0000 7260 0000 00da 0864 6573 656c  ....r`.....desel
-00002150: 6563 7472 6200 0000 7245 0000 00da 0e43  ectrb...rE.....C
+00002130: 4300 0000 da07 5072 6f6a 6563 7429 0972  C.....Project).r
+00002140: 8c00 0000 7262 0000 00da 0864 6573 656c  ....rb.....desel
+00002150: 6563 7472 6400 0000 7247 0000 00da 0e43  ectrd...rG.....C
 00002160: 546b 496e 7075 7444 6961 6c6f 67da 0967  TkInputDialog..g
-00002170: 6574 5f69 6e70 7574 727a 0000 0072 9100  et_inputrz...r..
-00002180: 0000 a903 7269 0000 0072 8900 0000 da06  ....ri...r......
-00002190: 6469 616c 6f67 726c 0000 0072 6c00 0000  dialogrl...rl...
-000021a0: 726d 0000 0072 5d00 0000 8701 0000 f312  rm...r].........
+00002170: 6574 5f69 6e70 7574 727c 0000 0072 9400  et_inputr|...r..
+00002180: 0000 a903 726b 0000 0072 8b00 0000 da06  ....rk...r......
+00002190: 6469 616c 6f67 726e 0000 0072 6e00 0000  dialogrn...rn...
+000021a0: 726f 0000 0072 5f00 0000 8701 0000 f312  ro...r_.........
 000021b0: 0000 0004 020a 010a 020a 0104 0204 0106  ................
 000021c0: ff0a 0412 027a 1f4d 7947 7569 2e73 696e  .....z.MyGui.sin
 000021d0: 676c 655f 7072 6f6a 6563 745f 6e61 6d65  gle_project_name
 000021e0: 5f65 7665 6e74 6301 0000 0000 0000 0000  _eventc.........
 000021f0: 0000 0003 0000 0004 0000 0043 0000 0072  ...........C...r
-00002200: 9200 0000 2906 4e72 6f00 0000 7a13 456e  ....).Nro...z.En
+00002200: 9500 0000 2906 4e72 7100 0000 7a13 456e  ....).Nrq...z.En
 00002210: 7465 7220 5072 6f66 696c 6520 6e61 6d65  ter Profile name
 00002220: 3a7a 1844 6973 706c 6179 2053 7065 6369  :z.Display Speci
-00002230: 6669 6320 5072 6f66 696c 6572 9300 0000  fic Profiler....
-00002240: da07 5072 6f66 696c 6529 0972 8a00 0000  ..Profile).r....
-00002250: 725e 0000 0072 9500 0000 7262 0000 0072  r^...r....rb...r
-00002260: 4500 0000 7296 0000 0072 9700 0000 727b  E...r....r....r{
-00002270: 0000 0072 9100 0000 7298 0000 0072 6c00  ...r....r....rl.
-00002280: 0000 726c 0000 0072 6d00 0000 725f 0000  ..rl...rm...r_..
-00002290: 009a 0100 0072 9a00 0000 7a1f 4d79 4775  .....r....z.MyGu
+00002230: 6669 6320 5072 6f66 696c 6572 9600 0000  fic Profiler....
+00002240: da07 5072 6f66 696c 6529 0972 8c00 0000  ..Profile).r....
+00002250: 7260 0000 0072 9800 0000 7264 0000 0072  r`...r....rd...r
+00002260: 4700 0000 7299 0000 0072 9a00 0000 727d  G...r....r....r}
+00002270: 0000 0072 9400 0000 729b 0000 0072 6e00  ...r....r....rn.
+00002280: 0000 726e 0000 0072 6f00 0000 7261 0000  ..rn...ro...ra..
+00002290: 009a 0100 0072 9d00 0000 7a1f 4d79 4775  .....r....z.MyGu
 000022a0: 692e 7369 6e67 6c65 5f70 726f 6669 6c65  i.single_profile
 000022b0: 5f6e 616d 655f 6576 656e 7463 0100 0000  _name_eventc....
 000022c0: 0000 0000 0000 0000 0300 0000 0400 0000  ................
-000022d0: 4300 0000 7292 0000 0029 064e 726f 0000  C...r....).Nro..
+000022d0: 4300 0000 7295 0000 0029 064e 7271 0000  C...r....).Nrq..
 000022e0: 007a 1045 6e74 6572 2054 6173 6b20 6e61  .z.Enter Task na
 000022f0: 6d65 3a7a 1544 6973 706c 6179 2053 7065  me:z.Display Spe
-00002300: 6369 6669 6320 5461 736b 7293 0000 00da  cific Taskr.....
-00002310: 0454 6173 6b29 0972 8a00 0000 725e 0000  .Task).r....r^..
-00002320: 0072 9500 0000 7260 0000 0072 4500 0000  .r....r`...rE...
-00002330: 7296 0000 0072 9700 0000 727c 0000 0072  r....r....r|...r
-00002340: 9100 0000 7298 0000 0072 6c00 0000 726c  ....r....rl...rl
-00002350: 0000 0072 6d00 0000 7261 0000 00ad 0100  ...rm...ra......
-00002360: 0072 9a00 0000 7a1c 4d79 4775 692e 7369  .r....z.MyGui.si
+00002300: 6369 6669 6320 5461 736b 7296 0000 00da  cific Taskr.....
+00002310: 0454 6173 6b29 0972 8c00 0000 7260 0000  .Task).r....r`..
+00002320: 0072 9800 0000 7262 0000 0072 4700 0000  .r....rb...rG...
+00002330: 7299 0000 0072 9a00 0000 727e 0000 0072  r....r....r~...r
+00002340: 9400 0000 729b 0000 0072 6e00 0000 726e  ....r....rn...rn
+00002350: 0000 0072 6f00 0000 7263 0000 00ad 0100  ...ro...rc......
+00002360: 0072 9d00 0000 7a1c 4d79 4775 692e 7369  .r....z.MyGui.si
 00002370: 6e67 6c65 5f74 6173 6b5f 6e61 6d65 5f65  ngle_task_name_e
 00002380: 7665 6e74 da13 6e65 775f 6170 7065 6172  vent..new_appear
 00002390: 616e 6365 5f6d 6f64 6563 0200 0000 0000  ance_modec......
 000023a0: 0000 0000 0000 0200 0000 0300 0000 4300  ..............C.
 000023b0: 0000 7314 0000 0074 00a0 017c 01a1 0101  ..s....t...|....
 000023c0: 007c 017c 005f 0264 0053 00a9 014e 2903  .|.|._.d.S...N).
-000023d0: 7245 0000 00da 1373 6574 5f61 7070 6561  rE.....set_appea
-000023e0: 7261 6e63 655f 6d6f 6465 727f 0000 0029  rance_moder....)
-000023f0: 0272 6900 0000 729d 0000 0072 6c00 0000  .ri...r....rl...
-00002400: 726c 0000 0072 6d00 0000 7252 0000 00c0  rl...rm...rR....
+000023d0: 7247 0000 00da 1373 6574 5f61 7070 6561  rG.....set_appea
+000023e0: 7261 6e63 655f 6d6f 6465 7281 0000 0029  rance_moder....)
+000023f0: 0272 6b00 0000 72a0 0000 0072 6e00 0000  .rk...r....rn...
+00002400: 726e 0000 0072 6f00 0000 7254 0000 00c0  rn...ro...rT....
 00002410: 0100 0073 0400 0000 0a01 0a01 7a22 4d79  ...s........z"My
 00002420: 4775 692e 6368 616e 6765 5f61 7070 6561  Gui.change_appea
 00002430: 7261 6e63 655f 6d6f 6465 5f65 7665 6e74  rance_mode_event
 00002440: da0e 6469 7370 6c61 795f 6465 7461 696c  ..display_detail
 00002450: 6302 0000 0000 0000 0000 0000 0002 0000  c...............
 00002460: 0002 0000 0043 0000 0073 0a00 0000 7c01  .....C...s....|.
-00002470: 7c00 5f00 6400 5300 729e 0000 0029 0172  |._.d.S.r....).r
-00002480: 7200 0000 2902 7269 0000 0072 a000 0000  r...).ri...r....
-00002490: 726c 0000 0072 6c00 0000 726d 0000 0072  rl...rl...rm...r
-000024a0: 4800 0000 c701 0000 7302 0000 000a 017a  H.......s......z
+00002470: 7c00 5f00 6400 5300 72a1 0000 0029 0172  |._.d.S.r....).r
+00002480: 7400 0000 2902 726b 0000 0072 a300 0000  t...).rk...r....
+00002490: 726e 0000 0072 6e00 0000 726f 0000 0072  rn...rn...ro...r
+000024a0: 4a00 0000 c701 0000 7302 0000 000a 017a  J.......s......z
 000024b0: 1b4d 7947 7569 2e64 6574 6169 6c5f 7365  .MyGui.detail_se
 000024c0: 6c65 6374 6564 5f65 7665 6e74 da13 636f  lected_event..co
 000024d0: 6c6f 725f 7365 6c65 6374 6564 5f69 7465  lor_selected_ite
 000024e0: 6d63 0200 0000 0000 0000 0000 0000 0500  mc..............
 000024f0: 0000 0700 0000 4300 0000 7396 0000 0074  ......C...s....t
 00002500: 0083 007d 027c 02a0 01a1 007d 037c 0364  ...}.|.....}.|.d
 00002510: 0075 0172 497c 006a 027d 047c 037c 006a  .u.rI|.j.}.|.|.j
 00002520: 0374 047c 0119 003c 007c 006a 05a0 0674  .t.|...<.|.j...t
 00002530: 076a 087c 006a 09a0 0a64 01a1 017c 019b  .j.|.j...d...|..
 00002540: 0064 029d 027c 0364 038d 03a1 0101 007c  .d...|.d.......|
 00002550: 006a 0564 0419 006a 0b7c 006a 0264 0564  .j.d...j.|.j.d.d
 00002560: 0564 0564 068d 0401 007c 0004 006a 0264  .d.d.....|...j.d
 00002570: 0737 0002 005f 027c 00a0 0c7c 019b 0064  .7..._.|...|...d
 00002580: 087c 039b 009d 0364 09a1 0201 0064 0053  .|.....d.....d.S
-00002590: 0064 0053 0029 0a4e 7237 0000 007a 0920  .d.S.).Nr7...z. 
+00002590: 0064 0053 0029 0a4e 7239 0000 007a 0920  .d.S.).Nr9...z. 
 000025a0: 3c3c 2063 6f6c 6f72 2902 7216 0000 0072  << color).r....r
-000025b0: 3200 0000 e9ff ffff ff72 0100 0000 7218  2........r....r.
+000025b0: 3300 0000 e9ff ffff ff72 0100 0000 7219  3........r....r.
 000025c0: 0000 0072 0700 0000 7a12 2063 6f6c 6f72  ...r....z. color
 000025d0: 2063 6861 6e67 6564 2074 6f20 5429 0d72   changed to T).r
-000025e0: 0200 0000 da03 6765 7472 7d00 0000 7282  ......getr}...r.
-000025f0: 0000 0072 0400 0000 727e 0000 00da 0661  ...r....r~.....a
-00002600: 7070 656e 6472 4500 0000 7247 0000 0072  ppendrE...rG...r
-00002610: 5a00 0000 725c 0000 0072 4600 0000 728f  Z...r\...rF...r.
-00002620: 0000 0029 0572 6900 0000 72a1 0000 005a  ...).ri...r....Z
-00002630: 0a70 6963 6b5f 636f 6c6f 7272 8e00 0000  .pick_colorr....
-00002640: 720f 0000 0072 6c00 0000 726c 0000 0072  r....rl...rl...r
-00002650: 6d00 0000 7263 0000 00cd 0100 0073 2a00  m...rc.......s*.
+000025e0: 0200 0000 da03 6765 7472 7f00 0000 7284  ......getr....r.
+000025f0: 0000 0072 0400 0000 7280 0000 00da 0661  ...r....r......a
+00002600: 7070 656e 6472 4700 0000 7249 0000 0072  ppendrG...rI...r
+00002610: 5c00 0000 725e 0000 0072 4800 0000 7291  \...r^...rH...r.
+00002620: 0000 0029 0572 6b00 0000 72a4 0000 005a  ...).rk...r....Z
+00002630: 0a70 6963 6b5f 636f 6c6f 7272 9000 0000  .pick_colorr....
+00002640: 720f 0000 0072 6e00 0000 726e 0000 0072  r....rn...rn...r
+00002650: 6f00 0000 7265 0000 00cd 0100 0073 2a00  o...re.......s*.
 00002660: 0000 0602 0801 0801 0601 0202 0cff 0603  ................
 00002670: 0401 0a01 0801 0201 04fd 04ff 0a07 0a01  ................
 00002680: 06ff 0e03 0401 0e01 08ff 04f0 7a12 4d79  ............z.My
 00002690: 4775 692e 636f 6c6f 7273 5f65 7665 6e74  Gui.colors_event
 000026a0: 6301 0000 0000 0000 0000 0000 0001 0000  c...............
 000026b0: 0002 0000 0043 0000 00f3 1000 0000 7c00  .....C........|.
-000026c0: 6a00 a001 a100 7c00 5f02 6400 5300 729e  j.....|._.d.S.r.
-000026d0: 0000 0029 0372 4b00 0000 72a3 0000 0072  ...).rK...r....r
-000026e0: 7300 0000 7268 0000 0072 6c00 0000 726c  s...rh...rl...rl
-000026f0: 0000 0072 6d00 0000 724a 0000 00e8 0100  ...rm...rJ......
+000026c0: 6a00 a001 a100 7c00 5f02 6400 5300 72a1  j.....|._.d.S.r.
+000026d0: 0000 0029 0372 4d00 0000 72a6 0000 0072  ...).rM...r....r
+000026e0: 7500 0000 726a 0000 0072 6e00 0000 726e  u...rj...rn...rn
+000026f0: 0000 0072 6f00 0000 724c 0000 00e8 0100  ...ro...rL......
 00002700: 00f3 0200 0000 1001 7a15 4d79 4775 692e  ........z.MyGui.
 00002710: 636f 6e64 6974 696f 6e5f 6576 656e 7463  condition_eventc
 00002720: 0100 0000 0000 0000 0000 0000 0100 0000  ................
-00002730: 0200 0000 4300 0000 72a5 0000 0072 9e00  ....C...r....r..
-00002740: 0000 2903 724f 0000 0072 a300 0000 7274  ..).rO...r....rt
-00002750: 0000 0072 6800 0000 726c 0000 0072 6c00  ...rh...rl...rl.
-00002760: 0000 726d 0000 0072 4e00 0000 ee01 0000  ..rm...rN.......
-00002770: 72a6 0000 007a 1f4d 7947 7569 2e64 6973  r....z.MyGui.dis
+00002730: 0200 0000 4300 0000 72a8 0000 0072 a100  ....C...r....r..
+00002740: 0000 2903 7251 0000 0072 a600 0000 7276  ..).rQ...r....rv
+00002750: 0000 0072 6a00 0000 726e 0000 0072 6e00  ...rj...rn...rn.
+00002760: 0000 726f 0000 0072 5000 0000 ee01 0000  ..ro...rP.......
+00002770: 72a9 0000 007a 1f4d 7947 7569 2e64 6973  r....z.MyGui.dis
 00002780: 706c 6179 5f70 7265 6665 7265 6e63 6573  play_preferences
 00002790: 5f65 7665 6e74 6301 0000 0000 0000 0000  _eventc.........
 000027a0: 0000 0001 0000 0002 0000 0043 0000 0072  ...........C...r
-000027b0: a500 0000 729e 0000 0029 0372 4d00 0000  ....r....).rM...
-000027c0: 72a3 0000 0072 7500 0000 7268 0000 0072  r....ru...rh...r
-000027d0: 6c00 0000 726c 0000 0072 6d00 0000 724c  l...rl...rm...rL
-000027e0: 0000 00f4 0100 0072 a600 0000 7a1d 4d79  .......r....z.My
+000027b0: a800 0000 72a1 0000 0029 0372 4f00 0000  ....r....).rO...
+000027c0: 72a6 0000 0072 7700 0000 726a 0000 0072  r....rw...rj...r
+000027d0: 6e00 0000 726e 0000 0072 6f00 0000 724e  n...rn...ro...rN
+000027e0: 0000 00f4 0100 0072 a900 0000 7a1d 4d79  .......r....z.My
 000027f0: 4775 692e 6469 7370 6c61 795f 7461 736b  Gui.display_task
 00002800: 6572 6e65 745f 6576 656e 7463 0100 0000  ernet_eventc....
 00002810: 0000 0000 0000 0000 0200 0000 0900 0000  ................
 00002820: 4300 0000 734a 0000 007c 006a 007c 006a  C...sJ...|.j.|.j
 00002830: 017c 006a 027c 006a 037c 006a 047c 006a  .|.j.|.j.|.j.|.j
 00002840: 057c 006a 067c 006a 0764 019c 087d 0174  .|.j.|.j.d...}.t
 00002850: 0864 027c 006a 097c 0183 035c 027d 017c  .d.|.j.|...\.}.|
 00002860: 005f 097c 00a0 0a64 0364 02a1 0201 0064  ._.|...d.d.....d
-00002870: 0053 0029 044e 2908 7272 0000 0072 7300  .S.).N).rr...rs.
-00002880: 0000 7274 0000 0072 7500 0000 727a 0000  ..rt...ru...rz..
-00002890: 0072 7b00 0000 727c 0000 0072 7600 0000  .r{...r|...rv...
+00002870: 0053 0029 044e 2908 7274 0000 0072 7500  .S.).N).rt...ru.
+00002880: 0000 7276 0000 0072 7700 0000 727c 0000  ..rv...rw...r|..
+00002890: 0072 7d00 0000 727e 0000 0072 7800 0000  .r}...r~...rx...
 000028a0: 547a 0f53 6574 7469 6e67 7320 7361 7665  Tz.Settings save
-000028b0: 642e 290b 7272 0000 0072 7300 0000 7274  d.).rr...rs...rt
-000028c0: 0000 0072 7500 0000 727a 0000 0072 7b00  ...ru...rz...r{.
-000028d0: 0000 727c 0000 0072 7600 0000 7203 0000  ..r|...rv...r...
-000028e0: 0072 8200 0000 728f 0000 0029 0272 6900  .r....r....).ri.
-000028f0: 0000 da09 7465 6d70 5f61 7267 7372 6c00  ....temp_argsrl.
-00002900: 0000 726c 0000 0072 6d00 0000 7250 0000  ..rl...rm...rP..
+000028b0: 642e 290b 7274 0000 0072 7500 0000 7276  d.).rt...ru...rv
+000028c0: 0000 0072 7700 0000 727c 0000 0072 7d00  ...rw...r|...r}.
+000028d0: 0000 727e 0000 0072 7800 0000 7203 0000  ..r~...rx...r...
+000028e0: 0072 8400 0000 7291 0000 0029 0272 6b00  .r....r....).rk.
+000028f0: 0000 da09 7465 6d70 5f61 7267 7372 6e00  ....temp_argsrn.
+00002900: 0000 726e 0000 0072 6f00 0000 7252 0000  ..rn...ro...rR..
 00002910: 00fa 0100 0073 1a00 0000 0402 0401 0401  .....s..........
 00002920: 0401 0401 0401 0401 0401 06f8 020a 0801  ................
 00002930: 0aff 1003 7a19 4d79 4775 692e 7361 7665  ....z.MyGui.save
 00002940: 5f73 6574 7469 6e67 735f 6576 656e 7463  _settings_eventc
 00002950: 0300 0000 0000 0000 0000 0000 0400 0000  ................
 00002960: 0400 0000 4300 0000 7344 0100 0064 017d  ....C...sD...d.}
 00002970: 037c 0104 0064 026b 0272 1801 007c 0272  .|...d.k.r...|.r
@@ -677,28 +677,28 @@
 00002a40: 7701 007c 0272 757c 039b 0064 087c 029b  w..|.ru|...d.|..
 00002a50: 0064 099d 047d 037c 0353 0004 0064 0a6b  .d...}.|.S...d.k
 00002a60: 0272 8801 007c 0272 867c 039b 0064 0b7c  .r...|.r.|...d.|
 00002a70: 029b 0064 099d 047d 037c 0353 0064 0c6b  ...d...}.|.S.d.k
 00002a80: 0272 977c 0272 957c 039b 0064 0d7c 029b  .r.|.r.|...d.|..
 00002a90: 0064 099d 047d 037c 0353 0009 007c 00a0  .d...}.|.S...|..
 00002aa0: 0964 0e7c 029b 009d 02a1 0101 007c 0353  .d.|.........|.S
-00002ab0: 0029 0f4e 726f 0000 0072 7600 0000 7272  .).Nro...rv...rr
-00002ac0: 0000 0072 7300 0000 7274 0000 0072 7500  ...rs...rt...ru.
-00002ad0: 0000 727a 0000 007a 0f50 726f 6a65 6374  ..rz...z.Project
-00002ae0: 2073 6574 2074 6f20 7a02 2e0a 727b 0000   set to z...r{..
+00002ab0: 0029 0f4e 7271 0000 0072 7800 0000 7274  .).Nrq...rx...rt
+00002ac0: 0000 0072 7500 0000 7276 0000 0072 7700  ...ru...rv...rw.
+00002ad0: 0000 727c 0000 007a 0f50 726f 6a65 6374  ..r|...z.Project
+00002ae0: 2073 6574 2074 6f20 7a02 2e0a 727d 0000   set to z...r}..
 00002af0: 007a 0f50 726f 6669 6c65 2073 6574 2074  .z.Profile set t
-00002b00: 6f20 727c 0000 007a 0c54 6173 6b20 7365  o r|...z.Task se
+00002b00: 6f20 727e 0000 007a 0c54 6173 6b20 7365  o r~...z.Task se
 00002b10: 7420 746f 207a 1d52 7574 726f 6821 2020  t to z.Rutroh!  
 00002b20: 556e 6465 6669 6e65 6420 6172 6775 6d65  Undefined argume
-00002b30: 6e74 3a20 290a 7265 0000 00da 0673 656c  nt: ).re.....sel
-00002b40: 6563 7472 9500 0000 7249 0000 0072 7100  ectr....rI...rq.
-00002b50: 0000 da03 7374 7272 4b00 0000 724f 0000  ....strrK...rO..
-00002b60: 0072 4d00 0000 728f 0000 0029 0472 6900  .rM...r....).ri.
-00002b70: 0000 da03 6b65 79da 0576 616c 7565 728d  ....key..valuer.
-00002b80: 0000 0072 6c00 0000 726c 0000 0072 6d00  ...rl...rl...rm.
+00002b30: 6e74 3a20 290a 7267 0000 00da 0673 656c  nt: ).rg.....sel
+00002b40: 6563 7472 9800 0000 724b 0000 0072 7300  ectr....rK...rs.
+00002b50: 0000 da03 7374 7272 4d00 0000 7251 0000  ....strrM...rQ..
+00002b60: 0072 4f00 0000 7291 0000 0029 0472 6b00  .rO...r....).rk.
+00002b70: 0000 da03 6b65 79da 0576 616c 7565 728f  ....key..valuer.
+00002b80: 0000 0072 6e00 0000 726e 0000 0072 6f00  ...rn...rn...ro.
 00002b90: 0000 da0f 7265 7374 6f72 655f 6469 7370  ....restore_disp
 00002ba0: 6c61 790d 0200 0073 5800 0000 0401 0201  lay....sX.......
 00002bb0: 0a01 0401 0a01 041f 0ae3 041d 0ae4 1001  ................
 00002bc0: 041b 0ae6 0401 0a01 0418 0aea 0416 0aeb  ................
 00002bd0: 0401 0a01 0413 0aef 0411 0af0 0401 0a01  ................
 00002be0: 040e 0af4 040c 0af5 0401 1001 0409 0af8  ................
 00002bf0: 0401 1001 0406 06fb 0401 1001 0403 02fe  ................
@@ -716,38 +716,38 @@
 00002cb0: 0074 06a0 03a1 0044 0083 017d 067c 006a  .t.....D...}.|.j
 00002cc0: 02a0 03a1 0044 005d 155c 027d 047d 057c  .....D.].\.}.}.|
 00002cd0: 0464 0075 0172 5c7c 029b 0064 057c 067c  .d.u.r\|...d.|.|
 00002ce0: 0419 009b 0064 067c 059b 0064 079d 067d  .....d.|...d...}
 00002cf0: 0271 477c 00a0 077c 029b 0064 089d 0264  .qG|...|...d...d
 00002d00: 09a1 0201 0064 0053 007c 00a0 0764 0a64  .....d.S.|...d.d
 00002d10: 01a1 0201 0064 0053 0029 0b4e 4629 0272  .....d.S.).NF).r
-00002d20: 6f00 0000 726f 0000 0063 0100 0000 0000  o...ro...c......
+00002d20: 7100 0000 7271 0000 0063 0100 0000 0000  q...rq...c......
 00002d30: 0000 0000 0000 0300 0000 0400 0000 5300  ..............S.
 00002d40: 0000 7316 0000 0069 007c 005d 075c 027d  ..s....i.|.].\.}
-00002d50: 017d 027c 027c 0193 0271 0253 0072 6c00  .}.|.|...q.S.rl.
-00002d60: 0000 726c 0000 0029 03da 022e 30da 016b  ..rl...)....0..k
-00002d70: da01 7672 6c00 0000 726c 0000 0072 6d00  ..vrl...rl...rm.
+00002d50: 017d 027c 027c 0193 0271 0253 0072 6e00  .}.|.|...q.S.rn.
+00002d60: 0000 726e 0000 0029 03da 022e 30da 016b  ..rn...)....0..k
+00002d70: da01 7672 6e00 0000 726e 0000 0072 6f00  ..vrn...rn...ro.
 00002d80: 0000 da0a 3c64 6963 7463 6f6d 703e 4602  ....<dictcomp>F.
 00002d90: 0000 7302 0000 0016 007a 304d 7947 7569  ..s......z0MyGui
 00002da0: 2e72 6573 746f 7265 5f73 6574 7469 6e67  .restore_setting
 00002db0: 735f 6576 656e 742e 3c6c 6f63 616c 733e  s_event.<locals>
 00002dc0: 2e3c 6469 6374 636f 6d70 3efa 0120 7a0e  .<dictcomp>.. z.
-00002dd0: 2063 6f6c 6f72 2073 6574 2074 6f20 728c   color set to r.
+00002dd0: 2063 6f6c 6f72 2073 6574 2074 6f20 728e   color set to r.
 00002de0: 0000 007a 130a 5365 7474 696e 6773 2072  ...z..Settings r
 00002df0: 6573 746f 7265 642e 547a 174e 6f20 7365  estored.Tz.No se
 00002e00: 7474 696e 6773 2066 696c 6520 666f 756e  ttings file foun
-00002e10: 642e 2908 7267 0000 0072 0300 0000 7282  d.).rg...r....r.
+00002e10: 642e 2908 7269 0000 0072 0300 0000 7284  d.).ri...r....r.
 00002e20: 0000 00da 0569 7465 6d73 da07 7365 7461  .....items..seta
-00002e30: 7474 7272 ac00 0000 7204 0000 0072 8f00  ttrr....r....r..
-00002e40: 0000 2907 7269 0000 0072 a700 0000 5a0c  ..).ri...r....Z.
+00002e30: 7474 7272 af00 0000 7204 0000 0072 9100  ttrr....r....r..
+00002e40: 0000 2907 726b 0000 0072 aa00 0000 5a0c  ..).rk...r....Z.
 00002e50: 616c 6c5f 6d65 7373 6167 6573 5a0b 6e65  all_messagesZ.ne
-00002e60: 775f 6d65 7373 6167 6572 aa00 0000 72ab  w_messager....r.
+00002e60: 775f 6d65 7373 6167 6572 ad00 0000 72ae  w_messager....r.
 00002e70: 0000 005a 0f69 6e76 5f63 6f6c 6f72 5f6e  ...Z.inv_color_n
-00002e80: 616d 6573 726c 0000 0072 6c00 0000 726d  amesrl...rl...rm
-00002e90: 0000 0072 5100 0000 3602 0000 732a 0000  ...rQ...6...s*..
+00002e80: 616d 6573 726e 0000 0072 6e00 0000 726f  amesrn...rn...ro
+00002e90: 0000 0072 5300 0000 3602 0000 732a 0000  ...rS...6...s*..
 00002ea0: 000a 0104 0102 0208 010a ff0a 0408 0110  ................
 00002eb0: 0108 010c 0110 0108 0102 8012 0212 0108  ................
 00002ec0: 0118 0202 ff02 8016 0410 037a 1c4d 7947  ...........z.MyG
 00002ed0: 7569 2e72 6573 746f 7265 5f73 6574 7469  ui.restore_setti
 00002ee0: 6e67 735f 6576 656e 7463 0100 0000 0000  ngs_eventc......
 00002ef0: 0000 0000 0000 0200 0000 0400 0000 4300  ..............C.
 00002f00: 0000 738c 0000 007c 006a 00a0 0164 01a1  ..s....|.j...d..
@@ -755,77 +755,77 @@
 00002f20: 04a0 03a1 0001 007c 006a 05a0 03a1 0001  .......|.j......
 00002f30: 007c 006a 06a0 0164 02a1 0101 0074 07a0  .|.j...d.....t..
 00002f40: 0864 02a1 0101 007c 006a 09a0 03a1 0001  .d.....|.j......
 00002f50: 007c 00a0 0a64 0364 04a1 0201 007c 00a0  .|...d.d.....|..
 00002f60: 0b64 05a1 0101 007c 006a 0c72 3f7c 006a  .d.....|.j.r?|.j
 00002f70: 0c44 005d 087d 017c 016a 0d64 0564 068d  .D.].}.|.j.d.d..
 00002f80: 0101 0071 367c 00a0 0e64 07a1 0101 0064  ...q6|...d.....d
-00002f90: 0053 0029 084e 721f 0000 0072 0500 0000  .S.).Nr....r....
+00002f90: 0053 0029 084e 7220 0000 0072 0500 0000  .S.).Nr ...r....
 00002fa0: 7a0f 5365 7474 696e 6773 2072 6573 6574  z.Settings reset
-00002fb0: 2e54 726f 0000 0072 3800 0000 4629 0f72  .Tro...r8...F).r
-00002fc0: 4900 0000 7271 0000 0072 4b00 0000 7295  I...rq...rK...r.
-00002fd0: 0000 0072 4f00 0000 724d 0000 0072 5300  ...rO...rM...rS.
-00002fe0: 0000 7245 0000 0072 9f00 0000 7265 0000  ..rE...r....re..
-00002ff0: 0072 8f00 0000 728a 0000 0072 7e00 0000  .r....r....r~...
-00003000: 7259 0000 0072 6700 0000 2902 7269 0000  rY...rg...).ri..
-00003010: 00da 056c 6162 656c 726c 0000 0072 6c00  ...labelrl...rl.
-00003020: 0000 726d 0000 0072 5400 0000 5502 0000  ..rm...rT...U...
+00002fb0: 2e54 7271 0000 0072 3a00 0000 4629 0f72  .Trq...r:...F).r
+00002fc0: 4b00 0000 7273 0000 0072 4d00 0000 7298  K...rs...rM...r.
+00002fd0: 0000 0072 5100 0000 724f 0000 0072 5500  ...rQ...rO...rU.
+00002fe0: 0000 7247 0000 0072 a200 0000 7267 0000  ..rG...r....rg..
+00002ff0: 0072 9100 0000 728c 0000 0072 8000 0000  .r....r....r....
+00003000: 725b 0000 0072 6900 0000 2902 726b 0000  r[...ri...).rk..
+00003010: 00da 056c 6162 656c 726e 0000 0072 6e00  ...labelrn...rn.
+00003020: 0000 726f 0000 0072 5600 0000 5502 0000  ..ro...rV...U...
 00003030: 731a 0000 000c 010a 010a 010a 010c 010a  s...............
 00003040: 010a 010c 010a 0106 010a 010e 010e 017a  ...............z
 00003050: 1a4d 7947 7569 2e72 6573 6574 5f73 6574  .MyGui.reset_set
 00003060: 7469 6e67 735f 6576 656e 7463 0100 0000  tings_eventc....
 00003070: 0000 0000 0000 0000 0100 0000 0400 0000  ................
 00003080: 4300 0000 731c 0000 007c 006a 00a0 01a1  C...s....|.j....
 00003090: 007c 005f 027c 00a0 0364 0164 02a1 0201  .|._.|...d.d....
 000030a0: 0064 0053 0029 034e 7a3e 4465 6275 6720  .d.S.).Nz>Debug 
 000030b0: 6d6f 6465 2072 6571 7569 7265 7320 5461  mode requires Ta
 000030c0: 736b 6572 2062 6163 6b75 7020 6669 6c65  sker backup file
 000030d0: 2074 6f20 6265 206e 616d 6564 3a20 6261   to be named: ba
-000030e0: 636b 7570 2e78 6d6c 5429 0472 6500 0000  ckup.xmlT).re...
-000030f0: 72a3 0000 0072 7600 0000 728f 0000 0072  r....rv...r....r
-00003100: 6800 0000 726c 0000 0072 6c00 0000 726d  h...rl...rl...rm
-00003110: 0000 0072 6400 0000 6702 0000 7308 0000  ...rd...g...s...
+000030e0: 636b 7570 2e78 6d6c 5429 0472 6700 0000  ckup.xmlT).rg...
+000030f0: 72a6 0000 0072 7800 0000 7291 0000 0072  r....rx...r....r
+00003100: 6a00 0000 726e 0000 0072 6e00 0000 726f  j...rn...rn...ro
+00003110: 0000 0072 6600 0000 6702 0000 7308 0000  ...rf...g...s...
 00003120: 000c 0104 0104 0108 ff7a 1a4d 7947 7569  .........z.MyGui
 00003130: 2e64 6562 7567 5f63 6865 636b 626f 785f  .debug_checkbox_
 00003140: 6576 656e 7463 0100 0000 0000 0000 0000  eventc..........
 00003150: 0000 0100 0000 0200 0000 4300 0000 f312  ..........C.....
 00003160: 0000 0064 017c 005f 007c 00a0 01a1 0001  ...d.|._.|......
-00003170: 0064 0053 00a9 024e 5429 0272 7900 0000  .d.S...NT).ry...
-00003180: da04 7175 6974 7268 0000 0072 6c00 0000  ..quitrh...rl...
-00003190: 726c 0000 0072 6d00 0000 7255 0000 0070  rl...rm...rU...p
+00003170: 0064 0053 00a9 024e 5429 0272 7b00 0000  .d.S...NT).r{...
+00003180: da04 7175 6974 726a 0000 0072 6e00 0000  ..quitrj...rn...
+00003190: 726e 0000 0072 6f00 0000 7257 0000 0070  rn...ro...rW...p
 000031a0: 0200 00f3 0400 0000 0601 0c01 7a11 4d79  ............z.My
 000031b0: 4775 692e 7275 6e5f 7072 6f67 7261 6d63  Gui.run_programc
 000031c0: 0100 0000 0000 0000 0000 0000 0100 0000  ................
-000031d0: 0200 0000 4300 0000 72b5 0000 0072 b600  ....C...r....r..
-000031e0: 0000 2902 7278 0000 0072 b700 0000 7268  ..).rx...r....rh
-000031f0: 0000 0072 6c00 0000 726c 0000 0072 6d00  ...rl...rl...rm.
-00003200: 0000 7256 0000 0077 0200 0072 b800 0000  ..rV...w...r....
+000031d0: 0200 0000 4300 0000 72b8 0000 0072 b900  ....C...r....r..
+000031e0: 0000 2902 727a 0000 0072 ba00 0000 726a  ..).rz...r....rj
+000031f0: 0000 0072 6e00 0000 726e 0000 0072 6f00  ...rn...rn...ro.
+00003200: 0000 7258 0000 0077 0200 0072 bb00 0000  ..rX...w...r....
 00003210: 7a12 4d79 4775 692e 6578 6974 5f70 726f  z.MyGui.exit_pro
 00003220: 6772 616d 291b da08 5f5f 6e61 6d65 5f5f  gram)...__name__
 00003230: da0a 5f5f 6d6f 6475 6c65 5f5f da0c 5f5f  ..__module__..__
-00003240: 7175 616c 6e61 6d65 5f5f 7240 0000 00da  qualname__r@....
-00003250: 0462 6f6f 6c72 6700 0000 728a 0000 0072  .boolrg...r....r
-00003260: 8f00 0000 7291 0000 0072 5d00 0000 725f  ....r....r]...r_
-00003270: 0000 0072 6100 0000 72a9 0000 0072 5200  ...ra...r....rR.
-00003280: 0000 7248 0000 0072 6300 0000 724a 0000  ..rH...rc...rJ..
-00003290: 0072 4e00 0000 724c 0000 0072 5000 0000  .rN...rL...rP...
-000032a0: 72ac 0000 0072 5100 0000 7254 0000 0072  r....rQ...rT...r
-000032b0: 6400 0000 7255 0000 0072 5600 0000 da0d  d...rU...rV.....
-000032c0: 5f5f 636c 6173 7363 656c 6c5f 5f72 6c00  __classcell__rl.
-000032d0: 0000 726c 0000 0072 6a00 0000 726d 0000  ..rl...rj...rm..
+00003240: 7175 616c 6e61 6d65 5f5f 7242 0000 00da  qualname__rB....
+00003250: 0462 6f6f 6c72 6900 0000 728c 0000 0072  .boolri...r....r
+00003260: 9100 0000 7294 0000 0072 5f00 0000 7261  ....r....r_...ra
+00003270: 0000 0072 6300 0000 72ac 0000 0072 5400  ...rc...r....rT.
+00003280: 0000 724a 0000 0072 6500 0000 724c 0000  ..rJ...re...rL..
+00003290: 0072 5000 0000 724e 0000 0072 5200 0000  .rP...rN...rR...
+000032a0: 72af 0000 0072 5300 0000 7256 0000 0072  r....rS...rV...r
+000032b0: 6600 0000 7257 0000 0072 5800 0000 da0d  f...rW...rX.....
+000032c0: 5f5f 636c 6173 7363 656c 6c5f 5f72 6e00  __classcell__rn.
+000032d0: 0000 726e 0000 0072 6c00 0000 726f 0000  ..rn...rl...ro..
 000032e0: 0072 0600 0000 3b00 0000 732e 0000 0008  .r....;...s.....
 000032f0: 000c 0100 7f0e 7408 1708 0c08 0d08 2808  ......t.......(.
 00003300: 1308 130e 130e 070e 0608 1b08 0608 0608  ................
 00003310: 0608 1308 2908 1f08 1208 0910 0772 0600  ....)........r..
-00003320: 0000 290c 7245 0000 005a 1f43 546b 436f  ..).rE...Z.CTkCo
+00003320: 0000 290c 7247 0000 005a 1f43 546b 436f  ..).rG...Z.CTkCo
 00003330: 6c6f 7250 6963 6b65 722e 6374 6b5f 636f  lorPicker.ctk_co
 00003340: 6c6f 725f 7069 636b 6572 7202 0000 00da  lor_pickerr.....
 00003350: 176d 6170 7461 736b 6572 2e73 7263 2e67  .maptasker.src.g
 00003360: 6574 7075 7461 7267 7203 0000 00da 166d  etputargr......m
 00003370: 6170 7461 736b 6572 2e73 7263 2e73 7973  aptasker.src.sys
-00003380: 636f 6e73 7472 0400 0000 729f 0000 005a  constr....r....Z
+00003380: 636f 6e73 7472 0400 0000 72a2 0000 005a  constr....r....Z
 00003390: 1773 6574 5f64 6566 6175 6c74 5f63 6f6c  .set_default_col
-000033a0: 6f72 5f74 6865 6d65 7281 0000 005a 0343  or_themer....Z.C
-000033b0: 546b 7206 0000 0072 6c00 0000 726c 0000  Tkr....rl...rl..
-000033c0: 0072 6c00 0000 726d 0000 00da 083c 6d6f  .rl...rm.....<mo
+000033a0: 6f72 5f74 6865 6d65 7283 0000 005a 0343  or_themer....Z.C
+000033b0: 546b 7206 0000 0072 6e00 0000 726e 0000  Tkr....rn...rn..
+000033c0: 0072 6e00 0000 726f 0000 00da 083c 6d6f  .rn...ro.....<mo
 000033d0: 6475 6c65 3e01 0000 0073 1200 0000 0812  dule>....s......
 000033e0: 0c02 0c01 0c01 0a03 0a02 0203 02ff 161d  ................
```

### Comparing `maptasker-1.3.1/maptasker/src/actargs.py` & `maptasker-1.3.2/maptasker/src/actargs.py`

 * *Files 23% similar despite different names*

```diff
@@ -8,17 +8,107 @@
 # Permissions of this strong copyleft license are conditioned on making available            #
 # complete source code of licensed works and modifications, which include larger works       #
 # using a licensed work, under the same license. Copyright and license notices must be       #
 # preserved. Contributors provide an express grant of patent rights.                         #
 # ########################################################################################## #
 from maptasker.src.actiond import process_condition_list
 from maptasker.src.sysconst import logger
+import xml.etree.ElementTree  # Need for type hints
 import maptasker.src.action as get_action
 
 
+def get_action_arguments(
+    evaluated_results: dict,
+    arg: object,
+    argeval: list,
+    argtype: list,
+    code_action: xml.etree,
+    action_type: xml.etree,
+    colormap: dict,
+    program_args: dict,
+) -> dict:
+    """
+
+    :param evaluated_results: all the Action argument "types" and "arguments"
+    :param arg: the incoming argument
+    :param argeval: the evaluation argument
+    :param argtype: the argument "type"
+    :param code_action: the Action code
+    :param action_type: the Action type
+    :param colormap: colors to use in output
+    :param program_args: runtime arguments
+    :return: dictionary of results
+    """
+    match argtype:
+        case "Str":
+            evaluated_results["get_xml_flag"] = True
+            evaluated_results["strargs"].append(f"arg{str(arg)}")
+            evaluated_results["streval"].append(argeval)
+            evaluated_results["returning_something"] = True
+        case "Int":
+            evaluated_results["get_xml_flag"] = True
+            evaluated_results["intargs"].append(f"arg{str(arg)}")
+            evaluated_results["inteval"].append(argeval)
+            evaluated_results["returning_something"] = True
+        case "App":
+            evaluated_results["strargs"].append(f"arg{str(arg)}")
+            evaluated_results["streval"].append(argeval)
+            app_class, app_pkg, app, extra = get_action.get_app_details(
+                code_action, action_type, colormap, program_args
+            )
+            evaluated_results["result_app"].append(f"{app_class}, {app_pkg}, {app}")
+            evaluated_results["returning_something"] = True
+        case "ConditionList":
+            evaluated_results["strargs"].append(f"arg{str(arg)}")
+            evaluated_results["streval"].append(argeval)
+            final_conditions = ""
+            condition_list, boolean_list = process_condition_list(code_action)
+            # Go through all conditions
+            for numx, condition in enumerate(condition_list):
+                final_conditions = (
+                    f"{final_conditions} {condition[0]}{condition[1]}{condition[2]}"
+                )
+                if boolean_list and len(boolean_list) > numx:
+                    final_conditions = f"{final_conditions} {boolean_list[numx]} "
+            evaluated_results["result_con"].append(final_conditions)
+            evaluated_results["returning_something"] = True
+        case "Img":
+            image, package = "", ""
+            child = code_action.find("Img")
+            if child.find("nme") is not None:
+                image = child.find("nme").text
+            if child.find("pkg") is not None:
+                package = ", Package:" + child.find("pkg").text
+            elif child.find("var") is not None:  # There is a variable name?
+                image = child.find("var").text
+            if image:
+                evaluated_results["result_img"].append(argeval + image + package)
+                evaluated_results["returning_something"] = True
+            else:
+                evaluated_results["result_img"].append(" ")
+        case "Bundle":  # It's a plugin
+            child1 = code_action.find("Bundle")
+            child2 = child1.find("Vals")
+            child3 = child2.find(
+                "com.twofortyfouram.locale.intent.extra.BLURB"
+            )  # 2:40 am...funny!
+            if child3 is not None and child3.text is not None:
+                # Get rid of extraneous html in Action's label
+                clean_string = child3.text.replace("</font><br><br>", "<br><br>")
+                clean_string = clean_string.replace("&lt;", "<")
+                clean_string = clean_string.replace("&gt;", ">")
+                evaluated_results["result_bun"].append(clean_string)
+                evaluated_results["returning_something"] = True
+        case _:
+            logger.debug(
+                "get_action_results:" + " unknown argtype:" + argtype + "!!!!!"
+            )
+    return evaluated_results
+
+
 # ####################################################################################################
 # Go through the arguments and parse each one based on its argument 'type'
 # ####################################################################################################
 def action_args(
     arg_list,
     dict_code,
     lookup_code_entry,
@@ -32,73 +122,19 @@
     for num, arg in enumerate(arg_list):
         # Find the location for this arg in dictionary key "types' since they can be non-sequential (e.g. '1', '3', '4', '6')
         index = num if arg == "if" else lookup_code_entry[dict_code]["args"].index(arg)
         # Get the arg name and type
         argeval = evaluate_list[num]
         argtype = lookup_code_entry[dict_code]["types"][index]
         evaluated_results["position_arg_type"].append(argtype)
-        match argtype:
-            case "Str":
-                evaluated_results["get_xml_flag"] = True
-                evaluated_results["strargs"].append(f"arg{str(arg)}")
-                evaluated_results["streval"].append(argeval)
-                evaluated_results["returning_something"] = True
-            case "Int":
-                evaluated_results["get_xml_flag"] = True
-                evaluated_results["intargs"].append(f"arg{str(arg)}")
-                evaluated_results["inteval"].append(argeval)
-                evaluated_results["returning_something"] = True
-            case "App":
-                evaluated_results["strargs"].append(f"arg{str(arg)}")
-                evaluated_results["streval"].append(argeval)
-                app_class, app_pkg, app, extra = get_action.get_app_details(
-                    code_action, action_type, colormap, program_args
-                )
-                evaluated_results["result_app"].append(f"{app_class}, {app_pkg}, {app}")
-                evaluated_results["returning_something"] = True
-            case "ConditionList":
-                evaluated_results["strargs"].append(f"arg{str(arg)}")
-                evaluated_results["streval"].append(argeval)
-                final_conditions = ""
-                condition_list, boolean_list = process_condition_list(code_action)
-                # Go through all conditions
-                for numx, condition in enumerate(condition_list):
-                    final_conditions = (
-                        f"{final_conditions} {condition[0]}{condition[1]}{condition[2]}"
-                    )
-                    if boolean_list and len(boolean_list) > numx:
-                        final_conditions = f"{final_conditions} {boolean_list[numx]} "
-                evaluated_results["result_con"].append(final_conditions)
-                evaluated_results["returning_something"] = True
-            case "Img":
-                image, package = "", ""
-                child = code_action.find("Img")
-                if child.find("nme") is not None:
-                    image = child.find("nme").text
-                if child.find("pkg") is not None:
-                    package = ", Package:" + child.find("pkg").text
-                elif child.find("var") is not None:  # There is a variable name?
-                    image = child.find("var").text
-                if image:
-                    evaluated_results["result_img"].append(argeval + image + package)
-                    evaluated_results["returning_something"] = True
-                else:
-                    evaluated_results["result_img"].append(" ")
-            case "Bundle":  # It's a plugin
-                child1 = code_action.find("Bundle")
-                child2 = child1.find("Vals")
-                child3 = child2.find(
-                    "com.twofortyfouram.locale.intent.extra.BLURB"
-                )  # 2:40 am...funny!
-                if child3 is not None and child3.text is not None:
-                    # Get rid of extraneous html in Action's label
-                    clean_string = child3.text.replace("</font><br><br>", "<br><br>")
-                    clean_string = clean_string.replace("&lt;", "<")
-                    clean_string = clean_string.replace("&gt;", ">")
-                    evaluated_results["result_bun"].append(clean_string)
-                    evaluated_results["returning_something"] = True
-            case _:
-                logger.debug(
-                    "get_action_results:" + " unknown argtype:" + argtype + "!!!!!"
-                )
+        evaluated_results = get_action_arguments(
+            evaluated_results,
+            arg,
+            argeval,
+            argtype,
+            code_action,
+            action_type,
+            colormap,
+            program_args,
+        )
 
     return evaluated_results
```

### Comparing `maptasker-1.3.1/maptasker/src/action.py` & `maptasker-1.3.2/maptasker/src/action.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,26 +1,25 @@
 #! /usr/bin/env python3
 
 # ########################################################################################## #
 #                                                                                            #
-# action: Task Action functions for MapTasker                                                #
+# action: Find Task's Action arguments (<argn>) and return as sorted list                    #
 #                                                                                            #
 # Permissions of this strong copyleft license are conditioned on making available            #
 # complete source code of licensed works and modifications, which include larger works       #
 # using a licensed work, under the same license. Copyright and license notices must be       #
 # preserved. Contributors provide an express grant of patent rights.                         #
 #                                                                                            #
 # ########################################################################################## #
 
-import maptasker.src.shellsort as shell_sort
-from maptasker.src.sysconst import logger
-import re
 import sys
 
-pattern = re.compile(r"<.*?>")
+from maptasker.src.shellsort import shell_sort
+from maptasker.src.sysconst import logger
+from maptasker.src.sysconst import FONT_TO_USE
 
 
 # #######################################################################################
 # Given a Task's Action, find all 'arg(n)' xml elements and return as a sorted list
 # Input:
 #   action: list of actions or parameters
 #   ignore_list: xml to ignore (e.g. label, on, etc.
@@ -198,93 +197,22 @@
             )
             logger.debug(msg)
             exit(8)  # Rutroh...not an even pair of elements
     return
 
 
 # ####################################################################################################
-#  Given an action code (xml), find Int (integer) args and match with names
-#  Example:
-#  3 Ints with arg0, arg1 and arg2, to be filled in with their matching name0, name1 and name2 + the associated text
-#  action = xml element for Action <code>
-#  arguments = list of Int arguments to look for (e.g. arg1,arg5,arg9)
-#  names = list of entries to substitute the argn value against.
-#    ...It can be a list, which signifies a pull-down list of options to map against:
-#         [ preceding_text1, value1, evaluated_text1, preceding_text2, value2, evaluated_text2, ...]
-#         ['', 'e', 'name'] > Test for '1' and plug in 'name' if '1'
-#         ['some_text', 'l', lookup_code] > use lookup_values dictionary to translate code and plug in value
-# ####################################################################################################
-def get_xml_int_argument_to_value(action, arguments, names):
-    match_results = []
-
-    for child in action:
-        if child.tag == "Int":
-            the_arg = child.attrib.get("sr")
-            for arg in arguments:
-                if arg == the_arg:
-                    arg_location = arguments.index(arg)
-                    the_int_value = ""
-                    if child.attrib.get("val") is not None:
-                        the_int_value = child.attrib.get(
-                            "val"
-                        )  # There a numeric value as a string?
-                    elif child.find("var") is not None:  # There is a variable name?
-                        the_int_value = child.find("var").text
-                    if the_int_value:  # If we have an integer or variable name
-                        # List of options for this Int?
-                        if type(names[arg_location]) is list:
-                            process_xml_list(
-                                names,
-                                arg_location,
-                                the_int_value,
-                                match_results,
-                                arguments,
-                            )
-                        else:  # Not a list
-                            match_results.append(
-                                names[arg_location] + the_int_value
-                            )  # Just grab the integer value
-                        break  # Get out of arg loop and get next child
-                    else:
-                        match_results.append(
-                            ""
-                        )  # No Integer value or variable found...return empty
-
-    return drop_trailing_comma(match_results)
-
-
-# ####################################################################################################
-#  Given an action code (xml), find Str (string) args and match with names
-#  Example:
-#  3 Strs with arg0, arg1 and arg2, to be filled in with their matching name0, name1 and name2 + the associated text
-# ####################################################################################################
-def get_xml_str_argument_to_value(action, arguments, names) -> list:
-    match_results = []
-    for child in action:
-        if child.tag == "Str":
-            the_arg = child.attrib.get("sr")
-            for arg in arguments:
-                if arg == the_arg:
-                    arg_location = arguments.index(arg)
-                    if child.text is not None:
-                        match_results.append(names[arg_location] + child.text + ", ")
-                    else:
-                        match_results.append("")
-                    break  # We have what we want.  Go to next child
-    return drop_trailing_comma(match_results)
-
-
-# ####################################################################################################
 # Get Task's label, disabled flag and any conditions
 # ####################################################################################################
 def get_label_disabled_condition(child, colormap):
     disabled_action_html = (
-        ' <span style = "color:'
+        ' </span><span style="color:'
         + colormap["disabled_action_color"]
-        + '"</span>[DISABLED]'
+        + FONT_TO_USE
+        + '>[DISABLED]</span>'
     )
 
     task_label = ""
     task_conditions = ""
     the_action_code = child.find("code").text
     if child.find("label") is not None:
         lbl = child.find("label").text
@@ -302,16 +230,16 @@
             if "bool" in children.tag:
                 booleans.append(children.text)
             elif children.tag == "Condition" and the_action_code != "37":
                 string1, operator, string2 = evaluate_condition(children)
                 if condition_count != 0:
                     boolean_to_inject = f"{booleans[condition_count - 1].upper()} "
                 task_conditions = (
-                    f'{task_conditions} <span style ='
-                    f' "color:{colormap["action_condition_color"]}"</span>'
+                    f'{task_conditions} <span style='
+                    f' "color:{colormap["action_condition_color"]}"></span>'
                     f' ({boolean_to_inject}condition:  If {string1}{operator}{string2})'
                 )
                 condition_count += 1
         if the_action_code == "35":  # Wait Until?
             task_conditions = task_conditions.replace(
                 "condition:  If", "<em>UNTIL</em>"
             )
@@ -330,19 +258,19 @@
     lbl = lbl.replace("</font></font>", "</font>")
     font_count = lbl.count("<font")
     if (
         font_count > 0
     ):  # Make sure we end with the same number combination of <font> and </font>
         end_font_count = lbl.count("/font")
         if font_count > end_font_count:
-            lbl = f'{lbl}<font "color:{colormap["action_label_color"]}"</font>'
+            lbl = f'{lbl}<span style="color:{colormap["action_label_color"]}"'
 
     return (
-        f' <span style = "color:{colormap["action_label_color"]}"</span>...with label:'
-        f' {lbl}'
+        f' <span style="color:{colormap["action_label_color"]}">...with label:'
+        f' {lbl}</span></b>'
     )
 
 
 # ####################################################################################################
 # Chase after relevant data after <code> Task action
 # code_flag identifies the type of xml data to go after based on the specific code in <code>xxx</code>
 # Get the: label, whether to continue Task after error, etc.
@@ -368,15 +296,16 @@
             extra_stuff = f"{extra_stuff}</b>"
     else:
         extra_stuff = ""
     if (
         program_args["debug"] and action_type
     ):  # Add the code if this is an Action and in debug mode
         extra_stuff = (
-            f'{extra_stuff}<span style="color:Red"</span>&nbsp;&nbsp;code:'
+            f'{extra_stuff}</span><span'
+            f' style="color:Red{program_args["font_to_use"]}>&nbsp;&nbsp;code:'
             + code_action.find("code").text
             + "-"
         )
 
     # See if Task action is to be continued after error
     child = code_action.find("se")
     if child is not None and child.text == "false":
```

### Comparing `maptasker-1.3.1/maptasker/src/actionc.py` & `maptasker-1.3.2/maptasker/src/actionc.py`

 * *Files identical despite different names*

### Comparing `maptasker-1.3.1/maptasker/src/actiond.py` & `maptasker-1.3.2/maptasker/src/actiond.py`

 * *Files identical despite different names*

### Comparing `maptasker-1.3.1/maptasker/src/actione.py` & `maptasker-1.3.2/maptasker/src/actione.py`

 * *Files 13% similar despite different names*

```diff
@@ -15,14 +15,15 @@
 import xml.etree.ElementTree  # Need for type hints
 
 import maptasker.src.actionr as action_results
 from maptasker.src.config import CONTINUE_LIMIT
 from maptasker.src.action import get_extra_stuff
 from maptasker.src.actionc import action_codes
 from maptasker.src.sysconst import logger
+from maptasker.src.sysconst import FONT_TO_USE
 
 pattern = re.compile(r",[, ]+")
 # pattern1 = re.compile(r'<.*?>')  # Get rid of all <something> html code
 
 
 # ####################################################################################################
 # Delete crap that might be in the label
@@ -91,35 +92,51 @@
     code_child: xml.etree.ElementTree,
     code_action: xml.etree.ElementTree,
     action_type: bool,
     colormap: dict,
     code_type: str,
     program_args: dict,
 ) -> str:
+    """
+    Given an action code, evaluate it for display
+        :param code_child: xml element of the <code>
+        :param code_action: value of <code> (e.g. "549")
+        :param action_type:
+        :param colormap: colors to use in output
+        :param code_type: 'e'=event, 's'=state, 't'=task
+        :param program_args: runtime arguments
+        :return: formatted output line with action details
+    """
     logger.debug(f"getcode:{code_child.text}{code_type}")
     dict_code = code_child.text + code_type
     # See if this code is deprecated
     check_for_deprecation(dict_code)
-    if (
-        dict_code not in action_codes or "display" not in action_codes[dict_code]
-    ):  # We have a code that is not yet in the dictionary?
-        the_result = f"Code {dict_code} not yet mapped{get_extra_stuff(code_action, action_type, colormap, program_args)}"
+    # We have a code that is not yet in the dictionary?
+    if dict_code not in action_codes or "display" not in action_codes[dict_code]:
+        the_result = (
+            f"Code {dict_code} not yet"
+            f" mapped{get_extra_stuff(code_action, action_type, colormap, program_args)}"
+        )
         logger.debug(f"unmapped task code: {dict_code} ")
 
     else:
+        # The code is in our dictionary.  Add the display name
         the_result = (
             '<span style="color:'
             + colormap["action_name_color"]
-            + '"</span>'
+            + program_args["font_to_use"]
+            + '>'
             + action_codes[dict_code]["display"]
+            + "</span>"
         )  # Just get the basics for now
         if "numargs" in action_codes[dict_code]:
             numargs = action_codes[dict_code]["numargs"]
         else:
             numargs = 0
+        # If there are required args, then parse them
         if numargs != 0 and "reqargs" in action_codes[dict_code]:
             the_result = action_results.get_action_results(
                 dict_code,
                 action_codes,
                 code_action,
                 action_type,
                 colormap,
@@ -157,15 +174,16 @@
 # #############################################################################################
 # Construct Task Action output line
 # #############################################################################################
 def build_action(alist, tcode, code_element, indent, indent_amt):
     # Calculate total indentation to put in front of action
     count = indent
     if count != 0:
-        tcode = indent_amt + tcode
+        tcode = tcode.replace(f"{FONT_TO_USE}>", f"{FONT_TO_USE}>{indent_amt}", 1)
+        # tcode = indent_amt + tcode
         count = 0
     if count < 0:
         tcode = indent_amt + tcode
 
     # Break-up very long actions at new line
     if tcode != "":
         newline = tcode.find("\n")  # Break-up new line breaks
@@ -183,13 +201,15 @@
                 else:
                     alist.append(f"...{item}")
                 count += 1
                 if (
                     count == CONTINUE_LIMIT
                 ):  # Only display up to so many continued lines
                     alist.append(
-                        f'<font color:red> ... continue limit of {str(CONTINUE_LIMIT)} reached.  See "CONTINUE_LIMIT =" in code for details'
+                        '<span style="color:red"> ... continue limit of'
+                        f' {str(CONTINUE_LIMIT)} reached.  See "CONTINUE_LIMIT =" in'
+                        ' code for details</span>'
                     )
                     break
     else:
         alist.append(f"Action {code_element.text}: not yet mapped")
     return
```

### Comparing `maptasker-1.3.1/maptasker/src/actionr.py` & `maptasker-1.3.2/maptasker/src/actionr.py`

 * *Files 4% similar despite different names*

```diff
@@ -14,14 +14,16 @@
 import xml.etree.ElementTree  # Need for type hints
 from collections import defaultdict
 
 import maptasker.src.action as get_action
 from maptasker.src.actargs import action_args
 from maptasker.src.actionc import action_codes
 from maptasker.src.sysconst import logger
+from maptasker.src.xmldata import get_xml_int_argument_to_value
+from maptasker.src.xmldata import get_xml_str_argument_to_value
 
 
 # ####################################################################################################
 # Given a list of positional items, return a string in the correct order based on position
 # ####################################################################################################
 def get_results_in_arg_order(evaluated_results: dict) -> str:
     return_result = ""
@@ -89,19 +91,19 @@
         colormap,
         program_args,
         evaluated_results,
     )
     # If we had at least one Int or Str then deal with them
     if evaluated_results["get_xml_flag"]:
         if evaluated_results["strargs"]:
-            evaluated_results["result_str"] = get_action.get_xml_str_argument_to_value(
+            evaluated_results["result_str"] = get_xml_str_argument_to_value(
                 code_action, evaluated_results["strargs"], evaluated_results["streval"]
             )
         if evaluated_results["intargs"]:
-            evaluated_results["result_int"] = get_action.get_xml_int_argument_to_value(
+            evaluated_results["result_int"] = get_xml_int_argument_to_value(
                 code_action, evaluated_results["intargs"], evaluated_results["inteval"]
             )
 
     return evaluated_results
 
 
 # ####################################################################################################
@@ -119,24 +121,29 @@
     program_args: xml.etree.ElementTree,
 ) -> str:
     evaluated_results = defaultdict(
         lambda: []
     )  # Setup default dictionary as empty list
     two_blanks = "&nbsp;&nbsp;"
     result = ""
-    returning_something = False
-    if "s" in dict_code or "e" in dict_code:
+    if "s" in dict_code or "e" in dict_code:  # Condition (State/Event)?
         display_name_color = ""
         display_detail_color = ""
-    else:
+    else:  # We have a Task
         display_name_color = (
-            '<span style="color:' + colormap["action_name_color"] + '"</span>'
+            '<span style="color:'
+            + colormap["action_name_color"]
+            + program_args["font_to_use"]
+            + '>'
         )
         display_detail_color = (
-            '<span style="color:' + colormap["action_color"] + '"</span>'
+            '</span><span style="color:'
+            + colormap["action_color"]
+            + program_args["font_to_use"]
+            + '>'
         )
 
     # Save the associated data
     # action_codes[dict_code]['display'] = display_name
     lookup_code_entry[dict_code]["reqargs"] = arg_list
     lookup_code_entry[dict_code]["evalargs"] = evaluate_list
     # If just displaying action names or there are no action details, then just display the name
```

### Comparing `maptasker-1.3.1/maptasker/src/actiont.py` & `maptasker-1.3.2/maptasker/src/actiont.py`

 * *Files identical despite different names*

### Comparing `maptasker-1.3.1/maptasker/src/caveats.py` & `maptasker-1.3.2/maptasker/src/caveats.py`

 * *Files 6% similar despite different names*

```diff
@@ -8,53 +8,48 @@
 # Permissions of this strong copyleft license are conditioned on making available            #
 # complete source code of licensed works and modifications, which include larger works       #
 # using a licensed work, under the same license. Copyright and license notices must be       #
 # preserved. Contributors provide an express grant of patent rights.                         #
 #                                                                                            #
 # ########################################################################################## #
 import maptasker.src.outputl as build_output
-from maptasker.src.config import trailing_comments_color
 
 
 def display_caveats(output_list: list[str], program_args: dict, colormap: dict) -> None:
     """output the program caveats
     Output the program caveats at the very end
         Parameters: list into which all output has been added, the program runtime arguments,
                     the dictionary of colors to use
 
         Returns: the count of the number of times the program has been called
 
     """
     caveat1 = (
-        f'<span style="color:{colormap["trailing_comments_color"]}">'
+        f'<span style="color:{colormap["trailing_comments_color"]}'
         + program_args["font_to_use"]
-        + "</font>CAVEATS:\n"
+        + ">CAVEATS:\n"
     )
     caveat3 = (
         "- This has only been tested on my own backup.xml file."
         "  For problems, report them on https://github.com/mctinker/Map-Tasker."
     )
     caveat4 = (
         '- Tasks that are identified as "Unnamed/Anonymous" have no name and are'
         ' considered Anonymous.\n'
     )
     caveat6 = (
-        '- Task labels that have embedded HTML (e.g. color=...>") will result in the'
+        '- Tasker fields that have embedded HTML (e.g. color=...>") will result in the'
         ' remaining label displayed in that same color/font.'
     )
-    caveat7 = (
-        '- With the more recent versions of Tasker, disabled Profiles are not'
-        ' easily detected and go unrecognized as disabled.'
-    )
     build_output.my_output(colormap, program_args, output_list, 0, "<hr>")  # line
     build_output.my_output(colormap, program_args, output_list, 4, caveat1)  # caveat
     if program_args["display_detail_level"] > 0:  # Caveat about Actions
         caveat2 = (
             "- Most but not all Task actions have been mapped and will display as such."
-            "  Likewise for Profile conditions.\n"
+            "  Likewise for Profile conditions and Plug-ins.\n</span>"
         )
         build_output.my_output(
             colormap, program_args, output_list, 4, caveat2
         )  # caveat
     build_output.my_output(colormap, program_args, output_list, 4, caveat3)  # caveat
     build_output.my_output(colormap, program_args, output_list, 4, caveat4)  # caveat
     if (
@@ -64,9 +59,8 @@
             '- For option -d0, Tasks that are identified as "Unnamed/Anonymous" will'
             ' have their first Task only listed....\n  just like Tasker does.\n'
         )
         build_output.my_output(
             colormap, program_args, output_list, 4, caveat5
         )  # caveat
     build_output.my_output(colormap, program_args, output_list, 4, caveat6)  # caveat
-    build_output.my_output(colormap, program_args, output_list, 4, caveat7)  # caveat
     return
```

### Comparing `maptasker-1.3.1/maptasker/src/colors.py` & `maptasker-1.3.2/maptasker/src/colors.py`

 * *Files identical despite different names*

### Comparing `maptasker-1.3.1/maptasker/src/colrmode.py` & `maptasker-1.3.2/maptasker/src/colrmode.py`

 * *Files 6% similar despite different names*

```diff
@@ -29,25 +29,25 @@
         mode = appearance_mode
 
     if mode == "Dark":
         colormap = {
             "project_color": "White",
             "profile_color": "Aqua",
             "disabled_profile_color": "Red",
-            "launcher_task_color": "Chartreuse",
+            "launcher_task_color": "GreenYellow",
             "task_color": "Yellow",
             "unknown_task_color": "Red",
             "scene_color": "Lime",
             "bullet_color": "White",
             "action_name_color": "PaleGoldenrod",
             "action_color": "DarkOrange",
             "action_label_color": "Magenta",
             "action_condition_color": "PapayaWhip",
             "disabled_action_color": "Crimson",
-            "profile_condition_color": "Turquoise",
+            "profile_condition_color": "Lavender",
             "background_color": "DarkBlue",
             "trailing_comments_color": "PeachPuff",
             "taskernet_color": "LightPink",
             "preferences_color": 'PeachPuff',
         }
     else:
         colormap = {
```

### Comparing `maptasker-1.3.1/maptasker/src/condition.py` & `maptasker-1.3.2/maptasker/src/condition.py`

 * *Files identical despite different names*

### Comparing `maptasker-1.3.1/maptasker/src/getids.py` & `maptasker-1.3.2/maptasker/src/getids.py`

 * *Files 4% similar despite different names*

```diff
@@ -46,10 +46,9 @@
         ids_to_find = 'tids'
     try:
         # Get a list of the Profiles for this Project
         project_pids = project.find(ids_to_find).text
     except Exception:  # Project has no Profiles
         if project_name not in projects_without_profiles:
             projects_without_profiles.append(project_name)
-        if doing_project:
-            my_output(colormap, program_args, output_list, 2, f"Profile: {NO_PROFILE}")
+
     return project_pids.split(",") if project_pids != "" else []
```

### Comparing `maptasker-1.3.1/maptasker/src/getputarg.py` & `maptasker-1.3.2/maptasker/src/getputarg.py`

 * *Files identical despite different names*

### Comparing `maptasker-1.3.1/maptasker/src/initparg.py` & `maptasker-1.3.2/maptasker/src/initparg.py`

 * *Files identical despite different names*

### Comparing `maptasker-1.3.1/maptasker/src/kidapp.py` & `maptasker-1.3.2/maptasker/src/kidapp.py`

 * *Files identical despite different names*

### Comparing `maptasker-1.3.1/maptasker/src/mapit.py` & `maptasker-1.3.2/maptasker/src/mapit.py`

 * *Files 9% similar despite different names*

```diff
@@ -26,77 +26,33 @@
 # using a licensed work, under the same license. Copyright and license notices must be       #
 # preserved. Contributors provide an express grant of patent rights.                         #
 #                                                                                            #
 # Reference: https://github.com/Taskomater/Tasker-XML-Info                                   #
 #                                                                                            #
 # ########################################################################################## #
 
-import atexit
 import sys
 import webbrowser  # To be removed in Python 10.13 (2023?)
 import xml.etree.ElementTree  # Need for type hints
-from json import dumps, loads  # For write and read counter
 from os import getcwd
-from pathlib import Path
-from tkinter import messagebox
 from typing import List, Dict
 
 import maptasker.src.outputl as build_output
 import maptasker.src.proginit as initialize
 import maptasker.src.projects as projects
 import maptasker.src.taskuniq as special_tasks
 from maptasker.src.caveats import display_caveats
-from maptasker.src.sysconst import COUNTER_FILE
-from maptasker.src.sysconst import logger
-from maptasker.src.taskerd import get_the_xml_data
 from maptasker.src.prefers import get_preferences
-from maptasker.src.debug import debug1
-
+from maptasker.src.sysconst import logger
 
 # import os
 # print('Path:', os.getcwd())
 # print('__file__={0:<35} | __name__={1:<25} | __package__={2:<25}'.format(__file__,__name__,str(__package__)))
 
 
-# #############################################################################################
-# Use a counter to determine if this is the first time run.
-#  If first time only, then provide a user prompt to locate the backup file
-# #############################################################################################
-def read_counter():
-    """Read the program counter
-
-    Parameters: none
-
-    Returns: the count of the number of times the program has been called
-
-    """
-    return (
-        loads(open(COUNTER_FILE, "r").read()) + 1
-        if Path.exists(Path(COUNTER_FILE).resolve())
-        else 0
-    )
-
-
-def write_counter():
-    """Write the program counter
-
-    Parameters: none
-
-    Returns: none
-
-    """
-    with open(COUNTER_FILE, "w") as f:
-        f.write(dumps(run_counter))
-    return
-
-
-run_counter = read_counter()
-atexit.register(write_counter)
-
-
 # #######################################################################################
 # Clean up our memory hogs
 # #######################################################################################
 def clean_up_memory(
     tree: xml.etree.ElementTree.ElementTree,
     root: xml.etree.ElementTree.Element,
     output_list: List[str],
@@ -171,16 +127,17 @@
     Cleanup memory and let user know there was no match found for Task/Profile
         :param name: the name to add to the log/print output
         :param profile_or_task_name: name of the Profile or Task to clean
         :param tree: xml tree to clear
         :param root: root of xml parsed from file to clear
         :param output_list: list of output lines to empty
         :param all_tasker_items: all Tasker Projects/Profiles/Tasks/Scenes to clear
-        :rtype: none
+        :rtype: colors, runtime arguments,
     """
+
     output_list.clear()
     error_message = f"{name} {profile_or_task_name} not found!!"
     print(error_message)
     logger.debug(error_message)
     clean_up_memory(tree, root, output_list, all_tasker_items)
     sys.exit(5)
 
@@ -239,55 +196,33 @@
         [],
         [],
         [],
         [],
     )
 
     # Get colors to use, runtime arguments etc.
-    colormap, program_args, found_items, heading = initialize.start_up()
+    (
+        colormap,
+        program_args,
+        found_items,
+        heading,
+        output_list,
+        tree,
+        root,
+        filename,
+        all_tasker_items,
+    ) = initialize.start_up(output_list)
 
     # Development only parameters here:
     # program_args["debug"] = True
     # program_args["display_detail_level"] = 3
     # program_args["display_profile_conditions"] = True
     # program_args['display_preferences'] = True
     # program_args['display_taskernet'] = True
 
-    # If we are debugging, output the runtime arguments and colors
-    if program_args["debug"]:
-        debug1(colormap, program_args, output_list)
-    # Prompt user for Tasker's backup.xml file location
-    if run_counter < 1:  # Only display message box on first run
-        msg = "Locate the Tasker backup xml file to use to map your Tasker environment"
-        title = "MapTasker"
-        messagebox.showinfo(title, msg)
-
-    # Open and read the file...
-    filename = initialize.open_and_get_backup_xml_file(program_args)
-
-    # Go get all the xml data
-    tree, root, all_tasker_items = get_the_xml_data(filename)
-
-    # Check for valid Tasker backup.xml file
-    if root.tag != "TaskerData":
-        error_msg = "You did not select a Tasker backup XML file...exit 2"
-        build_output.my_output(colormap, program_args, output_list, 0, error_msg)
-        logger.debug(f"{error_msg}exit 3")
-        sys.exit(3)
-    else:
-        heading = (
-            f'<span style="color:Green"</span>{heading}    Tasker version:'
-            f' {root.attrib["tv"]}'
-        )
-
-    # Start the output with heading
-    build_output.my_output(colormap, program_args, output_list, 0, heading)
-    # Start Project list
-    build_output.my_output(colormap, program_args, output_list, 1, "")
-
     #######################################################################################
     # Process Tasker Preferences
     #######################################################################################
     if program_args["display_preferences"]:
         get_preferences(
             output_list,
             program_args,
```

### Comparing `maptasker-1.3.1/maptasker/src/parsearg.py` & `maptasker-1.3.2/maptasker/src/parsearg.py`

 * *Files identical despite different names*

### Comparing `maptasker-1.3.1/maptasker/src/prefers.py` & `maptasker-1.3.2/maptasker/src/prefers.py`

 * *Files 6% similar despite different names*

```diff
@@ -13,28 +13,29 @@
 # ########################################################################################## #
 import gc
 import re
 from operator import itemgetter
 
 from maptasker.src.outputl import my_output
 from maptasker.src.servicec import service_codes
+from maptasker.src.sysconst import FONT_TO_USE
 
 
 def process_service(
     colormap: dict, service_name: str, service_value: str, output_lines: list
 ) -> None:
     """
     We have a service xml element that we have mapped as a preference.  Process it.
         :param colormap: colors to use in output
         :param service_name: name of the preference in <Service xml
         :param service_value: value of the preference in <Service xml
         :param output_lines: accumulated output lines generated thus far (to append to)
     """
     preferences_html = (
-        ' <span style = "color:' + colormap["preferences_color"] + '"</span>'
+        " <span style=\"color:" + colormap["preferences_color"] + FONT_TO_USE + '>'
     )
     blank = "&nbsp;"
 
     # Get the name to display
     output_service_name = service_codes[service_name]["display"]
     # Left justify and fill to 15 characters
     output_service_name = output_service_name.ljust(45, '.')
@@ -59,15 +60,15 @@
         service_value = package_names
 
     # Add the output details to our list of output stuff
     output_lines.append(
         [
             service_codes[service_name]['num'],
             (
-                f"{preferences_html}{blank * 2}{output_service_name}{blank * 4}{service_value}"
+                f"{preferences_html}{blank * 2}{output_service_name}{blank * 4}{service_value}</span>"
             ),
         ]
     )
 
 
 def get_preferences(
     output_list: list, program_args: dict, colormap: dict, all_tasker_items: dict
@@ -94,28 +95,28 @@
         "Action > Reset Error Notifications",
         "Misc",
         "Misc > Debugging",
         "Unlisted (Perhaps Deprecated)",
     ]
     output_lines = []
     preferences_html = (
-        ' <span style = "color:' + colormap["preferences_color"] + '"</span>'
+        ' <span style="color:' + colormap["preferences_color"] + FONT_TO_USE + '>'
     )
     blank = "&nbsp;"
     first_time = True
 
     # Output title line
     my_output(
         colormap,
         program_args,
         output_list,
         4,
         (
             f"{preferences_html}Tasker Preferences"
-            " >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
+            " >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>></span>"
         ),
     )
 
     # Go through each <Service xml element
     current_section = 999
     dummy_num = 100
     for service in all_tasker_items["all_services"]:
@@ -135,15 +136,15 @@
                 output_lines.append([dummy_num, "<br>"])
             # Add the output details to our list of output stuff
             output_lines.append(
                 [
                     dummy_num,
                     (
                         f"{preferences_html}&nbsp;&nbsp;Not yet mapped:"
-                        f" {service_name}{blank * 4}type:{service_type}{blank * 4}value:{service_value}"
+                        f" {service_name}{blank * 4}type:{service_type}{blank * 4}value:{service_value}</span>"
                     ),
                 ]
             )
             dummy_num += 1
 
     # All service xml elements have been processed.
     # Sort our output by order of display in Tasker (key=list element 0)
@@ -160,15 +161,15 @@
                 my_output(
                     colormap,
                     program_args,
                     output_list,
                     4,
                     (
                         f"<br>{preferences_html}&nbsp;Section:"
-                        f" {section_names[item[1]['section']]}"
+                        f" {section_names[item[1]['section']]}</span>"
                     ),
                 )
                 current_section = item[1]["section"]
         my_output(colormap, program_args, output_list, 4, line[1])
 
     my_output(
         colormap,
```

### Comparing `maptasker-1.3.1/maptasker/src/priority.py` & `maptasker-1.3.2/maptasker/src/priority.py`

 * *Files identical despite different names*

### Comparing `maptasker-1.3.1/maptasker/src/proclist.py` & `maptasker-1.3.2/maptasker/src/proclist.py`

 * *Files 3% similar despite different names*

```diff
@@ -54,21 +54,25 @@
         temp_item = ""
         temp_list = ""
         if program_args["debug"]:  # Add Task ID if in debug mode
             logger.debug(
                 "process_list "
                 f" the_item:{str(the_item)} the_list:{the_list} list_type:{list_type}"
             )
-        elif "⎯Task:" in list_type:
+        # If "--Task:" then this is a Task under a Scene.
+        # Need to temporarily save the_item since my_output changes the_item
+        if "&#45;&#45;Task:" in list_type:
             temp_item = the_item
             temp_list = list_type
             the_item = ""
-            id_loc = list_type.find("ID:")
-            if id_loc != -1:
-                list_type = list_type[:id_loc]
+            if program_args["debug"]:  # Get the Task ID
+                id_loc = list_type.find("ID:")
+                if id_loc != -1:
+                    list_type = f'{list_type}{str(id_loc)}'
+            # list_type = list_type.replace("&#45;&#45;Task:", "&nbsp;&nbsp;Task:")
 
         # Add this Task to the output
         my_output(
             colormap, program_args, output_list, 2, f"{list_type}&nbsp;{the_item}"
         )
         if temp_item:  # Put the_item back with the 'ID: nnn' portion included.
             the_item = temp_item
```

#### encoding

```diff
@@ -1 +1 @@
-utf-8
+us-ascii
```

### Comparing `maptasker-1.3.1/maptasker/src/profiles.py` & `maptasker-1.3.2/maptasker/src/profiles.py`

 * *Files 2% similar despite different names*

```diff
@@ -11,18 +11,19 @@
 # preserved. Contributors provide an express grant of patent rights.                         #
 #                                                                                            #
 # ########################################################################################## #
 import xml.etree.ElementTree  # Need for type hints
 
 import maptasker.src.condition as condition
 import maptasker.src.tasks as tasks
-from maptasker.src.kidapp import get_kid_app
+
+# from maptasker.src.kidapp import get_kid_app
 from maptasker.src.outputl import my_output
 from maptasker.src.outputl import refresh_our_output
-from maptasker.src.priority import get_priority
+
 from maptasker.src.share import share
 from maptasker.src.sysconst import NO_PROFILE
 
 
 # #######################################################################################
 # Get a specific Profile's Tasks (maximum of two:entry and exit)
 # #######################################################################################
@@ -69,97 +70,106 @@
     profile: xml.etree,
     output_list: list,
     program_args: dict,
     colormap: dict,
 ) -> tuple:
     # Set up html to use
     profile_color_html = (
-        '<span style = "color:'
+        '<span style="color:'
         + colormap["profile_color"]
-        + '"</span>'
         + program_args["font_to_use"]
+        + "></span>"
     )
     disabled_profile_html = (
-        ' <span style = "color:'
+        '<span style="color:'
         + colormap["disabled_profile_color"]
-        + '"</span>[DISABLED] '
+        + program_args["font_to_use"]
+        + '>[DISABLED]</span>'
     )
     launcher_task_html = (
-        ' <span style = "color:'
+        '  style="color:'
         + colormap["launcher_task_color"]
-        + '"</span>[Launcher Task] '
+        + '"[Launcher Task]'
         + profile_color_html
     )
     condition_color_html = (
-        ' <span style = "color:' + colormap["profile_condition_color"] + '"</span>'
+        '<span style="color:'
+        + colormap["profile_condition_color"]
+        + program_args["font_to_use"]
+        + '>'
     )
     profile_condition = ""
 
     # Look for disabled Profile
     limit = profile.find("limit")  # Is the Profile disabled?
     if limit is not None and limit.text == "true":
         disabled = disabled_profile_html
     else:
         disabled = ""
     launcher_xml = project.find(
         "ProfileVariable"
     )  # Is there a Launcher Task with this Project?
     launcher = launcher_task_html if launcher_xml is not None else ""
 
-    # See if there is a Kid app and/or Priority
-    kid_app_info = ''
-    if program_args["display_detail_level"] == 3:
-        kid_app_info = get_kid_app(profile)
-        priority = get_priority(profile, False)
+    # See if there is a Kid app and/or Priority (FOR FUTURE USE)
+    # kid_app_info = ''
+    # if program_args["display_detail_level"] == 3:
+    #     kid_app_info = get_kid_app(profile)
+    #     priority = get_priority(profile, False)
+
+    # Display flags for debug mode
+    flags = ""
+    if program_args["debug"]:
+        flags = profile.find("flags")
+        if flags is not None:
+            flags = (
+                f' <span style="color:GreenYellow{program_args["font_to_use"]}>flags:'
+                f' {flags.text}</span><span'
+                f' style="color:Red{program_args["font_to_use"]}>'
+            )
 
     # Check for Profile 'conditions'
     profile_name = ""
     if program_args["display_profile_conditions"]:
         profile_condition = condition.parse_profile_condition(
             profile, colormap, program_args
         )  # Get the Profile's condition
         if profile_condition:
             profile_name = (
-                f"{condition_color_html} ({profile_condition})"
-                f" {profile_name}{launcher}{disabled}"
+                f"{condition_color_html} ({profile_condition})</span>"
+                f" {profile_name}{launcher}{disabled} {flags}</span>"
             )
 
     # Start formulating the Profile output line
     try:
         profile_name = profile.find("nme").text + profile_name  # Get Profile's name
     except Exception as e:  # no Profile name
         if program_args["display_profile_conditions"]:
             profile_condition = condition.parse_profile_condition(
                 profile, colormap, program_args
             )  # Get the Profile's condition
-            if profile_condition:
-                profile_name = (
-                    NO_PROFILE
-                    + condition_color_html
-                    + " ("
-                    + profile_condition
-                    + ") "
-                    + profile_color_html
-                    + launcher
-                    + disabled
-                )
-            else:
-                profile_name = profile_name + NO_PROFILE + launcher + disabled
+            profile_name = (
+                f"{NO_PROFILE}</span>{condition_color_html} ({profile_condition})</span>"
+                f" {profile_color_html}{launcher}{disabled}{flags}"
+                if profile_condition
+                else profile_name + NO_PROFILE + launcher + disabled
+            )
         else:
             profile_name = profile_name + NO_PROFILE + launcher + disabled
+
     if program_args["debug"]:
         profile_id = profile.find("id").text
         profile_name = f"{profile_name} ID:{profile_id}"
     # Output the Profile line
     my_output(
         colormap,
         program_args,
         output_list,
         2,
-        f"{profile_color_html}Profile: {profile_name}",
+        f"Profile: {profile_name}",
     )
     return limit, launcher, profile_condition, profile_name
 
 
 # #######################################################################################
 # process_projects: go through all Projects Profiles...and output them
 # #######################################################################################
@@ -246,14 +256,15 @@
             profile_name,
             list_of_found_tasks,
             heading,
             colormap,
             program_args,
             all_tasker_items,
             found_items,
+            True,
         )
 
         # Get out if doing a specific Task, and it was found
         if (
             specific_task
             and program_args["single_task_name"]
             and found_items["single_task_found"]
```

### Comparing `maptasker-1.3.1/maptasker/src/progargs.py` & `maptasker-1.3.2/maptasker/src/progargs.py`

 * *Files 7% similar despite different names*

```diff
@@ -35,10 +35,10 @@
         (
             prog_args,
             colormap,
         ) = process_cli(colormap)
 
     # Are we in development mode?  If so, override debug argument
     if DEBUG_PROGRAM:
-        debug = True
+        prog_args["debug"] = True
 
     return prog_args, colormap
```

### Comparing `maptasker-1.3.1/maptasker/src/projects.py` & `maptasker-1.3.2/maptasker/src/projects.py`

 * *Files 6% similar despite different names*

```diff
@@ -20,14 +20,15 @@
 from maptasker.src.share import share
 from maptasker.src.kidapp import get_kid_app
 from maptasker.src.priority import get_priority
 from maptasker.src.getids import get_ids
 from maptasker.src.scenes import process_project_scenes
 import maptasker.src.tasks as tasks
 from maptasker.src.sysconst import NO_PROFILE
+from maptasker.src.sysconst import FONT_TO_USE
 
 
 # #######################################################################################
 # process_projects: go through all Projects Profiles...and output them
 # #######################################################################################
 def process_projects_and_their_profiles(
     output_list: list,
@@ -83,17 +84,18 @@
     """
     launcher_task_info = ""
     share_element = project.find("Share")
     if share_element is not None:
         launcher_task_element = share_element.find("t")
         if launcher_task_element is not None and launcher_task_element.text is not None:
             launcher_task_info = (
-                ' <span style = "color:'
+                '</span><span style="color:'
                 + colormap["launcher_task_color"]
-                + f'"</span>[Launcher Task: {launcher_task_element.text}] '
+                + FONT_TO_USE
+                + f'>[Launcher Task: {launcher_task_element.text}]</span> '
                 + project_color_html
             )
     return launcher_task_info
 
 
 # #############################################################################################
 # Process all Tasks in Project that are not referenced by a Profile
@@ -152,19 +154,21 @@
                 my_output(
                     colormap,
                     program_args,
                     output_list,
                     4,
                     (
                         '<br><span'
-                        f' style="color:{colormap["task_color"]}">&nbsp;&nbsp;&nbsp;The'
+                        f' style="color:{colormap["task_color"]};font-family:'
+                        f'{program_args["font_to_use"]}>&nbsp;&nbsp;&nbsp;The'
                         f' following Tasks in Project {project_name} are not in any'
                         ' Profile...</span><br>'
                     ),
                 )
+                my_output(colormap, program_args, output_list, 1, "")
                 output_the_heading = False
 
                 # Format the output line
             task_list = [
                 f"{our_task_name} <em>(Not referenced by any Profile in Project"
                 f" {project_name})</em>"
             ]
@@ -179,15 +183,18 @@
                 NO_PROFILE,
                 found_tasks,
                 heading,
                 colormap,
                 program_args,
                 all_tasker_items,
                 found_items,
+                True,
             )
+    # Force a line break
+    my_output(colormap, program_args, output_list, 4, "")
     return
 
 
 # #############################################################################################
 # Add extra info to Project output line as appropriate and then output it.
 # #############################################################################################
 def get_extra_and_output_project(
@@ -263,18 +270,18 @@
         :param colormap: output colors to use
         :param program_args: runtime arguments
         :param all_tasker_items: all Projects/Profiles/Tasks/Scenes
         :return: list of found Tasks
     """
     # Set up html to use
     project_color_html = (
-        '<span style = "color:'
+        '<span style="color:'
         + colormap["project_color"]
-        + '"</span>'
         + program_args["font_to_use"]
+        + ">"
     )
 
     for project in all_tasker_items["all_projects"]:
         # Don't bother with another Project if we've done a single Task or Profile only
         if found_items["single_task_found"] or found_items["single_profile_found"]:
             break
         project_name = project.find("name").text
@@ -295,27 +302,23 @@
         ):
             continue
 
         # Process any <Share> information from TaskerNet
         if program_args["display_taskernet"]:
             share(project, colormap, program_args, output_list)
 
-        # Get Profiles IDs
-        profile_ids = get_ids(
+        if profile_ids := get_ids(
             True,
             program_args,
             colormap,
             output_list,
             project,
             project_name,
             projects_without_profiles,
-        )
-
-        if profile_ids != "":
-            # Process the Project's Profiles
+        ):
             our_task_element = process_profiles(
                 output_list,
                 project,
                 project_name,
                 profile_ids,
                 found_tasks,
                 program_args,
@@ -327,15 +330,27 @@
 
             # Go to next Project if we are looking for a specific Profile and didn't find it.
             if (
                 program_args["single_profile_name"]
                 and not found_items["single_profile_found"]
             ):
                 continue  # On to next Project
-
+        else:
+            my_output(
+                colormap,
+                program_args,
+                output_list,
+                2,
+                (
+                    '</span><span style="color:'
+                    + colormap["profile_color"]
+                    + FONT_TO_USE
+                    + '><em>Project has no Profiles</em></span>'
+                ),
+            )
         my_output(colormap, program_args, output_list, 3, "")  # Close Profile list
 
         # # See if there are Tasks in Project that have no Profile
         if task_ids := get_ids(False, {}, {}, [], project, project_name, []):
             # Process Tasks in Project that are not referenced by a Profile
             tasks_not_in_profiles(
                 task_ids,
```

### Comparing `maptasker-1.3.1/maptasker/src/runcli.py` & `maptasker-1.3.2/maptasker/src/runcli.py`

 * *Files identical despite different names*

### Comparing `maptasker-1.3.1/maptasker/src/rungui.py` & `maptasker-1.3.2/maptasker/src/rungui.py`

 * *Files identical despite different names*

### Comparing `maptasker-1.3.1/maptasker/src/scenes.py` & `maptasker-1.3.2/maptasker/src/scenes.py`

 * *Files 3% similar despite different names*

```diff
@@ -62,16 +62,17 @@
     element_name = name_xml_element.text
     my_output(
         colormap,
         program_args,
         output_list,
         4,
         (
-            f'<span style="color:{colormap["scene_color"]}">&nbsp;&nbsp;&nbsp;Element:'
-            f' {element_type[0]} named {element_name}'
+            '<span'
+            f' style="color:{colormap["scene_color"]}{program_args["font_to_use"]}>&nbsp;&nbsp;&nbsp;Element:'
+            f' {element_type[0]} named {element_name}</span>'
         ),
     )
 
     return
 
 
 def process_scene(
@@ -119,28 +120,30 @@
                             temp_task_list,
                             "",
                             all_tasker_items["all_tasks"],
                         )
                         # reset to task name since get_task_name changes its value
                         temp_task_list = [sub_child.text]
                         extra = "&nbsp;&nbsp;ID:"
-                        task_type = f"⎯Task: {SCENE_TASK_TYPES[sub_child.tag]}{extra}"
+                        task_type = (
+                            "&nbsp;&#45;&#45;Task:"
+                            f" {SCENE_TASK_TYPES[sub_child.tag]}{extra}"
+                        )
+                        # process the Scene's Task
                         process_list(
                             task_type,
                             output_list,
                             temp_task_list,
                             task_element,
                             tasks_found,
                             program_args,
                             colormap,
                             all_tasker_items,
-                        )  # process the Scene's Task
-                        my_output(
-                            colormap, program_args, output_list, 3, ""
-                        )  # End list
+                        )
+                        my_output(colormap, program_args, output_list, 1, "")
                     else:
                         break
                 elif sub_child.tag == "Str":
                     break
     return
 
 
@@ -186,8 +189,10 @@
                 scene_list,
                 our_task_element,
                 found_tasks,
                 program_args,
                 colormap,
                 all_tasker_items,
             )
+            # Force a line break
+            my_output(colormap, program_args, output_list, 4, "")
     return
```

#### encoding

```diff
@@ -1 +1 @@
-utf-8
+us-ascii
```

### Comparing `maptasker-1.3.1/maptasker/src/servicec.py` & `maptasker-1.3.2/maptasker/src/servicec.py`

 * *Files identical despite different names*

### Comparing `maptasker-1.3.1/maptasker/src/share.py` & `maptasker-1.3.2/maptasker/src/share.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,22 +1,28 @@
 #! /usr/bin/env python3
 
+import re
+
 # ########################################################################################## #
 #                                                                                            #
 # share: process TaskerNet 'Share" information                                               #
 #                                                                                            #
 # GNU General Public License v3.0                                                            #
 # Permissions of this strong copyleft license are conditioned on making available            #
 # complete source code of licensed works and modifications, which include larger works       #
 # using a licensed work, under the same license. Copyright and license notices must be       #
 # preserved. Contributors provide an express grant of patent rights.                         #
 #                                                                                            #
 # ########################################################################################## #
 import xml.etree.ElementTree  # Need for type hints
+
+
 from maptasker.src.outputl import my_output
+from maptasker.src.xmldata import remove_html_tags
+from maptasker.src.sysconst import FONT_TO_USE
 
 
 def share(
     root_element: xml.etree,
     colormap: dict,
     program_args: dict,
     output_list: list,
@@ -31,37 +37,54 @@
             description_element_output(
                 description_element, colormap, program_args, output_list
             )
         # Look for search parameters
         search_element = share_element.find("g")
         if search_element is not None and search_element.text:
             # Found search...format and output
-            my_output(colormap, program_args, output_list, 3, "")  # Force new line
-            out_string = f"TaskerNet search on: {search_element.text}"
+            # my_output(colormap, program_args, output_list, 4, "")  # Force new line
+            out_string = f"&nbsp;&nbsp;TaskerNet search on: {search_element.text}"
             my_output(colormap, program_args, output_list, 2, out_string)
 
 
 # Process the description <d> element
 def description_element_output(
-    description_element, colormap, program_args, output_list
-):
+    description_element: str, colormap: dict, program_args: dict, output_list: list
+) -> str:
+    """
+    We have a Taskernet description (<Share>).  Process it
+        :param description_element: the xml element with the description
+        :param colormap: the colors to use for the output
+        :param program_args: the runtime arguments
+        :param output_list: the output lines thus far
+    """
     # We need to properly format this since it has embedded stuff that screws it up
-    out_string = f"TaskerNet description: {description_element.text}"
-    indent_html = '<p style="margin-left:20px; margin-right:50px;">'
+    out_string = f"&nbsp;&nbsp;TaskerNet description: {description_element.text}"
+    indent_html = (
+        '</p><p'
+        f' style="margin-left:20px;margin-right:50px;color:{colormap["taskernet_color"]}{FONT_TO_USE}>'
+    )
 
-    # Indent the description
+    # Indent the description and override various embedded HTML attributes
     out_string = out_string.replace("<p>", indent_html)
     out_string = out_string.replace("<br/>", indent_html)
     out_string = out_string.replace("<h1>", indent_html)
+    out_string = out_string.replace("\r", indent_html)
+    out_string = out_string.replace("<li>", f'{indent_html}')
+    out_string = out_string.replace("</li>", "")
+    # out_string = remove_html_tags(out_string, indent_html)
+
     # Look for double blanks = line break
     new_line = ""
     if indent_html not in out_string:  # Only if we have not already formatted
         for position, character_index in enumerate(out_string):
             new_line = (
-                f'{new_line}<p style="margin-left:20px; margin-right:50px;">'
-                if character_index == " " and out_string[position + 1] == " "
+                f'{new_line}<p style="margin-left:20px;'
+                f'margin-right:50px;color:{colormap["taskernet_color"]}{FONT_TO_USE}>'
+                if (character_index == " " and out_string[position + 1] == " ")
+                or (character_index == "-" and out_string[position + 1] == " ")
                 else new_line + character_index
             )
         out_string = new_line
-
+    out_string = f'{out_string}'
     # Output the description line
     my_output(colormap, program_args, output_list, 2, out_string)
```

### Comparing `maptasker-1.3.1/maptasker/src/shellsort.py` & `maptasker-1.3.2/maptasker/src/shellsort.py`

 * *Files identical despite different names*

### Comparing `maptasker-1.3.1/maptasker/src/sysconst.py` & `maptasker-1.3.2/maptasker/src/sysconst.py`

 * *Files 1% similar despite different names*

```diff
@@ -12,20 +12,20 @@
 #                                                                                            #
 # ########################################################################################## #
 from maptasker.src.config import OUTPUT_FONT
 from maptasker.src.config import logging
 
 # Global constants
 UNKNOWN_TASK_NAME = "Unnamed/Anonymous."
-MY_VERSION = "MapTasker version 1.3.01"
+MY_VERSION = "MapTasker version 1.3.2"
 MY_LICENSE = "GNU GENERAL PUBLIC LICENSE (Version 3, 29 June 2007)"
 NO_PROJECT = "-none found."
 COUNTER_FILE = ".MapTasker_RunCount.txt"
-ARGUMENTS_FILE = ".arguments.txt"
-FONT_TO_USE = f"<font face={OUTPUT_FONT}>"
+ARGUMENTS_FILE = ".MapTasker_arguments.txt"
+FONT_TO_USE = f';font-family:{OUTPUT_FONT}"'
 NO_PROFILE = "None or unnamed!"
 
 #  List of color arguments and their names
 #  Two different key/value structures in one:
 #    1- Used as lookup for color selection in GUI.  E.g. key=Disabled Profiles
 #    2- Used as color lookup from runtime parameters.  E.g. DisabledProfile (must follow #1)
 #       Only needed for keys that are different between case #1 and case #2
```

### Comparing `maptasker-1.3.1/maptasker/src/taskactn.py` & `maptasker-1.3.2/maptasker/src/taskactn.py`

 * *Files 4% similar despite different names*

```diff
@@ -28,18 +28,19 @@
     program_args: dict,
     list_type: str,
     the_item: str,
     tasks_found: list[str],
     colormap: dict,
     all_tasks: dict,
 ) -> None:
-    # If Unknown task, then 'the_task' is not valid, and we have to find it.
+    # If Unknown task or displaying more detail, then 'the_task' is not valid, and we have to find it.
     if UNKNOWN_TASK_NAME in the_item or program_args["display_detail_level"] > 0:
         # Get the Task ID so that we can get the Task xml element
-        temp_id = 'x' if "⎯Task:" in list_type else the_item.split("Task ID: ")
+        # "--Task:" denotes a Task in a Scene
+        temp_id = 'x' if "&#45;&#45;Task:" in list_type else the_item.split("Task ID: ")
         # Get the Task xml element
         if len(temp_id) > 1:
             temp_id[1] = temp_id[1].split(' ', 1)[0]  # ID = 1st word of temp_id[1]
             the_task, kaka = tasks.get_task_name(
                 temp_id[1], tasks_found, [temp_id[1]], "", all_tasks
             )
         # Get Task actions
@@ -48,14 +49,18 @@
                 my_output(
                     colormap, program_args, output_list, 1, ""
                 )  # Start Action list
                 action_count = 1
                 output_list_of_actions(
                     colormap, program_args, output_list, action_count, alist, the_item
                 )
+                # End list if Scene Task
+                if "&#45;&#45;Task:" in list_type:
+                    my_output(colormap, program_args, output_list, 3, "")
+                    my_output(colormap, program_args, output_list, 3, "")
         else:
             error_msg = 'Error: No Task found!!!'
             logger.debug(error_msg)
             print(error_msg)
     return
 
 
@@ -91,15 +96,15 @@
                 my_output(colormap, program_args, output_list, 2, f"Action: {taction}")
             else:
                 my_output(
                     colormap,
                     program_args,
                     output_list,
                     2,
-                    f"Action: {str(action_count).zfill(2)} {taction}",
+                    f"Action: {str(action_count).zfill(2)} </span>{taction}",
                 )
                 action_count += 1
             if (
                 action_count == 2
                 and program_args["display_detail_level"] == 0
                 and UNKNOWN_TASK_NAME in the_item
             ):  # Just show first Task if unknown Task
```

#### encoding

```diff
@@ -1 +1 @@
-utf-8
+us-ascii
```

### Comparing `maptasker-1.3.1/maptasker/src/taskerd.py` & `maptasker-1.3.2/maptasker/src/taskerd.py`

 * *Files identical despite different names*

### Comparing `maptasker-1.3.1/maptasker/src/tasks.py` & `maptasker-1.3.2/maptasker/src/tasks.py`

 * *Files 22% similar despite different names*

```diff
@@ -54,16 +54,15 @@
         # Task's Action statements can be out-of-order, and we need them in proper-order/sequence
         # sort the Task's Actions by attrib sr (e.g. sr='act0', act1, act2, etc.) to get them in true order
         if len(task_actions) > 0:
             shell_sort(task_actions, True, False)
         # Now go through each Action to start processing it.
         for action in task_actions:
             child = action.find("code")  # Get the <code> element
-            # if create_dictionary:  # Are we creating a dictionary for Actions?
-            #     process_action_codes.build_action_code(child, action, 't')
+            # Get the Action code ( <code> )
             task_code = action_evaluate.get_action_code(
                 child, action, True, colormap, "t", prog_args
             )
             logger.debug(
                 "Task ID:"
                 + str(action.attrib["sr"])
                 + " Code:"
@@ -71,28 +70,26 @@
                 + " task_code:"
                 + task_code
                 + "Action attr:"
                 + str(action.attrib)
             )
             # Calculate the amount of indention required
             if (
-                "</span>End If" in task_code
-                or "</span>Else" in task_code
-                or "</span>End For" in task_code
+                ">End If" in task_code
+                or ">Else" in task_code
+                or ">End For" in task_code
             ):  # Do we un-indent?
                 indentation -= 1
                 length_indent = len(indentation_amount)
                 indentation_amount = indentation_amount[24:length_indent]
             action_evaluate.build_action(
                 tasklist, task_code, child, indentation, indentation_amount
             )
             if (
-                "</span>If" in task_code
-                or "</span>Else" in task_code
-                or "</span>For" in task_code
+                ">If" in task_code or ">Else" in task_code or ">For" in task_code
             ):  # Do we indent?
                 indentation += 1
                 indentation_amount = f"{indentation_amount}&nbsp;&nbsp;&nbsp;&nbsp;"
 
     return tasklist
 
 
@@ -151,14 +148,21 @@
 
 # #######################################################################################
 # Find the Project belonging to the Task id passed in
 # #######################################################################################
 def get_project_for_solo_task(
     the_task_id: str, projects_with_no_tasks: list, all_projects: dict
 ) -> tuple[str, xml.etree]:
+    """
+    Find the Project belonging to the Task id passed in
+        :param the_task_id: the ID of the Task
+        :param projects_with_no_tasks: list of Projects that do not have any Tasks
+        :param all_projects: all Tasker Projects
+        :return: name of the Project that belongs to this task and the Project xml element
+    """
     proj_name = NO_PROJECT
     project = None
     if all_projects is not None:
         # Go through each Project
         for project in all_projects:
             proj_name = project.find("name").text
             task_ids = get_ids(
@@ -168,48 +172,71 @@
                 return proj_name, project
     return proj_name, project
 
 
 # #######################################################################################
 # Identify whether the Task passed in is part of a Scene: True = yes, False = no
 # #######################################################################################
-def task_in_scene(the_task_id, all_scenes):
-    for scene in all_scenes:
-        for child in all_scenes[scene]:  # Go through sub-elements in the Scene element
+def task_in_scene(the_task_id: str, all_scenes: dict) -> bool:
+    """
+    Identify whether the Task passed in is part of a Scene: True = yes, False = no
+        :param the_task_id: the id of the Task to check against
+        :param all_scenes: all Scenes in Tasker configuration
+        :return: True if Task is part of a Scene, False otherwise
+    """
+    # Go through each Scene
+    for value in all_scenes.values():
+        for child in value:  # Go through sub-elements in the Scene element
             if tag_in_type(child.tag, True):
                 for subchild in child:  # Go through xxxxElement sub-items
-                    if tag_in_type(subchild.tag, False):
-                        if (
-                            the_task_id == subchild.text
-                        ):  # Is this Task in this specific Scene (child)?
-                            return True
+                    # Is this Task in this specific Scene (child)?
+                    if (
+                        tag_in_type(subchild.tag, False)
+                        and the_task_id == subchild.text
+                    ):
+                        return True
                     elif child.tag == "Str":  # Passed any click Task
                         break
                     else:
                         continue
     return False
 
 
 # #######################################################################################
 # We're processing a single task only
 # #######################################################################################
 def do_single_task(
-    our_task_name,
-    output_list,
-    project_name,
-    profile_name,
-    heading,
-    found_items,
-    task_list,
-    our_task_element,
-    list_of_found_tasks,
-    all_tasker_items,
-    colormap,
-    program_args,
-):
+    our_task_name: str,
+    output_list: list,
+    project_name: str,
+    profile_name: str,
+    heading: str,
+    found_items: dict,
+    task_list: list,
+    our_task_element: xml.etree,
+    list_of_found_tasks: list,
+    all_tasker_items: dict,
+    colormap: dict,
+    program_args: dict,
+) -> None:
+    """
+    Process a single Task only
+        :param our_task_name: name of the Task to process
+        :param output_list: where the output line goes for Task
+        :param project_name: name of the Project Task belongs to
+        :param profile_name: name of the Profile the Task belongs to
+        :param heading: the heading, if any
+        :param found_items: single name for Project/Profile/Task
+        :param task_list: list of Tasks
+        :param our_task_element: the xml element for this Task
+        :param list_of_found_tasks: all Tasks processed so far
+        :param all_tasker_items: all Projects/Profiles/Tasks/Scenes
+        :param colormap: colors to use in output
+        :param program_args: runtime arguments
+    """
     # Do NOT move this import.  Otherwise, will get recursion error
     from maptasker.src.proclist import process_list
 
     logger.debug(
         f'tasks single task name:{program_args["single_task_name"]} our Task'
         f' name:{our_task_name}'
     )
@@ -263,17 +290,17 @@
                     task_list,
                     our_task_element,
                     list_of_found_tasks,
                     program_args,
                     colormap,
                     all_tasker_items,
                 )
-                build_output.my_output(
-                    colormap, program_args, output_list, 3, ""
-                )  # End Task list
+                # build_output.my_output(
+                #     colormap, program_args, output_list, 3, ""
+                # )  # End Task list
                 break
 
 
 # #######################################################################################
 # output_task: we have a Task and need to generate the output
 # #######################################################################################
 def output_task(
@@ -285,14 +312,15 @@
     profile_name: str,
     list_of_found_tasks: list,
     heading: str,
     colormap: dict,
     program_args: dict,
     all_tasker_items: dict,
     found_items: dict,
+    do_extra: bool,
 ) -> bool:
     """
     We have a single Task or a list of Tasks.  Output it/them.
         :param output_list: list of output lines generated thus far
         :param our_task_name: name of Task
         :param our_task_element: Task xml element
         :param task_list: Task list
@@ -300,45 +328,43 @@
         :param profile_name: name of current Profile
         :param list_of_found_tasks: list of Tasks found so far
         :param heading: current heading
         :param colormap: colors to use in output
         :param program_args: runtime arguments
         :param all_tasker_items: all Projects/Profiles/Tasks/Scenes
         :param found_items: single Project/Profile/Task to search for
+        :param do_extra: flag to do/output extra Task stuff
         :return: True if we are searching for a single Task and found it.  Otherwise, False
     """
     # Do NOT move this import.  Otherwise, will get recursion error
     from maptasker.src.proclist import process_list
 
     # See if there is a Kid app and/or Priority
-    if program_args["display_detail_level"] == 3:
+    if do_extra and program_args["display_detail_level"] == 3:
         if kid_app_info := get_kid_app(our_task_element):
             task_list[0] = f'{task_list[0]} {kid_app_info}'
         if priority := get_priority(our_task_element, False):
             task_list[0] = f'{task_list[0]} {priority}'
 
     # Looking for a single Task?
-    if (
-        our_task_name != "" and program_args["single_task_name"]
-    ):  # Are we mapping just a single Task?
+    if our_task_name != "" and program_args["single_task_name"]:
         do_single_task(
             our_task_name,
             output_list,
             project_name,
             profile_name,
             heading,
             found_items,
             task_list,
             our_task_element,
             list_of_found_tasks,
             all_tasker_items,
             colormap,
             program_args,
         )
-
         return True  # Call it quits on Task...we have the one we want
     elif task_list:
         # Start a list
         build_output.my_output(colormap, program_args, output_list, 1, "")
         # Process the list of Task(s)
         process_list(
             "Task:",
@@ -346,12 +372,11 @@
             task_list,
             our_task_element,
             list_of_found_tasks,
             program_args,
             colormap,
             all_tasker_items,
         )
-        build_output.my_output(
-            colormap, program_args, output_list, 3, ""
-        )  # End Task list
+        # End Task list
+        build_output.my_output(colormap, program_args, output_list, 3, "")
 
     return False  # Normal Task...continue processing them
```

### Comparing `maptasker-1.3.1/maptasker/src/taskuniq.py` & `maptasker-1.3.2/maptasker/src/taskuniq.py`

 * *Files 4% similar despite different names*

```diff
@@ -36,45 +36,52 @@
         build_output.my_output(
             colormap,
             program_args,
             output_list,
             0,
             (
                 '<hr><span'
-                f' style=color={colormap["trailing_comments_color"]}"{FONT_TO_USE}</font><em>Projects</font>'
-                ' Without Tasks...</em>'
+                f' style="color:{colormap["trailing_comments_color"]}{FONT_TO_USE}><em>Projects'
+                ' Without Tasks...</em></span>'
             ),
         )
         for item in projects_with_no_tasks:
             build_output.my_output(
-                colormap, program_args, output_list, 4, f"Project {item} has no Tasks"
+                colormap,
+                program_args,
+                output_list,
+                4,
+                (
+                    f'<span style="color:{colormap["trailing_comments_color"]}'
+                    f'{FONT_TO_USE}>Project {item} has no Tasks</span>'
+                ),
             )
 
     # List all Projects without Profiles
     if projects_without_profiles:
         build_output.my_output(
             colormap,
             program_args,
             output_list,
             0,
             (
                 '<hr><span'
-                f' style="color:{colormap["trailing_comments_color"]}">{FONT_TO_USE}</font><em>Projects'
+                f' style=color:{colormap["trailing_comments_color"]}{FONT_TO_USE}><em>Projects'
                 ' Without Profiles...</em>'
             ),
         )
         for item in projects_without_profiles:
             build_output.my_output(
                 colormap,
                 program_args,
                 output_list,
                 4,
                 (
                     '<span'
-                    f' style="color:{colormap["trailing_comments_color"]}">{FONT_TO_USE}</font>Project'
+                    f' style="color:{colormap["trailing_comments_color"]}{FONT_TO_USE}>Project'
                     f' {item} has no Profiles'
                 ),
             )
     return
 
 
 # #######################################################################################
@@ -122,17 +129,17 @@
         )  # blank line
         build_output.my_output(
             colormap,
             program_args,
             output_list,
             0,
             (
-                f'<font color="{colormap["trailing_comments_color"]}"'
-                + program_args["font_to_use"]
-                + "Tasks that are not called by any Profile..."
+                '<span'
+                f' style="color:{colormap["trailing_comments_color"]}{program_args["font_to_use"]}>'
+                + "Tasks that are not called by any Profile...<span>"
             ),
         )
         build_output.my_output(
             colormap, program_args, output_list, 1, ""
         )  # Start Task list
         have_heading = True
 
@@ -161,14 +168,15 @@
             "None",
             [],
             heading,
             colormap,
             program_args,
             all_tasker_items,
             found_items,
+            False,
         )
     return have_heading, specific_task, unnamed_task_count
 
 
 # #######################################################################################
 # process_tasks: go through all tasks and output them
 # #######################################################################################
@@ -230,17 +238,18 @@
         ):
             build_output.my_output(
                 colormap,
                 program_args,
                 output_list,
                 0,
                 (
-                    f'<font color={colormap["unknown_task_color"]}>There are a total of'
-                    f' {unnamed_task_count} unnamed Tasks not associated with a'
-                    ' Profile!'
+                    '<span'
+                    f' style="color:{colormap["unknown_task_color"]}{program_args["font_to_use"]}>There'
+                    f' are a total of {unnamed_task_count} unnamed Tasks not associated'
+                    ' with a Profile!</span>'
                 ),
             )
 
     if task_name is True:
         build_output.my_output(
             colormap, program_args, output_list, 3, ""
         )  # Close Task list
```

### Comparing `maptasker-1.3.1/maptasker/src/userintr.py` & `maptasker-1.3.2/maptasker/src/userintr.py`

 * *Files identical despite different names*

### Comparing `maptasker-1.3.1/pyproject.toml` & `maptasker-1.3.2/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "maptasker"
-version = "1.3.01"
+version = "1.3.2"
 description = "Utility to display your entire Android 'Tasker' configuration on your MAC."
 authors = ["Michael Rubin <mikrubin@gmail.com>"]
 readme = "README_PyPl.md"
 license = "GPL-3.0-or-later"
 repository = "https://github.com/mctinker/Map-Tasker"
 keywords = ["tasker", "Tasker", "map tasker"]
 packages = [
```

### Comparing `maptasker-1.3.1/PKG-INFO` & `maptasker-1.3.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: maptasker
-Version: 1.3.1
+Version: 1.3.2
 Summary: Utility to display your entire Android 'Tasker' configuration on your MAC.
 Home-page: https://github.com/mctinker/Map-Tasker
 License: GPL-3.0-or-later
 Keywords: tasker,Tasker,map tasker
 Author: Michael Rubin
 Author-email: mikrubin@gmail.com
 Requires-Python: >=3.10,<4.0
```

