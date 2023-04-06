# Comparing `tmp/genpypress-0.1.8.tar.gz` & `tmp/genpypress-0.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "genpypress-0.1.8.tar", max compression
+gzip compressed data, was "genpypress-0.1.9.tar", max compression
```

## Comparing `genpypress-0.1.8.tar` & `genpypress-0.1.9.tar`

### file list

```diff
@@ -1,12 +1,12 @@
--rw-r--r--   0        0        0     1067 2023-02-20 08:13:52.452246 genpypress-0.1.8/LICENSE
--rw-r--r--   0        0        0     1210 2023-04-06 07:39:55.096980 genpypress-0.1.8/pyproject.toml
--rw-r--r--   0        0        0     1504 2023-04-06 07:14:37.595274 genpypress-0.1.8/readme.md
--rw-r--r--   0        0        0        0 2023-02-19 13:16:43.000000 genpypress-0.1.8/src/genpypress/__init__.py
--rw-r--r--   0        0        0     6170 2023-04-06 07:10:31.494415 genpypress-0.1.8/src/genpypress/app_cc/__init__.py
--rw-r--r--   0        0        0     8807 2023-04-06 07:36:45.999898 genpypress-0.1.8/src/genpypress/app_patch_to_validtime/__init__.py
--rw-r--r--   0        0        0     8779 2023-04-06 07:11:55.970553 genpypress-0.1.8/src/genpypress/mapping/__init__.py
--rw-r--r--   0        0        0     1283 2023-04-06 07:10:31.441008 genpypress-0.1.8/src/genpypress/ph.py
--rw-r--r--   0        0        0     2152 2023-04-06 07:10:31.463144 genpypress-0.1.8/src/genpypress/session/__init__.py
--rw-r--r--   0        0        0     6704 2023-04-06 07:10:31.541291 genpypress-0.1.8/src/genpypress/table/__init__.py
--rwxr-xr-x   0        0        0  7513088 2023-02-26 10:51:51.257033 genpypress-0.1.8/src/genpypress/table/_bin/table2json.exe
--rw-r--r--   0        0        0     2297 1970-01-01 00:00:00.000000 genpypress-0.1.8/PKG-INFO
+-rw-r--r--   0        0        0     1067 2023-02-20 08:13:52.452246 genpypress-0.1.9/LICENSE
+-rw-r--r--   0        0        0     1228 2023-04-06 08:36:31.061857 genpypress-0.1.9/pyproject.toml
+-rw-r--r--   0        0        0     1504 2023-04-06 07:14:37.595274 genpypress-0.1.9/readme.md
+-rw-r--r--   0        0        0        0 2023-02-19 13:16:43.000000 genpypress-0.1.9/src/genpypress/__init__.py
+-rw-r--r--   0        0        0     6170 2023-04-06 07:10:31.494415 genpypress-0.1.9/src/genpypress/app_cc/__init__.py
+-rw-r--r--   0        0        0     9424 2023-04-06 08:45:27.555680 genpypress-0.1.9/src/genpypress/app_patch_to_validtime/__init__.py
+-rw-r--r--   0        0        0     8779 2023-04-06 07:11:55.970553 genpypress-0.1.9/src/genpypress/mapping/__init__.py
+-rw-r--r--   0        0        0     1381 2023-04-06 08:41:10.092591 genpypress-0.1.9/src/genpypress/ph.py
+-rw-r--r--   0        0        0     2152 2023-04-06 07:10:31.463144 genpypress-0.1.9/src/genpypress/session/__init__.py
+-rw-r--r--   0        0        0     6704 2023-04-06 07:10:31.541291 genpypress-0.1.9/src/genpypress/table/__init__.py
+-rwxr-xr-x   0        0        0  7513088 2023-02-26 10:51:51.257033 genpypress-0.1.9/src/genpypress/table/_bin/table2json.exe
+-rw-r--r--   0        0        0     2336 1970-01-01 00:00:00.000000 genpypress-0.1.9/PKG-INFO
```

### Comparing `genpypress-0.1.8/LICENSE` & `genpypress-0.1.9/LICENSE`

 * *Files identical despite different names*

### Comparing `genpypress-0.1.8/pyproject.toml` & `genpypress-0.1.9/pyproject.toml`

 * *Files 10% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "genpypress"
-version = "0.1.8"
+version = "0.1.9"
 description = "Set of tools and utilities connected with press code generator."
 authors = ["Jan Herout <jan.herout@gmail.com>"]
 license = "MIT"
 
 # -----------------------------------
 # readme
 # -----------------------------------
@@ -31,14 +31,15 @@
 
 [tool.poetry.dependencies]
 python = "^3.10, <3.12"
 attrs = "^22.2.0"
 cattrs = "^22.2.0"
 teradatasql = "^17.20.0.19"
 fire = "^0.5.0"
+rich = "^13.3.3"
 
 [tool.poetry.group.dev.dependencies]
 black = "^23.1.0"
 isort = "^5.12.0"
 flake8 = "^6.0.0"
 pytest = "^7.2.1"
```

