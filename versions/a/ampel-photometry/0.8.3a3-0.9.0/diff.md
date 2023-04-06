# Comparing `tmp/ampel_photometry-0.8.3a3.tar.gz` & `tmp/ampel_photometry-0.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "ampel_photometry-0.8.3a3.tar", max compression
+gzip compressed data, was "ampel_photometry-0.9.0.tar", max compression
```

## Comparing `ampel_photometry-0.8.3a3.tar` & `ampel_photometry-0.9.0.tar`

### file list

```diff
@@ -1,22 +1,21 @@
--rwxr-xr-x   0        0        0      886 2023-01-18 15:44:21.841596 ampel_photometry-0.8.3a3/ampel/abstract/AbsLightCurveT2Unit.py
--rwxr-xr-x   0        0        0      706 2023-01-18 15:44:21.841596 ampel_photometry-0.8.3a3/ampel/abstract/AbsPhotoT3Unit.py
--rw-r--r--   0        0        0     1265 2023-01-18 15:44:21.841596 ampel_photometry-0.8.3a3/ampel/abstract/AbsT2Tabulator.py
--rw-r--r--   0        0        0     3361 2023-01-18 15:44:21.841596 ampel_photometry-0.8.3a3/ampel/abstract/AbsTabulatedT2Unit.py
--rwxr-xr-x   0        0        0     2292 2023-01-18 15:44:21.841596 ampel_photometry-0.8.3a3/ampel/abstract/AbsTiedLightCurveT2Unit.py
--rw-r--r--   0        0        0      613 2023-01-18 15:44:21.841596 ampel_photometry-0.8.3a3/ampel/aux/PPSFilter.py
--rw-r--r--   0        0        0      613 2023-01-18 15:44:21.841596 ampel_photometry-0.8.3a3/ampel/aux/ULSFilter.py
--rw-r--r--   0        0        0      919 2023-01-18 15:44:21.841596 ampel_photometry-0.8.3a3/ampel/demo/DemoEvery3PhotoPointT2Unit.py
--rw-r--r--   0        0        0      919 2023-01-18 15:44:21.845595 ampel_photometry-0.8.3a3/ampel/demo/DemoEvery4PhotoPointT2Unit.py
--rw-r--r--   0        0        0      907 2023-01-18 15:44:21.845595 ampel_photometry-0.8.3a3/ampel/demo/DemoFirstPhotoPointT2Unit.py
--rw-r--r--   0        0        0      907 2023-01-18 15:44:21.845595 ampel_photometry-0.8.3a3/ampel/demo/DemoFirstUpperLimitT2Unit.py
--rw-r--r--   0        0        0      857 2023-01-18 15:44:21.845595 ampel_photometry-0.8.3a3/ampel/demo/DemoLightCurveT2Unit.py
--rw-r--r--   0        0        0      871 2023-01-18 15:44:21.845595 ampel_photometry-0.8.3a3/ampel/demo/DemoPhotoPointT2Unit.py
--rw-r--r--   0        0        0     1080 2023-01-18 15:44:21.845595 ampel_photometry-0.8.3a3/ampel/demo/DemoTiedLightCurveT2Unit.py
--rw-r--r--   0        0        0        0 2023-01-18 15:44:21.845595 ampel_photometry-0.8.3a3/ampel/py.typed
--rwxr-xr-x   0        0        0     1184 2023-01-18 15:44:21.845595 ampel_photometry-0.8.3a3/ampel/t1/T1PhotoRetroCombiner.py
--rwxr-xr-x   0        0        0     6959 2023-01-18 15:44:21.845595 ampel_photometry-0.8.3a3/ampel/view/LightCurve.py
--rwxr-xr-x   0        0        0     2154 2023-01-18 15:44:21.845595 ampel_photometry-0.8.3a3/ampel/view/TransientView.py
--rw-r--r--   0        0        0      543 2023-01-18 15:44:21.845595 ampel_photometry-0.8.3a3/conf/ampel-photometry/ampel.yaml
--rw-r--r--   0        0        0     1254 2023-01-18 15:44:21.845595 ampel_photometry-0.8.3a3/pyproject.toml
--rw-r--r--   0        0        0      956 1970-01-01 00:00:00.000000 ampel_photometry-0.8.3a3/setup.py
--rw-r--r--   0        0        0      739 1970-01-01 00:00:00.000000 ampel_photometry-0.8.3a3/PKG-INFO
+-rwxr-xr-x   0        0        0      886 2023-04-06 20:02:42.167689 ampel_photometry-0.9.0/ampel/abstract/AbsLightCurveT2Unit.py
+-rwxr-xr-x   0        0        0      688 2023-04-06 20:02:42.167689 ampel_photometry-0.9.0/ampel/abstract/AbsPhotoT3Unit.py
+-rw-r--r--   0        0        0     1265 2023-04-06 20:02:42.167689 ampel_photometry-0.9.0/ampel/abstract/AbsT2Tabulator.py
+-rw-r--r--   0        0        0     3361 2023-04-06 20:02:42.167689 ampel_photometry-0.9.0/ampel/abstract/AbsTabulatedT2Unit.py
+-rwxr-xr-x   0        0        0     2292 2023-04-06 20:02:42.167689 ampel_photometry-0.9.0/ampel/abstract/AbsTiedLightCurveT2Unit.py
+-rw-r--r--   0        0        0      613 2023-04-06 20:02:42.167689 ampel_photometry-0.9.0/ampel/aux/PPSFilter.py
+-rw-r--r--   0        0        0      613 2023-04-06 20:02:42.167689 ampel_photometry-0.9.0/ampel/aux/ULSFilter.py
+-rw-r--r--   0        0        0      919 2023-04-06 20:02:42.167689 ampel_photometry-0.9.0/ampel/demo/DemoEvery3PhotoPointT2Unit.py
+-rw-r--r--   0        0        0      919 2023-04-06 20:02:42.167689 ampel_photometry-0.9.0/ampel/demo/DemoEvery4PhotoPointT2Unit.py
+-rw-r--r--   0        0        0      907 2023-04-06 20:02:42.167689 ampel_photometry-0.9.0/ampel/demo/DemoFirstPhotoPointT2Unit.py
+-rw-r--r--   0        0        0      907 2023-04-06 20:02:42.167689 ampel_photometry-0.9.0/ampel/demo/DemoFirstUpperLimitT2Unit.py
+-rw-r--r--   0        0        0      857 2023-04-06 20:02:42.167689 ampel_photometry-0.9.0/ampel/demo/DemoLightCurveT2Unit.py
+-rw-r--r--   0        0        0      871 2023-04-06 20:02:42.167689 ampel_photometry-0.9.0/ampel/demo/DemoPhotoPointT2Unit.py
+-rw-r--r--   0        0        0     1080 2023-04-06 20:02:42.167689 ampel_photometry-0.9.0/ampel/demo/DemoTiedLightCurveT2Unit.py
+-rw-r--r--   0        0        0        0 2023-04-06 20:02:42.167689 ampel_photometry-0.9.0/ampel/py.typed
+-rwxr-xr-x   0        0        0     1184 2023-04-06 20:02:42.167689 ampel_photometry-0.9.0/ampel/t1/T1PhotoRetroCombiner.py
+-rwxr-xr-x   0        0        0     6959 2023-04-06 20:02:42.167689 ampel_photometry-0.9.0/ampel/view/LightCurve.py
+-rwxr-xr-x   0        0        0     2154 2023-04-06 20:02:42.167689 ampel_photometry-0.9.0/ampel/view/TransientView.py
+-rw-r--r--   0        0        0      543 2023-04-06 20:02:42.167689 ampel_photometry-0.9.0/conf/ampel-photometry/ampel.yaml
+-rw-r--r--   0        0        0     1236 2023-04-06 20:02:42.171687 ampel_photometry-0.9.0/pyproject.toml
+-rw-r--r--   0        0        0      723 1970-01-01 00:00:00.000000 ampel_photometry-0.9.0/PKG-INFO
```

### Comparing `ampel_photometry-0.8.3a3/ampel/abstract/AbsLightCurveT2Unit.py` & `ampel_photometry-0.9.0/ampel/abstract/AbsLightCurveT2Unit.py`

 * *Files identical despite different names*

### Comparing `ampel_photometry-0.8.3a3/ampel/abstract/AbsPhotoT3Unit.py` & `ampel_photometry-0.9.0/ampel/abstract/AbsPhotoT3Unit.py`

 * *Files 5% similar despite different names*

```diff
@@ -3,18 +3,18 @@
 # File:                Ampel-photometry/ampel/abstract/AbsPhotoT3Unit.py
 # License:             BSD-3-Clause
 # Author:              valery brinnel <firstname.lastname@gmail.com>
 # Date:                01.06.2020
 # Last Modified Date:  19.04.2021
 # Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
