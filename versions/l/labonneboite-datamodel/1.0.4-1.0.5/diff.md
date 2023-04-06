# Comparing `tmp/labonneboite_datamodel-1.0.4.tar.gz` & `tmp/labonneboite_datamodel-1.0.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "labonneboite_datamodel-1.0.4.tar", max compression
+gzip compressed data, was "labonneboite_datamodel-1.0.5.tar", max compression
```

## Comparing `labonneboite_datamodel-1.0.4.tar` & `labonneboite_datamodel-1.0.5.tar`

### file list

```diff
@@ -1,10 +1,10 @@
--rw-r--r--   0        0        0      224 2023-04-04 13:45:03.269004 labonneboite_datamodel-1.0.4/labonneboite_datamodel/__init__.py
--rw-r--r--   0        0        0      697 2023-04-05 09:46:10.763862 labonneboite_datamodel-1.0.4/labonneboite_datamodel/crud.py
--rw-r--r--   0        0        0     2185 2023-04-05 09:46:10.763862 labonneboite_datamodel-1.0.4/labonneboite_datamodel/job.py
--rw-r--r--   0        0        0     7590 2023-04-06 10:24:17.812541 labonneboite_datamodel-1.0.4/labonneboite_datamodel/office.py
--rw-r--r--   0        0        0        0 2023-04-04 13:25:50.527619 labonneboite_datamodel-1.0.4/labonneboite_datamodel/tests/__init__.py
--rw-r--r--   0        0        0     3589 2023-04-06 09:31:09.039521 labonneboite_datamodel-1.0.4/labonneboite_datamodel/tests/data/test.csv
--rw-r--r--   0        0        0     1026 2023-04-04 13:25:50.531619 labonneboite_datamodel-1.0.4/labonneboite_datamodel/tests/test_job.py
--rw-r--r--   0        0        0     5276 2023-04-06 10:24:17.812541 labonneboite_datamodel-1.0.4/labonneboite_datamodel/tests/test_office.py
--rw-r--r--   0        0        0     1205 2023-04-06 10:26:06.239782 labonneboite_datamodel-1.0.4/pyproject.toml
--rw-r--r--   0        0        0      498 1970-01-01 00:00:00.000000 labonneboite_datamodel-1.0.4/PKG-INFO
+-rw-r--r--   0        0        0      224 2023-04-04 13:45:03.269004 labonneboite_datamodel-1.0.5/labonneboite_datamodel/__init__.py
+-rw-r--r--   0        0        0      697 2023-04-05 09:46:10.763862 labonneboite_datamodel-1.0.5/labonneboite_datamodel/crud.py
+-rw-r--r--   0        0        0     2185 2023-04-05 09:46:10.763862 labonneboite_datamodel-1.0.5/labonneboite_datamodel/job.py
+-rw-r--r--   0        0        0     7672 2023-04-06 11:40:38.459864 labonneboite_datamodel-1.0.5/labonneboite_datamodel/office.py
+-rw-r--r--   0        0        0        0 2023-04-04 13:25:50.527619 labonneboite_datamodel-1.0.5/labonneboite_datamodel/tests/__init__.py
+-rw-r--r--   0        0        0     3589 2023-04-06 09:31:09.039521 labonneboite_datamodel-1.0.5/labonneboite_datamodel/tests/data/test.csv
+-rw-r--r--   0        0        0     1026 2023-04-04 13:25:50.531619 labonneboite_datamodel-1.0.5/labonneboite_datamodel/tests/test_job.py
+-rw-r--r--   0        0        0     5612 2023-04-06 11:40:38.459864 labonneboite_datamodel-1.0.5/labonneboite_datamodel/tests/test_office.py
+-rw-r--r--   0        0        0     1205 2023-04-06 11:43:57.658443 labonneboite_datamodel-1.0.5/pyproject.toml
+-rw-r--r--   0        0        0      498 1970-01-01 00:00:00.000000 labonneboite_datamodel-1.0.5/PKG-INFO
```

### Comparing `labonneboite_datamodel-1.0.4/labonneboite_datamodel/crud.py` & `labonneboite_datamodel-1.0.5/labonneboite_datamodel/crud.py`

 * *Files identical despite different names*

### Comparing `labonneboite_datamodel-1.0.4/labonneboite_datamodel/job.py` & `labonneboite_datamodel-1.0.5/labonneboite_datamodel/job.py`

 * *Files identical despite different names*

### Comparing `labonneboite_datamodel-1.0.4/labonneboite_datamodel/office.py` & `labonneboite_datamodel-1.0.5/labonneboite_datamodel/office.py`

 * *Files 2% similar despite different names*

```diff
@@ -219,14 +219,17 @@
             - a postcode should be made up of numbers
             - a postcode cannot be 00000
 
         Raises:
             ValueError:
 
         """
+        if not v:
+            return ""
+
         if len(v) < 5:
             raise ValueError(
                 "a postcode should be made up of at least 5 numbers")
 
         if not v.isdigit():
             raise ValueError(
                 "a postcode should be made up of numbers")
@@ -244,14 +247,17 @@
             - should be made up of at least 5 numbers
             - a citycode cannot be 00000
 
         Raises:
             ValueError:
 
         """