### Comparing `genpypress-0.1.8/readme.md` & `genpypress-0.1.9/readme.md`

 * *Files identical despite different names*

### Comparing `genpypress-0.1.8/src/genpypress/app_cc/__init__.py` & `genpypress-0.1.9/src/genpypress/app_cc/__init__.py`

 * *Files identical despite different names*

### Comparing `genpypress-0.1.8/src/genpypress/app_patch_to_validtime/__init__.py` & `genpypress-0.1.9/src/genpypress/app_patch_to_validtime/__init__.py`

 * *Files 4% similar despite different names*

```diff
@@ -14,17 +14,20 @@
 
 
 def async_patch(directory: Path, limit: int = 50, encoding: str = "utf-8"):
     """provede patch TPT skriptů v kontextu použití asynchronní stage"""
     # sestav seznam souborů
     files = list(directory.rglob("*.tpt"))
     if len(files) == 0:
-        raise PatchError(f"Nula souborů na vstupu: {directory=}")
+        raise PatchError(f"Nula souborů na vstupu: directory={str(directory)}")
     if len(files) > limit:
-        raise PatchError(f"Více souborů než jsme čekali. {directory=}, {limit=}, {len(files)=}")
+        raise PatchError(
+            f"Více souborů než jsme čekali.\n- {limit=}\n- {len(files)=}\n- directory={str(directory)}"
+            + "\n\nPoužij parametr --limit, pokud chceš limit zvednout."
+        )
 
     # projdi soubor za souborem, seber si informaci o tom kde jsme měli úspěch a kde problém
     problems = []
     for f in files:
         relpath = f.relative_to(directory)
         try:
             script = f.read_text(encoding=encoding, errors="strict")
@@ -71,20 +74,29 @@
     # pokud již ve skriptu JE set session validtime, končíme a nic neděláme
     if io_set_session > -1:
         return text
 
     # jinak musíme provést patch
     out_lines = lines.copy()
 
+    # pokud je na řádku s APPLY apostrof, musíme ho "zasmrtit", ale současně ho musíme dodat za SET SESSION VALIDTIME
+    i_apply_apostrof = ""
+    if "'" in out_lines[i_apply]:
+        if out_lines[i_apply].count("'") > 1:
+            raise PatchError(f"na řádce s APPLY je víc apostrofů než jeden: {out_lines[i_apply]}")
+        i_apply_apostrof = "\n          '\n"
+        out_lines[i_apply] = out_lines[i_apply].replace("'", "")
+
     # řádek, kde je APPLY, obohatíme o SET SESSION VALIDTIME
     # to musíme udělat vždy - set session ve skriptu není (jinak bychom ho vrátili bez úprav)
     out_lines[i_apply] = (
         out_lines[i_apply]
-        + "\n          SET SESSION VALIDTIME AS OF TIMESTAMP ''%LOAD_DT% 23:59:59'';'"
+        + "\n          'SET SESSION VALIDTIME AS OF TIMESTAMP ''%LOAD_DT% 23:59:59'';'"
         + "\n          ,"
+        + i_apply_apostrof
     )
 
     # řádek, kde je insert, musíme zabalit do SELECT * FROM (
     # poslední statement musíme zakončit na ) as T
     # ale jen opkud prní select není SELECT * FROM
     if not tpt_is_first_select_star(lines):
         out_lines[i_insert] = out_lines[i_insert] + "\n          SELECT * FROM ("
```