-from ampel.abstract.AbsT3ReviewUnit import AbsT3ReviewUnit
+from ampel.abstract.AbsT3Unit import AbsT3Unit
 from ampel.view.TransientView import TransientView
 
 
-class AbsPhotoT3Unit(AbsT3ReviewUnit[TransientView], abstract=True):
+class AbsPhotoT3Unit(AbsT3Unit[TransientView], abstract=True):
 	"""
 	Parametrized abstract class for T3 units receiving TransientView instances
 	(and potentially LightCurve instances as well)
 	"""
 	_View = TransientView
 	pass
```

### Comparing `ampel_photometry-0.8.3a3/ampel/abstract/AbsT2Tabulator.py` & `ampel_photometry-0.9.0/ampel/abstract/AbsT2Tabulator.py`

 * *Files identical despite different names*

### Comparing `ampel_photometry-0.8.3a3/ampel/abstract/AbsTabulatedT2Unit.py` & `ampel_photometry-0.9.0/ampel/abstract/AbsTabulatedT2Unit.py`

 * *Files identical despite different names*

### Comparing `ampel_photometry-0.8.3a3/ampel/abstract/AbsTiedLightCurveT2Unit.py` & `ampel_photometry-0.9.0/ampel/abstract/AbsTiedLightCurveT2Unit.py`

 * *Files identical despite different names*

### Comparing `ampel_photometry-0.8.3a3/ampel/aux/PPSFilter.py` & `ampel_photometry-0.9.0/ampel/aux/PPSFilter.py`

 * *Files identical despite different names*

### Comparing `ampel_photometry-0.8.3a3/ampel/aux/ULSFilter.py` & `ampel_photometry-0.9.0/ampel/aux/ULSFilter.py`

 * *Files identical despite different names*

### Comparing `ampel_photometry-0.8.3a3/ampel/demo/DemoEvery3PhotoPointT2Unit.py` & `ampel_photometry-0.9.0/ampel/demo/DemoEvery3PhotoPointT2Unit.py`

 * *Files identical despite different names*

### Comparing `ampel_photometry-0.8.3a3/ampel/demo/DemoEvery4PhotoPointT2Unit.py` & `ampel_photometry-0.9.0/ampel/demo/DemoEvery4PhotoPointT2Unit.py`

 * *Files identical despite different names*

### Comparing `ampel_photometry-0.8.3a3/ampel/demo/DemoFirstPhotoPointT2Unit.py` & `ampel_photometry-0.9.0/ampel/demo/DemoFirstPhotoPointT2Unit.py`

 * *Files identical despite different names*

### Comparing `ampel_photometry-0.8.3a3/ampel/demo/DemoFirstUpperLimitT2Unit.py` & `ampel_photometry-0.9.0/ampel/demo/DemoFirstUpperLimitT2Unit.py`

 * *Files identical despite different names*

### Comparing `ampel_photometry-0.8.3a3/ampel/demo/DemoLightCurveT2Unit.py` & `ampel_photometry-0.9.0/ampel/demo/DemoLightCurveT2Unit.py`

 * *Files identical despite different names*

### Comparing `ampel_photometry-0.8.3a3/ampel/demo/DemoPhotoPointT2Unit.py` & `ampel_photometry-0.9.0/ampel/demo/DemoPhotoPointT2Unit.py`

 * *Files identical despite different names*

### Comparing `ampel_photometry-0.8.3a3/ampel/demo/DemoTiedLightCurveT2Unit.py` & `ampel_photometry-0.9.0/ampel/demo/DemoTiedLightCurveT2Unit.py`

 * *Files identical despite different names*

### Comparing `ampel_photometry-0.8.3a3/ampel/t1/T1PhotoRetroCombiner.py` & `ampel_photometry-0.9.0/ampel/t1/T1PhotoRetroCombiner.py`

 * *Files identical despite different names*

### Comparing `ampel_photometry-0.8.3a3/ampel/view/LightCurve.py` & `ampel_photometry-0.9.0/ampel/view/LightCurve.py`

 * *Files identical despite different names*

### Comparing `ampel_photometry-0.8.3a3/ampel/view/TransientView.py` & `ampel_photometry-0.9.0/ampel/view/TransientView.py`

 * *Files identical despite different names*

### Comparing `ampel_photometry-0.8.3a3/conf/ampel-photometry/ampel.yaml` & `ampel_photometry-0.9.0/conf/ampel-photometry/ampel.yaml`

 * *Files identical despite different names*

### Comparing `ampel_photometry-0.8.3a3/pyproject.toml` & `ampel_photometry-0.9.0/pyproject.toml`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "ampel-photometry"
-version = "0.8.3a3"
+version = "0.9.0"
 description = "Photometry add-on for the Ampel system"
 authors = ["Valery Brinnel"]
 license = "BSD-3-Clause"
 packages = [
     {include = "ampel"}
 ]
 include = [
@@ -21,21 +21,21 @@
 url = "https://test.pypi.org/simple"
 
 [tool.poetry.dependencies]
 python = ">=3.10,<3.12"
 Sphinx = {version = ">=6.1.3,<6.2.0", optional = true}
 sphinx-autodoc-typehints = {version = "^1.11.1", optional = true}
 tomlkit = {version = "^0.11.0"}
-ampel-interface = {version = "^0.8.3-beta.14"}
-ampel-core = {version = "^0.8.3-beta.21"}
+ampel-interface = {version = "^0.9.0"}
+ampel-core = {version = "^0.9.0"}
 astropy = "^5"
 
 [tool.poetry.dev-dependencies]
-pytest = "^7.2.1"
-mypy = "^0.991"
+pytest = "^7.2.2"
+mypy = "^1.1.1"
 pytest-cov = "^4.0.0"
 
 [tool.poetry.extras]
 docs = ["Sphinx", "sphinx-press-theme", "sphinx-autodoc-typehints", "tomlkit"]
 
 [build-system]
 requires = ["poetry-core>=1.0.0"]
```

