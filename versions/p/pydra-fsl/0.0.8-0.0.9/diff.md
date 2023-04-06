# Comparing `tmp/pydra_fsl-0.0.8.tar.gz` & `tmp/pydra_fsl-0.0.9.tar.gz`

## Comparing `pydra_fsl-0.0.8.tar` & `pydra_fsl-0.0.9.tar`

### file list

```diff
@@ -1,29 +1,29 @@
--rw-r--r--   0        0        0      275 2020-02-02 00:00:00.000000 pydra_fsl-0.0.8/.editorconfig
--rw-r--r--   0        0        0      112 2020-02-02 00:00:00.000000 pydra_fsl-0.0.8/.github/dependabot.yaml
--rw-r--r--   0        0        0      559 2020-02-02 00:00:00.000000 pydra_fsl-0.0.8/.github/workflows/publish.yaml
--rw-r--r--   0        0        0     1187 2020-02-02 00:00:00.000000 pydra_fsl-0.0.8/.github/workflows/test.yaml
--rw-r--r--   0        0        0      479 2020-02-02 00:00:00.000000 pydra_fsl-0.0.8/pydra/tasks/fsl/__init__.py
--rw-r--r--   0        0        0    12486 2020-02-02 00:00:00.000000 pydra_fsl-0.0.8/pydra/tasks/fsl/eddy.py
--rw-r--r--   0        0        0     5716 2020-02-02 00:00:00.000000 pydra_fsl-0.0.8/pydra/tasks/fsl/fast.py
--rw-r--r--   0        0        0     2352 2020-02-02 00:00:00.000000 pydra_fsl-0.0.8/pydra/tasks/fsl/fnirt.py
--rw-r--r--   0        0        0     2319 2020-02-02 00:00:00.000000 pydra_fsl-0.0.8/pydra/tasks/fsl/fslmaths.py
--rw-r--r--   0        0        0     1714 2020-02-02 00:00:00.000000 pydra_fsl-0.0.8/pydra/tasks/fsl/fslmerge.py
--rw-r--r--   0        0        0     1483 2020-02-02 00:00:00.000000 pydra_fsl-0.0.8/pydra/tasks/fsl/fslreorient2std.py
--rw-r--r--   0        0        0     3065 2020-02-02 00:00:00.000000 pydra_fsl-0.0.8/pydra/tasks/fsl/fslroi.py
--rw-r--r--   0        0        0     2449 2020-02-02 00:00:00.000000 pydra_fsl-0.0.8/pydra/tasks/fsl/susan.py
--rw-r--r--   0        0        0       86 2020-02-02 00:00:00.000000 pydra_fsl-0.0.8/pydra/tasks/fsl/bet/__init__.py
--rw-r--r--   0        0        0     5785 2020-02-02 00:00:00.000000 pydra_fsl-0.0.8/pydra/tasks/fsl/bet/bet.py
--rw-r--r--   0        0        0     1545 2020-02-02 00:00:00.000000 pydra_fsl-0.0.8/pydra/tasks/fsl/bet/robustfov.py
--rw-r--r--   0        0        0      257 2020-02-02 00:00:00.000000 pydra_fsl-0.0.8/pydra/tasks/fsl/flirt/__init__.py
--rw-r--r--   0        0        0     2774 2020-02-02 00:00:00.000000 pydra_fsl-0.0.8/pydra/tasks/fsl/flirt/apply_xfm.py
--rw-r--r--   0        0        0      872 2020-02-02 00:00:00.000000 pydra_fsl-0.0.8/pydra/tasks/fsl/flirt/concat_xfm.py
--rw-r--r--   0        0        0     1805 2020-02-02 00:00:00.000000 pydra_fsl-0.0.8/pydra/tasks/fsl/flirt/convert_xfm.py
--rw-r--r--   0        0        0     3669 2020-02-02 00:00:00.000000 pydra_fsl-0.0.8/pydra/tasks/fsl/flirt/flirt.py
--rw-r--r--   0        0        0      768 2020-02-02 00:00:00.000000 pydra_fsl-0.0.8/pydra/tasks/fsl/flirt/invert_xfm.py
--rw-r--r--   0        0        0     2990 2020-02-02 00:00:00.000000 pydra_fsl-0.0.8/pydra/tasks/fsl/flirt/specs.py
--rw-r--r--   0        0        0     1959 2020-02-02 00:00:00.000000 pydra_fsl-0.0.8/.gitignore
--rw-r--r--   0        0        0    11357 2020-02-02 00:00:00.000000 pydra_fsl-0.0.8/LICENSE
--rw-r--r--   0        0        0     2063 2020-02-02 00:00:00.000000 pydra_fsl-0.0.8/README.md
--rw-r--r--   0        0        0      617 2020-02-02 00:00:00.000000 pydra_fsl-0.0.8/hatch.toml
--rw-r--r--   0        0        0     1428 2020-02-02 00:00:00.000000 pydra_fsl-0.0.8/pyproject.toml
--rw-r--r--   0        0        0     3199 2020-02-02 00:00:00.000000 pydra_fsl-0.0.8/PKG-INFO
+-rw-r--r--   0        0        0      275 2020-02-02 00:00:00.000000 pydra_fsl-0.0.9/.editorconfig
+-rw-r--r--   0        0        0      112 2020-02-02 00:00:00.000000 pydra_fsl-0.0.9/.github/dependabot.yaml
+-rw-r--r--   0        0        0      559 2020-02-02 00:00:00.000000 pydra_fsl-0.0.9/.github/workflows/publish.yaml
+-rw-r--r--   0        0        0     1187 2020-02-02 00:00:00.000000 pydra_fsl-0.0.9/.github/workflows/test.yaml
+-rw-r--r--   0        0        0      385 2020-02-02 00:00:00.000000 pydra_fsl-0.0.9/pydra/tasks/fsl/__init__.py
+-rw-r--r--   0        0        0    12486 2020-02-02 00:00:00.000000 pydra_fsl-0.0.9/pydra/tasks/fsl/eddy.py
+-rw-r--r--   0        0        0     5716 2020-02-02 00:00:00.000000 pydra_fsl-0.0.9/pydra/tasks/fsl/fast.py
+-rw-r--r--   0        0        0     2352 2020-02-02 00:00:00.000000 pydra_fsl-0.0.9/pydra/tasks/fsl/fnirt.py
+-rw-r--r--   0        0        0     2319 2020-02-02 00:00:00.000000 pydra_fsl-0.0.9/pydra/tasks/fsl/fslmaths.py
+-rw-r--r--   0        0        0     1714 2020-02-02 00:00:00.000000 pydra_fsl-0.0.9/pydra/tasks/fsl/fslmerge.py
+-rw-r--r--   0        0        0     1483 2020-02-02 00:00:00.000000 pydra_fsl-0.0.9/pydra/tasks/fsl/fslreorient2std.py
+-rw-r--r--   0        0        0     3065 2020-02-02 00:00:00.000000 pydra_fsl-0.0.9/pydra/tasks/fsl/fslroi.py
+-rw-r--r--   0        0        0     2449 2020-02-02 00:00:00.000000 pydra_fsl-0.0.9/pydra/tasks/fsl/susan.py
+-rw-r--r--   0        0        0       54 2020-02-02 00:00:00.000000 pydra_fsl-0.0.9/pydra/tasks/fsl/bet/__init__.py
+-rw-r--r--   0        0        0     5785 2020-02-02 00:00:00.000000 pydra_fsl-0.0.9/pydra/tasks/fsl/bet/bet.py
+-rw-r--r--   0        0        0     1545 2020-02-02 00:00:00.000000 pydra_fsl-0.0.9/pydra/tasks/fsl/bet/robustfov.py
+-rw-r--r--   0        0        0      161 2020-02-02 00:00:00.000000 pydra_fsl-0.0.9/pydra/tasks/fsl/flirt/__init__.py
+-rw-r--r--   0        0        0     2774 2020-02-02 00:00:00.000000 pydra_fsl-0.0.9/pydra/tasks/fsl/flirt/apply_xfm.py
+-rw-r--r--   0        0        0      872 2020-02-02 00:00:00.000000 pydra_fsl-0.0.9/pydra/tasks/fsl/flirt/concat_xfm.py
+-rw-r--r--   0        0        0     1805 2020-02-02 00:00:00.000000 pydra_fsl-0.0.9/pydra/tasks/fsl/flirt/convert_xfm.py
+-rw-r--r--   0        0        0     3669 2020-02-02 00:00:00.000000 pydra_fsl-0.0.9/pydra/tasks/fsl/flirt/flirt.py
+-rw-r--r--   0        0        0      768 2020-02-02 00:00:00.000000 pydra_fsl-0.0.9/pydra/tasks/fsl/flirt/invert_xfm.py
+-rw-r--r--   0        0        0     2990 2020-02-02 00:00:00.000000 pydra_fsl-0.0.9/pydra/tasks/fsl/flirt/specs.py
+-rw-r--r--   0        0        0     1959 2020-02-02 00:00:00.000000 pydra_fsl-0.0.9/.gitignore
+-rw-r--r--   0        0        0    11357 2020-02-02 00:00:00.000000 pydra_fsl-0.0.9/LICENSE
+-rw-r--r--   0        0        0     2063 2020-02-02 00:00:00.000000 pydra_fsl-0.0.9/README.md
+-rw-r--r--   0        0        0      617 2020-02-02 00:00:00.000000 pydra_fsl-0.0.9/hatch.toml
+-rw-r--r--   0        0        0     1428 2020-02-02 00:00:00.000000 pydra_fsl-0.0.9/pyproject.toml
+-rw-r--r--   0        0        0     3199 2020-02-02 00:00:00.000000 pydra_fsl-0.0.9/PKG-INFO
```