### Comparing `genpypress-0.1.8/src/genpypress/mapping/__init__.py` & `genpypress-0.1.9/src/genpypress/mapping/__init__.py`

 * *Files identical despite different names*

### Comparing `genpypress-0.1.8/src/genpypress/ph.py` & `genpypress-0.1.9/src/genpypress/ph.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,23 +1,28 @@
 from pathlib import Path as _Path
 import fire as _fire
+from rich import traceback
 from genpypress import app_cc as _app_cc
 from genpypress import app_patch_to_validtime as _app_patch_to_validtime
 
+traceback.install(show_locals=False, max_frames=1)
+
 
 def apatch(directory: str, limit: int = 50, encoding: str = "utf-8"):
     """apatch: patch TPT skriptů pro async stage
 
     Args:
         directory (str): adresář, kde jsou TPT skripty
         limit (int): kolik maximálně souborů upravit
         encoding (str): jak jsou soubory nakódované
     """
     d = _Path(directory)
-    assert d.is_dir(), f"toto není adresdář: {directory}"
+    if not d.is_dir():
+        print(f"toto není adresář: {directory}")
+        exit(1)
     _app_patch_to_validtime.async_patch(d, limit, encoding)
 
 
 def cc(
     directory: str,
     scenario: str = "drop",
     input_encoding: str = "utf-8",
@@ -28,17 +33,15 @@
 
     Args:
         directory (str): directory where to do the work
         scenario (str): ["drop", "create", "cleanup", "drop-only"]
         input_encoding (str): Defaults to "utf-8".
         output_encoding (str): Defaults to "utf-8".
     """
-    _app_cc.conditional_create(
-        directory, scenario, input_encoding, output_encoding, max_files
-    )
+    _app_cc.conditional_create(directory, scenario, input_encoding, output_encoding, max_files)
 
 
 def _main():
     _fire.Fire()
 
 
 if __name__ == "__main__":
```

### Comparing `genpypress-0.1.8/src/genpypress/session/__init__.py` & `genpypress-0.1.9/src/genpypress/session/__init__.py`

 * *Files identical despite different names*

### Comparing `genpypress-0.1.8/src/genpypress/table/__init__.py` & `genpypress-0.1.9/src/genpypress/table/__init__.py`

 * *Files identical despite different names*

### Comparing `genpypress-0.1.8/src/genpypress/table/_bin/table2json.exe` & `genpypress-0.1.9/src/genpypress/table/_bin/table2json.exe`

 * *Files identical despite different names*

### Comparing `genpypress-0.1.8/PKG-INFO` & `genpypress-0.1.9/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: genpypress
-Version: 0.1.8
+Version: 0.1.9
 Summary: Set of tools and utilities connected with press code generator.
 License: MIT
 Author: Jan Herout
 Author-email: jan.herout@gmail.com
 Requires-Python: >=3.10,<3.12
 Classifier: Development Status :: 1 - Planning
 Classifier: Environment :: Console
@@ -14,14 +14,15 @@
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
 Classifier: Topic :: Database
 Requires-Dist: attrs (>=22.2.0,<23.0.0)
 Requires-Dist: cattrs (>=22.2.0,<23.0.0)
 Requires-Dist: fire (>=0.5.0,<0.6.0)
+Requires-Dist: rich (>=13.3.3,<14.0.0)
 Requires-Dist: teradatasql (>=17.20.0.19,<18.0.0.0)
 Description-Content-Type: text/markdown
 
 # genpypress
 
 This library contains several code generator helpers. It is connected to the `press` code generator.
```