+        if not v:
+            return ""
+
         if len(v) < 5:
             raise ValueError(
                 "a citycode should be made up of 4 numbers and a letter")
 
         if v == "0".zfill(5):
             raise ValueError(
                 "a citycode cannot be 00000")
```

### Comparing `labonneboite_datamodel-1.0.4/labonneboite_datamodel/tests/data/test.csv` & `labonneboite_datamodel-1.0.5/labonneboite_datamodel/tests/data/test.csv`

 * *Files identical despite different names*

### Comparing `labonneboite_datamodel-1.0.4/labonneboite_datamodel/tests/test_job.py` & `labonneboite_datamodel-1.0.5/labonneboite_datamodel/tests/test_job.py`

 * *Files identical despite different names*

### Comparing `labonneboite_datamodel-1.0.4/labonneboite_datamodel/tests/test_office.py` & `labonneboite_datamodel-1.0.5/labonneboite_datamodel/tests/test_office.py`

 * *Files 13% similar despite different names*

```diff
@@ -92,15 +92,21 @@
                 Office.validate(data)
 
     def test_postcode_valid(self) -> None:
         data = self._get_valid_office()
         data["postcode"] = "75014"
         self.assertTrue(Office.validate(data).postcode == "75014")
 
+        data["postcode"] = None
+        self.assertTrue(Office.validate(data).postcode == "")
+
+        data["postcode"] = ""
+        self.assertTrue(Office.validate(data).postcode == "")
     # citycode
+
     def test_citycode_invalid(self) -> None:
         data = self._get_valid_office()
 
         for value in ["1234", "00000"]:
 
             data["citycode"] = value
 
@@ -108,18 +114,23 @@
                 Office.validate(data)
 
     def test_citycode_valid(self) -> None:
         data = self._get_valid_office()
         data["citycode"] = "75014"
         self.assertTrue(Office.validate(data).citycode == "75014")
 
-        data = self._get_valid_office()
         data["citycode"] = "2B014"
         self.assertTrue(Office.validate(data).citycode == "2B014")
 
+        data["citycode"] = None
+        self.assertTrue(Office.validate(data).citycode == "")
+
+        data["citycode"] = ""
+        self.assertTrue(Office.validate(data).citycode == "")
+
     # problems due to pandas
     def test_pandas_null(self) -> None:
 
         with pd.read_csv("./labonneboite_datamodel/tests/data/test.csv", delimiter=";", chunksize=10, keep_default_na=False, on_bad_lines='warn') as reader:
             for chunk in reader:
 
                 chunk["siret"] = chunk["siret"].astype(str)
```

### Comparing `labonneboite_datamodel-1.0.4/pyproject.toml` & `labonneboite_datamodel-1.0.5/pyproject.toml`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "labonneboite-datamodel"
-version = "1.0.4"
+version = "1.0.5"
 description = "Datamodel for labonneboite"
 authors = ["Sylvain Touret"]
 license = "MIT"
 packages = [{include = "labonneboite_datamodel"}]
 
 [tool.poetry.dependencies]
 python = "^3.10"
```