### Comparing `pydra_fsl-0.0.8/.github/workflows/publish.yaml` & `pydra_fsl-0.0.9/.github/workflows/publish.yaml`

 * *Files identical despite different names*

### Comparing `pydra_fsl-0.0.8/.github/workflows/test.yaml` & `pydra_fsl-0.0.9/.github/workflows/test.yaml`

 * *Files identical despite different names*

### Comparing `pydra_fsl-0.0.8/pydra/tasks/fsl/eddy.py` & `pydra_fsl-0.0.9/pydra/tasks/fsl/eddy.py`

 * *Files identical despite different names*

### Comparing `pydra_fsl-0.0.8/pydra/tasks/fsl/fast.py` & `pydra_fsl-0.0.9/pydra/tasks/fsl/fast.py`

 * *Files identical despite different names*

### Comparing `pydra_fsl-0.0.8/pydra/tasks/fsl/fnirt.py` & `pydra_fsl-0.0.9/pydra/tasks/fsl/fnirt.py`

 * *Files identical despite different names*

### Comparing `pydra_fsl-0.0.8/pydra/tasks/fsl/fslmaths.py` & `pydra_fsl-0.0.9/pydra/tasks/fsl/fslmaths.py`

 * *Files identical despite different names*

### Comparing `pydra_fsl-0.0.8/pydra/tasks/fsl/fslmerge.py` & `pydra_fsl-0.0.9/pydra/tasks/fsl/fslmerge.py`

 * *Files identical despite different names*