### Comparing `ampel_photometry-0.8.3a3/PKG-INFO` & `ampel_photometry-0.9.0/PKG-INFO`

 * *Files 19% similar despite different names*

```diff
@@ -1,18 +1,18 @@
 Metadata-Version: 2.1
 Name: ampel-photometry
-Version: 0.8.3a3
+Version: 0.9.0
 Summary: Photometry add-on for the Ampel system
 License: BSD-3-Clause
 Author: Valery Brinnel
 Requires-Python: >=3.10,<3.12
 Classifier: License :: OSI Approved :: BSD License
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
 Provides-Extra: docs
 Requires-Dist: Sphinx (>=6.1.3,<6.2.0) ; extra == "docs"
-Requires-Dist: ampel-core (>=0.8.3-beta.21,<0.9.0)
-Requires-Dist: ampel-interface (>=0.8.3-beta.14,<0.9.0)
+Requires-Dist: ampel-core (>=0.9.0,<0.10.0)
+Requires-Dist: ampel-interface (>=0.9.0,<0.10.0)
 Requires-Dist: astropy (>=5,<6)
 Requires-Dist: sphinx-autodoc-typehints (>=1.11.1,<2.0.0) ; extra == "docs"
 Requires-Dist: tomlkit (>=0.11.0,<0.12.0) ; extra == "docs"
```

