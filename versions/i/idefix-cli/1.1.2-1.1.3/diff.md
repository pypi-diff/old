# Comparing `tmp/idefix_cli-1.1.2.tar.gz` & `tmp/idefix_cli-1.1.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "idefix_cli-1.1.2.tar", last modified: Fri Mar  3 18:11:02 2023, max compression
+gzip compressed data, was "idefix_cli-1.1.3.tar", last modified: Thu Apr  6 08:51:00 2023, max compression
```

## Comparing `idefix_cli-1.1.2.tar` & `idefix_cli-1.1.3.tar`

### file list

```diff
@@ -1,38 +1,38 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 18:11:02.685643 idefix_cli-1.1.2/
--rw-r--r--   0 runner    (1001) docker     (123)    35149 2023-03-03 18:10:53.000000 idefix_cli-1.1.2/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     2528 2023-03-03 18:11:02.685643 idefix_cli-1.1.2/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1995 2023-03-03 18:10:53.000000 idefix_cli-1.1.2/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 18:11:02.681643 idefix_cli-1.1.2/idefix_cli/
--rw-r--r--   0 runner    (1001) docker     (123)       22 2023-03-03 18:10:53.000000 idefix_cli-1.1.2/idefix_cli/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2102 2023-03-03 18:10:53.000000 idefix_cli-1.1.2/idefix_cli/_backports.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 18:11:02.681643 idefix_cli-1.1.2/idefix_cli/_commands/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-03 18:10:53.000000 idefix_cli-1.1.2/idefix_cli/_commands/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2965 2023-03-03 18:10:53.000000 idefix_cli-1.1.2/idefix_cli/_commands/clean.py
--rw-r--r--   0 runner    (1001) docker     (123)     3801 2023-03-03 18:10:53.000000 idefix_cli-1.1.2/idefix_cli/_commands/clone.py
--rw-r--r--   0 runner    (1001) docker     (123)     8644 2023-03-03 18:10:53.000000 idefix_cli-1.1.2/idefix_cli/_commands/conf.py
--rw-r--r--   0 runner    (1001) docker     (123)      718 2023-03-03 18:10:53.000000 idefix_cli-1.1.2/idefix_cli/_commands/read.py
--rw-r--r--   0 runner    (1001) docker     (123)     8951 2023-03-03 18:10:53.000000 idefix_cli-1.1.2/idefix_cli/_commands/run.py
--rw-r--r--   0 runner    (1001) docker     (123)     1680 2023-03-03 18:10:53.000000 idefix_cli-1.1.2/idefix_cli/_commands/stamp.py
--rw-r--r--   0 runner    (1001) docker     (123)     1256 2023-03-03 18:10:53.000000 idefix_cli-1.1.2/idefix_cli/_commands/write.py
--rw-r--r--   0 runner    (1001) docker     (123)     5503 2023-03-03 18:10:53.000000 idefix_cli-1.1.2/idefix_cli/_main.py
--rw-r--r--   0 runner    (1001) docker     (123)      364 2023-03-03 18:10:53.000000 idefix_cli-1.1.2/idefix_cli/_theme.py
--rw-r--r--   0 runner    (1001) docker     (123)    11754 2023-03-03 18:10:53.000000 idefix_cli-1.1.2/idefix_cli/lib.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 18:11:02.681643 idefix_cli-1.1.2/idefix_cli.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     2528 2023-03-03 18:11:02.000000 idefix_cli-1.1.2/idefix_cli.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      769 2023-03-03 18:11:02.000000 idefix_cli-1.1.2/idefix_cli.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-03 18:11:02.000000 idefix_cli-1.1.2/idefix_cli.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       83 2023-03-03 18:11:02.000000 idefix_cli-1.1.2/idefix_cli.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)      248 2023-03-03 18:11:02.000000 idefix_cli-1.1.2/idefix_cli.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       11 2023-03-03 18:11:02.000000 idefix_cli-1.1.2/idefix_cli.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1804 2023-03-03 18:10:53.000000 idefix_cli-1.1.2/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-03 18:11:02.685643 idefix_cli-1.1.2/setup.cfg
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 18:11:02.685643 idefix_cli-1.1.2/tests/
--rw-r--r--   0 runner    (1001) docker     (123)     3685 2023-03-03 18:10:53.000000 idefix_cli-1.1.2/tests/test_app_structure.py
--rw-r--r--   0 runner    (1001) docker     (123)     4636 2023-03-03 18:10:53.000000 idefix_cli-1.1.2/tests/test_clean.py
--rw-r--r--   0 runner    (1001) docker     (123)     2753 2023-03-03 18:10:53.000000 idefix_cli-1.1.2/tests/test_clone.py
--rw-r--r--   0 runner    (1001) docker     (123)     1480 2023-03-03 18:10:53.000000 idefix_cli-1.1.2/tests/test_commons.py
--rw-r--r--   0 runner    (1001) docker     (123)     1673 2023-03-03 18:10:53.000000 idefix_cli-1.1.2/tests/test_conf.py
--rw-r--r--   0 runner    (1001) docker     (123)      653 2023-03-03 18:10:53.000000 idefix_cli-1.1.2/tests/test_read.py
--rw-r--r--   0 runner    (1001) docker     (123)     2210 2023-03-03 18:10:53.000000 idefix_cli-1.1.2/tests/test_stamp.py
--rw-r--r--   0 runner    (1001) docker     (123)     1373 2023-03-03 18:10:53.000000 idefix_cli-1.1.2/tests/test_ux.py
--rw-r--r--   0 runner    (1001) docker     (123)     3635 2023-03-03 18:10:53.000000 idefix_cli-1.1.2/tests/test_write.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 08:51:00.335744 idefix_cli-1.1.3/
+-rw-r--r--   0 runner    (1001) docker     (123)    35149 2023-04-06 08:50:47.000000 idefix_cli-1.1.3/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     2528 2023-04-06 08:51:00.331744 idefix_cli-1.1.3/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1995 2023-04-06 08:50:47.000000 idefix_cli-1.1.3/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 08:51:00.327744 idefix_cli-1.1.3/idefix_cli/
+-rw-r--r--   0 runner    (1001) docker     (123)       22 2023-04-06 08:50:47.000000 idefix_cli-1.1.3/idefix_cli/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2102 2023-04-06 08:50:47.000000 idefix_cli-1.1.3/idefix_cli/_backports.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 08:51:00.331744 idefix_cli-1.1.3/idefix_cli/_commands/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 08:50:47.000000 idefix_cli-1.1.3/idefix_cli/_commands/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2965 2023-04-06 08:50:47.000000 idefix_cli-1.1.3/idefix_cli/_commands/clean.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3858 2023-04-06 08:50:47.000000 idefix_cli-1.1.3/idefix_cli/_commands/clone.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8644 2023-04-06 08:50:47.000000 idefix_cli-1.1.3/idefix_cli/_commands/conf.py
+-rw-r--r--   0 runner    (1001) docker     (123)      718 2023-04-06 08:50:47.000000 idefix_cli-1.1.3/idefix_cli/_commands/read.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8950 2023-04-06 08:50:47.000000 idefix_cli-1.1.3/idefix_cli/_commands/run.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1680 2023-04-06 08:50:47.000000 idefix_cli-1.1.3/idefix_cli/_commands/stamp.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1256 2023-04-06 08:50:47.000000 idefix_cli-1.1.3/idefix_cli/_commands/write.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5503 2023-04-06 08:50:47.000000 idefix_cli-1.1.3/idefix_cli/_main.py
+-rw-r--r--   0 runner    (1001) docker     (123)      364 2023-04-06 08:50:47.000000 idefix_cli-1.1.3/idefix_cli/_theme.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11754 2023-04-06 08:50:47.000000 idefix_cli-1.1.3/idefix_cli/lib.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 08:51:00.331744 idefix_cli-1.1.3/idefix_cli.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     2528 2023-04-06 08:51:00.000000 idefix_cli-1.1.3/idefix_cli.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      769 2023-04-06 08:51:00.000000 idefix_cli-1.1.3/idefix_cli.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 08:51:00.000000 idefix_cli-1.1.3/idefix_cli.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       83 2023-04-06 08:51:00.000000 idefix_cli-1.1.3/idefix_cli.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      248 2023-04-06 08:51:00.000000 idefix_cli-1.1.3/idefix_cli.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       11 2023-04-06 08:51:00.000000 idefix_cli-1.1.3/idefix_cli.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1780 2023-04-06 08:50:47.000000 idefix_cli-1.1.3/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 08:51:00.335744 idefix_cli-1.1.3/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 08:51:00.331744 idefix_cli-1.1.3/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)     3685 2023-04-06 08:50:47.000000 idefix_cli-1.1.3/tests/test_app_structure.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4636 2023-04-06 08:50:47.000000 idefix_cli-1.1.3/tests/test_clean.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2791 2023-04-06 08:50:47.000000 idefix_cli-1.1.3/tests/test_clone.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1480 2023-04-06 08:50:47.000000 idefix_cli-1.1.3/tests/test_commons.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1673 2023-04-06 08:50:47.000000 idefix_cli-1.1.3/tests/test_conf.py
+-rw-r--r--   0 runner    (1001) docker     (123)      653 2023-04-06 08:50:47.000000 idefix_cli-1.1.3/tests/test_read.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2210 2023-04-06 08:50:47.000000 idefix_cli-1.1.3/tests/test_stamp.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1373 2023-04-06 08:50:47.000000 idefix_cli-1.1.3/tests/test_ux.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3635 2023-04-06 08:50:47.000000 idefix_cli-1.1.3/tests/test_write.py
```

### Comparing `idefix_cli-1.1.2/LICENSE` & `idefix_cli-1.1.3/LICENSE`

 * *Files identical despite different names*

### Comparing `idefix_cli-1.1.2/PKG-INFO` & `idefix_cli-1.1.3/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: idefix_cli
-Version: 1.1.2
+Version: 1.1.3
 Summary: A CLI to automate mundane tasks with Idefix
 Author: C.M.T. Robert
 License: GPL-3.0
 Project-URL: Homepage, https://github.com/neutrinoceros/idefix_cli
 Classifier: License :: OSI Approved :: GNU General Public License v3 (GPLv3)
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3 :: Only
```

### Comparing `idefix_cli-1.1.2/README.md` & `idefix_cli-1.1.3/README.md`

 * *Files identical despite different names*

### Comparing `idefix_cli-1.1.2/idefix_cli/_backports.py` & `idefix_cli-1.1.3/idefix_cli/_backports.py`

 * *Files identical despite different names*

### Comparing `idefix_cli-1.1.2/idefix_cli/_commands/clean.py` & `idefix_cli-1.1.3/idefix_cli/_commands/clean.py`

 * *Files identical despite different names*

### Comparing `idefix_cli-1.1.2/idefix_cli/_commands/clone.py` & `idefix_cli-1.1.3/idefix_cli/_commands/clone.py`

 * *Files 2% similar despite different names*

```diff
@@ -93,15 +93,16 @@
             if shallow:
                 os.symlink(fd, fdest)
             elif os.path.isfile(fd):
                 shutil.copy(fd, fdest)
             elif os.path.isdir(fd):
                 subdir = os.path.join(tmpdir, os.path.basename(fd))
                 os.mkdir(subdir)