### Comparing `pydra_fsl-0.0.8/pydra/tasks/fsl/fslreorient2std.py` & `pydra_fsl-0.0.9/pydra/tasks/fsl/fslreorient2std.py`

 * *Files identical despite different names*

### Comparing `pydra_fsl-0.0.8/pydra/tasks/fsl/fslroi.py` & `pydra_fsl-0.0.9/pydra/tasks/fsl/fslroi.py`

 * *Files identical despite different names*

### Comparing `pydra_fsl-0.0.8/pydra/tasks/fsl/susan.py` & `pydra_fsl-0.0.9/pydra/tasks/fsl/susan.py`

 * *Files identical despite different names*

### Comparing `pydra_fsl-0.0.8/pydra/tasks/fsl/bet/bet.py` & `pydra_fsl-0.0.9/pydra/tasks/fsl/bet/bet.py`

 * *Files identical despite different names*

### Comparing `pydra_fsl-0.0.8/pydra/tasks/fsl/bet/robustfov.py` & `pydra_fsl-0.0.9/pydra/tasks/fsl/bet/robustfov.py`

 * *Files identical despite different names*

### Comparing `pydra_fsl-0.0.8/pydra/tasks/fsl/flirt/apply_xfm.py` & `pydra_fsl-0.0.9/pydra/tasks/fsl/flirt/apply_xfm.py`

 * *Files identical despite different names*