-                recursive_write(tmpdir=subdir, files_and_dirs=os.listdir(fd))
+                files_and_dirs = [os.path.join(fd, _) for _ in os.listdir(fd)]
+                recursive_write(subdir, files_and_dirs)
             else:
                 raise RuntimeError(
                     "If you see this error message, please report to "
                     "https://github.com/neutrinoceros/idefix_cli/issues/new"
                 )
 
     with TemporaryDirectory(dir=os.path.dirname(dest)) as tmpdir:
```

### Comparing `idefix_cli-1.1.2/idefix_cli/_commands/conf.py` & `idefix_cli-1.1.3/idefix_cli/_commands/conf.py`

 * *Files identical despite different names*

### Comparing `idefix_cli-1.1.2/idefix_cli/_commands/read.py` & `idefix_cli-1.1.3/idefix_cli/_commands/read.py`

 * *Files identical despite different names*

### Comparing `idefix_cli-1.1.2/idefix_cli/_commands/run.py` & `idefix_cli-1.1.3/idefix_cli/_commands/run.py`

 * *Files 0% similar despite different names*

```diff
@@ -62,15 +62,14 @@
             return check_call(cmd)
     except CalledProcessError as exc:
         print_err("failed to compile idefix")
         return exc.returncode
 
 
 def add_arguments(parser) -> None:
-
     parser.add_argument("--dir", dest="directory", default=".", help="target directory")
     parser.add_argument(
         "-i",
         dest="inifile",
         action="store",
         type=str,
         default="idefix.ini",
```

### Comparing `idefix_cli-1.1.2/idefix_cli/_commands/stamp.py` & `idefix_cli-1.1.3/idefix_cli/_commands/stamp.py`

 * *Files identical despite different names*

### Comparing `idefix_cli-1.1.2/idefix_cli/_commands/write.py` & `idefix_cli-1.1.3/idefix_cli/_commands/write.py`

 * *Files identical despite different names*

### Comparing `idefix_cli-1.1.2/idefix_cli/_main.py` & `idefix_cli-1.1.3/idefix_cli/_main.py`

 * *Files identical despite different names*

### Comparing `idefix_cli-1.1.2/idefix_cli/lib.py` & `idefix_cli-1.1.3/idefix_cli/lib.py`

 * *Files identical despite different names*

### Comparing `idefix_cli-1.1.2/idefix_cli.egg-info/PKG-INFO` & `idefix_cli-1.1.3/idefix_cli.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: idefix-cli
-Version: 1.1.2
+Version: 1.1.3
 Summary: A CLI to automate mundane tasks with Idefix
 Author: C.M.T. Robert
 License: GPL-3.0
 Project-URL: Homepage, https://github.com/neutrinoceros/idefix_cli
 Classifier: License :: OSI Approved :: GNU General Public License v3 (GPLv3)
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3 :: Only
```

### Comparing `idefix_cli-1.1.2/idefix_cli.egg-info/SOURCES.txt` & `idefix_cli-1.1.3/idefix_cli.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `idefix_cli-1.1.2/pyproject.toml` & `idefix_cli-1.1.3/pyproject.toml`

 * *Files 6% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["setuptools>=61.2"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "idefix_cli"
-version = "1.1.2"
+version = "1.1.3"
 description = "A CLI to automate mundane tasks with Idefix"
 authors = [
     { name = "C.M.T. Robert" },
 ]
 classifiers = [
     "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
     "Programming Language :: Python :: 3",
@@ -60,15 +60,14 @@
 ]
 namespaces = false
 
 [tool.black]
 line-length = 88
 
 [tool.ruff]
-target-version = "py38"
 exclude = ["*__init__.py"]
 ignore = ["E501"]
 select = [
     "E",
     "F",
     "W",
     "B",
```

### Comparing `idefix_cli-1.1.2/tests/test_app_structure.py` & `idefix_cli-1.1.3/tests/test_app_structure.py`

 * *Files identical despite different names*

### Comparing `idefix_cli-1.1.2/tests/test_clean.py` & `idefix_cli-1.1.3/tests/test_clean.py`

 * *Files identical despite different names*

### Comparing `idefix_cli-1.1.2/tests/test_clone.py` & `idefix_cli-1.1.3/tests/test_clone.py`

 * *Files 5% similar despite different names*

```diff
@@ -69,18 +69,19 @@
     assert "README.md\n" in out
     assert "util.py\n" in out
     assert ret == 0
 
 
 def test_include_dir(tmp_path):
     # https://github.com/neutrinoceros/idefix_cli/issues/228
-    dest1 = str(tmp_path / "setup_with_mydir")
-    main(["clone", str(BASE_SETUP), dest1])
-    os.mkdir(os.path.join(dest1, "mydir"))
+    dest1 = tmp_path / "setup_with_mydir"
+    main(["clone", str(BASE_SETUP), str(dest1)])
+    os.mkdir(dest1 / "mydir")
+    (dest1 / "mydir" / "myfile").touch()
 
-    dest2 = str(tmp_path / "final")
-    ret = main(["clone", dest1, dest2, "--include", "mydir"])
+    dest2 = tmp_path / "final"
+    ret = main(["clone", str(dest1), str(dest2), "--include", "mydir"])
     assert ret == 0
 
-    dest3 = str(tmp_path / "final_shallow")
-    ret = main(["clone", dest1, dest3, "--include", "mydir", "--shallow"])
+    dest3 = tmp_path / "final_shallow"
+    ret = main(["clone", str(dest1), str(dest3), "--include", "mydir", "--shallow"])
     assert ret == 0
```

### Comparing `idefix_cli-1.1.2/tests/test_commons.py` & `idefix_cli-1.1.3/tests/test_commons.py`

 * *Files identical despite different names*

### Comparing `idefix_cli-1.1.2/tests/test_conf.py` & `idefix_cli-1.1.3/tests/test_conf.py`

 * *Files identical despite different names*

### Comparing `idefix_cli-1.1.2/tests/test_read.py` & `idefix_cli-1.1.3/tests/test_read.py`

 * *Files identical despite different names*

### Comparing `idefix_cli-1.1.2/tests/test_stamp.py` & `idefix_cli-1.1.3/tests/test_stamp.py`

 * *Files identical despite different names*

### Comparing `idefix_cli-1.1.2/tests/test_ux.py` & `idefix_cli-1.1.3/tests/test_ux.py`

 * *Files identical despite different names*

### Comparing `idefix_cli-1.1.2/tests/test_write.py` & `idefix_cli-1.1.3/tests/test_write.py`

 * *Files identical despite different names*