### Comparing `pydra_fsl-0.0.8/pydra/tasks/fsl/flirt/concat_xfm.py` & `pydra_fsl-0.0.9/pydra/tasks/fsl/flirt/concat_xfm.py`

 * *Files identical despite different names*

### Comparing `pydra_fsl-0.0.8/pydra/tasks/fsl/flirt/convert_xfm.py` & `pydra_fsl-0.0.9/pydra/tasks/fsl/flirt/convert_xfm.py`

 * *Files identical despite different names*

### Comparing `pydra_fsl-0.0.8/pydra/tasks/fsl/flirt/flirt.py` & `pydra_fsl-0.0.9/pydra/tasks/fsl/flirt/flirt.py`

 * *Files identical despite different names*

### Comparing `pydra_fsl-0.0.8/pydra/tasks/fsl/flirt/invert_xfm.py` & `pydra_fsl-0.0.9/pydra/tasks/fsl/flirt/invert_xfm.py`

 * *Files identical despite different names*

### Comparing `pydra_fsl-0.0.8/pydra/tasks/fsl/flirt/specs.py` & `pydra_fsl-0.0.9/pydra/tasks/fsl/flirt/specs.py`

 * *Files identical despite different names*

### Comparing `pydra_fsl-0.0.8/.gitignore` & `pydra_fsl-0.0.9/.gitignore`

 * *Files identical despite different names*

### Comparing `pydra_fsl-0.0.8/LICENSE` & `pydra_fsl-0.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `pydra_fsl-0.0.8/README.md` & `pydra_fsl-0.0.9/README.md`

 * *Files identical despite different names*

### Comparing `pydra_fsl-0.0.8/hatch.toml` & `pydra_fsl-0.0.9/hatch.toml`

 * *Files identical despite different names*

### Comparing `pydra_fsl-0.0.8/pyproject.toml` & `pydra_fsl-0.0.9/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["hatchling"]
 build-backend = "hatchling.build"
 
 [project]
 name = "pydra-fsl"
-version = "0.0.8"
+version = "0.0.9"
 description = "Pydra tasks for FSL"
 readme = "README.md"
 requires-python = ">=3.7"
 license = "Apache-2.0"
 keywords = ["pydra", "neuroimaging", "fsl"]
 authors = [
   { name = "Ghislain Vaillant", email = "ghislain.vaillant@icm-institute.org" },
```

### Comparing `pydra_fsl-0.0.8/PKG-INFO` & `pydra_fsl-0.0.9/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pydra-fsl
-Version: 0.0.8
+Version: 0.0.9
 Summary: Pydra tasks for FSL
 Project-URL: Documentation, https://github.com/aramis-lab/pydra-fsl#readme
 Project-URL: Issues, https://github.com/aramis-lab/pydra-fsl/issues
 Project-URL: Source, https://github.com/aramis-lab/pydra-fsl
 Author-email: Ghislain Vaillant <ghislain.vaillant@icm-institute.org>
 License-Expression: Apache-2.0
 License-File: LICENSE
```

